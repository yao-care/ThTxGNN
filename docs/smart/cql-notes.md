---
layout: default
title: CQL 語法學習筆記
parent: SMART on FHIR
nav_order: 12
---

# CQL (Clinical Quality Language) 學習筆記

本文件整理 CQL 語法基礎，供 ThTxGNN 設計臨床決策支援規則參考。

---

## CQL 概覽

| 項目 | 內容 |
|------|------|
| **全名** | Clinical Quality Language |
| **用途** | 臨床品質測量 (CQM) + 臨床決策支援 (CDS) |
| **規範版本** | v1.5.3 (Normative)、v2.0.0 (Ballot) |
| **與 FHIRPath 關係** | CQL 是 FHIRPath 的超集 |
| **執行引擎** | cql-execution (JavaScript)、HAPI FHIR (Java) |

---

## 基本結構

### Library 宣告

```cql
library ThTxGNNCommons version '1.0.0'

using FHIR version '4.0.1'

include FHIRHelpers version '4.0.1' called FHIRHelpers

context Patient
```

| 語法 | 說明 |
|------|------|
| `library` | 程式庫名稱和版本 |
| `using` | 資料模型（FHIR R4） |
| `include` | 引用其他 CQL 程式庫 |
| `context` | 執行情境（Patient 或 Population） |

---

## 資料類型

### 基本類型

| 類型 | 範例 |
|------|------|
| **Boolean** | `true`, `false`, `null` |
| **Integer** | `16`, `-28` |
| **Decimal** | `100.015` |
| **String** | `'pending'`, `'active'` |
| **Date** | `@2014-01-25` |
| **DateTime** | `@2014-01-25T14:30:14.559` |
| **Time** | `@T12:00` |

### 臨床類型

| 類型 | 範例 |
|------|------|
| **Quantity** | `6 'gm/cm3'` |
| **Code** | `Code '442487003' from "SNOMED"` |
| **ValueSet** | `valueset "Diabetes": 'urn:oid:...'` |
| **Interval** | `Interval[@2013-01-01, @2014-01-01)` |

---

## 資料檢索 (Retrieve)

### 基本語法

```cql
[Condition: "Diabetes"]
[MedicationRequest: "Metformin"]
[Encounter: "Ambulatory Visit"]
```

### 篩選條件

```cql
[MedicationRequest: medication in "Antidiabetic Medications"]
  where status = 'active'
```

---

## 查詢 (Query)

### 完整語法

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

### 子句順序

| 順序 | 子句 | 說明 |
|------|------|------|
| 1 | `with/without` | 關聯條件 |
| 2 | `where` | 篩選條件 |
| 3 | `return` | 回傳欄位 |
| 4 | `sort` | 排序 |

---

## 定義表達式 (Define)

```cql
define "PatientHasDiabetes":
  exists([Condition: "Diabetes"] D
    where D.clinicalStatus ~ "Active")

define "CurrentMedications":
  [MedicationRequest] M
    where M.status = 'active'
```

---

## 函數 (Function)

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

## 參數 (Parameter)

```cql
parameter MeasurementPeriod Interval<DateTime>
  default Interval[@2026-01-01T00:00:00.0, @2027-01-01T00:00:00.0)

parameter DrugList List<Code>
```

---

## ThTxGNN 應用範例

### 定義：取得病患目前用藥

```cql
library ThTxGNNDrugRepurposing version '1.0.0'

using FHIR version '4.0.1'
include FHIRHelpers version '4.0.1'

context Patient

// 取得目前有效的用藥
define "ActiveMedications":
  [MedicationRequest] M
    where M.status = 'active'
      and M.intent = 'order'

// 取得藥物名稱清單
define "MedicationNames":
  "ActiveMedications" M
    return FHIRHelpers.ToConcept(M.medication as CodeableConcept).display
```

### 定義：DDI 檢查邏輯

```cql
// 檢查是否有 Warfarin + NSAID 併用
define "WarfarinPlusNSAID":
  exists([MedicationRequest: "Warfarin"] W
    where W.status = 'active')
  and exists([MedicationRequest: "NSAIDs"] N
    where N.status = 'active')

// DDI 警示訊息
define "DDIAlertMessage":
  if "WarfarinPlusNSAID" then
    'WARNING: Concurrent use of Warfarin and NSAIDs increases bleeding risk.'
  else
    null
```

### 定義：老藥新用候選篩選

```cql
// 參數：ThTxGNN 預測分數門檻
parameter PredictionScoreThreshold Decimal default 0.9

// 定義：高信心度候選
define "HighConfidenceCandidates":
  "DrugRepurposingPredictions" P
    where P.score >= PredictionScoreThreshold
      and P.evidenceLevel in {'L1', 'L2', 'L3'}
```

---

## 值集 (ValueSet) 定義

```cql
// 使用 OID 參照外部值集
valueset "Diabetes Medications":
  'http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.113883.3.464.1003.196.12.1001'

// 使用 SNOMED CT 代碼
codesystem "SNOMED": 'http://snomed.info/sct'
code "Type 2 Diabetes": '44054006' from "SNOMED" display 'Type 2 diabetes mellitus'

// 使用 RxNorm 代碼
codesystem "RxNorm": 'http://www.nlm.nih.gov/research/umls/rxnorm'
code "Metformin": '6809' from "RxNorm" display 'Metformin'
```

---

## 執行引擎整合

### JavaScript (cql-execution)

```javascript
const cql = require('cql-execution');
const cqlfhir = require('cql-exec-fhir');

// 載入 ELM JSON（CQL 編譯結果）
const elmJson = require('./ThTxGNNCommons.json');

// 建立病患資料來源
const patientSource = cqlfhir.PatientSource.FHIRv401();
patientSource.loadBundles([patientBundle]);

// 執行 CQL
const executor = new cql.Executor(new cql.Library(elmJson));
const results = await executor.exec(patientSource);

console.log(results.patientResults);
```

### CQL → ELM 編譯

```bash
# 安裝 CQL-to-ELM translator
npm install cql-to-elm

# 編譯 CQL 為 ELM JSON
cql-to-elm -i ThTxGNNCommons.cql -o ThTxGNNCommons.json
```

---

## 學習資源

- [CQL 規範](https://cql.hl7.org/) - 官方完整規範
- [Author's Guide](https://cql.hl7.org/02-authorsguide.html) - 入門指南
- [Developer's Guide](https://cql.hl7.org/03-developersguide.html) - 開發者指南
- [cqframework/clinical_quality_language](https://github.com/cqframework/clinical_quality_language) - 官方工具
- [Cooking with CQL](https://github.com/cqframework/CQL-Formatting-and-Usage-Wiki/wiki/Cooking-with-CQL-Examples) - 範例集

---

## 待辦事項

- [ ] 建立 ThTxGNNCommons.cql 基礎函式庫
- [ ] 定義藥物名稱值集
- [ ] 實作 DDI 檢查規則
- [ ] 整合 cql-execution 引擎
- [ ] 設計老藥新用決策邏輯

---

*建立日期：2026-03-01*
