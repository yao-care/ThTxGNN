/**
 * ThTxGNN PDDI-CDS (Potential Drug-Drug Interaction Clinical Decision Support)
 *
 * Implements HL7 PDDI-CDS Implementation Guide patterns for
 * contextualized drug-drug interaction alerts.
 *
 * Reference: https://github.com/HL7/PDDI-CDS
 *
 * @author ThTxGNN Team
 * @version 1.0.0
 */
(function(global) {
  'use strict';

  /**
   * PDDI Severity Levels per HL7 PDDI-CDS IG
   */
  const PDDI_INDICATOR = {
    CRITICAL: 'critical',   // Immediate attention required
    WARNING: 'warning',     // Attention needed
    INFO: 'info'           // Informational
  };

  /**
   * PDDI Alert Types
   */
  const ALERT_TYPE = {
    CONTRAINDICATED: 'contraindicated',
    CONDITIONAL: 'conditional',
    RELATIVE: 'relative'
  };

  /**
   * PDDI Knowledge Base - High-priority interactions with contextual factors
   * Based on DDI-CDS.org research and DDInter 2.0
   */
  const PDDI_KNOWLEDGE_BASE = [
    // Warfarin-NSAID (DDInteract pattern)
    {
      id: 'warfarin-nsaid',
      drugs: {
        object: ['warfarin', 'coumadin'],
        precipitant: ['ibuprofen', 'naproxen', 'aspirin', 'diclofenac', 'celecoxib', 'meloxicam']
      },
      alertType: ALERT_TYPE.CONDITIONAL,
      indicator: PDDI_INDICATOR.WARNING,
      clinicalConsequence: 'เพิ่มความเสี่ยงเลือดออกในทางเดินอาหารและเลือดออกทั่วร่างกาย',
      frequency: 'พบบ่อย (ประมาณ 10-15% ของผู้ใช้มีเลือดออกที่มีนัยสำคัญทางคลินิก)',
      mechanism: 'NSAIDs ยับยั้งการทำงานของเกล็ดเลือดและอาจเพิ่มผลการต้านการแข็งตัวของเลือดของ Warfarin',
      contextualFactors: [
        {
          factor: 'ประวัติเลือดออกในทางเดินอาหาร',
          impact: 'ความเสี่ยงเพิ่มขึ้นอย่างมีนัยสำคัญ',
          recommendation: 'แนะนำอย่างยิ่งให้หลีกเลี่ยงการใช้ร่วมกัน'
        },
        {
          factor: 'อายุ > 65 ปี',
          impact: 'ความเสี่ยงเพิ่มขึ้น',
          recommendation: 'หากต้องใช้ ให้เพิ่ม PPI เพื่อปกป้อง'
        },
        {
          factor: 'ใช้ PPI/H2 blocker',
          impact: 'ความเสี่ยงลดลง',
          recommendation: 'อาจพิจารณาใช้ระยะสั้น'
        },
        {
          factor: 'INR ควบคุมไม่คงที่',
          impact: 'ความเสี่ยงเพิ่มขึ้น',
          recommendation: 'หลีกเลี่ยงการใช้ร่วมกัน'
        }
      ],
      managementOptions: [
        {
          option: 'ใช้ Acetaminophen แทน',
          description: 'สำหรับการจัดการความปวด Acetaminophen เป็นทางเลือกที่ปลอดภัยกว่า',
          recommended: true
        },
        {
          option: 'เพิ่ม PPI',
          description: 'หากต้องใช้ NSAID ให้เพิ่ม PPI (เช่น Omeprazole) เพื่อลดความเสี่ยงเลือดออกในทางเดินอาหาร',
          recommended: true
        },
        {
          option: 'เลือกใช้ COX-2 Inhibitor',
          description: 'Celecoxib มีความเสี่ยงต่อทางเดินอาหารค่อนข้างต่ำกว่า แต่ยังต้องระวัง',
          recommended: false
        },
        {
          option: 'ใช้ระยะสั้น + ติดตามอย่างใกล้ชิด',
          description: 'ใช้ขนาดต่ำสุดที่ได้ผล ระยะเวลาสั้นที่สุด และติดตามอาการเลือดออก',
          recommended: false
        }
      ],
      evidence: {
        level: 'High',
        sources: ['DDInteract RCT', 'AHRQ Evidence Review', 'DDInter 2.0']
      }
    },

    // Colchicine-CYP3A4 Inhibitor
    {
      id: 'colchicine-cyp3a4',
      drugs: {
        object: ['colchicine', 'colcrys'],
        precipitant: ['clarithromycin', 'erythromycin', 'ritonavir', 'cobicistat', 'itraconazole', 'ketoconazole']
      },
      alertType: ALERT_TYPE.CONTRAINDICATED,
      indicator: PDDI_INDICATOR.CRITICAL,
      clinicalConsequence: 'ความเป็นพิษรุนแรงของ Colchicine (กดไขกระดูก, โรคระบบประสาท, อวัยวะหลายส่วนล้มเหลว)',
      frequency: 'พบน้อยแต่อาจถึงชีวิต',
      mechanism: 'CYP3A4 Inhibitor เพิ่มระดับ Colchicine ในเลือดอย่างมาก (อาจถึง 2-4 เท่า)',
      contextualFactors: [
        {
          factor: 'ไตวาย',
          impact: 'ห้ามใช้ร่วมกัน',
          recommendation: 'ข้อห้ามเด็ดขาด'
        },
        {
          factor: 'ตับวาย',
          impact: 'ห้ามใช้ร่วมกัน',
          recommendation: 'ข้อห้ามเด็ดขาด'
        },
        {
          factor: 'ไตและตับทำงานปกติ',
          impact: 'ความเสี่ยงยังสูง',
          recommendation: 'ลดขนาด Colchicine อย่างมีนัยสำคัญหรือหลีกเลี่ยง'
        }
      ],
      managementOptions: [
        {
          option: 'หลีกเลี่ยงการใช้ร่วมกัน',
          description: 'เลือกใช้ยาปฏิชีวนะหรือยาต้านเชื้อราอื่นแทน',
          recommended: true
        },
        {
          option: 'ลดขนาด Colchicine',
          description: 'หากต้องใช้ร่วมกัน ลดขนาด Colchicine เป็น 0.3mg ต่อวันหรือต่ำกว่า',
          recommended: false
        },
        {
          option: 'หยุด Colchicine ชั่วคราว',
          description: 'หยุด Colchicine ระหว่างใช้ CYP3A4 Inhibitor ที่แรง',
          recommended: true
        }
      ],
      evidence: {
        level: 'High',
        sources: ['DDI-CDS.org Colchicine CDS', 'FDA Warning', 'DDInter 2.0']
      }
    },

    // Tizanidine-CYP1A2 Inhibitor
    {
      id: 'tizanidine-cyp1a2',
      drugs: {
        object: ['tizanidine', 'zanaflex'],
        precipitant: ['ciprofloxacin', 'fluvoxamine', 'zileuton']
      },
      alertType: ALERT_TYPE.CONTRAINDICATED,
      indicator: PDDI_INDICATOR.CRITICAL,
      clinicalConsequence: 'ความดันโลหิตต่ำรุนแรง, สงบประสาทเกินไป',
      frequency: 'เมื่อใช้ Ciprofloxacin AUC เพิ่มขึ้น 10 เท่า',
      mechanism: 'CYP1A2 Inhibitor เพิ่ม Bioavailability ของ Tizanidine อย่างมีนัยสำคัญ',
      contextualFactors: [
        {
          factor: 'ใช้ Ciprofloxacin',
          impact: 'ห้ามใช้ร่วมกัน',
          recommendation: 'เปลี่ยนไปใช้ยาปฏิชีวนะอื่น'
        },
        {
          factor: 'ใช้ Fluvoxamine',
          impact: 'ห้ามใช้ร่วมกัน',
          recommendation: 'เปลี่ยนไปใช้ SSRI อื่น'
        }
      ],
      managementOptions: [
        {
          option: 'หลีกเลี่ยงการใช้ร่วมกัน',
          description: 'เลือกยาอื่นที่ไม่ยับยั้ง CYP1A2',
          recommended: true
        },
        {
          option: 'ยาคลายกล้ามเนื้ออื่นแทน',
          description: 'ใช้ Baclofen หรือ Cyclobenzaprine แทน',
          recommended: true
        }
      ],
      evidence: {
        level: 'High',
        sources: ['DDI-CDS.org Tizanidine CDS', 'FDA Label', 'DDInter 2.0']
      }
    },

    // Digoxin-Amiodarone
    {
      id: 'digoxin-amiodarone',
      drugs: {
        object: ['digoxin', 'lanoxin'],
        precipitant: ['amiodarone', 'cordarone']
      },
      alertType: ALERT_TYPE.CONDITIONAL,
      indicator: PDDI_INDICATOR.WARNING,
      clinicalConsequence: 'พิษ Digoxin (หัวใจเต้นผิดจังหวะ, คลื่นไส้อาเจียน, การมองเห็นผิดปกติ)',
      frequency: 'ระดับ Digoxin เพิ่มขึ้นเฉลี่ย 70%',
      mechanism: 'Amiodarone ยับยั้งการขจัด Digoxin ทางไตและนอกไต',
      contextualFactors: [
        {
          factor: 'ไตวาย',
          impact: 'ความเสี่ยงเพิ่มขึ้น',
          recommendation: 'ลดขนาด Digoxin อย่างเข้มงวดมากขึ้น'
        },
        {
          factor: 'ความผิดปกติของเกลือแร่ (โพแทสเซียมต่ำ)',
          impact: 'ความเสี่ยงเพิ่มขึ้นอย่างมีนัยสำคัญ',
          recommendation: 'แก้ไขเกลือแร่และติดตามอย่างใกล้ชิด'
        }
      ],
      managementOptions: [
        {
          option: 'ลดขนาด Digoxin 50%',
          description: 'ลดขนาด Digoxin ลงครึ่งหนึ่งทันทีเมื่อเริ่ม Amiodarone',
          recommended: true
        },
        {
          option: 'ติดตามระดับ Digoxin',
          description: 'ตรวจระดับในเลือดเป็นประจำ เป้าหมาย 0.5-1.0 ng/mL',
          recommended: true
        },
        {
          option: 'ติดตามคลื่นไฟฟ้าหัวใจ',
          description: 'ระวังหัวใจเต้นช้าและหัวใจเต้นผิดจังหวะ',
          recommended: true
        }
      ],
      evidence: {
        level: 'High',
        sources: ['Clinical Pharmacokinetics Studies', 'DDInter 2.0']
      }
    },

    // QT Prolongation (multiple drugs)
    {
      id: 'qt-prolongation-combo',
      drugs: {
        object: ['amiodarone', 'sotalol', 'dofetilide', 'dronedarone'],
        precipitant: ['moxifloxacin', 'haloperidol', 'ziprasidone', 'ondansetron', 'methadone']
      },
      alertType: ALERT_TYPE.CONDITIONAL,
      indicator: PDDI_INDICATOR.CRITICAL,
      clinicalConsequence: 'Torsades de Pointes (Polymorphic Ventricular Tachycardia)',
      frequency: 'พบน้อยแต่อาจถึงชีวิต',
      mechanism: 'ผลรวมของยาหลายตัวที่ยืด QT',
      contextualFactors: [
        {
          factor: 'ความผิดปกติของเกลือแร่',
          impact: 'ความเสี่ยงเพิ่มขึ้นอย่างมีนัยสำคัญ',
          recommendation: 'แก้ไขโพแทสเซียมต่ำ แมกนีเซียมต่ำ'
        },
        {
          factor: 'QTc พื้นฐาน > 450ms',
          impact: 'ห้ามใช้ร่วมกัน',
          recommendation: 'หลีกเลี่ยงการเพิ่มยาที่ยืด QT'
        },
        {
          factor: 'เพศหญิง',
          impact: 'ความเสี่ยงเพิ่มขึ้น',
          recommendation: 'ติดตามอย่างระมัดระวังมากขึ้น'
        },
        {
          factor: 'ประวัติโรคหัวใจ',
          impact: 'ความเสี่ยงเพิ่มขึ้น',
          recommendation: 'พิจารณาใช้ยาอื่นแทน'
        }
      ],
      managementOptions: [
        {
          option: 'หลีกเลี่ยงการใช้ร่วมกัน',
          description: 'เลือกยาอื่นที่ไม่ยืด QT',
          recommended: true
        },
        {
          option: 'ติดตามคลื่นไฟฟ้าหัวใจ',
          description: 'หากต้องใช้ร่วมกัน ตรวจ QTc เป็นประจำ',
          recommended: true
        },
        {
          option: 'แก้ไขเกลือแร่',
          description: 'ให้แน่ใจว่าโพแทสเซียม > 4.0 mEq/L, แมกนีเซียม > 2.0 mg/dL',
          recommended: true
        }
      ],
      evidence: {
        level: 'High',
        sources: ['CredibleMeds QT Drug Lists', 'FDA Warnings', 'DDInter 2.0']
      }
    }
  ];

  /**
   * Find matching PDDI for given drugs
   */
  function findPDDI(drug1, drug2) {
    const d1 = drug1.toLowerCase();
    const d2 = drug2.toLowerCase();

    for (const pddi of PDDI_KNOWLEDGE_BASE) {
      const objectMatch = pddi.drugs.object.some(d => d1.includes(d) || d.includes(d1)) ||
                         pddi.drugs.object.some(d => d2.includes(d) || d.includes(d2));
      const precipitantMatch = pddi.drugs.precipitant.some(d => d1.includes(d) || d.includes(d1)) ||
                               pddi.drugs.precipitant.some(d => d2.includes(d) || d.includes(d2));

      if (objectMatch && precipitantMatch) {
        // Determine which is which
        const objectDrug = pddi.drugs.object.some(d => d1.includes(d) || d.includes(d1)) ? drug1 : drug2;
        const precipitantDrug = objectDrug === drug1 ? drug2 : drug1;

        return {
          ...pddi,
          objectDrug,
          precipitantDrug
        };
      }
    }

    return null;
  }

  /**
   * Check all drug pairs for PDDI
   */
  function checkPDDI(medications) {
    if (!medications || medications.length < 2) {
      return [];
    }

    const alerts = [];
    const seen = new Set();

    for (let i = 0; i < medications.length; i++) {
      for (let j = i + 1; j < medications.length; j++) {
        const pairKey = [medications[i], medications[j]].sort().join('|');
        if (seen.has(pairKey)) continue;
        seen.add(pairKey);

        const pddi = findPDDI(medications[i], medications[j]);
        if (pddi) {
          alerts.push(pddi);
        }
      }
    }

    // Sort by severity
    return alerts.sort((a, b) => {
      const priority = { critical: 3, warning: 2, info: 1 };
      return priority[b.indicator] - priority[a.indicator];
    });
  }

  /**
   * Generate CDS Hooks card for a PDDI alert
   * Following HL7 PDDI-CDS IG structure
   */
  function generateCDSHooksCard(pddi) {
    const card = {
      uuid: `pddi-${pddi.id}-${Date.now()}`,
      summary: `${pddi.objectDrug} + ${pddi.precipitantDrug}: ${pddi.clinicalConsequence}`,
      indicator: pddi.indicator,
      detail: generateDetailMarkdown(pddi),
      source: {
        label: 'ThTxGNN PDDI-CDS',
        url: 'https://thtxgnn.yao.care/smart/',
        icon: 'https://thtxgnn.yao.care/assets/img/icon-192.png'
      },
      suggestions: pddi.managementOptions
        .filter(opt => opt.recommended)
        .map((opt, idx) => ({
          label: opt.option,
          uuid: `suggestion-${pddi.id}-${idx}`,
          actions: []
        })),
      links: [
        {
          label: 'ดูข้อมูลทั้งหมด',
          url: `https://thtxgnn.yao.care/drugs/`,
          type: 'absolute'
        }
      ],
      overrideReasons: [
        { code: 'patient-aware', display: 'ผู้ป่วยทราบความเสี่ยงแล้ว' },
        { code: 'benefit-outweighs', display: 'ประโยชน์มากกว่าความเสี่ยง' },
        { code: 'alternative-unavailable', display: 'ไม่มีทางเลือกอื่น' },
        { code: 'monitoring-in-place', display: 'มีแผนติดตามแล้ว' }
      ]
    };

    return card;
  }

  /**
   * Generate detailed markdown for PDDI alert
   */
  function generateDetailMarkdown(pddi) {
    let md = `## การเตือนปฏิสัมพันธ์ระหว่างยา\n\n`;
    md += `**ประเภทปฏิสัมพันธ์**: ${getAlertTypeLabel(pddi.alertType)}\n\n`;
    md += `**กลไก**: ${pddi.mechanism}\n\n`;
    md += `**ผลทางคลินิก**: ${pddi.clinicalConsequence}\n\n`;
    md += `**ความถี่ที่เกิด**: ${pddi.frequency}\n\n`;

    md += `### ปัจจัยบริบท\n\n`;
    pddi.contextualFactors.forEach(cf => {
      md += `- **${cf.factor}**: ${cf.impact} - ${cf.recommendation}\n`;
    });

    md += `\n### ตัวเลือกการจัดการ\n\n`;
    pddi.managementOptions.forEach(opt => {
      const marker = opt.recommended ? '✓' : '○';
      md += `- ${marker} **${opt.option}**: ${opt.description}\n`;
    });

    md += `\n### ระดับหลักฐาน\n\n`;
    md += `ระดับ: ${pddi.evidence.level}\n`;
    md += `แหล่งที่มา: ${pddi.evidence.sources.join(', ')}\n`;

    return md;
  }

  /**
   * Get human-readable alert type label
   */
  function getAlertTypeLabel(type) {
    const labels = {
      contraindicated: 'ห้ามใช้ร่วมกัน',
      conditional: 'เตือนตามเงื่อนไข',
      relative: 'ข้อห้ามสัมพัทธ์'
    };
    return labels[type] || type;
  }

  /**
   * Render PDDI alert as HTML
   */
  function renderPDDIAlert(pddi) {
    const indicatorClass = {
      critical: 'pddi-critical',
      warning: 'pddi-warning',
      info: 'pddi-info'
    }[pddi.indicator] || 'pddi-info';

    let html = `
      <div class="pddi-alert ${indicatorClass}">
        <div class="pddi-header">
          <span class="pddi-indicator">${getIndicatorLabel(pddi.indicator)}</span>
          <span class="pddi-type">${getAlertTypeLabel(pddi.alertType)}</span>
        </div>
        <div class="pddi-drugs">
          <strong>${escapeHtml(pddi.objectDrug)}</strong> +
          <strong>${escapeHtml(pddi.precipitantDrug)}</strong>
        </div>
        <div class="pddi-consequence">${escapeHtml(pddi.clinicalConsequence)}</div>
        <div class="pddi-mechanism">
          <strong>กลไก:</strong>${escapeHtml(pddi.mechanism)}
        </div>
        <div class="pddi-context">
          <strong>ปัจจัยบริบท:</strong>
          <ul>
    `;

    pddi.contextualFactors.forEach(cf => {
      html += `<li><strong>${escapeHtml(cf.factor)}：</strong>${escapeHtml(cf.impact)} - ${escapeHtml(cf.recommendation)}</li>`;
    });

    html += `
          </ul>
        </div>
        <div class="pddi-management">
          <strong>ข้อเสนอแนะการจัดการ:</strong>
          <ul>
    `;

    pddi.managementOptions.forEach(opt => {
      const marker = opt.recommended ? '✓' : '○';
      html += `<li class="${opt.recommended ? 'recommended' : ''}">${marker} <strong>${escapeHtml(opt.option)}：</strong>${escapeHtml(opt.description)}</li>`;
    });

    html += `
          </ul>
        </div>
        <div class="pddi-evidence">
          <strong>ระดับหลักฐาน:</strong>${pddi.evidence.level} |
          <strong>แหล่งที่มา:</strong>${pddi.evidence.sources.join(', ')}
        </div>
      </div>
    `;

    return html;
  }

  function getIndicatorLabel(indicator) {
    const labels = {
      critical: '⚠️ รุนแรง',
      warning: '⚡ เตือน',
      info: 'ℹ️ ข้อมูล'
    };
    return labels[indicator] || indicator;
  }

  function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Export
  global.ThTxGNN = global.ThTxGNN || {};
  global.ThTxGNN.PDDI = {
    checkPDDI: checkPDDI,
    findPDDI: findPDDI,
    generateCDSHooksCard: generateCDSHooksCard,
    renderPDDIAlert: renderPDDIAlert,
    INDICATOR: PDDI_INDICATOR,
    ALERT_TYPE: ALERT_TYPE,
    KNOWLEDGE_BASE: PDDI_KNOWLEDGE_BASE
  };

})(typeof window !== 'undefined' ? window : this);
