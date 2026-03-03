---
layout: default
title: API Reference
parent: แหล่งข้อมูล
nav_order: 3
---

# API Reference

ThTxGNN มี API ที่เป็นไปตามมาตรฐาน FHIR R4 สำหรับการคาดการณ์การใช้ยาเก่าในข้อบ่งใช้ใหม่

## FHIR Endpoints

### Capability Statement

```
GET /fhir/metadata
```

คืนค่า CapabilityStatement ของเซิร์ฟเวอร์ที่อธิบาย resource และ operation ที่รองรับ

### MedicationKnowledge

```
GET /fhir/MedicationKnowledge/{id}
```

คืนค่าข้อมูลยา ประกอบด้วย:
- รหัสยา (DrugBank ID)
- ชื่อยา
- สถานะการลงทะเบียน
- ข้อบ่งใช้ที่ทราบ

**ตัวอย่าง Response:**
```json
{
  "resourceType": "MedicationKnowledge",
  "id": "DB00381",
  "code": {
    "coding": [{
      "system": "https://www.drugbank.ca",
      "code": "DB00381",
      "display": "Amlodipine"
    }]
  },
  "status": "active"
}
```

### ClinicalUseDefinition

```
GET /fhir/ClinicalUseDefinition/{id}
```

คืนค่าการคาดการณ์การใช้ยาที่มีศักยภาพ ประกอบด้วย:
- การอ้างอิงยา
- การอ้างอิงข้อบ่งใช้
- แหล่งหลักฐาน
- คะแนนความเชื่อมั่น

## Search Parameters

### MedicationKnowledge Search

| พารามิเตอร์ | ประเภท | คำอธิบาย |
|------------|--------|----------|
| code | token | DrugBank ID |
| status | token | active, inactive |

### ClinicalUseDefinition Search

| พารามิเตอร์ | ประเภท | คำอธิบาย |
|------------|--------|----------|
| subject | reference | MedicationKnowledge reference |
| type | token | indication, contraindication |

## SMART on FHIR

ThTxGNN รองรับ SMART on FHIR สำหรับการเชื่อมต่อกับ EHR

### Launch URL

```
/smart/launch.html
```

### Supported Scopes

- `launch`
- `patient/MedicationKnowledge.read`
- `patient/ClinicalUseDefinition.read`

## Rate Limits

- ไม่ต้องการการยืนยันตัวตนสำหรับการอ่าน
- จำกัดอัตรา: 100 คำขอต่อนาที
- รูปแบบ Response: JSON เท่านั้น

## Status Codes

| รหัส | คำอธิบาย |
|------|----------|
| 200 | สำเร็จ |
| 404 | ไม่พบ Resource |
| 429 | เกินขีดจำกัดอัตรา |
| 500 | Server error |

## ข้อจำกัดความรับผิดชอบ

API นี้มีไว้เพื่อการวิจัยเท่านั้น การคาดการณ์การใช้ยาเก่าในข้อบ่งใช้ใหม่ต้องผ่านการทดลองทางคลินิกก่อนนำไปใช้
