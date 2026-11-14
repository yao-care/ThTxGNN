---
layout: default
title: หลักฐานระดับกลาง (L3-L4)
parent: รายงานยา
nav_order: 2
has_children: true
description: "ยาที่มีข้อบ่งใช้ใหม่ระดับ L3-L4 มีหลักฐานจากการศึกษาเชิงสังเกตหรือ Preclinical ต้องการการศึกษาเพิ่มเติม"
permalink: /evidence-medium/
redirect_from:
  - /evidence-medium.html
---

# ยาที่มีหลักฐานระดับกลาง

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L3 | plus: site.data.drug_stats.level_counts.L4 %}
หน้านี้แสดงยา **{{ pd_m }}** รายการ จากยาทั้งหมด **{{ site.data.drug_stats.total_drugs }}** รายการที่มีรายงานเผยแพร่บนเว็บไซต์นี้ ({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%) นิยามระดับหลักฐาน: [วิธีการคาดการณ์]({{ '/methodology/' | relative_url }})
<!-- page-data:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
ยาที่มีหลักฐานเบื้องต้น ต้องการการศึกษาเพิ่มเติม
</p>

---

## มาตรฐานหลักฐาน

| ระดับ | คำจำกัดความ | ความสำคัญทางคลินิก |
|-------|-------------|-------------------|
| **L3** | การศึกษาเชิงสังเกต / กลุ่มตัวอย่างขนาดใหญ่ | มีหลักฐานเบื้องต้น ต้องเพิ่มเติมก่อนประเมิน |
| **L4** | การศึกษา Preclinical / กลไก / รายงานผู้ป่วย | กลไกสมเหตุสมผล ขาดการยืนยันทางคลินิก |

---

## รายการยา

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### ระดับ L3 ({{ l3_drugs.size }} รายการ)

| ชื่อยา | จำนวนข้อบ่งใช้ | ลิงก์ |
|--------|--------------|------|
{% for drug in l3_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [ดูรายงาน]({{ drug.url | relative_url }}) |
{% endfor %}

### ระดับ L4 ({{ l4_drugs.size }} รายการ)

| ชื่อยา | จำนวนข้อบ่งใช้ | ลิงก์ |
|--------|--------------|------|
{% for drug in l4_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [ดูรายงาน]({{ drug.url | relative_url }}) |
{% endfor %}

