---
layout: default
title: Aspirin
description: "Aspirin 的老藥新用潛力分析。模型預測等級 L5。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 0
---

# Aspirin

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>0</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Aspirin：從鎮痛解熱到新適應症探索

## 一句話總結

<p class="key-answer" data-question="Aspirin 可以用於治療什麼新適應症？">
Aspirin 主要用於解熱鎮痛及預防心血管疾病。
目前尚無新的適應症預測，但其廣泛的藥理作用提示可能有其他潛在用途。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 解熱鎮痛劑 |
| 預測新適應症 | 無 |
| TxGNN 預測分數 | 無 |
| 證據等級 | L5 |
| 泰國上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

<p class="key-answer" data-question="這個藥物的作用機轉是什麼？">
目前缺乏詳細的作用機轉資料。根據已知資訊，Aspirin 是一種常用的解熱鎮痛藥，
其成分在緩解疼痛和發炎反應中的療效已被證實，並且在心血管疾病的預防中也有應用。
儘管缺乏新適應症的預測，Aspirin 的廣泛作用機轉提示可能有其他潛在用途。
</p>

<div class="key-takeaway">
此預測基於藥物的作用機轉，與現有臨床證據方向一致。
</div>


## 泰國上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 內衛藥輸字第001097號 | 醋酸基柳酸鹽 | （粉） | 解熱鎮痛劑 |
| 內衛藥輸字第002145號 | 乙醯基水楊酸 | （粉） | 鎮痛解熱 |
| 內衛藥輸字第004402號 | 乙醯水楊酸 | （粉） | 鎮痛、退熱 |
| 內衛藥輸字第005984號 | 彼施必寧 | 錠劑 | 肌肉痙攣及其疼痛、神經痛 |
| 內衛藥製字第004155號 | 乙醯水楊酸片０．３２４公分 | 錠劑 | 解熱鎮痛 |

## 安全性考量

- **藥物交互作用**：
  - 與 ASIC3 的交互作用
  - 與 COX-1 的交互作用
  - 與 COX-2 的交互作用

安全性資訊請參考原廠仿單。

### 藥物-草藥交互作用 (DHI)

**銀杏** 🟡 Moderate
- 影響：銀杏增加出血風險
- 建議：避免併用或監測出血

**大蒜** 🟡 Moderate
- 影響：大蒜增加抗血小板作用
- 建議：避免高劑量大蒜補充品


## 結論與下一步

**決策：Hold**

**理由：**
目前缺乏新的適應症預測和詳細的作用機轉資料，需進一步研究以確認新的適應症可能性。

**若要推進需要：**
- 詳細的藥物作用機轉資料（MOA）
- 針對特定適應症的臨床試驗設計
- 更廣泛的藥物交互作用研究


---

## 相關藥物報告

- [Polysorbate 80]({{ "/drugs/polysorbate_80/" | relative_url }}) - 證據等級 L5
- [Trihexyphenidyl]({{ "/drugs/trihexyphenidyl/" | relative_url }}) - 證據等級 L5
- [Timepidium]({{ "/drugs/timepidium/" | relative_url }}) - 證據等級 L5
- [Tolmetin]({{ "/drugs/tolmetin/" | relative_url }}) - 證據等級 L5
- [Pemetrexed]({{ "/drugs/pemetrexed/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
ThTxGNN. (2026). Aspirin老藥新用驗證報告. https://thtxgnn.yao.care/drugs/aspirin/
```

**BibTeX 格式：**
```bibtex
@misc{thtxgnn_aspirin,
  title = {Aspirin老藥新用驗證報告},
  author = {ThTxGNN Team},
  year = {2026},
  url = {https://thtxgnn.yao.care/drugs/aspirin/}
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
