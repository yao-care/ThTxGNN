/**
 * ThTxGNN Drug-Drug Interaction Checker
 *
 * Client-side DDI checking based on DDInter 2.0 database.
 * Provides real-time interaction alerts for drug repurposing candidates.
 *
 * @author ThTxGNN Team
 * @version 1.0.0
 */
(function(global) {
  'use strict';

  const CONFIG = {
    ddiDataUrl: '/data/ddi-index.json',
    maxAlerts: 10
  };

  // Severity levels with priority (higher = more severe)
  const SEVERITY = {
    'Major': { priority: 3, class: 'ddi-major', label: 'รุนแรง' },
    'Moderate': { priority: 2, class: 'ddi-moderate', label: 'ปานกลาง' },
    'Minor': { priority: 1, class: 'ddi-minor', label: 'เล็กน้อย' }
  };

  // High-priority DDI rules (curated from DDInter 2.0)
  // Format: { drug1: [synonym list], drug2: [synonym list], severity, summary, detail }
  const CURATED_DDI_RULES = [
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['ibuprofen', 'advil', 'motrin', 'brufen']
      ],
      severity: 'Major',
      summary: 'Warfarin + Ibuprofen: เพิ่มความเสี่ยงเลือดออก',
      detail: 'NSAIDs ยับยั้งการทำงานของเกล็ดเลือดและอาจเพิ่มผลการต้านการแข็งตัวของเลือดของ Warfarin เพิ่มความเสี่ยงเลือดออกในทางเดินอาหารอย่างมีนัยสำคัญ',
      recommendation: 'แนะนำใช้ Acetaminophen แทน หรือเพิ่ม PPI เพื่อปกป้องกระเพาะ'
    },
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['aspirin', 'acetylsalicylic acid']
      ],
      severity: 'Major',
      summary: 'Warfarin + Aspirin: เพิ่มความเสี่ยงเลือดออก',
      detail: 'ทั้งสองตัวส่งผลต่อการแข็งตัวของเลือด การใช้ร่วมกันเพิ่มความเสี่ยงเลือดออกอย่างมาก',
      recommendation: 'หากต้องใช้ร่วมกัน ควรใช้ Aspirin ขนาดต่ำและติดตาม INR อย่างใกล้ชิด'
    },
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['naproxen', 'aleve', 'naprosyn']
      ],
      severity: 'Major',
      summary: 'Warfarin + Naproxen: เพิ่มความเสี่ยงเลือดออก',
      detail: 'Naproxen ใช้ร่วมกับ Warfarin จะเพิ่มความเสี่ยงเลือดออกในทางเดินอาหารและเหตุการณ์เลือดออกอื่นๆ',
      recommendation: 'แนะนำใช้ Acetaminophen แทนเพื่อบรรเทาปวด'
    },
    {
      drugs: [
        ['metformin', 'glucophage'],
        ['iodixanol', 'visipaque', 'iopamidol', 'isovue', 'contrast']
      ],
      severity: 'Major',
      summary: 'Metformin + สารทึบรังสีไอโอดีน: ความเสี่ยงกรดแลคติกคั่ง',
      detail: 'สารทึบรังสีอาจทำให้ไตบาดเจ็บเฉียบพลัน ทำให้ Metformin สะสมและเกิดภาวะกรดแลคติกคั่ง',
      recommendation: 'หยุด Metformin 48 ชั่วโมงก่อนตรวจ และเริ่มใหม่หลังยืนยันว่าไตทำงานปกติ'
    },
    {
      drugs: [
        ['colchicine', 'colcrys'],
        ['clarithromycin', 'biaxin', 'klacid']
      ],
      severity: 'Major',
      summary: 'Colchicine + Clarithromycin: ความเสี่ยงเป็นพิษ',
      detail: 'Clarithromycin เป็นตัวยับยั้ง CYP3A4 ที่แรง จะเพิ่มระดับ Colchicine ในเลือดอย่างมาก',
      recommendation: 'หลีกเลี่ยงการใช้ร่วมกัน หรือลดขนาด Colchicine อย่างมีนัยสำคัญ'
    },
    {
      drugs: [
        ['colchicine', 'colcrys'],
        ['ritonavir', 'norvir', 'cobicistat', 'tybost']
      ],
      severity: 'Major',
      summary: 'Colchicine + HIV Protease Inhibitor: ความเสี่ยงเป็นพิษรุนแรง',
      detail: 'HIV Protease Inhibitor จะเพิ่มระดับ Colchicine อย่างมาก อาจทำให้เกิดความเป็นพิษถึงชีวิต',
      recommendation: 'ห้ามใช้ร่วมกันในผู้ป่วยไตวาย/ตับวาย'
    },
    {
      drugs: [
        ['simvastatin', 'zocor'],
        ['amiodarone', 'cordarone']
      ],
      severity: 'Major',
      summary: 'Simvastatin + Amiodarone: ความเสี่ยงโรคกล้ามเนื้อ',
      detail: 'Amiodarone จะเพิ่มระดับ Simvastatin เพิ่มความเสี่ยงภาวะกล้ามเนื้อสลาย',
      recommendation: 'ขนาด Simvastatin ไม่ควรเกิน 20mg/วัน หรือเปลี่ยนไปใช้ Statin ตัวอื่น'
    },
    {
      drugs: [
        ['fluoxetine', 'prozac', 'sertraline', 'zoloft', 'paroxetine', 'paxil'],
        ['tramadol', 'ultram']
      ],
      severity: 'Major',
      summary: 'SSRI + Tramadol: ความเสี่ยงกลุ่มอาการเซโรโทนิน',
      detail: 'ทั้งสองตัวเพิ่มฤทธิ์ของเซโรโทนิน การใช้ร่วมกันอาจทำให้เกิดกลุ่มอาการเซโรโทนินที่เป็นอันตรายถึงชีวิต',
      recommendation: 'ติดตามอาการอย่างใกล้ชิด (ไข้สูง, กล้ามเนื้อกระตุก, สติเปลี่ยนแปลง) พิจารณาใช้ยาแก้ปวดอื่นแทน'
    },
    {
      drugs: [
        ['fluoxetine', 'prozac', 'sertraline', 'zoloft', 'paroxetine', 'paxil'],
        ['linezolid', 'zyvox']
      ],
      severity: 'Major',
      summary: 'SSRI + Linezolid: ความเสี่ยงกลุ่มอาการเซโรโทนิน',
      detail: 'Linezolid เป็น MAO Inhibitor การใช้ร่วมกับ SSRI มีอันตรายสูง',
      recommendation: 'หลีกเลี่ยงการใช้ร่วมกัน หากต้องใช้ Linezolid ควรหยุด SSRI และรอเวลาขจัดยาที่เหมาะสม'
    },
    {
      drugs: [
        ['amiodarone', 'cordarone'],
        ['moxifloxacin', 'avelox']
      ],
      severity: 'Major',
      summary: 'Amiodarone + Moxifloxacin: ความเสี่ยง QT ยาว',
      detail: 'ทั้งสองตัวสามารถยืดช่วง QT การใช้ร่วมกันเพิ่มความเสี่ยง Torsades de Pointes',
      recommendation: 'หลีกเลี่ยงการใช้ร่วมกัน หรือติดตามคลื่นไฟฟ้าหัวใจอย่างใกล้ชิด'
    },
    {
      drugs: [
        ['digoxin', 'lanoxin'],
        ['amiodarone', 'cordarone']
      ],
      severity: 'Major',
      summary: 'Digoxin + Amiodarone: ความเสี่ยงพิษ Digoxin',
      detail: 'Amiodarone จะเพิ่มระดับ Digoxin ในเลือดประมาณ 70%',
      recommendation: 'เมื่อเริ่ม Amiodarone ลดขนาด Digoxin ลงครึ่งหนึ่งและติดตามระดับในเลือด'
    },
    {
      drugs: [
        ['clopidogrel', 'plavix'],
        ['omeprazole', 'prilosec', 'esomeprazole', 'nexium']
      ],
      severity: 'Moderate',
      summary: 'Clopidogrel + PPI: ลดผลต้านเกล็ดเลือด',
      detail: 'Omeprazole ยับยั้ง CYP2C19 ลดการเปลี่ยน Clopidogrel เป็นเมตาบอไลต์ที่ออกฤทธิ์',
      recommendation: 'พิจารณาใช้ Pantoprazole หรือ H2 blocker แทน'
    },
    {
      drugs: [
        ['lithium', 'lithobid'],
        ['ibuprofen', 'advil', 'naproxen', 'aleve', 'diclofenac']
      ],
      severity: 'Major',
      summary: 'Lithium + NSAIDs: ความเสี่ยงพิษ Lithium',
      detail: 'NSAIDs ลดการขับ Lithium ทางไต ทำให้ระดับในเลือดสูงขึ้น',
      recommendation: 'หลีกเลี่ยงการใช้ร่วมกัน หรือติดตามระดับ Lithium อย่างใกล้ชิด'
    },
    {
      drugs: [
        ['potassium', 'k-dur', 'klor-con'],
        ['spironolactone', 'aldactone', 'eplerenone', 'inspra']
      ],
      severity: 'Major',
      summary: 'อาหารเสริมโพแทสเซียม + ยาขับปัสสาวะเก็บโพแทสเซียม: ความเสี่ยงโพแทสเซียมสูง',
      detail: 'ทั้งสองตัวเพิ่มโพแทสเซียมในเลือด การใช้ร่วมกันอาจทำให้เกิดภาวะโพแทสเซียมสูงเป็นอันตรายถึงชีวิต',
      recommendation: 'ติดตามระดับโพแทสเซียมเป็นประจำ หลีกเลี่ยงการเสริมโพแทสเซียมพร้อมกัน'
    },
    {
      drugs: [
        ['methotrexate', 'trexall'],
        ['trimethoprim', 'bactrim', 'septra', 'sulfamethoxazole']
      ],
      severity: 'Major',
      summary: 'Methotrexate + TMP-SMX: ความเสี่ยงกดไขกระดูก',
      detail: 'ทั้งสองตัวยับยั้งเมตาบอลิซึมของโฟเลต การใช้ร่วมกันเพิ่มความเสี่ยงกดไขกระดูกและเยื่อบุอักเสบ',
      recommendation: 'หลีกเลี่ยงการใช้ร่วมกัน หรือให้โฟเลตเสริมเพียงพอและติดตามเม็ดเลือดอย่างใกล้ชิด'
    }
  ];

  let ddiIndex = null;
  let isLoaded = false;

  /**
   * Load DDI index data
   */
  async function loadDDIIndex() {
    if (isLoaded) return;

    try {
      const response = await fetch(CONFIG.ddiDataUrl);
      if (response.ok) {
        ddiIndex = await response.json();
        isLoaded = true;
        console.log('DDI index loaded:', ddiIndex?.count || 0, 'interactions');
      }
    } catch (error) {
      console.warn('DDI index not available, using curated rules only');
      isLoaded = true;
    }
  }

  /**
   * Normalize drug name for comparison
   */
  function normalizeDrugName(name) {
    if (!name) return '';
    return name.toLowerCase()
      .replace(/\s+/g, ' ')
      .replace(/[^a-z0-9\s]/g, '')
      .trim();
  }

  /**
   * Check if a drug name matches any of the synonyms
   */
  function matchesDrug(drugName, synonyms) {
    const normalized = normalizeDrugName(drugName);
    return synonyms.some(syn => {
      const normalizedSyn = normalizeDrugName(syn);
      return normalized.includes(normalizedSyn) || normalizedSyn.includes(normalized);
    });
  }

  /**
   * Check for DDI between two drugs using curated rules
   */
  function checkCuratedDDI(drug1, drug2) {
    const alerts = [];

    for (const rule of CURATED_DDI_RULES) {
      const [drugGroup1, drugGroup2] = rule.drugs;

      // Check if drug1 matches group1 and drug2 matches group2, or vice versa
      if (
        (matchesDrug(drug1, drugGroup1) && matchesDrug(drug2, drugGroup2)) ||
        (matchesDrug(drug1, drugGroup2) && matchesDrug(drug2, drugGroup1))
      ) {
        alerts.push({
          drug1: drug1,
          drug2: drug2,
          severity: rule.severity,
          severityInfo: SEVERITY[rule.severity],
          summary: rule.summary,
          detail: rule.detail,
          recommendation: rule.recommendation,
          source: 'ThTxGNN DDI Rules (based on DDInter 2.0)'
        });
      }
    }

    return alerts;
  }

  /**
   * Check DDI for a list of medications
   * @param {string[]} medications - Array of medication names
   * @returns {Object[]} Array of DDI alerts
   */
  function checkInteractions(medications) {
    if (!medications || medications.length < 2) {
      return [];
    }

    const allAlerts = [];
    const seen = new Set();

    // Check all pairs
    for (let i = 0; i < medications.length; i++) {
      for (let j = i + 1; j < medications.length; j++) {
        const drug1 = medications[i];
        const drug2 = medications[j];
        const pairKey = [drug1, drug2].sort().join('|');

        if (seen.has(pairKey)) continue;
        seen.add(pairKey);

        const alerts = checkCuratedDDI(drug1, drug2);
        allAlerts.push(...alerts);
      }
    }

    // Sort by severity (highest first) and limit
    return allAlerts
      .sort((a, b) => b.severityInfo.priority - a.severityInfo.priority)
      .slice(0, CONFIG.maxAlerts);
  }

  /**
   * Check if a new drug has interactions with existing medications
   * @param {string} newDrug - The new drug to check
   * @param {string[]} currentMeds - Array of current medication names
   * @returns {Object[]} Array of DDI alerts
   */
  function checkNewDrug(newDrug, currentMeds) {
    if (!newDrug || !currentMeds || currentMeds.length === 0) {
      return [];
    }

    const allAlerts = [];

    for (const currentDrug of currentMeds) {
      const alerts = checkCuratedDDI(newDrug, currentDrug);
      allAlerts.push(...alerts);
    }

    return allAlerts
      .sort((a, b) => b.severityInfo.priority - a.severityInfo.priority);
  }

  /**
   * Format alerts as HTML for display
   */
  function formatAlertsHTML(alerts) {
    if (!alerts || alerts.length === 0) {
      return '<div class="ddi-no-alerts">ไม่พบการเตือนปฏิสัมพันธ์ระหว่างยา</div>';
    }

    let html = '<div class="ddi-alerts">';

    alerts.forEach((alert, index) => {
      html += `
        <div class="ddi-alert ${alert.severityInfo.class}">
          <div class="ddi-alert-header">
            <span class="ddi-severity-badge">${alert.severityInfo.label}</span>
            <span class="ddi-summary">${escapeHtml(alert.summary)}</span>
          </div>
          <div class="ddi-alert-body">
            <p class="ddi-detail">${escapeHtml(alert.detail)}</p>
            <p class="ddi-recommendation"><strong>คำแนะนำ:</strong>${escapeHtml(alert.recommendation)}</p>
          </div>
          <div class="ddi-alert-footer">
            <span class="ddi-source">แหล่งที่มา: ${escapeHtml(alert.source)}</span>
          </div>
        </div>
      `;
    });

    html += '</div>';
    return html;
  }

  /**
   * Format alerts for CDS Hooks response
   */
  function formatForCDSHooks(alerts) {
    return alerts.map((alert, index) => ({
      uuid: `ddi-alert-${index}`,
      summary: alert.summary,
      indicator: alert.severity === 'Major' ? 'critical' : alert.severity === 'Moderate' ? 'warning' : 'info',
      detail: `${alert.detail}\n\nคำแนะนำ: ${alert.recommendation}`,
      source: {
        label: 'ThTxGNN DDI Checker',
        url: 'https://twtxgnn.yao.care/'
      }
    }));
  }

  function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Export
  global.ThTxGNN = global.ThTxGNN || {};
  global.ThTxGNN.DDIChecker = {
    load: loadDDIIndex,
    checkInteractions: checkInteractions,
    checkNewDrug: checkNewDrug,
    formatAlertsHTML: formatAlertsHTML,
    formatForCDSHooks: formatForCDSHooks,
    SEVERITY: SEVERITY
  };

  // Auto-load when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadDDIIndex);
  } else {
    loadDDIIndex();
  }

})(typeof window !== 'undefined' ? window : this);
