---
layout: default
title: Theophylline
parent: การคาดการณ์จากโมเดล (L5)
nav_order: 151
evidence_level: L5
indication_count: 7
---

# Theophylline
{: .fs-9 }

ระดับหลักฐาน: **L5** | ข้อบ่งใช้ที่ทำนาย: **7** รายการ
{: .fs-6 .fw-300 }

---

## สารบัญ
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## รายงานการประเมินของเภสัชกร

</div>

Using `txgnn-pipeline` skill to confirm context — then proceeding to generate the multi-indication report per the v5 Prompt format.

---

# Theophylline: จากโรคหอบหืดและ COPD สู่โรคหลอดเลือดอุดตัน

## สรุปสั้นๆ

Theophylline เป็นยาขยายหลอดลมกลุ่ม methylxanthine ที่ใช้รักษาโรคหอบหืดและโรคปอดอุดกั้นเรื้อรัง (COPD) มาเป็นเวลากว่า 80 ปี แม้ว่าปัจจุบันยังไม่มีการจดทะเบียนในประเทศไทย
โมเดล TxGNN คาดการณ์ว่าอาจมีศักยภาพต่อ **โรคหลอดเลือดอุดตัน (Thrombotic Disease)** โดยอาศัยกลไกยับยั้ง PDE ที่เพิ่มระดับ cAMP ในเกล็ดเลือดและลดการรวมตัวของเกล็ดเลือด
อย่างไรก็ตาม ปัจจุบัน**ไม่มีการทดลองทางคลินิก**ที่เกี่ยวข้อง มีเพียง **วรรณกรรม 19 ฉบับ** ซึ่งเป็นงานวิจัยพื้นฐานและการสังเกตการณ์ ไม่มีชิ้นใดทดสอบ Theophylline โดยตรงในข้อบ่งใช้นี้

---

## ภาพรวมฉบับย่อ

| รายการ | เนื้อหา |
|---|---|
| ข้อบ่งใช้เดิม | โรคหอบหืดและ COPD |
| ข้อบ่งใช้ใหม่ที่ทำนาย | โรคหลอดเลือดอุดตัน (Thrombotic Disease) |
| คะแนนการทำนาย TxGNN | 99.62% |
| ระดับหลักฐาน | L5 |
| สถานะการวางจำหน่ายในไทย | ✗ ไม่ได้วางจำหน่าย |
| จำนวนใบอนุญาต | 0 รายการ |
| คำแนะนำในการตัดสินใจ | Hold |

---

## ผลการทำนายทั้งหมด (Multi-Indication Summary)

รายงานฉบับนี้เป็นการประเมินแบบ multi-indication (TW-DB00277-multi) ครอบคลุมข้อบ่งใช้ที่ทำนาย 7 รายการ โดยแต่ละรายการมีระดับหลักฐานแตกต่างกัน:

| อันดับ | ข้อบ่งใช้ | คะแนน TxGNN | ระดับหลักฐาน | คำแนะนำ |
|---|---|---|---|---|
| 1 | Thrombotic Disease | 99.62% | L5 | Hold |
| 2 | Nasal Cavity Disease | 99.53% | L2 | Proceed with Guardrails |
| 3 | Laryngotracheitis | 99.51% | L5 | Hold |
| 4 | Tracheal Disease | 99.49% | L4 | Research Question |
| 5 | Obstructive Lung Disease | 99.48% | L1 | Proceed with Guardrails |
| 6 | Pharyngitis | 99.46% | L5 | Hold |
| 7 | Acute Laryngopharyngitis | 99.35% | L5 | Hold |

> หมายเหตุ: คะแนน TxGNN สูงทั้ง 7 รายการ (>99%) สะท้อนความน่าจะเป็นของโมเดล ไม่ได้บ่งบอกระดับหลักฐานทางคลินิก ข้อบ่งใช้ที่มีหลักฐานแข็งแกร่งที่สุดคือ **Obstructive Lung Disease (L1)** และ **Nasal Cavity Disease (L2)**

---

## ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

ปัจจุบันยังขาดข้อมูลกลไกการออกฤทธิ์โดยละเอียดจากฐานข้อมูล DrugBank ตามข้อมูลที่ทราบกันดี Theophylline เป็นยา methylxanthine ที่ยับยั้งเอนไซม์ phosphodiesterase (PDE) แบบไม่เลือกชนิด และต้านตัวรับ adenosine ซึ่งเป็นกลไกหลักในการขยายหลอดลมและลดการอักเสบของทางเดินหายใจ

กลไกการยับยั้ง PDE เดียวกันนี้ทำงานในเกล็ดเลือดด้วย การยับยั้ง PDE3 ในเกล็ดเลือดทำให้ระดับ cyclic AMP (cAMP) สูงขึ้น ส่งผลให้เกล็ดเลือดตอบสนองต่อตัวกระตุ้น (เช่น ADP, collagen) ลดลง ซึ่งในทางทฤษฎีอาจยับยั้งการก่อตัวของลิ่มเลือดในหลอดเลือดแดงได้ กลไกนี้ได้รับการพิสูจน์ในยากลุ่มเดียวกัน เช่น milrinone (PDE3 inhibitor) ซึ่งยับยั้ง platelet aggregation ในระดับ ex vivo

อย่างไรก็ตาม ความเชื่อมโยงนี้ยังคงเป็นทฤษฎี วรรณกรรม 19 ฉบับที่ค้นพบส่วนใหญ่เป็นการศึกษาชีววิทยาเกล็ดเลือดในบริบทอื่น ไม่มีงานชิ้นใดที่ทดสอบ Theophylline โดยตรงในฐานะยารักษาโรคหลอดเลือดอุดตัน ที่น่าสังเกตคือ PMID 749930 กล่าวถึง Theophylline ในฐานะส่วนผสมของสารป้องกันเลือดแข็ง (ร่วมกับ EDTA และ PGE1) เพื่อลดการกระตุ้นเกล็ดเลือด in vitro ระหว่างการเตรียมตัวอย่างพลาสมา ซึ่งสะท้อนฤทธิ์ยับยั้งเกล็ดเลือดที่มีอยู่จริง แต่เป็นบทบาทที่แตกต่างจากการรักษาทางคลินิก

---

## หลักฐานจากการทดลองทางคลินิก

ปัจจุบันยังไม่มีการลงทะเบียนการทดลองทางคลินิกที่เกี่ยวข้อง

---

## หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|---|---|---|---|---|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clin Pharmacokinet | ticlopidine มีฤทธิ์ต้านเกล็ดเลือดกว้างขวาง ใช้ป้องกัน arterial thrombosis; บริบทกลไกยาต้านเกล็ดเลือดในทางคลินิก |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Crit Rev Biochem | thromboxane A2 กระตุ้น platelet aggregation; prostacyclin ยับยั้งผ่านการเพิ่ม cAMP — กลไกเดียวกับ Theophylline (PDE inhibition) |
| [197665](https://pubmed.ncbi.nlm.nih.gov/197665/) | 1977 | Review | Stroke | การรักษา cerebral edema ใน stroke; กล่าวถึง aminophylline (prodrug ของ theophylline) เป็นหนึ่งในแนวทางรักษา |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Cohort | Br J Haematol | พัฒนา RIA วัด platelet factor 4; ต้องใช้ **theophylline** ร่วมกับ EDTA และ PGE1 เพื่อป้องกันการกระตุ้นเกล็ดเลือด in vitro |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | Cohort | Rheumatology | การกระตุ้นเกล็ดเลือดและนิวโทรฟิลใน Behçet's disease สัมพันธ์กับอายุ เพศ และความรุนแรงของโรคที่มีภาวะหลอดเลือดอักเสบ |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | Cohort | Platelets | soluble CLEC-2 (sCLEC-2) เป็น biomarker บ่งชี้การกระตุ้นเกล็ดเลือด in vivo สำหรับผู้ป่วยเสี่ยงโรคหลอดเลือดอุดตัน |
| [32824700](https://pubmed.ncbi.nlm.nih.gov/32824700/) | 2020 | Cohort | Cells | การเตรียมตัวอย่างเลือดที่ไม่เหมาะสมกระตุ้นเกล็ดเลือดและส่งผลต่อ microRNA biomarker ของโรคหัวใจและหลอดเลือด |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | Case-control | Inflamm Bowel Dis | platelet-leukocyte aggregates (PLAs) เพิ่มขึ้นในภาวะ IBD และโรคลิ่มเลือด สัมพันธ์กับการกระตุ้นเกล็ดเลือดและนิวโทรฟิล |
| [6241135](https://pubmed.ncbi.nlm.nih.gov/6241135/) | 1984 | Cohort | Cor et Vasa | **theophylline-resistant** T-helper cells เพิ่มขึ้นอย่างมีนัยสำคัญในผู้ป่วย myocardial infarction และ thrombophlebitis |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | In vitro | Gen Pharmacol | milrinone (PDE3 inhibitor) ยับยั้ง platelet aggregation โดยเพิ่ม cAMP — กลไกเดียวกับ Theophylline ในฐานะ PDE inhibitor |

---

## ข้อพิจารณาด้านความปลอดภัย

กรุณาดูข้อมูลความปลอดภัยในเอกสารกำกับยา

---

## สรุปและขั้นตอนถัดไป

**การตัดสินใจ: Hold**

**เหตุผล:**
ไม่มีการทดลองทางคลินิกหรือหลักฐานเชิงแทรกแซงใดๆ ที่ศึกษา Theophylline โดยตรงในการรักษาโรคหลอดเลือดอุดตัน การทำนายนี้อยู่บนพื้นฐานกลไกทางทฤษฎีเท่านั้น ยังไม่มีข้อมูลเพียงพอที่จะประเมินความเป็นไปได้ทางคลินิก

**หากต้องการดำเนินการต่อต้อง:**
- ดำเนินการศึกษาก่อนคลินิก (in vitro / in vivo) เพื่อยืนยันฤทธิ์ยับยั้งเกล็ดเลือดของ Theophylline ในโมเดล thrombosis โดยตรง
- ขอข้อมูล MOA และ toxicity profile ฉบับสมบูรณ์จากฐานข้อมูล DrugBank
- ดาวน์โหลดและวิเคราะห์ฉลากยาจาก Thai FDA เพื่อประเมินความปลอดภัยเบื้องต้น (แก้ไข DG001)
- **พิจารณาข้อบ่งใช้ที่มีหลักฐานแข็งแกร่งกว่าใน Multi-Indication Pack นี้ก่อน ได้แก่ Obstructive Lung Disease (L1, Proceed with Guardrails) และ Nasal Cavity Disease (L2, Proceed with Guardrails)**
---

