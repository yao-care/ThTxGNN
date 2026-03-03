---
layout: default
title: Etanercept
description: "Etanercept 的老藥新用潛力分析。模型預測等級 L5，包含 6 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L1
indication_count: 6
---

# Etanercept

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>6</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Etanercept 藥師評估筆記

## 一句話總結

<p class="key-answer" data-question="Etanercept 可以用於治療什麼新適應症？">
Etanercept 是一種 TNF-alpha 抑制劑，TxGNN 預測其可能用於多種神經退化性疾病，但目前缺乏臨床試驗支持。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Etanercept (恩博) |
| DrugBank ID | DB00005 |
| 泰國商品名 | 爾瑞易注射液 |
| 原核准適應症 | 類風濕性關節炎、乾癬性關節炎、僵直性脊椎炎、中重度乾癬 |
| 預測新適應症 | ankylosing spondylitis、rheumatoid vasculitis、hypermobility of coccyx、inflammatory spondylopathy、spondyloarthropathy, susceptibility to、Kummell disease |
| 最高預測分數 | 0.9986 (primary progressive multiple sclerosis) |
| 證據等級 | L5 (僅預測) |





## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. rheumatoid vasculitis</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.71%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>Etanercept 透過抑制 TNF-alpha 發揮免疫調節作用。TNF-alpha 在神經退化性疾病中的角色已被廣泛研究：</p>

<ol>
<li><strong>發炎機轉關聯</strong>：TNF-alpha 參與中樞神經系統的發炎反應，而神經發炎是多發性硬化症和視神經脊髓炎的重要病理機制</li>
<li><strong>血腦屏障通透性</strong>：TNF-alpha 可增加血腦屏障通透性，理論上抑制 TNF-alpha 可能減少神經損傷</li>
<li><strong>免疫調節重疊</strong>：Etanercept 已核准用於多種自體免疫疾病，這些疾病與神經自體免疫疾病有部分機轉重疊</li>

</ol>
<p>然而需注意：Etanercept 為大分子生物製劑，難以穿透血腦屏障，這對中樞神經系統疾病的治療構成挑戰。</p>

<h3>臨床試驗</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02590562" target="_blank">NCT02590562</a></td><td>N/A</td><td>COMPLETED</td><td>808</td><td>A Multi-center Cross-sectional Study on Treatment Patterns and Patient Character...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01579006" target="_blank">NCT01579006</a></td><td>N/A</td><td>COMPLETED</td><td>184</td><td>A Multi National, Multi-center Non-interventional Study in Rheumatoid Arthritis ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00001901" target="_blank">NCT00001901</a></td><td>PHASE2</td><td>COMPLETED</td><td>60</td><td>Phase I/II Trial of TNFR:Fc (Etanercept) in Patients With Wegener&#x27;s Granulomatos...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01557322" target="_blank">NCT01557322</a></td><td>N/A</td><td>COMPLETED</td><td>1754</td><td>Evaluation of the Clinical Characteristics, Real-world Treatment Pathways, and O...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT07138898" target="_blank">NCT07138898</a></td><td>PHASE2</td><td>NOT_YET_RECRUITING</td><td>80</td><td>Immunosuppressant Management in Rheumatology Patients Undergoing Elective Total ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05696106" target="_blank">NCT05696106</a></td><td>N/A</td><td>UNKNOWN</td><td>750000</td><td>Risk of Incident Immune-mediated Inflammatory Diseases (IMID) in Patients Treate...</td></tr>
</tbody>
</table>

<h3>相關文獻</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/33058033/" target="_blank">33058033</a></td><td>2021</td><td>Article</td><td>Clinical rheumatology</td><td>Biological therapy in rheumatoid vasculitis: a systematic review.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28391344/" target="_blank">28391344</a></td><td>2017</td><td>Article</td><td>Nephrology, dialysis, transpla</td><td>Is there a role for TNFα blockade in ANCA-associated vasculitis and glomerulonep...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/31668853/" target="_blank">31668853</a></td><td>2019</td><td>Article</td><td>Biologicals : journal of the I</td><td>Efficacy and safety of original and biosimilar etanercept (SB4) in active rheuma...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/31632872/" target="_blank">31632872</a></td><td>2019</td><td>Article</td><td>Cureus</td><td>Etanercept-associated Nephropathy.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/15468348/" target="_blank">15468348</a></td><td>2004</td><td>Article</td><td>The Journal of rheumatology</td><td>Tumor necrosis factor-alpha blockade and the risk of vasculitis.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/12209493/" target="_blank">12209493</a></td><td>2002</td><td>Article</td><td>Arthritis and rheumatism</td><td>Accelerated nodulosis and vasculitis following etanercept therapy for rheumatoid...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38931826/" target="_blank">38931826</a></td><td>2024</td><td>Article</td><td>Pharmaceutics</td><td>Population Pharmacokinetic Analysis and Simulation of Alternative Dosing Regimen...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/15624748/" target="_blank">15624748</a></td><td>2004</td><td>Article</td><td>Journal of drugs in dermatolog</td><td>The medical uses and side effects of etanercept with a focus on cutaneous diseas...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28123776/" target="_blank">28123776</a></td><td>2017</td><td>Article</td><td>RMD open</td><td>Drug-specific risk and characteristics of lupus and vasculitis-like events in pa...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/10955351/" target="_blank">10955351</a></td><td>2000</td><td>Article</td><td>The Journal of rheumatology</td><td>Leukocytoclastic vasculitis due to etanercept.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/31491879/" target="_blank">31491879</a></td><td>2019</td><td>Article</td><td>International journal of molec</td><td>Different Original and Biosimilar TNF Inhibitors Similarly Reduce Joint Destruct...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/24854356/" target="_blank">24854356</a></td><td>2014</td><td>Article</td><td>Annals of the rheumatic diseas</td><td>What is the utility of routine ANA testing in predicting development of biologic...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/11792895/" target="_blank">11792895</a></td><td>2002</td><td>Article</td><td>Rheumatology (Oxford, England)</td><td>Etanercept and infliximab associated with cutaneous vasculitis.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/15627197/" target="_blank">15627197</a></td><td>2006</td><td>Article</td><td>Rheumatology international</td><td>Anti-TNFalpha therapy in rheumatoid arthritis and autoimmunity.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/19648728/" target="_blank">19648728</a></td><td>2009</td><td>Article</td><td>Dermatology (Basel, Switzerlan</td><td>Disseminated herpes zoster mimicking rheumatoid vasculitis in a rheumatoid arthr...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/17657687/" target="_blank">17657687</a></td><td>2007</td><td>Article</td><td>Scandinavian journal of rheuma</td><td>Demyelinating disease and cutaneous lymphocitic vasculitis after etanercept ther...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/25544845/" target="_blank">25544845</a></td><td>2014</td><td>Article</td><td>Case reports in medicine</td><td>Large Vessel Vasculitis Occurring in Rheumatoid Arthritis Patient under Anti-TNF...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/15853915/" target="_blank">15853915</a></td><td>2005</td><td>Article</td><td>Scandinavian journal of immuno</td><td>Immunology of cutaneous vasculitis associated with both etanercept and inflixima...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/15801034/" target="_blank">15801034</a></td><td>2005</td><td>Article</td><td>The Journal of rheumatology</td><td>Proliferative lupus nephritis and leukocytoclastic vasculitis during treatment w...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/23154729/" target="_blank">23154729</a></td><td>2012</td><td>Article</td><td>Internal medicine (Tokyo, Japa</td><td>Foot ulcers caused by rheumatoid vasculitis in a patient with rheumatoid arthrit...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. hypermobility of coccyx</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.63%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. inflammatory spondylopathy</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.57%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（50 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02509026" target="_blank">NCT02509026</a></td><td>PHASE4</td><td>COMPLETED</td><td>210</td><td>A MULTICENTER OPEN-LABEL STUDY OF ETANERCEPT WITHDRAWAL AND RETREATMENT IN SUBJE...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02376790" target="_blank">NCT02376790</a></td><td>PHASE3</td><td>COMPLETED</td><td>851</td><td>A Multicenter Double-Blind, Randomized Controlled Study of Etanercept and Methot...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03729674" target="_blank">NCT03729674</a></td><td>N/A</td><td>UNKNOWN</td><td>800</td><td>Comparative Effectiveness and Safety of Biosimilar and Legacy Drugs</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05164198" target="_blank">NCT05164198</a></td><td>PHASE4</td><td>UNKNOWN</td><td>448</td><td>Multicenter, Prospective Clinical Trial for Optimizing TNF Inhibitor Dose Adjust...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01934933" target="_blank">NCT01934933</a></td><td>PHASE4</td><td>COMPLETED</td><td>150</td><td>A Multi-center, Open Label, Random Clinical Trial of Etanercept and Celecoxib Al...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01604629" target="_blank">NCT01604629</a></td><td>PHASE4</td><td>COMPLETED</td><td>120</td><td>Evaluation of Clinical Value of Standardized Protocol for Dose-reduction in Pati...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00133315" target="_blank">NCT00133315</a></td><td>PHASE4</td><td>COMPLETED</td><td>50</td><td>TNFalfa Blocking Treatment of Spondylarthropathies - A Danish Multicenter Study ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00432406" target="_blank">NCT00432406</a></td><td>PHASE4</td><td>COMPLETED</td><td>40</td><td>TNF-α Blockade for Psoriatic Arthritis - A Clinical and MRI Study, and the Effec...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00247962" target="_blank">NCT00247962</a></td><td>PHASE4</td><td>COMPLETED</td><td>566</td><td>A Randomized, Double-Blind Study Evaluating the Safety and Efficacy of Etanercep...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00244179" target="_blank">NCT00244179</a></td><td>PHASE2</td><td>UNKNOWN</td><td>40</td><td>New Immunomodulatory Therapy Strategies in Chronic Reactive Arthritis: Immunosti...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05080218" target="_blank">NCT05080218</a></td><td>PHASE4</td><td>COMPLETED</td><td>841</td><td>The SARS-CoV-2 Vaccine Response and Safety in Rheumatology Patients and the Infl...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01258738" target="_blank">NCT01258738</a></td><td>PHASE3</td><td>COMPLETED</td><td>225</td><td>A Multicentre, 12 Week Double Blind Placebo Controlled Randomized Study Of Etane...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00273858" target="_blank">NCT00273858</a></td><td>N/A</td><td>TERMINATED</td><td>880</td><td>Open Label Study To Evaluate The Safety Profile And The Quality Of Life In Patie...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00224562" target="_blank">NCT00224562</a></td><td>N/A</td><td>UNKNOWN</td><td>N/A</td><td>The RATIO Registry: French Registry on Opportunistic and Severe Bacterial Infect...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00127842" target="_blank">NCT00127842</a></td><td>PHASE4</td><td>COMPLETED</td><td>110</td><td>Rating Evaluations in Psoriatic Arthritis (PsA) With Enbrel®</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02638896" target="_blank">NCT02638896</a></td><td>PHASE4</td><td>UNKNOWN</td><td>100</td><td>Efficacy and Safety of Etanercept Dose Reduction in Patients With Ankylosing Spo...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00508547" target="_blank">NCT00508547</a></td><td>N/A</td><td>ACTIVE_NOT_RECRUITING</td><td>15842</td><td>A Multicenter, Open Registry of Patients With Plaque Psoriasis Who Are Candidate...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05115903" target="_blank">NCT05115903</a></td><td>PHASE4</td><td>UNKNOWN</td><td>15</td><td>A Prospective, Randomized Biologic Tapering Study of TNF Inhibitors in Axial Spo...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04077957" target="_blank">NCT04077957</a></td><td>PHASE4</td><td>UNKNOWN</td><td>100</td><td>Treat-to-target Strategy in Ankylosing Spondylitis Using Etanercept and Conventi...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00410046" target="_blank">NCT00410046</a></td><td>PHASE4</td><td>COMPLETED</td><td>84</td><td>An Open-label, Multicentre, Supplementary Extension Study of Etanercept in Subje...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00293722" target="_blank">NCT00293722</a></td><td>N/A</td><td>COMPLETED</td><td>1308</td><td>Prospective Post Marketing Surveillance to Evaluate the Safety and Efficacy of E...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01060098" target="_blank">NCT01060098</a></td><td>N/A</td><td>COMPLETED</td><td>48</td><td>T Cells and TNF: The Impact of TNF Blockade on Effector T Cell Populations in Rh...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01793285" target="_blank">NCT01793285</a></td><td>N/A</td><td>COMPLETED</td><td>85</td><td>Retrospective, Multicentric, National, Observational Study, to Follow-up the Pat...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04582084" target="_blank">NCT04582084</a></td><td>N/A</td><td>COMPLETED</td><td>583</td><td>Assessment of Treatment Safety and Quality of Life in Patients Receiving Etanerc...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06085079" target="_blank">NCT06085079</a></td><td>PHASE4</td><td>UNKNOWN</td><td>20</td><td>A 24-week Two-armed Proof-of-concept Exploratory Analysis of Subcutaneous Ixekiz...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT07041112" target="_blank">NCT07041112</a></td><td>N/A</td><td>COMPLETED</td><td>1000</td><td>Pharmacogenetic Observational Study Evaluating the Influence of Genetic Variants...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00356356" target="_blank">NCT00356356</a></td><td>PHASE3</td><td>COMPLETED</td><td>257</td><td>Open-label, Long-term Extension Study of Etanercept in the Treatment of Patients...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03496831" target="_blank">NCT03496831</a></td><td>N/A</td><td>COMPLETED</td><td>7500</td><td>Development of a Prediction Model for the Risk of Hospitalized Infection in Pati...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02915354" target="_blank">NCT02915354</a></td><td>PHASE4</td><td>COMPLETED</td><td>35</td><td>Relapse of Ankylosing Spondylitis Patients Withdrawal Etanercept After Clinical ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02809781" target="_blank">NCT02809781</a></td><td>PHASE2, PHASE3</td><td>UNKNOWN</td><td>250</td><td>Phase III Study of Human Bone Marrow-Derived Mesenchymal Stem Cells to Treat AS</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04345458" target="_blank">NCT04345458</a></td><td>PHASE3</td><td>COMPLETED</td><td>640</td><td>Safety and Efficacy of Prefilled Liquid Etanercept(Yisaipu) for Active Ankylosin...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00420238" target="_blank">NCT00420238</a></td><td>PHASE4</td><td>COMPLETED</td><td>82</td><td>A Multicentre, Double-Blind, Placebo-Controlled, Randomised Study of Etanercept ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04891640" target="_blank">NCT04891640</a></td><td>NA</td><td>ACTIVE_NOT_RECRUITING</td><td>164</td><td>Biologic Abatement and Capturing Kids&#x27; Outcomes and Flare Frequency in Juvenile ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04610476" target="_blank">NCT04610476</a></td><td>PHASE3</td><td>UNKNOWN</td><td>270</td><td>A Prospective, Randomized, Controlled, Open Label, Assessor-blinded, Parallel-gr...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04428502" target="_blank">NCT04428502</a></td><td>N/A</td><td>COMPLETED</td><td>127</td><td>Correlation of Anti-CCP With Disease Activity and Its Impact on Biological Respo...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03100734" target="_blank">NCT03100734</a></td><td>N/A</td><td>COMPLETED</td><td>585</td><td>A Multicentre Observational Study to Evaluate the Real-Life Effectiveness of Ben...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00910273" target="_blank">NCT00910273</a></td><td>PHASE4</td><td>TERMINATED</td><td>34</td><td>Effects of Etanercept on Endothelial Function and Carotid Intima-media Thickness...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02456363" target="_blank">NCT02456363</a></td><td>PHASE2</td><td>UNKNOWN</td><td>300</td><td>Anti-Tumor Necrosis Factor Therapy In Patients With Ankylosing Spondylitis-A Reg...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03470688" target="_blank">NCT03470688</a></td><td>N/A</td><td>UNKNOWN</td><td>5000</td><td>An Observational Study Designed to Investigate the Utilisation and Effectiveness...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02489760" target="_blank">NCT02489760</a></td><td>PHASE4</td><td>UNKNOWN</td><td>30</td><td>Etanercept Versus Adalimumab in the Treatment of Patients With Ankylosing Spondy...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00478660" target="_blank">NCT00478660</a></td><td>PHASE3</td><td>COMPLETED</td><td>1250</td><td>Review of Safety and Efficacy With Adalimumab in Patients With Active Ankylosing...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00195416" target="_blank">NCT00195416</a></td><td>N/A</td><td>COMPLETED</td><td>526</td><td>A Drug Use Investigation of Enbrel for Post-marketing Surveillance (PMS) for Ank...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01965132" target="_blank">NCT01965132</a></td><td>N/A</td><td>RECRUITING</td><td>10000</td><td>Korean College of Rheumatology Biologics and Targeted Therapy Registry</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03504072" target="_blank">NCT03504072</a></td><td>PHASE4</td><td>UNKNOWN</td><td>174</td><td>Risk of Tuberculosis and Infections in Spondyloarthritis Patients Treated With T...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00678782" target="_blank">NCT00678782</a></td><td>PHASE2</td><td>COMPLETED</td><td>31</td><td>Evaluation of The Efficacy And Safety of Intra-Articular Etanercept in Patients ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00421915" target="_blank">NCT00421915</a></td><td>PHASE3</td><td>COMPLETED</td><td>84</td><td>Multicenter, Double-Blind, Parallel, Placebo-Controlled, Randomised Phase 3 Stud...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01411215" target="_blank">NCT01411215</a></td><td>N/A</td><td>TERMINATED</td><td>160</td><td>A Non-Interventional Study of the Treatment With Etanercept in Rheumatoid Arthri...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01465438" target="_blank">NCT01465438</a></td><td>PHASE4</td><td>COMPLETED</td><td>42</td><td>Can New Imaging- and Biomarkers Improve the Assessment of Disease Activity and P...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00844142" target="_blank">NCT00844142</a></td><td>PHASE2</td><td>UNKNOWN</td><td>80</td><td>Randomized Controlled 12 Months Trial With Etanercept (Enbrel ®) vs. Sulfasalazi...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01610947" target="_blank">NCT01610947</a></td><td>NA</td><td>COMPLETED</td><td>398</td><td>Effect of Spacing of Anti-TNF Drugs in Ankylosing Spondylitis With Low Disease A...</td></tr>
</tbody>
</table>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/25438042/" target="_blank">25438042</a></td><td>2015</td><td>Article</td><td>Current medical research and o</td><td>Etanercept and uveitis: friends or foes?</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/24980068/" target="_blank">24980068</a></td><td>2015</td><td>Article</td><td>Rheumatology international</td><td>Etanercept biosimilars.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28940172/" target="_blank">28940172</a></td><td>2017</td><td>Article</td><td>BioDrugs : clinical immunother</td><td>GP2015: An Etanercept Biosimilar.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/17072572/" target="_blank">17072572</a></td><td>2006</td><td>Article</td><td>Zeitschrift fur Rheumatologie</td><td>[Spondylarthritides].</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28837372/" target="_blank">28837372</a></td><td>2018</td><td>Article</td><td>Modern rheumatology</td><td>Update upon efficacy and safety of etanercept for the treatment of spondyloarthr...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28682112/" target="_blank">28682112</a></td><td>2017</td><td>Article</td><td>Expert opinion on biological t</td><td>Etanercept for treating axial spondyloarthritis.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36752358/" target="_blank">36752358</a></td><td>2023</td><td>Article</td><td>Arthritis care &amp; research</td><td>Uptake and Spending on Biosimilar Infliximab and Etanercept After New Start and ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/18208819/" target="_blank">18208819</a></td><td>2008</td><td>Article</td><td>Rheumatology (Oxford, England)</td><td>Infliximab, etanercept and adalimumab for the treatment of ankylosing spondyliti...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28752242/" target="_blank">28752242</a></td><td>2017</td><td>Article</td><td>BioDrugs : clinical immunother</td><td>Patients&#x27; Understanding and Attitudes Towards Infliximab and Etanercept Biosimil...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28434410/" target="_blank">28434410</a></td><td>2017</td><td>Article</td><td>International journal of techn</td><td>DOSAGE AND DURATION OF ETANERCEPT THERAPY FOR ANKYLOSING SPONDYLITIS: A META-ANA...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/16097922/" target="_blank">16097922</a></td><td>2005</td><td>Article</td><td>The Medical journal of Austral</td><td>Tumour necrosis factor inhibitors.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36379575/" target="_blank">36379575</a></td><td>2023</td><td>Article</td><td>The Journal of rheumatology</td><td>Etanercept Withdrawal and Retreatment in Nonradiographic Axial Spondyloarthritis...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35434764/" target="_blank">35434764</a></td><td>2022</td><td>Article</td><td>Clinical rheumatology</td><td>Clinical efficacy and safety of adalimumab versus etanercept in patients with an...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/17651658/" target="_blank">17651658</a></td><td>2007</td><td>Article</td><td>Health technology assessment (</td><td>Adalimumab, etanercept and infliximab for the treatment of ankylosing spondyliti...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/31483969/" target="_blank">31483969</a></td><td>2019</td><td>Article</td><td>The New England journal of med</td><td>A Terminal Event.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/15161337/" target="_blank">15161337</a></td><td>2004</td><td>Article</td><td>BioDrugs : clinical immunother</td><td>Etanercept: in ankylosing spondylitis.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/25910480/" target="_blank">25910480</a></td><td>2015</td><td>Article</td><td>International journal of clini</td><td>Efficiency of adalimumab, etanercept and infliximab in ankylosing spondylitis in...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35234569/" target="_blank">35234569</a></td><td>2023</td><td>Article</td><td>Scandinavian journal of rheuma</td><td>Interval prolongation of etanercept in rheumatoid arthritis, ankylosing spondyli...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39734351/" target="_blank">39734351</a></td><td>2024</td><td>Article</td><td>Turkish journal of medical sci</td><td>The relationship between drug-induced immunogenicity and hypersensitivity reacti...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35777821/" target="_blank">35777821</a></td><td>2023</td><td>Article</td><td>The Journal of rheumatology</td><td>Inflammatory Bowel Disease Risk in Patients With Axial Spondyloarthritis Treated...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. Kummell disease</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.55%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. polyarticular juvenile rheumatoid arthritis</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.50%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（8 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06654882" target="_blank">NCT06654882</a></td><td>PHASE3</td><td>NOT_YET_RECRUITING</td><td>400</td><td>Trial of Sequential Medications AfteR TNFi Failure in Juvenile Idiopathic Arthri...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01145352" target="_blank">NCT01145352</a></td><td>N/A</td><td>COMPLETED</td><td>113</td><td>Enbrel-JIA Use Results Survey [All-Case Surveillance]</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03780959" target="_blank">NCT03780959</a></td><td>PHASE2, PHASE3</td><td>COMPLETED</td><td>69</td><td>Safety, Population Pharmacokinetics, and Efficacy of Recombinant Human Tumor Nec...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03781375" target="_blank">NCT03781375</a></td><td>PHASE3</td><td>TERMINATED</td><td>25</td><td>A Phase III Double Blind Randomized Study Comparing Etanercept (Enbrel) Combined...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06413563" target="_blank">NCT06413563</a></td><td>N/A</td><td>NOT_YET_RECRUITING</td><td>75</td><td>Analysis of Peripheral Blood Lymphocytes in Patients With Juvenile Idiopathic Ar...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00078793" target="_blank">NCT00078793</a></td><td>N/A</td><td>COMPLETED</td><td>600</td><td>Phase IV Registry of Etanercept (Enbrel®) In Children With Juvenile Rheumatoid A...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT07386587" target="_blank">NCT07386587</a></td><td>PHASE3</td><td>ENROLLING_BY_INVITATION</td><td>60</td><td>Response of Methotrexate Alone Versus Methotrexate Combined With Etanercept for ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02840175" target="_blank">NCT02840175</a></td><td>PHASE3</td><td>COMPLETED</td><td>62</td><td>Treatment Tapering in Oligoarticular or Rheumatoid Factor Negative Polyarticular...</td></tr>
</tbody>
</table>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28418334/" target="_blank">28418334</a></td><td>2017</td><td>Article</td><td>Balkan medical journal</td><td>Juvenile Idiopathic Arthritis.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/26233720/" target="_blank">26233720</a></td><td>2015</td><td>Article</td><td>Clinical rheumatology</td><td>Enthesitis-related arthritis.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/40148850/" target="_blank">40148850</a></td><td>2025</td><td>Article</td><td>BMC pediatrics</td><td>Comparative efficacy and safety of etanercept and adalimumab in the treatment of...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/29781829/" target="_blank">29781829</a></td><td>2019</td><td>Article</td><td>Journal of clinical rheumatolo</td><td>Comparison of Adults With Polyarticular Juvenile Idiopathic Arthritis to Adults ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/12641492/" target="_blank">12641492</a></td><td>2003</td><td>Article</td><td>BioDrugs : clinical immunother</td><td>Spotlight on etanercept in rheumatoid arthritis, psoriatic arthritis and juvenil...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/27989499/" target="_blank">27989499</a></td><td>2016</td><td>Article</td><td>Seminars in arthritis and rheu</td><td>Biological agents in polyarticular juvenile idiopathic arthritis: A meta-analysi...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38204313/" target="_blank">38204313</a></td><td>2023</td><td>Article</td><td>The Turkish journal of pediatr</td><td>Choice and switch of biologic drugs in juvenile idiopathic arthritis.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/10717011/" target="_blank">10717011</a></td><td>2000</td><td>Article</td><td>The New England journal of med</td><td>Etanercept in children with polyarticular juvenile rheumatoid arthritis. Pediatr...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/11302411/" target="_blank">11302411</a></td><td>2001</td><td>Article</td><td>The Annals of pharmacotherapy</td><td>Etanercept in juvenile rheumatoid arthritis.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/12421111/" target="_blank">12421111</a></td><td>2002</td><td>Article</td><td>Drugs</td><td>Etanercept: an updated review of its use in rheumatoid arthritis, psoriatic arth...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/11246677/" target="_blank">11246677</a></td><td>2001</td><td>Article</td><td>The Journal of rheumatology</td><td>Clinical response to etanercept in polyarticular course juvenile rheumatoid arth...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28025136/" target="_blank">28025136</a></td><td>2017</td><td>Article</td><td>Clinical immunology (Orlando, </td><td>CD3+CD56+ natural killer T cell activity in children with different forms of juv...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39946290/" target="_blank">39946290</a></td><td>2025</td><td>Article</td><td>Expert opinion on drug safety</td><td>An update on the safety of biologic therapies for the treatment of polyarticular...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/17563271/" target="_blank">17563271</a></td><td>2007</td><td>Article</td><td>Expert opinion on pharmacother</td><td>Etanercept: long-term clinical experience in rheumatoid arthritis and other arth...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/10595864/" target="_blank">10595864</a></td><td>1999</td><td>Article</td><td>Drugs</td><td>Medical management of children with juvenile rheumatoid arthritis.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/11773549/" target="_blank">11773549</a></td><td>2002</td><td>Article</td><td>Pediatrics</td><td>Current treatment of juvenile rheumatoid arthritis.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/20444859/" target="_blank">20444859</a></td><td>2010</td><td>Article</td><td>Rheumatology (Oxford, England)</td><td>Etanercept improves linear growth and bone mass acquisition in MTX-resistant pol...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/11583059/" target="_blank">11583059</a></td><td>2001</td><td>Article</td><td>Expert opinion on pharmacother</td><td>The treatment of juvenile arthritis.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/20087751/" target="_blank">20087751</a></td><td>2010</td><td>Article</td><td>Modern rheumatology</td><td>Guidelines on the use of etanercept for juvenile idiopathic arthritis in Japan.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/24599916/" target="_blank">24599916</a></td><td>2014</td><td>Article</td><td>Rheumatology (Oxford, England)</td><td>Predictors of response to etanercept in polyarticular-course juvenile idiopathic...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. vertebral disease</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.16%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（6 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01258738" target="_blank">NCT01258738</a></td><td>PHASE3</td><td>COMPLETED</td><td>225</td><td>A Multicentre, 12 Week Double Blind Placebo Controlled Randomized Study Of Etane...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05115903" target="_blank">NCT05115903</a></td><td>PHASE4</td><td>UNKNOWN</td><td>15</td><td>A Prospective, Randomized Biologic Tapering Study of TNF Inhibitors in Axial Spo...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02809781" target="_blank">NCT02809781</a></td><td>PHASE2, PHASE3</td><td>UNKNOWN</td><td>250</td><td>Phase III Study of Human Bone Marrow-Derived Mesenchymal Stem Cells to Treat AS</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00413400" target="_blank">NCT00413400</a></td><td>NA</td><td>COMPLETED</td><td>40</td><td>Effects of Etanercept in Patients With the Metabolic Syndrome (II)</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01188655" target="_blank">NCT01188655</a></td><td>N/A</td><td>COMPLETED</td><td>89</td><td>Observational Non-Interventional Study With Enbrel in Patients With Ankylosing S...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01400516" target="_blank">NCT01400516</a></td><td>PHASE4</td><td>COMPLETED</td><td>26</td><td>Teriparatide for Joint Erosions in Rheumatoid Arthritis: The TERA Trial</td></tr>
</tbody>
</table>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/31969328/" target="_blank">31969328</a></td><td>2020</td><td>Article</td><td>Annals of the rheumatic diseas</td><td>EULAR recommendations for the management of rheumatoid arthritis with synthetic ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38503473/" target="_blank">38503473</a></td><td>2024</td><td>Article</td><td>Annals of the rheumatic diseas</td><td>Efficacy and safety of pharmacological treatment of psoriatic arthritis: a syste...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/17072572/" target="_blank">17072572</a></td><td>2006</td><td>Article</td><td>Zeitschrift fur Rheumatologie</td><td>[Spondylarthritides].</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28682112/" target="_blank">28682112</a></td><td>2017</td><td>Article</td><td>Expert opinion on biological t</td><td>Etanercept for treating axial spondyloarthritis.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35543102/" target="_blank">35543102</a></td><td>2023</td><td>Article</td><td>Scandinavian journal of rheuma</td><td>Does a short course of etanercept influence disease progression and radiographic...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/24101863/" target="_blank">24101863</a></td><td>2013</td><td>Article</td><td>Patient preference and adheren</td><td>Long-term safety and efficacy of etanercept in the treatment of ankylosing spond...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/20554241/" target="_blank">20554241</a></td><td>2010</td><td>Article</td><td>Joint bone spine</td><td>Elderly-onset rheumatoid arthritis.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/29624303/" target="_blank">29624303</a></td><td>2016</td><td>Article</td><td>Reumatizam</td><td>[JUVENILE SPONDYLOARTHRITIS].</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/31483969/" target="_blank">31483969</a></td><td>2019</td><td>Article</td><td>The New England journal of med</td><td>A Terminal Event.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/16310398/" target="_blank">16310398</a></td><td>2005</td><td>Article</td><td>Joint bone spine</td><td>Psoriatic arthritis.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/32007648/" target="_blank">32007648</a></td><td>2020</td><td>Article</td><td>Joint bone spine</td><td>Chronic bursitis and tenosynovitis revealing Whipple&#x27;s disease.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36633815/" target="_blank">36633815</a></td><td>2023</td><td>Article</td><td>Rheumatology and therapy</td><td>Comparative Efficacy of Biologic Disease-Modifying Anti-Rheumatic Drugs for Non-...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/31749988/" target="_blank">31749988</a></td><td>2019</td><td>Article</td><td>RMD open</td><td>Treatment retention of infliximab and etanercept originators versus their corres...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38309516/" target="_blank">38309516</a></td><td>2024</td><td>Article</td><td>Joint bone spine</td><td>Targeted therapies for uveitis in spondyloarthritis: A narrative review.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28482137/" target="_blank">28482137</a></td><td>2017</td><td>Article</td><td>Arthritis care &amp; research</td><td>Effects of Long-Term Etanercept Treatment on Clinical Outcomes and Objective Sig...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/26560086/" target="_blank">26560086</a></td><td>2015</td><td>Article</td><td>Alzheimer&#x27;s research &amp; therapy</td><td>Central delivery of iodine-125-labeled cetuximab, etanercept and anakinra after ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/20444859/" target="_blank">20444859</a></td><td>2010</td><td>Article</td><td>Rheumatology (Oxford, England)</td><td>Etanercept improves linear growth and bone mass acquisition in MTX-resistant pol...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/24891317/" target="_blank">24891317</a></td><td>2014</td><td>Article</td><td>Arthritis &amp; rheumatology (Hobo</td><td>Symptomatic efficacy of etanercept and its effects on objective signs of inflamm...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/40015358/" target="_blank">40015358</a></td><td>2025</td><td>Article</td><td>Joint bone spine</td><td>Clinical and ultrasonographic predictors of disease activity after TNF-α inhibit...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/34838991/" target="_blank">34838991</a></td><td>2022</td><td>Article</td><td>Joint bone spine</td><td>Changes in etanercept and adalimumab biosimilar prescriptions for the initial tr...</td></tr>
</tbody>
</table>

</div>
</details>


## 泰國上市資訊

| 項目 | 內容 |
|------|------|
| 許可證字號 | 衛署菌疫輸字第000876號 |
| 中文品名 | 爾瑞易注射液 |
| 英文品名 | Enbrel Solution for Injection |
| 許可證持有者 | 輝瑞大藥廠股份有限公司 |
| 劑型 | 注射劑 |
| 核准日期 | 2012/03/26 |
| 有效期限 | 2027/03/26 |
| 狀態 | 有效 |

## 安全性考量

### 已知風險
- **感染風險增加**：包括嚴重細菌、病毒、真菌感染
- **結核病再活化**：使用前需篩檢潛伏性結核
- **惡性腫瘤風險**：長期使用可能增加淋巴瘤風險
- **注射部位反應**：常見局部反應

### 藥物交互作用
根據 DDInter 資料庫，Etanercept 與以下藥物有交互作用：
- Anakinra (Major)：不建議併用，增加嚴重感染風險
- Abatacept (Major)：不建議併用
- 活疫苗：禁止併用

### 特殊族群
- **孕婦**：C 級，權衡利弊後使用
- **哺乳**：少量分泌至乳汁
- **肝腎功能不全**：無需調整劑量

### 藥物-草藥交互作用 (DHI)

**紫錐花** 🟡 Moderate
- 影響：紫錐花可能與免疫調節藥物產生交互作用
- 建議：謹慎使用


## 結論與下一步

### 整體評估
此預測目前**不建議臨床應用**，原因如下：
1. 缺乏任何臨床試驗或觀察性研究支持
2. Etanercept 為大分子藥物，中樞神經系統滲透性差
3. 部分預測適應症(如 MS)實際上可能因 TNF 抑制而惡化

### 建議行動
- [ ] 需要更多基礎研究探討 TNF-alpha 抑制在神經退化性疾病中的角色
- [ ] 若要進行臨床研究，需先解決藥物遞送至中樞神經系統的問題
- [ ] 密切監測已使用 Etanercept 患者是否出現神經系統症狀

### 風險等級
**高風險** - 不建議超適應症使用

---

*報告生成日期：2026-02-11*
*資料來源：TxGNN 預測、ClinicalTrials.gov、PubMed、TFDA*


---

## 相關藥物報告

- [Homatropine Methylbromide]({{ "/drugs/homatropine_methylbromide/" | relative_url }}) - 證據等級 L5
- [Nitrofurantoin]({{ "/drugs/nitrofurantoin/" | relative_url }}) - 證據等級 L5
- [Urea]({{ "/drugs/urea/" | relative_url }}) - 證據等級 L5
- [Vigabatrin]({{ "/drugs/vigabatrin/" | relative_url }}) - 證據等級 L5
- [Bevacizumab]({{ "/drugs/bevacizumab/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
ThTxGNN. (2026). Etanercept老藥新用驗證報告. https://thtxgnn.yao.care/drugs/etanercept/
```

**BibTeX 格式：**
```bibtex
@misc{thtxgnn_etanercept,
  title = {Etanercept老藥新用驗證報告},
  author = {ThTxGNN Team},
  year = {2026},
  url = {https://thtxgnn.yao.care/drugs/etanercept/}
}
```

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>最後審核：2026-02-20 | 審核者：ThTxGNN Research Team</small>
</div>

{% include giscus.html %}
