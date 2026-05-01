---
layout: default
title: Atorvastatin
parent: การคาดการณ์จากโมเดล (L5)
nav_order: 22
evidence_level: L5
indication_count: 6
---

# Atorvastatin
{: .fs-9 }

ระดับหลักฐาน: **L5** | ข้อบ่งใช้ที่ทำนาย: **6** รายการ
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

# Atorvastatin: จากยาลดไขมันในเลือดสู่ภาวะคอเลสเตอรอลสูงทางพันธุกรรม

## สรุปสั้นๆ

Atorvastatin เป็นยาลดไขมันกลุ่ม statin (HMG-CoA reductase inhibitor) ที่ใช้กันแพร่หลายทั่วโลกในการรักษาภาวะไขมันในเลือดสูงและลดความเสี่ยงโรคหัวใจและหลอดเลือด
โมเดล TxGNN คาดการณ์ว่าอาจมีผลต่อ **ภาวะคอเลสเตอรอลสูงทางพันธุกรรม (Familial Hypercholesterolemia)** เป็นอันดับแรก และมีข้อบ่งใช้ใหม่ที่ทำนายเพิ่มเติมอีก 5 รายการ
ข้อบ่งใช้อันดับ 1 มี **การทดลองทางคลินิก 34 รายการ** และ **วรรณกรรม 19 ฉบับ** สนับสนุน ถือเป็นหลักฐานระดับ L1 (สูงสุด)

---

## ภาพรวมฉบับย่อ

| รายการ | เนื้อหา |
|------|------|
| ข้อบ่งใช้เดิม | ไม่พบข้อมูลที่ได้รับอนุมัติในฐานข้อมูล อย. ไทย (ระดับสากล: ภาวะไขมันในเลือดสูง, ลดความเสี่ยงโรคหัวใจและหลอดเลือด) |
| ข้อบ่งใช้ใหม่ที่ทำนาย | ภาวะคอเลสเตอรอลสูงทางพันธุกรรม (Familial Hypercholesterolemia) |
| คะแนนการทำนาย TxGNN | 99.42% |
| ระดับหลักฐาน | L1 (มี ≥2 Phase 3 RCT เสร็จสมบูรณ์) |
| สถานะการวางจำหน่ายในไทย | ✗ ไม่พบข้อมูลการวางจำหน่าย |
| จำนวนใบอนุญาต | 0 รายการ |
| คำแนะนำในการตัดสินใจ | Proceed with Guardrails |

---

## ภาพรวมข้อบ่งใช้ใหม่ทั้งหมดที่ทำนาย

| อันดับ | ชื่อโรค | คะแนน TxGNN | ระดับหลักฐาน | การทดลอง | วรรณกรรม | คำแนะนำ |
|:---:|------|:---:|:---:|:---:|:---:|------|
| 1 | Familial Hypercholesterolemia | 99.42% | L1 | 34 | 19 | Proceed with Guardrails |
| 2 | HIV Infectious Disease | 99.31% | L2 | 22 | 20 | Research Question |
| 3 | Brain Stem Infarction | 99.31% | L3 | 2 | 5 | Research Question |
| 4 | CETP Deficiency | 99.25% | L4 | 0 | 5 | Hold |
| 5 | Hypercholesterolemia (CYP7A1 Deficiency) | 99.20% | L4 | 0 | 3 | Hold |
| 6 | Neurodevelopmental Disorder (Ataxic Gait, Absent Speech) | 99.13% | L5 | 0 | 0 | Hold |

---

## ข้อบ่งใช้ที่ 1: Familial Hypercholesterolemia

### ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

Atorvastatin ยับยั้งเอนไซม์ HMG-CoA reductase ซึ่งเป็นเอนไซม์สำคัญในการสังเคราะห์คอเลสเตอรอลในตับ เมื่อการสังเคราะห์คอเลสเตอรอลลดลง ตับจะตอบสนองด้วยการเพิ่มการแสดงออกของ LDL receptor บนผิวเซลล์ เพื่อดึง LDL-cholesterol จากกระแสเลือดเข้าสู่ตับมากขึ้น

ภาวะ Familial Hypercholesterolemia (FH) เกิดจากความผิดปกติทางพันธุกรรมที่ทำให้ LDL receptor ทำงานบกพร่อง (ในรูปแบบ Heterozygous) หรือแทบไม่ทำงาน (ในรูปแบบ Homozygous) ส่งผลให้ระดับ LDL-cholesterol ในเลือดสูงผิดปกติตั้งแต่เกิด และเพิ่มความเสี่ยงโรคหลอดเลือดหัวใจอย่างมาก กลไกของ atorvastatin ที่กระตุ้นการแสดงออกของ LDL receptor ตรงเป้าหมายกับพยาธิสภาพหลักของ FH โดยตรง

ในระดับสากล atorvastatin เป็นยาตัวเลือกแรก (first-line therapy) สำหรับ FH ตามแนวทาง AACE/ACE, AHA/ACC และองค์กรทางการแพทย์หลายแห่ง มีการทดลองทางคลินิก Phase 3 จำนวนมากที่ยืนยันประสิทธิผลทั้งใน HeFH และ HoFH รวมถึงในกลุ่มเด็กและวัยรุ่น

### หลักฐานจากการทดลองทางคลินิก

| หมายเลขการทดลอง | ระยะ | สถานะ | ผู้เข้าร่วม | ผลลัพธ์หลัก |
|---------|------|------|:---:|---------|
| [NCT00136981](https://clinicaltrials.gov/study/NCT00136981) | Phase 3 | เสร็จสิ้น | 800 | ประเมินผลต้านหลอดเลือดแข็งของ torcetrapib/atorvastatin ด้วยอัลตราซาวด์หลอดเลือดคอใน HeFH 24 เดือน |
| [NCT03867318](https://clinicaltrials.gov/study/NCT03867318) | Phase 3 | เสร็จสิ้น | 621 | ประสิทธิผลและความปลอดภัยของ ezetimibe ร่วมกับ atorvastatin ในผู้ป่วย HeFH หรือโรคหลอดเลือดหัวใจ |
| [NCT03882996](https://clinicaltrials.gov/study/NCT03882996) | Phase 3 | เสร็จสิ้น | 432 | ความปลอดภัยระยะยาว (12 เดือน) ของ ezetimibe ร่วมกับ atorvastatin 10-80 mg ในผู้ป่วย HeFH |
| [NCT00134485](https://clinicaltrials.gov/study/NCT00134485) | Phase 3 | เสร็จสิ้น | 400 | เปรียบเทียบ torcetrapib/atorvastatin กับ atorvastatin เดี่ยวใน HeFH (6 เดือน) |
| [NCT01730040](https://clinicaltrials.gov/study/NCT01730040) | Phase 3 | เสร็จสิ้น | 355 | เปรียบเทียบ alirocumab, ezetimibe, เพิ่มขนาด atorvastatin และเปลี่ยนเป็น rosuvastatin ในผู้ป่วย HeFH |
| [NCT00827606](https://clinicaltrials.gov/study/NCT00827606) | Phase 3 | เสร็จสิ้น | 272 | ประสิทธิผลการลดคอเลสเตอรอลและการเจริญเติบโตในเด็ก HeFH ที่ได้รับ atorvastatin นาน 3 ปี |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Phase 3 | เสร็จสิ้น | 153 | RCT double-blind ประเมิน alirocumab ในเด็ก HeFH อายุ 8-17 ปีบน statin therapy |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | เสร็จสิ้น | 50 | ประสิทธิผลของ ezetimibe ร่วมกับ atorvastatin หรือ simvastatin ใน Homozygous FH |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | เสร็จสิ้น | 44 | ความปลอดภัยระยะยาว (24 เดือน) ของ ezetimibe + atorvastatin/simvastatin ใน HoFH |
| [NCT00739999](https://clinicaltrials.gov/study/NCT00739999) | Phase 1 | เสร็จสิ้น | 39 | เภสัชจลนศาสตร์ เภสัชพลศาสตร์ และความปลอดภัยของ atorvastatin ในเด็กและวัยรุ่น HeFH |

### หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|:---:|------|------|---------|
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Cohort | J Am Coll Cardiol | Statin ลดโรคหลอดเลือดหัวใจและอัตราการเสียชีวิตในผู้ป่วย HeFH อย่างมีนัยสำคัญ |
| [9301631](https://pubmed.ncbi.nlm.nih.gov/9301631/) | 1997 | Clinical trial | Arterioscler Thromb Vasc Biol | Atorvastatin 40-80 mg ลด LDL-C ได้อย่างมีประสิทธิภาพในผู้ป่วย FH ที่ได้รับการพิสูจน์ทางพันธุกรรม |
| [27678432](https://pubmed.ncbi.nlm.nih.gov/27678432/) | 2016 | Clinical trial | J Clin Lipidol | Atorvastatin มีประสิทธิผลและปลอดภัยในเด็ก HeFH ตลอดระยะเวลา 3 ปี |
| [22957727](https://pubmed.ncbi.nlm.nih.gov/22957727/) | 2013 | Clinical trial | Echocardiography | Atorvastatin ปรับปรุงการไหลเวียนเลือดในหัวใจและหลอดเลือดส่วนปลายในผู้ป่วย FH |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Comparative | NMCD | เปรียบเทียบ atorvastatin กับ simvastatin ใน HeFH; atorvastatin มีประสิทธิภาพดีกว่าในการบรรลุเป้าหมาย LDL-C |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review | Curr Atheroscler Rep | ทบทวนการรักษา HoFH ใหม่ล่าสุด รวมถึงยาและแนวทางที่พัฒนาขึ้น |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | แนวทาง AACE/ACE สำหรับการจัดการภาวะไขมันผิดปกติและป้องกันโรคหัวใจ |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | Review | Ann Pharmacother | ทบทวนประสิทธิผลและความปลอดภัยของ atorvastatin ในภาวะไขมันผิดปกติ |
| [15199433](https://pubmed.ncbi.nlm.nih.gov/15199433/) | 2004 | Review | Semin Vasc Med | การวินิจฉัย การรักษา และการจัดการ FH ในเด็ก รวมถึงเกณฑ์ LDL-C สำหรับการวินิจฉัย |
| [35361995](https://pubmed.ncbi.nlm.nih.gov/35361995/) | 2022 | Review | Pharmacogenomics J | การผสมผสานการศึกษาพันธุกรรม FH กับเภสัชพันธุศาสตร์ของ statin เพื่อการแพทย์เฉพาะบุคคล |

---

## ข้อบ่งใช้ที่ 2: HIV Infectious Disease

### ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

Atorvastatin นอกจากลดไขมันแล้ว ยังมีฤทธิ์ต้านการอักเสบและปรับภูมิคุ้มกัน (pleiotropic effects) ผ่านการยับยั้งวิถี mevalonate pathway ผู้ป่วย HIV ที่ได้รับยาต้านไวรัส (ART) มักประสบปัญหาภาวะภูมิคุ้มกันถูกกระตุ้นเรื้อรัง (chronic immune activation) และ T-cell exhaustion ซึ่งนำไปสู่โรคหลอดเลือดหัวใจเร็วขึ้น โรคไตเรื้อรัง และภาวะเสื่อมถอยก่อนวัย

นอกจากนี้ ยา ART โดยเฉพาะกลุ่ม protease inhibitors (PIs) มักทำให้เกิดภาวะไขมันในเลือดผิดปกติ Atorvastatin จึงมีบทบาทสองทาง: ลดไขมันที่ผิดปกติจากยาต้านไวรัส และลดการอักเสบเรื้อรังที่เป็นตัวขับเคลื่อนโรคร่วมของผู้ป่วย HIV อย่างไรก็ตาม ต้องระวังปฏิกิริยาระหว่างยา เนื่องจาก atorvastatin ถูกเมตาบอไลซ์โดย CYP3A4 ซึ่ง PIs หลายตัวยับยั้งเอนไซม์นี้

### หลักฐานจากการทดลองทางคลินิก

| หมายเลขการทดลอง | ระยะ | สถานะ | ผู้เข้าร่วม | ผลลัพธ์หลัก |
|---------|------|------|:---:|---------|
| [NCT03037372](https://clinicaltrials.gov/study/NCT03037372) | Phase 3 | ไม่ทราบ | 320 | เปรียบเทียบ atorvastatin vs rosuvastatin ในการลด immune activation เป็นเวลา 36 เดือน |
| [NCT01351025](https://clinicaltrials.gov/study/NCT01351025) | Phase 2 | เสร็จสิ้น | 98 | ผลของ atorvastatin ต่อ biomarkers ของการอักเสบ การแข็งตัวของเลือด และ T-cell activation ในผู้ป่วย HIV |
| [NCT04101136](https://clinicaltrials.gov/study/NCT04101136) | N/A | ไม่ทราบ | 80 | Atorvastatin ลด subclinical atherosclerosis ในผู้ป่วย HIV ที่ควบคุมไวรัสได้ร่วมกับ CMV |
| [NCT00000941](https://clinicaltrials.gov/study/NCT00000941) | Phase 1 | เสร็จสิ้น | 56 | ปฏิกิริยาทางเภสัชจลนศาสตร์ระหว่าง protease inhibitors กับ atorvastatin, pravastatin, simvastatin |
| [NCT02081638](https://clinicaltrials.gov/study/NCT02081638) | Phase 2 | เสร็จสิ้น | 53 | เปรียบเทียบ statin กับ aspirin ต่อการอักเสบและการแข็งตัวของเลือดใน elite controllers และ ART-treated HIV |
| [NCT02577042](https://clinicaltrials.gov/study/NCT02577042) | Phase 4 | เสร็จสิ้น | 42 | Atorvastatin ลดภาวะ "inflaming" (การอักเสบจากความชรา) ในผู้ป่วย HIV อายุ >45 ปี |
| [NCT00965185](https://clinicaltrials.gov/study/NCT00965185) | N/A | เสร็จสิ้น | 40 | Statin ลดการอักเสบของ plaque ชะลอ plaque progression และปรับปรุง endothelial function ในผู้ป่วย HIV |
| [NCT01766076](https://clinicaltrials.gov/study/NCT01766076) | Phase 3 | เสร็จสิ้น | 30 | Atorvastatin เป็นยาเสริม ART ช่วยลด immune activation 25% ในผู้ที่ CD4 ฟื้นไม่เพียงพอ (แอฟริกา) |
| [NCT00367458](https://clinicaltrials.gov/study/NCT00367458) | Phase 2 | เสร็จสิ้น | 24 | RCT ศึกษาผลของ atorvastatin ต่อ HIV viral load และ immune activation ในผู้ไม่ได้รับ ART |
| [NCT00663234](https://clinicaltrials.gov/study/NCT00663234) | Phase 1/2 | ยุติก่อนกำหนด | 28 | ความปลอดภัยและประสิทธิผลของ atorvastatin สำหรับ PI-associated LDL สูงในเด็กและวัยรุ่น HIV |

### หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|:---:|------|------|---------|
| [37450602](https://pubmed.ncbi.nlm.nih.gov/37450602/) | 2023 | RCT | AIDS | Atorvastatin vs aspirin ใน elite controllers และ ART-treated: atorvastatin ลดการอักเสบ |
| [18991624](https://pubmed.ncbi.nlm.nih.gov/18991624/) | 2008 | RCT | Curr HIV Res | เปรียบเทียบ rosuvastatin, pravastatin, atorvastatin สำหรับ PI-associated hypercholesterolemia |
| [25574964](https://pubmed.ncbi.nlm.nih.gov/25574964/) | 2014 | Retrospective | AIDS | Atorvastatin ลด CD8 T-cell activation (HLA-DR, CD38) และ exhaustion (TIM-3, PD-1) ในผู้ป่วย HIV |
| [25441397](https://pubmed.ncbi.nlm.nih.gov/25441397/) | 2015 | Crossover trial | Trop Med Int Health | Atorvastatin ลด T-cell activation ในผู้ป่วย HIV-Uganda ที่ CD4 ฟื้นไม่เพียงพอ |
| [36549898](https://pubmed.ncbi.nlm.nih.gov/36549898/) | 2023 | Cohort | HIV Med | ประเมิน atorvastatin exposure, vitamin D และผลลัพธ์ด้านไขมันในผู้ป่วย HIV บน boosted PIs |
| [31126301](https://pubmed.ncbi.nlm.nih.gov/31126301/) | 2019 | Review | AIDS Res Ther | บทบาท statin และ aspirin ในป้องกันโรคหัวใจในผู้ป่วย HIV: ข้อถกเถียงและความต้องการที่ยังไม่ได้รับการตอบสนอง |
| [29770749](https://pubmed.ncbi.nlm.nih.gov/29770749/) | 2018 | Cohort | HIV Clin Trials | Atorvastatin และ rosuvastatin ช่วยรักษาการทำงานของไตในผู้ป่วย HIV ที่มีโรคไตเรื้อรัง |
| [29804227](https://pubmed.ncbi.nlm.nih.gov/29804227/) | 2018 | Review | Curr Infect Dis Rep | ทบทวนประโยชน์และความเสี่ยงของ statin ในผู้ป่วย HIV: ลดความเสี่ยง CVD 1.5-2 เท่า |
| [41774493](https://pubmed.ncbi.nlm.nih.gov/41774493/) | 2026 | Animal | JCI Insight | Atorvastatin ยับยั้ง cardiac fibrosis จาก HIV/ART ในหนูผ่าน platelet TGFβ1 signaling |
| [27192322](https://pubmed.ncbi.nlm.nih.gov/27192322/) | 2016 | Review | Expert Opin Pharmacother | ยารักษาภาวะเมตาบอลิกผิดปกติที่เกี่ยวข้องกับ HIV และ cART |

---

## ข้อบ่งใช้ที่ 3: Brain Stem Infarction

### ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

Atorvastatin มีคุณสมบัติหลายประการที่อาจเป็นประโยชน์ต่อโรคหลอดเลือดสมอง ได้แก่ การปรับปรุงการทำงานของ endothelium ทำให้ plaque มีเสถียรภาพมากขึ้น ลดการอักเสบของหลอดเลือด และอาจส่งเสริมการฟื้นตัวของเซลล์ประสาทผ่านการกระตุ้น eNOS และ tPA อย่างไรก็ตาม หลักฐานเฉพาะสำหรับภาวะสมองส่วนก้านสมองขาดเลือด (brain stem infarction) ยังมีจำกัดมาก มีเพียง 2 การทดลองทางคลินิก (ซึ่งศึกษาโรคหลอดเลือดสมองทั่วไป ไม่ได้เจาะจงก้านสมอง) และ 5 วรรณกรรม ส่วนใหญ่เป็น case reports

### หลักฐานจากการทดลองทางคลินิก

| หมายเลขการทดลอง | ระยะ | สถานะ | ผู้เข้าร่วม | ผลลัพธ์หลัก |
|---------|------|------|:---:|---------|
| [NCT02225834](https://clinicaltrials.gov/study/NCT02225834) | Phase 4 | เสร็จสิ้น | 50 | ผลของ atorvastatin ต่อ markers ภูมิคุ้มกัน/การอักเสบในระยะเฉียบพลันของโรคหลอดเลือดสมอง (LAAS) |
| [NCT03176498](https://clinicaltrials.gov/study/NCT03176498) | Phase 1/2 | ระงับชั่วคราว | 40 | เซลล์ต้นกำเนิดสำหรับผู้ป่วยสมองขาดเลือด (atorvastatin ไม่ใช่ยาวิจัยหลัก) |

### หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|:---:|------|------|---------|
| [30073508](https://pubmed.ncbi.nlm.nih.gov/30073508/) | 2019 | In vitro | Mol Neurobiol | Atorvastatin ฟื้นฟูเซลล์ต้นกำเนิดประสาทที่ได้รับบาดเจ็บจากภาวะขาดออกซิเจน ผ่าน PI3K/Akt และ ERK |
| [29592977](https://pubmed.ncbi.nlm.nih.gov/29592977/) | 2018 | Case report | BMJ Case Rep | Artery of Percheron stroke: bilateral medial thalamic infarcts ใน myeloproliferative neoplasm |
| [25754163](https://pubmed.ncbi.nlm.nih.gov/25754163/) | 2015 | Case report | BMJ Case Rep | โรคหลอดเลือดสมองซ้ำจาก polycythaemia vera: acute และ chronic infarctions ในก้านสมองและสมองใหญ่ |

---

## ข้อบ่งใช้ที่ 4: Cholesterol-Ester Transfer Protein (CETP) Deficiency

### ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

CETP deficiency ทำให้เกิดภาวะ HDL สูงผิดปกติ เนื่องจาก cholesteryl ester ไม่สามารถถ่ายโอนจาก HDL ไปยัง apoB-containing lipoproteins ได้ Atorvastatin อาจมีบทบาทในการจัดการสมดุลไขมันโดยรวมผ่านการลด LDL-C แต่ความจำเป็นในการรักษา CETP deficiency ยังเป็นที่ถกเถียง เนื่องจาก HDL สูงจากภาวะนี้ไม่ได้หมายความว่าเพิ่มความเสี่ยงโรคหัวใจเสมอไป ปัจจุบันไม่มีการทดลองทางคลินิกที่ศึกษาโดยตรง

### หลักฐานจากการทดลองทางคลินิก

ปัจจุบันยังไม่มีการลงทะเบียนการทดลองทางคลินิกที่เกี่ยวข้อง

### หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|:---:|------|------|---------|
| [21804130](https://pubmed.ncbi.nlm.nih.gov/21804130/) | 2011 | RCT | Circulation | Torcetrapib (CETP inhibitor) + atorvastatin มีผลต่อ glucose homeostasis ในทิศทางที่เป็นประโยชน์ |
| [18331394](https://pubmed.ncbi.nlm.nih.gov/18331394/) | 2008 | Cohort | Basic Clin Pharmacol Toxicol | CETP TaqI B polymorphism มีผลต่อการตอบสนองต่อ atorvastatin ในผู้ป่วยไขมันผิดปกติ |
| [18414186](https://pubmed.ncbi.nlm.nih.gov/18414186/) | 2008 | Review | Cardiol Rev | ทบทวน HDL metabolism และ CETP inhibition รวมถึงบทบาทของ statin ในการเพิ่ม HDL เล็กน้อย |
| [17169247](https://pubmed.ncbi.nlm.nih.gov/17169247/) | 2007 | Review | Curr Atheroscler Rep | Torcetrapib (CETP inhibitor) ร่วมกับ atorvastatin: อนาคตการลดความเสี่ยง CHD |
| [31189741](https://pubmed.ncbi.nlm.nih.gov/31189741/) | 2019 | Animal | Biosci Rep | ผลของ atorvastatin ขนาดต่างๆ ต่อ CETP และ lipid parameters ในหนู T2DM |

---

## ข้อบ่งใช้ที่ 5: Hypercholesterolemia Due to CYP7A1 Deficiency

### ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

CYP7A1 (cholesterol 7α-hydroxylase) เป็นเอนไซม์สำคัญในการเปลี่ยนคอเลสเตอรอลเป็นกรดน้ำดี เมื่อเอนไซม์นี้ขาด คอเลสเตอรอลจะไม่สามารถถูกกำจัดผ่านทางน้ำดีได้เพียงพอ ส่งผลให้ LDL-C สูง Atorvastatin สามารถลด LDL-C ผ่านกลไกอื่น (เพิ่ม LDL receptor) ซึ่งอาจชดเชยความบกพร่องของการกำจัดคอเลสเตอรอลทางน้ำดี แต่ปัจจุบันมีหลักฐานเฉพาะในสัตว์ทดลอง ยังไม่มีการศึกษาในมนุษย์

### หลักฐานจากการทดลองทางคลินิก

ปัจจุบันยังไม่มีการลงทะเบียนการทดลองทางคลินิกที่เกี่ยวข้อง

### หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|:---:|------|------|---------|
| [11387232](https://pubmed.ncbi.nlm.nih.gov/11387232/) | 2001 | Animal | FASEB J | Growth hormone ลด cholesterol ในหนู LDLR-deficient ผ่าน CYP7A1 upregulation |
| [12810816](https://pubmed.ncbi.nlm.nih.gov/12810816/) | 2003 | Animal | J Lipid Res | การยับยั้ง ASBT เพิ่มการสังเคราะห์กรดน้ำดีและลด atherosclerosis ใน apoE-/- mice |
| [12475897](https://pubmed.ncbi.nlm.nih.gov/12475897/) | 2003 | Animal | FASEB J | การเพิ่ม fecal bile acid loss ลด cholesterol ใน LDLR/apoE deficiency ผ่าน CYP7A1 |

---

## ข้อบ่งใช้ที่ 6: Neurodevelopmental Disorder With Ataxic Gait, Absent Speech, and Decreased Cortical White Matter

### ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

ปัจจุบันไม่มีหลักฐานที่สนับสนุนความเชื่อมโยงระหว่าง atorvastatin กับโรคนี้โดยตรง เป็นเพียงการคาดการณ์จากโมเดล TxGNN เท่านั้น มีสมมติฐานว่าฤทธิ์ pleiotropic ของ statin อาจมีบทบาทในการส่งเสริมการสร้างไมอีลิน (myelination) และลดการอักเสบของระบบประสาท ซึ่งอาจเกี่ยวข้องกับพยาธิสภาพของ white matter ที่ลดลง แต่ยังไม่มีการศึกษาใดๆ สนับสนุนแนวคิดนี้

### หลักฐานจากการทดลองทางคลินิก

ปัจจุบันยังไม่มีการลงทะเบียนการทดลองทางคลินิกที่เกี่ยวข้อง

### หลักฐานจากวรรณกรรม

ปัจจุบันยังไม่มีวรรณกรรมที่เกี่ยวข้อง

---

## ข้อมูลการวางจำหน่ายในประเทศไทย

ไม่พบข้อมูลการขึ้นทะเบียนของ Atorvastatin ในฐานข้อมูล อย. ไทย (สืบค้นเมื่อ 10 มีนาคม 2569)

> **หมายเหตุ:** Atorvastatin เป็นยาที่ใช้อย่างแพร่หลายทั่วโลกภายใต้ชื่อการค้าหลายชื่อ (เช่น Lipitor) ผลลัพธ์ที่ไม่พบข้อมูลนี้อาจเกิดจากข้อจำกัดในการสืบค้น เช่น การขึ้นทะเบียนภายใต้ชื่อการค้าหรือสูตรผสมที่แตกต่างออกไป แนะนำให้ตรวจสอบกับฐานข้อมูล อย. โดยตรง

---

## ข้อพิจารณาด้านความปลอดภัย

> กรุณาดูข้อมูลความปลอดภัยในเอกสารกำกับยา
>
> **ข้อมูลเพิ่มเติมจาก DrugBank (DB01076):** ปัจจุบันขาดข้อมูลกลไกการออกฤทธิ์ (MOA) โดยละเอียด คำเตือนหลัก และข้อห้ามใช้ในระบบ แนะนำให้สืบค้นเพิ่มเติมจาก DrugBank API และเอกสารกำกับยาจาก อย.

---

## สรุปและขั้นตอนถัดไป

### ข้อบ่งใช้ที่ 1: Familial Hypercholesterolemia

**การตัดสินใจ: Proceed with Guardrails**

**เหตุผล:**
Atorvastatin เป็นยาตัวเลือกแรกสำหรับ FH ตามแนวทางเวชปฏิบัติสากล มี Phase 3 RCT เสร็จสมบูรณ์มากกว่า 10 รายการ ครอบคลุมทั้ง HeFH และ HoFH รวมถึงกลุ่มเด็กและวัยรุ่น หลักฐานอยู่ในระดับ L1 สูงสุด

**หากต้องการดำเนินการต่อต้อง:**
- ตรวจสอบสถานะการขึ้นทะเบียนในประเทศไทยอีกครั้งโดยสืบค้นชื่อการค้าภาษาไทย
- สืบค้นข้อมูลกลไกการออกฤทธิ์ (MOA) จาก DrugBank API
- สืบค้นคำเตือน ข้อห้ามใช้ และปฏิกิริยาระหว่างยาจากเอกสารกำกับยา อย.

---

### ข้อบ่งใช้ที่ 2: HIV Infectious Disease

**การตัดสินใจ: Research Question**

**เหตุผล:**
มีหลักฐานระดับ L2 จากหลายการศึกษาที่สนับสนุนบทบาทของ atorvastatin ในการลดการอักเสบเรื้อรังและจัดการภาวะไขมันผิดปกติจาก ART แต่ยังไม่มี Phase 3 RCT ขนาดใหญ่ที่เสร็จสมบูรณ์สำหรับผลลัพธ์ทางคลินิกหลัก

**หากต้องการดำเนินการต่อต้อง:**
- ติดตามผลการทดลอง NCT03037372 (n=320, 36 เดือน) ซึ่งเปรียบเทียบ atorvastatin vs rosuvastatin โดยตรง
- ประเมินปฏิกิริยาระหว่างยากับ ART regimens ที่ใช้ในประเทศไทย (โดยเฉพาะ CYP3A4 interactions กับ PIs)
- วิเคราะห์ความคุ้มค่าของการเพิ่ม statin ใน ART regimen มาตรฐาน

---

### ข้อบ่งใช้ที่ 3: Brain Stem Infarction

**การตัดสินใจ: Research Question**

**เหตุผล:**
หลักฐานระดับ L3 มีเพียง 1 การทดลอง Phase 4 (n=50) ที่ศึกษาโรคหลอดเลือดสมองทั่วไป ไม่ได้เจาะจงก้านสมอง และวรรณกรรมส่วนใหญ่เป็น case reports หรือ in vitro จำเป็นต้องมีการศึกษาทางคลินิกที่มุ่งเป้าก่อน

---

### ข้อบ่งใช้ที่ 4-6: CETP Deficiency / CYP7A1 Deficiency / Neurodevelopmental Disorder

**การตัดสินใจ: Hold**

**เหตุผล:**
ข้อบ่งใช้ที่ 4-5 มีหลักฐานระดับ L4 (มีเฉพาะการศึกษาก่อนคลินิก/กลไก) และข้อบ่งใช้ที่ 6 มีหลักฐานระดับ L5 (มีเฉพาะการทำนายจากโมเดล ไม่มีการศึกษาจริงใดๆ) ยังไม่เพียงพอต่อการดำเนินการทางคลินิก ต้องรอหลักฐานจากการศึกษาในมนุษย์ก่อน

---

> ⚠️ **ข้อจำกัดของรายงาน:** ผลการวิเคราะห์นี้มีช่องว่างข้อมูลสำคัญ 2 รายการ ได้แก่ (1) ข้อมูลคำเตือน/ข้อห้ามใช้จากเอกสารกำกับยา อย. และ (2) ข้อมูลกลไกการออกฤทธิ์โดยละเอียดจาก DrugBank ซึ่งจำเป็นต้องได้รับการเติมเต็มก่อนเข้าสู่ขั้นตอนการประเมินความปลอดภัย (S1) ได้อย่างสมบูรณ์
>
> ⚠️ **ผลการวิจัยนี้เป็นเพียงข้อมูลสำหรับการวิจัยเท่านั้น ไม่ถือเป็นคำแนะนำทางการแพทย์** การนำยาเก่ามาใช้ใหม่ต้องผ่านการทดลองทางคลินิกและได้รับการอนุมัติจากหน่วยงานกำกับดูแลก่อนนำไปใช้จริง
---

