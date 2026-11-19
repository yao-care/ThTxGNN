---
layout: default
title: หลักฐานระดับสูง (L1-L2)
parent: รายงานยา
nav_order: 1
has_children: true
description: "ยา 10 รายการที่มีหลักฐานระดับ L1–L2 บนเว็บไซต์นี้ (ประเทศไทย) เช่น Atorvastatin, Bupropion, Clozapine พร้อมข้อบ่งใช้หลักที่คาดการณ์ ทะเบียนตำรับยา (อย.) และประวัติการตรวจสอบของแต่ละยา"
permalink: /evidence-high/
redirect_from:
  - /evidence-high.html
---

# ยาที่มีหลักฐานระดับสูง

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
หน้านี้แสดงยา **{{ site.data.evidence_tier_facts.high.count }}** รายการ จากยาทั้งหมด **{{ site.data.drug_stats.total_drugs }}** รายการที่มีรายงานเผยแพร่บนเว็บไซต์นี้ ({{ site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L1 **{{ site.data.evidence_tier_facts.high.by_level.L1 }}**, L2 **{{ site.data.evidence_tier_facts.high.by_level.L2 }}**
ค่ามัธยฐานสัดส่วนระดับ L1–L2 ของเว็บไซต์ TxGNN ทั้ง 30 แห่ง: {{ site.data.evidence_tier_facts.high.cross.median_share }}% {% if ev_share > site.data.evidence_tier_facts.high.cross.median_share %}เว็บไซต์นี้สูงกว่าค่ามัธยฐาน{% elsif ev_share < site.data.evidence_tier_facts.high.cross.median_share %}เว็บไซต์นี้ต่ำกว่าค่ามัธยฐาน{% else %}เว็บไซต์นี้เท่ากับค่ามัธยฐาน{% endif %}

{% if site.data.evidence_tier_facts.high.count > 0 %}
ในข้อมูลในประเทศ (ทะเบียนตำรับยา (อย.)) ยาเหล่านี้ **{{ site.data.evidence_tier_facts.high.with_current }}** รายการมีทะเบียนที่คงอยู่อย่างน้อยหนึ่งรายการ **{{ site.data.evidence_tier_facts.high.none_current }}** รายการมีทะเบียนแต่ไม่มีที่คงอยู่ และ **{{ site.data.evidence_tier_facts.high.without_data }}** รายการไม่อยู่ในข้อมูลในประเทศ **{{ site.data.evidence_tier_facts.high.with_reviews }}** รายการมีบันทึกในประวัติการตรวจสอบ (การแก้ไขข้อมูลทะเบียนบนหน้ายา) **{{ site.data.evidence_tier_facts.high.cross.unique_drugs }}** รายการมีข้อบ่งใช้ที่คาดการณ์ซึ่งเว็บไซต์ TxGNN อื่นไม่มีสำหรับยาเดียวกัน
{% if site.data.evidence_tier_facts.high.none_current_list.size > 0 %}

มีทะเบียนแต่ไม่มีที่คงอยู่: {% for r in site.data.evidence_tier_facts.high.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}
{% endif %}

นิยามของทุกระดับ: [วิธีการคาดการณ์]({{ '/methodology/' | relative_url }})
<!-- tier-facts:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
ยาที่ควรพิจารณาเข้าสู่การประเมินทางคลินิกเป็นอันดับแรก
</p>

ยาใดในกลุ่มนี้มีหลักฐานจากการทดลองสำหรับข้อบ่งใช้ใหม่ที่ทำนาย และอ้างอิงการทดลองที่ลงทะเบียนกี่รายการ? ดู[ยาในประเทศไทยที่ข้อบ่งใช้ใหม่มีหลักฐานจากการทดลองทางคลินิก]({{ '/clinical-trial-evidence/' | relative_url }})

---

## มาตรฐานหลักฐาน

| ระดับ | คำจำกัดความ | ความสำคัญทางคลินิก |
|-------|-------------|-------------------|
| **L1** | Phase 3 RCT หลายรายการ / Systematic Review | สนับสนุนอย่างแข็งแกร่ง พิจารณาใช้ทางคลินิกได้ |
| **L2** | RCT เดี่ยว หรือ Phase 2 หลายรายการ | สนับสนุนปานกลาง สามารถออกแบบการทดลองยืนยันได้ |

---

## รายการยา

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### ระดับ L1 ({{ site.data.evidence_tier_facts.high.by_level.L1 }} รายการ)

<!-- tier-table:start L1（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| ยา | ระดับ | ข้อบ่งใช้ใหม่หลักที่คาดการณ์ | ทะเบียนตำรับยา (อย.): คงอยู่ / ทั้งหมด | ประวัติการตรวจสอบ | มีเฉพาะเว็บไซต์นี้ |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L1" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ใช่ ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### ระดับ L2 ({{ site.data.evidence_tier_facts.high.by_level.L2 }} รายการ)

<!-- tier-table:start L2（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| ยา | ระดับ | ข้อบ่งใช้ใหม่หลักที่คาดการณ์ | ทะเบียนตำรับยา (อย.): คงอยู่ / ทั้งหมด | ประวัติการตรวจสอบ | มีเฉพาะเว็บไซต์นี้ |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L2" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ใช่ ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

