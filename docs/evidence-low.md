---
layout: default
title: เฉพาะการคาดการณ์ (L5)
parent: รายงานยา
nav_order: 3
has_children: true
description: "ยา 101 รายการที่มีหลักฐานระดับ L5 บนเว็บไซต์นี้ (ประเทศไทย) เช่น Amoxicillin, Chlorpheniramine, Ibuprofen พร้อมข้อบ่งใช้หลักที่คาดการณ์ ทะเบียนตำรับยา (อย.) และประวัติการตรวจสอบของแต่ละยา"
permalink: /evidence-low/
redirect_from:
  - /evidence-low.html
---

# ยาที่มีเฉพาะการคาดการณ์จากโมเดล

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
หน้านี้แสดงยา **{{ site.data.evidence_tier_facts.low.count }}** รายการ จากยาทั้งหมด **{{ site.data.drug_stats.total_drugs }}** รายการที่มีรายงานเผยแพร่บนเว็บไซต์นี้ ({{ site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L5 **{{ site.data.evidence_tier_facts.low.by_level.L5 }}**
ค่ามัธยฐานสัดส่วนระดับ L5 ของเว็บไซต์ TxGNN ทั้ง 30 แห่ง: {{ site.data.evidence_tier_facts.low.cross.median_share }}% {% if ev_share > site.data.evidence_tier_facts.low.cross.median_share %}เว็บไซต์นี้สูงกว่าค่ามัธยฐาน{% elsif ev_share < site.data.evidence_tier_facts.low.cross.median_share %}เว็บไซต์นี้ต่ำกว่าค่ามัธยฐาน{% else %}เว็บไซต์นี้เท่ากับค่ามัธยฐาน{% endif %}

{% if site.data.evidence_tier_facts.low.count > 0 %}
ในข้อมูลในประเทศ (ทะเบียนตำรับยา (อย.)) ยาเหล่านี้ **{{ site.data.evidence_tier_facts.low.with_current }}** รายการมีทะเบียนที่คงอยู่อย่างน้อยหนึ่งรายการ **{{ site.data.evidence_tier_facts.low.none_current }}** รายการมีทะเบียนแต่ไม่มีที่คงอยู่ และ **{{ site.data.evidence_tier_facts.low.without_data }}** รายการไม่อยู่ในข้อมูลในประเทศ **{{ site.data.evidence_tier_facts.low.with_reviews }}** รายการมีบันทึกในประวัติการตรวจสอบ (การแก้ไขข้อมูลทะเบียนบนหน้ายา) **{{ site.data.evidence_tier_facts.low.cross.unique_drugs }}** รายการมีข้อบ่งใช้ที่คาดการณ์ซึ่งเว็บไซต์ TxGNN อื่นไม่มีสำหรับยาเดียวกัน
{% if site.data.evidence_tier_facts.low.none_current_list.size > 0 %}

มีทะเบียนแต่ไม่มีที่คงอยู่: {% for r in site.data.evidence_tier_facts.low.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

แสดงยาที่มีทะเบียนในประเทศที่คงอยู่ก่อน
{% endif %}

นิยามของทุกระดับ: [วิธีการคาดการณ์]({{ '/methodology/' | relative_url }})
<!-- tier-facts:end -->

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

### ระดับ L5 ({{ site.data.evidence_tier_facts.low.by_level.L5 }} รายการ)

<!-- tier-table:start L5（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| ยา | ระดับ | ข้อบ่งใช้ใหม่หลักที่คาดการณ์ | ทะเบียนตำรับยา (อย.): คงอยู่ / ทั้งหมด | ประวัติการตรวจสอบ | มีเฉพาะเว็บไซต์นี้ |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.low.rows %}{% if r.l == "L5" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ใช่ ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

