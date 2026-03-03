---
layout: default
title: 中證據等級 (L3-L4)
parent: 藥物報告
nav_order: 2
has_children: true
description: "L3-L4 等級的老藥新用候選藥物，具有觀察性研究或前臨床證據支持，值得進一步研究探索。"
---

# 中證據等級藥物

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
需補充證據後可進一步評估的候選藥物
</p>

---

## 證據標準

| 等級 | 定義 | 臨床意義 |
|------|------|---------|
| **L3** | 觀察性研究 / 大型病例系列 | 有初步證據，待補件後評估 |
| **L4** | 前臨床 / 機轉研究 / 個案報告 | 機轉合理，缺乏臨床驗證 |

---

## 藥物列表

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | sort: "title" %}

### L3 等級 ({{ l3_drugs.size }} 個)

| 藥物名稱 | 適應症數 | 連結 |
|---------|---------|------|
{% for drug in l3_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [查看報告]({{ drug.url | relative_url }}) |
{% endfor %}

### L4 等級 ({{ l4_drugs.size }} 個)

| 藥物名稱 | 適應症數 | 連結 |
|---------|---------|------|
{% for drug in l4_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [查看報告]({{ drug.url | relative_url }}) |
{% endfor %}
