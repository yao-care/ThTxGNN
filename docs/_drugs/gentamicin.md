---
layout: default
title: "Gentamicin"
description: "รายงานการวิเคราะห์ศักยภาพการใช้ยา Gentamicin ในข้อบ่งใช้ใหม่ - ThTxGNN"
parent: การคาดการณ์จากโมเดล (L5)
nav_order: 1
drug_name: "Gentamicin"
drugbank_id: "DB00798"
evidence_level: "L5"
indication_count: 10
---

# Gentamicin

<p class="fs-5 text-grey-dk-100">
ระดับหลักฐาน: <strong>L5</strong> | ข้อบ่งใช้ที่คาดการณ์: <strong>10</strong> รายการ
</p>

---

## สรุปภาพรวม

| รายการ | รายละเอียด |
|--------|------------|
| **DrugBank ID** | [DB00798](https://go.drugbank.com/drugs/DB00798) |
| **เลขทะเบียนยา** | 1A 59/67 |
| **ข้อบ่งใช้เดิม** | โรคติดเชื้อแบคทีเรียรุนแรง |
| **ข้อบ่งใช้ที่คาดการณ์อันดับ 1** | rheumatoid arthritis |
| **คะแนน TxGNN สูงสุด** | 0.9776 |
| **ระดับหลักฐาน** | L5 |
| **ขึ้นทะเบียนในประเทศไทย** | ✅ จดทะเบียนแล้ว |
| **การตัดสินใจแนะนำ** | รอหลักฐานเพิ่มเติม |

## การคาดการณ์ข้อบ่งใช้ใหม่จาก TxGNN

| อันดับ | ข้อบ่งใช้ที่คาดการณ์ | คะแนน TxGNN |
|:------:|---------------------|:-----------:|
| 1 | rheumatoid arthritis | 0.9776 |
| 2 | sclerosing cholangitis | 0.9750 |
| 3 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 0.9632 |
| 4 | brachydactyly-syndactyly syndrome | 0.9528 |
| 5 | autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | 0.9199 |
| 6 | brain small vessel disease 1 with or without ocular anomalies | 0.9170 |
| 7 | osteoarthritis susceptibility | 0.9062 |
| 8 | diabetic nephropathy | 0.8992 |
| 9 | congenital hypotrichosis milia | 0.8890 |
| 10 | unclassified myelodysplastic syndrome | 0.8874 |


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

- [DrugBank: Gentamicin](https://go.drugbank.com/drugs/DB00798)
- [PubMed: Gentamicin](https://pubmed.ncbi.nlm.nih.gov/?term=Gentamicin)
- [ClinicalTrials.gov](https://clinicaltrials.gov/search?term=Gentamicin)

---

<div class="disclaimer" style="background-color: #fff3cd; padding: 1rem; border-radius: 0.5rem; margin-top: 2rem;">
<strong>⚠️ ข้อจำกัดความรับผิดชอบ</strong><br>
รายงานนี้มีไว้เพื่อการวิจัยทางวิชาการเท่านั้น <strong>ไม่ถือเป็นคำแนะนำทางการแพทย์</strong>
การใช้ยาต้องปฏิบัติตามคำแนะนำของแพทย์ ห้ามปรับเปลี่ยนการใช้ยาด้วยตนเอง
การตัดสินใจใช้ยาเก่าในข้อบ่งใช้ใหม่ต้องผ่านการตรวจสอบทางคลินิกและกฎระเบียบอย่างครบถ้วน
<br><br>
<small>ตรวจสอบล่าสุด: 2026-03-03 | ThTxGNN Research Team</small>
</div>
