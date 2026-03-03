---
layout: default
title: "Praziquantel"
description: "รายงานการวิเคราะห์ศักยภาพการใช้ยา Praziquantel ในข้อบ่งใช้ใหม่ - ThTxGNN"
parent: การคาดการณ์จากโมเดล (L5)
nav_order: 1
drug_name: "Praziquantel"
drugbank_id: "DB01058"
evidence_level: "L5"
indication_count: 10
---

# Praziquantel

<p class="fs-5 text-grey-dk-100">
ระดับหลักฐาน: <strong>L5</strong> | ข้อบ่งใช้ที่คาดการณ์: <strong>10</strong> รายการ
</p>

---

## สรุปภาพรวม

| รายการ | รายละเอียด |
|--------|------------|
| **DrugBank ID** | [DB01058](https://go.drugbank.com/drugs/DB01058) |
| **เลขทะเบียนยา** | 1A 112/67 |
| **ข้อบ่งใช้เดิม** | พยาธิใบไม้ตับ |
| **ข้อบ่งใช้ที่คาดการณ์อันดับ 1** | uterine corpus epithelioid leiomyosarcoma |
| **คะแนน TxGNN สูงสุด** | 0.9728 |
| **ระดับหลักฐาน** | L5 |
| **ขึ้นทะเบียนในประเทศไทย** | ✅ จดทะเบียนแล้ว |
| **การตัดสินใจแนะนำ** | รอหลักฐานเพิ่มเติม |

## การคาดการณ์ข้อบ่งใช้ใหม่จาก TxGNN

| อันดับ | ข้อบ่งใช้ที่คาดการณ์ | คะแนน TxGNN |
|:------:|---------------------|:-----------:|
| 1 | uterine corpus epithelioid leiomyosarcoma | 0.9728 |
| 2 | Plasmodium falciparum malaria | 0.9722 |
| 3 | retroperitoneal sarcoma | 0.9716 |
| 4 | uterine corpus myxoid leiomyosarcoma | 0.9716 |
| 5 | anus leiomyosarcoma | 0.9715 |
| 6 | opisthorchiasis | 0.9672 |
| 7 | small intestinal sarcoma | 0.9669 |
| 8 | gnathomiasis | 0.9647 |
| 9 | enterobiasis | 0.9635 |
| 10 | fascioliasis | 0.9626 |


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

- [DrugBank: Praziquantel](https://go.drugbank.com/drugs/DB01058)
- [PubMed: Praziquantel](https://pubmed.ncbi.nlm.nih.gov/?term=Praziquantel)
- [ClinicalTrials.gov](https://clinicaltrials.gov/search?term=Praziquantel)

---

<div class="disclaimer" style="background-color: #fff3cd; padding: 1rem; border-radius: 0.5rem; margin-top: 2rem;">
<strong>⚠️ ข้อจำกัดความรับผิดชอบ</strong><br>
รายงานนี้มีไว้เพื่อการวิจัยทางวิชาการเท่านั้น <strong>ไม่ถือเป็นคำแนะนำทางการแพทย์</strong>
การใช้ยาต้องปฏิบัติตามคำแนะนำของแพทย์ ห้ามปรับเปลี่ยนการใช้ยาด้วยตนเอง
การตัดสินใจใช้ยาเก่าในข้อบ่งใช้ใหม่ต้องผ่านการตรวจสอบทางคลินิกและกฎระเบียบอย่างครบถ้วน
<br><br>
<small>ตรวจสอบล่าสุด: 2026-03-03 | ThTxGNN Research Team</small>
</div>
