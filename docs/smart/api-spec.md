---
layout: default
title: ข้อกำหนด FHIR API
parent: SMART on FHIR
nav_order: 7
---

# ข้อกำหนด ThTxGNN FHIR API

เอกสารนี้อธิบายข้อกำหนด FHIR API สำหรับข้อมูลการคาดการณ์ข้อบ่งใช้ใหม่ของ ThTxGNN สำหรับการรวมระบบภายนอก

---

## ภาพรวม API

| รายการ | เนื้อหา |
|------|------|
| **Base URL** | `https://thtxgnn.yao.care/fhir` |
| **เวอร์ชัน FHIR** | R4 (4.0.1) |
| **รูปแบบ** | `application/fhir+json` |
| **วิธีการเข้าถึง** | ไฟล์ JSON แบบ Static (ไม่ต้องยืนยันตัวตน) |
| **ปริมาณข้อมูล** | ยา 189 รายการ, ข้อบ่งใช้ที่คาดการณ์ 1,268 รายการ |

---

## ประเภททรัพยากร

### 1. MedicationKnowledge

ข้อมูลพื้นฐานของยา รวมถึงชื่อยา, DrugBank ID, จำนวนข้อบ่งใช้ที่คาดการณ์ ฯลฯ

**Endpoint**:
```
GET /fhir/MedicationKnowledge/{drug-slug}.json
```

**ตัวอย่างคำขอ**:
```bash
curl https://thtxgnn.yao.care/fhir/MedicationKnowledge/metformin.json
```

**โครงสร้างการตอบกลับ**:
```json
{
  "resourceType": "MedicationKnowledge",
  "id": "metformin",
  "status": "active",
  "code": {
    "coding": [
      {
        "system": "https://www.drugbank.ca/drugs/",
        "code": "DB00331",
        "display": "Metformin"
      }
    ],
    "text": "Metformin"
  },
  "indicationGuideline": [
    {
      "indication": [
        {
          "reference": "ClinicalUseDefinition/metformin-breast-carcinoma"
        }
      ]
    }
  ],
  "extension": [
    {
      "url": "https://thtxgnn.yao.care/fhir/StructureDefinition/prediction-count",
      "valueInteger": 15
    },
    {
      "url": "https://thtxgnn.yao.care/fhir/StructureDefinition/evidence-level",
      "valueString": "L2"
    }
  ]
}
```

**คำอธิบายฟิลด์**:

| ฟิลด์ | ประเภท | คำอธิบาย |
|------|------|------|
| `id` | string | Slug ของยา (ชื่อที่เหมาะกับ URL) |
| `code.coding[0].code` | string | DrugBank ID |
| `code.coding[0].display` | string | ชื่อยาภาษาอังกฤษ |
| `indicationGuideline` | array | รายการอ้างอิงข้อบ่งใช้ที่คาดการณ์ |
| `extension[prediction-count]` | integer | จำนวนข้อบ่งใช้ที่คาดการณ์ |
| `extension[evidence-level]` | string | ระดับหลักฐานสูงสุด (L1-L5) |

---

### 2. ClinicalUseDefinition

ผลการคาดการณ์ข้อบ่งใช้ใหม่ รวมถึงคู่ยา-ข้อบ่งใช้, คะแนนการคาดการณ์, ระดับหลักฐาน ฯลฯ

**Endpoint**:
```
GET /fhir/ClinicalUseDefinition/{drug-indication-slug}.json
```

**ตัวอย่างคำขอ**:
```bash
curl https://thtxgnn.yao.care/fhir/ClinicalUseDefinition/metformin-breast-carcinoma.json
```

**โครงสร้างการตอบกลับ**:
```json
{
  "resourceType": "ClinicalUseDefinition",
  "id": "metformin-breast-carcinoma",
  "type": "indication",
  "status": "active",
  "subject": [
    {
      "reference": "MedicationKnowledge/metformin"
    }
  ],
  "indication": {
    "diseaseSymptomProcedure": {
      "concept": {
        "coding": [
          {
            "system": "http://www.disease-ontology.org",
            "code": "DOID:1612",
            "display": "breast carcinoma"
          }
        ],
        "text": "breast carcinoma"
      }
    }
  },
  "extension": [
    {
      "url": "https://thtxgnn.yao.care/fhir/StructureDefinition/prediction-score",
      "valueDecimal": 0.9923
    },
    {
      "url": "https://thtxgnn.yao.care/fhir/StructureDefinition/evidence-level",
      "valueString": "L2"
    },
    {
      "url": "https://thtxgnn.yao.care/fhir/StructureDefinition/clinical-trials-count",
      "valueInteger": 45
    },
    {
      "url": "https://thtxgnn.yao.care/fhir/StructureDefinition/pubmed-count",
      "valueInteger": 128
    }
  ]
}
```

**คำอธิบายฟิลด์**:

| ฟิลด์ | ประเภท | คำอธิบาย |
|------|------|------|
| `id` | string | Slug ของยา-ข้อบ่งใช้ |
| `subject[0].reference` | string | ทรัพยากรยาที่เกี่ยวข้อง |
| `indication.diseaseSymptomProcedure.concept.coding[0].code` | string | Disease Ontology ID (DOID) |
| `indication.diseaseSymptomProcedure.concept.text` | string | ชื่อโรคภาษาอังกฤษ |
| `extension[prediction-score]` | decimal | คะแนนการคาดการณ์ TxGNN (0-1) |
| `extension[evidence-level]` | string | ระดับหลักฐาน (L1-L5) |
| `extension[clinical-trials-count]` | integer | จำนวนการทดลองทางคลินิกที่เกี่ยวข้อง |
| `extension[pubmed-count]` | integer | จำนวนเอกสาร PubMed ที่เกี่ยวข้อง |

---

### 3. Bundle (ข้อมูลทั้งหมด)

รับข้อมูลการคาดการณ์ทั้งหมดในครั้งเดียว

**Endpoint**:
```
GET /fhir/Bundle/all-predictions.json
```

**โครงสร้างการตอบกลับ**:
```json
{
  "resourceType": "Bundle",
  "type": "collection",
  "total": 1457,
  "entry": [
    { "resource": { "resourceType": "MedicationKnowledge", ... } },
    { "resource": { "resourceType": "ClinicalUseDefinition", ... } }
  ]
}
```

---

## นิยามระดับหลักฐาน

| ระดับ | นิยาม | คำอธิบาย |
|------|------|------|
| **L1** | หลาย Phase 3 RCT | หลักฐานสูงสุด หลายการทดลองสุ่มควบคุมขนาดใหญ่ |
| **L2** | Phase 3 เดียว หรือหลาย Phase 2 | มีการทดลองทางคลินิกสนับสนุน |
| **L3** | Phase 1/2 หรือเอกสารจำนวนมาก | หลักฐานทางคลินิกระยะแรก |
| **L4** | การศึกษาในสัตว์/ในหลอดทดลอง | หลักฐานก่อนคลินิก |
| **L5** | เฉพาะการคาดการณ์จากโมเดล | ไม่มีหลักฐานทางคลินิก เป็นเพียงการคาดการณ์ AI |

---

## ตัวอย่างการใช้งาน

### JavaScript (Front-end)

```javascript
async function getDrugPredictions(drugSlug) {
  const response = await fetch(
    `https://thtxgnn.yao.care/fhir/MedicationKnowledge/${drugSlug}.json`
  );
  const drug = await response.json();

  // รับข้อบ่งใช้ที่คาดการณ์
  const indications = await Promise.all(
    drug.indicationGuideline.flatMap(g =>
      g.indication.map(async i => {
        const ref = i.reference.replace('ClinicalUseDefinition/', '');
        const res = await fetch(
          `https://thtxgnn.yao.care/fhir/ClinicalUseDefinition/${ref}.json`
        );
        return res.json();
      })
    )
  );

  return { drug, indications };
}
```

### Python

```python
import requests

def get_drug_predictions(drug_slug):
    base_url = "https://thtxgnn.yao.care/fhir"

    # รับข้อมูลยา
    drug = requests.get(f"{base_url}/MedicationKnowledge/{drug_slug}.json").json()

    # รับข้อบ่งใช้ที่คาดการณ์
    indications = []
    for guideline in drug.get("indicationGuideline", []):
        for ind in guideline.get("indication", []):
            ref = ind["reference"].replace("ClinicalUseDefinition/", "")
            indication = requests.get(
                f"{base_url}/ClinicalUseDefinition/{ref}.json"
            ).json()
            indications.append(indication)

    return {"drug": drug, "indications": indications}
```

### cURL

```bash
# รับข้อมูลยา Metformin
curl -s https://thtxgnn.yao.care/fhir/MedicationKnowledge/metformin.json | jq .

# รับการคาดการณ์เฉพาะ
curl -s https://thtxgnn.yao.care/fhir/ClinicalUseDefinition/metformin-breast-carcinoma.json | jq .

# รับข้อมูลทั้งหมด
curl -s https://thtxgnn.yao.care/fhir/Bundle/all-predictions.json | jq .total
```

---

## คำแนะนำการเชื่อมต่อ

### สำหรับ SMART on FHIR App

1. เรียกใช้ ThTxGNN API ใน SMART App เพื่อเสริมข้อมูลข้อบ่งใช้ใหม่
2. ใช้ `MedicationKnowledge.code.coding[0].code` (DrugBank ID) สำหรับการแมปยา
3. แสดง `ClinicalUseDefinition.extension[evidence-level]` เป็นตัวบ่งชี้ความเชื่อมั่น

### สำหรับระบบ Back-end

1. แคช `/fhir/Bundle/all-predictions.json` เป็นระยะ (แนะนำอัปเดตรายวัน)
2. สร้างตารางแมป DrugBank ID → ThTxGNN slug
3. เชื่อมต่อกับระบบสนับสนุนการตัดสินใจทางคลินิกที่มีอยู่

---

## ข้อจำกัดและข้อจำกัดความรับผิดชอบ

1. **เพื่อการวิจัยเท่านั้น**: ผลการคาดการณ์ไม่ถือเป็นคำแนะนำทางการแพทย์
2. **ข้อมูลแบบ Static**: ข้อมูลอัปเดตเดือนละครั้ง
3. **ไม่มี API แบบ Real-time**: เป็นไฟล์ JSON แบบ Static ไม่มีฟังก์ชันค้นหา
4. **ข้อมูลภาษาอังกฤษ**: ชื่อยาและโรคเป็นภาษาอังกฤษ

---

## ข้อมูลติดต่อ

- **เว็บไซต์**: https://thtxgnn.yao.care/
- **GitHub**: https://github.com/yao-care/ThTxGNN
- **สถานะ API**: https://thtxgnn.yao.care/fhir/metadata

---

<div class="disclaimer">
<strong>ข้อจำกัดความรับผิดชอบ</strong>: ข้อมูลที่ให้โดย API นี้มีไว้เพื่อการวิจัยเท่านั้น ไม่สามารถทดแทนคำแนะนำทางการแพทย์จากผู้เชี่ยวชาญ ผลการคาดการณ์การใช้ยาเก่าในข้อบ่งใช้ใหม่ทั้งหมดต้องผ่านการทดลองทางคลินิกก่อนนำไปใช้
</div>
