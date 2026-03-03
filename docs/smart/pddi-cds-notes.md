---
layout: default
title: HL7 PDDI-CDS IG 技術筆記
parent: SMART on FHIR
nav_order: 13
---

# HL7 PDDI-CDS Implementation Guide 技術筆記

本文件整理 HL7 Potential Drug-Drug Interaction Clinical Decision Support (PDDI-CDS) Implementation Guide 的關鍵概念，供 ThTxGNN 整合 DDI 警示功能參考。

---

## 概覽

| 項目 | 內容 |
|------|------|
| **全名** | Potential Drug-Drug Interaction Clinical Decision Support |
| **HL7 頁面** | http://hl7.org/fhir/uv/pddi/ |
| **GitHub** | https://github.com/HL7/PDDI-CDS |
| **授權** | CC0-1.0（公共領域） |
| **目的** | 提高 DDI 警示的臨床相關性和特異性 |

---

## 問題背景

現有的 PDDI 警示系統存在以下問題：

- **過度敏感**：簡單的成對藥物比較導致大量誤報
- **警示疲勞**：研究發現近乎所有 PDDI 警示都被忽略
- **缺乏情境**：未考慮病患特定條件（如腎功能、年齡）

PDDI-CDS IG 透過以下方式解決：

1. **最小資訊模型**：定義 DDI 警示必須包含的資訊元素
2. **分級回應**：根據臨床情境調整警示嚴重程度
3. **可分享 artifacts**：使用標準化的 CQL + FHIR + CDS Hooks

---

## 核心組件

### 1. CDS Hooks 整合

| Hook | 觸發時機 | 用途 |
|------|----------|------|
| `order-select` | 醫師選擇藥物時 | 早期檢測，提供建議 |
| `order-sign` | 醫師簽署處方時 | 最終確認，提供詳細資訊 |

**流程**：

```
EHR → order-select hook → CDS 服務 → 檢測 PDDI → 回傳 Card
                                            ↓
                                      醫師選擇動作
                                            ↓
EHR → order-sign hook → CDS 服務 → 提供詳細建議 → 回傳 Card
```

### 2. PlanDefinition 結構

PlanDefinition 是 PDDI-CDS artifacts 的核心資源：

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

### 3. CQL 程式庫範例

```cql
library Warfarin_NSAIDs_CDS version '1.0.0'

using FHIR version '4.0.1'
include FHIRHelpers version '4.0.1'

context Patient

// 術語定義
valueset "Warfarins": 'http://example.org/fhir/ValueSet/warfarins'
valueset "NSAIDs": 'http://example.org/fhir/ValueSet/nsaids'

// 檢測邏輯
define "Is On Warfarin":
  exists([MedicationRequest: "Warfarins"] M
    where M.status = 'active')

define "Is On NSAID":
  exists([MedicationRequest: "NSAIDs"] M
    where M.status = 'active')

define "Inclusion Criteria":
  "Is On Warfarin" and "Is On NSAID"

// 動態訊息
define "Get Detail":
  if "Has GI Risk Factors" then
    'HIGH RISK: Patient has GI risk factors. Consider alternatives.'
  else
    'MODERATE RISK: Monitor for signs of bleeding.'
```

### 4. Response Card 結構

CDS 服務回傳 CDS Hooks Card：

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

### 5. DetectedIssue 資源

用於記錄 PDDI 檢測結果和醫師回應：

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

## 實作層級

| 層級 | 要求 | ThTxGNN 建議 |
|------|------|-------------|
| **Level 1** | 基本 PDDI 檢測 + DetectedIssue 儲存 | 目前目標 |
| **Level 2** | + 情境化篩選（年齡、腎功能等） | 未來擴展 |
| **Level 3** | + 共同決策介面 + 替代建議 | 長期目標 |

---

## ThTxGNN 整合方案

### Phase 1：基礎警示

1. **實作 CDS Hooks 端點**
   - 支援 `order-select` 觸發
   - 回傳 Warning/Info Card

2. **使用現有 DDI 資料**
   - DDInter: 222,391 筆
   - GtoPdb: 4,636 筆

3. **基本 Card 設計**
   ```
   ⚠️ DDI Warning: Warfarin + Ibuprofen
   Bleeding risk increased 3-4x.
   [View Evidence] [Dismiss]
   ```

### Phase 2：情境化

1. **整合病患資料**
   - 年齡、腎功能、病史
   - 調整警示嚴重程度

2. **CQL 邏輯**
   - 實作風險分層規則
   - 根據情境客製化訊息

### Phase 3：老藥新用整合

1. **替代建議**
   - 當 DDI 發生時，建議 ThTxGNN 預測的替代藥物

2. **共同決策**
   - 提供風險/效益比較
   - 支援臨床決策

---

## 範例 DDI 規則（ThTxGNN）

### Warfarin + NSAID

```cql
library ThTxGNN_DDI_Warfarin_NSAID version '1.0.0'

using FHIR version '4.0.1'

context Patient

// 定義
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

// ThTxGNN 整合：替代建議
define "Alternative Analgesic Candidates":
  // 查詢 ThTxGNN 預測：哪些藥物可替代 NSAID 用於疼痛
  // 且不會與 Warfarin 交互
  null // 實際實作時連接 ThTxGNN API
```

---

## 待辦事項

- [ ] 設計 ThTxGNN CDS Hooks 服務架構
- [ ] 建立 Warfarin + NSAID 範例實作
- [ ] 整合現有 DDI 資料到 CQL 值集
- [ ] 設計 Card UI 元件
- [ ] 實作 DetectedIssue 儲存（可選）

---

## 參考資源

- [HL7 PDDI-CDS IG](http://hl7.org/fhir/uv/pddi/)
- [GitHub: HL7/PDDI-CDS](https://github.com/HL7/PDDI-CDS)
- [CDS Hooks 規範](https://cds-hooks.org/)
- [PubMed: Implementation of CDS Services for PDDI](https://pubmed.ncbi.nlm.nih.gov/31438019/)

---

*建立日期：2026-03-01*
