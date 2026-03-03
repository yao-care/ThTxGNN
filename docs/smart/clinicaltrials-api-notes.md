---
layout: default
title: ClinicalTrials.gov API v2 技術筆記
parent: SMART on FHIR
nav_order: 11
---

# ClinicalTrials.gov API v2 技術筆記

本文件整理 ClinicalTrials.gov API v2 的技術規格，供 ThTxGNN 整合臨床試驗搜尋功能參考。

---

## API 概覽

| 項目 | 內容 |
|------|------|
| **Base URL** | `https://clinicaltrials.gov/api/v2` |
| **規格** | OpenAPI Specification 3.0 |
| **格式** | JSON（預設）、CSV |
| **速率限制** | 10 requests/second |
| **舊版 API** | 已於 2024 年 6 月退役 |

---

## 主要端點

### 1. 搜尋臨床試驗

```
GET /studies
```

**查詢參數**：

| 參數 | 說明 | 範例 |
|------|------|------|
| `query.cond` | 疾病/狀況名稱 | `breast+cancer` |
| `query.intr` | 介入措施（藥物名稱） | `metformin` |
| `query.term` | 通用搜尋詞 | `phase+3` |
| `filter.overallStatus` | 試驗狀態 | `RECRUITING` |
| `filter.phase` | 試驗階段 | `PHASE3` |
| `pageSize` | 每頁結果數 | `10`（最大 1000） |
| `format` | 回應格式 | `json` 或 `csv` |
| `countTotal` | 是否包含總數 | `true` |

**狀態篩選值**：
- `RECRUITING` - 招募中
- `COMPLETED` - 已完成
- `ACTIVE_NOT_RECRUITING` - 進行中但不招募
- `NOT_YET_RECRUITING` - 尚未開始招募
- `TERMINATED` - 已終止

**階段篩選值**：
- `PHASE1` - Phase 1
- `PHASE2` - Phase 2
- `PHASE3` - Phase 3
- `PHASE4` - Phase 4
- `EARLY_PHASE1` - 早期 Phase 1

---

## ThTxGNN 整合範例

### 查詢藥物 + 疾病的臨床試驗

當 ThTxGNN 預測 Metformin 可用於乳癌時，搜尋相關臨床試驗：

```bash
curl "https://clinicaltrials.gov/api/v2/studies?query.cond=breast+cancer&query.intr=metformin&pageSize=10&format=json"
```

### 回應結構

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

### 關鍵欄位對應

| JSON 路徑 | ThTxGNN 用途 |
|-----------|-------------|
| `protocolSection.identificationModule.nctId` | NCT 編號（連結） |
| `protocolSection.identificationModule.briefTitle` | 試驗標題 |
| `protocolSection.statusModule.overallStatus` | 試驗狀態 |
| `protocolSection.designModule.phases` | 試驗階段 |
| `protocolSection.designModule.enrollmentInfo.count` | 受試者人數 |
| `protocolSection.conditionsModule.conditions` | 疾病名稱 |

---

## JavaScript 實作範例

```javascript
/**
 * 搜尋藥物-疾病相關臨床試驗
 * @param {string} drugName - 藥物名稱
 * @param {string} condition - 疾病名稱
 * @param {number} pageSize - 每頁結果數
 * @returns {Promise<Array>} 臨床試驗列表
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

// 使用範例
const trials = await searchClinicalTrials('metformin', 'breast cancer');
console.log(`找到 ${trials.length} 個臨床試驗`);
```

---

## 與 ThTxGNN 整合流程

```
ThTxGNN 老藥新用預測
        │
        ▼
┌───────────────────────────────┐
│ 藥物: Metformin               │
│ 預測適應症: breast carcinoma  │
│ 預測分數: 0.9923              │
│ 證據等級: L2                  │
└───────────────┬───────────────┘
                │
                ▼
    ClinicalTrials.gov API v2
                │
                ▼
┌───────────────────────────────┐
│ 相關臨床試驗:                  │
│ ─────────────────────────────  │
│ NCT00909506 (Phase 2, 完成)   │
│ NCT01101438 (Phase 3, 招募中) │
│ ...                           │
└───────────────────────────────┘
```

---

## 待辦事項

- [ ] 在 `smart-app.js` 新增 `searchClinicalTrials()` 函數
- [ ] 建立疾病名稱 → API 查詢詞映射表（處理 Disease Ontology 名稱）
- [ ] 設計 UI：在老藥新用結果中顯示「相關臨床試驗」區塊
- [ ] 處理 API 錯誤和速率限制
- [ ] 快取查詢結果以減少 API 呼叫

---

## 參考資源

- [ClinicalTrials.gov API 官方文件](https://clinicaltrials.gov/data-api/api)
- [API Migration Guide](https://clinicaltrials.gov/data-api/about-api/api-migration)
- [NLM Technical Bulletin - API v2 公告](https://www.nlm.nih.gov/pubs/techbull/ma24/ma24_clinicaltrials_api.html)
- [Study Data Structure](https://clinicaltrials.gov/data-api/about-api/study-data-structure)

---

*建立日期：2026-03-01*
