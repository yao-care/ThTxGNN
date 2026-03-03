---
layout: default
title: "Oseltamivir"
description: "รายงานการวิเคราะห์ศักยภาพการใช้ยา Oseltamivir ในข้อบ่งใช้ใหม่ - ThTxGNN"
parent: การคาดการณ์จากโมเดล (L5)
nav_order: 1
drug_name: "Oseltamivir"
drugbank_id: "DB00198"
evidence_level: "L5"
indication_count: 10
---

# Oseltamivir

<p class="fs-5 text-grey-dk-100">
ระดับหลักฐาน: <strong>L5</strong> | ข้อบ่งใช้ที่คาดการณ์: <strong>10</strong> รายการ
</p>

---

## สรุปภาพรวม

| รายการ | รายละเอียด |
|--------|------------|
| **DrugBank ID** | [DB00198](https://go.drugbank.com/drugs/DB00198) |
| **เลขทะเบียนยา** | 1A 94/67 |
| **ข้อบ่งใช้เดิม** | ไข้หวัดใหญ่ |
| **ข้อบ่งใช้ที่คาดการณ์อันดับ 1** | influenza, severe, susceptibility to |
| **คะแนน TxGNN สูงสุด** | 0.9872 |
| **ระดับหลักฐาน** | L5 |
| **ขึ้นทะเบียนในประเทศไทย** | ✅ จดทะเบียนแล้ว |
| **การตัดสินใจแนะนำ** | รอหลักฐานเพิ่มเติม |

## การคาดการณ์ข้อบ่งใช้ใหม่จาก TxGNN

| อันดับ | ข้อบ่งใช้ที่คาดการณ์ | คะแนน TxGNN |
|:------:|---------------------|:-----------:|
| 1 | influenza, severe, susceptibility to | 0.9872 |
| 2 | pyelonephritis | 0.9785 |
| 3 | disorder of tyrosine metabolism | 0.9669 |
| 4 | teratogenic Pierre Robin syndrome | 0.9612 |
| 5 | disorder of phenylalanine metabolism | 0.9574 |
| 6 | tetrahydrobiopterin-responsive hyperphenylalaninemia/phenylketonuria | 0.9510 |
| 7 | staphylococcus aureus infection | 0.9505 |
| 8 | cardioencephalomyopathy, fatal infantile, due to cytochrome c oxidase deficiency | 0.9393 |
| 9 | pneumonia | 0.9214 |
| 10 | influenza | 0.9074 |


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

- [DrugBank: Oseltamivir](https://go.drugbank.com/drugs/DB00198)
- [PubMed: Oseltamivir](https://pubmed.ncbi.nlm.nih.gov/?term=Oseltamivir)
- [ClinicalTrials.gov](https://clinicaltrials.gov/search?term=Oseltamivir)

---

<div class="disclaimer" style="background-color: #fff3cd; padding: 1rem; border-radius: 0.5rem; margin-top: 2rem;">
<strong>⚠️ ข้อจำกัดความรับผิดชอบ</strong><br>
รายงานนี้มีไว้เพื่อการวิจัยทางวิชาการเท่านั้น <strong>ไม่ถือเป็นคำแนะนำทางการแพทย์</strong>
การใช้ยาต้องปฏิบัติตามคำแนะนำของแพทย์ ห้ามปรับเปลี่ยนการใช้ยาด้วยตนเอง
การตัดสินใจใช้ยาเก่าในข้อบ่งใช้ใหม่ต้องผ่านการตรวจสอบทางคลินิกและกฎระเบียบอย่างครบถ้วน
<br><br>
<small>ตรวจสอบล่าสุด: 2026-03-03 | ThTxGNN Research Team</small>
</div>
