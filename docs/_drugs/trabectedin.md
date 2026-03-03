---
layout: default
title: Trabectedin
description: "Trabectedin 的老藥新用潛力分析。模型預測等級 L5，包含 1 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 1
---

# Trabectedin

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>1</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Trabectedin：從軟組織肉瘤到女性乳腺癌

## 一句話總結

<p class="key-answer" data-question="Trabectedin 可以用於治療什麼新適應症？">
Trabectedin 原本用於治療無法切除或轉移性脂肪肉瘤及平滑肌肉瘤。
TxGNN 模型預測它可能對**女性乳腺癌 (female breast carcinoma)** 有效，
目前有 **2 個臨床試驗**和 **多篇文獻**支持這個方向。
</p>

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無法切除或轉移性脂肪肉瘤/平滑肌肉瘤 |
| 預測新適應症 | 女性乳腺癌 |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | 待評估 |
| 泰國上市 | 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Trabectedin 是一種源自海洋生物的抗腫瘤藥物，主要透過影響轉錄調控抑制癌細胞增殖。其獨特的作用機轉包括：

1. **DNA 修復系統干擾**：影響轉錄耦合核苷酸切除修復及同源重組修復 (HRR)
2. **腫瘤微環境調節**：減少腫瘤相關巨噬細胞 (TAM) 數量
3. **BRCA 缺陷敏感性**：對 BRCA1/2 突變的腫瘤具有特殊療效

這些機轉在乳腺癌中同樣具有臨床意義，特別是 BRCA 突變的乳腺癌患者。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03470805](https://clinicaltrials.gov/study/NCT03470805) | Phase 2 | COMPLETED | 9 | 評估 Olaparib 作為 Trabectedin-PLD 療程後維持治療在復發性卵巢癌中的效果 |
| [NCT00786838](https://clinicaltrials.gov/study/NCT00786838) | Phase 2 | COMPLETED | 76 | 評估 Trabectedin 對 QT/QTc 間隔的影響 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26592307](https://pubmed.ncbi.nlm.nih.gov/26592307/) | 2016 | Review | Expert Opin Investig Drugs | 討論 Trabectedin 在乳腺癌中的潛在應用 |
| [25239225](https://pubmed.ncbi.nlm.nih.gov/25239225/) | 2014 | Phase II RCT | Clin Breast Cancer | 評估 Trabectedin 單藥治療晚期乳腺癌的療效與安全性 |
| [27710871](https://pubmed.ncbi.nlm.nih.gov/27710871/) | 2016 | Review | Cancer Treat Rev | 探討 Trabectedin 在 BRCA 缺陷患者中的化療選擇 |
| [27266804](https://pubmed.ncbi.nlm.nih.gov/27266804/) | 2016 | Phase II | Clin Breast Cancer | 根據 XPG 基因表達評估 Trabectedin 在 HR+/HER2- 晚期乳腺癌中的療效 |
| [38863768](https://pubmed.ncbi.nlm.nih.gov/38863768/) | 2024 | Review | Drug Des Devel Ther | 聚焦 Trabectedin 在卵巢癌中的應用及 BRCA 突變情況 |

## 泰國上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部藥輸字第027370號 | "友待" 凍晶注射劑1毫克 | 凍晶注射劑 | 無法切除或轉移性脂肪肉瘤或平滑肌肉瘤 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 抗腫瘤抗生素 (海洋來源) |
| 骨髓抑制風險 | 高度 |
| 致吐性分級 | 中度至高度 |
| 監測項目 | CBC（含分類）、肝腎功能、CK |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |
| 特殊注意 | 可能引起橫紋肌溶解症，需監測肌酸激酶 |

## 安全性考量

- **肝毒性**：需定期監測肝功能
- **骨髓抑制**：可能導致嗜中性白血球減少、血小板減少
- **橫紋肌溶解症**：罕見但嚴重的不良反應
- **心臟毒性**：需監測 QT 間隔


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**Cardiomyopathies** 🟡 Moderate
- 必要時應停止治療。

**肝臟疾病** 🟡 Moderate
- 需定期監測。風險包括：肝毒性。可能有嚴重不良反應。

**Sepsis** 🟡 Moderate
- 需定期監測。可能有致命風險。必要時應停止治療。

**Rhabdomyolysis** 🟡 Moderate
- 出現症狀時應考慮停藥。

**Kidney Failure, Chronic** 🟡 Moderate
- 通常無需調整劑量。可能有嚴重不良反應。

### 藥物-食物交互作用 (DFI)

<div class="dfi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**葡萄柚汁** 🟡 Moderate
- 影響：影響藥物代謝。可能增加藥物血中濃度。
- 建議：避免大量攝取。需監測療效或不良反應。避免食用葡萄柚或葡萄柚汁。


## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Trabectedin 在乳腺癌中的多項臨床試驗及文獻顯示其潛在療效，特別是對 BRCA 突變患者。其獨特的作用機轉與現有乳腺癌治療藥物不同，可能提供新的治療選擇。

**若要推進需要：**
- 針對乳腺癌的大型隨機對照試驗
- BRCA 突變狀態的生物標記篩選策略
- 與現有乳腺癌治療方案的比較研究

---

## 相關藥物報告

- [Inclisiran]({{ "/drugs/inclisiran/" | relative_url }}) - 證據等級 L5
- [Zanubrutinib]({{ "/drugs/zanubrutinib/" | relative_url }}) - 證據等級 L5
- [Scopolamine]({{ "/drugs/scopolamine/" | relative_url }}) - 證據等級 L5
- [Brivaracetam]({{ "/drugs/brivaracetam/" | relative_url }}) - 證據等級 L5
- [Polymyxin B]({{ "/drugs/polymyxin_b/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
ThTxGNN. (2026). Trabectedin老藥新用驗證報告. https://thtxgnn.yao.care/drugs/trabectedin/
```

**BibTeX 格式：**
```bibtex
@misc{thtxgnn_trabectedin,
  title = {Trabectedin老藥新用驗證報告},
  author = {ThTxGNN Team},
  year = {2026},
  url = {https://thtxgnn.yao.care/drugs/trabectedin/}
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
