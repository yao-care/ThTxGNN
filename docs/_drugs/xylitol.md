---
layout: default
title: Xylitol
description: "Xylitol 的老藥新用潛力分析。模型預測等級 L5，包含 1 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 1
---

# Xylitol

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>1</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Xylitol：從糖尿病代謝異常到腦膜炎球菌感染

## 一句話總結

<p class="key-answer" data-question="Xylitol 可以用於治療什麼新適應症？">
Xylitol 原本用於糖尿病患者的醣類補充與代謝異常改善。
TxGNN 模型預測它可能對**腦膜炎球菌感染 (meningococcal infection)** 有效，
但目前缺乏臨床試驗和文獻支持這個方向。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 糖尿病代謝異常、醣類補充 |
| 預測新適應症 | meningococcal infection |
| TxGNN 預測分數 | 99.66% |
| 證據等級 | 無臨床證據 |
| 泰國上市 | 僅 1 張有效許可證 |
| 許可證數 | 117 張 (大部分已註銷) |
| 建議決策 | Wait for More Evidence |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Xylitol 是一種五碳糖醇，主要作為糖尿病患者的醣類補充劑使用，
其代謝途徑不依賴胰島素。知識圖譜中將其與腦膜炎球菌感染關聯的原因尚不明確，
可能需要進一步研究其潛在的抗菌或免疫調節特性。

值得注意的是，有研究顯示 xylitol 在口腔和鼻腔中具有抗菌作用，可能抑制細菌生物膜形成。
但這與腦膜炎球菌感染的直接關聯仍待釐清。

## 臨床試驗證據

目前未發現任何 Xylitol 用於腦膜炎球菌感染的臨床試驗。

## 文獻證據

目前未發現任何 Xylitol 用於腦膜炎球菌感染的相關文獻。

## 泰國上市資訊

| 許可證號 | 品名 | 劑型 | 許可證持有者 | 狀態 |
|---------|------|------|-------------|------|
| 衛署藥製字第009683號 | 可樂醣注射液 5% | 注射劑 | 杏林新生製藥股份有限公司 | 有效 |

> 注意：歷史上共有 117 張許可證，但大部分已註銷。僅剩 1 張仍有效。

## 安全性考量

- **藥物交互作用**：目前資料庫中未發現已知的藥物交互作用記錄。
- **警語與禁忌**：未檢索到詳細仿單資訊。

## 結論與下一步

**決策：Wait for More Evidence**

**理由：**
Xylitol 與腦膜炎球菌感染之間的關聯缺乏任何臨床試驗或文獻支持。
預測分數雖高 (99.66%)，但排名較低 (7287)，且缺乏機轉上的合理解釋。

**若要推進需要：**
- 基礎研究確認 Xylitol 的抗菌或免疫調節機轉
- 體外或動物模型研究驗證對腦膜炎球菌的抑制效果
- 進一步了解知識圖譜中此預測的推論路徑


---

## 相關藥物報告

- [Travoprost]({{ "/drugs/travoprost/" | relative_url }}) - 證據等級 L5
- [Insulin Lispro]({{ "/drugs/insulin_lispro/" | relative_url }}) - 證據等級 L5
- [Loteprednol Etabonate]({{ "/drugs/loteprednol_etabonate/" | relative_url }}) - 證據等級 L5
- [Irbesartan]({{ "/drugs/irbesartan/" | relative_url }}) - 證據等級 L5
- [Scopolamine]({{ "/drugs/scopolamine/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
ThTxGNN. (2026). Xylitol老藥新用驗證報告. https://thtxgnn.yao.care/drugs/xylitol/
```

**BibTeX 格式：**
```bibtex
@misc{thtxgnn_xylitol,
  title = {Xylitol老藥新用驗證報告},
  author = {ThTxGNN Team},
  year = {2026},
  url = {https://thtxgnn.yao.care/drugs/xylitol/}
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
