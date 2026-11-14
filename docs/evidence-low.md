---
layout: default
title: เฉพาะการคาดการณ์ (L5)
parent: รายงานยา
nav_order: 3
has_children: true
description: "ยาที่มีข้อบ่งใช้ใหม่ระดับ L5 เป็นผลการคาดการณ์จากโมเดล AI เท่านั้น ใช้เป็นแนวทางสำหรับการวิจัยในอนาคต"
permalink: /evidence-low/
redirect_from:
  - /evidence-low.html
---

# ยาที่มีเฉพาะการคาดการณ์จากโมเดล

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L5 %}
หน้านี้แสดงยา **{{ pd_m }}** รายการ จากยาทั้งหมด **{{ site.data.drug_stats.total_drugs }}** รายการที่มีรายงานเผยแพร่บนเว็บไซต์นี้ ({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%) นิยามระดับหลักฐาน: [วิธีการคาดการณ์]({{ '/methodology/' | relative_url }})
<!-- page-data:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
การคาดการณ์จากโมเดล TxGNN ที่ยังไม่มีหลักฐานทางคลินิกสนับสนุน
</p>

---

## มาตรฐานหลักฐาน

| ระดับ | คำจำกัดความ | ความสำคัญทางคลินิก |
|-------|-------------|-------------------|
| **L5** | เฉพาะการคาดการณ์จากโมเดล ไม่มีหลักฐานทางคลินิก | สามารถใช้เป็นสมมติฐานการวิจัย ต้องการการยืนยัน |

<div style="background: #fff3cd; padding: 1rem; border-left: 4px solid #ffc107; border-radius: 4px; margin: 1rem 0;">
<strong>ข้อควรระวัง:</strong> ยาระดับ L5 อิงจากการคาดการณ์ของโมเดลเท่านั้น ยังไม่มีหลักฐานทางคลินิกโดยตรงสนับสนุน ไม่แนะนำให้ใช้สำหรับการตัดสินใจทางคลินิกโดยตรง สามารถใช้เป็นแนวทางการวิจัยได้
</div>

---

## รายการยา

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### ระดับ L5 ({{ l5_drugs.size }} รายการ)

| ชื่อยา | จำนวนข้อบ่งใช้ | ลิงก์ |
|--------|--------------|------|
{% for drug in l5_drugs %}| {{ drug.title }} | {{ drug.indication_count }} | [ดูรายงาน]({{ drug.url | relative_url }}) |
{% endfor %}

