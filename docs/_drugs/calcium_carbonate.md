---
layout: default
title: Calcium Carbonate
parent: การคาดการณ์จากโมเดล (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Calcium Carbonate
{: .fs-9 }

ระดับหลักฐาน: **L5** | ข้อบ่งใช้ที่ทำนาย: **10** รายการ
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

Using `txgnn-pipeline` skill confirmed — no additional pipeline constraints for report generation. Proceeding to generate the report following Prompt v5 format.

---

# Calcium Carbonate: จากยาลดกรดสู่ Calcium-Alkali Syndrome

## สรุปสั้นๆ

Calcium carbonate เป็นยาลดกรดและอาหารเสริมแคลเซียมที่ใช้มาอย่างยาวนาน แต่ปัจจุบัน**ไม่มีทะเบียนยาในประเทศไทย**
โมเดล TxGNN คาดการณ์ว่าอาจมีความเชื่อมโยงกับ **Calcium-Alkali Syndrome (กลุ่มอาการแคลเซียม-อัลคาไล)** ด้วยคะแนน 93.16% อย่างไรก็ตาม หลักฐานทั้งหมดที่รวบรวมได้ชี้ว่ายานี้**เป็นสาเหตุ**ของโรค ไม่ใช่ยารักษา ซึ่งถือเป็น false positive — ปัจจุบันมี **การทดลองทางคลินิก 1 รายการ** และ **วรรณกรรม 16 ฉบับ** ที่บันทึกความสัมพันธ์นี้ในฐานะปัจจัยก่อโรค

---

## ภาพรวมฉบับย่อ

| รายการ | เนื้อหา |
|---|---|
| ข้อบ่งใช้เดิม | ยาลดกรด / อาหารเสริมแคลเซียม (ไม่มีทะเบียนยาในประเทศไทย) |
| ข้อบ่งใช้ใหม่ที่ทำนาย | Calcium-Alkali Syndrome (กลุ่มอาการแคลเซียม-อัลคาไล) |
| คะแนนการทำนาย TxGNN | 93.16% |
| ระดับหลักฐาน | L5 |
| สถานะการวางจำหน่ายในไทย | ✗ ยังไม่วางจำหน่าย |
| จำนวนใบอนุญาต | 0 รายการ |
| คำแนะนำในการตัดสินใจ | Hold |

---

## ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

> ⚠️ **การคาดการณ์นี้เป็น False Positive** — Calcium carbonate ไม่ได้รักษา Calcium-Alkali Syndrome แต่เป็น**สาเหตุโดยตรง**ของโรคนี้

Calcium carbonate เมื่อรับประทานในปริมาณสูงเกินกว่าที่แนะนำ จะทำให้เกิดวงจรพยาธิสรีรวิทยาต่อเนื่องกัน ดังนี้: แคลเซียมดูดซึมจากลำไส้มากขึ้น → **ภาวะแคลเซียมในเลือดสูง (hypercalcemia)** → ไตดูดน้ำกลับน้อยลงและทิ้งไฮโดรเจนไอออน → **ภาวะด่างจากเมตาบอลิซึม (metabolic alkalosis)** → ไตดูดแคลเซียมกลับมากขึ้นอีก → วงจรอุบาทว์จนเกิด Calcium-Alkali Syndrome ร่วมกับไตวายเฉียบพลัน

คะแนน TxGNN ที่สูงถึง 93.16% เกิดจากโมเดลตรวจพบ**ความสัมพันธ์ทางสถิติในวรรณกรรมจำนวนมาก** ระหว่าง calcium carbonate กับ calcium-alkali syndrome โดยไม่สามารถแยกแยะได้ว่าความสัมพันธ์นั้นคือ "ยาทำให้เกิดโรค" หรือ "ยารักษาโรค" วรรณกรรมทั้ง 16 ฉบับที่รวบรวมล้วนบันทึก calcium carbonate ในฐานะ**ปัจจัยก่อโรค**ทั้งสิ้น

กรณีนี้จึงเป็นตัวอย่างคลาสสิกของ false positive จาก knowledge graph co-occurrence ควรใช้เป็น case study สำหรับการปรับปรุงการกรอง causal vs. therapeutic relationship ในโมเดล TxGNN

---

## หลักฐานจากการทดลองทางคลินิก

| หมายเลขการทดลอง | ระยะ | สถานะ | จำนวนผู้เข้าร่วม | ผลลัพธ์หลัก |
|---|---|---|---|---|
| [NCT01622673](https://clinicaltrials.gov/study/NCT01622673) | Phase 1 | เสร็จสิ้น | 27 | ศึกษาผลของ calcium carbonate antacid ต่อระดับ Raltegravir ในเลือดผู้ป่วย HIV — เป็นการศึกษาปฏิกิริยาระหว่างยา (DDI) ไม่ได้เกี่ยวกับการรักษา calcium-alkali syndrome โดยตรง |

---

## หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|---|---|---|---|---|
| [33732556](https://pubmed.ncbi.nlm.nih.gov/33732556/) | 2021 | Review | Cureus | ทบทวนประวัติ กลไก และการอัปเดต calcium-alkali syndrome ที่เกิดจากการรับประทาน CaCO₃ ปริมาณสูง |
| [26260640](https://pubmed.ncbi.nlm.nih.gov/26260640/) | 2015 | Review | Consultant Pharmacist | แนวทางสำหรับเภสัชกรในการระบุ รักษา และป้องกัน calcium-alkali syndrome ในผู้สูงอายุ |
| [23543983](https://pubmed.ncbi.nlm.nih.gov/23543983/) | 2013 | Review | Baylor Univ Med Ctr Proc | Calcium-alkali syndrome — สาเหตุพบบ่อยอันดับ 3 ของ hypercalcemia ที่เชื่อมโยงกับการใช้ CaCO₃ เป็นอาหารเสริม |
| [33178509](https://pubmed.ncbi.nlm.nih.gov/33178509/) | 2020 | Review | Cureus | Calcium Alkali Thiazide Syndrome — การใช้ CaCO₃ ร่วมกับยาขับปัสสาวะ thiazide เพิ่มความเสี่ยง hypercalcemia อย่างมีนัยสำคัญ |
| [38784190](https://pubmed.ncbi.nlm.nih.gov/38784190/) | 2024 | Case series | Obstetric Medicine | CAS รุนแรงต้องฟอกไตฉุกเฉินในสตรีตั้งครรภ์แฝดที่รับประทาน CaCO₃ รักษาอาการแพ้ท้องตั้งแต่สัปดาห์ที่ 5 |
| [41444901](https://pubmed.ncbi.nlm.nih.gov/41444901/) | 2025 | Case series | Ann General Psychiatry | ผู้ป่วยจิตเวชรับประทาน OTC CaCO₃ (Tums) เกินขนาดจนเกิด milk-alkali syndrome — การเข้าถึงง่ายของยา OTC เป็นความเสี่ยงที่ถูกมองข้าม |
| [33842126](https://pubmed.ncbi.nlm.nih.gov/33842126/) | 2021 | Case series | Cureus | Hypercalcemia รุนแรงจากการรับประทาน CaCO₃ (Tums) ต้องรักษาด้วยการฟอกไตทางเลือด (hemodialysis) |
| [36712775](https://pubmed.ncbi.nlm.nih.gov/36712775/) | 2022 | Case series | Cureus | วิกฤตแคลเซียมสูงเฉียบพลัน (hypercalcemic crisis) จากการใช้ calcium carbonate — ภาวะฉุกเฉินที่คุกคามชีวิต |
| [38404648](https://pubmed.ncbi.nlm.nih.gov/38404648/) | 2024 | Case series | Case Reports in Endocrinology | Severe hypercalcemia จาก CAS ในผู้ป่วย hypoparathyroidism หลังผ่าตัดไทรอยด์ที่รับ CaCO₃ มา 15 ปี ร่วมกับ hyperaldosteronism ที่ไม่ได้รับการวินิจฉัย |
| [32675162](https://pubmed.ncbi.nlm.nih.gov/32675162/) | 2020 | Case series | Clinical Medicine | Hypercalcemia รุนแรง, นิ่วในไต, และไตวายจากการรับประทาน CaCO₃ antacid ปริมาณใกล้เคียงปกติเป็นเวลานาน ร่วมกับยาลดความดัน |

---

## ข้อพิจารณาด้านความปลอดภัย

กรุณาดูข้อมูลความปลอดภัยในเอกสารกำกับยา

---

## สรุปและขั้นตอนถัดไป

**การตัดสินใจ: Hold**

**เหตุผล:**
การคาดการณ์นี้เป็น **false positive ที่ชัดเจน** — calcium carbonate คือสาเหตุของ calcium-alkali syndrome ไม่ใช่ยารักษา ไม่มีหลักฐานทางคลินิกใดๆ ที่สนับสนุนการใช้ยานี้ในการรักษาโรคดังกล่าว และการดำเนินการต่อในแนวทางนี้มีความเสี่ยงอย่างมีนัยสำคัญต่อผู้ป่วย

**หากต้องการดำเนินการต่อต้อง:**
- พัฒนา logic กรอง causal/adverse relationship ออกจาก therapeutic relationship ใน TxGNN pipeline ก่อนเข้า S1
- พิจารณาการคาดการณ์อื่นที่มีกลไกการรักษาสมเหตุสมผลกว่า ได้แก่ **Gastroduodenitis (L3, Research Question)**, **Hyperlipidemia (L2, Research Question)** และ **Peptic Ulcer Disease (L3, Research Question)** ซึ่งล้วนมีกลไกการออกฤทธิ์ทางการรักษาจริงสำหรับ calcium carbonate
- รวบรวมข้อมูลกลไกการออกฤทธิ์ (MOA) จาก DrugBank API เพื่อเสริมการวิเคราะห์ในรอบถัดไป
---

