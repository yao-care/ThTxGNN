---
layout: default
title: รายการยาทั้งหมด
parent: รายงานยา
nav_order: 4
permalink: /drugs/
---
{%- comment -%}2026-10-27 build gate：站上各頁的藥物數讀 site.data.drug_stats；它和實際公開藥物頁數／等級分布不一致時，
故意 include 不存在的檔讓 Jekyll 建置失敗，錯誤訊息即修法。{%- endcomment -%}
{%- assign gate_listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign gate_ds = site.data.drug_stats -%}
{%- assign gate_l1 = gate_listed | where: "evidence_level", "L1" | size -%}
{%- assign gate_l2 = gate_listed | where: "evidence_level", "L2" | size -%}
{%- assign gate_l3 = gate_listed | where: "evidence_level", "L3" | size -%}
{%- assign gate_l4 = gate_listed | where: "evidence_level", "L4" | size -%}
{%- assign gate_l5 = gate_listed | where: "evidence_level", "L5" | size -%}
{%- if gate_listed.size != gate_ds.total_drugs or gate_l1 != gate_ds.level_counts.L1 or gate_l2 != gate_ds.level_counts.L2 or gate_l3 != gate_ds.level_counts.L3 or gate_l4 != gate_ds.level_counts.L4 or gate_l5 != gate_ds.level_counts.L5 -%}
{% include ERROR-docs-data-drug_stats-json-out-of-sync--run-python3-scripts-generate_drug_stats-py.html %}
{%- endif %}
{%- comment -%}2026-10-16：列表不含舊 ID 轉址頁與 noindex 頁{%- endcomment -%}
{% assign listed_drugs = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" %}

# รายการยาทั้งหมด

<p style="font-size: 1.1rem; color: #666; margin-bottom: 1.5rem;">
รายการยา <strong>{{ site.data.drug_stats.total_drugs }}</strong> รายการที่ขึ้นทะเบียนกับ อย. ประเทศไทย พร้อมการคาดการณ์ข้อบ่งใช้ใหม่
</p>

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
รายการนี้อ้างอิงข้อมูลทะเบียนยาของ [Thai FDA](https://www.fda.moph.go.th/) (ประเทศไทย)

<!-- local-home:end -->

รายการคัดเลือก: [ยาในประเทศไทยที่ข้อบ่งใช้ใหม่มีหลักฐานจากการทดลองทางคลินิก]({{ '/clinical-trial-evidence/' | relative_url }}) (L1–L2 พร้อมข้อบ่งใช้ที่ทำนายและจำนวนการทดลองที่ลงทะเบียนซึ่งอ้างอิง)

## ภาพรวม

ThTxGNN วิเคราะห์ยา {{ site.data.drug_stats.total_drugs }} รายการจาก Thai FDA และระบุข้อบ่งใช้ใหม่ที่มีศักยภาพ {{ site.data.site_stats.indications }} รายการ

## สรุปตามระดับหลักฐาน

{% assign lc = site.data.drug_stats.level_counts %}{% assign lv_hi = lc.L1 | plus: lc.L2 %}{% assign lv_mid = lc.L3 | plus: lc.L4 %}

| ระดับ | จำนวนยา | คำอธิบาย |
|-------|---------|----------|
| L1-L2 | {{ lv_hi }} | มีการทดลองทางคลินิกสนับสนุน |
| L3-L4 | {{ lv_mid }} | มีหลักฐานจากวรรณกรรม |
| L5 | {{ lc.L5 }} | เฉพาะการคาดการณ์จากโมเดล |

---

## ค้นหายา

<div id="drug-list-container">
{% assign all_drugs = listed_drugs | sort: "title" %}

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
