---
layout: default
title: "Warfarin"
description: "รายงานการวิเคราะห์ศักยภาพการใช้ยา Warfarin ในข้อบ่งใช้ใหม่ - ThTxGNN"
parent: หลักฐานอ่อน (L4)
nav_order: 1
drug_name: "Warfarin"
drugbank_id: "DB00682"
evidence_level: "L4"
indication_count: 10
---

# Warfarin

<p class="fs-5 text-grey-dk-100">
ระดับหลักฐาน: <strong>L4</strong> | ข้อบ่งใช้ที่คาดการณ์: <strong>10</strong> รายการ
</p>

---

## สรุปภาพรวม

| รายการ | รายละเอียด |
|--------|------------|
| **DrugBank ID** | [DB00682](https://go.drugbank.com/drugs/DB00682) |
| **เลขทะเบียนยา** | 1A 24/67 |
| **ข้อบ่งใช้เดิม** | ป้องกันลิ่มเลือด |
| **ข้อบ่งใช้ที่คาดการณ์อันดับ 1** | heparin cofactor 2 deficiency |
| **คะแนน TxGNN สูงสุด** | 0.9987 |
| **ระดับหลักฐาน** | L4 |
| **ขึ้นทะเบียนในประเทศไทย** | ✅ จดทะเบียนแล้ว |
| **การตัดสินใจแนะนำ** | รอหลักฐานเพิ่มเติม |

## การคาดการณ์ข้อบ่งใช้ใหม่จาก TxGNN

| อันดับ | ข้อบ่งใช้ที่คาดการณ์ | คะแนน TxGNN |
|:------:|---------------------|:-----------:|
| 1 | heparin cofactor 2 deficiency | 0.9987 |
| 2 | factor 5 excess with spontaneous thrombosis | 0.9984 |
| 3 | antithrombin deficiency type 2 | 0.9984 |
| 4 | thrombophilia | 0.9975 |
| 5 | thrombotic disease | 0.9958 |
| 6 | rheumatoid arthritis | 0.9921 |
| 7 | breast fibrocystic disease | 0.9920 |
| 8 | benign mammary dysplasia | 0.9910 |
| 9 | blunt duct adenosis of breast | 0.9873 |
| 10 | apocrine adenosis of breast | 0.9873 |


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

- [DrugBank: Warfarin](https://go.drugbank.com/drugs/DB00682)
- [PubMed: Warfarin](https://pubmed.ncbi.nlm.nih.gov/?term=Warfarin)
- [ClinicalTrials.gov](https://clinicaltrials.gov/search?term=Warfarin)

---

<div class="disclaimer" style="background-color: #fff3cd; padding: 1rem; border-radius: 0.5rem; margin-top: 2rem;">
<strong>⚠️ ข้อจำกัดความรับผิดชอบ</strong><br>
รายงานนี้มีไว้เพื่อการวิจัยทางวิชาการเท่านั้น <strong>ไม่ถือเป็นคำแนะนำทางการแพทย์</strong>
การใช้ยาต้องปฏิบัติตามคำแนะนำของแพทย์ ห้ามปรับเปลี่ยนการใช้ยาด้วยตนเอง
การตัดสินใจใช้ยาเก่าในข้อบ่งใช้ใหม่ต้องผ่านการตรวจสอบทางคลินิกและกฎระเบียบอย่างครบถ้วน
<br><br>
<small>ตรวจสอบล่าสุด: 2026-03-03 | ThTxGNN Research Team</small>
</div>
