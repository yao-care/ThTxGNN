---
layout: default
title: Diosmin
description: "Diosmin 的老藥新用潛力分析。模型預測等級 L5，包含 1 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 57
evidence_level: L5
indication_count: 1
---

# Diosmin

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>1</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Diosmin (地奧司明) - 藥師評估報告

## 一句話總結

<p class="key-answer" data-question="Diosmin 可以用於治療什麼新適應症？">
Diosmin 是一種類黃酮靜脈活性劑，用於慢性靜脈功能不全和痔瘡；TxGNN 僅預測出一項新適應症（閉經），但分數較低且缺乏任何臨床或文獻支持，老藥新用潛力極為有限。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Diosmin (地奧司明/香葉木素芸香糖苷) |
| DrugBank ID | DB08995 |
| 泰國商品名 | 艾歐復隆膜衣錠、迪歐明膜衣錠、淨脈舒膜衣錠等 |
| 原適應症 | 慢性靜脈功能不全、靜脈曲張、痔瘡、機能性月經過多 |
| 預測新適應症 | amenorrhea (disease) |
| 最高 TxGNN 分數 | 0.9942 |
| 臨床試驗支持 | 無 |
| 文獻支持 | 無 |

## 為什麼預測合理

### 機轉分析

1. **閉經 (amenorrhea)**：
   - TxGNN 分數 0.9942，排名 10904（較低）
   - Diosmin 的原適應症包含「機能性月經過多症」，是一種影響月經的藥物
   - 理論上，具有血管保護和抗發炎作用的藥物可能影響子宮內膜血流
   - 但從「月經過多」到「閉經」的機轉連結極為薄弱
   - 閉經通常由荷爾蒙失調、下視丘-腦垂體-卵巢軸問題或解剖異常引起，與靜脈活性劑的作用無直接關聯

### 預測品質評估

- 僅有一項預測適應症，顯示 TxGNN 對此藥物的預測能力有限
- 預測分數相對較低（0.99 以下門檻邊緣）
- 無任何臨床試驗或文獻支持
- 機轉連結薄弱

## 臨床試驗

**無相關臨床試驗**

ClinicalTrials.gov 和 WHO ICTRP 均未發現 diosmin 用於閉經的臨床試驗。

## 文獻證據

**無相關文獻**

PubMed 搜尋未發現 diosmin 與閉經治療相關的文獻。

## 泰國上市狀態

| 許可證號 | 商品名 | 劑型 | 狀態 |
|----------|--------|------|------|
| 衛部藥輸字第026665號 | 艾歐復隆膜衣錠 500mg | 膜衣錠 | 有效 (至2031) |
| 衛部藥製字第061185號 | 迪歐明膜衣錠 500mg | 膜衣錠 | 有效 (至2027) |
| 衛部藥製字第061418號 | 淨脈舒膜衣錠 500mg | 膜衣錠 | 有效 (至2028) |
| 衛部藥製字第061424號 | 治昌優膜衣錠 500mg | 膜衣錠 | 有效 (至2028) |
| 衛部藥輸字第027992號 | 地奧司明 | 粉劑 | 有效 (至2030) |
| 衛部藥製字第060902號 | 法迪朗膜衣錠 500mg | 膜衣錠 | 有效 (至2026) |
| 衛部藥陸輸字第001025號 | 香葉木素芸香糖苷 | 粉劑 | 有效 (至2026) |
| 衛部藥陸輸字第001111號 | 香葉木苷 | 粉劑 | 有效 (至2028) |

**現況**：泰國有多項有效許可證，近年有多家廠商新取得許可，市場競爭活躍。

## 安全性

### 藥物交互作用

**無已知重大藥物交互作用**

DDInter 資料庫未記錄 diosmin 的顯著藥物交互作用。

### 一般安全性

Diosmin 的安全性良好：
- 常見副作用：輕微腸胃不適
- 罕見副作用：頭痛、皮疹
- 禁忌症：對此藥過敏者

## 結論

### 整體評估：極低優先級

Diosmin 的 TxGNN 預測極為有限，僅有一項新適應症（閉經），且完全缺乏機轉支持和臨床證據。此藥物應維持其作為靜脈活性劑的傳統角色，不建議投入資源研究新適應症。

### 建議

1. **不建議**進行任何老藥新用研究
2. 維持其作為慢性靜脈功能不全和痔瘡治療的角色
3. TxGNN 對此藥物的預測能力受限，可能是因為其在知識圖譜中的連結較少

### 證據等級總結

| 預測適應症 | TxGNN 分數 | 臨床試驗 | 文獻支持 | 機轉合理性 | 綜合評估 |
|------------|------------|----------|----------|------------|----------|
| 閉經 | 0.9942 | 無 | 無 | 極低 | 不推薦 |

---
*報告產生日期：2026-02-11*
*資料來源：TxGNN 預測、ClinicalTrials.gov、PubMed、泰國 FDA*


---

## 相關藥物報告

- [Chloral Hydrate]({{ "/drugs/chloral_hydrate/" | relative_url }}) - 證據等級 L5
- [Tinidazole]({{ "/drugs/tinidazole/" | relative_url }}) - 證據等級 L5
- [Methocarbamol]({{ "/drugs/methocarbamol/" | relative_url }}) - 證據等級 L5
- [Cyclizine]({{ "/drugs/cyclizine/" | relative_url }}) - 證據等級 L5
- [Caspofungin]({{ "/drugs/caspofungin/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
ThTxGNN. (2026). Diosmin老藥新用驗證報告. https://thtxgnn.yao.care/drugs/diosmin/
```

**BibTeX 格式：**
```bibtex
@misc{thtxgnn_diosmin,
  title = {Diosmin老藥新用驗證報告},
  author = {ThTxGNN Team},
  year = {2026},
  url = {https://thtxgnn.yao.care/drugs/diosmin/}
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
