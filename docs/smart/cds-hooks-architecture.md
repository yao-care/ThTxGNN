---
layout: default
title: CDS Hooks 架構設計
parent: SMART on FHIR
nav_order: 14
---

# ThTxGNN CDS Hooks 架構設計

本文件定義 ThTxGNN 的 CDS Hooks 服務架構，用於在 EHR 工作流程中提供老藥新用建議和 DDI 警示。

---

## 概覽

### 目標

| 功能 | 說明 |
|------|------|
| **老藥新用建議** | 當醫師開立藥物時，提示該藥物的潛在新適應症 |
| **DDI 警示** | 當檢測到藥物交互作用時，提供警示和替代建議 |
| **臨床試驗連結** | 顯示相關臨床試驗作為驗證依據 |

### 技術選型

| 項目 | 選擇 | 理由 |
|------|------|------|
| **CDS Hooks 版本** | 2.0 | 目前主流版本 |
| **部署方式** | Serverless (Cloudflare Workers) | 低成本、低延遲 |
| **資料來源** | 靜態 JSON + 外部 API | 無後端資料庫需求 |

---

## 系統架構

```
┌─────────────────────────────────────────────────────────────────────────┐
│                              EHR 系統                                    │
│                                                                         │
│  ┌─────────────┐    ┌─────────────────────────────────────────────────┐ │
│  │   處方介面   │───►│  CDS Hooks Client (EHR 內建)                    │ │
│  └─────────────┘    └─────────────────────┬───────────────────────────┘ │
│                                           │                             │
└───────────────────────────────────────────┼─────────────────────────────┘
                                            │ HTTPS POST
                                            │ order-select / order-sign
                                            ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                     ThTxGNN CDS Hooks 服務                               │
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
│  │  │  老藥新用建議       │  │  DDI 警示          │                │   │
│  │  └─────────┬──────────┘  └─────────┬──────────┘                │   │
│  │            │                       │                            │   │
│  └────────────┼───────────────────────┼────────────────────────────┘   │
│               │                       │                                │
│               ▼                       ▼                                │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                      資料查詢層                                  │   │
│  │                                                                 │   │
│  │  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────┐  │   │
│  │  │ search-index.json│  │   DDI 資料庫     │  │ClinicalTrials│  │   │
│  │  │ (ThTxGNN 預測)   │  │ (DDInter+GtoPdb) │  │   .gov API   │  │   │
│  │  └──────────────────┘  └──────────────────┘  └──────────────┘  │   │
│  │                                                                 │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
                                            │
                                            ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                           CDS Hooks Card 回應                           │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ 💊 Drug Repurposing Candidate: Metformin                        │   │
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

## CDS Hooks 服務定義

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

### 觸發條件

- **Hook**: `order-select`
- **觸發時機**: 醫師選擇藥物時

### Request 範例

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

### Response 範例

```json
{
  "cards": [
    {
      "uuid": "thtxgnn-repurposing-001",
      "summary": "💊 Drug Repurposing: Metformin may be effective for Breast Carcinoma",
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

### 觸發條件

- **Hook**: `order-sign`
- **觸發時機**: 醫師簽署處方前

### Response 範例

```json
{
  "cards": [
    {
      "uuid": "thtxgnn-ddi-001",
      "summary": "⚠️ Drug Interaction: Warfarin + Ibuprofen",
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

## 技術實作

### Cloudflare Worker 範例

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
  // 1. 從 context 提取藥物資訊
  const medications = extractMedications(request.context?.draftOrders);

  // 2. 查詢 ThTxGNN 預測
  const searchIndex = await fetch(SEARCH_INDEX_URL).then(r => r.json());

  // 3. 匹配藥物
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
    summary: `💊 Drug Repurposing: ${drug.name} may be effective for ${topIndication.name}`,
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

## 部署規劃

### Phase 1：原型驗證

| 項目 | 內容 |
|------|------|
| **部署平台** | Cloudflare Workers |
| **功能** | Drug Repurposing (order-select) |
| **資料來源** | 靜態 search-index.json |
| **驗證方式** | SMART Launcher 測試 |

### Phase 2：DDI 整合

| 項目 | 內容 |
|------|------|
| **新增功能** | DDI Alert (order-sign) |
| **資料來源** | DDInter + GtoPdb |
| **替代建議** | 整合 ThTxGNN 預測 |

### Phase 3：CQL 整合

| 項目 | 內容 |
|------|------|
| **新增功能** | CQL 規則引擎 |
| **情境化** | 根據病患資料調整警示 |
| **合規性** | HL7 PDDI-CDS IG |

---

## 端點 URL 規劃

| 環境 | URL |
|------|-----|
| **Discovery** | `https://cds.thtxgnn.yao.care/cds-services` |
| **Drug Repurposing** | `https://cds.thtxgnn.yao.care/cds-services/drug-repurposing` |
| **DDI Alert** | `https://cds.thtxgnn.yao.care/cds-services/ddi-alert` |

---

## 待辦事項

- [ ] 設定 Cloudflare Workers 專案
- [ ] 實作 Discovery endpoint
- [ ] 實作 Drug Repurposing service
- [ ] 在 SMART Launcher 測試
- [ ] 實作 DDI Alert service
- [ ] 整合 ClinicalTrials.gov API
- [ ] 設計 Card UI 樣式指南

---

## 參考資源

- [CDS Hooks 規範](https://cds-hooks.org/)
- [CDS Hooks 2.0 Specification](https://cds-hooks.org/specification/current/)
- [Cloudflare Workers 文件](https://developers.cloudflare.com/workers/)

---

*建立日期：2026-03-01*
