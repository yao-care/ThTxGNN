---
layout: default
title: Potassium Chloride
parent: หลักฐานระดับกลาง (L3-L4)
nav_order: 125
evidence_level: L3
indication_count: 10
---

# Potassium Chloride
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

ใช้ทักษะ `txgnn-pipeline` เพื่อตรวจสอบบริบทโครงการแล้ว — กำลังสร้างรายงานประเมินการนำยาเก่ามาใช้ใหม่สำหรับ Potassium Chloride ตาม Evidence Pack v4

---

# Potassium Chloride: จากการเสริมโพแทสเซียมสู่โรคกรดในท่อไตฝอย

## สรุปสั้นๆ

Potassium Chloride (KCl) เป็นสารเสริมอิเล็กโทรไลต์ที่ใช้แก้ไขภาวะโพแทสเซียมในเลือดต่ำ (hypokalemia) ทั้งในรูปแบบรับประทานและให้ทางหลอดเลือดดำ โดยทั่วไปใช้เป็นยาเสริม K⁺ ร่วมกับยาอื่นในหลายภาวะทางคลินิก
โมเดล TxGNN คาดการณ์ว่าอาจมีผลต่อ **โรคกรดในท่อไตฝอย (Renal Tubular Acidosis, RTA)**
ปัจจุบันมี **การทดลองทางคลินิก 9 รายการ** และ **วรรณกรรม 19 ฉบับ** สนับสนุนแนวทางนี้

---

## ภาพรวมฉบับย่อ

| รายการ | เนื้อหา |
|------|------|
| ข้อบ่งใช้เดิม | ยังไม่มีทะเบียนยาในไทย (ใช้เสริมโพแทสเซียมในภาวะโพแทสเซียมต่ำทั่วโลก) |
| ข้อบ่งใช้ใหม่ที่ทำนาย | โรคกรดในท่อไตฝอย (Renal Tubular Acidosis) |
| คะแนนการทำนาย TxGNN | 99.87% |
| ระดับหลักฐาน | L3 |
| สถานะการวางจำหน่ายในไทย | ✗ ยังไม่วางจำหน่าย |
| จำนวนใบอนุญาต | 0 รายการ |
| คำแนะนำในการตัดสินใจ | Proceed with Guardrails |

---

## ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

Potassium Chloride จัดหาไอออน K⁺ โดยตรงให้แก่ร่างกาย กลไกนี้สอดคล้องกับพยาธิสรีรวิทยาของ RTA โดยตรง เนื่องจากท่อไตฝอยที่ทำงานผิดปกติใน Type 1 (distal) และ Type 2 (proximal) RTA ไม่สามารถรักษาสมดุล K⁺ ได้ตามปกติ ส่งผลให้เกิด hypokalemia รุนแรงที่อาจนำไปสู่กล้ามเนื้ออ่อนแรง หัวใจเต้นผิดจังหวะ และในกรณีรุนแรงถึงขั้นระบบหายใจล้มเหลว นอกจากนี้ องค์ประกอบ Cl⁻ ยังช่วยสนับสนุนสมดุล Cl⁻/HCO₃⁻ แลกเปลี่ยนในท่อไตฝอย สนับสนุนกระบวนการรักษาสมดุลกรด-ด่าง

ในทางคลินิก วรรณกรรมระบุชัดเจนว่าการรักษา RTA ประกอบด้วยการให้ด่าง (alkali) ร่วมกับ potassium supplementation โดย KCl เป็นรูปแบบที่นิยมใช้ โดยเฉพาะใน distal RTA ที่มี hypokalemia เด่นชัด กรณีศึกษาหลายรายยืนยันการฟื้นตัวของผู้ป่วย RTA หลังได้รับ potassium supplementation ควบคู่กับ sodium bicarbonate

**ข้อควรระวังสำคัญ:** กลไกข้างต้นใช้ได้เฉพาะ Type 1 และ Type 2 RTA ที่มี hypokalemia เท่านั้น — Type 4 RTA มีลักษณะตรงข้ามคือมี **hyperkalemia** ซึ่ง KCl เป็นข้อห้ามใช้อย่างเด็ดขาด การแยกชนิด RTA ก่อนการรักษาจึงเป็นสิ่งจำเป็น ข้อมูล MOA โดยละเอียดจาก DrugBank ยังไม่ได้รับการรวบรวมในรอบนี้และจำเป็นต้องเสริมก่อนเข้าสู่ขั้นตอนถัดไป

---

## หลักฐานจากการทดลองทางคลินิก

| หมายเลขการทดลอง | ระยะ | สถานะ | จำนวนผู้เข้าร่วม | ผลลัพธ์หลัก |
|---------|------|------|------|---------|
| [NCT03644706](https://clinicaltrials.gov/study/NCT03644706) | Phase 3 | ยุติ | 3 | Phase 3 RCT แบบ withdrawal study เปรียบเทียบ ADV7103 กับ placebo ในการป้องกัน metabolic acidosis จาก serum bicarbonate ในผู้ป่วย distal RTA ทั้งเด็กและผู้ใหญ่ (ยุติก่อนกำหนด สรรหาผู้เข้าร่วมได้เพียง 3 รายจากเป้า) |
| [NCT01843309](https://clinicaltrials.gov/study/NCT01843309) | Phase 4 | ยุติ | 36 | ศึกษา Spironolactone ในการป้องกันความผิดปกติของอิเล็กโทรไลต์ในผู้ป่วยที่ใช้ Amphotericin B — มีความเกี่ยวข้องสูงเนื่องจาก AmB เป็นสาเหตุที่ทราบกันดีของ Type 1 dRTA และบริบทสะท้อนความจำเป็นในการเสริม K⁺ |
| [NCT03354507](https://clinicaltrials.gov/study/NCT03354507) | N/A | ไม่ทราบ | 40 | ผลของ oral sodium bicarbonate ต่อ RTA ในผู้ป่วยเด็กโรคลมชักที่ใช้ Topiramate (ซึ่งยับยั้ง carbonic anhydrase และเหนี่ยวนำ RTA) |
| [NCT00120731](https://clinicaltrials.gov/study/NCT00120731) | N/A | ถอนตัว | 0 | ศึกษาผลของ Potassium Citrate ต่อเคมีในปัสสาวะและสมดุลกรด-ด่างในเด็กที่มี idiopathic hypercalciuria และนิ่วในไต — กลุ่มประชากรและเป้าหมายใกล้เคียงกับการเสริม K⁺ ใน RTA แต่ถอนตัวแล้ว |
| [NCT01894594](https://clinicaltrials.gov/study/NCT01894594) | Phase 1 | ยุติ | 7 | Prospective study ประเมินผลของ alkali therapy ต่อระดับ bicarbonate และ potassium ใน Sickle Cell Disease ที่มี bicarbonate ต่ำ — มีความเชื่อมโยงทางกลไกด้านการปรับสมดุล K⁺ ใต้บริบท metabolic acidosis |
| [NCT06867471](https://clinicaltrials.gov/study/NCT06867471) | N/A | กำลังสรรหา | 43 | RCT crossover ศึกษาผลของ exogenous ketones ต่อ proteinuria และการทำงานของไตในผู้ป่วย CKD และ PKD |
| [NCT06750172](https://clinicaltrials.gov/study/NCT06750172) | N/A | กำลังสรรหา | 33 | ตรวจสอบความสม่ำเสมอของ 24-hour urinary aldosterone ในการวินิจฉัย primary aldosteronism (เชื่อมโยงกับ Type 4 RTA ผ่านกลไก aldosterone-electrolyte) |
| [NCT07273838](https://clinicaltrials.gov/study/NCT07273838) | Phase 2 | กำลังสรรหา | 130 | RCT ศึกษา SGLT2 inhibitor ในผู้ป่วย heart failure ที่มี AKI เพื่อประเมิน composite cardio-renal outcome |
| [NCT01834768](https://clinicaltrials.gov/study/NCT01834768) | Phase 2 | ไม่ทราบ | 31 | ศึกษาความปลอดภัยของ Eplerenone ในผู้รับการปลูกถ่ายไตที่ใช้ Cyclosporine A ซึ่งเป็นยาที่ทราบว่าเหนี่ยวนำ Type 4 RTA |

---

## หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|-----|------|------|---------|
| [38445406](https://pubmed.ncbi.nlm.nih.gov/38445406/) | 2023 | Cohort | La Tunisie Medicale | ความสัมพันธ์ genotype-phenotype ของ distal RTA ในตูนิเซีย — ยืนยัน hypokalemia และ hypercalciuria เป็นลักษณะเด่น สนับสนุนความจำเป็นของ potassium supplementation |
| [783200](https://pubmed.ncbi.nlm.nih.gov/783200/) | 1976 | Cohort | J Clin Investigation | ผู้ป่วย Type 1 RTA 10 ราย ได้รับการแก้ไข acidosis ด้วย potassium bicarbonate — พบความบกพร่องในการอนุรักษ์ Na⁺ และ Cl⁻ ของไต เป็นหลักฐานพื้นฐานในการรักษา RTA ด้วย potassium |
| [33459628](https://pubmed.ncbi.nlm.nih.gov/33459628/) | 2021 | Review | Arch Esp Urol | RTA และนิ่วในไต: การวินิจฉัยและการจัดการอย่างครอบคลุม รวมบทบาทของ alkali และ potassium supplementation ใน distal RTA |
| [21314872](https://pubmed.ncbi.nlm.nih.gov/21314872/) | 2011 | Review | Int J Clin Practice | แนวทางทางคลินิกในการวินิจฉัยและรักษา RTA ในผู้ใหญ่ ครอบคลุม Type I, II และ IV พร้อมแนวทางการให้ potassium |
| [8694660](https://pubmed.ncbi.nlm.nih.gov/8694660/) | 1996 | Review | Arch Intern Med | พยาธิสรีรวิทยาและการวินิจฉัย RTA — ยืนยันความสำคัญของระดับ K⁺ ในซีรัมและปัสสาวะเป็นตัวชี้วัดหลักในการจำแนกชนิด |
| [34748193](https://pubmed.ncbi.nlm.nih.gov/34748193/) | 2022 | Case series | J Nephrology | Distal RTA ร่วมกับ hypokalemic periodic paralysis ระหว่างตั้งครรภ์ — สนับสนุนความสำคัญของ potassium supplementation ในกลุ่มเสี่ยง |
| [20228475](https://pubmed.ncbi.nlm.nih.gov/20228475/) | 2010 | Case series | Neurology India | RTA ที่แสดงอาการ respiratory paralysis — ผู้ป่วยฟื้นตัวหลังได้รับ sodium bicarbonate ร่วมกับ potassium supplementation |
| [17297212](https://pubmed.ncbi.nlm.nih.gov/17297212/) | 2007 | Review | Acta Med Indonesiana | แนวทางในการดูแลภาวะ hypokalemia รวมถึงสาเหตุจาก renal tubular loss ที่พบบ่อยใน RTA |
| [37081692](https://pubmed.ncbi.nlm.nih.gov/37081692/) | 2023 | Review | Endocrine J | การจำแนก pseudohypoaldosteronism type II เป็น type IV RTA — ทบทวนความแตกต่างของ hyperkalemic RTA ซึ่งมีนัยสำคัญต่อการใช้ KCl |
| [3518609](https://pubmed.ncbi.nlm.nih.gov/3518609/) | 1986 | Review | Annu Rev Med | Clinical spectrum of RTA — นิยามกลุ่มย่อย 3 แบบ: proximal, hypokalemic distal, และ hyperkalemic distal RTA พร้อมแนวทางรักษา |

---

## ข้อพิจารณาด้านความปลอดภัย

กรุณาดูข้อมูลความปลอดภัยในเอกสารกำกับยา

> **หมายเหตุจากผู้วิเคราะห์:** ข้อมูลคำเตือนและข้อห้ามใช้จาก TFDA ยังไม่ได้รับการรวบรวม (DG001) — การดำเนินการต่อเนื่องต้องพิจารณาความเสี่ยง hyperkalemia และ cardiac toxicity จากการให้ KCl เกินขนาดอย่างรอบคอบ โดยเฉพาะในผู้ป่วยที่มีการทำงานของไตบกพร่อง

---

## สรุปและขั้นตอนถัดไป

**การตัดสินใจ: Proceed with Guardrails**

**เหตุผล:**
มีวรรณกรรมทางคลินิกที่สนับสนุนการใช้ potassium supplementation ในบริบทของ RTA หลายฉบับ และกลไกการออกฤทธิ์มีความสมเหตุสมผลในเชิงพยาธิสรีรวิทยาสำหรับ Type 1 และ Type 2 RTA อย่างไรก็ตามยังขาดการทดลองทางคลินิกที่ประเมิน KCl โดยตรงสำหรับ RTA และมีความเสี่ยงสำคัญในชนิด Type 4 ที่ต้องระวังเป็นพิเศษ

**หากต้องการดำเนินการต่อต้อง:**
- รวบรวมข้อมูล MOA โดยละเอียดจาก DrugBank API (แก้ไข DG002)
- ดาวน์โหลดและวิเคราะห์ข้อมูลคำเตือนและข้อห้ามใช้จาก TFDA/EMA/FDA (แก้ไข DG001) โดยเฉพาะข้อมูล hyperkalemia และ cardiac toxicity
- กำหนดขอบเขตชนิด RTA ที่เหมาะสม — เน้น Type 1 (distal) ที่มี hypokalemia เป็นหลัก ยกเว้น Type 4 อย่างเด็ดขาด
- ออกแบบ prospective cohort หรือ pragmatic clinical trial ที่ประเมิน KCl ในประชากร RTA Type 1/2 โดยตรง พร้อม endpoint ด้านการแก้ไข hypokalemia และ metabolic acidosis
- พิจารณาขึ้นทะเบียนยาในประเทศไทยก่อนการศึกษาทางคลินิก เนื่องจากปัจจุบันยังมีสถานะ "ยังไม่วางจำหน่าย"
---

