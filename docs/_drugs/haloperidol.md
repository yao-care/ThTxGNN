---
layout: default
title: Haloperidol
parent: หลักฐานระดับสูง (L1-L2)
nav_order: 80
evidence_level: L1
indication_count: 10
---

# Haloperidol
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

The txgnn-pipeline skill confirms TxGNN domain context. The system prompt provides the complete report format. I'll now generate the report.

**Note on Evidence Pack analysis before writing:**
- The 10 predicted indications — ranks 1–9 are all **L5 / Hold** with zero clinical evidence and no biological rationale
- Rank 10 (manic bipolar affective disorder) is the only **L1 / Proceed with Guardrails** finding with 9 clinical trials and 20 literature items
- Report will feature rank 10 as the primary actionable prediction per clinical relevance design intent
- `taiwan_regulatory` → 0 licenses → skip the detailed license table (Rule 5)
- No antineoplastic criteria met → skip cytotoxicity section
- All safety fields = `[Data Gap]` → use fallback text

---

# Haloperidol: จากโรคจิตเภทสู่โรคอารมณ์สองขั้วชนิดอาการคลุ้มคลั่ง

## สรุปสั้นๆ

Haloperidol เป็นยาต้านโรคจิตแบบดั้งเดิม (typical antipsychotic) กลุ่ม butyrophenone ซึ่งเดิมใช้รักษาโรคจิตเภทและภาวะจิตเวชเฉียบพลัน โมเดล TxGNN คาดการณ์ว่าอาจมีผลต่อ **โรคอารมณ์สองขั้วชนิดอาการคลุ้มคลั่ง (Manic Bipolar Affective Disorder)** ซึ่งเป็นข้อบ่งใช้เดียวในกลุ่มการทำนายทั้ง 10 รายการที่มีหลักฐานรองรับระดับสูง ปัจจุบันมี **การทดลองทางคลินิก 9 รายการ** และ **วรรณกรรม 20 ฉบับ** สนับสนุนแนวทางนี้

## ภาพรวมฉบับย่อ

| รายการ | เนื้อหา |
|------|------|
| ข้อบ่งใช้เดิม | โรคจิตเภทและภาวะจิตเวชเฉียบพลัน |
| ข้อบ่งใช้ใหม่ที่ทำนาย | โรคอารมณ์สองขั้วชนิดอาการคลุ้มคลั่ง (Manic Bipolar Affective Disorder) |
| คะแนนการทำนาย TxGNN | 99.83% |
| ระดับหลักฐาน | L1 |
| สถานะการวางจำหน่ายในไทย | ✗ ไม่มีทะเบียนในระบบ Thai FDA |
| จำนวนใบอนุญาต | 0 รายการ |
| คำแนะนำในการตัดสินใจ | Proceed with Guardrails |

## ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

ปัจจุบันยังขาดข้อมูลกลไกการออกฤทธิ์โดยละเอียดจากแหล่งข้อมูลอย่างเป็นทางการ (DrugBank API ยังไม่ได้รับการ query) อย่างไรก็ตาม จากหลักฐานเภสัชวิทยาที่เป็นที่ยอมรับ Haloperidol มีกลไกหลักคือการเป็น **D2 dopamine receptor antagonist** ที่มีประสิทธิภาพสูง ซึ่งตรงกับพยาธิสรีรวิทยาของโรคอารมณ์สองขั้วชนิดอาการคลุ้มคลั่ง โดยภาวะ dopaminergic hyperactivity ในวงจรเมโซลิมบิกเป็นหนึ่งในกลไกหลักที่ก่อให้เกิดอาการคลุ้มคลั่ง ความคิดแล่น และพฤติกรรมก้าวร้าว

โรคจิตเภทและโรคอารมณ์สองขั้วชนิดอาการคลุ้มคลั่งมีพยาธิสรีรวิทยาร่วมกันในด้านการเพิ่มขึ้นของการส่งสัญญาณโดปามีน ดังนั้น การที่ Haloperidol บล็อก D2 receptor ได้รวดเร็วและมีประสิทธิภาพ จึงทำให้มีผลระงับอาการคลุ้มคลั่งทางคลินิกได้ สอดคล้องกับการที่ยานี้ถูกใช้เป็น **active control** ในการทดลอง Phase 3 หลายรายการในข้อบ่งใช้นี้มาตั้งแต่ทศวรรษ 1970 จนถึงปัจจุบัน

ยิ่งไปกว่านั้น แนวปฏิบัติทางจิตเวชสากล (เช่น Kishi et al. 2022 network meta-analysis) ยืนยันว่า Haloperidol มีประสิทธิผลในการรักษาอาการคลุ้มคลั่งเฉียบพลันในระดับที่เทียบเคียงได้กับยาต้านโรคจิตยุคที่สองหลายชนิด แม้จะมีโปรไฟล์ผลข้างเคียงด้าน extrapyramidal symptoms (EPS) ที่ต้องติดตามเพิ่มเติม

## หลักฐานจากการทดลองทางคลินิก

| หมายเลขการทดลอง | ระยะ | สถานะ | จำนวนผู้เข้าร่วม | ผลลัพธ์หลัก |
|---------|------|------|------|---------|
| [NCT00253149](https://clinicaltrials.gov/study/NCT00253149) | Phase 3 | เสร็จสิ้น | 158 | Haloperidol เป็นหนึ่งในสามแขนการรักษา เปรียบเทียบกับ Risperidone และยาหลอก ในฐานะยาเสริม mood stabilizer สำหรับโรคอารมณ์สองขั้ว |
| [NCT00129220](https://clinicaltrials.gov/study/NCT00129220) | Phase 3 | เสร็จสิ้น | 224 | Haloperidol เป็น active control ใน 3-arm trial เปรียบเทียบกับ Olanzapine ในอาการคลุ้มคลั่งหรืออารมณ์ปนป่วนของโรคอารมณ์สองขั้ว I |
| [NCT00253162](https://clinicaltrials.gov/study/NCT00253162) | Phase 3 | เสร็จสิ้น | 439 | Haloperidol เป็น active control ระยะ 12 สัปดาห์ เปรียบเทียบกับ Risperidone ในอาการคลุ้มคลั่ง Bipolar I Disorder |
| [NCT00126009](https://clinicaltrials.gov/study/NCT00126009) | Phase 2 | เสร็จสิ้น | 120 | เปรียบเทียบ Valproate + Amisulpride กับ Valproate + Haloperidol (5–15 mg/day) ในผู้ป่วยอาการคลุ้มคลั่ง Bipolar I ระยะ 3 เดือน |
| [NCT00097266](https://clinicaltrials.gov/study/NCT00097266) | Phase 3 | เสร็จสิ้น | 615 | ยืนยันประสิทธิผลและความปลอดภัยของ Aripiprazole monotherapy ในโรคอารมณ์สองขั้วชนิดอาการคลุ้มคลั่ง ระยะ 12 สัปดาห์ ให้บริบทเปรียบเทียบ |
| [NCT06049953](https://clinicaltrials.gov/study/NCT06049953) | N/A | กำลังรับสมัคร | 200 | ศึกษาผลต่อพัฒนาการของทารกจากการรับยาต้านโรคจิต (รวม Haloperidol) ระหว่างตั้งครรภ์ในผู้ป่วยโรคจิตเวชรุนแรง ให้ข้อมูลด้านความปลอดภัยในกลุ่มพิเศษ |
| [NCT00767715](https://clinicaltrials.gov/study/NCT00767715) | Phase 4 | ยุติก่อนกำหนด | 11 | เปรียบเทียบ Olanzapine กับยาต้านโรคจิตแบบดั้งเดิม (รวม Haloperidol) ในโรคอารมณ์สองขั้วชนิดอาการคลุ้มคลั่งเฉียบพลัน ยุติก่อนกำหนดเนื่องจาก n น้อยเกินไป |
| [NCT03541031](https://clinicaltrials.gov/study/NCT03541031) | N/A | ไม่ทราบ | 120 | ศึกษาการเสริม Micronutrient และ Fish oil สำหรับโรคอารมณ์สองขั้ว เพื่อลดขนาดยาหลัก ให้บริบทด้านการจัดการร่วม |
| [NCT04327843](https://clinicaltrials.gov/study/NCT04327843) | Phase 3 | เสร็จสิ้น | 22 | ศึกษา LAI (Long-Acting Injectable) ในโรคจิตเวชเรื้อรังในแทนซาเนีย ให้บริบทสำหรับ Haloperidol decanoate (LAI) ในฐานะทางเลือกเพิ่มการยึดมั่นต่อการรักษา |

## หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|-----|------|------|---------|
| [34642461](https://pubmed.ncbi.nlm.nih.gov/34642461/) | 2022 | Meta-analysis | Molecular Psychiatry | Systematic review และ network meta-analysis เปรียบเทียบประสิทธิผล ความสามารถรับ และความปลอดภัยของยาในอาการคลุ้มคลั่งเฉียบพลัน ครอบคลุม Haloperidol เป็นตัวเปรียบเทียบหลัก |
| [36789916](https://pubmed.ncbi.nlm.nih.gov/36789916/) | 2023 | Meta-analysis | BMJ Mental Health | เปรียบเทียบขนาดยาเทียบเท่าของยาต้านโรคจิตระหว่างอาการคลุ้มคลั่งเฉียบพลันและโรคจิตเภท ให้แนวทางปรับขนาดยา Haloperidol ในสองข้อบ่งใช้ |
| [22161387](https://pubmed.ncbi.nlm.nih.gov/22161387/) | 2011 | Meta-analysis | Cochrane Database Syst Rev | Cochrane systematic review: Oxcarbazepine ในโรคอารมณ์สองขั้ว ใช้ Haloperidol เป็น reference standard ในการเปรียบเทียบ |
| [22134043](https://pubmed.ncbi.nlm.nih.gov/22134043/) | 2012 | RCT | Journal of Affective Disorders | Haloperidol เป็น active control ในการศึกษาสุ่มปกปิดสองทาง: Olanzapine vs Haloperidol vs Placebo ในผู้ป่วยชาวญี่ปุ่นที่มีอาการคลุ้มคลั่ง/ปนป่วน Bipolar I |
| [3312180](https://pubmed.ncbi.nlm.nih.gov/3312180/) | 1987 | RCT | J Clinical Psychiatry | Double-blind controlled study เปรียบเทียบ Clonazepam กับ Haloperidol และ Lithium ในผู้ป่วยอาการคลุ้มคลั่งเฉียบพลัน ชี้ข้อดี-ข้อเสียของ Haloperidol โดยตรง |
| [369472](https://pubmed.ncbi.nlm.nih.gov/369472/) | 1979 | RCT | Arch General Psychiatry | Double-blind 5-week trial: Lithium + Haloperidol vs Placebo + Haloperidol ในผู้ป่วย schizo-affective excited พบประสิทธิผลที่ดีขึ้นอย่างมีนัยสำคัญ |
| [10343182](https://pubmed.ncbi.nlm.nih.gov/10343182/) | 1999 | RCT | Neuropsychobiology | ศึกษาผล Lithium และ Haloperidol ต่อระดับ Gαs protein ในเม็ดเลือดขาวผู้ป่วย Bipolar Affective Disorder ให้หลักฐานกลไกระดับโมเลกุล |
| [22070611](https://pubmed.ncbi.nlm.nih.gov/22070611/) | 2012 | Review | CNS Neuroscience & Therapeutics | ทบทวนการรักษา Bipolar ที่ดื้อยา: แนะนำให้เพิ่ม Haloperidol ในผู้ป่วยที่ตอบสนองต่อ Lithium/Valproate บางส่วน เป็นกลยุทธ์ที่ได้รับการยอมรับ |
| [18344731](https://pubmed.ncbi.nlm.nih.gov/18344731/) | 2008 | Review | J Clinical Psychopharmacology | Systematic review: เปรียบเทียบอุบัติการณ์ EPS จาก Haloperidol เทียบกับยาต้านโรคจิตยุคที่สองใน BD และ SZ ข้อมูลสำคัญสำหรับการจัดการผลข้างเคียง |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Review | Acta Psychiatrica Scandinavica | ทบทวนทางเลือกการรักษาตามหลักฐานสำหรับอาการคลุ้มคลั่ง รวมถึงบทบาทของ Haloperidol ในการจัดการอาการเฉียบพลัน |

## ข้อพิจารณาด้านความปลอดภัย

กรุณาดูข้อมูลความปลอดภัยในเอกสารกำกับยา

> ⚠️ ข้อควรทราบ: มีรายงานในวรรณกรรม (PMID 18344731) เกี่ยวกับอัตรา extrapyramidal symptoms (EPS) ที่สูงกว่ายาต้านโรคจิตยุคที่สองเมื่อใช้ Haloperidol ในโรคอารมณ์สองขั้ว — ควรพิจารณาเป็นส่วนหนึ่งของการประเมินความเสี่ยง-ประโยชน์

## สรุปและขั้นตอนถัดไป

**การตัดสินใจ: Proceed with Guardrails**

**เหตุผล:**
มี Phase 3 RCT ที่เสร็จสมบูรณ์อย่างน้อย 3 รายการซึ่ง Haloperidol ถูกใช้เป็น active control โดยตรงในผู้ป่วยโรคอารมณ์สองขั้วชนิดอาการคลุ้มคลั่ง ร่วมกับ network meta-analysis ระดับ Molecular Psychiatry (2022) ที่รวมยานี้ไว้ในการเปรียบเทียบ ยืนยันระดับหลักฐาน L1 อย่างชัดเจน อย่างไรก็ตาม ยาไม่มีทะเบียนใน Thai FDA และข้อมูลความปลอดภัยฉบับสมบูรณ์ยังขาด

**หากต้องการดำเนินการต่อต้อง:**
- ดาวน์โหลดและวิเคราะห์ฉลากยา (Package Insert/PIL) จากประเทศที่ยาได้รับอนุมัติ เพื่อรวบรวมคำเตือนหลัก ข้อห้ามใช้ และข้อมูล DDI
- Query DrugBank API สำหรับ MOA โดยละเอียด (DrugBank ID: DB00502)
- ประเมินเส้นทางการขอทะเบียนยาใน Thai FDA หรือพิจารณาใช้ผ่านกลไก compassionate use / off-label ภายใต้การดูแลของแพทย์ผู้เชี่ยวชาญ
- วางแผนติดตาม EPS (Extrapyramidal Symptoms) และ Tardive Dyskinesia อย่างเป็นระบบ เนื่องจากเป็นความเสี่ยงหลักที่แตกต่างจากยาต้านโรคจิตยุคใหม่
---

