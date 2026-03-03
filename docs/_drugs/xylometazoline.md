---
layout: default
title: Xylometazoline
description: "Xylometazoline 的老藥新用潛力分析。模型預測等級 L5，包含 2 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 200
evidence_level: L2
indication_count: 2
---

# Xylometazoline

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>2</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Xylometazoline：從過敏性鼻炎到鼻腔疾病的廣泛應用

## 一句話總結

<p class="key-answer" data-question="Xylometazoline 可以用於治療什麼新適應症？">
Xylometazoline 原本用於緩解鼻塞、過敏性鼻炎等症狀。
TxGNN 模型預測它可能對**鼻腔疾病 (nasal cavity disease)** 和**急性咽喉炎 (acute laryngopharyngitis)** 有效，
有 **2 個臨床試驗**和 **7 篇文獻**支持鼻腔疾病方向。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 感冒、鼻塞、過敏性鼻炎 |
| 預測新適應症 | nasal cavity disease、acute laryngopharyngitis |
| TxGNN 預測分數 | 99.91% (鼻腔疾病)、99.89% (急性咽喉炎) |
| 證據等級 | L3 (有文獻支持) |
| 泰國上市 | 已上市 |
| 許可證數 | 24 張 (多張有效) |
| 建議決策 | Proceed with Guardrails |






## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. nasal cavity disease</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.91%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>Xylometazoline 是一種 alpha 腎上腺素受體激動劑，作用於鼻黏膜血管，</p>
<p>使血管收縮而達到減少鼻腔充血的效果。其作用標靶包括：</p>

<ul>
<li><strong>alpha-1D 腎上腺素受體</strong> (ADRA1D)</li>
<li><strong>alpha-2A 腎上腺素受體</strong> (ADRA2A)</li>
<li><strong>alpha-2B 腎上腺素受體</strong> (ADRA2B)</li>
<li><strong>alpha-2C 腎上腺素受體</strong> (ADRA2C)</li>

</ul>
<p>由於其本身就是作用於鼻腔的血管收縮劑，預測其對鼻腔疾病有效在機轉上完全合理。</p>
<p>這個預測更像是確認現有適應症的延伸，而非真正的「老藥新用」。</p>

<h3>臨床試驗</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05072392" target="_blank">NCT05072392</a></td><td>NA</td><td>UNKNOWN</td><td>80</td><td>Determining the Effects of Foley Catheter-assisted Nasal Intubation on Nasal Ble...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06443255" target="_blank">NCT06443255</a></td><td>PHASE3</td><td>COMPLETED</td><td>16</td><td>Comparison of Cocaine, Lidocaine/xylometazoline and Saline for Intranasal Analge...</td></tr>
</tbody>
</table>

<h3>相關文獻</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/24023995/" target="_blank">24023995</a></td><td>2013</td><td>Article</td><td>Korean journal of anesthesiolo</td><td>The effect of xylometazoline spray for expansion of nasal cavity.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/8740084/" target="_blank">8740084</a></td><td>1996</td><td>Article</td><td>Arzneimittel-Forschung</td><td>Efficacy of topical tuaminoheptane combined with N-acetyl-cysteine in reducing n...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/34783482/" target="_blank">34783482</a></td><td>2021</td><td>Article</td><td>Vestnik otorinolaringologii</td><td>[The nasal mucosa in the elderly: features, modern approaches to the treatment o...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/22427029/" target="_blank">22427029</a></td><td>2013</td><td>Article</td><td>European archives of oto-rhino</td><td>Preparation of nose for nasal endoscopy: cotton pledget packing versus topical s...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/1281924/" target="_blank">1281924</a></td><td>1992</td><td>Article</td><td>Rhinology</td><td>Nasal airflow asymmetry and the effects of a topical nasal decongestant.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/24158493/" target="_blank">24158493</a></td><td>2013</td><td>Article</td><td>JAMA otolaryngology-- head &amp; n</td><td>Intranasal topical local anesthetic and decongestant for flexible nasendoscopy i...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/20632242/" target="_blank">20632242</a></td><td>2010</td><td>Article</td><td>Pneumologie (Stuttgart, German</td><td>[Geometry and function of the dog nose: how does function change when form of th...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. acute laryngopharyngitis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.89%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>


## 泰國上市資訊

| 許可證號 | 品名 | 劑型 | 許可證持有者 | 狀態 |
|---------|------|------|-------------|------|
| 衛部藥製字第061432號 | 大豐克敏通噴鼻液 0.1% | 鼻用噴液劑 | 大豐製藥 | 有效 |
| 衛部藥製字第059249號 | 強生欣鼻通噴鼻液 0.1% | 鼻用噴液劑 | 強生化學製藥 | 有效 |
| 衛署藥製字第043631號 | 斯斯鼻通噴鼻液 0.1% | 鼻用噴液劑 | 五洲製藥 | 有效 |
| 衛署藥輸字第024654號 | 歐治鼻噴鼻液 0.1% | 鼻用噴液劑 | 英商赫力昂 | 有效 |
| 衛署藥製字第047345號 | 大正百保能噴鼻液 0.1% | 鼻用噴液劑 | 泰國大正製藥 | 有效 |

## 安全性考量

- **藥物交互作用**：作用於 alpha-腎上腺素受體，與其他交感神經藥物併用需謹慎。
- **使用限制**：連續使用不宜超過 7 天，以避免藥物性鼻炎 (rhinitis medicamentosa)。
- **禁忌**：閉角型青光眼、嚴重高血壓患者應謹慎使用。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Xylometazoline 在鼻腔疾病中的應用與其原適應症高度相關，機轉明確且有充足的臨床證據支持。
預測的「鼻腔疾病」實際上是原適應症的泛化表述，臨床上已廣泛應用。

**若要推進需要：**
- 對於急性咽喉炎適應症，需要額外的臨床證據
- 針對特定鼻腔疾病亞型的療效評估
- 長期使用安全性監測


---

## 相關藥物報告

- [Pemetrexed]({{ "/drugs/pemetrexed/" | relative_url }}) - 證據等級 L5
- [Emedastine]({{ "/drugs/emedastine/" | relative_url }}) - 證據等級 L5
- [Magnesium Sulfate]({{ "/drugs/magnesium_sulfate/" | relative_url }}) - 證據等級 L5
- [Potassium Iodide]({{ "/drugs/potassium_iodide/" | relative_url }}) - 證據等級 L5
- [Methocarbamol]({{ "/drugs/methocarbamol/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
ThTxGNN. (2026). Xylometazoline老藥新用驗證報告. https://thtxgnn.yao.care/drugs/xylometazoline/
```

**BibTeX 格式：**
```bibtex
@misc{thtxgnn_xylometazoline,
  title = {Xylometazoline老藥新用驗證報告},
  author = {ThTxGNN Team},
  year = {2026},
  url = {https://thtxgnn.yao.care/drugs/xylometazoline/}
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
