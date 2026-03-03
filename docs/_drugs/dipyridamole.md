---
layout: default
title: Dipyridamole
description: "Dipyridamole 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L1
indication_count: 10
---

# Dipyridamole

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Dipyridamole (待乙妥) - 藥師評估報告

## 一句話總結

<p class="key-answer" data-question="Dipyridamole 可以用於治療什麼新適應症？">
Dipyridamole 是一種磷酸二酯酶抑制劑和腺苷再攝取抑制劑，用於心絞痛和血栓預防；TxGNN 預測其對變異型心絞痛和中風有潛在療效，有豐富的臨床試驗和文獻支持，但變異型心絞痛預測與原適應症高度重疊。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Dipyridamole (待乙妥/雙乙妥) |
| DrugBank ID | DB00975 |
| 泰國商品名 | 百心康、Aggrenox（與 aspirin 複方） |
| 原適應症 | 慢性狹心症、冠狀動脈不全、血小板凝集降低、心肌灌流造影替代運動試驗 |
| 預測新適應症 | Prinzmetal angina、stroke disorder、thrombotic disease、atrial fibrillation (disease)、sick sinus syndrome 2, autosomal dominant、transient ischemic attack (disease)、sarcoglycanopathy、Wildervanck syndrome、macrocephaly, dysmorphic facies, and psychomotor retardation、lateral sinus thrombosis |
| 最高 TxGNN 分數 | 0.9999 (Prinzmetal angina) |
| 臨床試驗支持 | **豐富** (中風預防) |
| 文獻支持 | **豐富** |





## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. Prinzmetal angina</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.99%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>### 機轉分析</p>

<ol>
<li><strong>變異型心絞痛 (Prinzmetal angina)</strong>：</li>
</ol>
<ul>
<li>TxGNN 分數 0.9999，排名 438</li>
<li>Dipyridamole 是冠狀動脈血管擴張劑</li>
<li>理論上可緩解冠狀動脈痙攣</li>
<li>但文獻顯示其對變異型心絞痛的效果不一，部分研究甚至指出無效或可能加重症狀</li>
<li><strong>注意</strong>：此預測與原適應症「慢性狹心症」高度重疊</li>

</ul>
<ol>
<li><strong>中風 (stroke disorder)</strong>：</li>
</ol>
<ul>
<li>TxGNN 分數 0.9995，排名 1695</li>
<li>Dipyridamole 抑制血小板凝集</li>
<li>與 aspirin 合用已被廣泛用於缺血性中風的二級預防</li>
<li><strong>重要</strong>：Aggrenox (dipyridamole + aspirin) 已是核准適應症</li>
</ul>

<h3>臨床試驗</h3>

<p>目前無針對此特定適應症的臨床試驗登記。</p>

<h3>相關文獻</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/633593/" target="_blank">633593</a></td><td>1978</td><td>Article</td><td>Japanese circulation journal</td><td>Pathogenesis and treatment of angina pectoris at rest as seen from its response ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/3421166/" target="_blank">3421166</a></td><td>1988</td><td>Article</td><td>The American journal of cardio</td><td>Aminophylline termination of dipyridamole stress as a trigger of coronary vasosp...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/3190956/" target="_blank">3190956</a></td><td>1988</td><td>Article</td><td>British heart journal</td><td>Short term reproducibility of exercise testing in patients with ST segment eleva...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/16630456/" target="_blank">16630456</a></td><td>2006</td><td>Article</td><td>Zhonghua xin xue guan bing za </td><td>[Clinical features of patients with atypical coronary artery spasm].</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/8417062/" target="_blank">8417062</a></td><td>1993</td><td>Article</td><td>Journal of the American Colleg</td><td>Increased echodensity of transiently asynergic myocardium in humans: a novel ech...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/8634169/" target="_blank">8634169</a></td><td>1996</td><td>Article</td><td>Revista portuguesa de cardiolo</td><td>[The 3-year prognosis of patients with suspected coronary disease and a normal m...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/6779029/" target="_blank">6779029</a></td><td>1981</td><td>Article</td><td>Japanese circulation journal</td><td>Noninvasive detection of coronary artery disease by myocardial imaging with thal...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/6125623/" target="_blank">6125623</a></td><td>1982</td><td>Article</td><td>Kardiologiia</td><td>[Current diagnostic and treatment problems in stenocardia].</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/3915223/" target="_blank">3915223</a></td><td>1985</td><td>Article</td><td>Cardiologia (Rome, Italy)</td><td>[Effects of other provoking tests on cardiovascular function].</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/7628141/" target="_blank">7628141</a></td><td>1995</td><td>Article</td><td>Clinical nuclear medicine</td><td>Is cardiac migraine a clinical entity?</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/6775030/" target="_blank">6775030</a></td><td>1980</td><td>Article</td><td>The Journal of the Indiana Sta</td><td>The five fingers of cardiology.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2022043/" target="_blank">2022043</a></td><td>1991</td><td>Article</td><td>Circulation</td><td>Pathophysiological basis for noninvasive functional evaluation of coronary steno...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2221701/" target="_blank">2221701</a></td><td>1990</td><td>Article</td><td>Annals of the New York Academy</td><td>Electrocardiographic diagnosis of transient myocardial ischemia. Sensitivity, sp...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/14050937/" target="_blank">14050937</a></td><td>1963</td><td>Article</td><td>Naika. Internal medicine</td><td>[4 CASES OF A VARIANT FORM OF ANGINA PECTORIS].</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/14060538/" target="_blank">14060538</a></td><td>1963</td><td>Article</td><td>Naika. Internal medicine</td><td>[CASE OF VARIANT FORM OF ANGINA PECTORIS].</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. stroke disorder</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.95%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（31 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02966119" target="_blank">NCT02966119</a></td><td>PHASE3</td><td>TERMINATED</td><td>23</td><td>Evaluation of the Benefit/Risk Ratio of Restarting or Avoiding Antiplatelet Drug...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01781611" target="_blank">NCT01781611</a></td><td>NA</td><td>TERMINATED</td><td>18</td><td>Dipyridamole Assessment for Flare Reduction in SLE</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06983795" target="_blank">NCT06983795</a></td><td>N/A</td><td>NOT_YET_RECRUITING</td><td>1000</td><td>Pioneering Advancements in Cardiocerebrovascular Interactions in the Asia pacFIC...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01528800" target="_blank">NCT01528800</a></td><td>PHASE2</td><td>COMPLETED</td><td>85</td><td>Inhibit Progression of Coronary Artery Calcification With Vitamin K in HemoDialy...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03993119" target="_blank">NCT03993119</a></td><td>N/A</td><td>COMPLETED</td><td>500</td><td>Non-Interventional, Cross-sectional Study to Describe NOACs Management in Elderl...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00134433" target="_blank">NCT00134433</a></td><td>PHASE1, PHASE2</td><td>COMPLETED</td><td>20</td><td>Endothelial Modulation With L-Arginine in Patients Undergoing Angiogenic Therapy...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00738894" target="_blank">NCT00738894</a></td><td>NA</td><td>COMPLETED</td><td>664</td><td>GORE® HELEX® Septal Occluder / GORE® CARDIOFORM Septal Occluder and Antiplatelet...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00562588" target="_blank">NCT00562588</a></td><td>PHASE4</td><td>COMPLETED</td><td>551</td><td>EARLY: Prospective, Randomised, National, Multi-centre, Open-label, Blinded Endp...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01613755" target="_blank">NCT01613755</a></td><td>PHASE4</td><td>COMPLETED</td><td>18</td><td>The Effect of Dipyridamole on the Pharmacokinetics of Metformin</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00153062" target="_blank">NCT00153062</a></td><td>PHASE4</td><td>COMPLETED</td><td>20332</td><td>PRoFESS - Prevention Regimen For Effectively Avoiding Second Strokes: A Double-b...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00161070" target="_blank">NCT00161070</a></td><td>PHASE4</td><td>COMPLETED</td><td>4500</td><td>ESPRIT: European/Australasian Stroke Prevention in Reversible Ischaemia Trial</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00627783" target="_blank">NCT00627783</a></td><td>NA</td><td>TERMINATED</td><td>642</td><td>Randomized Strategy Trial Comparing Detection of Silent Ischemia With no Detecti...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01295567" target="_blank">NCT01295567</a></td><td>PHASE4</td><td>COMPLETED</td><td>95</td><td>Can Dipyridamole Induce Protection Against Ischemia and Reperfusion Injury in Pa...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02468102" target="_blank">NCT02468102</a></td><td>N/A</td><td>COMPLETED</td><td>99999</td><td>A Pharmacoepidemiological Study of Rivaroxaban Use and Potential Adverse Outcome...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT07137104" target="_blank">NCT07137104</a></td><td>PHASE1, PHASE2</td><td>NOT_YET_RECRUITING</td><td>39</td><td>A Phase I/IIa Study to Investigate the Safety, Tolerability, and Preliminary Eff...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01947998" target="_blank">NCT01947998</a></td><td>N/A</td><td>COMPLETED</td><td>50299</td><td>A Pharmacoepidemiological Study of Rivaroxaban Use and Potential Adverse Outcome...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00238667" target="_blank">NCT00238667</a></td><td>PHASE3</td><td>COMPLETED</td><td>250</td><td>Cervical Artery Dissection in Stroke Study</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00562289" target="_blank">NCT00562289</a></td><td>PHASE3</td><td>COMPLETED</td><td>664</td><td>Closure of Patent Foramen Ovale or Anticoagulants Versus Antiplatelet Therapy to...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01661322" target="_blank">NCT01661322</a></td><td>PHASE3</td><td>TERMINATED</td><td>3096</td><td>Safety and Efficacy of Intensive Versus Guideline Antiplatelet Therapy in High R...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06899399" target="_blank">NCT06899399</a></td><td>NA</td><td>RECRUITING</td><td>982</td><td>Efficacy and Safety Study of Endovascular Treatment of Asymptomatic Carotid Arte...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05081115" target="_blank">NCT05081115</a></td><td>N/A</td><td>RECRUITING</td><td>10000</td><td>The International Stress Echo Study to to Define the Future of Imaging</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01947985" target="_blank">NCT01947985</a></td><td>N/A</td><td>COMPLETED</td><td>208958</td><td>A Pharmacoepidemiological Study of Rivaroxaban Use and Potential Adverse Outcome...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02565693" target="_blank">NCT02565693</a></td><td>PHASE2</td><td>COMPLETED</td><td>101</td><td>Apixaban Versus Antiplatelet Drugs or no Antithrombotic Drugs After Anticoagulat...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06549582" target="_blank">NCT06549582</a></td><td>NA</td><td>NOT_YET_RECRUITING</td><td>160</td><td>Effect of Taohong Tongluo Xiaoban Prescription on Reprogramming of Lipid Metabol...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02630862" target="_blank">NCT02630862</a></td><td>NA</td><td>COMPLETED</td><td>240</td><td>Oxidative Stress and Oxysterols Profiling in Patients With Carotid Revasculariza...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04666454" target="_blank">NCT04666454</a></td><td>PHASE4</td><td>RECRUITING</td><td>1000</td><td>BROKEN-SWEDEHEART- Optimized Pharmacological Treatment for Broken Heart (Takotsu...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00311402" target="_blank">NCT00311402</a></td><td>PHASE3</td><td>COMPLETED</td><td>1295</td><td>JASAP: Japanese Aggrenox Stroke Prevention vs. Aspirin Programme, Phase III Stud...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01947959" target="_blank">NCT01947959</a></td><td>N/A</td><td>COMPLETED</td><td>665533</td><td>A Pharmacoepidemiological Study of Rivaroxaban Use and Potential Adverse Outcome...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05763862" target="_blank">NCT05763862</a></td><td>NA</td><td>RECRUITING</td><td>350</td><td>Genotype Guided Antiplatelet Therapy in Ischemic Stroke</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00465270" target="_blank">NCT00465270</a></td><td>NA</td><td>COMPLETED</td><td>980</td><td>Randomized Evaluation of Recurrent Stroke Comparing PFO Closure to Established C...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06053021" target="_blank">NCT06053021</a></td><td>NA</td><td>UNKNOWN</td><td>1200</td><td>Antiplatelet Therapy for Acute Ischemic Stroke Patients With Thrombocytopenia</td></tr>
</tbody>
</table>

<h3>相關文獻（18 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/11786451/" target="_blank">11786451</a></td><td>2002</td><td>Article</td><td>BMJ (Clinical research ed.)</td><td>Collaborative meta-analysis of randomised trials of antiplatelet therapy for pre...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/27816341/" target="_blank">27816341</a></td><td>2016</td><td>Article</td><td>Presse medicale (Paris, France</td><td>Stroke prevention.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/4119751/" target="_blank">4119751</a></td><td>1973</td><td>Article</td><td>Lancet (London, England)</td><td>Glycerol and stroke.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/9064773/" target="_blank">9064773</a></td><td>1997</td><td>Article</td><td>Science (New York, N.Y.)</td><td>Aspirin and stroke.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/16102029/" target="_blank">16102029</a></td><td>2005</td><td>Article</td><td>Journal of thrombosis and haem</td><td>Preventable stroke and stroke prevention.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/18342579/" target="_blank">18342579</a></td><td>2008</td><td>Article</td><td>Vascular pharmacology</td><td>Dipyridamole, cerebrovascular disease, and the vasculature.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/20955428/" target="_blank">20955428</a></td><td>2010</td><td>Article</td><td>Annals of the New York Academy</td><td>Effect of dipyridamole during acute stroke: exploring antithrombosis and neuropr...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/26274799/" target="_blank">26274799</a></td><td>2015</td><td>Article</td><td>Journal of comparative effecti</td><td>Antiplatelet therapies for secondary stroke prevention: an update on clinical an...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/30649687/" target="_blank">30649687</a></td><td>2019</td><td>Article</td><td>CNS drugs</td><td>Combination Therapy with Dipyridamole and Clopidogrel for Secondary Stroke Preve...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/15569877/" target="_blank">15569877</a></td><td>2005</td><td>Article</td><td>Stroke</td><td>Dipyridamole for preventing recurrent ischemic stroke and other vascular events:...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/12765506/" target="_blank">12765506</a></td><td>2003</td><td>Article</td><td>The Medical journal of Austral</td><td>Antiplatelet drugs.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/9744826/" target="_blank">9744826</a></td><td>1998</td><td>Article</td><td>Neurology</td><td>Dipyridamole trials in stroke prevention.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/18356634/" target="_blank">18356634</a></td><td>2008</td><td>Article</td><td>American journal of therapeuti</td><td>Acute ischemic coronary artery disease and ischemic stroke: similarities and dif...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/17389280/" target="_blank">17389280</a></td><td>2007</td><td>Article</td><td>Circulation</td><td>Secondary prevention of stroke and transient ischemic attack: is more platelet i...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/10543686/" target="_blank">10543686</a></td><td>1999</td><td>Article</td><td>Lancet (London, England)</td><td>Treatment and secondary prevention of stroke: evidence, costs, and effects on in...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/12535415/" target="_blank">12535415</a></td><td>2003</td><td>Article</td><td>The Cochrane database of syste</td><td>Dipyridamole for preventing stroke and other vascular events in patients with va...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/382146/" target="_blank">382146</a></td><td>1979</td><td>Article</td><td>Postgraduate medicine</td><td>Antiplatelet drugs in thromboembolism.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/17636684/" target="_blank">17636684</a></td><td>2007</td><td>Article</td><td>The Cochrane database of syste</td><td>Dipyridamole for preventing stroke and other vascular events in patients with va...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. thrombotic disease</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.94%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（2 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01528800" target="_blank">NCT01528800</a></td><td>PHASE2</td><td>COMPLETED</td><td>85</td><td>Inhibit Progression of Coronary Artery Calcification With Vitamin K in HemoDialy...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01661322" target="_blank">NCT01661322</a></td><td>PHASE3</td><td>TERMINATED</td><td>3096</td><td>Safety and Efficacy of Intensive Versus Guideline Antiplatelet Therapy in High R...</td></tr>
</tbody>
</table>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/26719230/" target="_blank">26719230</a></td><td>2016</td><td>Article</td><td>Lancet (London, England)</td><td>Bevacizumab for newly diagnosed pleural mesothelioma in the Mesothelioma Avastin...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36696191/" target="_blank">36696191</a></td><td>2023</td><td>Article</td><td>Journal of thrombosis and haem</td><td>Targeting thromboinflammation in antiphospholipid syndrome.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2107174/" target="_blank">2107174</a></td><td>1990</td><td>Article</td><td>Hematology/oncology clinics of</td><td>Thrombotic thrombocytopenic purpura and related disorders.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/382146/" target="_blank">382146</a></td><td>1979</td><td>Article</td><td>Postgraduate medicine</td><td>Antiplatelet drugs in thromboembolism.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/32574107/" target="_blank">32574107</a></td><td>2020</td><td>Article</td><td>Emerging microbes &amp; infections</td><td>Kawasaki-like diseases and thrombotic coagulopathy in COVID-19: delayed over-act...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/559478/" target="_blank">559478</a></td><td>1977</td><td>Article</td><td>Archives of internal medicine</td><td>Platelet-latelet-.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/33760800/" target="_blank">33760800</a></td><td>2021</td><td>Article</td><td>Journal of cardiovascular phar</td><td>Revisiting the Evidence for Dipyridamole in Reducing Restenosis: A Systematic Re...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2182246/" target="_blank">2182246</a></td><td>1990</td><td>Article</td><td>Clinical cardiology</td><td>Aspirin and dipyridamole and their limitations in the therapy of coronary artery...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/18174451/" target="_blank">18174451</a></td><td>2008</td><td>Article</td><td>Arteriosclerosis, thrombosis, </td><td>Translational therapeutics of dipyridamole.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/15494585/" target="_blank">15494585</a></td><td>2004</td><td>Article</td><td>JAMA</td><td>Oral antiplatelet therapy in cerebrovascular disease, coronary artery disease, a...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/20484211/" target="_blank">20484211</a></td><td>2010</td><td>Article</td><td>American journal of health-sys</td><td>Effects of antiplatelet and anticoagulant medications on the vasoocclusive and t...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/15095934/" target="_blank">15095934</a></td><td>2004</td><td>Article</td><td>Journal of the American Pharma</td><td>Peripheral arterial disease: pathophysiology, risk factors, and role of antithro...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/786606/" target="_blank">786606</a></td><td>1976</td><td>Article</td><td>Drugs</td><td>Antithrombotic drugs: part II.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/379914/" target="_blank">379914</a></td><td>1979</td><td>Article</td><td>Progress in cardiovascular dis</td><td>The role of platelets in thrombotic and vascular disease.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/19160220/" target="_blank">19160220</a></td><td>2009</td><td>Article</td><td>The Cochrane database of syste</td><td>Interventions for haemolytic uraemic syndrome and thrombotic thrombocytopenic pu...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/8123958/" target="_blank">8123958</a></td><td>1994</td><td>Article</td><td>The Annals of pharmacotherapy</td><td>Heparin-induced thrombotic thrombocytopenia.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/37350766/" target="_blank">37350766</a></td><td>2023</td><td>Article</td><td>Journal of Crohn&#x27;s &amp; colitis</td><td>Gut Microbiome-Generated Phenylacetylglutamine from Dietary Protein is Associate...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28707198/" target="_blank">28707198</a></td><td>2017</td><td>Article</td><td>Cancer metastasis reviews</td><td>Platelet-targeted pharmacologic treatments as anti-cancer therapy.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/15461876/" target="_blank">15461876</a></td><td>2004</td><td>Article</td><td>Health technology assessment (</td><td>Clinical effectiveness and cost-effectiveness of clopidogrel and modified-releas...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/7025599/" target="_blank">7025599</a></td><td>1981</td><td>Article</td><td>American family physician</td><td>Antiplatelet therapy.</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. sick sinus syndrome 2, autosomal dominant</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.89%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. transient ischemic attack (disease)</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.87%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（15 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06983795" target="_blank">NCT06983795</a></td><td>N/A</td><td>NOT_YET_RECRUITING</td><td>1000</td><td>Pioneering Advancements in Cardiocerebrovascular Interactions in the Asia pacFIC...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00027170" target="_blank">NCT00027170</a></td><td>N/A</td><td>COMPLETED</td><td>8781</td><td>Technical Development of Cardiovascular Magnetic Resonance Imaging</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01528800" target="_blank">NCT01528800</a></td><td>PHASE2</td><td>COMPLETED</td><td>85</td><td>Inhibit Progression of Coronary Artery Calcification With Vitamin K in HemoDialy...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03993119" target="_blank">NCT03993119</a></td><td>N/A</td><td>COMPLETED</td><td>500</td><td>Non-Interventional, Cross-sectional Study to Describe NOACs Management in Elderl...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00738894" target="_blank">NCT00738894</a></td><td>NA</td><td>COMPLETED</td><td>664</td><td>GORE® HELEX® Septal Occluder / GORE® CARDIOFORM Septal Occluder and Antiplatelet...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00562588" target="_blank">NCT00562588</a></td><td>PHASE4</td><td>COMPLETED</td><td>551</td><td>EARLY: Prospective, Randomised, National, Multi-centre, Open-label, Blinded Endp...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01613755" target="_blank">NCT01613755</a></td><td>PHASE4</td><td>COMPLETED</td><td>18</td><td>The Effect of Dipyridamole on the Pharmacokinetics of Metformin</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00161070" target="_blank">NCT00161070</a></td><td>PHASE4</td><td>COMPLETED</td><td>4500</td><td>ESPRIT: European/Australasian Stroke Prevention in Reversible Ischaemia Trial</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02468102" target="_blank">NCT02468102</a></td><td>N/A</td><td>COMPLETED</td><td>99999</td><td>A Pharmacoepidemiological Study of Rivaroxaban Use and Potential Adverse Outcome...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01661322" target="_blank">NCT01661322</a></td><td>PHASE3</td><td>TERMINATED</td><td>3096</td><td>Safety and Efficacy of Intensive Versus Guideline Antiplatelet Therapy in High R...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03688815" target="_blank">NCT03688815</a></td><td>N/A</td><td>COMPLETED</td><td>50</td><td>Relationship Between the L-arginine Pathway Metabolites and Dipyridamole Stress ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06549582" target="_blank">NCT06549582</a></td><td>NA</td><td>NOT_YET_RECRUITING</td><td>160</td><td>Effect of Taohong Tongluo Xiaoban Prescription on Reprogramming of Lipid Metabol...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02630862" target="_blank">NCT02630862</a></td><td>NA</td><td>COMPLETED</td><td>240</td><td>Oxidative Stress and Oxysterols Profiling in Patients With Carotid Revasculariza...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00311402" target="_blank">NCT00311402</a></td><td>PHASE3</td><td>COMPLETED</td><td>1295</td><td>JASAP: Japanese Aggrenox Stroke Prevention vs. Aspirin Programme, Phase III Stud...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05763862" target="_blank">NCT05763862</a></td><td>NA</td><td>RECRUITING</td><td>350</td><td>Genotype Guided Antiplatelet Therapy in Ischemic Stroke</td></tr>
</tbody>
</table>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/11786451/" target="_blank">11786451</a></td><td>2002</td><td>Article</td><td>BMJ (Clinical research ed.)</td><td>Collaborative meta-analysis of randomised trials of antiplatelet therapy for pre...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35470408/" target="_blank">35470408</a></td><td>2022</td><td>Article</td><td>Acta neurologica Thailandica</td><td>Antiplatelets and Anticoagulants in Ischemic Stroke,Transient Ischaemic Attack: ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/26304937/" target="_blank">26304937</a></td><td>2015</td><td>Article</td><td>Journal of the American Heart </td><td>Long-Term Antiplatelet Mono- and Dual Therapies After Ischemic Stroke or Transie...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/17389280/" target="_blank">17389280</a></td><td>2007</td><td>Article</td><td>Circulation</td><td>Secondary prevention of stroke and transient ischemic attack: is more platelet i...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/24157563/" target="_blank">24157563</a></td><td>2014</td><td>Article</td><td>Frontiers of neurology and neu</td><td>Antithrombotic therapy in transient ischemic attack patients.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/26042726/" target="_blank">26042726</a></td><td>2015</td><td>Article</td><td>Platelets</td><td>Platelet function testing in transient ischaemic attack and ischaemic stroke: A ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/22277143/" target="_blank">22277143</a></td><td>2012</td><td>Article</td><td>Journal of clinical hypertensi</td><td>Antiplatelet therapy for transient ischemic attack.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/15569877/" target="_blank">15569877</a></td><td>2005</td><td>Article</td><td>Stroke</td><td>Dipyridamole for preventing recurrent ischemic stroke and other vascular events:...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/12535415/" target="_blank">12535415</a></td><td>2003</td><td>Article</td><td>The Cochrane database of syste</td><td>Dipyridamole for preventing stroke and other vascular events in patients with va...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/34399713/" target="_blank">34399713</a></td><td>2021</td><td>Article</td><td>BMC neurology</td><td>Antiplatelet drugs for secondary prevention in patients with ischemic stroke or ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/12765506/" target="_blank">12765506</a></td><td>2003</td><td>Article</td><td>The Medical journal of Austral</td><td>Antiplatelet drugs.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/18454579/" target="_blank">18454579</a></td><td>2008</td><td>Article</td><td>The Consultant pharmacist : th</td><td>Urgent need for secondary stroke prevention after transient ischemic attack.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/31177983/" target="_blank">31177983</a></td><td>2019</td><td>Article</td><td>Stroke</td><td>Antiplatelet Therapy After Noncardioembolic Stroke.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/22282894/" target="_blank">22282894</a></td><td>2012</td><td>Article</td><td>Stroke</td><td>Dual or mono antiplatelet therapy for patients with acute ischemic stroke or tra...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/17636684/" target="_blank">17636684</a></td><td>2007</td><td>Article</td><td>The Cochrane database of syste</td><td>Dipyridamole for preventing stroke and other vascular events in patients with va...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/18343263/" target="_blank">18343263</a></td><td>2008</td><td>Article</td><td>Clinical therapeutics</td><td>Antiplatelet profiles of the fixed-dose combination of extended-release dipyrida...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/17847044/" target="_blank">17847044</a></td><td>2007</td><td>Article</td><td>Clinical cardiology</td><td>Antiplatelet therapy in cerebrovascular disease: implications of Management of A...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/22145656/" target="_blank">22145656</a></td><td>2011</td><td>Article</td><td>Journal of the American Academ</td><td>Preventing recurrent cerebrovascular events in patients with stroke or transient...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/20170841/" target="_blank">20170841</a></td><td>2010</td><td>Article</td><td>The Lancet. Neurology</td><td>Antithrombotic drugs for patients with ischaemic stroke and transient ischaemic ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/17877660/" target="_blank">17877660</a></td><td>2007</td><td>Article</td><td>International journal of clini</td><td>Prevention of secondary stroke and transient ischaemic attack with antiplatelet ...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. sarcoglycanopathy</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.82%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. Wildervanck syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.78%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. macrocephaly, dysmorphic facies, and psychomotor retardation</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.77%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. cavernous sinus thrombosis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.72%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. lateral sinus thrombosis</span>
<span class="evidence-badge evidence-L3">L3</span>
<span class="prediction-score">99.72%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（1 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01528800" target="_blank">NCT01528800</a></td><td>PHASE2</td><td>COMPLETED</td><td>85</td><td>Inhibit Progression of Coronary Artery Calcification With Vitamin K in HemoDialy...</td></tr>
</tbody>
</table>

</div>
</details>


## 泰國上市狀態

| 許可證號 | 商品名 | 劑型 | 適應症 | 狀態 |
|----------|--------|------|--------|------|
| 多項 | 百心康等 | 錠劑/膠囊 | 慢性狹心症、血小板凝集降低 | 部分有效 |

**備註**：Aggrenox（dipyridamole + aspirin 複方）國際上用於中風預防，泰國需確認是否有上市。

## 安全性

### 藥物交互作用

Dipyridamole 的主要交互作用與其腺苷再攝取抑制作用相關：

| 併用藥物 | 注意事項 |
|----------|----------|
| Adenosine | 增強腺苷作用，需調整劑量 |
| 抗凝血劑 | 增加出血風險 |
| 抗血小板藥物 | 出血風險加成 |

### 重要警語

- 不穩定型心絞痛或急性心肌梗塞期間應謹慎使用
- 低血壓風險
- 可能引起頭痛、頭暈

## 結論

### 整體評估：已有成熟適應症

Dipyridamole 的 TxGNN 預測雖然分數很高，但兩項主要預測都與現有適應症高度重疊：

1. **變異型心絞痛**：文獻證據矛盾，且部分研究顯示無效
2. **中風預防**：Dipyridamole + aspirin 複方已是確立的二級預防方案

### 建議

1. **不需要**進行新適應症研究，因為預測的適應症已是現有用途或其延伸
2. 對於變異型心絞痛，現有證據不支持將 dipyridamole 作為首選治療
3. 中風預防應優先考慮 Aggrenox 複方或其他已證實有效的抗血小板方案

### 證據等級總結

| 預測適應症 | TxGNN 分數 | 臨床試驗 | 文獻支持 | 機轉合理性 | 綜合評估 |
|------------|------------|----------|----------|------------|----------|
| Prinzmetal angina | 0.9999 | 診斷用途 | 有（但矛盾） | 中等 | 與原適應症重疊，效果存疑 |
| 中風 | 0.9995 | **豐富** | **豐富** | 高 | 已為適應症（複方） |

---
*報告產生日期：2026-02-11*
*資料來源：TxGNN 預測、ClinicalTrials.gov、PubMed、泰國 FDA*


---

## 相關藥物報告

- [Tenofovir Alafenamide]({{ "/drugs/tenofovir_alafenamide/" | relative_url }}) - 證據等級 L5
- [Titanium Dioxide]({{ "/drugs/titanium_dioxide/" | relative_url }}) - 證據等級 L5
- [Berberine]({{ "/drugs/berberine/" | relative_url }}) - 證據等級 L5
- [Sodium Citrate]({{ "/drugs/sodium_citrate/" | relative_url }}) - 證據等級 L5
- [Mannitol]({{ "/drugs/mannitol/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
ThTxGNN. (2026). Dipyridamole老藥新用驗證報告. https://thtxgnn.yao.care/drugs/dipyridamole/
```

**BibTeX 格式：**
```bibtex
@misc{thtxgnn_dipyridamole,
  title = {Dipyridamole老藥新用驗證報告},
  author = {ThTxGNN Team},
  year = {2026},
  url = {https://thtxgnn.yao.care/drugs/dipyridamole/}
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
