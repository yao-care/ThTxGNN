---
layout: default
title: Amitriptyline
parent: การคาดการณ์จากโมเดล (L5)
nav_order: 16
evidence_level: L5
indication_count: 10
---

# Amitriptyline
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

# Amitriptyline: จากยาต้านซึมเศร้าสู่โรคซึมเศร้ารุนแรง (MDD) และข้อบ่งใช้ใหม่อีก 9 รายการ

---

## สรุปสั้นๆ

Amitriptyline เป็นยาต้านซึมเศร้ากลุ่มไตรไซคลิก (TCA) ที่ใช้ในระดับสากลมาตั้งแต่ปี 1961 สำหรับรักษาโรคซึมเศร้า ปวดเส้นประสาท และป้องกันไมเกรน
โมเดล TxGNN คาดการณ์ข้อบ่งใช้ใหม่ **10 รายการ** โดยครอบคลุมกลุ่มโรคซึมเศร้าหลายชนิดย่อย โรคกลัว/วิตกกังวล และโรคหายากทางพันธุกรรม
ข้อบ่งใช้ที่มีหลักฐานสนับสนุนแข็งแกร่งที่สุดคือ **โรคซึมเศร้ารุนแรง (MDD)** ซึ่งมี **การทดลองทางคลินิก 19 รายการ** และ **วรรณกรรม 20 ฉบับ** อย่างไรก็ตาม ยานี้ **ยังไม่ได้ขึ้นทะเบียนในประเทศไทย**

---

## ภาพรวมฉบับย่อ

| รายการ | เนื้อหา |
|------|------|
| ข้อบ่งใช้เดิม | โรคซึมเศร้า ปวดเส้นประสาท ป้องกันไมเกรน (ข้อมูลจากแหล่งสากล — ไม่มีข้อมูลจาก Thai FDA) |
| จำนวนข้อบ่งใช้ใหม่ที่ทำนาย | 10 รายการ |
| สถานะการวางจำหน่ายในไทย | ✗ ยังไม่วางจำหน่าย |
| จำนวนใบอนุญาต | 0 รายการ |

### ตารางสรุปข้อบ่งใช้ใหม่ทั้งหมด

| อันดับ | ข้อบ่งใช้ใหม่ที่ทำนาย | คะแนน TxGNN | ระดับหลักฐาน | การทดลอง | วรรณกรรม | คำแนะนำ |
|:------:|----------------------|:-----------:|:------------:|:--------:|:--------:|:-------:|
| 1 | โรคคอบิดชั่วคราวในทารก (Benign Paroxysmal Torticollis of Infancy) | 97.72% | L5 | 0 | 0 | Hold |
| 2 | โรคซึมเศร้าจากภายใน (Endogenous Depression) | 97.71% | L1 | 0 | 20 | Proceed with Guardrails |
| 3 | โรคกลัวที่โล่ง (Agoraphobia) | 97.27% | L4 | 0 | 6 | Research Question |
| 4 | โรคซึมเศร้ารุนแรง (Major Depressive Disorder) | 96.85% | L1 | 19 | 20 | Proceed with Guardrails |
| 5 | กลุ่มอาการ Ohdo และสายพันธุ์ย่อย | 95.95% | L5 | 0 | 0 | Hold |
| 6 | เมลันโคเลีย (Melancholia) | 95.52% | L5 | 0 | 0 | Hold |
| 7 | โรคซึมเศร้าชนิดประสาท (Neurotic Depression) | 95.48% | L5 | 0 | 0 | Hold |
| 8 | โรคกลัว (Phobic Disorder) | 94.68% | L4 | 0 | 20 | Research Question |
| 9 | โรคซึมเศร้าขั้วเดียว (Unipolar Depression) | 94.61% | L1 | 8 | 0 | Proceed with Guardrails |
| 10 | กลุ่มอาการเปลือกตาตีบ-บกพร่องทางสติปัญญา ชนิด Ohdo | 94.47% | L5 | 0 | 0 | Hold |

---

## ทำไมการคาดการณ์เหล่านี้จึงสมเหตุสมผล?

Amitriptyline ออกฤทธิ์โดยยับยั้งการนำกลับของสารสื่อประสาท serotonin (5-HT) และ norepinephrine (NE) ที่บริเวณ synapse ส่งผลให้ระดับสารสื่อประสาทเหล่านี้ในสมองเพิ่มขึ้น นอกจากนี้ยังมีฤทธิ์ต้าน histamine (H₁), muscarinic และ α-adrenergic receptor ซึ่งอธิบายทั้งผลข้างเคียงและฤทธิ์ทางเภสัชวิทยาที่หลากหลาย

การคาดการณ์จาก TxGNN แบ่งได้เป็น 3 กลุ่มหลัก:

**กลุ่มโรคซึมเศร้า (อันดับ 2, 4, 6, 7, 9):** Amitriptyline เป็นยารักษาซึมเศร้าที่มีประสิทธิภาพพิสูจน์แล้วมากว่า 60 ปี การที่โมเดลทำนายข้อบ่งใช้ในกลุ่มนี้ถือเป็นการยืนยัน (validation) ความถูกต้องของโมเดล เนื่องจาก endogenous depression, MDD, unipolar depression, melancholia และ neurotic depression ล้วนเป็นชนิดย่อยหรือคำเรียกทางประวัติศาสตร์ของโรคซึมเศร้าที่ Amitriptyline ใช้รักษาอยู่แล้วในระดับสากล กลไก 5-HT/NE reuptake inhibition ตรงกับสมมติฐาน monoamine ของโรคซึมเศร้าโดยตรง

**กลุ่มโรควิตกกังวล/กลัว (อันดับ 3, 8):** ฤทธิ์ต้านวิตกกังวลของ Amitriptyline มาจากการเพิ่มระดับ serotonin ซึ่งช่วยปรับสมดุลวงจร amygdala-fear circuit ร่วมกับฤทธิ์สงบประสาทจากการต้าน H₁ receptor อย่างไรก็ตาม หลักฐานทางคลินิกในโรคกลัวที่โล่ง (agoraphobia) และโรคกลัว (phobic disorder) ยังจำกัด โดยส่วนใหญ่ศึกษายาในกลุ่มเดียวกัน (เช่น clomipramine) หรือยากลุ่ม SSRI/MAOI

**กลุ่มโรคหายาก (อันดับ 1, 5, 10):** การคาดการณ์สำหรับ benign paroxysmal torticollis of infancy, Ohdo syndrome และ blepharophimosis-intellectual disability syndrome ขาดความเชื่อมโยงเชิงกลไกที่ชัดเจน โรคเหล่านี้เกิดจากความผิดปกติทางพันธุกรรม (เช่น KAT6B mutation) ซึ่งกลไกการปรับ monoamine ของ Amitriptyline ไม่สามารถแก้ไขได้

---

## ข้อบ่งใช้ที่ 4: โรคซึมเศร้ารุนแรง (Major Depressive Disorder)

> **ระดับหลักฐาน: L1** | **คำแนะนำ: Proceed with Guardrails** | **คะแนน TxGNN: 96.85%**

### หลักฐานจากการทดลองทางคลินิก

| หมายเลขการทดลอง | ระยะ | สถานะ | จำนวนผู้เข้าร่วม | ผลลัพธ์หลัก |
|---------|------|------|:------:|---------|
| [NCT05952713](https://clinicaltrials.gov/study/NCT05952713) | — | เสร็จสิ้น | 73,336 | เปรียบเทียบ 15 ยาต้านซึมเศร้า (รวม amitriptyline) ในผู้ป่วย MDD ระดับประชากร จำลองการทดลองแบบสุ่ม |
| [NCT02014363](https://clinicaltrials.gov/study/NCT02014363) | Phase 2 | เสร็จสิ้น | 164 | ศึกษา non-inferiority ของ ETS6103 เทียบ amitriptyline ในผู้ป่วย MDD ที่ไม่ตอบสนองต่อ SSRI |
| [NCT00351910](https://clinicaltrials.gov/study/NCT00351910) | Phase 3 | เสร็จสิ้น | 494 | Quetiapine SR + ยาต้านซึมเศร้า vs ยาต้านซึมเศร้าเดี่ยว ในผู้ป่วย MDD |
| [NCT01049347](https://clinicaltrials.gov/study/NCT01049347) | Phase 3 | เสร็จสิ้น | 127 | ศึกษาระบบ HPA ระหว่างรักษาด้วย amitriptyline และ paroxetine ในผู้ป่วยซึมเศร้าปานกลาง-รุนแรง |
| [NCT05931965](https://clinicaltrials.gov/study/NCT05931965) | — | เสร็จสิ้น | 88 | เปรียบเทียบยาต้านซึมเศร้า + L-methylfolate, B12 หรือ magnesium ในผู้ป่วยซึมเศร้า |
| [NCT02237937](https://clinicaltrials.gov/study/NCT02237937) | Phase 4 | ไม่ทราบ | 80 | ปรับขนาดยาต้านซึมเศร้า (รวม amitriptyline) ตามจีโนไทป์ ABCB1 |
| [NCT00704860](https://clinicaltrials.gov/study/NCT00704860) | Phase 4 | เสร็จสิ้น | 27 | ศึกษาการฝ่อของ hippocampus และ serotonin genetic polymorphism ในซึมเศร้าดื้อยา |
| [NCT00325000](https://clinicaltrials.gov/study/NCT00325000) | — | ยุติ | — | จิตบำบัด IPT เข้มข้น + เภสัชบำบัด ในผู้ป่วยซึมเศร้ารุนแรง |
| [NCT04777006](https://clinicaltrials.gov/study/NCT04777006) | Phase 4 | กำลังดำเนินการ | 487 | Stepped care สำหรับซึมเศร้าในระบบ HIV มาลาวี |
| [NCT03324035](https://clinicaltrials.gov/study/NCT03324035) | Phase 3 | ไม่ทราบ | 102 | Amitriptyline ในอาการปวดเส้นประสาทจากโรคเรื้อน |

### หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|:---:|------|------|---------|
| [29477251](https://pubmed.ncbi.nlm.nih.gov/29477251/) | 2018 | Meta-analysis | Lancet | Network meta-analysis ของ 21 ยาต้านซึมเศร้า ยืนยัน amitriptyline มีประสิทธิผลเหนือยาหลอก |
| [23235671](https://pubmed.ncbi.nlm.nih.gov/23235671/) | 2012 | Meta-analysis | Cochrane Database | Cochrane systematic review: amitriptyline vs placebo ใน MDD ยืนยันประสิทธิผล |
| [36253442](https://pubmed.ncbi.nlm.nih.gov/36253442/) | 2023 | Meta-analysis | Mol Psychiatry | Network meta-analysis ยาต้านซึมเศร้าใน MDD ระยะรักษาต่อเนื่อง |
| [27289172](https://pubmed.ncbi.nlm.nih.gov/27289172/) | 2016 | Meta-analysis | Lancet | เปรียบเทียบยาต้านซึมเศร้าใน MDD ในเด็กและวัยรุ่น |
| [38360024](https://pubmed.ncbi.nlm.nih.gov/38360024/) | 2024 | Meta-analysis | Lancet Psychiatry | Network meta-analysis การรักษาซึมเศร้าชนิดมีอาการจิต |
| [25911132](https://pubmed.ncbi.nlm.nih.gov/25911132/) | 2015 | Meta-analysis | J Affect Disord | ขนาดยาเทียบเท่าของยาต้านซึมเศร้าจาก RCT |
| [28850959](https://pubmed.ncbi.nlm.nih.gov/28850959/) | 2018 | Systematic Review | Pharmacopsychiatry | การชักภายใต้การรักษาด้วยยาต้านซึมเศร้า |
| [38856993](https://pubmed.ncbi.nlm.nih.gov/38856993/) | 2024 | Review | JAMA | การจัดการโรคซึมเศร้าในผู้ใหญ่ — ทบทวนภาพรวม |
| [38379028](https://pubmed.ncbi.nlm.nih.gov/38379028/) | 2024 | Cohort | Acta Psychiatr Scand | เปรียบเทียบ 17 ยาต้านซึมเศร้าระยะยาว 2 ปี ระดับประชากร |
| [32565594](https://pubmed.ncbi.nlm.nih.gov/32565594/) | 2020 | RCT | Indian J Pharmacol | Vilazodone vs escitalopram vs amitriptyline ใน MDD — RCT เปิดเผย |

---

## ข้อบ่งใช้ที่ 2: โรคซึมเศร้าจากภายใน (Endogenous Depression)

> **ระดับหลักฐาน: L1** | **คำแนะนำ: Proceed with Guardrails** | **คะแนน TxGNN: 97.71%**

### หลักฐานจากการทดลองทางคลินิก

ปัจจุบันยังไม่มีการลงทะเบียนการทดลองทางคลินิกที่เกี่ยวข้องโดยตรงกับ "endogenous depression" เนื่องจากคำนิยามนี้ถูกแทนที่ด้วย MDD ในระบบการจำแนกสมัยใหม่

### หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|:---:|------|------|---------|
| [10757255](https://pubmed.ncbi.nlm.nih.gov/10757255/) | 2000 | RCT | J Psychopharmacol | Venlafaxine vs amitriptyline ใน MDD ±melancholia: ทั้งคู่มีประสิทธิผลใกล้เคียง |
| [1960381](https://pubmed.ncbi.nlm.nih.gov/1960381/) | 1991 | RCT | Int Clin Psychopharmacol | Fluoxetine vs amitriptyline ใน MDD: ประสิทธิผลเท่ากัน fluoxetine ดีกว่าด้านความจำ |
| [2858187](https://pubmed.ncbi.nlm.nih.gov/2858187/) | 1985 | RCT | Arch Gen Psychiatry | Alprazolam, amitriptyline, doxepin vs placebo (n=504): ยาทั้งสามดีกว่ายาหลอกอย่างมีนัยสำคัญ |
| [7052009](https://pubmed.ncbi.nlm.nih.gov/7052009/) | 1982 | RCT | Arch Gen Psychiatry | Phenelzine vs amitriptyline vs placebo: ยาทั้งสองดีกว่ายาหลอกและมีประสิทธิผลเทียบเท่า |
| [6461690](https://pubmed.ncbi.nlm.nih.gov/6461690/) | 1982 | RCT | J Affect Disord | Lithium + L-tryptophan vs amitriptyline ใน endogenous depression: ไม่แตกต่างกัน |
| [6452798](https://pubmed.ncbi.nlm.nih.gov/6452798/) | 1981 | RCT | Acta Psychiatr Scand | Zimelidine vs amitriptyline ใน endogenous depression (n=40): ประสิทธิผลเทียบเท่า |
| [7007357](https://pubmed.ncbi.nlm.nih.gov/7007357/) | 1981 | RCT | J Clin Psychiatry | Amoxapine vs amitriptyline ใน endogenous depression (n=46): ผลลัพธ์ใกล้เคียง |
| [7212100](https://pubmed.ncbi.nlm.nih.gov/7212100/) | 1981 | Cohort | Am J Psychiatry | EEG sleep criteria ทำนายการตอบสนองต่อ amitriptyline ใน endogenous depression (n=34) |
| [400982](https://pubmed.ncbi.nlm.nih.gov/400982/) | 1979 | Cohort | Prog Neuropsychopharmacol | เภสัชจลนศาสตร์ของ amitriptyline ใน endogenous depression (n=35) |
| [33438398](https://pubmed.ncbi.nlm.nih.gov/33438398/) | 2021 | Review | ACS Chem Neurosci | ทบทวนครอบคลุม: Amitriptyline ยับยั้ง 5-HT/NE reuptake และมีผลต่อ histaminergic, muscarinic receptor |

---

## ข้อบ่งใช้ที่ 9: โรคซึมเศร้าขั้วเดียว (Unipolar Depression)

> **ระดับหลักฐาน: L1** | **คำแนะนำ: Proceed with Guardrails** | **คะแนน TxGNN: 94.61%**

### หลักฐานจากการทดลองทางคลินิก

| หมายเลขการทดลอง | ระยะ | สถานะ | จำนวนผู้เข้าร่วม | ผลลัพธ์หลัก |
|---------|------|------|:------:|---------|
| [NCT05952713](https://clinicaltrials.gov/study/NCT05952713) | — | เสร็จสิ้น | 73,336 | เปรียบเทียบ 15 ยาต้านซึมเศร้าระยะยาวระดับประชากร รวม amitriptyline |
| [NCT02014363](https://clinicaltrials.gov/study/NCT02014363) | Phase 2 | เสร็จสิ้น | 164 | ETS6103 non-inferiority vs amitriptyline ในผู้ป่วยดื้อ SSRI |
| [NCT00351910](https://clinicaltrials.gov/study/NCT00351910) | Phase 3 | เสร็จสิ้น | 494 | Quetiapine SR เสริมยาต้านซึมเศร้าใน MDD ที่ตอบสนองไม่เพียงพอ |
| [NCT01049347](https://clinicaltrials.gov/study/NCT01049347) | Phase 3 | เสร็จสิ้น | 127 | Amitriptyline vs paroxetine — ศึกษาระบบ HPA ในซึมเศร้าปานกลาง-รุนแรง |
| [NCT02237937](https://clinicaltrials.gov/study/NCT02237937) | Phase 4 | ไม่ทราบ | 80 | ปรับขนาดยาตามจีโนไทป์ ABCB1 (P-glycoprotein) |
| [NCT00704860](https://clinicaltrials.gov/study/NCT00704860) | Phase 4 | เสร็จสิ้น | 27 | ซึมเศร้าดื้อยา: hippocampus atrophy + serotonin polymorphism |
| [NCT05931965](https://clinicaltrials.gov/study/NCT05931965) | — | เสร็จสิ้น | 88 | ยาต้านซึมเศร้า + อาหารเสริม (folate, B12, Mg) ในซึมเศร้า |
| [NCT00325000](https://clinicaltrials.gov/study/NCT00325000) | — | ยุติ | — | IPT เข้มข้น + เภสัชบำบัด ในซึมเศร้ารุนแรง |

> **หมายเหตุ:** การทดลองทางคลินิกในกลุ่ม unipolar depression ทับซ้อนกับกลุ่ม MDD ทั้งหมด เนื่องจากทั้งสองเป็นหน่วยโรคที่ทับซ้อนกันทางคลินิก

### หลักฐานจากวรรณกรรม

ปัจจุบันยังไม่มีวรรณกรรมที่สืบค้นได้โดยตรงภายใต้คำค้น "unipolar depression" อย่างไรก็ตาม วรรณกรรมภายใต้ MDD และ endogenous depression สามารถนำมาอ้างอิงได้โดยตรง

---

## ข้อบ่งใช้ที่ 8: โรคกลัว (Phobic Disorder)

> **ระดับหลักฐาน: L4** | **คำแนะนำ: Research Question** | **คะแนน TxGNN: 94.68%**

### หลักฐานจากการทดลองทางคลินิก

ปัจจุบันยังไม่มีการลงทะเบียนการทดลองทางคลินิกที่เกี่ยวข้อง

### หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|:---:|------|------|---------|
| [7052009](https://pubmed.ncbi.nlm.nih.gov/7052009/) | 1982 | RCT | Arch Gen Psychiatry | Phenelzine vs amitriptyline vs placebo ในซึมเศร้า±อาการกลัว: amitriptyline มีประสิทธิผล |
| [2404536](https://pubmed.ncbi.nlm.nih.gov/2404536/) | 1990 | RCT | Br J Psychiatry | Isocarboxazid + amitriptyline ในความผิดปกติทางประสาทดื้อยา: ตอบสนองดีเยี่ยม |
| [7234472](https://pubmed.ncbi.nlm.nih.gov/7234472/) | 1981 | Case series | Acta Psychiatr Scand | Amitriptyline ยับยั้ง MAO เล็กน้อย สัมพันธ์กับการควบคุมวิตกกังวลและอาการกลัว |
| [365127](https://pubmed.ncbi.nlm.nih.gov/365127/) | 1978 | Review | Arch Gen Psychiatry | Phenelzine มีประสิทธิผลในซึมเศร้าและ phobic disorders; amitriptyline เป็นตัวเปรียบเทียบ |
| [7717094](https://pubmed.ncbi.nlm.nih.gov/7717094/) | 1995 | Review | Acta Psychiatr Scand | RIMAs (moclobemide) เทียบ amitriptyline ในโรคซึมเศร้า ข้อมูลอ้อมต่อโรคกลัว |
| [23338224](https://pubmed.ncbi.nlm.nih.gov/23338224/) | 1997 | Review | CNS Drugs | Paroxetine สำหรับ panic disorder ± agoraphobia: amitriptyline กล่าวถึงเป็นตัวเปรียบเทียบ |

---

## ข้อบ่งใช้ที่ 3: โรคกลัวที่โล่ง (Agoraphobia)

> **ระดับหลักฐาน: L4** | **คำแนะนำ: Research Question** | **คะแนน TxGNN: 97.27%**

### หลักฐานจากการทดลองทางคลินิก

ปัจจุบันยังไม่มีการลงทะเบียนการทดลองทางคลินิกที่เกี่ยวข้อง

### หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|:---:|------|------|---------|
| [2178909](https://pubmed.ncbi.nlm.nih.gov/2178909/) | 1990 | Review | Drugs | ทบทวน clomipramine ใน OCD/panic disorder; amitriptyline เป็นตัวเปรียบเทียบ |
| [23914085](https://pubmed.ncbi.nlm.nih.gov/23914085/) | 2013 | Cohort | J Neurosci Rural Pract | โรคร่วมทางจิตเวชใน chronic daily headache: amitriptyline ช่วยลดอาการวิตกกังวลร่วม |
| [7717094](https://pubmed.ncbi.nlm.nih.gov/7717094/) | 1995 | Review | Acta Psychiatr Scand | RIMAs เทียบ amitriptyline ในโรคซึมเศร้า มีข้อมูลอ้อมต่อโรควิตกกังวล |
| [23338224](https://pubmed.ncbi.nlm.nih.gov/23338224/) | 1997 | Review | CNS Drugs | Paroxetine สำหรับ panic disorder ± agoraphobia |
| [1356491](https://pubmed.ncbi.nlm.nih.gov/1356491/) | 1992 | Case report | Biol Psychiatry | MDMA กระตุ้น panic disorder + agoraphobia; ตอบสนองต่อยาต้านซึมเศร้า serotonergic |
| [2963053](https://pubmed.ncbi.nlm.nih.gov/2963053/) | 1988 | Review | J Affect Disord | HAM-A: ไม่สามารถแยกฤทธิ์ต้านวิตกกังวลจากฤทธิ์ต้านซึมเศร้าได้ชัดเจน |

> **ข้อสังเกต:** วรรณกรรมส่วนใหญ่ศึกษายาในกลุ่มเดียวกัน (clomipramine) หรือ SSRI (paroxetine) มากกว่า amitriptyline โดยตรง หลักฐานเป็นแบบอ้อม

---

## ข้อบ่งใช้ที่ไม่มีหลักฐานสนับสนุน (ระดับ L5)

ข้อบ่งใช้ต่อไปนี้ได้รับการทำนายจากโมเดล TxGNN เท่านั้น โดยไม่มีการทดลองทางคลินิกหรือวรรณกรรมสนับสนุน:

| อันดับ | ข้อบ่งใช้ | คะแนน TxGNN | เหตุผลที่ Hold |
|:------:|----------|:-----------:|--------------|
| 1 | โรคคอบิดชั่วคราวในทารก (BPTI) | 97.72% | แม้ถือเป็น migraine equivalent แต่ขาดหลักฐานทุกระดับ กลุ่มเป้าหมายเป็นทารกทำให้มีข้อจำกัดด้านความปลอดภัยสูง |
| 5 | กลุ่มอาการ Ohdo | 95.95% | โรคพันธุกรรมหายาก (KAT6B mutation) กลไก monoamine ไม่เกี่ยวข้องกับพยาธิสภาพ |
| 6 | เมลันโคเลีย (Melancholia) | 95.52% | แม้ amitriptyline มีชื่อเสียงว่ามีประสิทธิผลดีในชนิดย่อยนี้ แต่การสืบค้นครั้งนี้ไม่พบวรรณกรรมโดยตรง ต้องสืบค้นเพิ่มเติม |
| 7 | โรคซึมเศร้าชนิดประสาท (Neurotic Depression) | 95.48% | ปัจจุบันจัดเป็นส่วนหนึ่งของ persistent depressive disorder ต้องสืบค้นเพิ่มเติม |
| 10 | กลุ่มอาการเปลือกตาตีบ-บกพร่องทางสติปัญญา ชนิด Ohdo | 94.47% | โรคพันธุกรรมหายากที่เกิดจากความผิดปกติของ chromatin remodeling ไม่มีเหตุผลทางกลไก |

---

## ข้อมูลการวางจำหน่ายในประเทศไทย

Amitriptyline **ยังไม่ได้ขึ้นทะเบียนกับ Thai FDA** และไม่มีใบอนุญาตวางจำหน่ายในประเทศไทย (ณ วันที่ตัดข้อมูล 3 เมษายน 2569)

> **ข้อสังเกตสำคัญ:** แม้ Amitriptyline จะเป็นยาต้านซึมเศร้าที่ใช้แพร่หลายในระดับสากลมากว่า 60 ปี แต่ไม่ปรากฏในฐานข้อมูล Thai FDA การนำไปใช้ในประเทศไทยจะต้องผ่านกระบวนการขึ้นทะเบียนยาก่อน

---

## ข้อพิจารณาด้านความปลอดภัย

> กรุณาดูข้อมูลความปลอดภัยในเอกสารกำกับยา
>
> ข้อมูลคำเตือน ข้อห้ามใช้ และปฏิกิริยาระหว่างยาจาก Thai FDA ยังไม่พร้อมใช้งาน เนื่องจากยาไม่ได้ขึ้นทะเบียนในประเทศไทย

**ข้อมูลความปลอดภัยทั่วไปจากแหล่งสากล (สำหรับอ้างอิง):**

Amitriptyline ในฐานะ TCA มีโปรไฟล์ผลข้างเคียงที่ทราบกันดี ได้แก่:
- **ผลต่อหัวใจ:** พิษต่อหัวใจ (cardiotoxicity) โดยเฉพาะในกรณีเกินขนาด — ยืดช่วง QT, arrhythmia
- **ฤทธิ์ anticholinergic:** ปากแห้ง ท้องผูก ปัสสาวะคั่ง ตามัว
- **ฤทธิ์สงบประสาท:** ง่วงซึม น้ำหนักเพิ่ม
- **ความดันโลหิตต่ำเมื่อเปลี่ยนท่า (orthostatic hypotension)**
- **ความเสี่ยงในเด็กและวัยรุ่น:** เพิ่มความคิดทำร้ายตัวเอง (suicidal ideation)

---

## สรุปและขั้นตอนถัดไป

### สำหรับข้อบ่งใช้กลุ่มซึมเศร้า (MDD, Endogenous Depression, Unipolar Depression)

**การตัดสินใจ: Proceed with Guardrails**

**เหตุผล:**
Amitriptyline เป็นยาต้านซึมเศร้าที่มีหลักฐานระดับ L1 แข็งแกร่งมาก ทั้ง Cochrane systematic review (PMID 23235671) และ Lancet network meta-analysis (PMID 29477251) ยืนยันประสิทธิผลเหนือยาหลอก การที่ TxGNN ทำนายข้อบ่งใช้กลุ่มนี้ถือเป็นการ validate ความถูกต้องของโมเดล อย่างไรก็ตาม ยาไม่ได้ขึ้นทะเบียนในไทย ซึ่งเป็นอุปสรรคหลักต่อการนำไปใช้

**หากต้องการดำเนินการต่อต้อง:**
- ดำเนินการขึ้นทะเบียนยากับ Thai FDA
- จัดหาข้อมูลเอกสารกำกับยา (คำเตือน ข้อห้ามใช้ ปฏิกิริยาระหว่างยา)
- ข้อมูลกลไกการออกฤทธิ์ (MOA) โดยละเอียดจาก DrugBank

### สำหรับข้อบ่งใช้กลุ่มวิตกกังวล/กลัว (Agoraphobia, Phobic Disorder)

**การตัดสินใจ: Hold — ตั้งเป็น Research Question**

**เหตุผล:**
หลักฐานในระดับ L4 ส่วนใหญ่เป็นการศึกษาเชิงสังเกตหรือทบทวนวรรณกรรม โดยข้อมูลตรงสำหรับ amitriptyline มีจำกัด ส่วนใหญ่ศึกษายาอื่นในกลุ่มเดียวกัน (clomipramine, SSRI, MAOI)

**หากต้องการดำเนินการต่อต้อง:**
- สืบค้นวรรณกรรมเพิ่มเติมเฉพาะ amitriptyline ใน phobic/anxiety disorders
- พิจารณาการทดลองทางคลินิกนำร่อง (pilot study)

### สำหรับข้อบ่งใช้กลุ่มโรคหายาก (BPTI, Ohdo Syndrome, Blepharophimosis-ID)

**การตัดสินใจ: Hold**

**เหตุผล:**
ขาดเหตุผลเชิงกลไกและหลักฐานทุกระดับ การทำนายอาจเกิดจาก noise ในโมเดล TxGNN ไม่แนะนำให้ดำเนินการต่อ

---

> ⚠️ **ข้อจำกัดสำคัญ:** ผลลัพธ์นี้เป็นการวิเคราะห์เชิงคอมพิวเตอร์เพื่อการวิจัยเท่านั้น ไม่ถือเป็นคำแนะนำทางการแพทย์ การนำยาเก่ามาใช้ในข้อบ่งใช้ใหม่ต้องผ่านการทดลองทางคลินิกและได้รับการอนุมัติจากหน่วยงานกำกับดูแลก่อนนำไปใช้จริง
---

