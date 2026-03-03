---
layout: default
title: บันทึกการเรียนรู้ไวยากรณ์ CQL
parent: SMART on FHIR
nav_order: 12
---

# บันทึกการเรียนรู้ CQL (Clinical Quality Language)

เอกสารนี้รวบรวมพื้นฐานไวยากรณ์ CQL สำหรับการออกแบบกฎการสนับสนุนการตัดสินใจทางคลินิกใน ThTxGNN

---

## ภาพรวม CQL

| รายการ | เนื้อหา |
|------|------|
| **ชื่อเต็ม** | Clinical Quality Language |
| **การใช้งาน** | การวัดคุณภาพทางคลินิก (CQM) + การสนับสนุนการตัดสินใจทางคลินิก (CDS) |
| **เวอร์ชันข้อกำหนด** | v1.5.3 (Normative), v2.0.0 (Ballot) |
| **ความสัมพันธ์กับ FHIRPath** | CQL เป็น superset ของ FHIRPath |
| **Execution Engine** | cql-execution (JavaScript), HAPI FHIR (Java) |

---

## โครงสร้างพื้นฐาน

### การประกาศ Library

```cql
library ThTxGNNCommons version '1.0.0'

using FHIR version '4.0.1'

include FHIRHelpers version '4.0.1' called FHIRHelpers

context Patient
```

| ไวยากรณ์ | คำอธิบาย |
|------|------|
| `library` | ชื่อและเวอร์ชันของ Library |
| `using` | Data Model (FHIR R4) |
| `include` | อ้างอิง CQL Library อื่น |
| `context` | บริบทการทำงาน (Patient หรือ Population) |

---

## ประเภทข้อมูล

### ประเภทพื้นฐาน

| ประเภท | ตัวอย่าง |
|------|------|
| **Boolean** | `true`, `false`, `null` |
| **Integer** | `16`, `-28` |
| **Decimal** | `100.015` |
| **String** | `'pending'`, `'active'` |
| **Date** | `@2014-01-25` |
| **DateTime** | `@2014-01-25T14:30:14.559` |
| **Time** | `@T12:00` |

### ประเภททางคลินิก

| ประเภท | ตัวอย่าง |
|------|------|
| **Quantity** | `6 'gm/cm3'` |
| **Code** | `Code '442487003' from "SNOMED"` |
| **ValueSet** | `valueset "Diabetes": 'urn:oid:...'` |
| **Interval** | `Interval[@2013-01-01, @2014-01-01)` |

---

## การดึงข้อมูล (Retrieve)

### ไวยากรณ์พื้นฐาน

```cql
[Condition: "Diabetes"]
[MedicationRequest: "Metformin"]
[Encounter: "Ambulatory Visit"]
```

### เงื่อนไขการกรอง

```cql
[MedicationRequest: medication in "Antidiabetic Medications"]
  where status = 'active'
```

---

## การสืบค้น (Query)

### ไวยากรณ์เต็ม

```cql
[Encounter: "Inpatient"] E
  with [Condition: "Diabetes"] D
    such that D.onset during E.period
  where E.status = 'finished'
  return Tuple {
    encounterId: E.id,
    diagnosis: D.code.text
  }
  sort by encounterId
```

### ลำดับ Clause

| ลำดับ | Clause | คำอธิบาย |
|------|------|------|
| 1 | `with/without` | เงื่อนไขความสัมพันธ์ |
| 2 | `where` | เงื่อนไขการกรอง |
| 3 | `return` | ฟิลด์ที่ส่งคืน |
| 4 | `sort` | การเรียงลำดับ |

---

## การกำหนดนิพจน์ (Define)

```cql
define "PatientHasDiabetes":
  exists([Condition: "Diabetes"] D
    where D.clinicalStatus ~ "Active")

define "CurrentMedications":
  [MedicationRequest] M
    where M.status = 'active'
```

---

## ฟังก์ชัน (Function)

```cql
define function "GetDrugName"(med MedicationRequest):
  if med.medication is CodeableConcept then
    (med.medication as CodeableConcept).text
  else
    null

define function "CalculateAge"(birthDate Date):
  years between birthDate and Today()
```

---

## พารามิเตอร์ (Parameter)

```cql
parameter MeasurementPeriod Interval<DateTime>
  default Interval[@2026-01-01T00:00:00.0, @2027-01-01T00:00:00.0)

parameter DrugList List<Code>
```

---

## ตัวอย่างการใช้งานใน ThTxGNN

### การกำหนด: รับยาปัจจุบันของผู้ป่วย

```cql
library ThTxGNNDrugRepurposing version '1.0.0'

using FHIR version '4.0.1'
include FHIRHelpers version '4.0.1'

context Patient

// รับยาที่ใช้อยู่ปัจจุบัน
define "ActiveMedications":
  [MedicationRequest] M
    where M.status = 'active'
      and M.intent = 'order'

// รับรายชื่อยา
define "MedicationNames":
  "ActiveMedications" M
    return FHIRHelpers.ToConcept(M.medication as CodeableConcept).display
```

### การกำหนด: ตรรกะการตรวจสอบ DDI

```cql
// ตรวจสอบการใช้ Warfarin + NSAID ร่วมกัน
define "WarfarinPlusNSAID":
  exists([MedicationRequest: "Warfarin"] W
    where W.status = 'active')
  and exists([MedicationRequest: "NSAIDs"] N
    where N.status = 'active')

// ข้อความแจ้งเตือน DDI
define "DDIAlertMessage":
  if "WarfarinPlusNSAID" then
    'WARNING: Concurrent use of Warfarin and NSAIDs increases bleeding risk.'
  else
    null
```

### การกำหนด: การกรองผู้สมัครข้อบ่งใช้ใหม่

```cql
// พารามิเตอร์: เกณฑ์คะแนนการคาดการณ์ ThTxGNN
parameter PredictionScoreThreshold Decimal default 0.9

// การกำหนด: ผู้สมัครที่มีความเชื่อมั่นสูง
define "HighConfidenceCandidates":
  "DrugRepurposingPredictions" P
    where P.score >= PredictionScoreThreshold
      and P.evidenceLevel in {'L1', 'L2', 'L3'}
```

---

## การกำหนด ValueSet

```cql
// ใช้ OID อ้างอิง ValueSet ภายนอก
valueset "Diabetes Medications":
  'http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.113883.3.464.1003.196.12.1001'

// ใช้รหัส SNOMED CT
codesystem "SNOMED": 'http://snomed.info/sct'
code "Type 2 Diabetes": '44054006' from "SNOMED" display 'Type 2 diabetes mellitus'

// ใช้รหัส RxNorm
codesystem "RxNorm": 'http://www.nlm.nih.gov/research/umls/rxnorm'
code "Metformin": '6809' from "RxNorm" display 'Metformin'
```

---

## การรวม Execution Engine

### JavaScript (cql-execution)

```javascript
const cql = require('cql-execution');
const cqlfhir = require('cql-exec-fhir');

// โหลด ELM JSON (ผลการคอมไพล์ CQL)
const elmJson = require('./ThTxGNNCommons.json');

// สร้างแหล่งข้อมูลผู้ป่วย
const patientSource = cqlfhir.PatientSource.FHIRv401();
patientSource.loadBundles([patientBundle]);

// ประมวลผล CQL
const executor = new cql.Executor(new cql.Library(elmJson));
const results = await executor.exec(patientSource);

console.log(results.patientResults);
```

### การคอมไพล์ CQL → ELM

```bash
# ติดตั้ง CQL-to-ELM translator
npm install cql-to-elm

# คอมไพล์ CQL เป็น ELM JSON
cql-to-elm -i ThTxGNNCommons.cql -o ThTxGNNCommons.json
```

---

## แหล่งเรียนรู้

- [ข้อกำหนด CQL](https://cql.hl7.org/) - ข้อกำหนดอย่างเป็นทางการฉบับเต็ม
- [Author's Guide](https://cql.hl7.org/02-authorsguide.html) - คู่มือเริ่มต้น
- [Developer's Guide](https://cql.hl7.org/03-developersguide.html) - คู่มือนักพัฒนา
- [cqframework/clinical_quality_language](https://github.com/cqframework/clinical_quality_language) - เครื่องมืออย่างเป็นทางการ
- [Cooking with CQL](https://github.com/cqframework/CQL-Formatting-and-Usage-Wiki/wiki/Cooking-with-CQL-Examples) - ชุดตัวอย่าง

---

## รายการสิ่งที่ต้องทำ

- [ ] สร้าง ThTxGNNCommons.cql library ฐาน
- [ ] กำหนด ValueSet ชื่อยา
- [ ] ใช้งานกฎการตรวจสอบ DDI
- [ ] รวม cql-execution engine
- [ ] ออกแบบตรรกะการตัดสินใจข้อบ่งใช้ใหม่

---

*วันที่สร้าง: 2026-03-01*
