---
layout: default
title: 可整合應用程式評估
parent: SMART on FHIR
nav_order: 6
---

# SMART App Gallery 可整合應用程式評估

本文件整理自 [SMART App Gallery](https://apps.smarthealthit.org/) 的 144 個應用程式，篩選出可為 ThTxGNN「老藥新用」功能提供補充參考資料的免費/開源應用程式。

**評估日期**：2026-03-01
**評估標準**：與老藥新用相關 + 免費/開源
**評估結果**：20 個應用程式

---

## 評估背景

### ThTxGNN 核心功能

**老藥新用（Drug Repurposing）**：使用 TxGNN 知識圖譜預測已核准藥物的新適應症

### 補充參考資料需求

| 補充資訊類型 | 用途 |
|-------------|------|
| DDI 警示 | 推薦新適應症時，需確認無危險交互作用 |
| 臨床試驗 | 驗證老藥新用候選是否有進行中的試驗 |
| 藥物基因組學 | 特定基因型患者的藥物反應 |
| 疾病資訊 | 目標疾病的詳細資訊 |
| 藥物使用/依從性 | 藥物在真實世界的使用情況 |

---

## 整合後運作流程

以下流程圖說明 ThTxGNN 如何整合外部 SMART App 提供補充參考資料：

```
┌─────────────────────────────────────────────────────────────────────┐
│                           EHR 系統                                                │
│  ┌──────────────┐      ┌─────────────────────────────────────────┐    │
│  │   病患資料      │ ───►│  MedicationRequest / MedicationStatement        │    │
│  └──────────────┘      └─────────────────────────────────────────┘    │
└───────────────────────────────────┬─────────────────────────────────┘
                                            │ FHIR R4
                                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      ThTxGNN SMART App                               │
│                                                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌───────────────────────┐  │
│  │SMART on FHIR │───►│ 讀取病患用藥  │───►│ 老藥新用預測引擎       │  │
│  │    啟動      │    │              │    │ (TxGNN 知識圖譜)      │  │
│  └──────────────┘    └──────────────┘    └───────────┬───────────┘  │
│                                                      │              │
│                                          ┌───────────▼───────────┐  │
│                                          │    候選適應症清單      │  │
│                                          └───────────┬───────────┘  │
└──────────────────────────────────────────────────────┼──────────────┘
                                                       │
                       ┌───────────────────────────────┼───────────────────────────────┐
                       │                               │                               │
                       ▼                               ▼                               ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                                    補充參考資料查詢層                                         │
│                                                                                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐         │
│  │    DDI 檢查     │  │    臨床試驗     │  │    疾病資訊     │  │    風險評估     │         │
│  │ ─────────────── │  │ ─────────────── │  │ ─────────────── │  │ ─────────────── │         │
│  │ • DDInter       │  │ • Clinical      │  │ • Diabetes      │  │ • CRC SCORE*    │         │
│  │ • GtoPdb        │  │   Trials        │  │   Monograph*    │  │ • Sepsis Watch* │         │
│  │ • DDI-CDS*      │  │   Search*       │  │ • ClinDat*      │  │ • GrowSmart*    │         │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘         │
│           │                    │                    │                    │                  │
└───────────┼────────────────────┼────────────────────┼────────────────────┼──────────────────┘
            │                    │                    │                    │
            └────────────────────┴──────────┬─────────┴────────────────────┘
                                            │
                                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         整合呈現介面                                 │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │  候選藥物: Metformin                                           │ │
│  │  預測適應症: 乳癌                                              │ │
│  │  ────────────────────────────────────────────────────────────  │ │
│  │  ⚠️  DDI 警示:  與病患目前用藥無嚴重交互作用                    │ │
│  │  📋 臨床試驗:  3 個進行中 (Phase II: 2, Phase III: 1)          │ │
│  │  📊 風險評估:  病患 10 年癌症風險: 中等                         │ │
│  └────────────────────────────────────────────────────────────────┘ │
└───────────────────────────────────┬─────────────────────────────────┘
                                    │
                                    ▼
                        ┌───────────────────────┐
                        │      臨床決策         │
                        │     (醫師判斷)        │
                        └───────────────────────┘

* = SMART App Gallery 候選應用程式
```

### 流程說明

| 階段 | 說明 | 資料來源 |
|------|------|----------|
| **1. EHR 啟動** | 臨床人員從 EHR 選擇病患，啟動 ThTxGNN SMART App | EHR 系統 |
| **2. 讀取用藥** | 透過 FHIR API 讀取病患目前用藥 | MedicationRequest |
| **3. 老藥新用預測** | 將用藥映射到知識圖譜，查詢候選適應症 | TxGNN + DrugBank |
| **4. 補充資料查詢** | 對每個候選查詢 DDI、臨床試驗、疾病資訊、風險評估 | 內部資料 + 外部 SMART App |
| **5. 整合呈現** | 將所有資訊整合呈現，輔助臨床決策 | 整合層 |

---

## 評估結果：20 個免費/開源應用程式

### 1. DDI / 藥物交互作用（3 個）

| # | 應用名稱 | 開發者 | FHIR | 補充價值 | 整合方向 | GitHub |
|---|---------|--------|------|----------|----------|--------|
| 1 | **Colchicine DDI-CDS App** | DDI-CDS.org | R4 | 秋水仙鹼與 CYP3A4/PGP 抑制劑的交互作用警示 | 當預測候選藥物為秋水仙鹼時，提示交互作用風險 | 無 |
| 2 | **DDInteract** | DDI-CDS.org | R4 | 華法林 + NSAIDs 出血風險的共同決策工具 | 當預測涉及抗凝血藥物時，提示出血風險 | 無 |
| 3 | **Tizanidine DDI-CDS App** | DDI-CDS.org | R4 | 替扎尼定與 CYP1A2 抑制劑的交互作用警示 | 當預測候選藥物為替扎尼定時，提示交互作用風險 | 無 |

**整合建議**：
- ThTxGNN 已有 DDInter + Guide to PHARMACOLOGY 的 DDI 資料
- 可參考 DDI-CDS 的**警示設計模式**和**視覺化呈現方式**
- 這 3 個 App 展示了如何將 DDI 資訊整合到臨床決策流程中
- AHRQ 資助的學術專案

---

### 2. 臨床試驗（1 個）

| # | 應用名稱 | 開發者 | FHIR | 補充價值 | 整合方向 | GitHub |
|---|---------|--------|------|----------|----------|--------|
| 4 | **Clinical Trials Search** | ShutdownHook | DSTU2, R4 | 根據患者條件搜尋匹配的臨床試驗 | 當顯示老藥新用候選時，連結「正在進行的相關臨床試驗」作為驗證依據 | [有](https://github.com/seanno/shutdownhook/tree/main/smart-trials) |

**整合建議**：
- **高價值整合**：當 ThTxGNN 預測藥物 X 可用於疾病 Y，可顯示「藥物 X + 疾病 Y 的臨床試驗」
- 提供「驗證途徑」給使用者，增加預測的可信度
- MIT 授權，程式碼可直接參考
- 支援 Epic/Cerner

---

### 3. 藥物基因組學（1 個）

| # | 應用名稱 | 開發者 | FHIR | 補充價值 | 整合方向 | GitHub |
|---|---------|--------|------|----------|----------|--------|
| 5 | **NGS Quality Reporting** | Samsung Medical Center | R4 | 新一代基因測序品質報告 | 若未來整合基因組資料，可參考此 App 的 FHIR 基因組資源處理方式 | [有](https://github.com/dhseong/ngs-qr-app-client) |

**整合建議**：
- 目前 ThTxGNN 未使用基因組資料，但未來若要擴展到「精準老藥新用」可參考
- 了解 FHIR 如何表達基因組資料
- 韓國三星醫學中心開發

---

### 4. 藥物資訊 / 用藥管理（4 個）

| # | 應用名稱 | 開發者 | FHIR | 補充價值 | 整合方向 | GitHub |
|---|---------|--------|------|----------|----------|--------|
| 6 | **CDS Connect: Pain Management** | AHRQ/MITRE | DSTU2, R4 | 疼痛管理儀表板，含鴉片類+苯二氮卓類警示 | 參考 CQL 邏輯架構，設計老藥新用的 CDS 規則 | [有](https://github.com/AHRQ-CDS/AHRQ-CDS-Connect-PAIN-MANAGEMENT-SUMMARY) |
| 7 | **COSRI** | U of Washington | R4 | 鴉片類藥物摘要 + PDMP 資料整合 | 參考多資料源整合模式（EHR + 外部資料庫） | [專案網站](https://project.cosri.app) |
| 8 | **MPR Monitor** | Boston Children's | DSTU2 | 根據處方/配藥歷史預測藥物依從性 | 當推薦老藥新用時，可參考患者對類似藥物的依從性歷史 | [有](https://github.com/smart-on-fhir/mpr-monitor-app) |
| 9 | **Meds Price Compare** | Technosoft | DSTU2 | 處方藥價格比較與優惠券 | 當推薦老藥新用時，可顯示藥物價格資訊 | 無 |

**整合建議**：
- **CDS Connect** 是最有價值的參考：展示如何用 CQL 定義臨床邏輯，Apache 2.0 授權，React + CQL 架構
- **COSRI** 展示如何整合外部資料源（PDMP）到 SMART App，Apache 2.0 授權，華盛頓州衛生部合作
- **MPR Monitor** 的依從性預測可作為「推薦理由」的補充資訊，波士頓兒童醫院演算法

---

### 5. 疾病管理（5 個）

| # | 應用名稱 | 開發者 | FHIR | 補充價值 | 整合方向 | GitHub |
|---|---------|--------|------|----------|----------|--------|
| 10 | **Lupus Advisor** | Aditus | R4 | 狼瘡照護自動化 EHR 輔助 | 當預測藥物用於自體免疫疾病時，參考疾病管理模式 | 無 |
| 11 | **Diabetes Monograph** | Boston Children's | DSTU2 | 糖尿病專用單圖檢視 | 參考「疾病專用檢視」的 UI 設計 | [有](https://github.com/smart-on-fhir/diabetes-monograph-app) |
| 12 | **RTI Wellmine** | RTI International | R4 | 罕見疾病患者數據收集 | 若擴展到罕見疾病的老藥新用，可參考 | 無 |
| 13 | **Major Depression Outcomes** | OM1 | DSTU2, STU3, R4 | PHQ-9 抑鬱症評分歷史追蹤 | 當預測藥物用於精神疾病時，參考療效追蹤模式 | 無 |
| 14 | **ClinDat** | Health Report Services | DSTU2 | 風濕性疾病症狀監測與評分 | 當預測藥物用於風濕疾病時，參考症狀評估模式 | 無 |

**整合建議**：
- **Diabetes Monograph** 展示如何設計「疾病專用檢視」，ThTxGNN 可為每個目標疾病設計類似檢視
- 疾病管理 App 提供「目標疾病」的詳細資訊，可作為老藥新用推薦時的背景說明
- Partners HealthCare 設計

---

### 6. 癌症 / 腫瘤（1 個）

| # | 應用名稱 | 開發者 | FHIR | 補充價值 | 整合方向 | GitHub |
|---|---------|--------|------|----------|----------|--------|
| 15 | **SMART Precision Cancer Medicine** | Vanderbilt | DSTU2 | 比較患者體細胞突變與人群數據 | 當預測藥物用於癌症時，整合基因突變資訊 | 無 |

**整合建議**：
- 癌症老藥新用是熱門領域，此 App 展示如何將基因突變與藥物選擇連結
- 可參考其「藥物-突變」關聯的呈現方式
- 支援 Epic, Cerner, Allscripts, Athena Health

---

### 7. 風險計算 / 預測（5 個）

| # | 應用名稱 | 開發者 | FHIR | 補充價值 | 整合方向 | GitHub |
|---|---------|--------|------|----------|----------|--------|
| 16 | **CRC SCORE** | Gradiant | DSTU2, STU3 | 結直腸癌風險預測（FAST/COLONPREDICT 模型） | 當預測藥物用於癌症預防時，參考風險分層 | 無 |
| 17 | **Sepsis Watch** | GA Tech/Emory | STU3 | 敗血症預測（預測 6 項實驗室數值） | 當預測藥物用於感染/敗血症時，參考病情預測 | 無 |
| 18 | **Stone LogiK** | Translational Analytics | DSTU2, STU3 | 尿石症治療成功率預測 | 展示如何預測「治療成功率」，可參考應用於老藥新用 | 無 |
| 19 | **CHF Predictive Analytics** | SFO Technologies | DSTU2 | 慢性心臟衰竭風險（30天/1年死亡率） | 當預測藥物用於心臟疾病時，參考風險分層 | 無 |
| 20 | **GrowSmart** | U Delaware & Nemours | R4 | 兒童肥胖風險預測（1-3年） | 當預測藥物用於代謝疾病時，參考風險預測模式 | 無 |

**整合建議**：
- 這些 App 展示如何將「預測模型」整合到臨床決策
- ThTxGNN 的老藥新用預測本質上也是預測模型，可參考其**結果呈現方式**和**信心度表達**

---

## 統計總結

| 類別 | 數量 | 有 GitHub | 最推薦 |
|------|------|-----------|--------|
| DDI / 藥物交互作用 | 3 | 0 | DDInteract（共同決策設計） |
| 臨床試驗 | 1 | 1 | Clinical Trials Search |
| 藥物基因組學 | 1 | 1 | NGS Quality Reporting |
| 藥物資訊/用藥管理 | 4 | 3 | CDS Connect |
| 疾病管理 | 5 | 1 | Diabetes Monograph |
| 癌症/腫瘤 | 1 | 0 | SMART Precision Cancer Medicine |
| 風險計算/預測 | 5 | 0 | Stone LogiK（治療成功率預測） |
| **總計** | **20** | **6** | |

---

## 整合可行性評估結果

以下是針對 20 個應用程式的深入研究結果，評估日期：2026-03-01。

### 可行性評估總表

| # | 應用名稱 | 可行性 | 授權 | 技術相容性 | 整合價值 | 主要障礙 |
|---|---------|--------|------|------------|----------|----------|
| 1 | Colchicine DDI-CDS | 中 | CC BY-NC-SA 3.0 | R4 相容 | 中 | 原始碼未公開 |
| 2 | DDInteract | 中 | CC BY-NC-SA 3.0 | R4 相容 | 高 | 原始碼未公開 |
| 3 | Tizanidine DDI-CDS | 中 | CC BY-NC-SA 3.0 | R4 相容 | 中 | 原始碼未公開 |
| 4 | Clinical Trials Search | **高** | MIT | R4 相容 | **高** | API 需更新至 v2 |
| 5 | NGS Quality Reporting | 中 | MIT | R4 相容 | 中 | 功能領域差異大 |
| 6 | CDS Connect | **高** | Apache 2.0 | R4 相容 | **高** | 需學習 CQL |
| 7 | COSRI | 中 | Apache 2.0 | R4 相容 | 中 | 針對美國法規設計 |
| 8 | MPR Monitor | **低** | Apache 2.0 | DSTU2 過時 | 中 | **已棄用** |
| 9 | Meds Price Compare | **低** | 未知 | DSTU2 過時 | 低 | 功能不相關 |
| 10 | Lupus Advisor | 中 | 未公開 | R4 相容 | 中 | 需取得合作 |
| 11 | Diabetes Monograph | 中 | Apache 2.0 | DSTU2 過時 | 中 | **已棄用** |
| 12 | RTI Wellmine | **高** | 開源 | R4 相容 | **高** | 罕見疾病專用 |
| 13 | Major Depression Outcomes | 中 | 未公開 | R4 相容 | 中 | 需聯繫 OM1 |
| 14 | ClinDat | 中 | 需洽談 | DSTU2 過時 | 中 | 學術合作 |
| 15 | SMART Precision Cancer Medicine | 中 | 開源 | DSTU2 過時 | 中 | 需基因組資料 |
| 16 | CRC SCORE | **低** | 免費 | DSTU2/STU3 | 低 | 功能不相關 |
| 17 | Sepsis Watch | **低** | 免費 | STU3 | 低 | **僅供展示** |
| 18 | Stone LogiK | **低** | 免費 | DSTU2/STU3 | 低 | 功能不相關 |
| 19 | CHF Predictive Analytics | 中 | 免費 | DSTU2 過時 | 中 | 需升級 FHIR |
| 20 | GrowSmart | 中 | 開源 | R4 相容 | 低 | 兒科專用 |

### 可行性分級說明

| 可行性 | 定義 | 數量 |
|--------|------|------|
| **高** | 授權開放、技術相容、整合價值高、可在 1-2 個月內實施 | 3 |
| **中** | 有整合潛力但有障礙（需合作、需升級、需學習新技術） | 12 |
| **低** | 不建議整合（已棄用、功能不相關、僅供展示） | 5 |

### 高可行性應用程式詳細分析

#### 1. Clinical Trials Search (#4)

| 項目 | 內容 |
|------|------|
| **GitHub** | https://github.com/seanno/shutdownhook/tree/main/smart-trials |
| **授權** | MIT（完全開放） |
| **整合價值** | 當 ThTxGNN 預測藥物 X 可用於疾病 Y 時，自動搜尋「藥物 X + 疾病 Y」的臨床試驗作為驗證依據 |
| **技術方案** | 直接在 ThTxGNN SMART App 中整合 ClinicalTrials.gov API v2（JavaScript 前端呼叫） |
| **預估工時** | 2-3 天 |
| **注意事項** | 原始碼使用舊版 API（已於 2024 年退役），需改用 API v2 |

#### 2. CDS Connect: Pain Management (#6)

| 項目 | 內容 |
|------|------|
| **GitHub** | https://github.com/AHRQ-CDS/AHRQ-CDS-Connect-PAIN-MANAGEMENT-SUMMARY |
| **授權** | Apache 2.0（可商業使用） |
| **整合價值** | 提供完整的 CQL 架構參考，可用於設計 ThTxGNN 的臨床決策邏輯 |
| **技術方案** | 參考其 CQL 邏輯架構，不直接整合程式碼 |
| **可借鏡項目** | CQL 共用函式庫、Value Set 管理、ELM 執行流程 |
| **預估工時** | 2-4 週（學習 CQL + 實作） |

#### 3. RTI Wellmine (#12)

| 項目 | 內容 |
|------|------|
| **官網** | https://wellmine.rti.org |
| **授權** | 開源 |
| **整合價值** | 罕見疾病是老藥新用的核心領域，RTI 為非營利研究機構，合作意願高 |
| **技術方案** | 建立 ThTxGNN FHIR API 端點，供 Wellmine 平台查詢老藥新用候選 |
| **預估工時** | 1-2 週（API 開發） |
| **建議行動** | 聯繫 RTI International 探討合作 |

### 不建議整合的應用程式

| # | 應用名稱 | 原因 |
|---|---------|------|
| 8 | MPR Monitor | 已棄用，Django 1.4 有安全漏洞，fhirclient 1.0.2 過時 |
| 9 | Meds Price Compare | 功能與老藥新用無關（藥價比較） |
| 11 | Diabetes Monograph | 已棄用，但 UI 設計模式仍有參考價值 |
| 16 | CRC SCORE | 功能不相關（癌症診斷篩檢而非藥物推薦） |
| 17 | Sepsis Watch | 僅為學術展示專案，非臨床級產品 |
| 18 | Stone LogiK | 功能不相關（泌尿科治療方式選擇） |

### DDI-CDS 系列特別說明

DDI-CDS.org 的 3 個應用程式（#1-3）由 AHRQ 資助的學術團隊開發，雖然原始碼未公開，但：

1. **HL7 PDDI-CDS IG** 採用 CC0-1.0 授權（公共領域），可直接參考實作
2. GitHub 儲存庫：https://github.com/HL7/PDDI-CDS
3. 可聯繫研究團隊（info@ddi-cds.org）請求技術合作

### 技術相容性分析

| FHIR 版本 | 應用數量 | 與 ThTxGNN 相容性 |
|-----------|----------|-------------------|
| R4 | 8 | 完全相容 |
| DSTU2 | 6 | 需版本轉換 |
| STU3 | 3 | 需版本轉換 |
| 多版本支援 | 3 | 部分相容 |

ThTxGNN 使用 FHIR R4，與 8 個應用程式完全相容。

---

## 整合計畫（15 個應用程式）

排除 5 個不建議整合的應用程式後，剩餘 15 個可整合應用程式，分為三個階段執行。

### Phase 1：高可行性（3 個）

預計時程：1-2 個月

| # | 應用名稱 | 整合方式 | 工時 | 產出 |
|---|---------|----------|------|------|
| 4 | **Clinical Trials Search** | 在 ThTxGNN SMART App 整合 ClinicalTrials.gov API v2 | 2-3 天 | 老藥新用候選 + 相關臨床試驗連結 |
| 6 | **CDS Connect** | 參考 CQL 架構設計 ThTxGNN 臨床邏輯 | 2-4 週 | CQL 規則庫 + Value Set 管理 |
| 12 | **RTI Wellmine** | 建立 ThTxGNN FHIR API 供罕見疾病平台查詢 | 1-2 週 | RESTful API 端點 |

#### Phase 1 詳細任務

**#4 Clinical Trials Search**
```
□ 研究 ClinicalTrials.gov API v2 規格
□ 在 smart-app.js 新增 searchClinicalTrials() 函數
□ 建立疾病名稱 → MeSH 術語映射表
□ 設計 UI：在老藥新用結果顯示「相關臨床試驗」區塊
□ 測試與部署
```

**#6 CDS Connect（參考架構）**
```
□ 學習 CQL 語法與 cql-execution 引擎
□ 建立 ThTxGNNCommons.cql 共用函式庫
□ 設計 valueset-db.json（RxNorm、SNOMED CT 對應）
□ 實作 ELM 執行流程
□ 撰寫文件
```

**#12 RTI Wellmine**
```
□ 聯繫 RTI International 探討合作
□ 設計 FHIR API 規格（/DrugRepurposing endpoint）
□ 實作 API 端點
□ 撰寫 API 文件
□ 與 Wellmine 團隊測試整合
```

---

### Phase 2：DDI 整合（3 個）

預計時程：2-3 個月

| # | 應用名稱 | 整合方式 | 工時 | 產出 |
|---|---------|----------|------|------|
| 1 | Colchicine DDI-CDS | 參考 HL7 PDDI-CDS IG 實作 DDI 警示 | 2 週 | 秋水仙鹼 DDI 規則 |
| 2 | DDInteract | 參考共同決策 UI 設計 | 2 週 | 華法林+NSAID 出血風險警示 |
| 3 | Tizanidine DDI-CDS | 整合 CYP1A2 抑制劑檢查 | 1 週 | 替扎尼定 DDI 規則 |

#### Phase 2 詳細任務

```
□ 聯繫 DDI-CDS.org (info@ddi-cds.org) 請求技術合作
□ 研究 HL7 PDDI-CDS Implementation Guide
□ 整合 ThTxGNN 現有 DDI 資料（DDInter + GtoPdb）
□ 實作 CDS Hooks (order-select, order-sign)
□ 設計 DDI 警示 UI
□ 測試與驗證
```

---

### Phase 3：疾病管理與風險評估（9 個）

預計時程：3-6 個月

| # | 應用名稱 | 整合方式 | 優先級 | 備註 |
|---|---------|----------|--------|------|
| 5 | NGS Quality Reporting | 讀取 MolecularSequence 資源 | 中 | 精準老藥新用前置準備 |
| 7 | COSRI | 參考多資料源整合模式 | 中 | 美國法規，需調整 |
| 10 | Lupus Advisor | 聯繫 Aditus 探討合作 | 中 | 自體免疫疾病 |
| 11 | Diabetes Monograph | 參考疾病專用 UI 設計 | 低 | 已棄用，僅參考設計 |
| 13 | Major Depression Outcomes | 聯繫 OM1 探討合作 | 中 | 精神科用藥 |
| 14 | ClinDat | 聯繫 Dr. Ted Pincus | 中 | 風濕科學術合作 |
| 15 | SMART Precision Cancer Medicine | 整合 mCODE 標準 | 中 | 癌症基因組 |
| 19 | CHF Predictive Analytics | 待 FHIR 升級後整合 | 低 | 心衰風險+藥物建議 |
| 20 | GrowSmart | 參考 OMOP-on-FHIR 架構 | 低 | 兒科，未來擴展 |

---

### 整合里程碑

```
2026-Q1 ─────────────────────────────────────────────────────
         [Phase 1]
         □ Clinical Trials Search 整合完成
         □ CQL 架構學習與實作

2026-Q2 ─────────────────────────────────────────────────────
         [Phase 1 續]
         □ RTI Wellmine API 開發
         □ RTI 合作協議

         [Phase 2]
         □ DDI-CDS.org 技術合作
         □ HL7 PDDI-CDS 實作

2026-Q3 ─────────────────────────────────────────────────────
         [Phase 2 續]
         □ DDI 警示功能上線
         □ CDS Hooks 整合

         [Phase 3]
         □ 疾病專用視圖設計
         □ 合作夥伴洽談

2026-Q4 ─────────────────────────────────────────────────────
         [Phase 3 續]
         □ NGS/基因組整合評估
         □ 癌症 mCODE 標準研究
```

---

### 聯繫工作事項

以下為需要聯繫的合作對象及工作事項：

---

#### 工作事項 1：聯繫 RTI International（RTI Wellmine）

**優先級**：高（Phase 1）
**聯繫方式**：https://wellmine.rti.org
**目的**：探討罕見疾病老藥新用合作

**聯繫內容草稿**：

```
Subject: Collaboration Inquiry: Drug Repurposing for Rare Diseases - ThTxGNN x RTI Wellmine

Dear RTI Wellmine Team,

I am writing to explore a potential collaboration between ThTxGNN and RTI Wellmine
for rare disease drug repurposing research.

About ThTxGNN:
- A SMART on FHIR application for drug repurposing predictions
- Based on Harvard's TxGNN knowledge graph model
- Currently covers 677 drugs and 1,035 potential new indications
- Website: https://thtxgnn.yao.care/

Proposed Collaboration:
1. Integrate ThTxGNN drug repurposing API into the Wellmine platform
2. Enable rare disease patients to view potential repurposed drug candidates
3. Facilitate research validation through patient-reported outcomes

We believe this collaboration could accelerate rare disease treatment discovery
while leveraging Wellmine's patient data collection capabilities.

Would you be available for a brief call to discuss this opportunity?

Best regards,
[Your Name]
ThTxGNN Team
```

**待辦事項**：
- [ ] 發送聯繫信件
- [ ] 安排視訊會議
- [ ] 準備技術規格文件
- [ ] 討論 API 整合方案

---

#### 工作事項 2：聯繫 DDI-CDS.org

**優先級**：高（Phase 2）
**聯繫方式**：info@ddi-cds.org
**目的**：請求技術合作或 API 存取

**聯繫內容草稿**：

```
Subject: Technical Collaboration Request: DDI-CDS Integration with ThTxGNN

Dear DDI-CDS Research Team,

I am reaching out regarding a potential technical collaboration for integrating
drug-drug interaction (DDI) alerts into ThTxGNN, a SMART on FHIR drug repurposing
application.

Our Project:
- ThTxGNN: Drug repurposing predictions using TxGNN knowledge graph
- FHIR R4 compatible SMART App
- Currently integrates DDInter and Guide to PHARMACOLOGY DDI data

Collaboration Goals:
1. Reference DDI-CDS alert design patterns for clinical decision support
2. Explore API access or technical documentation sharing
3. Potentially contribute to the HL7 PDDI-CDS Implementation Guide

We are particularly interested in:
- DDInteract's shared decision-making UI design
- Colchicine and Tizanidine DDI algorithms
- CDS Hooks implementation patterns

Would it be possible to schedule a technical discussion?

Best regards,
[Your Name]
ThTxGNN Team
```

**待辦事項**：
- [ ] 發送聯繫信件
- [ ] 研究 HL7 PDDI-CDS IG（CC0 授權）
- [ ] 評估 CDS Hooks 實作需求
- [ ] 準備 DDI 整合技術方案

---

#### 工作事項 3：聯繫 Dr. Ted Pincus（ClinDat）

**優先級**：中（Phase 3）
**聯繫方式**：tedpincus@gmail.com
**目的**：探討風濕科學術合作

**聯繫內容草稿**：

```
Subject: Academic Collaboration: Drug Repurposing for Rheumatic Diseases

Dear Dr. Pincus,

I am writing to explore a potential academic collaboration between ThTxGNN
and your ClinDat rheumatology monitoring platform.

ThTxGNN Overview:
- AI-powered drug repurposing predictions using Harvard's TxGNN model
- SMART on FHIR compatible for EHR integration
- Includes predictions for rheumatoid arthritis, lupus, and other rheumatic conditions

Proposed Collaboration:
1. Integrate drug repurposing candidates when disease activity scores (DAS28/RAPID3)
   indicate inadequate treatment response
2. Provide alternative therapeutic options based on AI predictions
3. Validate predictions through ClinDat's patient outcome data

Given your expertise in RAPID3 and rheumatology outcome measures, we believe
this collaboration could benefit patients with treatment-resistant rheumatic diseases.

Would you be interested in discussing this further?

Best regards,
[Your Name]
ThTxGNN Team
```

**待辦事項**：
- [ ] 發送聯繫信件
- [ ] 整理 ThTxGNN 風濕疾病相關預測資料
- [ ] 準備學術合作提案
- [ ] 安排視訊會議

---

#### 工作事項 4：聯繫 Aditus（Lupus Advisor）

**優先級**：中（Phase 3）
**聯繫方式**：https://www.lupusadvisor.com/
**目的**：探討狼瘡照護整合

**聯繫內容草稿**：

```
Subject: Integration Inquiry: ThTxGNN Drug Repurposing for Lupus Care

Dear Aditus Team,

I am exploring a potential integration between ThTxGNN and Lupus Advisor
to enhance clinical decision support for systemic lupus erythematosus (SLE) patients.

ThTxGNN Capabilities:
- Drug repurposing predictions based on TxGNN knowledge graph
- SMART on FHIR R4 compatible
- Includes lupus-related drug candidates

Integration Proposal:
- Display drug repurposing candidates within Lupus Advisor workflow
- Complement ACR/EULAR guideline recommendations with AI predictions
- Provide alternative therapeutic options for refractory cases

As both applications use FHIR R4, technical integration should be straightforward.

Would you be open to discussing a pilot integration?

Best regards,
[Your Name]
ThTxGNN Team
```

**待辦事項**：
- [ ] 透過官網聯繫表單發送
- [ ] 整理狼瘡相關藥物預測
- [ ] 準備整合技術方案

---

#### 工作事項 5：聯繫 OM1（Major Depression Outcomes）

**優先級**：中（Phase 3）
**聯繫方式**：透過 SMART App Gallery 聯繫
**目的**：探討精神科用藥合作

**聯繫內容草稿**：

```
Subject: Collaboration Inquiry: Drug Repurposing for Depression Treatment

Dear OM1 Team,

I am writing regarding a potential collaboration between ThTxGNN and your
Major Depression Outcomes application.

Proposed Integration:
- When PHQ-9 scores indicate inadequate treatment response, suggest
  drug repurposing candidates as alternative therapeutic options
- Integrate AI predictions into the outcomes dashboard
- Support shared decision-making with evidence-based alternatives

ThTxGNN includes predictions for major depressive disorder and related
psychiatric conditions.

Would you be interested in exploring this integration?

Best regards,
[Your Name]
ThTxGNN Team
```

**待辦事項**：
- [ ] 透過 SMART App Gallery 聯繫
- [ ] 整理精神疾病相關藥物預測
- [ ] 評估精神科用藥安全性考量
- [ ] 準備免責聲明

---

### 工作事項總覽

| # | 聯繫對象 | 優先級 | 狀態 | 預計完成 |
|---|----------|--------|------|----------|
| 1 | RTI International | 高 | 待聯繫 | 2026-Q1 |
| 2 | DDI-CDS.org | 高 | 待聯繫 | 2026-Q1 |
| 3 | Dr. Ted Pincus | 中 | 待聯繫 | 2026-Q2 |
| 4 | Aditus | 中 | 待聯繫 | 2026-Q2 |
| 5 | OM1 | 中 | 待聯繫 | 2026-Q3 |

---

### 技術準備工作事項

在聯繫合作夥伴前，需完成以下技術準備：

| # | 工作事項 | 產出 | 狀態 | 優先級 |
|---|----------|------|------|--------|
| T1 | 建立 ThTxGNN FHIR API 規格文件 | [api-spec.md](api-spec) | 已完成 | 高 |
| T2 | 準備英文版專案簡介 | [project-intro-en.md](project-intro-en) | 已完成 | 高 |
| T3 | 整理各疾病領域藥物預測統計 | 見下方統計表 | 已完成 | 高 |
| T4 | 研究 ClinicalTrials.gov API v2 | [clinicaltrials-api-notes.md](clinicaltrials-api-notes) | 已完成 | 高 |
| T5 | 學習 CQL 語法基礎 | [cql-notes.md](cql-notes) | 已完成 | 中 |
| T6 | 研究 HL7 PDDI-CDS IG | [pddi-cds-notes.md](pddi-cds-notes) | 已完成 | 中 |
| T7 | 設計 CDS Hooks 架構 | [cds-hooks-architecture.md](cds-hooks-architecture) | 已完成 | 中 |

---

### T3 產出：各疾病領域藥物預測統計

以下統計基於 search-index.json（189 藥物、704 適應症）：

#### 疾病領域分布

| 疾病領域 | 涉及藥物數 | 預測適應症數 | L1-L2 預測 | L3-L4 預測 | L5 預測 |
|----------|-----------|-------------|-----------|-----------|---------|
| Oncology | 38 | 103 | 36 | 42 | 91 |
| Rare Diseases | 101 | 101 | 7 | 25 | 159 |
| Gastrointestinal | 27 | 28 | 6 | 19 | 26 |
| Cardiology | 20 | 26 | 6 | 20 | 23 |
| Respiratory | 28 | 24 | 14 | 19 | 18 |
| Neurology | 23 | 22 | 3 | 15 | 25 |
| Dermatology | 26 | 20 | 8 | 12 | 26 |
| Ophthalmology | 20 | 17 | 3 | 14 | 16 |
| Autoimmune | 17 | 16 | 4 | 6 | 11 |
| Infectious | 16 | 12 | 6 | 4 | 14 |
| Metabolic | 13 | 8 | 4 | 3 | 12 |
| Psychiatric | 14 | 8 | 1 | 7 | 8 |

**注意**：未分類適應症數量 360 個。一個適應症可能同時屬於多個領域。

#### 證據等級分布

| 等級 | 藥物數 | 適應症數 |
|------|--------|----------|
| L1 | 49 | 68 |
| L2 | 18 | 50 |
| L3 | 31 | 64 |
| L4 | 54 | 193 |
| L5 | 37 | 492 |

#### 合作對象領域對應

| 合作對象 | 相關疾病領域 | ThTxGNN 資料量 |
|----------|-------------|----------------|
| RTI Wellmine | Rare Diseases | 101 藥物、101 適應症 |
| DDI-CDS.org | 所有領域（DDI 警示） | 222,391 筆 DDI |
| Dr. Ted Pincus (ClinDat) | Autoimmune | 17 藥物、16 適應症 |
| Aditus (Lupus Advisor) | Autoimmune | 17 藥物、16 適應症 |
| OM1 (Depression) | Psychiatric | 14 藥物、8 適應症 |

---

## 資料來源

- SMART App Gallery: https://apps.smarthealthit.org/
- 評估日期: 2026-03-01
- 總應用數: 144
- 篩選結果: 20 個免費/開源應用程式

---

## 待專家審閱事項

1. 上述 20 個應用程式的補充價值評估是否正確？
2. 整合優先順序是否合理？
3. 是否有遺漏的重要應用程式？
4. 是否有其他整合方向建議？

---

<div class="disclaimer">
<strong>免責聲明</strong>：本文件僅整理公開資訊供內部參考，不構成對任何應用程式的推薦或背書。
</div>
