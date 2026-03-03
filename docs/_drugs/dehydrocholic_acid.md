---
layout: default
title: Dehydrocholic Acid
description: "Dehydrocholic Acid 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L4
indication_count: 10
---

# Dehydrocholic Acid

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Dehydrocholic Acid (去氫膽酸) - 藥師評估報告

## 一句話總結

<p class="key-answer" data-question="Dehydrocholic Acid 可以用於治療什麼新適應症？">
Dehydrocholic acid 是一種傳統利膽劑，TxGNN 預測其可能對膽道疾病和腎結石有潛在療效，但這些預測與其原有膽道適應症高度重疊，缺乏真正的新適應症發現價值。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Dehydrocholic acid (去氫膽酸/脫氫膽酸) |
| DrugBank ID | DB11622 |
| 泰國商品名 | 得利膽錠、派頓去氫膽酸錠 |
| 原適應症 | 利膽劑、膽石症、膽囊炎、膽道炎、肝硬化、黃疸 |
| 預測新適應症 | 急性尿酸腎病、腎結石、膽道疾病、膽管腫瘤 |
| 最高 TxGNN 分數 | 0.9999 (急性尿酸腎病) |
| 臨床試驗支持 | 無 |
| 文獻支持 | 部分 (膽道疾病相關) |





## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. acute urate nephropathy</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">100.00%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>### 機轉分析</p>

<ol>
<li><strong>膽道疾病 (bile duct disease)</strong>：TxGNN 分數 0.9999，但這與藥物原有的利膽適應症完全重疊，不具新藥再利用價值。</li>

<li><strong>腎結石 (nephrolithiasis)</strong>：TxGNN 分數 0.9999。理論上，dehydrocholic acid 可增加膽汁流動，可能影響膽固醇和膽鹽代謝，間接影響某些類型結石的形成。但目前無直接機轉證據支持其用於腎結石治療。</li>

<li><strong>急性尿酸腎病 (acute urate nephropathy)</strong>：TxGNN 分數最高 (0.9999)，但無任何文獻或臨床試驗支持，機轉連結薄弱。</li>
</ol>

<h3>臨床試驗</h3>

<p>目前無針對此特定適應症的臨床試驗登記。</p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. nephrolithiasis</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">100.00%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（1 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/6080021/" target="_blank">6080021</a></td><td>1967</td><td>Article</td><td>Journal of the Canadian Associ</td><td>Nephrotomography in various renal disorders.</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. bile duct disease</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.99%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/9149351/" target="_blank">9149351</a></td><td>1997</td><td>Article</td><td>The Tohoku journal of experime</td><td>A controlled trial of choleretic and hepatoprotective actions of Livzon and dehy...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/4947701/" target="_blank">4947701</a></td><td>1971</td><td>Article</td><td>Postgraduate medical journal</td><td>Primary sclerosing cholangitis.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/839737/" target="_blank">839737</a></td><td>1977</td><td>Article</td><td>Laboratory investigation; a jo</td><td>Subcellular pathology of rat liver in cholestasis and choleresis induced by bile...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/37191344/" target="_blank">37191344</a></td><td>2023</td><td>Article</td><td>Gut microbes</td><td>Bacterial and metabolic phenotypes associated with inadequate response to ursode...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/21010742/" target="_blank">21010742</a></td><td>1945</td><td>Article</td><td>The Journal of pharmacology an</td><td>The choleretic action of dehydrocholic acid (decholin) and deoxycholic acid (deg...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2919585/" target="_blank">2919585</a></td><td>1989</td><td>Article</td><td>The American journal of gastro</td><td>The biotransformed metabolite profiles in blood after intravenous administration...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/18613358/" target="_blank">18613358</a></td><td>2008</td><td>Article</td><td>Hepato-gastroenterology</td><td>Magnetic resonance cholangiopancreatography: potential usefulness of dehydrochol...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/21560523/" target="_blank">21560523</a></td><td>2010</td><td>Article</td><td>Tropical gastroenterology : of</td><td>Surgical outcome in relation to duct size at the porta hepatis and the use of ch...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/22194894/" target="_blank">22194894</a></td><td>2011</td><td>Article</td><td>PloS one</td><td>Ursodeoxycholic acid is conjugated with taurine to promote secretin-stimulated b...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/18989781/" target="_blank">18989781</a></td><td>2009</td><td>Article</td><td>Digestive diseases and science</td><td>Acidic and basic solutions dissolve protein plugs made of lithostathine complica...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/9314037/" target="_blank">9314037</a></td><td>1997</td><td>Article</td><td>European journal of pharmacolo</td><td>Effect of sodium tauroursodeoxycholate (UR-906) on liver dysfunction in bile duc...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/1502488/" target="_blank">1502488</a></td><td>1992</td><td>Article</td><td>Scandinavian journal of gastro</td><td>Influence of dehydrocholic and cholic acids on the biliary secretion of anionic ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2347547/" target="_blank">2347547</a></td><td>1990</td><td>Article</td><td>Hepatology (Baltimore, Md.)</td><td>Estradiol-17 beta-D-glucuronide (E-17G) cholestasis in perfused rat liver: fate ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/6229465/" target="_blank">6229465</a></td><td>1984</td><td>Article</td><td>Hepatology (Baltimore, Md.)</td><td>Cholestasis induced by estradiol-17 beta-D-glucuronide: mechanisms and preventio...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/3194431/" target="_blank">3194431</a></td><td>1988</td><td>Article</td><td>Proceedings of the Society for</td><td>Contribution of the fluid phase endocytosis to bile flow in cholestasis and chol...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/6742802/" target="_blank">6742802</a></td><td>1984</td><td>Article</td><td>Antibiotiki</td><td>[Effect of bile and bile acids on bacterial resistance to antibiotics].</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/13160724/" target="_blank">13160724</a></td><td>1953</td><td>Article</td><td>Bulletin. New York Medical Col</td><td>Decholin as adjunct in treatment of hepatobiliary disorders.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/863183/" target="_blank">863183</a></td><td>1977</td><td>Article</td><td>Gastroenterology</td><td>Taurolithocholate-induced cholestasis: taurocholate but not dehydrocholate, reve...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/969779/" target="_blank">969779</a></td><td>1976</td><td>Article</td><td>Zeitschrift fur Gastroenterolo</td><td>[Effect of some choleretics on the hepatic flow and its composition in man].</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/8155864/" target="_blank">8155864</a></td><td>1994</td><td>Article</td><td>Journal of gastroenterology an</td><td>Reversibility of organic anion-induced cholestasis: association with compensator...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. bile duct neoplasm</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.98%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（1 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2919585/" target="_blank">2919585</a></td><td>1989</td><td>Article</td><td>The American journal of gastro</td><td>The biotransformed metabolite profiles in blood after intravenous administration...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. apical periodontitis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.98%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. suppurative periapical periodontitis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.98%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. periapical granuloma</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.98%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. disorder of phenylalanine metabolism</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.96%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. urolithiasis</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.96%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（1 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/6080021/" target="_blank">6080021</a></td><td>1967</td><td>Article</td><td>Journal of the Canadian Associ</td><td>Nephrotomography in various renal disorders.</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. disorder of tyrosine metabolism</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.94%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>


## 泰國上市狀態

| 許可證號 | 商品名 | 劑型 | 狀態 |
|----------|--------|------|------|
| 衛署藥製字第014319號 | 派頓去氫膽酸錠 | 錠劑 | **有效** (至2028/05/25) |
| 內衛藥製字第004206號 | 得利膽錠 | 錠劑 | 已註銷 |
| 其他多項 | - | 粉劑/注射劑 | 已註銷 |

**現況**：泰國目前僅剩派頓去氫膽酸錠一項有效許可證。

## 安全性

### 藥物交互作用

| 併用藥物 | 嚴重程度 | 來源 |
|----------|----------|------|
| Cyclosporine | Minor | DDInter |

### 警語與禁忌

- 仿單詳細資訊未提供完整警語資料
- 一般禁忌：完全膽道阻塞時禁用

## 結論

### 整體評估：低優先級

Dehydrocholic acid 的 TxGNN 預測新適應症主要集中在膽道相關疾病，與其原有適應症高度重疊，不具真正的老藥新用價值。對於腎臟相關預測（如急性尿酸腎病、腎結石），缺乏機轉支持和臨床證據。

### 建議

1. **不建議**進一步投入資源研究此藥物的新適應症
2. 維持其作為傳統利膽劑的角色
3. 泰國目前僅剩一項有效許可證，市場重要性已大幅下降

### 證據等級總結

| 預測適應症 | TxGNN 分數 | 臨床試驗 | 文獻支持 | 機轉合理性 | 綜合評估 |
|------------|------------|----------|----------|------------|----------|
| 急性尿酸腎病 | 0.9999 | 無 | 無 | 低 | 不推薦 |
| 腎結石 | 0.9999 | 無 | 極弱 | 低 | 不推薦 |
| 膽道疾病 | 0.9999 | 無 | 有 | 高 | 已為適應症 |
| 膽管腫瘤 | 0.9998 | 無 | 極弱 | 低 | 不推薦 |

---
*報告產生日期：2026-02-11*
*資料來源：TxGNN 預測、ClinicalTrials.gov、PubMed、泰國 FDA*


---

## 相關藥物報告

- [Theophylline]({{ "/drugs/theophylline/" | relative_url }}) - 證據等級 L5
- [Scopolamine]({{ "/drugs/scopolamine/" | relative_url }}) - 證據等級 L5
- [Fenoprofen]({{ "/drugs/fenoprofen/" | relative_url }}) - 證據等級 L5
- [Sodium Citrate]({{ "/drugs/sodium_citrate/" | relative_url }}) - 證據等級 L5
- [Belimumab]({{ "/drugs/belimumab/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
ThTxGNN. (2026). Dehydrocholic Acid老藥新用驗證報告. https://thtxgnn.yao.care/drugs/dehydrocholic_acid/
```

**BibTeX 格式：**
```bibtex
@misc{thtxgnn_dehydrocholic_acid,
  title = {Dehydrocholic Acid老藥新用驗證報告},
  author = {ThTxGNN Team},
  year = {2026},
  url = {https://thtxgnn.yao.care/drugs/dehydrocholic_acid/}
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
