---
layout: default
title: Griseofulvin
description: "Griseofulvin 的老藥新用潛力分析。模型預測等級 L5，包含 5 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L4
indication_count: 5
---

# Griseofulvin

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>5</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Griseofulvin (灰黴素) - 藥師評估報告

## 一句話總結

<p class="key-answer" data-question="Griseofulvin 可以用於治療什麼新適應症？">
灰黴素是一種傳統口服抗黴菌藥物，TxGNN 預測其對蠅蛆症（myiasis）和包蟲病有潛在療效，這些預測基於知識圖譜中寄生蟲感染的連結，但臨床證據極為有限。
</p>

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物學名 | Griseofulvin |
| 泰國商品名 | 克黴敏片、派頓癬黴淨膠囊、克膚癬錠、格利癬錠等 |
| DrugBank ID | DB00400 |
| 原核准適應症 | 甲癬、髮癬、皮膚黴菌感染（香港腳、灰指甲、頑癬） |
| 預測新適應症 | tinea corporis、tinea pedis、myiasis、furuncular myiasis、wound myiasis |
| 最高證據等級 | L5 (僅預測) |
| 泰國上市狀態 | 多項有效許可證 |





## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. myiasis</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.41%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>灰黴素透過抑制真菌有絲分裂發揮抗黴菌作用。其預測適應症涉及非真菌性寄生蟲感染：</p>

<ol>
<li><strong>蠅蛆症 (Myiasis)</strong> (TxGNN Score: 0.994, Rank: 11014)：</li>
</ol>
<ul>
<li>蠅蛆症是雙翅目幼蟲寄生於活體組織的感染</li>
<li>灰黴素對此類感染的作用機轉不明</li>
<li>知識圖譜可能因「皮膚寄生蟲感染」的廣義關聯而產生此預測</li>

</ul>
<ol>
<li><strong>包蟲病 (Echinococcosis)</strong> (TxGNN Score: 0.993, Rank: 12340)：</li>
</ol>
<ul>
<li>由棘球絛蟲引起的寄生蟲感染</li>
<li>與灰黴素的抗真菌機轉無明顯關聯</li>
<li>標準治療為 albendazole 或手術</li>

</ul>
<p><strong>預測機轉分析：</strong> 這些預測可能源於知識圖譜中「皮膚/軟組織感染」的非特異性連結，而非藥理學上的合理推論。</p>

<h3>臨床試驗</h3>

<p>目前無針對此特定適應症的臨床試驗登記。</p>

<h3>相關文獻</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/4098614/" target="_blank">4098614</a></td><td>1970</td><td>Article</td><td>The Veterinary record</td><td>Parasitic skin diseases of dogs and cats.</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. furuncular myiasis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.34%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. wound myiasis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.34%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. creeping myiasis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.34%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. echinococcus granulosus infectious disease</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.32%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>


## 泰國上市資訊

**有效許可證：**

| 許可證字號 | 商品名 | 許可證持有者 | 效期 |
|------------|--------|--------------|------|
| 內衛藥製字第003414號 | 克黴敏片 | 中國化學新豐工廠 | 2028/05/09 |
| 衛署藥製字第010941號 | 派頓癬黴淨膠囊 | 臺灣派頓化學 | 2028/05/25 |
| 衛署藥製字第027776號 | 榮民克癬錠 500mg | 榮民製藥 | 2028/08/15 |
| 衛署藥製字第027109號 | 克膚癬錠 500mg | 中美兄弟製藥 | 2029/05/25 |
| 衛署藥製字第019146號 | 格利癬錠 | 政德製藥 | 2029/10/19 |
| 衛署藥製字第025159號 | 克黴星錠 500mg | 嘉林藥品 | 2029/02/14 |

**總計：** 76 筆相關許可證紀錄，多為有效許可證。

**核准適應症：**
- 甲癬 (Onychomycosis)
- 髮癬 (Tinea capitis)
- 不適宜局部外用治療或局部外用無效的皮膚黴菌感染
- 香港腳、灰指甲、頑癬等皮癬菌引起之皮膚病

## 安全性考量

### 主要藥物交互作用

| 交互作用藥物 | 嚴重程度 | 說明 |
|--------------|----------|------|
| Ethinylestradiol | **Major** | 可能降低口服避孕藥效果 |
| Warfarin | Moderate | 可能降低抗凝血效果 |
| Cyclosporine | Moderate | 可能降低 cyclosporine 濃度 |
| Barbiturates | Moderate | 可能影響 griseofulvin 代謝 |
| Alcohol | Moderate | 可能產生類 disulfiram 反應 |

**共記錄多項與 CYP450 酶相關的藥物交互作用。**

### 常見不良反應
- 頭痛（最常見）
- 腸胃不適（噁心、嘔吐、腹瀉）
- 皮疹
- 光敏感性
- 口腔念珠菌感染

### 禁忌症
- 肝功能不全
- 紫質症
- 全身性紅斑性狼瘡
- 懷孕（致畸性）

### 特殊族群
- **孕婦**：禁用，有動物致畸性證據
- **哺乳**：不建議使用
- **兒童**：可用於髮癬治療
- **肝病患者**：禁忌使用


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**Lupus Erythematosus, Systemic** 🟡 Moderate
- 注意事項：The use of griseofulvin has been associated with the development of lupus erythematosus and lupus-like syndromes, as well as exacerbation of the disea...

**肝臟疾病** 🟢 Minor
- 本藥物在此情況下禁用。必要時應停止治療。

**Porphyrias** 🟢 Minor
- 本藥物在此情況下禁用。

### 藥物-食物交互作用 (DFI)

<div class="dfi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**酒精** 🟡 Moderate
- 影響：產生協同作用。可能增強藥效。
- 建議：請諮詢醫師或藥師了解詳細建議。


## 結論與下一步

### 預測評估結論

Griseofulvin 對蠅蛆症和包蟲病的預測**缺乏藥理學基礎和臨床證據**。這些預測很可能是知識圖譜中疾病連結的偽陽性結果：

1. **蠅蛆症**是由雙翅目幼蟲引起，治療通常為機械性移除幼蟲或使用殺蟲劑
2. **包蟲病**需要驅蟲藥物如 albendazole 或手術治療
3. Griseofulvin 的抗真菌機轉（抑制有絲分裂紡錘體形成）與抗寄生蟲作用無明顯關聯

### 證據等級總結

| 預測適應症 | TxGNN Score | 證據等級 | 評估 |
|------------|-------------|----------|------|
| 蠅蛆症 | 0.994 | L5 | 機轉不支持，無證據 |
| 疥蟲性蠅蛆症 | 0.993 | L5 | 機轉不支持，無證據 |
| 傷口蠅蛆症 | 0.993 | L5 | 機轉不支持，無證據 |
| 爬行性蠅蛆症 | 0.993 | L5 | 機轉不支持，無證據 |
| 包蟲病 | 0.993 | L5 | 機轉不支持，無證據 |

### 建議

1. **不建議進一步開發**：
   - 預測缺乏藥理學合理性
   - 無前臨床或臨床證據支持
   - 現有更有效的標準治療方案

2. **模型警示**：
   - 此案例展示了知識圖譜預測可能產生的偽陽性結果
   - 應結合藥理機轉和臨床證據評估預測

3. **現有適應症**：
   - Griseofulvin 在皮膚黴菌感染的治療仍有其價值
   - 特別是對於需要口服治療的髮癬和甲癬
   - 但在 terbinafine 和 itraconazole 等更新藥物出現後，使用頻率已減少

---

*報告生成日期：2026-02-11*
*資料來源：TxGNN 知識圖譜預測、ClinicalTrials.gov、PubMed、泰國 FDA*

---

## 相關藥物報告

- [Diosmin]({{ "/drugs/diosmin/" | relative_url }}) - 證據等級 L5
- [Raloxifene]({{ "/drugs/raloxifene/" | relative_url }}) - 證據等級 L5
- [Zanubrutinib]({{ "/drugs/zanubrutinib/" | relative_url }}) - 證據等級 L5
- [Trabectedin]({{ "/drugs/trabectedin/" | relative_url }}) - 證據等級 L5
- [Carbenoxolone]({{ "/drugs/carbenoxolone/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
ThTxGNN. (2026). Griseofulvin老藥新用驗證報告. https://thtxgnn.yao.care/drugs/griseofulvin/
```

**BibTeX 格式：**
```bibtex
@misc{thtxgnn_griseofulvin,
  title = {Griseofulvin老藥新用驗證報告},
  author = {ThTxGNN Team},
  year = {2026},
  url = {https://thtxgnn.yao.care/drugs/griseofulvin/}
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
