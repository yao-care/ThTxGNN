---
layout: default
title: "Dabigatran"
description: "รายงานการวิเคราะห์ศักยภาพการใช้ยา Dabigatran ในข้อบ่งใช้ใหม่ - ThTxGNN"
parent: การคาดการณ์จากโมเดล (L5)
nav_order: 1
drug_name: "Dabigatran"
drugbank_id: "DB14726"
evidence_level: "L5"
indication_count: 10
---

# Dabigatran

<p class="fs-5 text-grey-dk-100">
ระดับหลักฐาน: <strong>L5</strong> | ข้อบ่งใช้ที่คาดการณ์: <strong>10</strong> รายการ
</p>

---

## สรุปภาพรวม

| รายการ | รายละเอียด |
|--------|------------|
| **DrugBank ID** | [DB14726](https://go.drugbank.com/drugs/DB14726) |
| **เลขทะเบียนยา** | 1A 124/67 |
| **ข้อบ่งใช้เดิม** | ป้องกันลิ่มเลือด, หัวใจเต้นผิดจังหวะ |
| **ข้อบ่งใช้ที่คาดการณ์อันดับ 1** | hemoglobinopathy |
| **คะแนน TxGNN สูงสุด** | 0.9843 |
| **ระดับหลักฐาน** | L5 |
| **ขึ้นทะเบียนในประเทศไทย** | ✅ จดทะเบียนแล้ว |
| **การตัดสินใจแนะนำ** | รอหลักฐานเพิ่มเติม |

## การคาดการณ์ข้อบ่งใช้ใหม่จาก TxGNN

| อันดับ | ข้อบ่งใช้ที่คาดการณ์ | คะแนน TxGNN |
|:------:|---------------------|:-----------:|
| 1 | hemoglobinopathy | 0.9843 |
| 2 | myocardial infarction | 0.9813 |
| 3 | partial deletion of the short arm of chromosome 16 | 0.9778 |
| 4 | beta-thalassemia with other manifestations | 0.9774 |
| 5 | hemolytic anemia due to glucophosphate isomerase deficiency | 0.9760 |
| 6 | pyruvate kinase deficiency of red cells | 0.9752 |
| 7 | posterolateral myocardial infarction | 0.9751 |
| 8 | posteroinferior myocardial infarction | 0.9751 |
| 9 | septal myocardial infarction | 0.9744 |
| 10 | coronary thrombosis | 0.9737 |


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

- [DrugBank: Dabigatran](https://go.drugbank.com/drugs/DB14726)
- [PubMed: Dabigatran](https://pubmed.ncbi.nlm.nih.gov/?term=Dabigatran)
- [ClinicalTrials.gov](https://clinicaltrials.gov/search?term=Dabigatran)

---

<div class="disclaimer" style="background-color: #fff3cd; padding: 1rem; border-radius: 0.5rem; margin-top: 2rem;">
<strong>⚠️ ข้อจำกัดความรับผิดชอบ</strong><br>
รายงานนี้มีไว้เพื่อการวิจัยทางวิชาการเท่านั้น <strong>ไม่ถือเป็นคำแนะนำทางการแพทย์</strong>
การใช้ยาต้องปฏิบัติตามคำแนะนำของแพทย์ ห้ามปรับเปลี่ยนการใช้ยาด้วยตนเอง
การตัดสินใจใช้ยาเก่าในข้อบ่งใช้ใหม่ต้องผ่านการตรวจสอบทางคลินิกและกฎระเบียบอย่างครบถ้วน
<br><br>
<small>ตรวจสอบล่าสุด: 2026-03-03 | ThTxGNN Research Team</small>
</div>
