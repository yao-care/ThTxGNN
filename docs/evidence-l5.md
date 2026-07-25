---
layout: default
title: การคาดการณ์จากโมเดล (L5)
nav_order: 15
has_children: true
permalink: /evidence-l5/
redirect_from:
  - /evidence-l5.html
---

# การคาดการณ์จากโมเดล (L5)

รายการยาในระดับหลักฐาน L5

{% assign drugs = site.drugs | where: "evidence_level", "L5" %}
{% for drug in drugs %}
- [{{ drug.title }}]({{ drug.url | relative_url }}) - {{ drug.drugbank_id }}
{% endfor %}

