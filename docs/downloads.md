---
layout: default
title: ดาวน์โหลด
parent: แหล่งข้อมูล
nav_order: 1
permalink: /downloads/
redirect_from:
  - /downloads.html
---

# ดาวน์โหลดข้อมูล

## ไฟล์ที่พร้อมดาวน์โหลด

| ไฟล์ | รูปแบบ | คำอธิบาย |
|------|:------:|----------|
| [thtxgnn_drugs_summary.csv](/downloads/thtxgnn_drugs_summary.csv) | CSV | สรุปยาทุกตัวที่มีหน้ายาเผยแพร่บนเว็บไซต์ ({{ site.data.drug_stats.total_drugs }} รายการ) หนึ่งแถวต่อยาหนึ่งตัว |
| [thtxgnn_drugs_summary.json](/downloads/thtxgnn_drugs_summary.json) | JSON | ข้อมูลเดียวกับไฟล์ CSV ด้านบนในรูปแบบ JSON |
| [thtxgnn_high_evidence.csv](/downloads/thtxgnn_high_evidence.csv) | CSV | เฉพาะยาที่ระดับหลักฐานบนหน้ายาเป็น L1–L4 |

ไฟล์ทั้งสามสร้างใหม่จากหน้ายาปัจจุบันทุกครั้งที่หน้ายาเปลี่ยน ไม่รวมหน้าที่ไม่ได้เผยแพร่ (noindex) และหน้าเปลี่ยนเส้นทาง ระดับหลักฐานในไฟล์ตรงกับที่แสดงบนหน้ายาแต่ละหน้า

### คำอธิบายคอลัมน์

| คอลัมน์ | ความหมาย |
|------|----------|
| `slug`, `name`, `url` | ชื่อไฟล์หน้ายา ชื่อยา และที่อยู่หน้ายา |
| `evidence_level` | ระดับหลักฐานที่แสดงบนหน้ายา (L1–L5; N/A = มีเฉพาะข้อบ่งใช้ที่ทราบแล้ว ไม่มีข้อบ่งใช้ใหม่ที่คาดการณ์) |
| `indication_count` | จำนวนข้อบ่งใช้ที่คาดการณ์ที่แสดงบนหน้ายา |
| `predicted_indication`, `txgnn_score` | ข้อบ่งใช้ที่คาดการณ์ซึ่งมีคะแนน TxGNN สูงสุดของยานั้นใน [ดัชนีค้นหา](/data/search-index.json) ตรงกับแถว "ข้อบ่งใช้ใหม่ที่ทำนาย" และ "คะแนนการทำนาย TxGNN" ในภาพรวมฉบับย่อของหน้ายา คะแนนอยู่ในช่วง 0–1 เป็นคะแนนของโมเดล ไม่ใช่ระดับหลักฐาน เว้นว่างเมื่อไม่มีการคาดการณ์ |
| `original_indication` | แถว "ข้อบ่งใช้เดิม" บนหน้ายา เว้นว่างเมื่อหน้ายาไม่มีบันทึก |
| `decision` | แถว "คำแนะนำในการตัดสินใจ" บนหน้ายา ตามข้อความเดิมบนหน้า (เช่น Hold, Proceed with Guardrails) เว้นว่างเมื่อไม่มี |
| `thailand_approved` | `True` = หน้ายาระบุว่ามีทะเบียนตำรับยาที่ยังมีผล; `False` = หน้ายาระบุว่าทะเบียนทั้งหมดถูกยกเลิก; ว่าง = ไม่พบข้อมูลทะเบียน |
| `drugbank_id`, `license_id` | เว้นว่าง (ยังไม่มีแหล่งข้อมูลที่ตรวจสอบได้) |

ผลการคาดการณ์ในไฟล์เหล่านี้เป็นข้อมูลเพื่อการวิจัยเท่านั้น ไม่ใช่คำแนะนำทางการแพทย์ และต้องผ่านการตรวจสอบทางคลินิกก่อนนำไปใช้

## FHIR Resources

- [FHIR CapabilityStatement](/fhir/metadata)
- MedicationKnowledge: [Bundle all-predictions.json](/fhir/Bundle/all-predictions.json)（รายการ: `/fhir/MedicationKnowledge/{drug-slug}.json`）
- ClinicalUseDefinition: `/fhir/ClinicalUseDefinition/{drug-indication-slug}.json`（ตัวอย่าง: [metformin-classic-stiff-person-syndrome.json](/fhir/ClinicalUseDefinition/metformin-classic-stiff-person-syndrome.json)）

## API

ดูเอกสาร [FHIR API](/api/) สำหรับการเข้าถึงข้อมูลผ่าน API

## ลิขสิทธิ์และการอนุญาต

ข้อมูลในเว็บไซต์นี้เผยแพร่ภายใต้สัญญาอนุญาต Creative Commons Attribution 4.0 International (CC BY 4.0)

