---
layout: default
title: หลักฐานอ่อน (L4)
nav_order: 14
has_children: true
permalink: /evidence-l4/
redirect_from:
  - /evidence-l4.html
---

# หลักฐานอ่อน (L4)

รายการยาในระดับหลักฐาน L4

{% assign drugs = site.drugs | where: "evidence_level", "L4" %}
{% for drug in drugs %}
- [{{ drug.title }}]({{ drug.url | relative_url }}) - {{ drug.drugbank_id }}
{% endfor %}

