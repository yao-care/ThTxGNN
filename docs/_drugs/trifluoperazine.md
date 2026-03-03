---
layout: default
title: Trifluoperazine
description: "Trifluoperazine 的老藥新用潛力分析。模型預測等級 L5，包含 1 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 185
evidence_level: L5
indication_count: 1
---

# Trifluoperazine

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>1</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Trifluoperazine：從精神病狀態到躁鬱症躁症期

## 一句話總結

<p class="key-answer" data-question="Trifluoperazine 可以用於治療什麼新適應症？">
Trifluoperazine (三氟陪拉辛) 原本用於治療精神病狀態及行為障礙。
TxGNN 模型預測它可能對**躁鬱症躁症期 (manic bipolar affective disorder)** 有效，
目前有 **20 篇文獻**支持這個方向。
</p>

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 精神病狀態、噁心嘔吐、攻擊性與破壞性行為障礙 |
| 預測新適應症 | manic bipolar affective disorder |
| TxGNN 預測分數 | 99.51% |
| 證據等級 | L3 (有間接文獻證據) |
| 泰國上市 | 已上市 |
| 許可證數 | 47 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Trifluoperazine 是一種典型抗精神病藥物（phenothiazine 類），其作用機轉支持在躁症期的應用：

1. **多巴胺 D2 受體阻斷**：抑制中腦邊緣系統的多巴胺過度活化
2. **鎮靜作用**：減少躁動、攻擊性行為
3. **抗精神病作用**：改善精神病性症狀（如妄想、幻覺）

躁症期常伴隨精神病性症狀，典型抗精神病藥物在非典型藥物問世前是躁症急性期的標準治療選擇之一。

## 臨床試驗證據

目前無針對躁鬱症躁症期的專門臨床試驗，但有多篇文獻支持其在躁症期的使用。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [14309092](https://pubmed.ncbi.nlm.nih.gov/14309092/) | 1965 | Clinical Study | Int J Neuropsychiatry | 比較 Haloperidol 與 Trifluoperazine 在精神分裂症及躁症患者中的療效 |
| [24943390](https://pubmed.ncbi.nlm.nih.gov/24943390/) | 2014 | Survey | J Clin Psychopharmacol | 烏干達精神病院處方模式：Trifluoperazine 與 Carbamazepine 併用治療躁鬱症佔 45% |
| [17017818](https://pubmed.ncbi.nlm.nih.gov/17017818/) | 2006 | Review | J Clin Psychiatry | 典型與非典型抗精神病藥物在躁鬱症焦慮症狀的療效回顧 |
| [970489](https://pubmed.ncbi.nlm.nih.gov/970489/) | 1976 | Case Study | Am J Psychiatry | 探討多巴胺機轉在躁症中的角色 |
| [3935307](https://pubmed.ncbi.nlm.nih.gov/3935307/) | 1985 | Case Report | Can J Psychiatry | 青少年躁鬱症案例，使用 Trifluoperazine 治療 |

## 泰國上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 內衛藥輸字第002368號 | 福路新1公絲 | 錠劑 | 意識運動機能亢進引起之急慢性精神病 |
| 衛署藥製字第002672號 | 惠鎮寧糖衣錠 | 糖衣錠 | 精神病狀態、噁心嘔吐、攻擊性與破壞性行為障礙 |
| 衛署藥製字第032029號 | "強生"富祿靜膜衣錠5毫克 | 膜衣錠 | 精神病狀態、噁心嘔吐、攻擊性與破壞性行為障礙 |
| 衛署藥製字第035165號 | 福樂靜膠囊2公絲 | 膠囊劑 | 精神病狀態、噁心嘔吐、攻擊性與破壞性行為障礙 |

## 安全性考量

- **錐體外症候群 (EPS)**：典型抗精神病藥物的主要副作用
- **遲發性運動障礙 (Tardive dyskinesia)**：長期使用風險
- **神經惡性症候群 (NMS)**：罕見但嚴重的不良反應
- **主要交互作用 (Major)**：
  - Bupropion（降低癲癇閾值）
  - Morphine（增強中樞抑制）
  - Metoclopramide（增加錐體外症狀風險）
  - Potassium chloride、Potassium citrate（增加腸胃道潰瘍風險）
  - Dolasetron（QT 延長風險）
- **中度交互作用 (Moderate)**：
  - 糖尿病藥物（可能影響血糖控制）
  - 抗膽鹼藥物（增加抗膽鹼作用）
  - Levofloxacin（QT 延長風險）


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**Anticholinergic Syndrome** 🟡 Moderate
- 風險包括：血壓控制不良。特別注意族群：老年人。

**Breast Neoplasms** 🟡 Moderate
- 注意事項：The chronic use of phenothiazines is associated with persistent elevations in prolactin levels...

**Dystonic Disorders** 🟡 Moderate
- 可能危及生命。特別注意族群：兒童。

**Hematologic Diseases** 🟡 Moderate
- 風險包括：骨髓抑制、出血、感染、血栓、貧血。

**Neuroleptic Malignant Syndrome** 🟡 Moderate
- 風險包括：心律不整。可能有致命風險。必要時應停止治療。

**Parkinsonian Disorders** 🟡 Moderate
- 注意事項：The use of phenothiazines is associated with pseudo-parkinsonian symptoms such as akinesia, bradykinesia, tremors, pill-rolling motion, cogwheel rigid...

**腎臟疾病** 🟡 Moderate
- 注意事項：Phenothiazines and their metabolites are excreted by the kidney...

**Lung Diseases** 🟡 Moderate
- 風險包括：感染。可能有嚴重不良反應。

**癲癇** 🟡 Moderate
- 風險包括：癲癇發作。

**Tardive Dyskinesia** 🟡 Moderate
- 可能有嚴重不良反應。特別注意族群：老年人。

**Dementia** 🟢 Minor
- 可能有致命風險。

**Alcoholic Intoxication** 🟢 Minor
- 本藥物在此情況下禁用。可能有嚴重不良反應。

**心血管疾病** 🟢 Minor
- 不應使用本藥物。需定期監測。風險包括：低血壓、血栓。可能有致命風險。

**Respiratory Insufficiency** 🟢 Minor
- 本藥物在此情況下禁用。可能有嚴重不良反應。

**Craniocerebral Trauma** 🟢 Minor
- 本藥物在此情況下禁用。

**Hepatic Insufficiency** 🟢 Minor
- 本藥物在此情況下禁用。

### 藥物-食物交互作用 (DFI)

<div class="dfi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**酒精** 🟡 Moderate
- 影響：產生協同作用。
- 建議：建議避免併用。


## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Trifluoperazine 作為典型抗精神病藥物，在躁症期的使用有歷史性臨床經驗支持。多篇文獻顯示其在躁鬱症患者中的應用，特別是在資源有限的地區仍是重要的治療選擇。

**若要推進需要：**
- 與非典型抗精神病藥物的比較研究
- 評估 EPS 及代謝副作用的風險效益比
- 制定明確的劑量建議及監測計畫
- 考量作為急性期治療而非長期維持治療

**臨床提醒：**
現代躁症急性期治療首選通常為非典型抗精神病藥物（如 Olanzapine、Quetiapine、Risperidone），Trifluoperazine 可作為替代選擇，但需注意 EPS 風險。

---

## 相關藥物報告

- [Magnesium Sulfate]({{ "/drugs/magnesium_sulfate/" | relative_url }}) - 證據等級 L5
- [Cephalexin]({{ "/drugs/cephalexin/" | relative_url }}) - 證據等級 L5
- [Deoxycholic Acid]({{ "/drugs/deoxycholic_acid/" | relative_url }}) - 證據等級 L5
- [Berberine]({{ "/drugs/berberine/" | relative_url }}) - 證據等級 L5
- [Butenafine]({{ "/drugs/butenafine/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
ThTxGNN. (2026). Trifluoperazine老藥新用驗證報告. https://thtxgnn.yao.care/drugs/trifluoperazine/
```

**BibTeX 格式：**
```bibtex
@misc{thtxgnn_trifluoperazine,
  title = {Trifluoperazine老藥新用驗證報告},
  author = {ThTxGNN Team},
  year = {2026},
  url = {https://thtxgnn.yao.care/drugs/trifluoperazine/}
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
