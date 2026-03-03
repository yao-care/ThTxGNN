/**
 * ThTxGNN SMART App Main Logic
 *
 * Handles FHIR client initialization, medication retrieval,
 * and UI rendering for drug repurposing candidates.
 */
(function(global) {
  'use strict';

  const CONFIG = {
    searchIndexUrl: '/data/search-index.json',
    drugsBaseUrl: '/drugs/',
    clinicalTrialsApiUrl: 'https://clinicaltrials.gov/api/v2/studies'
  };

  // Clinical trials cache to avoid repeated API calls
  const clinicalTrialsCache = new Map();

  // UI Elements
  let elements = {};

  // State
  let fhirClient = null;
  let drugMapper = null;
  let searchIndex = null;
  let patientMedications = [];
  let mappingResults = [];

  /**
   * Initialize the SMART App
   */
  async function init() {
    elements = {
      loading: document.getElementById('loading'),
      error: document.getElementById('error'),
      content: document.getElementById('content'),
      patientInfo: document.getElementById('patient-info'),
      medList: document.getElementById('medication-list'),
      results: document.getElementById('repurposing-results'),
      queryBtn: document.getElementById('query-btn'),
      selectAllBtn: document.getElementById('select-all-btn')
    };

    try {
      showLoading('กำลังโหลดฐานข้อมูลยา...');

      // Load search index
      searchIndex = await loadSearchIndex();

      showLoading('กำลังเชื่อมต่อกับระบบ EHR...');

      // Initialize FHIR client
      fhirClient = await FHIR.oauth2.ready();

      // Initialize drug mapper
      drugMapper = new ThTxGNN.DrugMapper(searchIndex);

      showLoading('กำลังอ่านข้อมูลยาของผู้ป่วย...');

      // Load patient info and medications
      await loadPatientData();

      // Show main content
      showContent();

      // Setup event listeners
      setupEventListeners();

    } catch (error) {
      console.error('SMART App initialization error:', error);
      showError('ไม่สามารถเริ่มต้นแอปพลิเคชันได้: ' + (error.message || error));
    }
  }

  /**
   * Load ThTxGNN search index
   */
  async function loadSearchIndex() {
    const response = await fetch(CONFIG.searchIndexUrl);
    if (!response.ok) {
      throw new Error('ไม่สามารถโหลดฐานข้อมูลยาได้');
    }
    return response.json();
  }

  /**
   * Load patient information and medications
   */
  async function loadPatientData() {
    // Get patient info
    const patient = await fhirClient.patient.read();
    renderPatientInfo(patient);

    // Get medications (try MedicationRequest first, then MedicationStatement)
    let medications = [];

    try {
      const medRequests = await fhirClient.request(
        `MedicationRequest?patient=${fhirClient.patient.id}&status=active,completed`,
        { flat: true }
      );
      if (Array.isArray(medRequests)) {
        medications = medications.concat(medRequests);
      }
    } catch (e) {
      console.warn('Could not fetch MedicationRequest:', e);
    }

    try {
      const medStatements = await fhirClient.request(
        `MedicationStatement?patient=${fhirClient.patient.id}&status=active,completed`,
        { flat: true }
      );
      if (Array.isArray(medStatements)) {
        medications = medications.concat(medStatements);
      }
    } catch (e) {
      console.warn('Could not fetch MedicationStatement:', e);
    }

    patientMedications = medications;

    // Map medications to ThTxGNN
    mappingResults = await drugMapper.mapMedications(medications);

    // Render medication list
    renderMedicationList();
  }

  /**
   * Render patient information
   */
  function renderPatientInfo(patient) {
    if (!elements.patientInfo) return;

    const name = patient.name?.[0];
    const displayName = name ?
      `${name.family || ''}, ${name.given?.join(' ') || ''}`.trim() :
      'ไม่ทราบ';

    const birthDate = patient.birthDate || 'ไม่ทราบ';
    const gender = {
      'male': 'ชาย',
      'female': 'หญิง',
      'other': 'อื่นๆ',
      'unknown': 'ไม่ทราบ'
    }[patient.gender] || patient.gender || 'ไม่ทราบ';

    elements.patientInfo.innerHTML = `
      <div class="patient-card">
        <div class="patient-name">${escapeHtml(displayName)}</div>
        <div class="patient-details">
          <span>วันเกิด: ${escapeHtml(birthDate)}</span>
          <span>เพศ: ${escapeHtml(gender)}</span>
        </div>
      </div>
    `;
  }

  /**
   * Render medication list with checkboxes
   */
  function renderMedicationList() {
    if (!elements.medList) return;

    if (mappingResults.length === 0) {
      elements.medList.innerHTML = `
        <div class="empty-state">
          <p>ไม่พบบันทึกการใช้ยาของผู้ป่วย</p>
        </div>
      `;
      return;
    }

    let html = '<div class="med-list">';

    mappingResults.forEach((result, index) => {
      const displayName = result.displayName || result.ingredientName || 'ยาไม่ทราบชื่อ';
      const matchStatus = result.matched ?
        `<span class="match-badge matched">มีข้อมูลการทำนาย</span>` :
        `<span class="match-badge unmatched">ไม่มีข้อมูลการทำนาย</span>`;

      const twtxgnnInfo = result.twtxgnnMatch ?
        `<span class="twtxgnn-name">→ ${escapeHtml(result.twtxgnnMatch.name)}</span>
         <span class="level-badge level-${result.twtxgnnMatch.level}">${result.twtxgnnMatch.level}</span>` :
        '';

      html += `
        <div class="med-item ${result.matched ? 'has-match' : 'no-match'}">
          <label class="med-label">
            <input type="checkbox" class="med-checkbox" data-index="${index}"
                   ${result.matched ? 'checked' : 'disabled'}>
            <span class="med-name">${escapeHtml(displayName)}</span>
            ${matchStatus}
          </label>
          <div class="med-mapping">
            ${twtxgnnInfo}
          </div>
        </div>
      `;
    });

    html += '</div>';
    elements.medList.innerHTML = html;
  }

  /**
   * Query repurposing candidates for selected medications
   */
  function queryRepurposingCandidates() {
    const checkboxes = document.querySelectorAll('.med-checkbox:checked');
    const selectedIndices = Array.from(checkboxes).map(cb => parseInt(cb.dataset.index));

    if (selectedIndices.length === 0) {
      elements.results.innerHTML = `
        <div class="empty-state">
          <p>กรุณาเลือกยาอย่างน้อย 1 รายการ</p>
        </div>
      `;
      return;
    }

    let html = '';

    selectedIndices.forEach(index => {
      const result = mappingResults[index];
      if (!result.twtxgnnMatch) return;

      const drug = result.twtxgnnMatch;
      const indications = drug.indications || [];

      html += `
        <div class="drug-result-card">
          <div class="drug-header">
            <h3>
              <a href="${CONFIG.drugsBaseUrl}${drug.slug}/" target="_blank">
                ${escapeHtml(drug.name)}
              </a>
              <span class="level-badge level-${drug.level}">${drug.level}</span>
            </h3>
            <a href="${CONFIG.drugsBaseUrl}${drug.slug}/" target="_blank" class="view-full">
              ดูรายงานฉบับเต็ม →
            </a>
          </div>

          <div class="drug-original">
            <strong>ข้อบ่งใช้เดิม:</strong>
            ${escapeHtml(drug.original) || '—'}
          </div>

          <div class="drug-indications">
            <strong>ข้อบ่งใช้ใหม่ที่ทำนาย (ตัวเลือกการนำยาเก่ามาใช้ใหม่):</strong>
            <div class="indication-list">
      `;

      if (indications.length > 0) {
        indications.slice(0, 10).forEach((ind, indIndex) => {
          const trialsContainerId = `trials-${drug.slug}-${indIndex}`;
          html += `
            <div class="indication-item">
              <div class="indication-header">
                <span class="level-badge level-${ind.level}">${ind.level}</span>
                <span class="ind-name">${escapeHtml(ind.name)}</span>
                <span class="ind-score">${ind.score}%</span>
                <button class="trials-btn" onclick="ThTxGNN.SmartApp.loadTrials('${escapeHtml(drug.name)}', '${escapeHtml(ind.name)}', '${trialsContainerId}')">
                  🔬 การทดลองทางคลินิก
                </button>
              </div>
              <div class="trials-container" id="${trialsContainerId}"></div>
            </div>
          `;
        });

        if (indications.length > 10) {
          html += `
            <div class="more-indications">
              ...และอีก ${indications.length - 10} ข้อบ่งใช้ที่ทำนาย
              <a href="${CONFIG.drugsBaseUrl}${drug.slug}/" target="_blank">ดูทั้งหมด</a>
            </div>
          `;
        }
      } else {
        html += '<p class="no-indications">ไม่มีข้อบ่งใช้ใหม่ที่ทำนาย</p>';
      }

      html += `
            </div>
          </div>
        </div>
      `;
    });

    if (!html) {
      html = `
        <div class="empty-state">
          <p>ยาที่เลือกไม่มีข้อมูลการทำนาย</p>
        </div>
      `;
    }

    elements.results.innerHTML = html;
  }

  /**
   * Setup event listeners
   */
  function setupEventListeners() {
    if (elements.queryBtn) {
      elements.queryBtn.addEventListener('click', queryRepurposingCandidates);
    }

    if (elements.selectAllBtn) {
      elements.selectAllBtn.addEventListener('click', function() {
        const checkboxes = document.querySelectorAll('.med-checkbox:not(:disabled)');
        const allChecked = Array.from(checkboxes).every(cb => cb.checked);

        checkboxes.forEach(cb => {
          cb.checked = !allChecked;
        });
      });
    }
  }

  // UI Helper functions
  function showLoading(message) {
    if (elements.loading) {
      elements.loading.style.display = 'flex';
      elements.loading.querySelector('.loading-text').textContent = message || 'กำลังโหลด...';
    }
    if (elements.error) elements.error.style.display = 'none';
    if (elements.content) elements.content.style.display = 'none';
  }

  function showError(message) {
    if (elements.loading) elements.loading.style.display = 'none';
    if (elements.error) {
      elements.error.style.display = 'block';
      elements.error.querySelector('.error-message').textContent = message;
    }
    if (elements.content) elements.content.style.display = 'none';
  }

  function showContent() {
    if (elements.loading) elements.loading.style.display = 'none';
    if (elements.error) elements.error.style.display = 'none';
    if (elements.content) elements.content.style.display = 'block';
  }

  function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  /**
   * Search ClinicalTrials.gov for drug + condition trials
   * @param {string} drugName - Drug name
   * @param {string} condition - Disease/condition name
   * @returns {Promise<Object>} Trial results with count and trials array
   */
  async function searchClinicalTrials(drugName, condition) {
    const cacheKey = `${drugName.toLowerCase()}|${condition.toLowerCase()}`;

    // Return cached result if available
    if (clinicalTrialsCache.has(cacheKey)) {
      return clinicalTrialsCache.get(cacheKey);
    }

    try {
      const params = new URLSearchParams({
        'query.intr': drugName,
        'query.cond': condition,
        'pageSize': '5',
        'format': 'json',
        'countTotal': 'true'
      });

      const response = await fetch(`${CONFIG.clinicalTrialsApiUrl}?${params}`);

      if (!response.ok) {
        console.warn('ClinicalTrials.gov API error:', response.status);
        return { totalCount: 0, trials: [] };
      }

      const data = await response.json();

      const result = {
        totalCount: data.totalCount || 0,
        trials: (data.studies || []).slice(0, 5).map(study => ({
          nctId: study.protocolSection?.identificationModule?.nctId,
          title: study.protocolSection?.identificationModule?.briefTitle,
          status: study.protocolSection?.statusModule?.overallStatus,
          phase: study.protocolSection?.designModule?.phases?.join(', ') || 'N/A',
          enrollment: study.protocolSection?.designModule?.enrollmentInfo?.count,
          url: `https://clinicaltrials.gov/study/${study.protocolSection?.identificationModule?.nctId}`
        }))
      };

      // Cache the result
      clinicalTrialsCache.set(cacheKey, result);

      return result;
    } catch (error) {
      console.warn('Failed to fetch clinical trials:', error);
      return { totalCount: 0, trials: [] };
    }
  }

  /**
   * Render clinical trials section for an indication
   * @param {string} drugName - Drug name
   * @param {string} indicationName - Indication name
   * @param {string} containerId - Container element ID
   */
  async function loadClinicalTrials(drugName, indicationName, containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    container.innerHTML = '<span class="trials-loading">กำลังค้นหาการทดลองทางคลินิก...</span>';

    const result = await searchClinicalTrials(drugName, indicationName);

    if (result.totalCount === 0) {
      container.innerHTML = '<span class="trials-none">ไม่มีการทดลองทางคลินิกที่เกี่ยวข้อง</span>';
      return;
    }

    let html = `
      <div class="trials-summary">
        พบ <strong>${result.totalCount}</strong> การทดลองทางคลินิกที่เกี่ยวข้อง
      </div>
      <div class="trials-list">
    `;

    result.trials.forEach(trial => {
      const statusClass = getTrialStatusClass(trial.status);
      html += `
        <div class="trial-item">
          <a href="${trial.url}" target="_blank" class="trial-nct">${trial.nctId}</a>
          <span class="trial-status ${statusClass}">${formatTrialStatus(trial.status)}</span>
          <span class="trial-phase">${trial.phase}</span>
          <div class="trial-title">${escapeHtml(trial.title)}</div>
        </div>
      `;
    });

    if (result.totalCount > 5) {
      const searchUrl = `https://clinicaltrials.gov/search?cond=${encodeURIComponent(indicationName)}&intr=${encodeURIComponent(drugName)}`;
      html += `
        <a href="${searchUrl}" target="_blank" class="trials-more">
          ดูการทดลองทางคลินิกทั้งหมด ${result.totalCount} รายการ →
        </a>
      `;
    }

    html += '</div>';
    container.innerHTML = html;
  }

  /**
   * Get CSS class for trial status
   */
  function getTrialStatusClass(status) {
    const statusMap = {
      'RECRUITING': 'status-recruiting',
      'ACTIVE_NOT_RECRUITING': 'status-active',
      'COMPLETED': 'status-completed',
      'TERMINATED': 'status-terminated',
      'NOT_YET_RECRUITING': 'status-pending'
    };
    return statusMap[status] || 'status-unknown';
  }

  /**
   * Format trial status for display
   */
  function formatTrialStatus(status) {
    const statusMap = {
      'RECRUITING': 'กำลังรับสมัคร',
      'ACTIVE_NOT_RECRUITING': 'ดำเนินการอยู่',
      'COMPLETED': 'เสร็จสิ้น',
      'TERMINATED': 'ยุติ',
      'NOT_YET_RECRUITING': 'ยังไม่รับสมัคร',
      'SUSPENDED': 'ระงับชั่วคราว',
      'WITHDRAWN': 'ถอน',
      'ENROLLING_BY_INVITATION': 'รับสมัครโดยคำเชิญ'
    };
    return statusMap[status] || status;
  }

  // Export
  global.ThTxGNN = global.ThTxGNN || {};
  global.ThTxGNN.SmartApp = {
    init: init,
    loadTrials: loadClinicalTrials,
    searchTrials: searchClinicalTrials
  };

  // Auto-initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})(typeof window !== 'undefined' ? window : this);
