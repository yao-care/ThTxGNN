---
layout: default
title: สถาปัตยกรรม CDS Hooks
parent: SMART on FHIR
nav_order: 14
---

# สถาปัตยกรรม ThTxGNN CDS Hooks

เอกสารนี้กำหนดสถาปัตยกรรมบริการ CDS Hooks ของ ThTxGNN สำหรับให้คำแนะนำข้อบ่งใช้ใหม่และการแจ้งเตือน DDI ในขั้นตอนการทำงานของ EHR

---

## ภาพรวม

### เป้าหมาย

| ฟังก์ชัน | คำอธิบาย |
|------|------|
| **คำแนะนำข้อบ่งใช้ใหม่** | เมื่อแพทย์สั่งยา แสดงข้อบ่งใช้ใหม่ที่มีศักยภาพของยานั้น |
| **การแจ้งเตือน DDI** | เมื่อตรวจพบปฏิกิริยาระหว่างยา ให้การแจ้งเตือนและคำแนะนำทางเลือก |
| **ลิงก์การทดลองทางคลินิก** | แสดงการทดลองทางคลินิกที่เกี่ยวข้องเป็นหลักฐานยืนยัน |

### การเลือกเทคโนโลยี

| รายการ | ตัวเลือก | เหตุผล |
|------|------|------|
| **เวอร์ชัน CDS Hooks** | 2.0 | เวอร์ชันหลักปัจจุบัน |
| **วิธีการ Deploy** | Serverless (Cloudflare Workers) | ต้นทุนต่ำ, ความหน่วงต่ำ |
| **แหล่งข้อมูล** | Static JSON + External API | ไม่ต้องการฐานข้อมูล Backend |

---

## สถาปัตยกรรมระบบ

```
┌─────────────────────────────────────────────────────────────────────────┐
│                              ระบบ EHR                                    │
│                                                                         │
│  ┌─────────────────┐    ┌─────────────────────────────────────────────┐ │
│  │   หน้าจอสั่งยา   │───►│  CDS Hooks Client (ในตัว EHR)               │ │
│  └─────────────────┘    └─────────────────────┬───────────────────────┘ │
│                                               │                         │
└───────────────────────────────────────────────┼─────────────────────────┘
                                                │ HTTPS POST
                                                │ order-select / order-sign
                                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                     บริการ ThTxGNN CDS Hooks                            │
│                  (https://cds.thtxgnn.yao.care)                         │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                      Discovery Endpoint                         │   │
│  │                    GET /cds-services                            │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                    Service Endpoints                            │   │
│  │                                                                 │   │
│  │  ┌────────────────────┐  ┌────────────────────┐                │   │
│  │  │  /drug-repurposing │  │  /ddi-alert        │                │   │
│  │  │  คำแนะนำข้อบ่งใช้ใหม่ │  │  การแจ้งเตือน DDI  │                │   │
│  │  └─────────┬──────────┘  └─────────┬──────────┘                │   │
│  │            │                       │                            │   │
│  └────────────┼───────────────────────┼────────────────────────────┘   │
│               │                       │                                │
│               ▼                       ▼                                │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                      ชั้นสืบค้นข้อมูล                            │   │
│  │                                                                 │   │
│  │  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────┐  │   │
│  │  │ search-index.json│  │   ฐานข้อมูล DDI  │  │ClinicalTrials│  │   │
│  │  │ (การคาดการณ์)     │  │ (DDInter+GtoPdb) │  │   .gov API   │  │   │
│  │  └──────────────────┘  └──────────────────┘  └──────────────┘  │   │
│  │                                                                 │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
                                            │
                                            ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                           การตอบกลับ CDS Hooks Card                     │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ Drug Repurposing Candidate: Metformin                          │   │
│  │ ──────────────────────────────────────────────────────────────  │   │
│  │ Predicted indication: Breast Carcinoma (L2 Evidence)            │   │
│  │ 3 active clinical trials | 128 PubMed articles                  │   │
│  │                                                                 │   │
│  │ [View Details]  [Related Clinical Trials]  [Dismiss]            │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## นิยามบริการ CDS Hooks

### Discovery Endpoint

**GET** `/cds-services`

```json
{
  "services": [
    {
      "id": "drug-repurposing",
      "hook": "order-select",
      "title": "ThTxGNN Drug Repurposing Suggestions",
      "description": "Provides AI-powered drug repurposing predictions when medications are selected",
      "prefetch": {
        "patient": "Patient/{{context.patientId}}",
        "currentMedications": "MedicationRequest?patient={{context.patientId}}&status=active"
      }
    },
    {
      "id": "ddi-alert",
      "hook": "order-sign",
      "title": "ThTxGNN DDI Alert Service",
      "description": "Checks for drug-drug interactions and suggests alternatives",
      "prefetch": {
        "patient": "Patient/{{context.patientId}}",
        "currentMedications": "MedicationRequest?patient={{context.patientId}}&status=active",
        "conditions": "Condition?patient={{context.patientId}}&clinical-status=active"
      }
    }
  ]
}
```

---

## Service 1: Drug Repurposing

### เงื่อนไขการเรียกใช้

- **Hook**: `order-select`
- **เวลาเรียกใช้**: เมื่อแพทย์เลือกยา

### ตัวอย่าง Request

```json
{
  "hookInstance": "d1577c69-dfbe-44ad-ba6d-3e05e953b2ea",
  "hook": "order-select",
  "fhirServer": "https://fhir.example.org",
  "context": {
    "patientId": "123",
    "userId": "Practitioner/456",
    "selections": ["MedicationRequest/metformin-draft-001"],
    "draftOrders": {
      "resourceType": "Bundle",
      "entry": [{
        "resource": {
          "resourceType": "MedicationRequest",
          "id": "metformin-draft-001",
          "medicationCodeableConcept": {
            "coding": [{
              "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
              "code": "6809",
              "display": "Metformin"
            }]
          }
        }
      }]
    }
  },
  "prefetch": {
    "patient": { "resourceType": "Patient", "id": "123" }
  }
}
```

### ตัวอย่าง Response

```json
{
  "cards": [
    {
      "uuid": "thtxgnn-repurposing-001",
      "summary": "Drug Repurposing: Metformin may be effective for Breast Carcinoma",
      "detail": "ThTxGNN AI prediction (score: 0.992, evidence: L2)\n\n• 45 clinical trials in progress\n• 128 PubMed publications\n\nThis is a research finding and requires clinical validation.",
      "indicator": "info",
      "source": {
        "label": "ThTxGNN",
        "url": "https://thtxgnn.yao.care/drugs/metformin/",
        "icon": "https://thtxgnn.yao.care/assets/images/icon.png"
      },
      "links": [
        {
          "label": "View Evidence Report",
          "url": "https://thtxgnn.yao.care/drugs/metformin/#breast-carcinoma",
          "type": "absolute"
        },
        {
          "label": "Search Clinical Trials",
          "url": "https://clinicaltrials.gov/search?cond=breast+cancer&intr=metformin",
          "type": "absolute"
        }
      ]
    }
  ]
}
```

---

## Service 2: DDI Alert

### เงื่อนไขการเรียกใช้

- **Hook**: `order-sign`
- **เวลาเรียกใช้**: ก่อนแพทย์ลงนามใบสั่งยา

### ตัวอย่าง Response

```json
{
  "cards": [
    {
      "uuid": "thtxgnn-ddi-001",
      "summary": "Drug Interaction: Warfarin + Ibuprofen",
      "detail": "Concurrent use increases bleeding risk by 3-4x.\n\n**Patient Risk Factors:**\n• Age > 65\n• History of GI bleeding\n\n**Recommendation:** Consider alternative analgesic.",
      "indicator": "warning",
      "source": {
        "label": "ThTxGNN DDI Service",
        "url": "https://thtxgnn.yao.care/ddi/"
      },
      "suggestions": [
        {
          "label": "Replace with Acetaminophen",
          "uuid": "replace-with-acetaminophen",
          "actions": [
            {
              "type": "delete",
              "description": "Remove Ibuprofen order",
              "resourceId": ["MedicationRequest/ibuprofen-draft-001"]
            },
            {
              "type": "create",
              "description": "Order Acetaminophen instead",
              "resource": {
                "resourceType": "MedicationRequest",
                "status": "draft",
                "intent": "order",
                "medicationCodeableConcept": {
                  "coding": [{
                    "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                    "code": "161",
                    "display": "Acetaminophen"
                  }]
                }
              }
            }
          ]
        }
      ],
      "overrideReasons": [
        {
          "code": "patient-benefit",
          "display": "Benefit outweighs risk for this patient"
        },
        {
          "code": "already-monitored",
          "display": "Patient is already being monitored for bleeding"
        }
      ]
    }
  ]
}
```

---

## การใช้งานทางเทคนิค

### ตัวอย่าง Cloudflare Worker

```javascript
// cds-hooks-worker.js

const SEARCH_INDEX_URL = 'https://thtxgnn.yao.care/data/search-index.json';

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // Discovery endpoint
    if (url.pathname === '/cds-services' && request.method === 'GET') {
      return handleDiscovery();
    }

    // Drug repurposing service
    if (url.pathname === '/cds-services/drug-repurposing' && request.method === 'POST') {
      const body = await request.json();
      return handleDrugRepurposing(body);
    }

    // DDI alert service
    if (url.pathname === '/cds-services/ddi-alert' && request.method === 'POST') {
      const body = await request.json();
      return handleDDIAlert(body);
    }

    return new Response('Not Found', { status: 404 });
  }
};

function handleDiscovery() {
  const services = {
    services: [
      {
        id: 'drug-repurposing',
        hook: 'order-select',
        title: 'ThTxGNN Drug Repurposing Suggestions',
        description: 'AI-powered drug repurposing predictions'
      },
      {
        id: 'ddi-alert',
        hook: 'order-sign',
        title: 'ThTxGNN DDI Alert',
        description: 'Drug-drug interaction checking'
      }
    ]
  };

  return new Response(JSON.stringify(services), {
    headers: { 'Content-Type': 'application/json' }
  });
}

async function handleDrugRepurposing(request) {
  // 1. ดึงข้อมูลยาจาก context
  const medications = extractMedications(request.context?.draftOrders);

  // 2. สืบค้นการคาดการณ์ ThTxGNN
  const searchIndex = await fetch(SEARCH_INDEX_URL).then(r => r.json());

  // 3. จับคู่ยา
  const cards = [];
  for (const med of medications) {
    const drug = findDrugInIndex(searchIndex, med.name);
    if (drug && drug.indications?.length > 0) {
      cards.push(createRepurposingCard(drug));
    }
  }

  return new Response(JSON.stringify({ cards }), {
    headers: { 'Content-Type': 'application/json' }
  });
}

function createRepurposingCard(drug) {
  const topIndication = drug.indications[0];
  return {
    uuid: `thtxgnn-${drug.slug}-${Date.now()}`,
    summary: `Drug Repurposing: ${drug.name} may be effective for ${topIndication.name}`,
    detail: `ThTxGNN AI prediction (score: ${topIndication.score.toFixed(2)}, evidence: ${topIndication.level})`,
    indicator: 'info',
    source: {
      label: 'ThTxGNN',
      url: `https://thtxgnn.yao.care/drugs/${drug.slug}/`
    },
    links: [{
      label: 'View Evidence Report',
      url: `https://thtxgnn.yao.care/drugs/${drug.slug}/`,
      type: 'absolute'
    }]
  };
}
```

---

## แผนการ Deploy

### Phase 1: การยืนยัน Prototype

| รายการ | เนื้อหา |
|------|------|
| **แพลตฟอร์ม Deploy** | Cloudflare Workers |
| **ฟังก์ชัน** | Drug Repurposing (order-select) |
| **แหล่งข้อมูล** | Static search-index.json |
| **วิธีการยืนยัน** | ทดสอบด้วย SMART Launcher |

### Phase 2: การรวม DDI

| รายการ | เนื้อหา |
|------|------|
| **ฟังก์ชันใหม่** | DDI Alert (order-sign) |
| **แหล่งข้อมูล** | DDInter + GtoPdb |
| **คำแนะนำทางเลือก** | รวมการคาดการณ์ ThTxGNN |

### Phase 3: การรวม CQL

| รายการ | เนื้อหา |
|------|------|
| **ฟังก์ชันใหม่** | CQL Rule Engine |
| **การปรับตามบริบท** | ปรับการแจ้งเตือนตามข้อมูลผู้ป่วย |
| **การปฏิบัติตามมาตรฐาน** | HL7 PDDI-CDS IG |

---

## แผน URL Endpoint

| สภาพแวดล้อม | URL |
|------|-----|
| **Discovery** | `https://cds.thtxgnn.yao.care/cds-services` |
| **Drug Repurposing** | `https://cds.thtxgnn.yao.care/cds-services/drug-repurposing` |
| **DDI Alert** | `https://cds.thtxgnn.yao.care/cds-services/ddi-alert` |

---

## รายการสิ่งที่ต้องทำ

- [ ] ตั้งค่าโปรเจค Cloudflare Workers
- [ ] ใช้งาน Discovery endpoint
- [ ] ใช้งาน Drug Repurposing service
- [ ] ทดสอบใน SMART Launcher
- [ ] ใช้งาน DDI Alert service
- [ ] รวม ClinicalTrials.gov API
- [ ] ออกแบบแนวทาง UI ของ Card

---

## แหล่งอ้างอิง

- [ข้อกำหนด CDS Hooks](https://cds-hooks.org/)
- [CDS Hooks 2.0 Specification](https://cds-hooks.org/specification/current/)
- [เอกสาร Cloudflare Workers](https://developers.cloudflare.com/workers/)

---

*วันที่สร้าง: 2026-03-01*
