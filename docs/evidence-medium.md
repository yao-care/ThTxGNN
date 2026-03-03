---
layout: default
title: หลักฐานระดับกลาง (L3-L4)
parent: รายงานยา
nav_order: 2
has_children: true
description: "ยาที่มีข้อบ่งใช้ใหม่ระดับ L3-L4 มีหลักฐานจากการศึกษาเชิงสังเกตหรือ Preclinical ต้องการการศึกษาเพิ่มเติม"
---

# ยาที่มีหลักฐานระดับกลาง

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

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | sort: "title" %}

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
