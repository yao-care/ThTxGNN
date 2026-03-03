---
layout: default
title: บันทึกเทคนิค ClinicalTrials.gov API v2
parent: SMART on FHIR
nav_order: 11
---

# บันทึกเทคนิค ClinicalTrials.gov API v2

เอกสารนี้รวบรวมข้อกำหนดทางเทคนิคของ ClinicalTrials.gov API v2 สำหรับการรวมฟังก์ชันค้นหาการทดลองทางคลินิกใน ThTxGNN

---

## ภาพรวม API

| รายการ | เนื้อหา |
|------|------|
| **Base URL** | `https://clinicaltrials.gov/api/v2` |
| **ข้อกำหนด** | OpenAPI Specification 3.0 |
| **รูปแบบ** | JSON (ค่าเริ่มต้น), CSV |
| **จำกัดอัตรา** | 10 requests/second |
| **API เวอร์ชันเก่า** | ยกเลิกแล้วในเดือนมิถุนายน 2024 |

---

## Endpoints หลัก

### 1. ค้นหาการทดลองทางคลินิก

```
GET /studies
```

**พารามิเตอร์การค้นหา**:

| พารามิเตอร์ | คำอธิบาย | ตัวอย่าง |
|------|------|------|
| `query.cond` | ชื่อโรค/อาการ | `breast+cancer` |
| `query.intr` | การแทรกแซง (ชื่อยา) | `metformin` |
| `query.term` | คำค้นหาทั่วไป | `phase+3` |
| `filter.overallStatus` | สถานะการทดลอง | `RECRUITING` |
| `filter.phase` | ระยะการทดลอง | `PHASE3` |
| `pageSize` | จำนวนผลลัพธ์ต่อหน้า | `10` (สูงสุด 1000) |
| `format` | รูปแบบการตอบกลับ | `json` หรือ `csv` |
| `countTotal` | รวมจำนวนทั้งหมดหรือไม่ | `true` |

**ค่าสถานะที่กรองได้**:
- `RECRUITING` - กำลังรับสมัคร
- `COMPLETED` - เสร็จสมบูรณ์
- `ACTIVE_NOT_RECRUITING` - ดำเนินการอยู่แต่ไม่รับสมัคร
- `NOT_YET_RECRUITING` - ยังไม่เริ่มรับสมัคร
- `TERMINATED` - ยุติแล้ว

**ค่าระยะที่กรองได้**:
- `PHASE1` - Phase 1
- `PHASE2` - Phase 2
- `PHASE3` - Phase 3
- `PHASE4` - Phase 4
- `EARLY_PHASE1` - Phase 1 ระยะแรก

---

## ตัวอย่างการรวม ThTxGNN

### ค้นหาการทดลองทางคลินิกของยา + โรค

เมื่อ ThTxGNN คาดการณ์ว่า Metformin อาจใช้ได้กับมะเร็งเต้านม ค้นหาการทดลองทางคลินิกที่เกี่ยวข้อง:

```bash
curl "https://clinicaltrials.gov/api/v2/studies?query.cond=breast+cancer&query.intr=metformin&pageSize=10&format=json"
```

### โครงสร้างการตอบกลับ

```json
{
  "studies": [
    {
      "protocolSection": {
        "identificationModule": {
          "nctId": "NCT00909506",
          "briefTitle": "Efficacy and Safety of Adjuvant Metformin for Operable Breast Cancer Patients"
        },
        "statusModule": {
          "overallStatus": "COMPLETED",
          "startDateStruct": { "date": "2009-06" },
          "completionDateStruct": { "date": "2011-12" }
        },
        "designModule": {
          "studyType": "INTERVENTIONAL",
          "phases": ["PHASE2"],
          "designInfo": {
            "allocation": "RANDOMIZED",
            "interventionModel": "PARALLEL"
          },
          "enrollmentInfo": { "count": 105 }
        },
        "conditionsModule": {
          "conditions": ["Breast Cancer"]
        },
        "armsInterventionsModule": {
          "interventions": [
            { "type": "DRUG", "name": "Metformin" }
          ]
        }
      }
    }
  ]
}
```

### การแมปฟิลด์ที่สำคัญ

| เส้นทาง JSON | การใช้งานใน ThTxGNN |
|-----------|-------------|
| `protocolSection.identificationModule.nctId` | หมายเลข NCT (ลิงก์) |
| `protocolSection.identificationModule.briefTitle` | ชื่อการทดลอง |
| `protocolSection.statusModule.overallStatus` | สถานะการทดลอง |
| `protocolSection.designModule.phases` | ระยะการทดลอง |
| `protocolSection.designModule.enrollmentInfo.count` | จำนวนผู้เข้าร่วม |
| `protocolSection.conditionsModule.conditions` | ชื่อโรค |

---

## ตัวอย่างการใช้งาน JavaScript

```javascript
/**
 * ค้นหาการทดลองทางคลินิกที่เกี่ยวข้องกับยา-โรค
 * @param {string} drugName - ชื่อยา
 * @param {string} condition - ชื่อโรค
 * @param {number} pageSize - จำนวนผลลัพธ์ต่อหน้า
 * @returns {Promise<Array>} รายการการทดลองทางคลินิก
 */
async function searchClinicalTrials(drugName, condition, pageSize = 10) {
  const baseUrl = 'https://clinicaltrials.gov/api/v2/studies';
  const params = new URLSearchParams({
    'query.cond': condition,
    'query.intr': drugName,
    'pageSize': pageSize,
    'format': 'json',
    'countTotal': 'true'
  });

  const response = await fetch(`${baseUrl}?${params}`);
  const data = await response.json();

  return data.studies.map(study => ({
    nctId: study.protocolSection.identificationModule.nctId,
    title: study.protocolSection.identificationModule.briefTitle,
    status: study.protocolSection.statusModule.overallStatus,
    phases: study.protocolSection.designModule?.phases || [],
    enrollment: study.protocolSection.designModule?.enrollmentInfo?.count,
    conditions: study.protocolSection.conditionsModule?.conditions || [],
    url: `https://clinicaltrials.gov/study/${study.protocolSection.identificationModule.nctId}`
  }));
}

// ตัวอย่างการใช้งาน
const trials = await searchClinicalTrials('metformin', 'breast cancer');
console.log(`พบ ${trials.length} การทดลองทางคลินิก`);
```

---

## ขั้นตอนการรวมกับ ThTxGNN

```
การคาดการณ์ข้อบ่งใช้ใหม่ ThTxGNN
        │
        ▼
┌───────────────────────────────┐
│ ยา: Metformin                 │
│ ข้อบ่งใช้ที่คาดการณ์: breast   │
│   carcinoma                   │
│ คะแนนการคาดการณ์: 0.9923      │
│ ระดับหลักฐาน: L2             │
└───────────────┬───────────────┘
                │
                ▼
    ClinicalTrials.gov API v2
                │
                ▼
┌───────────────────────────────┐
│ การทดลองทางคลินิกที่เกี่ยวข้อง: │
│ ─────────────────────────────  │
│ NCT00909506 (Phase 2, เสร็จ)   │
│ NCT01101438 (Phase 3, รับสมัคร)│
│ ...                           │
└───────────────────────────────┘
```

---

## รายการสิ่งที่ต้องทำ

- [ ] เพิ่มฟังก์ชัน `searchClinicalTrials()` ใน `smart-app.js`
- [ ] สร้างตารางแมปชื่อโรค → คำค้นหา API (จัดการชื่อ Disease Ontology)
- [ ] ออกแบบ UI: แสดงส่วน "การทดลองทางคลินิกที่เกี่ยวข้อง" ในผลลัพธ์ข้อบ่งใช้ใหม่
- [ ] จัดการข้อผิดพลาด API และการจำกัดอัตรา
- [ ] แคชผลการค้นหาเพื่อลดการเรียก API

---

## แหล่งอ้างอิง

- [เอกสาร ClinicalTrials.gov API อย่างเป็นทางการ](https://clinicaltrials.gov/data-api/api)
- [คู่มือการย้าย API](https://clinicaltrials.gov/data-api/about-api/api-migration)
- [NLM Technical Bulletin - ประกาศ API v2](https://www.nlm.nih.gov/pubs/techbull/ma24/ma24_clinicaltrials_api.html)
- [โครงสร้างข้อมูลการศึกษา](https://clinicaltrials.gov/data-api/about-api/study-data-structure)

---

*วันที่สร้าง: 2026-03-01*
