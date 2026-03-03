---
layout: default
title: บันทึกเทคนิค HL7 PDDI-CDS IG
parent: SMART on FHIR
nav_order: 13
---

# บันทึกเทคนิค HL7 PDDI-CDS Implementation Guide

เอกสารนี้รวบรวมแนวคิดสำคัญของ HL7 Potential Drug-Drug Interaction Clinical Decision Support (PDDI-CDS) Implementation Guide สำหรับการรวมฟังก์ชันการแจ้งเตือน DDI ใน ThTxGNN

---

## ภาพรวม

| รายการ | เนื้อหา |
|------|------|
| **ชื่อเต็ม** | Potential Drug-Drug Interaction Clinical Decision Support |
| **หน้า HL7** | http://hl7.org/fhir/uv/pddi/ |
| **GitHub** | https://github.com/HL7/PDDI-CDS |
| **สัญญาอนุญาต** | CC0-1.0 (สาธารณสมบัติ) |
| **วัตถุประสงค์** | เพิ่มความเกี่ยวข้องทางคลินิกและความเฉพาะเจาะจงของการแจ้งเตือน DDI |

---

## พื้นหลังปัญหา

ระบบการแจ้งเตือน PDDI ที่มีอยู่มีปัญหาดังนี้:

- **ไวเกินไป**: การเปรียบเทียบยาเป็นคู่แบบง่ายทำให้เกิดการแจ้งเตือนผิดพลาดจำนวนมาก
- **ความเหนื่อยล้าจากการแจ้งเตือน**: การวิจัยพบว่าการแจ้งเตือน PDDI เกือบทั้งหมดถูกเพิกเฉย
- **ขาดบริบท**: ไม่พิจารณาสภาพเฉพาะของผู้ป่วย (เช่น การทำงานของไต, อายุ)

PDDI-CDS IG แก้ไขปัญหาเหล่านี้ด้วย:

1. **โมเดลข้อมูลขั้นต่ำ**: กำหนดองค์ประกอบข้อมูลที่การแจ้งเตือน DDI ต้องรวมไว้
2. **การตอบสนองแบบแบ่งระดับ**: ปรับความรุนแรงของการแจ้งเตือนตามบริบททางคลินิก
3. **Artifacts ที่แชร์ได้**: ใช้ CQL + FHIR + CDS Hooks มาตรฐาน

---

## คอมโพเนนต์หลัก

### 1. การรวม CDS Hooks

| Hook | เวลาเรียกใช้ | การใช้งาน |
|------|----------|------|
| `order-select` | เมื่อแพทย์เลือกยา | ตรวจจับระยะแรก ให้คำแนะนำ |
| `order-sign` | เมื่อแพทย์ลงนามใบสั่งยา | ยืนยันขั้นสุดท้าย ให้ข้อมูลรายละเอียด |

**ขั้นตอน**:

```
EHR → order-select hook → บริการ CDS → ตรวจจับ PDDI → ส่งคืน Card
                                            ↓
                                      แพทย์เลือกการกระทำ
                                            ↓
EHR → order-sign hook → บริการ CDS → ให้คำแนะนำรายละเอียด → ส่งคืน Card
```

### 2. โครงสร้าง PlanDefinition

PlanDefinition เป็นทรัพยากรหลักของ PDDI-CDS artifacts:

```json
{
  "resourceType": "PlanDefinition",
  "id": "warfarin-nsaid-pddi",
  "type": {
    "coding": [{
      "system": "http://terminology.hl7.org/CodeSystem/plan-definition-type",
      "code": "eca-rule"
    }]
  },
  "trigger": [{
    "type": "named-event",
    "name": "order-select"
  }],
  "condition": [{
    "kind": "applicability",
    "expression": {
      "language": "text/cql",
      "expression": "Inclusion Criteria"
    }
  }],
  "action": [{
    "title": "Warfarin + NSAID Interaction",
    "description": "Concurrent use increases bleeding risk",
    "dynamicValue": [{
      "path": "action.description",
      "expression": {
        "language": "text/cql",
        "expression": "Get Detail"
      }
    }]
  }]
}
```

### 3. ตัวอย่าง CQL Library

```cql
library Warfarin_NSAIDs_CDS version '1.0.0'

using FHIR version '4.0.1'
include FHIRHelpers version '4.0.1'

context Patient

// นิยามคำศัพท์
valueset "Warfarins": 'http://example.org/fhir/ValueSet/warfarins'
valueset "NSAIDs": 'http://example.org/fhir/ValueSet/nsaids'

// ตรรกะการตรวจจับ
define "Is On Warfarin":
  exists([MedicationRequest: "Warfarins"] M
    where M.status = 'active')

define "Is On NSAID":
  exists([MedicationRequest: "NSAIDs"] M
    where M.status = 'active')

define "Inclusion Criteria":
  "Is On Warfarin" and "Is On NSAID"

// ข้อความแบบไดนามิก
define "Get Detail":
  if "Has GI Risk Factors" then
    'HIGH RISK: Patient has GI risk factors. Consider alternatives.'
  else
    'MODERATE RISK: Monitor for signs of bleeding.'
```

### 4. โครงสร้าง Response Card

บริการ CDS ส่งคืน CDS Hooks Card:

```json
{
  "cards": [{
    "uuid": "warfarin-nsaid-001",
    "summary": "Potential Drug-Drug Interaction: Warfarin + NSAID",
    "detail": "Concurrent use increases bleeding risk by 3-4x.",
    "indicator": "warning",
    "source": {
      "label": "PDDI-CDS Service",
      "url": "https://example.org/pddi-cds"
    },
    "suggestions": [{
      "label": "Use alternative analgesic",
      "actions": [{
        "type": "create",
        "description": "Order acetaminophen instead",
        "resource": {
          "resourceType": "MedicationRequest",
          "medicationCodeableConcept": {
            "coding": [{"code": "161", "display": "Acetaminophen"}]
          }
        }
      }]
    }],
    "links": [{
      "label": "Warfarin-NSAID Interaction Evidence",
      "url": "https://example.org/evidence/warfarin-nsaid",
      "type": "smart"
    }]
  }]
}
```

### 5. ทรัพยากร DetectedIssue

ใช้สำหรับบันทึกผลการตรวจจับ PDDI และการตอบสนองของแพทย์:

```json
{
  "resourceType": "DetectedIssue",
  "id": "pddi-warfarin-nsaid-001",
  "status": "final",
  "code": {
    "coding": [{
      "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
      "code": "DRG",
      "display": "Drug Interaction Alert"
    }]
  },
  "severity": "moderate",
  "patient": { "reference": "Patient/123" },
  "identifiedDateTime": "2026-03-01T10:00:00Z",
  "implicated": [
    { "reference": "MedicationRequest/warfarin-001" },
    { "reference": "MedicationRequest/ibuprofen-001" }
  ],
  "mitigation": [{
    "action": {
      "coding": [{
        "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
        "code": "13",
        "display": "Stopped Concurrent Therapy"
      }]
    },
    "date": "2026-03-01T10:05:00Z",
    "author": { "reference": "Practitioner/456" }
  }]
}
```

---

## ระดับการใช้งาน

| ระดับ | ข้อกำหนด | คำแนะนำ ThTxGNN |
|------|------|-------------|
| **Level 1** | การตรวจจับ PDDI พื้นฐาน + การจัดเก็บ DetectedIssue | เป้าหมายปัจจุบัน |
| **Level 2** | + การกรองตามบริบท (อายุ, การทำงานของไต ฯลฯ) | การขยายในอนาคต |
| **Level 3** | + อินเทอร์เฟซการตัดสินใจร่วม + คำแนะนำทางเลือก | เป้าหมายระยะยาว |

---

## แผนการรวม ThTxGNN

### Phase 1: การแจ้งเตือนพื้นฐาน

1. **ใช้งาน CDS Hooks endpoint**
   - รองรับ `order-select` trigger
   - ส่งคืน Warning/Info Card

2. **ใช้ข้อมูล DDI ที่มีอยู่**
   - DDInter: 222,391 รายการ
   - GtoPdb: 4,636 รายการ

3. **การออกแบบ Card พื้นฐาน**
   ```
   DDI Warning: Warfarin + Ibuprofen
   Bleeding risk increased 3-4x.
   [View Evidence] [Dismiss]
   ```

### Phase 2: การปรับตามบริบท

1. **รวมข้อมูลผู้ป่วย**
   - อายุ, การทำงานของไต, ประวัติการเจ็บป่วย
   - ปรับความรุนแรงของการแจ้งเตือน

2. **ตรรกะ CQL**
   - ใช้งานกฎการแบ่งระดับความเสี่ยง
   - ปรับแต่งข้อความตามบริบท

### Phase 3: การรวมข้อบ่งใช้ใหม่

1. **คำแนะนำทางเลือก**
   - เมื่อเกิด DDI แนะนำยาทางเลือกที่ ThTxGNN คาดการณ์

2. **การตัดสินใจร่วม**
   - ให้การเปรียบเทียบความเสี่ยง/ประโยชน์
   - สนับสนุนการตัดสินใจทางคลินิก

---

## ตัวอย่างกฎ DDI (ThTxGNN)

### Warfarin + NSAID

```cql
library ThTxGNN_DDI_Warfarin_NSAID version '1.0.0'

using FHIR version '4.0.1'

context Patient

// นิยาม
define "Is On Warfarin":
  exists([MedicationRequest] M
    where M.status = 'active'
    and M.medication.coding.code in {'855288', '855290'}) // RxNorm

define "Is On NSAID":
  exists([MedicationRequest] M
    where M.status = 'active'
    and M.medication.coding.code in {'5640', '197805'}) // RxNorm

define "Has GI Bleed History":
  exists([Condition] C
    where C.code.coding.code in {'74474003'}) // SNOMED: GI hemorrhage

define "Risk Level":
  if "Has GI Bleed History" then 'critical'
  else if AgeInYears() > 65 then 'warning'
  else 'info'

// การรวม ThTxGNN: คำแนะนำทางเลือก
define "Alternative Analgesic Candidates":
  // สืบค้นการคาดการณ์ ThTxGNN: ยาใดที่ทดแทน NSAID สำหรับความเจ็บปวดได้
  // และไม่มีปฏิกิริยากับ Warfarin
  null // ในการใช้งานจริงเชื่อมต่อ ThTxGNN API
```

---

## รายการสิ่งที่ต้องทำ

- [ ] ออกแบบสถาปัตยกรรมบริการ ThTxGNN CDS Hooks
- [ ] สร้างตัวอย่างการใช้งาน Warfarin + NSAID
- [ ] รวมข้อมูล DDI ที่มีอยู่เข้าสู่ CQL ValueSet
- [ ] ออกแบบคอมโพเนนต์ UI สำหรับ Card
- [ ] ใช้งานการจัดเก็บ DetectedIssue (ตัวเลือก)

---

## แหล่งอ้างอิง

- [HL7 PDDI-CDS IG](http://hl7.org/fhir/uv/pddi/)
- [GitHub: HL7/PDDI-CDS](https://github.com/HL7/PDDI-CDS)
- [ข้อกำหนด CDS Hooks](https://cds-hooks.org/)
- [PubMed: Implementation of CDS Services for PDDI](https://pubmed.ncbi.nlm.nih.gov/31438019/)

---

*วันที่สร้าง: 2026-03-01*
