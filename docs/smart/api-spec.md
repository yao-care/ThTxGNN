---
layout: default
title: FHIR API 規格
parent: SMART on FHIR
nav_order: 7
---

# ThTxGNN FHIR API 規格

本文件說明 ThTxGNN 老藥新用預測資料的 FHIR API 規格，供外部系統整合參考。

---

## API 概覽

| 項目 | 內容 |
|------|------|
| **Base URL** | `https://thtxgnn.yao.care/fhir` |
| **FHIR 版本** | R4 (4.0.1) |
| **格式** | `application/fhir+json` |
| **存取方式** | 靜態 JSON 檔案（無需認證） |
| **資料量** | 189 個藥物、1,268 個預測適應症 |

---

## 資源類型

### 1. MedicationKnowledge

藥物基本資訊，包含藥物名稱、DrugBank ID、預測適應症數量等。

**端點**：
```
GET /fhir/MedicationKnowledge/{drug-slug}.json
```

**範例請求**：
```bash
curl https://thtxgnn.yao.care/fhir/MedicationKnowledge/metformin.json
```

**回應結構**：
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

**欄位說明**：

| 欄位 | 類型 | 說明 |
|------|------|------|
| `id` | string | 藥物 slug（URL 友善名稱） |
| `code.coding[0].code` | string | DrugBank ID |
| `code.coding[0].display` | string | 藥物英文名 |
| `indicationGuideline` | array | 預測適應症參照清單 |
| `extension[prediction-count]` | integer | 預測適應症數量 |
| `extension[evidence-level]` | string | 最高證據等級（L1-L5） |

---

### 2. ClinicalUseDefinition

老藥新用預測結果，包含藥物-適應症配對、預測分數、證據等級等。

**端點**：
```
GET /fhir/ClinicalUseDefinition/{drug-indication-slug}.json
```

**範例請求**：
```bash
curl https://thtxgnn.yao.care/fhir/ClinicalUseDefinition/metformin-breast-carcinoma.json
```

**回應結構**：
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

**欄位說明**：

| 欄位 | 類型 | 說明 |
|------|------|------|
| `id` | string | 藥物-適應症 slug |
| `subject[0].reference` | string | 關聯藥物資源 |
| `indication.diseaseSymptomProcedure.concept.coding[0].code` | string | 疾病本體 ID (DOID) |
| `indication.diseaseSymptomProcedure.concept.text` | string | 疾病英文名 |
| `extension[prediction-score]` | decimal | TxGNN 預測分數 (0-1) |
| `extension[evidence-level]` | string | 證據等級 (L1-L5) |
| `extension[clinical-trials-count]` | integer | 相關臨床試驗數量 |
| `extension[pubmed-count]` | integer | 相關 PubMed 文獻數量 |

---

### 3. Bundle（全部資料）

一次取得所有預測資料。

**端點**：
```
GET /fhir/Bundle/all-predictions.json
```

**回應結構**：
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

## 證據等級定義

| 等級 | 定義 | 說明 |
|------|------|------|
| **L1** | 多個 Phase 3 RCT | 最高證據，多個大型隨機對照試驗 |
| **L2** | 單一 Phase 3 或多個 Phase 2 | 有臨床試驗支持 |
| **L3** | Phase 1/2 或大量文獻 | 早期臨床證據 |
| **L4** | 動物/體外研究 | 臨床前證據 |
| **L5** | 僅模型預測 | 無臨床證據，僅 AI 預測 |

---

## 使用範例

### JavaScript (前端)

```javascript
async function getDrugPredictions(drugSlug) {
  const response = await fetch(
    `https://thtxgnn.yao.care/fhir/MedicationKnowledge/${drugSlug}.json`
  );
  const drug = await response.json();

  // 取得預測適應症
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

    # 取得藥物資訊
    drug = requests.get(f"{base_url}/MedicationKnowledge/{drug_slug}.json").json()

    # 取得預測適應症
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
# 取得 Metformin 藥物資訊
curl -s https://thtxgnn.yao.care/fhir/MedicationKnowledge/metformin.json | jq .

# 取得特定預測
curl -s https://thtxgnn.yao.care/fhir/ClinicalUseDefinition/metformin-breast-carcinoma.json | jq .

# 取得全部資料
curl -s https://thtxgnn.yao.care/fhir/Bundle/all-predictions.json | jq .total
```

---

## 整合建議

### 對於 SMART on FHIR App

1. 在 SMART App 中呼叫 ThTxGNN API 補充老藥新用資訊
2. 使用 `MedicationKnowledge.code.coding[0].code` (DrugBank ID) 進行藥物映射
3. 顯示 `ClinicalUseDefinition.extension[evidence-level]` 作為信心指標

### 對於後端系統

1. 定期快取 `/fhir/Bundle/all-predictions.json`（建議每日更新）
2. 建立 DrugBank ID → ThTxGNN slug 映射表
3. 整合至現有臨床決策支援系統

---

## 限制與免責

1. **僅供研究參考**：預測結果不構成醫療建議
2. **靜態資料**：資料每月更新一次
3. **無即時 API**：為靜態 JSON 檔案，無查詢功能
4. **英文資料**：藥物和疾病名稱為英文

---

## 聯絡資訊

- **網站**：https://thtxgnn.yao.care/
- **GitHub**：https://github.com/yao-care/ThTxGNN
- **API 狀態**：https://thtxgnn.yao.care/fhir/metadata

---

<div class="disclaimer">
<strong>免責聲明</strong>：本 API 提供的資料僅供研究參考，不能取代專業醫療建議。所有藥物再利用預測結果需經過臨床驗證才能應用。
</div>
