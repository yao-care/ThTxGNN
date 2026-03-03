---
layout: default
title: 高證據等級 (L1-L2)
parent: 藥物報告
nav_order: 1
has_children: true
description: "L1-L2 等級的老藥新用候選藥物，具有多項臨床試驗或系統性回顧支持，可優先考慮進入臨床評估。"
---

# 高證據等級藥物

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
可優先考慮進入臨床評估階段的候選藥物
</p>

---

## 證據標準

| 等級 | 定義 | 臨床意義 |
|------|------|---------|
| **L1** | 多個 Phase 3 RCT / 系統性回顧 | 強力支持，可考慮臨床使用 |
| **L2** | 單一 RCT 或多個 Phase 2 試驗 | 中等支持，可設計驗證試驗 |

---

## 藥物列表

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | sort: "title" %}

### L1 等級 ({{ l1_drugs.size }} 個)

| 藥物名稱 | 適應症數 | 連結 |
|---------|---------|------|
{% for drug in l1_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [查看報告]({{ drug.url | relative_url }}) |
{% endfor %}

### L2 等級 ({{ l2_drugs.size }} 個)

| 藥物名稱 | 適應症數 | 連結 |
|---------|---------|------|
{% for drug in l2_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [查看報告]({{ drug.url | relative_url }}) |
{% endfor %}
