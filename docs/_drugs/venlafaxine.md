---
layout: default
title: "Venlafaxine"
description: "รายงานการวิเคราะห์ศักยภาพการใช้ยา Venlafaxine ในข้อบ่งใช้ใหม่ - ThTxGNN"
parent: การคาดการณ์จากโมเดล (L5)
nav_order: 1
drug_name: "Venlafaxine"
drugbank_id: "DB00285"
evidence_level: "L5"
indication_count: 10
---

# Venlafaxine

<p class="fs-5 text-grey-dk-100">
ระดับหลักฐาน: <strong>L5</strong> | ข้อบ่งใช้ที่คาดการณ์: <strong>10</strong> รายการ
</p>

---

## สรุปภาพรวม

| รายการ | รายละเอียด |
|--------|------------|
| **DrugBank ID** | [DB00285](https://go.drugbank.com/drugs/DB00285) |
| **เลขทะเบียนยา** | 1A 148/67 |
| **ข้อบ่งใช้เดิม** | ซึมเศร้า, วิตกกังวล |
| **ข้อบ่งใช้ที่คาดการณ์อันดับ 1** | endogenous depression |
| **คะแนน TxGNN สูงสุด** | 0.9897 |
| **ระดับหลักฐาน** | L5 |
| **ขึ้นทะเบียนในประเทศไทย** | ✅ จดทะเบียนแล้ว |
| **การตัดสินใจแนะนำ** | รอหลักฐานเพิ่มเติม |

## การคาดการณ์ข้อบ่งใช้ใหม่จาก TxGNN

| อันดับ | ข้อบ่งใช้ที่คาดการณ์ | คะแนน TxGNN |
|:------:|---------------------|:-----------:|
| 1 | endogenous depression | 0.9897 |
| 2 | major depressive disorder | 0.9883 |
| 3 | Ohdo syndrome and variants | 0.9586 |
| 4 | unipolar depression | 0.9555 |
| 5 | ligneous conjunctivitis | 0.9399 |
| 6 | blepharophimosis - intellectual disability syndrome, Ohdo type | 0.9379 |
| 7 | anxiety disorder | 0.9210 |
| 8 | phobic disorder | 0.9094 |
| 9 | benign paroxysmal torticollis of infancy | 0.8973 |
| 10 | dysthymic disorder | 0.8914 |


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

- [DrugBank: Venlafaxine](https://go.drugbank.com/drugs/DB00285)
- [PubMed: Venlafaxine](https://pubmed.ncbi.nlm.nih.gov/?term=Venlafaxine)
- [ClinicalTrials.gov](https://clinicaltrials.gov/search?term=Venlafaxine)

---

<div class="disclaimer" style="background-color: #fff3cd; padding: 1rem; border-radius: 0.5rem; margin-top: 2rem;">
<strong>⚠️ ข้อจำกัดความรับผิดชอบ</strong><br>
รายงานนี้มีไว้เพื่อการวิจัยทางวิชาการเท่านั้น <strong>ไม่ถือเป็นคำแนะนำทางการแพทย์</strong>
การใช้ยาต้องปฏิบัติตามคำแนะนำของแพทย์ ห้ามปรับเปลี่ยนการใช้ยาด้วยตนเอง
การตัดสินใจใช้ยาเก่าในข้อบ่งใช้ใหม่ต้องผ่านการตรวจสอบทางคลินิกและกฎระเบียบอย่างครบถ้วน
<br><br>
<small>ตรวจสอบล่าสุด: 2026-03-03 | ThTxGNN Research Team</small>
</div>
