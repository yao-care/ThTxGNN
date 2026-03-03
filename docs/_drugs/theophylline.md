---
layout: default
title: "Theophylline"
description: "รายงานการวิเคราะห์ศักยภาพการใช้ยา Theophylline ในข้อบ่งใช้ใหม่ - ThTxGNN"
parent: หลักฐานอ่อน (L4)
nav_order: 1
drug_name: "Theophylline"
drugbank_id: "DB00277"
evidence_level: "L4"
indication_count: 10
---

# Theophylline

<p class="fs-5 text-grey-dk-100">
ระดับหลักฐาน: <strong>L4</strong> | ข้อบ่งใช้ที่คาดการณ์: <strong>10</strong> รายการ
</p>

---

## สรุปภาพรวม

| รายการ | รายละเอียด |
|--------|------------|
| **DrugBank ID** | [DB00277](https://go.drugbank.com/drugs/DB00277) |
| **เลขทะเบียนยา** | 1A 65/67 |
| **ข้อบ่งใช้เดิม** | โรคหอบหืด |
| **ข้อบ่งใช้ที่คาดการณ์อันดับ 1** | bronchitis |
| **คะแนน TxGNN สูงสุด** | 0.9996 |
| **ระดับหลักฐาน** | L4 |
| **ขึ้นทะเบียนในประเทศไทย** | ✅ จดทะเบียนแล้ว |
| **การตัดสินใจแนะนำ** | รอหลักฐานเพิ่มเติม |

## การคาดการณ์ข้อบ่งใช้ใหม่จาก TxGNN

| อันดับ | ข้อบ่งใช้ที่คาดการณ์ | คะแนน TxGNN |
|:------:|---------------------|:-----------:|
| 1 | bronchitis | 0.9996 |
| 2 | thrombotic disease | 0.9962 |
| 3 | nasal cavity disease | 0.9953 |
| 4 | laryngotracheitis | 0.9951 |
| 5 | tracheal disease | 0.9949 |
| 6 | obstructive lung disease | 0.9948 |
| 7 | pharyngitis | 0.9946 |
| 8 | acute laryngopharyngitis | 0.9935 |
| 9 | bronchial neoplasm (disease) | 0.9889 |
| 10 | respiratory malformation | 0.9887 |


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
การคาดการณ์นี้อยู่ในระดับหลักฐาน L4 ซึ่งต้องการการวิจัยเพิ่มเติมเพื่อยืนยันประสิทธิภาพ

**สิ่งที่ต้องการเพื่อดำเนินการต่อ:**
- การศึกษากลไกการออกฤทธิ์ของยา (Mechanism of Action)
- การทดลองทางคลินิกเบื้องต้น (Phase I/II Clinical Trial)
- การศึกษาปฏิกิริยาระหว่างยา (Drug Interactions)

---

## แหล่งข้อมูล

- [DrugBank: Theophylline](https://go.drugbank.com/drugs/DB00277)
- [PubMed: Theophylline](https://pubmed.ncbi.nlm.nih.gov/?term=Theophylline)
- [ClinicalTrials.gov](https://clinicaltrials.gov/search?term=Theophylline)

---

<div class="disclaimer" style="background-color: #fff3cd; padding: 1rem; border-radius: 0.5rem; margin-top: 2rem;">
<strong>⚠️ ข้อจำกัดความรับผิดชอบ</strong><br>
รายงานนี้มีไว้เพื่อการวิจัยทางวิชาการเท่านั้น <strong>ไม่ถือเป็นคำแนะนำทางการแพทย์</strong>
การใช้ยาต้องปฏิบัติตามคำแนะนำของแพทย์ ห้ามปรับเปลี่ยนการใช้ยาด้วยตนเอง
การตัดสินใจใช้ยาเก่าในข้อบ่งใช้ใหม่ต้องผ่านการตรวจสอบทางคลินิกและกฎระเบียบอย่างครบถ้วน
<br><br>
<small>ตรวจสอบล่าสุด: 2026-03-03 | ThTxGNN Research Team</small>
</div>
