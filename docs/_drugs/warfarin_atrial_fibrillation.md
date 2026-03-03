---
layout: default
title: Warfarin Atrial Fibrillation
description: "Warfarin Atrial Fibrillation 的老藥新用潛力分析。模型預測等級 L5。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 0
---

# Warfarin Atrial Fibrillation

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>0</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Warfarin - Atrial Fibrillation（心房顫動）適應症評估

## 一句話總結

<p class="key-answer" data-question="Warfarin Atrial Fibrillation 可以用於治療什麼新適應症？">
Warfarin 用於心房顫動（Atrial Fibrillation）的血栓預防**已是核准適應症**，
此為長期確立的標準治療，非新適應症預測。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥品名稱 | Warfarin |
| DrugBank ID | DB00682 |
| 適應症 | 心房纖維顫動（Atrial Fibrillation）血栓預防 |
| 適應症狀態 | **已核准** |
| 證據等級 | L1（多個 RCT 支持） |
| 泰國上市 | 已上市 |
| 建議決策 | 標準治療（非老藥新用候選） |

## 背景說明

本筆記針對 Warfarin 在心房顫動的應用進行說明。

**重要聲明：**
此適應症並非 TxGNN 預測的「老藥新用」候選，而是已確立數十年的標準治療。Warfarin 自 1950 年代以來即被用於抗凝血治療，並在心房顫動的中風預防中扮演核心角色。

## 泰國核准適應症（TFDA）

根據多張現行許可證（欣服寧錠 1mg/5mg、可化凝錠等）：

```
1. 預防及/或治療靜脈栓塞症及其相關疾病，以及肺栓塞
2. 預防或治療因心房纖維顫動及/或更換心臟瓣膜引起之血栓性栓塞症
```

## 臨床證據

### 關鍵臨床試驗

Warfarin 在心房顫動的療效已被多個大型 RCT 證實：

1. **SPAF 系列研究（1990s）**
   - Stroke Prevention in Atrial Fibrillation
   - 確立 Warfarin 可降低 AF 患者中風風險約 60-70%

2. **AFASAK 研究**
   - Copenhagen Atrial Fibrillation, Aspirin, Anticoagulation Study
   - 比較 Warfarin vs Aspirin vs 安慰劑

3. **後續與 DOAC 比較研究**
   - RE-LY（Dabigatran vs Warfarin）
   - ROCKET AF（Rivaroxaban vs Warfarin）
   - ARISTOTLE（Apixaban vs Warfarin）
   - ENGAGE AF-TIMI 48（Edoxaban vs Warfarin）

### 證據等級：L1

具有多個大型隨機對照試驗支持，證據等級最高。

## 臨床實務重點

### 適應症選擇

**優先考慮 Warfarin 的情況：**
- 機械性心臟瓣膜置換後
- 中度至重度風濕性二尖瓣狹窄
- 嚴重腎功能不全（CrCl < 15-30 mL/min）
- 抗磷脂質症候群
- DOAC 禁忌或不耐受

**可考慮 DOAC 優先的情況：**
- 非瓣膜性心房顫動
- 無法定期監測 INR
- 藥物交互作用顧慮較高

### INR 監測目標

| 適應症 | 目標 INR |
|--------|---------|
| 非瓣膜性心房顫動 | 2.0-3.0 |
| 機械性二尖瓣 | 2.5-3.5 |
| 機械性主動脈瓣（無其他風險因子） | 2.0-3.0 |

### 起始與維持劑量

- **起始劑量**：通常 2-5 mg/天，依患者特性調整
- **維持劑量**：個體差異大，需根據 INR 調整
- **藥物基因檢測**：CYP2C9、VKORC1 基因多型性可協助預測劑量需求

## 安全性考量

### 主要風險

1. **出血**：最重要的不良反應
   - 輕微出血（牙齦、瘀青）
   - 重大出血（腸胃道、顱內）

2. **藥物交互作用**
   - 增強效果：Aspirin、NSAID、部分抗生素、Amiodarone 等
   - 減弱效果：Rifampin、Carbamazepine、高維生素K食物

3. **皮膚壞死**（罕見但嚴重）
   - 通常發生在治療初期
   - 與 Protein C/S 缺乏有關

### 出血風險評估

使用 HAS-BLED 評分評估出血風險：
- Hypertension
- Abnormal renal/liver function
- Stroke history
- Bleeding history
- Labile INR
- Elderly (>65)
- Drugs/alcohol

## 泰國上市製劑

| 許可證號 | 品名 | 劑量 | 狀態 |
|---------|------|------|------|
| 衛署藥製字第050068號 | 欣服寧錠 | 1 mg | 有效 |
| 衛署藥製字第052458號 | 欣服寧錠 | 5 mg | 有效 |
| 衛署藥製字第055271號 | 政德可化凝錠 | 5 mg | 有效 |
| 衛部藥輸字第026478號 | 苯甲香豆醇鈉籠晶 | 原料藥 | 有效 |

## 與 TxGNN 預測的關聯

本專案（ThTxGNN）使用 TxGNN 模型預測 Warfarin 的潛在新適應症。

**預測結果顯示：**
- Heparin Cofactor 2 Deficiency（99.87%）
- Factor 5 Excess with Spontaneous Thrombosis（99.84%）
- Antithrombin Deficiency Type 2（99.84%）

上述為真正的「老藥新用」候選適應症，詳見 [Warfarin 主要藥師筆記](../warfarin/drug_pharmacist_notes.md)。

心房顫動作為已核准適應症，不在預測範圍內。

## 結論

**此筆記為參考性質說明**

Warfarin 用於心房顫動是已確立的標準治療，具有 L1 等級證據支持。
醫療人員應依據現行治療指引及個別患者特性選擇抗凝血治療。

**相關資源：**
- [Warfarin 完整藥師筆記（含新適應症預測）](../warfarin/drug_pharmacist_notes.md)
- [Warfarin - AF 簡要說明](../warfarin_af/drug_pharmacist_notes.md)
- 泰國心臟學會心房顫動治療指引


---

## 相關藥物報告

- [Gefitinib]({{ "/drugs/gefitinib/" | relative_url }}) - 證據等級 L5
- [Emedastine]({{ "/drugs/emedastine/" | relative_url }}) - 證據等級 L5
- [Titanium Dioxide]({{ "/drugs/titanium_dioxide/" | relative_url }}) - 證據等級 L5
- [Fenoprofen]({{ "/drugs/fenoprofen/" | relative_url }}) - 證據等級 L5
- [Methocarbamol]({{ "/drugs/methocarbamol/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
ThTxGNN. (2026). Warfarin Atrial Fibrillation老藥新用驗證報告. https://thtxgnn.yao.care/drugs/warfarin_atrial_fibrillation/
```

**BibTeX 格式：**
```bibtex
@misc{thtxgnn_warfarin_atrial_fibrillation,
  title = {Warfarin Atrial Fibrillation老藥新用驗證報告},
  author = {ThTxGNN Team},
  year = {2026},
  url = {https://thtxgnn.yao.care/drugs/warfarin_atrial_fibrillation/}
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
