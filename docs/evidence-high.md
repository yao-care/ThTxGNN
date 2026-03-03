---
layout: default
title: หลักฐานระดับสูง (L1-L2)
parent: รายงานยา
nav_order: 1
has_children: true
description: "ยาที่มีข้อบ่งใช้ใหม่ระดับ L1-L2 มีการทดลองทางคลินิกหลายรายการหรือ Systematic Review สนับสนุน ควรพิจารณาเข้าสู่การประเมินทางคลินิก"
---

# ยาที่มีหลักฐานระดับสูง

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
ยาที่ควรพิจารณาเข้าสู่การประเมินทางคลินิกเป็นอันดับแรก
</p>

---

## มาตรฐานหลักฐาน

| ระดับ | คำจำกัดความ | ความสำคัญทางคลินิก |
|-------|-------------|-------------------|
| **L1** | Phase 3 RCT หลายรายการ / Systematic Review | สนับสนุนอย่างแข็งแกร่ง พิจารณาใช้ทางคลินิกได้ |
| **L2** | RCT เดี่ยว หรือ Phase 2 หลายรายการ | สนับสนุนปานกลาง สามารถออกแบบการทดลองยืนยันได้ |

---

## รายการยา

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | sort: "title" %}

### ระดับ L1 ({{ l1_drugs.size }} รายการ)

| ชื่อยา | จำนวนข้อบ่งใช้ | ลิงก์ |
|--------|--------------|------|
{% for drug in l1_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [ดูรายงาน]({{ drug.url | relative_url }}) |
{% endfor %}

### ระดับ L2 ({{ l2_drugs.size }} รายการ)

| ชื่อยา | จำนวนข้อบ่งใช้ | ลิงก์ |
|--------|--------------|------|
{% for drug in l2_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [ดูรายงาน]({{ drug.url | relative_url }}) |
{% endfor %}
