---
layout: default
title: Trastuzumab Deruxtecan
description: "Trastuzumab Deruxtecan 的老藥新用潛力分析。模型預測等級 L5，包含 1 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 1
---

# Trastuzumab Deruxtecan

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>1</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Trastuzumab Deruxtecan：從 HER2 陽性腫瘤到藥物誘發性骨質疏鬆

## 一句話總結

<p class="key-answer" data-question="Trastuzumab Deruxtecan 可以用於治療什麼新適應症？">
Trastuzumab deruxtecan (優赫得) 原本用於治療 HER2 陽性乳癌、非小細胞肺癌、胃癌等腫瘤。
TxGNN 模型預測它可能對**藥物誘發性骨質疏鬆 (drug-induced osteoporosis)** 有效，
目前**無臨床試驗或文獻**支持這個方向。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HER2 陽性乳癌、非小細胞肺癌、胃癌、實體腫瘤 |
| 預測新適應症 | 藥物誘發性骨質疏鬆 (drug-induced osteoporosis) |
| TxGNN 預測分數 | 99.31% |
| 證據等級 | 無證據 |
| 泰國上市 | 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Not Recommended |

## 為什麼這個預測可能不合理？

Trastuzumab deruxtecan 是一種抗體藥物複合體 (ADC)，由抗 HER2 單株抗體與拓樸異構酶 I 抑制劑藥物連接而成。其設計目的是：

1. **靶向 HER2**：透過抗體部分辨識 HER2 陽性腫瘤細胞
2. **細胞毒殺**：藥物載荷進入細胞後釋放，殺死腫瘤細胞
3. **旁觀者效應**：可影響鄰近 HER2 低表達細胞

藥物誘發性骨質疏鬆與 HER2 訊號傳導無明確關聯，且抗腫瘤藥物通常會加重而非改善骨質疏鬆。此預測可能是知識圖譜的假陽性結果。

## 臨床試驗證據

無相關臨床試驗。

## 文獻證據

無相關文獻。

## 泰國上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部菌疫輸字第001179號 | 優赫得凍晶注射劑100毫克 | 凍晶注射劑 | HER2 陽性/弱陽性轉移性乳癌、非小細胞肺癌、胃癌、其他 HER2 陽性實體腫瘤 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 抗體藥物複合體 (ADC) |
| 骨髓抑制風險 | 高度 |
| 致吐性分級 | 中度 |
| 監測項目 | CBC、肝腎功能、左心室射出分率、肺功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |
| 特殊警告 | 間質性肺病 (ILD) 風險，需密切監測呼吸症狀 |

## 安全性考量

- **間質性肺病 (ILD)**：最嚴重的不良反應，可能致命
- **心臟毒性**：可能降低左心室射出分率
- **骨髓抑制**：嗜中性白血球減少、貧血、血小板減少
- **主要交互作用 (Major)**：
  - Deferiprone（增加嗜中性白血球減少風險）
  - TNF-alpha 抑制劑（Adalimumab、Etanercept、Infliximab、Golimumab）
  - JAK 抑制劑（Baricitinib、Tofacitinib、Upadacitinib）
  - 其他免疫抑制劑

## 結論與下一步

**決策：Not Recommended**

**理由：**
此預測缺乏生物學合理性。Trastuzumab deruxtecan 是一種靶向 HER2 的細胞毒性抗體藥物複合體，其作用機轉與骨質疏鬆的病理生理學無關聯。抗腫瘤治療通常會導致骨質流失而非改善。

**不建議推進的原因：**
- 無任何臨床或基礎研究證據
- 作用機轉與適應症無生物學關聯
- 藥物本身可能加重骨質疏鬆
- 高度細胞毒性不適用於非腫瘤適應症


---

## 相關藥物報告

- [Disopyramide]({{ "/drugs/disopyramide/" | relative_url }}) - 證據等級 L5
- [Verteporfin]({{ "/drugs/verteporfin/" | relative_url }}) - 證據等級 L5
- [Irbesartan]({{ "/drugs/irbesartan/" | relative_url }}) - 證據等級 L5
- [Cephalexin]({{ "/drugs/cephalexin/" | relative_url }}) - 證據等級 L5
- [Benazepril]({{ "/drugs/benazepril/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
ThTxGNN. (2026). Trastuzumab Deruxtecan老藥新用驗證報告. https://thtxgnn.yao.care/drugs/trastuzumab_deruxtecan/
```

**BibTeX 格式：**
```bibtex
@misc{thtxgnn_trastuzumab_deruxtecan,
  title = {Trastuzumab Deruxtecan老藥新用驗證報告},
  author = {ThTxGNN Team},
  year = {2026},
  url = {https://thtxgnn.yao.care/drugs/trastuzumab_deruxtecan/}
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
