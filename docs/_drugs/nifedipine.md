---
layout: default
title: "Nifedipine"
description: "รายงานการวิเคราะห์ศักยภาพการใช้ยา Nifedipine ในข้อบ่งใช้ใหม่ - ThTxGNN"
parent: การคาดการณ์จากโมเดล (L5)
nav_order: 1
drug_name: "Nifedipine"
drugbank_id: "DB01115"
evidence_level: "L5"
indication_count: 10
---

# Nifedipine

<p class="fs-5 text-grey-dk-100">
ระดับหลักฐาน: <strong>L5</strong> | ข้อบ่งใช้ที่คาดการณ์: <strong>10</strong> รายการ
</p>

---

## สรุปภาพรวม

| รายการ | รายละเอียด |
|--------|------------|
| **DrugBank ID** | [DB01115](https://go.drugbank.com/drugs/DB01115) |
| **เลขทะเบียนยา** | 1A 15/67 |
| **ข้อบ่งใช้เดิม** | ความดันโลหิตสูง, โรคหัวใจขาดเลือด |
| **ข้อบ่งใช้ที่คาดการณ์อันดับ 1** | Prinzmetal angina |
| **คะแนน TxGNN สูงสุด** | 0.9362 |
| **ระดับหลักฐาน** | L5 |
| **ขึ้นทะเบียนในประเทศไทย** | ✅ จดทะเบียนแล้ว |
| **การตัดสินใจแนะนำ** | รอหลักฐานเพิ่มเติม |

## การคาดการณ์ข้อบ่งใช้ใหม่จาก TxGNN

| อันดับ | ข้อบ่งใช้ที่คาดการณ์ | คะแนน TxGNN |
|:------:|---------------------|:-----------:|
| 1 | Prinzmetal angina | 0.9362 |
| 2 | migraine with brainstem aura | 0.9263 |
| 3 | migraine disorder | 0.9180 |
| 4 | pulmonary hypertension owing to lung disease and/or hypoxia | 0.7776 |
| 5 | pulmonary hypertension with unclear multifactorial mechanism | 0.7776 |
| 6 | malignant hypertensive renal disease | 0.7657 |
| 7 | malignant renovascular hypertension | 0.7657 |
| 8 | Braddock syndrome | 0.7396 |
| 9 | tendinitis | 0.7051 |
| 10 | common cold | 0.7016 |


## วิธีการคาดการณ์

การคาดการณ์นี้ใช้โมเดล TxGNN (Therapeutics-Centric Knowledge Graph for Drug Repurposing)
จาก Harvard ซึ่งวิเคราะห์ความสัมพันธ์ระหว่างยาและโรคจาก Knowledge Graph ที่ประกอบด้วย:

- ข้อมูลยาจาก DrugBank
- ข้อมูลโรคจาก Disease Ontology
- ความสัมพันธ์ยา-โรคที่ผ่านการตรวจสอบ

## ข้อควรพิจารณาด้านความปลอดภัย

⚠️ กรุณาอ้างอิงเอกสารกำกับยาฉบับเต็มและปรึกษาแพทย์หรือเภสัชกรก่อนใช้ยา

## สรุปและขั้นตอนถัดไป

**การตัดสินใจ: รอหลักฐานเพิ่มเติม**

**เหตุผล:**
การคาดการณ์นี้อยู่ในระดับหลักฐาน L5 ซึ่งต้องการการวิจัยเพิ่มเติมเพื่อยืนยันประสิทธิภาพ

**สิ่งที่ต้องการเพื่อดำเนินการต่อ:**
- การศึกษากลไกการออกฤทธิ์ของยา (Mechanism of Action)
- การทดลองทางคลินิกเบื้องต้น (Phase I/II Clinical Trial)
- การศึกษาปฏิกิริยาระหว่างยา (Drug Interactions)

---

## แหล่งข้อมูล

- [DrugBank: Nifedipine](https://go.drugbank.com/drugs/DB01115)
- [PubMed: Nifedipine](https://pubmed.ncbi.nlm.nih.gov/?term=Nifedipine)
- [ClinicalTrials.gov](https://clinicaltrials.gov/search?term=Nifedipine)

---

<div class="disclaimer" style="background-color: #fff3cd; padding: 1rem; border-radius: 0.5rem; margin-top: 2rem;">
<strong>⚠️ ข้อจำกัดความรับผิดชอบ</strong><br>
รายงานนี้มีไว้เพื่อการวิจัยทางวิชาการเท่านั้น <strong>ไม่ถือเป็นคำแนะนำทางการแพทย์</strong>
การใช้ยาต้องปฏิบัติตามคำแนะนำของแพทย์ ห้ามปรับเปลี่ยนการใช้ยาด้วยตนเอง
การตัดสินใจใช้ยาเก่าในข้อบ่งใช้ใหม่ต้องผ่านการตรวจสอบทางคลินิกและกฎระเบียบอย่างครบถ้วน
<br><br>
<small>ตรวจสอบล่าสุด: 2026-03-03 | ThTxGNN Research Team</small>
</div>
