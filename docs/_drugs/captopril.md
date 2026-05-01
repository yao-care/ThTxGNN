---
layout: default
title: Captopril
parent: หลักฐานระดับกลาง (L3-L4)
nav_order: 34
evidence_level: L3
indication_count: 10
---

# Captopril
{: .fs-9 }

ระดับหลักฐาน: **L3** | ข้อบ่งใช้ที่ทำนาย: **10** รายการ
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

Using `txgnn-pipeline` skill confirmed — this is a ThTxGNN report generation task. Proceeding with the full Evidence Pack analysis for Captopril.

---

# Captopril: จากความดันโลหิตสูงสู่ความดันโลหิตสูงจากหลอดเลือดไตชนิดร้ายแรง

## สรุปสั้นๆ

Captopril เป็นยายับยั้ง Angiotensin-Converting Enzyme (ACE Inhibitor) ซึ่งเดิมใช้รักษาความดันโลหิตสูงและภาวะหัวใจล้มเหลว โดยกลไกหลักคือการยับยั้งการแปลง Angiotensin I เป็น Angiotensin II ลดภาระต่อหัวใจและหลอดเลือด
โมเดล TxGNN คาดการณ์ว่าอาจมีผลต่อ **ความดันโลหิตสูงจากหลอดเลือดไตชนิดร้ายแรง (Malignant Renovascular Hypertension)**
ปัจจุบันมี **วรรณกรรม 20 ฉบับ** สนับสนุนแนวทางนี้ แต่ยังไม่มีการทดลองทางคลินิกที่ลงทะเบียนโดยตรงสำหรับข้อบ่งใช้นี้

---

## ภาพรวมฉบับย่อ

| รายการ | เนื้อหา |
|---|---|
| ข้อบ่งใช้เดิม | ไม่มีทะเบียนยาใน Thai FDA |
| ข้อบ่งใช้ใหม่ที่ทำนาย | Malignant Renovascular Hypertension (ความดันโลหิตสูงจากหลอดเลือดไตชนิดร้ายแรง) |
| คะแนนการทำนาย TxGNN | 99.28% |
| ระดับหลักฐาน | L3 |
| สถานะการวางจำหน่ายในไทย | ✗ ยังไม่ได้จดทะเบียนในประเทศไทย |
| จำนวนใบอนุญาต | 0 |
| คำแนะนำในการตัดสินใจ | Proceed with Guardrails |

---

## ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

Captopril เป็น ACE Inhibitor ที่ยับยั้งเอนไซม์ Angiotensin-Converting Enzyme โดยตรง ส่งผลให้ระดับ Angiotensin II ซึ่งเป็นสารหดหลอดเลือดและกระตุ้นการหลั่ง Aldosterone ลดลงอย่างมีนัยสำคัญ กลไกนี้ทำให้ความดันโลหิตลดลงและลดภาระต่อทั้งหัวใจและไต

ใน Malignant Renovascular Hypertension ระบบ Renin-Angiotensin System (RAS) ถูกกระตุ้นอย่างรุนแรงจากภาวะเลือดไปเลี้ยงไตไม่เพียงพอ (renal ischemia) ทำให้ renin หลั่งมากผิดปกติ Captopril ซึ่งตัดวงจรนี้ที่จุด ACE จึงมีกลไกที่สอดรับกับพยาธิสรีรวิทยาของโรคนี้โดยตรง ยิ่งกว่านั้น **Captopril Renogram** (การทดสอบสมรรถภาพไตด้วย Captopril) ได้รับการยอมรับว่าเป็นเครื่องมือวินิจฉัย Renovascular Hypertension มาตรฐาน ซึ่งยืนยันว่ากลไกของ Captopril สัมพันธ์กับโรคนี้ในระดับกายภาพอย่างชัดเจน

อย่างไรก็ตาม มีข้อควรระวังสำคัญ: ผู้ป่วยที่มีการตีบของหลอดเลือดแดงไตทั้งสองข้าง (bilateral renal artery stenosis) **ห้ามใช้** ACE Inhibitor เนื่องจากอาจทำให้ไตวายเฉียบพลัน การประเมินกายวิภาคของหลอดเลือดไตก่อนเริ่มยาจึงเป็นสิ่งจำเป็น

---

## หลักฐานจากการทดลองทางคลินิก

ปัจจุบันยังไม่มีการลงทะเบียนการทดลองทางคลินิกที่เกี่ยวข้องกับการใช้ Captopril ใน Malignant Renovascular Hypertension โดยตรง

---

## หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|---|---|---|---|---|
| [6145432](https://pubmed.ncbi.nlm.nih.gov/6145432/) | 1984 | Cohort | Biull Vsesoiuz Kardiol Nauch Tsentra | การใช้ Captopril ในความดันโลหิตสูงแบบคงที่และแบบร้ายแรง (malignant course) |
| [232024](https://pubmed.ncbi.nlm.nih.gov/232024/) | 1979 | Observational | Clin Sci | Captopril เพิ่ม PRA >14 ng/h/ml ใน 43/44 ราย ของ untreated renovascular hypertension; ช่วยแยกออกจาก high-renin essential hypertension ได้อย่างมีนัยสำคัญ |
| [8070421](https://pubmed.ncbi.nlm.nih.gov/8070421/) | 1994 | Review | Endocrinol Metab Clin N Am | เนื้องอกหลั่ง renin (JGC tumor): ความดันโลหิตลดลงเมื่อรักษาด้วย converting enzyme inhibitor; Captopril acute test ใช้เพื่อยืนยันการพึ่งพา RAS |
| [17008836](https://pubmed.ncbi.nlm.nih.gov/17008836/) | 2006 | Review | Minerva Medica | ทบทวนแนวคิดทางคลินิกของ Renovascular Hypertension; แนวทางรักษาควรมุ่งเป้าที่ renal ischemia พร้อมพิจารณา RAS-directed therapy |
| [2040938](https://pubmed.ncbi.nlm.nih.gov/2040938/) | 1991 | Review | J Pediatrics | ทบทวน Malignant Hypertension ในเด็ก ครอบคลุมพยาธิสรีรวิทยาและแนวทางการรักษา |
| [10955932](https://pubmed.ncbi.nlm.nih.gov/10955932/) | 2000 | Case series | Pediatr Nephrol | NF1 ในเด็ก 27 ราย (อายุ 4.2–24 ปี): ประเมินด้วย captopril test, Doppler ultrasonography และ angiography พบ renal artery stenosis และ secondary hypertension |
| [11334320](https://pubmed.ncbi.nlm.nih.gov/11334320/) | 2001 | Case series | Clin Nephrol | 2 กรณี Renovascular Hypertension กับ Neurofibromatosis; Captopril 50 mg เพิ่ม PRA จาก 2.8 เป็น 12.6 ng/ml/h ยืนยัน renin-dependent mechanism |
| [3928961](https://pubmed.ncbi.nlm.nih.gov/3928961/) | 1985 | Case series | Klin Wochenschr | Neurofibromatosis กับ bilateral renal artery stenosis + coarctation of aorta; รักษาด้วย Captopril ควบคุมความดันโลหิตได้เมื่อผู้ป่วยปฏิเสธการผ่าตัด |
| [1572120](https://pubmed.ncbi.nlm.nih.gov/1572120/) | 1992 | Case series | Clin Nucl Med | Malignant hypertension ที่ captopril renal scintigraphy ให้ผล false positive bilateral; angiogram ยืนยันไม่มี renal artery stenosis — เน้นข้อจำกัดของ test |
| [2887673](https://pubmed.ncbi.nlm.nih.gov/2887673/) | 1987 | Animal | Jpn Heart J | ศึกษา neurohormonal changes ใน 2K2C Goldblatt hypertensive dogs ระยะ benign และ malignant; ติดตาม PRA, Angiotensin I/II, Aldosterone และ Vasopressin |

---

## ข้อมูลการวางจำหน่ายในประเทศไทย

Captopril **ยังไม่มีทะเบียนยาในประเทศไทย** (Thai FDA) ณ วันที่ตัดข้อมูล 25 เมษายน 2569 — ไม่มีใบอนุญาตที่ใช้งานอยู่

---

## ข้อพิจารณาด้านความปลอดภัย

กรุณาดูข้อมูลความปลอดภัยในเอกสารกำกับยา

---

## สรุปและขั้นตอนถัดไป

**การตัดสินใจ: Proceed with Guardrails**

**เหตุผล:**
กลไกการออกฤทธิ์ของ Captopril ในฐานะ ACE Inhibitor สอดคล้องโดยตรงกับพยาธิสรีรวิทยาของ Malignant Renovascular Hypertension ซึ่งเป็นโรคที่ขับเคลื่อนโดย RAS มากเกิน มีวรรณกรรมระดับ Cohort และ Case series สนับสนุน รวมถึงการใช้ Captopril Test เป็น diagnostic standard ที่ยอมรับในวงกว้าง อย่างไรก็ตาม ยังไม่มีการทดลองทางคลินิกแบบ RCT ที่เฉพาะเจาะจง และ Captopril ยังไม่ได้จดทะเบียนใน Thai FDA

**หากต้องการดำเนินการต่อต้อง:**
- ดาวน์โหลด SmPC / FDA Label (ต่างประเทศ) เพื่อระบุข้อมูล MOA อย่างเป็นทางการ คำเตือนหลัก และข้อห้ามใช้ที่ครบถ้วน
- ตรวจสอบสถานะ bilateral renal artery stenosis ของผู้ป่วยก่อนเริ่มยาทุกราย
- วางแผนติดตาม serum creatinine, potassium และ blood pressure ภายใน 1–2 สัปดาห์หลังเริ่มยา
- ยื่นขอขึ้นทะเบียนยาใน Thai FDA หรือพิจารณาการนำเข้าในกรณีใช้ฉุกเฉิน
- พิจารณาออกแบบ Pilot Study หรือ Retrospective Cohort เพื่อยืนยันประสิทธิผลในบริบทประชากรไทย

---

> ⚠️ **ข้อความปฏิเสธความรับผิดชอบ**: รายงานนี้จัดทำขึ้นเพื่อการวิจัยเท่านั้น ไม่ถือเป็นคำแนะนำทางการแพทย์ ผลการทำนายจาก TxGNN จำเป็นต้องได้รับการตรวจสอบทางคลินิกก่อนนำไปใช้จริง
---

