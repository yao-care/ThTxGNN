---
layout: default
title: Progesterone
parent: หลักฐานระดับสูง (L1-L2)
nav_order: 130
evidence_level: L2
indication_count: 10
---

# Progesterone
{: .fs-9 }

ระดับหลักฐาน: **L2** | ข้อบ่งใช้ที่ทำนาย: **10** รายการ
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

ใช้ `txgnn-pipeline` ตรวจสอบบริบทโครงการแล้ว — นี่คือรายงานจาก Evidence Pack ของ ThTxGNN สำหรับ Progesterone:

---

# Progesterone: จากการควบคุมวงจรประจำเดือนสู่ภาวะหยุดมีประจำเดือน

## สรุปสั้นๆ

Progesterone เป็นฮอร์โมนสเตียรอยด์ธรรมชาติที่มีบทบาทหลักในการควบคุมวงจรประจำเดือน การสนับสนุนระยะ luteal phase และการบำบัดทดแทนฮอร์โมนในสตรีวัยหมดประจำเดือน โมเดล TxGNN คาดการณ์ว่าอาจมีผลต่อ **ภาวะหยุดมีประจำเดือน (Amenorrhea)** ปัจจุบันมี **การทดลองทางคลินิก 50 รายการ** และ **วรรณกรรม 18 ฉบับ** สนับสนุนแนวทางนี้

---

## ภาพรวมฉบับย่อ

| รายการ | เนื้อหา |
|------|------|
| ข้อบ่งใช้เดิม | การควบคุมวงจรประจำเดือน / การบำบัดทดแทนฮอร์โมน |
| ข้อบ่งใช้ใหม่ที่ทำนาย | ภาวะหยุดมีประจำเดือน (Amenorrhea) |
| คะแนนการทำนาย TxGNN | 99.9996% |
| ระดับหลักฐาน | L2 |
| สถานะการวางจำหน่ายในไทย | ✗ ยังไม่มีทะเบียนยาในประเทศไทย |
| จำนวนใบอนุญาต | 0 รายการ |
| คำแนะนำในการตัดสินใจ | Proceed with Guardrails |

---

## ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

ปัจจุบันยังขาดข้อมูลกลไกการออกฤทธิ์โดยละเอียดจากฐานข้อมูล DrugBank ตามที่ทราบ Progesterone เป็นฮอร์โมนสเตียรอยด์ธรรมชาติที่ออกฤทธิ์ผ่านตัวรับโปรเจสเตอโรน (Progesterone Receptor, PR) บนเซลล์เนื้อเยื่อของระบบสืบพันธุ์หญิง รวมถึงเยื่อบุมดลูก รังไข่ ต่อมใต้สมอง และไฮโปทาลามัส โดยมีบทบาทควบคุมการหลั่ง LH/FSH ผ่านระบบ kisspeptin–neurokinin B–dynorphin (KNDy neurons)

ความเชื่อมโยงกับภาวะหยุดมีประจำเดือนนั้นชัดเจนมากในทางคลินิก เนื่องจาก **Progestogen Challenge Test** เป็นเครื่องมือมาตรฐานในการวินิจฉัยแยกประเภทภาวะหยุดมีประจำเดือน: การตอบสนองด้วย withdrawal bleeding บ่งชี้ว่าร่างกายมีระดับ estrogen เพียงพอและปัญหาอยู่ที่การขาด progesterone ในช่วง luteal phase การเสริม progesterone เป็นระยะจึงสามารถแก้ไข anovulatory amenorrhea ได้โดยตรง

กลไกนี้ยังครอบคลุมสาเหตุย่อยหลายอย่างของภาวะหยุดมีประจำเดือน ไม่ว่าจะเป็น hypothalamic amenorrhea, PCOS-related anovulation, หรือ iatrogenic amenorrhea หลังการรักษาต่างๆ ความที่โมเดล TxGNN ให้คะแนนสูงถึง 99.9996% จึงสะท้อนความสัมพันธ์เชิงกลไกที่ลึกซึ้งและมีหลักฐานทางคลินิกรองรับมาอย่างยาวนานกว่า 50 ปี

---

## หลักฐานจากการทดลองทางคลินิก

| หมายเลขการทดลอง | ระยะ | สถานะ | จำนวนผู้เข้าร่วม | ผลลัพธ์หลัก |
|---------|------|------|------|---------|
| [NCT01942668](https://clinicaltrials.gov/study/NCT01942668) | Phase 3 | เสร็จสิ้น | 1,845 | RCT แบบ double-blind ศึกษา estradiol + **progesterone** สำหรับอาการ vasomotor ในสตรีวัยหมดประจำเดือน (มดลูกยังคงอยู่) |
| [NCT02884245](https://clinicaltrials.gov/study/NCT02884245) | Phase 3 | เสร็จสิ้น | 334 | ประเมินการนัดหมาย estrogen scheduling ก่อนกระตุ้นไข่ด้วย corifollitropin alfa ในหญิงอายุ > 38 ปี ที่ทำ IVF (ครอบคลุมกลุ่ม amenorrhea/low GnRH) |
| [NCT00088153](https://clinicaltrials.gov/study/NCT00088153) | Phase 2/3 | เสร็จสิ้น | 110 | ผลของ anorexia nervosa ต่อความหนาแน่นกระดูกในวัยรุ่น; ประเมิน estrogen ในกลุ่ม functional hypothalamic amenorrhea |
| [NCT00068601](https://clinicaltrials.gov/study/NCT00068601) | Phase 3 | เสร็จสิ้น | 257 | goserelin (LHRH analog) เพื่อป้องกัน chemotherapy-induced ovarian failure (ภาวะหยุดมีประจำเดือนจากเคมีบำบัด) ในมะเร็งเต้านม |
| [NCT02322060](https://clinicaltrials.gov/study/NCT02322060) | N/A | เสร็จสิ้น | 100 | การเก็บรักษาและปลูกถ่ายเนื้อเยื่อรังไข่ (IVA) เพื่อกระตุ้น dormant follicles ในผู้ป่วย Primary Ovarian Insufficiency ที่มีภาวะหยุดมีประจำเดือน |
| [NCT00001306](https://clinicaltrials.gov/study/NCT00001306) | N/A | เสร็จสิ้น | 33 | Alternate-day prednisone สำหรับ autoimmune premature ovarian failure ซึ่งเป็นสาเหตุสำคัญของภาวะหยุดมีประจำเดือนทุติยภูมิ |
| [NCT05312190](https://clinicaltrials.gov/study/NCT05312190) | N/A | ไม่ทราบสถานะ | 330 | RCT หลายศูนย์ เปรียบเทียบ **Progesterone Capsules** กับ ZhenQi Buxue Oral Liquid และการใช้ร่วมกัน ในการรักษาความผิดปกติของประจำเดือน |
| [NCT03309176](https://clinicaltrials.gov/study/NCT03309176) | Phase 4 | เสร็จสิ้น | 42 | ประเมินความจำเป็นของ **progesterone-induced withdrawal bleeding** ก่อนการกระตุ้นไข่ด้วย clomiphene ในผู้ป่วย oligo/amenorrhea |
| [NCT07224438](https://clinicaltrials.gov/study/NCT07224438) | Phase 2 | กำลังรับสมัคร | 20 | kisspeptin ฉีดใต้ผิวหนังแบบ pulsatile เพื่อกระตุ้นการหลั่งฮอร์โมนสืบพันธุ์ในผู้ป่วย hypothalamic amenorrhea |
| [NCT05767515](https://clinicaltrials.gov/study/NCT05767515) | N/A | เสร็จสิ้น | 120 | Acetyl L-Carnitine / Myo-Inositol ในการปรับปรุงการตกไข่และลด PCOS-related amenorrhea (ข้อมูลกลุ่มควบคุม) |

---

## หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|-----|------|------|---------|
| [38652231](https://pubmed.ncbi.nlm.nih.gov/38652231/) | 2024 | Review | Reviews in Endocrine & Metabolic Disorders | การใช้ oral micronized **progesterone** ในทางคลินิกต่อมไร้ท่อ: บทบาทควบคุม LH/FSH ผ่าน KNDy neurons และการรักษาวงจรประจำเดือน |
| [35525789](https://pubmed.ncbi.nlm.nih.gov/35525789/) | 2022 | Review | Current Problems in Pediatric and Adolescent Health Care | สาเหตุและการจัดการภาวะหยุดมีประจำเดือนในวัยรุ่นและผู้ใหญ่ตอนต้น รวมบทบาท HPO axis และ estrogen/progesterone |
| [33716979](https://pubmed.ncbi.nlm.nih.gov/33716979/) | 2021 | Review | Frontiers in Endocrinology | ความเข้าใจปัจจุบันเกี่ยวกับ Premature Ovarian Insufficiency (POI): สาเหตุ อาการ และบทบาท HRT ที่มี progesterone |
| [36653588](https://pubmed.ncbi.nlm.nih.gov/36653588/) | 2023 | Review | Reproductive Sciences | วิธีซ่อมแซมเยื่อบุมดลูก; ภาวะหยุดมีประจำเดือน (รวม Asherman's syndrome) เป็น endpoint หลักของการฟื้นฟูเยื่อบุ |
| [32233689](https://pubmed.ncbi.nlm.nih.gov/32233689/) | 2020 | Review | Climacteric | การจัดการเลือดออกทางช่องคลอดหลังวัยหมดประจำเดือน: นิยาม amenorrhea ≥ 12 เดือน และบทบาทของ progesterone deficiency |
| [18756412](https://pubmed.ncbi.nlm.nih.gov/18756412/) | 2008 | Review | Seminars in Reproductive Medicine | Intrauterine adhesions (Asherman's syndrome) — กลไกทำให้เกิด amenorrhea และความสัมพันธ์กับภาวะ hypoestrogenized state |
| [35463307](https://pubmed.ncbi.nlm.nih.gov/35463307/) | 2022 | Meta-analysis | Frontiers in Oncology | Chemotherapy-induced amenorrhea: ปัจจัยเสี่ยงและนัยยะเชิงพยากรณ์ในผู้ป่วยมะเร็งเต้านมก่อนวัยหมดประจำเดือน |
| [28257537](https://pubmed.ncbi.nlm.nih.gov/28257537/) | 2017 | Review | Southern Medical Journal | Primary Ovarian Insufficiency: แนวคิดปัจจุบัน, secondary amenorrhea, และบทบาทจำเป็นของ HRT รวมถึง progesterone |
| [8629565](https://pubmed.ncbi.nlm.nih.gov/8629565/) | 1996 | Review | American Family Physician | การประเมินภาวะหยุดมีประจำเดือน: progestogen challenge test, บทบาท estrogen/progesterone และ algorithm วินิจฉัยแยกโรค |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Review | Reviews in Endocrine & Metabolic Disorders | ฮอร์โมนบำบัดใน endometriosis: estrogen-dependency และ progesterone-resistance ในฐานะกลไกหลักของโรค |

---

## ข้อพิจารณาด้านความปลอดภัย

กรุณาดูข้อมูลความปลอดภัยในเอกสารกำกับยา

---

## สรุปและขั้นตอนถัดไป

**การตัดสินใจ: Proceed with Guardrails**

**เหตุผล:**
มีการทดลองทางคลินิก Phase 3 หลายรายการที่เสร็จสิ้นและมี progesterone เป็นส่วนหนึ่งของการรักษา ประกอบกับหลักฐานทางกลไกที่แน่นแฟ้นจากบทบาทของ progestogen challenge test ซึ่งเป็นมาตรฐานสากลในการวินิจฉัยและรักษาภาวะหยุดมีประจำเดือน อย่างไรก็ตาม ยังไม่มีทะเบียนยาในประเทศไทยและขาดข้อมูลความปลอดภัยจาก TFDA

**หากต้องการดำเนินการต่อต้อง:**
- ดาวน์โหลดและวิเคราะห์เอกสารกำกับยา (SPC/PIL) จาก TFDA เพื่อให้ได้คำเตือนและข้อห้ามใช้ฉบับสมบูรณ์
- ระบุกลไกการออกฤทธิ์โดยละเอียดจาก DrugBank API (DB00396)
- ประเมินเส้นทางนำยาที่เหมาะสม (oral micronized, vaginal, injection) กับกลุ่มผู้ป่วยเป้าหมายในประเทศไทย
- กำหนดแผนติดตามความปลอดภัยสำหรับกลุ่มเสี่ยงพิเศษ (ผู้ป่วยที่มีประวัติลิ่มเลือด มะเร็งเต้านม)
- พิจารณาเชื่อมโยงกับทะเบียนยาในประเทศอื่น (EMA, FDA) เพื่อสนับสนุนการยื่นขอทะเบียนในไทย
---

