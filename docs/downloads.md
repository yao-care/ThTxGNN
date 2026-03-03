---
layout: default
title: 資料下載
parent: 資源
nav_order: 2
description: "下載 ThTxGNN 老藥新用預測資料，包含 191 個藥物的證據等級摘要、高證據藥物清單，以及完整預測資料集。"
permalink: /downloads/
---

# 資料下載

<p class="key-answer" data-question="如何下載 ThTxGNN 的預測資料？">
我們提供多種格式的開放資料下載，供研究人員進行後續分析。所有資料皆採用 CC BY 4.0 授權。
</p>

<div class="key-takeaway">
下載資料前請先閱讀使用條款。引用本資料時，請同時引用原始 TxGNN 論文。
</div>

---

## 快速下載

### 藥物摘要資料

| 檔案 | 格式 | 說明 | 下載 |
|------|------|------|------|
| 藥物證據摘要 | CSV | 191 個藥物的證據等級與適應症數量 | [下載 CSV]({{ '/downloads/thtxgnn_drugs_summary.csv' | relative_url }}) |
| 藥物證據摘要 | JSON | 同上，含證據分布統計 | [下載 JSON]({{ '/downloads/thtxgnn_drugs_summary.json' | relative_url }}) |
| 高證據藥物 | CSV | L1-L2 等級的 18 個藥物 | [下載 CSV]({{ '/downloads/thtxgnn_high_evidence.csv' | relative_url }}) |

### 完整預測資料

完整的老藥新用候選資料（142,328 筆）請從 GitHub 下載：

<p style="margin: 1.5rem 0;">
  <a href="https://github.com/yao-care/ThTxGNN/tree/main/data/processed" target="_blank" rel="noopener" style="display: inline-block; padding: 0.75rem 1.5rem; background: #24292e; color: white; text-decoration: none; border-radius: 4px; font-weight: 600;">
    前往 GitHub 下載完整資料
  </a>
</p>

---

## 資料欄位說明

### thtxgnn_drugs_summary.csv

| 欄位 | 說明 |
|------|------|
| `drug_name` | 藥物英文名稱 |
| `evidence_level` | 證據等級（L1-L5） |
| `indication_count` | 預測適應症數量 |
| `parent_category` | 分類（高/中/低證據等級） |
| `url` | 報告頁面連結 |

### thtxgnn_high_evidence.csv

| 欄位 | 說明 |
|------|------|
| `drug_name` | 藥物英文名稱 |
| `evidence_level` | 證據等級（L1 或 L2） |
| `indication_count` | 預測適應症數量 |
| `url` | 完整報告頁面 URL |

---

## 完整資料集

GitHub 上提供的完整資料：

| 檔案 | 大小 | 說明 |
|------|------|------|
| `repurposing_candidates.csv` | 17 MB | 142,328 筆老藥新用候選 |
| `drug_mapping.csv` | 9 MB | 藥物 DrugBank ID 對應表 |
| `indication_mapping.csv` | 28 MB | 適應症對應表 |

---

## 使用條款

<ol class="actionable-steps">
<li><strong>授權方式</strong>：CC BY 4.0 國際授權</li>
<li><strong>引用要求</strong>：使用資料時需引用本平台及原始 TxGNN 論文</li>
<li><strong>免責聲明</strong>：資料僅供研究參考，不構成醫療建議</li>
<li><strong>更新頻率</strong>：資料隨網站更新同步</li>
</ol>

### 引用格式

**引用本平台：**
```
ThTxGNN. (2026). ThTxGNN 老藥新用驗證報告. https://thtxgnn.yao.care/
```

**引用 TxGNN 模型：**
```
Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. Nature Medicine.
DOI: 10.1038/s41591-023-02233-x
```

---

## API 存取

目前尚未提供 API 存取。如有大量資料需求，請直接從 GitHub 下載或聯繫我們。

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本資料僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>最後更新：2026-02-20 | 資料版本：v1.0</small>
</div>
