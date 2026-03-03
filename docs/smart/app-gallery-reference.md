---
layout: default
title: SMART App Gallery 參考
parent: SMART on FHIR
nav_order: 5
---

# SMART App Gallery 應用程式參考

本文件整理自 [SMART App Gallery](https://apps.smarthealthit.org/apps?sort=name-asc)，共收錄 143 個 SMART on FHIR 應用程式，供 ThTxGNN 服務升級參考。

**資料擷取日期**：2026-02-27

---

## 目錄

- [依功能類別分類](#依功能類別分類)
- [依 FHIR 版本分類](#依-fhir-版本分類)
- [完整應用程式列表](#完整應用程式列表)
- [值得參考的功能亮點](#值得參考的功能亮點)

---

## 依功能類別分類

### 風險計算 (Risk Calculation)

| 應用名稱 | 開發者 | 功能 | FHIR |
|---------|--------|------|------|
| ASCVD Risk Calculator | Cerner | 10年/終身心血管風險評分 | DSTU2 |
| BP Centiles v1/v2 | Boston Children's / Interopion | 兒童血壓百分位數計算 | DSTU2 |
| Cardiac Risk | Boston Children's | 雷諾茲風險評分（心臟病/中風） | DSTU2 |
| CHF Predictive Analytics | SFO Technologies | 慢性心臟衰竭風險辨識 | DSTU2 |
| CRC SCORE | Gradiant | 結直腸癌檢測預測 | DSTU2, STU3 |
| Diabetes Predictive Analytics | SFO Technologies | 第2型糖尿病風險計算 | DSTU2 |
| GrowSmart | U Delaware & Nemours | 兒童肥胖症風險預測（1-3年） | R4 |
| HealthConnect: AI Cardiovascular Risk | Mindbowser | AI心血管風險評估 | R4 |
| HEART Pathway | Impathiq | 胸痛患者決策工具 | DSTU2, STU3 |
| MoleCare | 2AY Ltd | 皮膚健康風險評估 | R4 |
| Population Cardiac Risk | Boston Children's | ASCVD人口管理風險計算 | STU3 |
| SMART - PreciseHBR calculator | 長庚醫院 | 心臟病風險自動計算 | R4 |
| SRDC QRISK2 | SRDC | QRISK2心血管風險算法 | R4 |
| Stone LogiK | Translational Analytics | 尿石症治療方案預測 | STU3 |
| YouScript | YouScript Inc. | 基因型用藥風險指導 | DSTU2 |

### 藥物管理 (Medication)

| 應用名稱 | 開發者 | 功能 | FHIR |
|---------|--------|------|------|
| CDS Connect: Pain Management | AHRQ/MITRE | 疼痛管理決策儀表板 | DSTU2, R4 |
| Colchicine DDI-CDS App | DDI-CDS.org | 秋水仙鹼藥物交互作用警示 | R4 |
| COSRI | 華盛頓大學 | PDMP數據+鴉片類藥物決策支援 | R4 |
| DDInteract | DDI-CDS.org | 華法林+NSAIDs出血風險警示 | R4 |
| DoseMeRx | DoseMe | 精密給藥計算 | DSTU2 |
| Duke PillBox | Duke Medicine | 藥物使用訓練提升依從性 | DSTU2 |
| Fullscript | Fullscript Inc. | 個性化治療方案平台 | R4 |
| Handtevy Hospital | Pediatric Emergency Standards | 兒科/成人快速復甦系統 | DSTU2 |
| HIE Incontext | CRISP | HIE藥物資訊整合 | STU3 |
| Meducation RS | First Databank | 多語言患者藥物指示 | DSTU2, STU3 |
| Meducation TimeView | First Databank | 用藥依從史視覺化 | DSTU2 |
| Meds Price Compare | Technosoft | 處方藥價格比較 | DSTU2 |
| MedTrue | Geisinger & Merck | 藥物核對與依從性 | STU3 |
| MPR Monitor | Boston Children's | 用藥佔有率與依從性預測 | DSTU2 |
| RxOrbit InWorkflow | Leap Orbit | PDMP藥物清單嵌入EHR | DSTU2, STU3 |
| RxPrime | AESOP Technology | ML藥物分析識別用藥錯誤 | R4 |
| Rx Studio | Rx Studio Inc. | 精準給藥臨床決策支持 | STU3 |
| Tizanidine DDI-CDS App | DDI-CDS.org | 替扎尼定藥物交互作用 | R4 |

### 疾病管理 (Disease Management)

| 應用名稱 | 開發者 | 功能 | FHIR |
|---------|--------|------|------|
| Bilirubin Chart | Intermountain | 新生兒高膽紅素血症治療 | DSTU2 |
| Chest Pain Application | Regenstrief | 胸痛相關數據檢索顯示 | DSTU2 |
| ClinDat | Health Report Services | 風濕性疾病症狀監測評分 | DSTU2 |
| Diabetes Monograph | Boston Children's | 糖尿病專用單圖顯示 | DSTU2 |
| Lupus Advisor | Aditus | 狼瘡照護EHR輔助服務 | R4 |
| Premier AKI Staging | Premier Inc. | 急性腎損傷臨床指南遵循 | DSTU2 |
| Rimidi | Rimidi | 心代謝疾病持續管理 | DSTU2-R4 |
| Sepsis Watch | GA Tech/Emory | 敗血症預測模型 | STU3 |

### 照護協調 (Care Coordination)

| 應用名稱 | 開發者 | 功能 | FHIR |
|---------|--------|------|------|
| 1upHealth | 1upHealth | 聚合外部健康系統患者數據 | DSTU2, STU3 |
| ACT.md | ACT.md | 跨社區電子病歷延伸 | DSTU2 |
| AristaMD | AristaMD | 電子會診連接專家 | STU3 |
| Current Health | Current Health | 居家護理整合平台 | R4 |
| DMEscripts | DMEscripts LLC | 醫療設備訂購簡化 | STU3, R4 |
| Doximity on FHIR | Doximity | 醫療提供者資料+安全通訊 | DSTU2 |
| Fasten Health | Fasten Health | 開源個人醫療記錄匯總 | R4 |
| Guava | Guava Health | 個人健康管理應用 | DSTU2-R4 |
| Hale Health | Hale Health | 視訊問診+安全訊息 | DSTU2 |
| HealthConnect: Patient Referral Manager | Mindbowser | 轉診流程簡化 | DSTU2-R4 |
| Major Depression Outcomes App | OM1 | PHQ-9評分追蹤 | DSTU2-R4 |
| MazikCare Timeline | MazikGlobal | 患者就醫時間軸視圖 | DSTU2 |
| Medocity MD | Medocity | 連接追蹤監測患者平台 | DSTU2, STU3 |
| Physician Sign Out | ET Labs | 臨床工作交班應用 | DSTU2, STU3 |
| SigmaMD | Sigmoid Health | 健康數據聚合管理 | R4 |
| T System SMART App | CorroHealth | 急診科臨床內容 | DSTU2-R4 |
| Verata Pathway | Verata Health | 先前授權流程自動化 | DSTU2-R4 |

### 數據可視化 (Data Visualization)

| 應用名稱 | 開發者 | 功能 | FHIR |
|---------|--------|------|------|
| Abstractive Health | Abstractive Health | AI生成臨床摘要 | R4 |
| AI-Powered Health Chart | Prairie Byte | AI健康數據理解 | R4 |
| Avatachart | KeyOn / Visual Terminology | 3D臨床數據可視化 | R4 |
| DS Patient Care | Dotsquares | 患者觀察值+圖表 | R4 |
| explain my notes | shutdownhook | AI解釋臨床文件 | R4 |
| Growth Chart | Boston Children's | 兒童成長數據互動檢視 | DSTU2, STU3 |
| Growth Chart for Infants | Georgia Tech | 0-36個月嬰幼兒成長 | DSTU2 |
| JindalX | JindalX | AI患者理賠分析 | R4 |
| PatientShare | Patient Centric Solutions | 臨床數據查看分享 | R4 |
| Pediatric Growth Chart | Boston Children's | 兒科成長追蹤（iOS） | DSTU2 |
| Records | MedVertical | FHIR數據檢索驗證 | DSTU1-R4 |
| Risk Benefit | Ratio Health | 醫療程序溝通資料庫 | R4 |
| seeCOLe | seeCOLe LLC | AR實時EHR訪問 | DSTU1-R4 |
| SMART- PopHealth | Boston Children's | 人群健康指標共享 | DSTU2 |

### 患者參與 (Patient Engagement)

| 應用名稱 | 開發者 | 功能 | FHIR |
|---------|--------|------|------|
| Aidbox Forms | Health Samurai | EHR/患者入口問卷整合 | R4 |
| AppScript on FHIR | IQVIA | 數位患者參與工具電子開方 | DSTU2, STU3 |
| Atrial Fibrillation Treatment Options | DynaMed Decisions | 心房顫動治療選項可視化 | DSTU2 |
| CarePassport Portal | CarePassport Corp. | 統一患者入口 | DSTU2 |
| Carefluence Patient Portal | Carefluence | 多設施醫療記錄整合 | DSTU2 |
| CommonHealth | The Commons Project | 健康數據蒐集管理分享 | DSTU2, R4 |
| Health Wizz | Health Wizz | 健康資料掌控管理 | STU3 |
| Kickcall AI | Kickcall AI | AI接待員自動化患者來電 | R4 |
| Krames On FHIR | Krames | 患者教育資源整合 | DSTU2 |
| Mere | Mere Medical | 開源個人健康記錄 | DSTU2 |
| Meta Care AI | Metacare.ai | 老年人/退伍軍人健康應用 | R4 |
| MyFHR | CareEvolution | 全功能患者健康記錄 | DSTU2, STU3 |
| MyLinks | PatientLink | 36,000+診所PHR | DSTU2-R4 |
| OneRecord | OneRecord | 跨裝置健康數據整合 | DSTU2-R4 |
| PatientWisdom | PatientWisdom Inc. | 患者資訊摘要整合 | STU3 |
| Primary Record | Primary Record Inc. | 家庭健康數據組織協作 | R4 |
| Visiontree | Visiontree Software | ePRO患者數據收集 | DSTU2-R4 |

### 臨床研究 (Clinical Research)

| 應用名稱 | 開發者 | 功能 | FHIR |
|---------|--------|------|------|
| AutoMed Query | AutoMed Health | 自然語言查詢患者數據 | R4 |
| Caren mHealth | Caren LLC | 實際健康數據蒐集 | DSTU2, R4 |
| Clinical Pipe | Protocol First | 臨床試驗數據EHR→EDC | DSTU2 |
| Clinical Trials Search | ShutdownHook | 搜尋符合條件的臨床試驗 | DSTU2, R4 |
| eDocSS | Across Healthcare | 手術操作證據文件記錄 | R4 |
| HealthCheck AI | HealthCheck Inc | AI醫療摘要決策支持 | R4 |
| HR-pQCT Data Accession | Georgia Tech | 小兒骨病研究資料 | R4 |
| LHC-Forms SDC Questionnaire | Lister Hill Center | FHIR問卷SDC配置檔 | R4, STU3 |
| mTuitive OpNote | mTuitive Inc. | 術後報告合規性 | R4 |
| NLP2FHIR | Mayo Clinic | 臨床數據正規化管道 | STU3 |
| RTI Wellmine | RTI International | 罕見疾病患者數據收集 | R4 |

### 基因組學 (Genomics)

| 應用名稱 | 開發者 | 功能 | FHIR |
|---------|--------|------|------|
| NGS Quality Reporting | Samsung Medical Center | 新一代測序品質報告 | R4 |
| Precision Medicine Genes + AI | grinformatics | EHR遺傳結果組織 | DSTU2 |
| SMART Precision Cancer Medicine | Vanderbilt | 癌症體細胞基因突變分析 | DSTU2 |

### AI 驅動應用

| 應用名稱 | 開發者 | 功能 | FHIR |
|---------|--------|------|------|
| Abstractive Health | Abstractive Health | AI臨床摘要生成 | R4 |
| AI-Powered Health Chart | Prairie Byte | AI健康數據理解 | R4 |
| AutoMed Query | AutoMed Health | 自然語言患者數據查詢 | R4 |
| DxPrime | AESOP Technology | ML診斷/程序代碼建議 | R4 |
| explain my notes | shutdownhook | AI解釋臨床文件 | R4 |
| HealthCheck AI | HealthCheck Inc | AI醫療摘要 | R4 |
| HealthConnect系列 | Mindbowser | AI風險預測/摘要/症狀分析 | R4 |
| iAnswer Health | iAnswer Health | AI證據型醫療見解 | DSTU1-R4 |
| Muen Liver/Lung Detection | Muen Biomedical | AI腫瘤/結節檢測 | R4 |
| RxPrime | AESOP Technology | ML用藥錯誤識別 | R4 |
| Tri-Service AI ECG Analyzer | 三軍總醫院 | AI心電圖解讀 | R4 |

### FHIR 工具

| 應用名稱 | 開發者 | 功能 | FHIR |
|---------|--------|------|------|
| Convergent | Leap Orbit | 提供者目錄FHIR API搜尋 | R4 |
| EBMcalc FHIR App | EBMcalc LLC | 證據醫學計算機 | R4 |
| EBM_FHIR | EBM Technologies | 患者數據獲取 | R4 |
| LACE Index Scoring | Leapfrog Tech | 30天再入院預防 | STU3 |
| OntoCommand | CSIRO | FHIR術語服務器儀表板 | STU3, R4 |
| pCom | Endpoint Technologies | HIPAA合規提供者通訊 | R4 |
| PDemo | CareEvolution | 患者人口統計查詢 | DSTU2 |
| Shrimp | CSIRO | FHIR術語瀏覽器 | STU3, R4 |
| Smart Forms | CSIRO | React臨床表單渲染器 | R4 |

---

## 依 FHIR 版本分類

### 僅支援 R4

- Abstractive Health
- AI-Powered Health Chart
- Aidbox Forms
- AutoMed Query
- Avatachart
- Colchicine DDI-CDS App
- COSRI
- Cozeva
- Current Health
- DDInteract
- DxPrime
- EBMcalc FHIR App
- EBM_FHIR
- eDocSS
- explain my notes
- Fasten Health
- Flexpa
- Fullscript
- GrowSmart
- HealthCheck AI
- HR-pQCT Data Accession
- JindalX
- Kickcall AI
- Lupus Advisor
- Meta Care AI
- MoleCare
- Muen Liver/Lung Detection
- mTuitive OpNote
- NGS-QR App
- PatientShare
- pCom
- Primary Record
- Risk Benefit
- RxPrime
- SigmaMD
- Smart Forms
- SMART - PreciseHBR calculator
- SMART on FHIR Appointment Scheduler
- SRDC QRISK2
- Tri-Service AI ECG Analyzer

### 支援多版本 (DSTU2-R4)

- 1upHealth
- Caren mHealth
- Clinical Trials Search
- CommonHealth
- Guava
- HealthConnect 系列
- iAnswer Health
- MyLinks
- OneRecord
- Records
- Rimidi
- seeCOLe
- T System SMART App
- Verata Pathway
- Visiontree

---

## 完整應用程式列表

### A

| # | 應用名稱 | 開發者 | 功能簡述 | FHIR |
|---|---------|--------|----------|------|
| 1 | 1upHealth | 1upHealth | 聚合外部健康系統患者數據 | DSTU2, STU3 |
| 2 | Abstractive Health | Abstractive Health | AI臨床摘要生成 | R4 |
| 3 | ACT.md | ACT.md | 跨社區電子病歷延伸 | DSTU2 |
| 4 | Aidbox Forms | Health Samurai | EHR/患者入口問卷整合 | R4 |
| 5 | AI-Powered Health Chart | Prairie Byte Solutions | AI健康數據理解 | R4 |
| 6 | AppScript on FHIR | IQVIA Inc. | 數位患者參與工具電子開方 | DSTU2, STU3 |
| 7 | AristaMD | AristaMD | 電子會診連接專家 | STU3 |
| 8 | ASCVD Risk Calculator | Cerner | 心血管風險評分 | DSTU2 |
| 9 | Atrial Fibrillation Treatment Options | DynaMed Decisions | 心房顫動治療選項 | DSTU2 |
| 10 | AutoMed Query | AutoMed Health | 自然語言患者數據查詢 | R4 |
| 11 | Avatachart | KeyOn / Visual Terminology | 3D臨床數據可視化 | R4 |

### B

| # | 應用名稱 | 開發者 | 功能簡述 | FHIR |
|---|---------|--------|----------|------|
| 12 | Bilirubin Chart | Intermountain | 新生兒高膽紅素血症治療 | DSTU2 |
| 13 | BP Centiles v1 | Boston Children's | 兒童血壓百分位數 | DSTU2 |
| 14 | BP Centiles v2 | Interopion | 兒童血壓百分位數（商業版） | DSTU2 |

### C

| # | 應用名稱 | 開發者 | 功能簡述 | FHIR |
|---|---------|--------|----------|------|
| 15 | Cardiac Risk | Boston Children's | 雷諾茲心臟風險評分 | DSTU2 |
| 16 | Carefluence | Carefluence | 臨床決策支援工作流程 | DSTU2 |
| 17 | Carefluence Patient Portal | Carefluence | 多設施醫療記錄整合 | DSTU2 |
| 18 | Caren mHealth | Caren LLC | 實際健康數據蒐集 | DSTU2, R4 |
| 19 | CarePassport Portal | CarePassport Corp. | 統一患者入口 | DSTU2 |
| 20 | CDS Connect: Pain Management | AHRQ/MITRE | 疼痛管理決策儀表板 | DSTU2, R4 |
| 21 | Chest Pain Application | Regenstrief | 胸痛數據檢索顯示 | DSTU2 |
| 22 | CHF Predictive Analytics | SFO Technologies | 慢性心臟衰竭風險 | DSTU2 |
| 23 | ClinDat | Health Report Services | 風濕性疾病症狀監測 | DSTU2 |
| 24 | Clinical Pipe | Protocol First | 臨床試驗數據轉移 | DSTU2 |
| 25 | Clinical Trials Search | ShutdownHook | 臨床試驗搜尋 | DSTU2, R4 |
| 26 | C-Now | athenahealth | 遠程患者記錄存取 | DSTU2 |
| 27 | Colchicine DDI-CDS App | DDI-CDS.org | 秋水仙鹼藥物交互作用 | R4 |
| 28 | CommonHealth | The Commons Project | 健康數據管理分享 | DSTU2, R4 |
| 29 | Convergent | Leap Orbit | 提供者目錄搜尋 | R4 |
| 30 | COSRI | 華盛頓大學 | PDMP+鴉片類決策支援 | R4 |
| 31 | Cozeva | Cozeva | 護理差距審查解決 | R4 |
| 32 | CRC SCORE | Gradiant | 結直腸癌預測 | DSTU2, STU3 |
| 33 | Current Health | Current Health | 居家護理整合平台 | R4 |

### D

| # | 應用名稱 | 開發者 | 功能簡述 | FHIR |
|---|---------|--------|----------|------|
| 34 | DDInteract | DDI-CDS.org | 華法林+NSAIDs出血風險 | R4 |
| 35 | Diabetes Monograph | Boston Children's | 糖尿病專用單圖 | DSTU2 |
| 36 | Diabetes Predictive Analytics | SFO Technologies | 第2型糖尿病風險 | DSTU2 |
| 37 | DMEscripts | DMEscripts LLC | 醫療設備訂購 | STU3, R4 |
| 38 | Doctor Care Portal | DigiLife | 患者參與連接護理 | DSTU1 |
| 39 | DoseMeRx | DoseMe | 精密給藥計算 | DSTU2 |
| 40 | Doximity on FHIR | Doximity | 醫療提供者資料通訊 | DSTU2 |
| 41 | DS Patient Care | Dotsquares | 患者觀察值圖表 | R4 |
| 42 | Duke PillBox | Duke Medicine | 藥物使用訓練 | DSTU2 |
| 43 | DxPrime | AESOP Technology | ML診斷程序代碼建議 | R4 |

### E

| # | 應用名稱 | 開發者 | 功能簡述 | FHIR |
|---|---------|--------|----------|------|
| 44 | EBMcalc FHIR App | EBMcalc LLC | 證據醫學計算機 | R4 |
| 45 | EBM_FHIR | EBM Technologies | 患者數據獲取 | R4 |
| 46 | eDocSS | Across Healthcare | 手術操作文件記錄 | R4 |
| 47 | explain my notes | shutdownhook | AI解釋臨床文件 | R4 |

### F

| # | 應用名稱 | 開發者 | 功能簡述 | FHIR |
|---|---------|--------|----------|------|
| 48 | Fasten Health | Fasten Health | 開源醫療記錄匯總 | R4 |
| 49 | Flexpa | Flexpa | 醫療記錄存取授權 | - |
| 50 | Fullscript | Fullscript Inc. | 個性化治療方案 | R4 |

### G-H

| # | 應用名稱 | 開發者 | 功能簡述 | FHIR |
|---|---------|--------|----------|------|
| 51 | GrowSmart | U Delaware & Nemours | 兒童肥胖風險預測 | R4 |
| 52 | Growth Chart | Boston Children's | 兒童成長數據互動檢視 | DSTU2, STU3 |
| 53 | Growth Chart and Immunizations | Prairie Byte Solutions | 兒童成長+免疫接種 | DSTU2 |
| 54 | Growth Chart for Infants | Georgia Tech | 0-36個月嬰幼兒成長 | DSTU2 |
| 55 | Guava | Guava Health Inc. | 個人健康管理 | DSTU2-R4 |
| 56 | Hale Health | Hale Health | 視訊問診+安全訊息 | DSTU2 |
| 57 | Handtevy Hospital | Pediatric Emergency Standards | 兒科/成人復甦系統 | DSTU2 |
| 58 | HealthCheck AI | HealthCheck Inc | AI醫療摘要決策 | R4 |
| 59 | HealthConnect: AI Cardiovascular Risk | Mindbowser | AI心血管風險 | R4 |
| 60 | HealthConnect: AI Length of Stay | Mindbowser | AI住院時間預測 | R4 |
| 61 | HealthConnect: AI Medical Summary | Mindbowser | AI健康記錄摘要 | R4 |
| 62 | HealthConnect: AI Patient Care Plan | Mindbowser | AI護理計畫生成 | R4 |
| 63 | HealthConnect: AI Readmission Risk | Mindbowser | AI再入院風險 | R4 |
| 64 | HealthConnect: AI Symptom Analyzer | Mindbowser | AI症狀分析 | R4 |
| 65 | HealthConnect: AI Call Bot | Mindbowser | AI語音機器人問卷 | R4 |
| 66 | HealthConnect: AI Chat Questionnaire | Mindbowser | AI聊天式問卷 | R4 |
| 67 | HealthConnect: Patient Questionnaire | Mindbowser | 可自訂表單範本 | R4 |
| 68 | HealthConnect: Patient Referral Manager | Mindbowser | 轉診流程簡化 | R4 |
| 69 | Healthsuite | SFO Technologies | 心臟/糖尿病風險 | DSTU2 |
| 70 | Health Wizz | Health Wizz | 健康資料掌控管理 | STU3 |
| 71 | HEART Pathway | Impathiq Inc. | 胸痛決策工具 | DSTU2, STU3 |
| 72 | HIE Incontext | CRISP | HIE藥物資訊整合 | STU3 |
| 73 | HMS Library of Evidence | 哈佛醫學院 | 證據型影像決策 | STU3 |
| 74 | HR-pQCT Data Accession | Georgia Tech | 小兒骨病研究 | R4 |

### I-L

| # | 應用名稱 | 開發者 | 功能簡述 | FHIR |
|---|---------|--------|----------|------|
| 75 | iAnswer Health | iAnswer Health | AI證據型醫療見解 | DSTU1-R4 |
| 76 | Jeeves | 314e | EMR即時訓練 | DSTU1-R4 |
| 77 | JindalX | JindalX | AI理賠分析 | R4 |
| 78 | Kickcall AI | Kickcall AI | AI接待員自動化 | R4 |
| 79 | Krames On FHIR | Krames | 患者教育資源 | DSTU2 |
| 80 | LACE Index Scoring | Leapfrog Tech | 30天再入院預防 | STU3 |
| 81 | LA Wallet | LA Wallet | 數位身份+疫苗證明 | SMART Health Cards |
| 82 | LHC-Forms SDC Questionnaire | Lister Hill Center | FHIR問卷處理 | R4, STU3 |
| 83 | Lupus Advisor | Aditus | 狼瘡照護EHR輔助 | R4 |
| 84 | Lush SMART on FHIR | Lush Group Inc. | 多EMR臨床數據連接 | DSTU2 |

### M

| # | 應用名稱 | 開發者 | 功能簡述 | FHIR |
|---|---------|--------|----------|------|
| 85 | Major Depression Outcomes | OM1 | PHQ-9評分追蹤 | DSTU2-R4 |
| 86 | MazikCare Timeline | MazikGlobal | 患者就醫時間軸 | DSTU2 |
| 87 | Medocity MD | Medocity Inc. | 患者連接追蹤監測 | DSTU2, STU3 |
| 88 | Meds Price Compare | Technosoft | 處方藥價格比較 | DSTU2 |
| 89 | MedTrue | Geisinger & Merck | 藥物核對依從性 | STU3 |
| 90 | Meducation RS | First Databank | 多語言藥物指示 | DSTU2, STU3 |
| 91 | Meducation TimeView | First Databank | 用藥依從史視覺化 | DSTU2 |
| 92 | Mere | Mere Medical | 開源個人健康記錄 | DSTU2 |
| 93 | Meta Care AI | Metacare.ai | 老年人健康應用 | R4 |
| 94 | MoleCare | 2AY Ltd | 皮膚健康風險評估 | R4 |
| 95 | MPR Monitor | Boston Children's | 用藥佔有率預測 | DSTU2 |
| 96 | mTuitive OpNote | mTuitive Inc. | 術後報告合規 | R4 |
| 97 | Muen Liver Tumor Detection | Muen Biomedical | AI肝臟腫瘤檢測 | R4 |
| 98 | Muen Lung Nodule Detection | Muen Biomedical | AI肺結節檢測 | R4 |
| 99 | MyFHR | CareEvolution | 全功能患者健康記錄 | DSTU2, STU3 |
| 100 | My Immunizations | Patient Centric Solutions | 免疫接種記錄 | R4 |
| 101 | MyLinks | PatientLink | 36,000+診所PHR | DSTU2-R4 |

### N-P

| # | 應用名稱 | 開發者 | 功能簡述 | FHIR |
|---|---------|--------|----------|------|
| 102 | NGS-QR App | Samsung Medical Center | 新一代測序品質報告 | R4 |
| 103 | NLP2FHIR | Mayo Clinic | 臨床數據正規化 | STU3 |
| 104 | OneRecord | OneRecord | 跨裝置健康數據整合 | DSTU2-R4 |
| 105 | OntoCommand | CSIRO | FHIR術語服務器儀表板 | STU3, R4 |
| 106 | PatientCare Portal | DigiLife | 患者數據整合PHR | DSTU2 |
| 107 | Patient Notification App | Melodon Healthcare | 影像檢查結果通知 | DSTU2 |
| 108 | PatientShare | Patient Centric Solutions | 臨床數據查看分享 | R4 |
| 109 | PatientWisdom | PatientWisdom Inc. | 患者資訊摘要整合 | STU3 |
| 110 | pCom | Endpoint Technologies | HIPAA合規通訊 | R4 |
| 111 | PDemo | CareEvolution | 患者人口統計查詢 | DSTU2 |
| 112 | Pediatric Growth Chart for iOS | Boston Children's | 兒科成長追蹤 | DSTU2 |
| 113 | Physician Sign Out | ET Labs | 臨床工作交班 | DSTU2, STU3 |
| 114 | Population Cardiac Risk | Boston Children's | ASCVD人口管理 | STU3 |
| 115 | Precision Medicine Genes + AI | grinformatics | EHR遺傳結果組織 | DSTU2 |
| 116 | Premier AKI Staging | Premier Inc. | 急性腎損傷指南 | DSTU2 |
| 117 | Primary Record | Primary Record Inc. | 家庭健康數據協作 | R4 |

### R-S

| # | 應用名稱 | 開發者 | 功能簡述 | FHIR |
|---|---------|--------|----------|------|
| 118 | Records | MedVertical | FHIR數據檢索驗證 | DSTU1-R4 |
| 119 | Rimidi | Rimidi | 心代謝疾病管理 | DSTU1-R4 |
| 120 | Risk Benefit | Ratio Health | 醫療程序溝通 | R4 |
| 121 | RTI Wellmine | RTI International | 罕見疾病數據收集 | R4 |
| 122 | RxOrbit InWorkflow | Leap Orbit | PDMP藥物清單嵌入 | DSTU1-STU3 |
| 123 | RxPrime | AESOP Technology | ML用藥錯誤識別 | R4 |
| 124 | Rx Studio | Rx Studio Inc. | 精準給藥決策支持 | STU3 |
| 125 | seeCOLe | seeCOLe LLC | AR實時EHR訪問 | DSTU1-R4 |
| 126 | Sepsis Watch | GA Tech/Emory | 敗血症預測 | STU3 |
| 127 | Shrimp | CSIRO | FHIR術語瀏覽器 | STU3, R4 |
| 128 | SigmaMD | Sigmoid Health | 健康數據聚合管理 | R4 |
| 129 | Smart Forms | CSIRO | React臨床表單渲染 | R4 |
| 130 | SMART on FHIR Appointment Scheduler | 個人專案 | 患者預約管理 | R4 |
| 131 | SMART- PopHealth | Boston Children's | 人群健康指標 | DSTU2 |
| 132 | SMART - PreciseHBR calculator | 長庚醫院 | 心臟病風險計算 | R4 |
| 133 | SMART Precision Cancer Medicine | Vanderbilt | 癌症基因突變分析 | DSTU2 |
| 134 | SRDC QRISK2 | SRDC | QRISK2心血管風險 | R4 |
| 135 | Stone LogiK | Translational Analytics | 尿石症治療預測 | STU3 |

### T-Z

| # | 應用名稱 | 開發者 | 功能簡述 | FHIR |
|---|---------|--------|----------|------|
| 136 | Tizanidine DDI-CDS App | DDI-CDS.org | 替扎尼定藥物交互 | R4 |
| 137 | Tri-Service AI ECG Analyzer | 三軍總醫院 | AI心電圖解讀 | R4 |
| 138 | T System SMART App | CorroHealth | 急診科臨床內容 | DSTU2-R4 |
| 139 | uPerform for Healthcare | ANCILE Solutions | EHR推出/升級準備 | DSTU2 |
| 140 | Verata Pathway | Verata Health | 先前授權自動化 | DSTU2-R4 |
| 141 | Visiontree | Visiontree Software | ePRO患者數據收集 | DSTU2-R4 |
| 142 | VizCat SMART Card Verifier | VizCat | SMART QR碼驗證 | SMART Health Cards |
| 143 | YouScript | YouScript Inc. | 基因型用藥指導 | DSTU2 |

---

## 值得參考的功能亮點

### 與 ThTxGNN 相關的功能方向

#### 1. 藥物交互作用警示 (DDI-CDS)

DDI-CDS.org 開發了多個藥物交互作用應用：
- **Colchicine DDI-CDS App**：秋水仙鹼 + CYP3A4 抑制劑
- **DDInteract**：華法林 + NSAIDs 出血風險
- **Tizanidine DDI-CDS App**：替扎尼定 + CYP1A2 抑制劑

**參考價值**：ThTxGNN 已有 DDI 資料（DDInter + Guide to PHARMACOLOGY），可考慮整合為類似的 CDS 警示功能。

#### 2. 風險計算視覺化

多個應用提供風險評分視覺化：
- **Cardiac Risk**：雷諾茲風險評分互動展示
- **ASCVD Risk Calculator**：10年/終身心血管風險
- **SMART - PreciseHBR calculator**：長庚醫院開發的心臟病風險計算

**參考價值**：老藥新用預測結果可增加風險/效益視覺化呈現。

#### 3. AI 臨床摘要

- **Abstractive Health**：AI 生成臨床摘要
- **explain my notes**：AI 解釋複雜臨床文件
- **HealthConnect 系列**：AI 驅動的多種臨床功能

**參考價值**：可考慮為老藥新用候選提供 AI 解釋功能。

#### 4. 個人健康記錄整合

- **MyLinks**：支援 36,000+ 診所
- **Fasten Health**：開源自託管 PHR
- **OneRecord**：跨裝置健康數據整合

**參考價值**：可擴展 SMART App 支援更多數據來源整合。

#### 5. 泰國機構開發的應用

- **SMART - PreciseHBR calculator**（長庚醫院）
- **Tri-Service AI ECG Analyzer**（三軍總醫院）
- **Muen Liver/Lung Detection**（沐恩生醫）

**參考價值**：可參考泰國機構的開發經驗與在地化策略。

---

## 資料來源

- SMART App Gallery: https://apps.smarthealthit.org/apps?sort=name-asc
- 擷取日期: 2026-02-27
- 總應用數: 143

---

<div class="disclaimer">
<strong>免責聲明</strong>：本文件僅整理公開資訊供內部參考，不構成對任何應用程式的推薦或背書。
</div>
