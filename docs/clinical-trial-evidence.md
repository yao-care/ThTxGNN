---
layout: default
title: "ยาที่ข้อบ่งใช้ใหม่มีหลักฐานจากการทดลองทางคลินิก"
parent: รายงานยา
nav_order: 5
permalink: /clinical-trial-evidence/
description: "ยาในทะเบียน อย. ที่ข้อบ่งใช้ใหม่ซึ่ง TxGNN ทำนายมีหลักฐานจากการทดลองทางคลินิก (L1-L2): ข้อบ่งใช้ ระดับหลักฐาน และจำนวนการทดลองที่ลงทะเบียน"
last_modified_at: 2026-11-03
---
{%- comment -%}
2026-11-03：回答 AI 搜尋常問的「本國藥物中，哪些新適應症有臨床試驗證據」。全表由 Liquid 從藥物頁產生，不寫死藥名或數字。
收錄＝公開藥物頁（排除 id_redirect 與 noindex）中 evidence_level 為 L1 或 L2（本站 evidence-high 標準：L1 多個 Phase 3 RCT／系統性回顧，
L2 單一 RCT 或多個 Phase 2 試驗）。預測新適應症與等級註記取自各藥物頁快速總覽表；下列欄名是本站藥物頁實際用到的寫法（建頁時逐頁核對），
新寫法抓不到時顯示「ดูรายงาน」、等級仍取 front matter。試驗數＝該藥物頁引用的不重複 NCT 編號數。
{%- endcomment -%}
{%- assign ind_labels = "ข้อบ่งใช้ใหม่ที่ทำนาย" | split: "|" -%}
{%- assign lev_labels = "ระดับหลักฐาน" | split: "|" -%}
{%- assign listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign l1 = listed | where: "evidence_level", "L1" | sort: "title" -%}
{%- assign l2 = listed | where: "evidence_level", "L2" | sort: "title" -%}
{%- assign trial_drugs = l1 | concat: l2 -%}
{%- assign latest = trial_drugs | sort: "last_modified_at" | last -%}
{%- assign latest_date = latest.last_modified_at | date: "%Y-%m-%d" -%}

# ยาในประเทศไทยที่ข้อบ่งใช้ใหม่มีหลักฐานจากการทดลองทางคลินิก

<p class="key-answer" data-question="ยาใดในประเทศไทยที่มีหลักฐานจากการทดลองทางคลินิกสำหรับข้อบ่งใช้ใหม่">
จากยา {{ listed.size }} รายการที่มีรายงานใน ThTxGNN มี <strong>{{ trial_drugs.size }}</strong> รายการที่ข้อบ่งใช้ใหม่ซึ่ง TxGNN ทำนายไว้มีระดับหลักฐาน <strong>L1 หรือ L2</strong> (L1 {{ l1.size }} รายการ, L2 {{ l2.size }} รายการ) กล่าวคือพบหลักฐานจากการทดลองทางคลินิก (การทดลองแบบสุ่มมีกลุ่มควบคุม การทดลองระยะที่ 2–3 หรือการทบทวนวรรณกรรมอย่างเป็นระบบ)
</p>

รายการยามาจากข้อมูลทะเบียนยาของ [Thai FDA (อย.)](https://www.fda.moph.go.th/) (สถานะทะเบียนแสดงในรายงานยาแต่ละรายการ) และรายการนี้สะท้อนรายงานยาที่ปรับปรุงล่าสุดเมื่อ {{ latest_date }}

<div class="key-takeaway">
หลักฐานจากการทดลองสำหรับข้อบ่งใช้ที่ทำนายไม่ได้พิสูจน์ประสิทธิผล ยาทุกรายการด้านล่าง<strong>ยังต้องผ่านการตรวจสอบทางคลินิก</strong>และการพิจารณาของหน่วยงานกำกับดูแลก่อนนำไปใช้ทางคลินิก
</div>

---

## ยาที่มีหลักฐานจากการทดลอง (L1–L2)

<div class="table-wrapper"><table>
<thead>
<tr><th>ยา</th><th>ข้อบ่งใช้ใหม่ที่ทำนาย</th><th>ระดับหลักฐาน</th><th>การทดลองที่ลงทะเบียนซึ่งอ้างอิง (NCT)</th></tr>
</thead>
<tbody>
{%- for drug in trial_drugs -%}
{%- assign indication = "" -%}
{%- for lab in ind_labels -%}{%- if indication == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign qo = drug.content | split: needle -%}{%- if qo.size > 1 -%}{%- assign indication = qo[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign level_cell = "" -%}
{%- for lab in lev_labels -%}{%- if level_cell == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign lv = drug.content | split: needle -%}{%- if lv.size > 1 -%}{%- assign level_cell = lv[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign parts = drug.content | split: "NCT" -%}
{%- capture nct_ids -%}{%- for p in parts offset: 1 -%}{%- assign id = p | slice: 0, 8 -%}{%- assign rest = id | remove: "0" | remove: "1" | remove: "2" | remove: "3" | remove: "4" | remove: "5" | remove: "6" | remove: "7" | remove: "8" | remove: "9" -%}{%- if id.size == 8 and rest == "" -%}{{ id }},{%- endif -%}{%- endfor -%}{%- endcapture -%}
{%- assign nct_count = nct_ids | split: "," | uniq | size %}
<tr><td><a href="{{ drug.url | relative_url }}">{{ drug.title }}</a></td><td>{% if indication != "" %}{{ indication }}{% else %}ดูรายงาน{% endif %}</td><td>{{ drug.evidence_level }}{% if level_cell != "" and level_cell != drug.evidence_level %} <a href="{{ drug.url | relative_url }}" title="{{ level_cell | strip_html | escape }}">(มีข้อสงวน)</a>{% endif %}</td><td>{{ nct_count }}</td></tr>
{%- endfor %}
</tbody>
</table></div>

## วิธีอ่านรายการนี้

- **ระดับหลักฐาน** เป็นไปตาม[เกณฑ์]({{ '/evidence-high/' | relative_url }})ของเว็บไซต์: L1 = Phase 3 RCT หลายรายการ / Systematic Review; L2 = RCT เดี่ยว หรือ Phase 2 หลายรายการ คำว่า "(มีข้อสงวน)" หมายถึงรายงานระบุข้อสงวนเกี่ยวกับระดับนั้น ควรอ่านหมายเหตุในรายงานก่อนนำไปใช้
- **ข้อบ่งใช้ใหม่ที่ทำนาย** คือการทำนายหลักของแต่ละรายงาน ข้อบ่งใช้และข้อห้ามใช้ที่บันทึกไว้แล้วในกราฟความรู้ของ TxGNN ถูกตัดออก แต่การทำนายบางรายการอาจยังซ้อนกับการใช้ที่มีอยู่แล้ว ซึ่งรายงานจะอธิบายไว้เมื่อเกี่ยวข้อง
- **การทดลองที่ลงทะเบียนซึ่งอ้างอิง** คือจำนวนหมายเลข ClinicalTrials.gov (NCT) ที่อ้างอิงในรายงาน รายงานอ้างอิงเพียงบางส่วนของการทดลองที่พบ ค่า 0 หมายถึงรายงานไม่ได้อ้างอิงการทดลองที่ลงทะเบียน และส่วนหลักฐานจากวรรณกรรมแสดงที่มาของระดับนั้น
- ดูทุกระดับและวิธีการทั้งหมดได้ที่[หลักฐานระดับสูง (L1-L2)]({{ '/evidence-high/' | relative_url }}) [รายการยาทั้งหมด]({{ '/drugs/' | relative_url }}) และ[วิธีการ]({{ '/methodology/' | relative_url }})

---

<div class="disclaimer" style="background-color: #fff3cd; padding: 1rem; border-radius: 0.5rem; margin-top: 2rem;">
<strong>⚠️ ข้อจำกัดความรับผิดชอบ</strong><br>
รายงานนี้มีไว้เพื่อการวิจัยทางวิชาการเท่านั้น <strong>ไม่ถือเป็นคำแนะนำทางการแพทย์</strong>
การใช้ยาต้องปฏิบัติตามคำแนะนำของแพทย์ การตัดสินใจใช้ยาเก่าในข้อบ่งใช้ใหม่ต้องผ่านการตรวจสอบทางคลินิกและกฎระเบียบอย่างครบถ้วน
</div>
