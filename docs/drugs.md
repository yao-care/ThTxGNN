---
layout: default
title: รายการยาทั้งหมด
parent: รายงานยา
nav_order: 4
permalink: /drugs/
---

# รายการยาทั้งหมด

<p style="font-size: 1.1rem; color: #666; margin-bottom: 1.5rem;">
รายการยา <strong>151</strong> รายการที่ขึ้นทะเบียนกับ อย. ประเทศไทย พร้อมการคาดการณ์ข้อบ่งใช้ใหม่
</p>

---

## ภาพรวม

ThTxGNN วิเคราะห์ยา 151 รายการจาก Thai FDA และระบุข้อบ่งใช้ใหม่ที่มีศักยภาพ 2,573,191 รายการ

## สรุปตามระดับหลักฐาน

| ระดับ | จำนวนยา | คำอธิบาย |
|-------|---------|----------|
| L1-L2 | 8 | มีการทดลองทางคลินิกสนับสนุน |
| L3-L4 | 15 | มีหลักฐานจากวรรณกรรม |
| L5 | 128 | เฉพาะการคาดการณ์จากโมเดล |

---

## ค้นหายา

<div id="drug-list-container">
{% assign all_drugs = site.drugs | sort: "title" %}

{% for drug in all_drugs %}
- [{{ drug.title }}]({{ drug.url | relative_url }}) - {{ drug.evidence_level | default: "L5" }}
{% endfor %}
</div>

---

## FHIR API

ใช้ FHIR API เพื่อค้นหายาเฉพาะ:

```bash
# ดูข้อมูลยาทั้งหมด
curl https://thtxgnn.yao.care/fhir/MedicationKnowledge/

# ดูการคาดการณ์สำหรับยาเฉพาะ
curl https://thtxgnn.yao.care/fhir/ClinicalUseDefinition?subject=MedicationKnowledge/DB00381
```

---

## ข้อจำกัดความรับผิดชอบ

การคาดการณ์ทั้งหมดเป็นสมมติฐานจากการคำนวณ ยาที่อาจใช้ในข้อบ่งใช้ใหม่ต้องผ่านการทดลองทางคลินิกก่อนนำไปใช้
