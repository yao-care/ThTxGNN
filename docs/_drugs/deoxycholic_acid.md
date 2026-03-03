---
layout: default
title: Deoxycholic Acid
description: "Deoxycholic Acid 的老藥新用潛力分析。模型預測等級 L5，包含 3 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 56
evidence_level: L4
indication_count: 3
---

# Deoxycholic Acid

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>3</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Deoxycholic Acid (去氧膽酸) - 藥師評估報告

## 一句話總結

<p class="key-answer" data-question="Deoxycholic Acid 可以用於治療什麼新適應症？">
Deoxycholic acid 是一種膽酸類藥物，用於膽結石溶解和皮下脂肪消除；TxGNN 預測其可能用於罕見遺傳性眼疾和糖尿病腎病，但這些預測的機轉連結薄弱，臨床轉化可能性低。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Deoxycholic acid (去氧膽酸) |
| DrugBank ID | DB03619 |
| 泰國商品名 | 去氧熊膽酸、Deoxycholic acid 等 |
| 原適應症 | 膽固醇性膽結石溶解、原發性膽道肝硬化、頦下脂肪消除 |
| 預測新適應症 | 家族性血尿-視網膜動脈迂曲-攣縮症候群、腦小血管病變、糖尿病腎病 |
| 最高 TxGNN 分數 | 0.9948 |
| 臨床試驗支持 | 無 |
| 文獻支持 | 間接有 (糖尿病腎病相關) |





## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.49%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>### 機轉分析</p>

<ol>
<li><strong>家族性血尿-視網膜動脈迂曲-攣縮症候群 (autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome)</strong>：</li>
</ol>
<ul>
<li>這是一種極為罕見的遺傳性疾病</li>
<li>TxGNN 分數 0.9948，但無任何文獻支持</li>
<li>機轉連結極為薄弱</li>

</ul>
<ol>
<li><strong>腦小血管病變伴或不伴眼部異常 (brain small vessel disease 1)</strong>：</li>
</ol>
<ul>
<li>TxGNN 分數 0.9948</li>
<li>有多篇文獻涉及眼部發育異常，但與膽酸無直接關聯</li>
<li>預測可能源於知識圖譜中的間接關聯</li>

</ul>
<ol>
<li><strong>糖尿病腎病 (diabetic nephropathy)</strong>：</li>
</ol>
<ul>
<li>TxGNN 分數 0.9932</li>
<li>有較多相關文獻支持膽酸在糖尿病腎病中的保護作用</li>
<li>機轉：膽酸可作為 FXR (farnesoid X receptor) 和 TGR5 的配體，調節糖脂代謝和發炎反應</li>
</ul>

<h3>臨床試驗</h3>

<p>目前無針對此特定適應症的臨床試驗登記。</p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. brain small vessel disease 1 with or without ocular anomalies</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.49%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（19 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35882526/" target="_blank">35882526</a></td><td>2023</td><td>Article</td><td>Journal of medical genetics</td><td>Axenfeld-Rieger syndrome: more than meets the eye.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/30182440/" target="_blank">30182440</a></td><td>2018</td><td>Article</td><td>American journal of medical ge</td><td>Neuropathology of holoprosencephaly.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/33870948/" target="_blank">33870948</a></td><td>2022</td><td>Article</td><td>Journal of neuro-ophthalmology</td><td>Optic Nerve Aplasia.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/11941259/" target="_blank">11941259</a></td><td>2002</td><td>Article</td><td>Journal francais d&#x27;ophtalmolog</td><td>[Congenital megalocornea].</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/6390155/" target="_blank">6390155</a></td><td>1983</td><td>Article</td><td>Neurologic clinics</td><td>Optic disk abnormalities.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/10498002/" target="_blank">10498002</a></td><td>1999</td><td>Article</td><td>Optometry and vision science :</td><td>Tilted disc syndrome.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/22963965/" target="_blank">22963965</a></td><td>2012</td><td>Article</td><td>Annales de dermatologie et de </td><td>[Branchio-oculo-facial syndrome].</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/1458324/" target="_blank">1458324</a></td><td>1992</td><td>Article</td><td>The Veterinary clinics of Nort</td><td>Congenital ocular anomalies.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/11581073/" target="_blank">11581073</a></td><td>2001</td><td>Article</td><td>Ophthalmology</td><td>Renal coloboma syndrome.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/406376/" target="_blank">406376</a></td><td>1977</td><td>Article</td><td>Journal of pediatric ophthalmo</td><td>Peters-Rieger&#x27;s syndrome.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36636984/" target="_blank">36636984</a></td><td>2023</td><td>Article</td><td>Ophthalmic genetics</td><td>Congenital inner eyelid folds.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2036354/" target="_blank">2036354</a></td><td>1991</td><td>Article</td><td>The British journal of ophthal</td><td>Ablepharon macrostomia syndrome.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/3050099/" target="_blank">3050099</a></td><td>1988</td><td>Article</td><td>Journal of medical genetics</td><td>The telecanthus-hypospadias syndrome.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36926528/" target="_blank">36926528</a></td><td>2023</td><td>Article</td><td>Clinical ophthalmology (Auckla</td><td>Ophthalmological Manifestations of Axenfeld-Rieger Syndrome: Current Perspective...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/37468646/" target="_blank">37468646</a></td><td>2024</td><td>Article</td><td>Pediatric nephrology (Berlin, </td><td>Ocular manifestations of congenital anomalies of the kidney and urinary tract (C...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35791156/" target="_blank">35791156</a></td><td>2022</td><td>Article</td><td>Indian journal of ophthalmolog</td><td>Clinical features and orbital anomalies in Fraser syndrome and a review of manag...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/16848213/" target="_blank">16848213</a></td><td>2006</td><td>Article</td><td>Acta medica Croatica : casopis</td><td>[Distichiasis].</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/30452766/" target="_blank">30452766</a></td><td>2018</td><td>Article</td><td>Journal of pediatric ophthalmo</td><td>Systemic Associations of Childhood Glaucoma: A Review.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/29133973/" target="_blank">29133973</a></td><td>2017</td><td>Article</td><td>Clinical ophthalmology (Auckla</td><td>Duane retraction syndrome: causes, effects and management strategies.</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. diabetic nephropathy</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.32%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/29089371/" target="_blank">29089371</a></td><td>2018</td><td>Article</td><td>Journal of the American Societ</td><td>FXR/TGR5 Dual Agonist Prevents Progression of Nephropathy in Diabetes and Obesit...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/27193377/" target="_blank">27193377</a></td><td>2016</td><td>Article</td><td>Biological &amp; pharmaceutical bu</td><td>Ursodeoxycholic Acid Ameliorated Diabetic Nephropathy by Attenuating Hyperglycem...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/26999661/" target="_blank">26999661</a></td><td>2016</td><td>Article</td><td>Laboratory investigation; a jo</td><td>Ursodeoxycholic acid and 4-phenylbutyrate prevent endoplasmic reticulum stress-i...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/30224065/" target="_blank">30224065</a></td><td>2018</td><td>Article</td><td>Biochemical and biophysical re</td><td>ERp44 depletion exacerbates ER stress and aggravates diabetic nephropathy in db/...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38377553/" target="_blank">38377553</a></td><td>2024</td><td>Article</td><td>ACS biomaterials science &amp; eng</td><td>Intestinal Absorption of Nanoparticles to Reduce Oxidative Stress and Vasoconstr...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/33378964/" target="_blank">33378964</a></td><td>2021</td><td>Article</td><td>Biomedicine &amp; pharmacotherapy </td><td>QiDiTangShen granules modulated the gut microbiome composition and improved bile...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/29941869/" target="_blank">29941869</a></td><td>2019</td><td>Article</td><td>Acta pharmacologica Sinica</td><td>Magnesium lithospermate B improves the gut microbiome and bile acid metabolic pr...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39384774/" target="_blank">39384774</a></td><td>2024</td><td>Article</td><td>Nutrition &amp; diabetes</td><td>Metabolomic profiling reveals the step-wise alteration of bile acid metabolism i...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/22429686/" target="_blank">22429686</a></td><td>2012</td><td>Article</td><td>Diabetes research and clinical</td><td>Ursodeoxycholic acid decreases sodium-glucose cotransporter (SGLT2) expression a...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36996678/" target="_blank">36996678</a></td><td>2023</td><td>Article</td><td>Biomedicine &amp; pharmacotherapy </td><td>Relaxin elicits renoprotective actions accompanied by increasing bile acid level...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28696246/" target="_blank">28696246</a></td><td>2017</td><td>Article</td><td>Journal of the American Societ</td><td>Farnesoid X Receptor Agonism Protects against Diabetic Tubulopathy: Potential Ad...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36690052/" target="_blank">36690052</a></td><td>2023</td><td>Article</td><td>European journal of pharmacolo</td><td>Evaluating the potential of tauroursodeoxycholic acid as add-on therapy in ameli...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/26655953/" target="_blank">26655953</a></td><td>2016</td><td>Article</td><td>The Journal of biological chem</td><td>Farnesoid X Receptor Protects against Kidney Injury in Uninephrectomized Obese M...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/37790634/" target="_blank">37790634</a></td><td>2023</td><td>Article</td><td>PeerJ</td><td>Loss of Farnesoid X receptor (FXR) accelerates dysregulated glucose and renal in...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/31940200/" target="_blank">31940200</a></td><td>2020</td><td>Article</td><td>Journal of medicinal chemistry</td><td>Nidufexor (LMB763), a Novel FXR Modulator for the Treatment of Nonalcoholic Stea...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/27669287/" target="_blank">27669287</a></td><td>2016</td><td>Article</td><td>Nutrients</td><td>Tauroursodeoxycholic Acid Attenuates Renal Tubular Injury in a Mouse Model of Ty...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/23593240/" target="_blank">23593240</a></td><td>2013</td><td>Article</td><td>PloS one</td><td>Autophagy attenuates diabetic glomerular damage through protection of hyperglyce...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/23977286/" target="_blank">23977286</a></td><td>2013</td><td>Article</td><td>PloS one</td><td>Involvement of endoplasmic reticulum stress in albuminuria induced inflammasome ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/18648192/" target="_blank">18648192</a></td><td>2008</td><td>Article</td><td>American journal of nephrology</td><td>Effect of taurine-conjugated ursodeoxycholic acid on endoplasmic reticulum stres...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/12595495/" target="_blank">12595495</a></td><td>2003</td><td>Article</td><td>Journal of the American Societ</td><td>CTGF mediates TGF-beta-induced fibronectin matrix deposition by upregulating act...</td></tr>
</tbody>
</table>

</div>
</details>


## 泰國上市狀態

| 許可證號 | 商品名 | 劑型 | 適應症 | 狀態 |
|----------|--------|------|--------|------|
| 多項 | 去氧熊膽酸等 | 粉劑/膠囊 | 膽結石溶解、利膽 | 部分有效 |

**備註**：多數許可證已註銷，目前主要以 ursodeoxycholic acid 產品為主流。

## 安全性

### 藥物交互作用

本次資料未包含 deoxycholic acid 的詳細 DDI 資訊。

### 一般注意事項

- 口服製劑：可能引起腹瀉
- 注射製劑（用於頦下脂肪消除）：
  - 注射部位反應（腫脹、疼痛、麻木）
  - 可能造成神經損傷
  - 吞嚥困難（罕見）

## 結論

### 整體評估：低優先級

Deoxycholic acid 的 TxGNN 預測多為罕見遺傳疾病，臨床實用性低。糖尿病腎病的預測雖有機轉支持，但現有研究主要使用 UDCA 而非 deoxycholic acid，且 deoxycholic acid 的溶解作用可能對腎臟反而有潛在風險。

### 建議

1. **不建議**優先研究此藥物的新適應症
2. 若對膽酸類藥物在糖尿病腎病的應用有興趣，應優先考慮 UDCA
3. 罕見遺傳眼疾的預測缺乏實證基礎，不建議追蹤

### 證據等級總結

| 預測適應症 | TxGNN 分數 | 臨床試驗 | 文獻支持 | 機轉合理性 | 綜合評估 |
|------------|------------|----------|----------|------------|----------|
| 家族性血尿-視網膜動脈迂曲-攣縮症候群 | 0.9948 | 無 | 無 | 極低 | 不推薦 |
| 腦小血管病變伴眼部異常 | 0.9948 | 無 | 無 | 極低 | 不推薦 |
| 糖尿病腎病 | 0.9932 | 無 | 間接有 | 中等 | 考慮 UDCA |

---
*報告產生日期：2026-02-11*
*資料來源：TxGNN 預測、ClinicalTrials.gov、PubMed、泰國 FDA*


---

## 相關藥物報告

- [Disopyramide]({{ "/drugs/disopyramide/" | relative_url }}) - 證據等級 L5
- [Brivaracetam]({{ "/drugs/brivaracetam/" | relative_url }}) - 證據等級 L5
- [Methocarbamol]({{ "/drugs/methocarbamol/" | relative_url }}) - 證據等級 L5
- [Tioconazole]({{ "/drugs/tioconazole/" | relative_url }}) - 證據等級 L5
- [Atracurium Besylate]({{ "/drugs/atracurium_besylate/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
ThTxGNN. (2026). Deoxycholic Acid老藥新用驗證報告. https://thtxgnn.yao.care/drugs/deoxycholic_acid/
```

**BibTeX 格式：**
```bibtex
@misc{thtxgnn_deoxycholic_acid,
  title = {Deoxycholic Acid老藥新用驗證報告},
  author = {ThTxGNN Team},
  year = {2026},
  url = {https://thtxgnn.yao.care/drugs/deoxycholic_acid/}
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
