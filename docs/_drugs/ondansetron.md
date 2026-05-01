---
layout: default
title: Ondansetron
parent: หลักฐานระดับสูง (L1-L2)
nav_order: 118
evidence_level: L1
indication_count: 10
---

# Ondansetron
{: .fs-9 }

ระดับหลักฐาน: **L1** | ข้อบ่งใช้ที่ทำนาย: **10** รายการ
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

ใช้ `txgnn-pipeline` เพื่อยืนยันบริบทโปรเจกต์ ThTxGNN แล้ว — skill ไม่มีคำสั่งเพิ่มเติมสำหรับการสร้างรายงาน ดำเนินการตามรูปแบบที่กำหนดได้เลย

---

> **หมายเหตุก่อนเริ่ม**: `candidate_id = TW-DB00904-multi` → นี่คือรายงานแบบ multi-indication ฉันจะใช้ **Tourette Syndrome (rank 2)** เป็นข้อบ่งใช้หลักในรายงาน เนื่องจากมีหลักฐานระดับ L1 (Phase 4 RCT เสร็จสิ้น + RCT ในวรรณกรรม 2 ฉบับ) ในขณะที่ข้อบ่งใช้ rank 1 (NSIAD) มีเพียงระดับ L5 ไม่มีหลักฐานใดๆ และยังรวม **สรุปการทำนายทั้งหมด 10 รายการ** ไว้ท้ายรายงาน

---

# Ondansetron: จากยาต้านอาการคลื่นไส้อาเจียนสู่ Tourette Syndrome

## สรุปสั้นๆ

Ondansetron เป็น 5-HT3 receptor antagonist ที่ได้รับการใช้อย่างกว้างขวางทั่วโลกในการป้องกันและรักษาอาการคลื่นไส้อาเจียนจากเคมีบำบัดและการผ่าตัด แม้ปัจจุบันจะยังไม่พบข้อมูลการจดทะเบียนในฐานข้อมูล Thai FDA

โมเดล TxGNN คาดการณ์ว่าอาจมีผลต่อ **Tourette Syndrome** โดยมีคะแนน 97.96% อาศัยกลไกการปรับสมดุล dopamine-serotonin ในวงจร cortico-striato-thalamo-cortical (CSTC)

ปัจจุบันมี **การทดลองทางคลินิก Phase 4 ที่เสร็จสิ้นแล้ว 1 รายการ (n=110)** และ **วรรณกรรม 10 ฉบับ** รวม RCT 2 ฉบับ และ cohort 1 ฉบับ สนับสนุนแนวทางนี้โดยตรง

---

## ภาพรวมฉบับย่อ

| รายการ | เนื้อหา |
|------|------|
| ข้อบ่งใช้เดิม | ยาต้านอาการคลื่นไส้อาเจียน (5-HT3 antagonist antiemetic) |
| ข้อบ่งใช้ใหม่ที่ทำนาย | Tourette Syndrome |
| คะแนนการทำนาย TxGNN | 97.96% |
| ระดับหลักฐาน | L1 |
| สถานะการวางจำหน่ายในไทย | ❌ ไม่พบข้อมูลการจดทะเบียน |
| จำนวนใบอนุญาต | 0 รายการ |
| คำแนะนำในการตัดสินใจ | Proceed with Guardrails |

---

## ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

Ondansetron ออกฤทธิ์โดยการปิดกั้นตัวรับ 5-HT3 อย่างจำเพาะเจาะจง ทั้งในบริเวณ area postrema ของสมองส่วน brainstem (ซึ่งเป็นจุดควบคุมการอาเจียน) และในทางเดินอาหาร กลไกนี้ทำให้ยาสามารถขัดขวางสัญญาณประสาทที่กระตุ้นอาการคลื่นไส้ได้อย่างมีประสิทธิภาพ

ความเชื่อมโยงกับ Tourette Syndrome อยู่ที่การที่ตัวรับ 5-HT3 มีการแสดงออกอย่างกว้างขวางในวงจร cortico-striato-thalamo-cortical (CSTC) โดยเฉพาะใน striatum ซึ่งเป็นศูนย์กลางการเกิด tic behavior การปิดกั้น 5-HT3 ส่งผลให้เกิดการปรับสมดุลการปล่อย dopamine และ GABAergic inhibition ซึ่งทั้งสองระบบมีความผิดปกติอย่างชัดเจนใน Tourette Syndrome นอกจากนี้ ผู้ป่วย Tourette มักมีอาการร่วมเช่น OCD ซึ่งใช้วงจร orbitofrontal cortex–striatum เดียวกัน ทำให้ Ondansetron อาจช่วยบรรเทาได้ทั้งอาการหลักและอาการร่วม

หลักฐานจากกรณีศึกษาคลาสสิก (PMID 18184945) ที่พบว่าเด็กชายผู้ป่วย Tourette ซึ่งได้รับ Ondansetron เพื่อรักษาอาการคลื่นไส้จากเคมีบำบัด มีอาการ tic ลดลงอย่างเห็นได้ชัด ยิ่งสนับสนุนความสมเหตุสมผลนี้ และนำไปสู่การออกแบบ RCT ในเวลาต่อมา

---

## หลักฐานจากการทดลองทางคลินิก

| หมายเลขการทดลอง | ระยะ | สถานะ | จำนวนผู้เข้าร่วม | ผลลัพธ์หลัก |
|---------|------|------|------|---------|
| [NCT03239210](https://clinicaltrials.gov/study/NCT03239210) | Phase 4 | เสร็จสิ้น | 110 | ศึกษาผลของ Ondansetron 24 mg/วัน นาน 4 สัปดาห์ เทียบกับยาหลอก ในผู้ป่วย OCD และ tic disorders (รวม Tourette syndrome) ประเมินอาการและการทำงานของสมองด้วย MRI ที่ baseline และสัปดาห์ที่ 4 |

---

## หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|-----|------|------|---------|
| [39876680](https://pubmed.ncbi.nlm.nih.gov/39876680/) | 2025 | RCT | The American Journal of Psychiatry | Ondansetron ขนาดสูง vs ยาหลอกใน OCD และ Tourette's disorder พบผลต่อความรุนแรงของ sensory phenomena และ brain connectivity ในวงจร interoceptive-sensorimotor |
| [15816793](https://pubmed.ncbi.nlm.nih.gov/15816793/) | 2005 | RCT | The Journal of Clinical Psychiatry | การทดลอง 3 สัปดาห์ แบบ randomized double-blind placebo-controlled ประเมินประสิทธิผลของ Ondansetron ใน Tourette's disorder |
| [10565805](https://pubmed.ncbi.nlm.nih.gov/10565805/) | 1999 | Cohort | International Clinical Psychopharmacology | Open-label pilot ใน 6 ผู้ป่วย Tourette ที่ดื้อต่อ haloperidol พบว่า Ondansetron ลดคะแนน YGTSS และ TS-CGI ได้ในขนาด 8–16 mg/วัน |
| [16314763](https://pubmed.ncbi.nlm.nih.gov/16314763/) | 2005 | Case-control | Psychiatric Genetics | ศึกษา HTR3A/HTR3B gene variants ใน Gilles de la Tourette Syndrome ระบุ Ondansetron เป็นยาที่มีศักยภาพในการรักษา GTS ผ่านกลไก 5-HT3 |
| [40489853](https://pubmed.ncbi.nlm.nih.gov/40489853/) | 2025 | Review | Medicine | Narrative review ของการทดลอง Phase III/IV ในการรักษา Tourette syndrome ด้วยยา ครอบคลุมทุกกลุ่มอายุ รวมถึงบทบาทของยาในกลุ่ม 5-HT3 antagonist |
| [21183132](https://pubmed.ncbi.nlm.nih.gov/21183132/) | 2010 | Review | Seminars in Pediatric Neurology | ทบทวน RCT (2005–2010) สำหรับการรักษา tics, Tourette syndrome และ stereotypies ใน ASD ด้วยยา |
| [11474424](https://pubmed.ncbi.nlm.nih.gov/11474424/) | 2001 | Review | CNS Drug Reviews | ทบทวนบทบาทของ Ondansetron ในฐานะ 5-HT3 antagonist และการประยุกต์ใช้ในโรคทาง CNS รวม Tourette syndrome |
| [18184945](https://pubmed.ncbi.nlm.nih.gov/18184945/) | 2008 | Case series | Journal of Child Neurology | รายงานเด็กชายอายุ 8 ปีที่มีทั้ง leukemia และ Tourette syndrome: ได้รับ Ondansetron เพื่อแก้ CINV แต่อาการ tic ดีขึ้นอย่างเห็นได้ชัด และกลับมาเมื่อลดขนาดยา |
| [21568361](https://pubmed.ncbi.nlm.nih.gov/21568361/) | 2011 | Review | Drugs | ทบทวนจุดร่วมระหว่าง OCD, impulse control disorders และการติดยา — วิเคราะห์บทบาทของ serotonin ในวงจรที่ทับซ้อนกับ Tourette |
| [23126479](https://pubmed.ncbi.nlm.nih.gov/23126479/) | 2013 | — | Nordic Journal of Psychiatry | ศึกษา 5-HTR3 C178T polymorphism ใน tardive dyskinesia อ้างอิงประสิทธิผลของ Ondansetron ใน GTS เป็นหลักฐานสนับสนุน |

---

## ข้อมูลการวางจำหน่ายในประเทศไทย

ตามผลการสืบค้นข้อมูล Thai FDA (ณ วันที่ 30 เมษายน 2569) **ไม่พบการจดทะเบียนยา Ondansetron** ในฐานข้อมูล

> **หมายเหตุ**: Ondansetron เป็นยาที่มีใช้อย่างแพร่หลายในทางคลินิกทั่วโลก ข้อมูลนี้อาจสะท้อนความไม่ครบถ้วนของการสืบค้น ควรตรวจสอบโดยตรงกับ อย. ก่อนตัดสินใจ

---

## ข้อพิจารณาด้านความปลอดภัย

กรุณาดูข้อมูลความปลอดภัยในเอกสารกำกับยา

---

## สรุปการทำนายทั้งหมด (Multi-Indication Pack)

| อันดับ | ข้อบ่งใช้ | คะแนน TxGNN | ระดับหลักฐาน | คำแนะนำ |
|------|---------|:-----------:|:-----------:|:------:|
| 1 | Nephrogenic Syndrome of Inappropriate Antidiuresis | 98.65% | L5 | Hold |
| **2** | **Tourette Syndrome** ⭐ | **97.96%** | **L1** | **Proceed with Guardrails** |
| 3 | Trichotillomania | 97.27% | L5 | Hold |
| 4 | Paranoid Personality Disorder | 97.16% | L5 | Hold |
| 5 | Schizoid Personality Disorder | 97.16% | L5 | Hold |
| 6 | Histrionic Personality Disorder | 97.16% | L5 | Hold |
| 7 | Schizotypal Personality Disorder | 97.16% | L5 | Hold |
| 8 | Common Cold | 97.03% | L5 | Hold |
| 9 | Allergic Urticaria | 96.78% | L5 | Hold |
| 10 | Acute Intermittent Porphyria | 96.56% | L5 | Hold |

> ⭐ = ข้อบ่งใช้หลักของรายงานฉบับนี้ | 9 ข้อบ่งใช้ที่เหลืออยู่ในสถานะ Hold เนื่องจากขาดหลักฐานทางคลินิก

---

## สรุปและขั้นตอนถัดไป

**การตัดสินใจ: Proceed with Guardrails (สำหรับ Tourette Syndrome)**

**เหตุผล:**
มีหลักฐานระดับ L1 จาก Phase 4 RCT ที่เสร็จสิ้นแล้ว (NCT03239210, n=110) ซึ่งศึกษา Ondansetron โดยตรงในผู้ป่วย Tourette syndrome/tic disorders และมี RCT สนับสนุนเพิ่มเติมอีก 1 ฉบับในวรรณกรรม กลไกผ่านวงจร CSTC มีความสมเหตุสมผลทางวิทยาศาสตร์และสอดคล้องกับพยาธิสรีรวิทยาของโรค

**หากต้องการดำเนินการต่อต้อง:**
- ดาวน์โหลดและวิเคราะห์ข้อมูล MOA และ safety จาก DrugBank API (แก้ไข Data Gap DG002 และ DG001)
- ตรวจสอบสถานะการจดทะเบียนยาในประเทศไทยจาก อย. โดยตรง เนื่องจากผลการสืบค้นอาจไม่ครบถ้วน
- ดาวน์โหลด full-text ผลการทดลอง NCT03239210 (ผลอาจอยู่ใน PMID 39876680) เพื่อประเมินขนาดผลเชิงปริมาณ
- ประเมินขนาดยาที่เหมาะสม — การทดลอง Phase 4 ใช้ 24 mg/วัน ซึ่งสูงกว่าขนาดยาต้านอาเจียนมาตรฐาน
- ปรึกษาผู้เชี่ยวชาญด้าน pediatric neurology หรือ movement disorders ในบริบทประเทศไทยก่อนวางแผนการศึกษาต่อ
---

