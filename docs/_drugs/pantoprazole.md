---
layout: default
title: Pantoprazole
parent: หลักฐานระดับสูง (L1-L2)
nav_order: 122
evidence_level: L1
indication_count: 6
---

# Pantoprazole
{: .fs-9 }

ระดับหลักฐาน: **L1** | ข้อบ่งใช้ที่ทำนาย: **6** รายการ
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

ใช้ `txgnn-pipeline` เป็น reference สำหรับรูปแบบรายงานนี้ ขณะนี้กำลังสร้างรายงานจาก Evidence Pack ที่ให้มา

---

# Pantoprazole: จากกรดไหลย้อนสู่แผลเพปติกในระยะกำเริบ

## สรุปสั้นๆ

Pantoprazole เป็นยายับยั้งโปรตอนปั๊ม (Proton Pump Inhibitor) ที่ใช้รักษากรดไหลย้อนและหลอดอาหารอักเสบกัดกร่อน โดยปัจจุบันยังไม่มีทะเบียนยาในประเทศไทย
โมเดล TxGNN คาดการณ์ว่ามีศักยภาพในการรักษา **แผลเพปติกในระยะกำเริบ (Active Peptic Ulcer Disease)**
ปัจจุบันมี **การทดลองทางคลินิก 3 รายการ** และ **วรรณกรรม 19 ฉบับ** สนับสนุนแนวทางนี้

---

## ภาพรวมฉบับย่อ

| รายการ | เนื้อหา |
|------|------|
| ข้อบ่งใช้เดิม | การรักษากรดไหลย้อน/หลอดอาหารอักเสบกัดกร่อน (ตามทะเบียน FDA สหรัฐ) |
| ข้อบ่งใช้ใหม่ที่ทำนาย | แผลเพปติกในระยะกำเริบ (Active Peptic Ulcer Disease) |
| คะแนนการทำนาย TxGNN | 99.69% |
| ระดับหลักฐาน | L1 |
| สถานะการวางจำหน่ายในไทย | ✗ ยังไม่ได้ขึ้นทะเบียนในประเทศไทย |
| จำนวนใบอนุญาต | 0 รายการ |
| คำแนะนำในการตัดสินใจ | Proceed with Guardrails |

---

## ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

ปัจจุบันยังขาดข้อมูลกลไกการออกฤทธิ์อย่างเป็นทางการจากฐานข้อมูล DrugBank อย่างไรก็ตาม จากข้อมูลที่ทราบ Pantoprazole จัดเป็นยาในกลุ่ม Proton Pump Inhibitor ที่ออกฤทธิ์โดยจับอย่างถาวรแบบ irreversible covalent binding กับเอนไซม์ H⁺/K⁺-ATPase ในเซลล์ผนังกระเพาะอาหาร (gastric parietal cells) ยับยั้งการหลั่งกรดในขั้นตอนสุดท้าย ทำให้ pH ภายในกระเพาะอาหารเพิ่มสูงขึ้นอย่างต่อเนื่องและยาวนานกว่า PPI รุ่นก่อนหน้า

แผลเพปติกเกิดจากความไม่สมดุลระหว่างปัจจัยทำลาย (กรด เอนไซม์เพปซิน เชื้อ H. pylori) และกลไกป้องกันเยื่อเมือก การรักษา pH > 3–4 อย่างต่อเนื่องสร้างสภาวะที่เหมาะต่อการฟื้นตัวของเยื่อเมือก นอกจากนี้ Pantoprazole ยังเป็นส่วนประกอบหลักของ Triple Therapy ที่ใช้กำจัดเชื้อ H. pylori ซึ่งเป็นสาเหตุสำคัญของแผลเพปติกทั่วโลก กลไกการออกฤทธิ์จึงตรงกับพยาธิสรีรวิทยาของโรคโดยตรง

ประสิทธิผลได้รับการยืนยันจาก Phase 3 RCT ที่เสร็จสมบูรณ์และวรรณกรรมมากกว่า 19 ฉบับ ครอบคลุมทั้งการกำจัด H. pylori, การป้องกันการกลับมาเลือดออกซ้ำหลังการส่องกล้อง, และการเปรียบเทียบกับยาอื่นในกลุ่มเดียวกัน การคาดการณ์จาก TxGNN จึงสอดคล้องกับหลักฐานทางคลินิกในระดับสูงสุด

---

## หลักฐานจากการทดลองทางคลินิก

| หมายเลขการทดลอง | ระยะ | สถานะ | จำนวนผู้เข้าร่วม | ผลลัพธ์หลัก |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | เสร็จสิ้น | 323 | RCT หลายศูนย์ แบบ double-blind เปรียบเทียบ Ilaprazole กับ Pantoprazole Triple Therapy 7 วัน ในผู้ป่วย H. pylori-positive gastric/duodenal ulcer — ประเมินอัตราการกำจัดเชื้อและความปลอดภัย |
| [NCT02197039](https://clinicaltrials.gov/study/NCT02197039) | N/A | เสร็จสิ้น | 316 | ศึกษา prospective เพื่อระบุปัจจัยเสี่ยงที่ใช้คัดเลือกผู้ป่วยแผลเพปติกมีเลือดออกที่ควรได้รับ second-look endoscopy หลังการส่องกล้องและให้ high-dose PPI |
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | เสร็จสิ้น | 320 | ประเมินผลของ PPI และ statin ต่อฤทธิ์ต้านเกล็ดเลือดของ clopidogrel ในผู้ป่วยที่ใส่ coronary stent และได้รับ dual antiplatelet therapy |

---

## หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|-----|------|------|---------|
| [18824852](https://pubmed.ncbi.nlm.nih.gov/18824852/) | 2008 | RCT | Digestion | Pantoprazole แบบ intermittent infusion เทียบกับ continuous infusion ในแผลเพปติกมีเลือดออก — ประเมินประสิทธิผลลดการ rebleeding หลังการส่องกล้อง |
| [16677158](https://pubmed.ncbi.nlm.nih.gov/16677158/) | 2006 | RCT | J Gastroenterol Hepatol | Pantoprazole IV infusion เป็น adjuvant therapy หลัง endoscopic hemostasis ลดอัตราการกลับมาเลือดออกซ้ำและการผ่าตัดฉุกเฉินในผู้ป่วยแผลเพปติก |
| [12752349](https://pubmed.ncbi.nlm.nih.gov/12752349/) | 2003 | RCT | Aliment Pharmacol Ther | เปรียบเทียบประสิทธิผลของ Pantoprazole-based Triple Therapy 3 สูตรในการกำจัด H. pylori และการหายของแผลในกระเพาะอาหาร |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | RCT | Hepato-gastroenterology | เปรียบเทียบ Lansoprazole กับ Pantoprazole ในการรักษา Active Duodenal Ulcer และกำจัดเชื้อ H. pylori — ประเมิน eradication rate และ ulcer healing |
| [10632647](https://pubmed.ncbi.nlm.nih.gov/10632647/) | 2000 | RCT | Aliment Pharmacol Ther | Pantoprazole + amoxycillin ร่วมกับ azithromycin หรือ clarithromycin สำหรับกำจัด H. pylori ในผู้ป่วย Duodenal Ulcer — 1-week triple therapy |
| [38384180](https://pubmed.ncbi.nlm.nih.gov/38384180/) | 2024 | RCT | Gut and Liver | Tegoprazan เทียบกับ Pantoprazole ในการรักษาแผลเทียม (artificial ulcer) หลัง ESD — multicenter, randomized, active-controlled study |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Meta-analysis | Am J Gastroenterol | Systematic review และ network meta-analysis เปรียบเทียบประสิทธิผล P-CAB กับ PPI รวมถึง Pantoprazole ในการรักษา Grade C/D Esophagitis |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Invest | ภาพรวมครอบคลุมของ Pantoprazole: กลไก irreversible binding, ระยะออกฤทธิ์ยาว, ไม่มี drug-drug interaction ที่มีนัยสำคัญ, ประสิทธิผลใน GERD และแผลเพปติก |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | Animal study | Inflammopharmacology | การรักษาร่วม Pantoprazole + adipose-derived mesenchymal stem cells ในหนูที่ถูกเหนี่ยวนำให้มีแผลในกระเพาะ — ศึกษา oxidative stress, inflammation, apoptosis pathways |
| [9017763](https://pubmed.ncbi.nlm.nih.gov/9017763/) | 1997 | Review | Pharmacotherapy | กลไก PPI ในการยับยั้ง H⁺/K⁺-ATPase ผ่าน acid-catalyzed activation และประสิทธิผลเหนือกว่า H2-receptor antagonist ในการควบคุมการหลั่งกรด |

---

## ข้อพิจารณาด้านความปลอดภัย

กรุณาดูข้อมูลความปลอดภัยในเอกสารกำกับยา

---

## สรุปและขั้นตอนถัดไป

**การตัดสินใจ: Proceed with Guardrails**

**เหตุผล:**
มีหลักฐานระดับ L1 ที่แข็งแกร่งสนับสนุนการใช้ Pantoprazole ในแผลเพปติก ทั้ง Phase 3 RCT ที่เสร็จสมบูรณ์และวรรณกรรมจำนวนมาก กลไกการออกฤทธิ์มีความสอดคล้องโดยตรงกับพยาธิสรีรวิทยาของโรค อย่างไรก็ตาม ยังขาดทะเบียนในประเทศไทยและข้อมูลความปลอดภัยอย่างเป็นทางการ จึงต้องดำเนินการขั้นตอนเพิ่มเติมก่อนนำไปใช้

**หากต้องการดำเนินการต่อต้อง:**
- ยื่นขอขึ้นทะเบียนยากับสำนักงานคณะกรรมการอาหารและยา (อย.) ประเทศไทย
- ดาวน์โหลดและวิเคราะห์เอกสารกำกับยา (Package Insert/SmPC) เพื่อรวบรวมข้อมูลคำเตือนและข้อห้ามใช้
- รับข้อมูล MOA และ safety profile อย่างเป็นทางการจาก DrugBank API (DB00213)
- ประเมิน Drug-Drug Interaction กับยาที่ใช้บ่อยในผู้ป่วยไทย โดยเฉพาะ clopidogrel และยาต้านการแข็งตัวของเลือด
- กำหนดแนวทางการติดตามความปลอดภัยในกลุ่มเสี่ยง เช่น ผู้สูงอายุ ผู้ป่วยโรคตับ และผู้ป่วยที่ใช้ยาหลายชนิด
---

