---
layout: default
title: หลักฐานระดับกลาง (L3-L4)
parent: รายงานยา
nav_order: 2
has_children: true
description: "ยา 14 รายการที่มีหลักฐานระดับ L3–L4 บนเว็บไซต์นี้ (ประเทศไทย) เช่น Alprazolam, Calcipotriol, Magnesium Sulfate พร้อมข้อบ่งใช้หลักที่คาดการณ์ ทะเบียนตำรับยา (อย.) และประวัติการตรวจสอบของแต่ละยา"
permalink: /evidence-medium/
redirect_from:
  - /evidence-medium.html
---

# ยาที่มีหลักฐานระดับกลาง

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
หน้านี้แสดงยา **{{ site.data.evidence_tier_facts.medium.count }}** รายการ จากยาทั้งหมด **{{ site.data.drug_stats.total_drugs }}** รายการที่มีรายงานเผยแพร่บนเว็บไซต์นี้ ({{ site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L3 **{{ site.data.evidence_tier_facts.medium.by_level.L3 }}**, L4 **{{ site.data.evidence_tier_facts.medium.by_level.L4 }}**
ค่ามัธยฐานสัดส่วนระดับ L3–L4 ของเว็บไซต์ TxGNN ทั้ง 30 แห่ง: {{ site.data.evidence_tier_facts.medium.cross.median_share }}% {% if ev_share > site.data.evidence_tier_facts.medium.cross.median_share %}เว็บไซต์นี้สูงกว่าค่ามัธยฐาน{% elsif ev_share < site.data.evidence_tier_facts.medium.cross.median_share %}เว็บไซต์นี้ต่ำกว่าค่ามัธยฐาน{% else %}เว็บไซต์นี้เท่ากับค่ามัธยฐาน{% endif %}

{% if site.data.evidence_tier_facts.medium.count > 0 %}
ในข้อมูลในประเทศ (ทะเบียนตำรับยา (อย.)) ยาเหล่านี้ **{{ site.data.evidence_tier_facts.medium.with_current }}** รายการมีทะเบียนที่คงอยู่อย่างน้อยหนึ่งรายการ **{{ site.data.evidence_tier_facts.medium.none_current }}** รายการมีทะเบียนแต่ไม่มีที่คงอยู่ และ **{{ site.data.evidence_tier_facts.medium.without_data }}** รายการไม่อยู่ในข้อมูลในประเทศ **{{ site.data.evidence_tier_facts.medium.with_reviews }}** รายการมีบันทึกในประวัติการตรวจสอบ (การแก้ไขข้อมูลทะเบียนบนหน้ายา) **{{ site.data.evidence_tier_facts.medium.cross.unique_drugs }}** รายการมีข้อบ่งใช้ที่คาดการณ์ซึ่งเว็บไซต์ TxGNN อื่นไม่มีสำหรับยาเดียวกัน
{% if site.data.evidence_tier_facts.medium.none_current_list.size > 0 %}

มีทะเบียนแต่ไม่มีที่คงอยู่: {% for r in site.data.evidence_tier_facts.medium.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}
{% endif %}

นิยามของทุกระดับ: [วิธีการคาดการณ์]({{ '/methodology/' | relative_url }})
<!-- tier-facts:end -->

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

### ระดับ L3 ({{ site.data.evidence_tier_facts.medium.by_level.L3 }} รายการ)

<!-- tier-table:start L3（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| ยา | ระดับ | ข้อบ่งใช้ใหม่หลักที่คาดการณ์ | ทะเบียนตำรับยา (อย.): คงอยู่ / ทั้งหมด | ประวัติการตรวจสอบ | มีเฉพาะเว็บไซต์นี้ |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L3" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ใช่ ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### ระดับ L4 ({{ site.data.evidence_tier_facts.medium.by_level.L4 }} รายการ)

<!-- tier-table:start L4（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| ยา | ระดับ | ข้อบ่งใช้ใหม่หลักที่คาดการณ์ | ทะเบียนตำรับยา (อย.): คงอยู่ / ทั้งหมด | ประวัติการตรวจสอบ | มีเฉพาะเว็บไซต์นี้ |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L4" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ใช่ ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

