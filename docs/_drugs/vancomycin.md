---
layout: default
title: Vancomycin
parent: หลักฐานระดับกลาง (L3-L4)
nav_order: 157
evidence_level: L3
indication_count: 10
---

# Vancomycin
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

Using `txgnn-pipeline` skill to align with TxGNN report generation standards. The skill confirms standard workflow applies. Now generating the report — this is a **multi-indication** Evidence Pack (10 รายการ) for Vancomycin, where rank 9 (streptococcal pneumonia) is the only prediction with biological rationale and actionable evidence. I'll adapt the format accordingly.

---

# Vancomycin: จากการรักษาการติดเชื้อแกรมบวกสู่ปอดอักเสบจากเชื้อสเตรปโตค็อกคัส

## สรุปสั้นๆ

Vancomycin เป็นยาปฏิชีวนะกลุ่ม Glycopeptide ที่ได้รับการยอมรับทั่วโลกในการรักษาการติดเชื้อแบคทีเรียแกรมบวกรุนแรง โดยเฉพาะ MRSA และเชื้อดื้อยา beta-lactam

โมเดล TxGNN ทำนายข้อบ่งใช้ใหม่ทั้งหมด **10 รายการ** แต่จากการวิเคราะห์หลักฐานพบว่า **9 ใน 10 รายการเป็นผลบวกปลอม (False Positive)** เนื่องจากมีข้อขัดแย้งทางกลไกพื้นฐาน มีเพียง **ปอดอักเสบจากเชื้อสเตรปโตค็อกคัส (Streptococcal Pneumonia)** เท่านั้นที่มีความสมเหตุสมผลทางชีววิทยา โดยมีหลักฐานจาก **การทดลองทางคลินิก 3 รายการ** และ **วรรณกรรม 20 ฉบับ** สนับสนุน

## ภาพรวมฉบับย่อ

> ⚠️ **รายงานนี้เป็น Multi-Indication Evidence Pack (10 รายการ)** ตารางด้านล่างแสดงข้อบ่งใช้ที่มีหลักฐานสนับสนุนสูงที่สุดและมีความสมเหตุสมผลทางคลินิก (อันดับ 9)

| รายการ | เนื้อหา |
|--------|---------|
| ข้อบ่งใช้เดิม | การรักษาการติดเชื้อแบคทีเรียแกรมบวกรุนแรง (MRSA และเชื้อดื้อยา beta-lactam) |
| ข้อบ่งใช้ใหม่ที่ทำนาย | ปอดอักเสบจากเชื้อสเตรปโตค็อกคัส (Streptococcal Pneumonia) |
| คะแนนการทำนาย TxGNN | 99.60% |
| ระดับหลักฐาน | L3 |
| สถานะการวางจำหน่ายในไทย | ✗ ไม่มีทะเบียนในระบบ TFDA |
| จำนวนใบอนุญาต | 0 รายการ |
| คำแนะนำในการตัดสินใจ | Proceed with Guardrails |

## ภาพรวมการทำนายทั้งหมด 10 รายการ

| อันดับ | ข้อบ่งใช้ที่ทำนาย | คะแนน TxGNN | ระดับหลักฐาน | คำแนะนำ | สถานะ |
|--------|----------|-----------|------------|--------|------|
| 1 | Diffuse Scleroderma | 99.92% | L5 | Hold | ⚠️ False Positive — เอกสารอ้างถึงผลข้างเคียงของยา ไม่ใช่ประโยชน์ทางการรักษา |
| 2 | Paratyphoid Fever | 99.85% | L5 | Hold | ⚠️ False Positive — *S. Paratyphi* เป็นแกรมลบ Vancomycin ผ่านเข้าไม่ได้ |
| 3 | Salmonellosis | 99.81% | L5 | Hold | ⚠️ False Positive — *Salmonella* เป็นแกรมลบ มีข้อขัดแย้งทางกลไกโดยสิ้นเชิง |
| 4 | Congenital Analbuminemia | 99.79% | L5 | Hold | ⚠️ False Positive — TxGNN สับสนระหว่าง protein binding กับผลทางการรักษา |
| 5 | Polyclonal Hyperviscosity Syndrome | 99.79% | L5 | Hold | ⚠️ False Positive — ไม่มีกลไกที่เชื่อมโยงใดๆ |
| 6 | Hyperamylasemia | 99.79% | L5 | Hold | ⚠️ False Positive — Vancomycin อาจเป็น *สาเหตุ* ของ pancreatitis ไม่ใช่การรักษา |
| 7 | Typhoid Fever | 99.75% | L5 | Hold | ⚠️ False Positive — *S. Typhi* เป็นแกรมลบ ข้อขัดแย้งทางโครงสร้างยา |
| 8 | Blood Group Incompatibility | 99.63% | L5 | Hold | ⚠️ False Positive — ไม่มีกลไกใดที่เชื่อมกับ antigen-antibody reaction |
| **9** | **Streptococcal Pneumonia** | **99.60%** | **L3** | **✅ Proceed with Guardrails** | **กลไกตรงกัน มีหลักฐานทางคลินิกและแนวทางสากลรองรับ** |
| 10 | Premalignant Hematological Disease | 99.54% | L5 | Hold | ⚠️ False Positive — ยาปฏิชีวนะไม่มีฤทธิ์ต้านเนื้องอกหรือปรับ epigenetics |

## ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

Vancomycin ออกฤทธิ์โดยจับโดยตรงกับ D-Ala-D-Ala ที่ปลายสายของ peptidoglycan precursors ในผนังเซลล์แบคทีเรีย ขัดขวางทั้งกระบวนการ transglycosylation และ transpeptidation ทำให้ผนังเซลล์แตกสลายและแบคทีเรียตาย กลไกนี้มีความจำเพาะต่อแบคทีเรีย**แกรมบวก**ที่มีผนัง peptidoglycan หนา ซึ่งเป็นเหตุผลว่าทำไมการทำนายที่เกี่ยวกับแบคทีเรียแกรมลบ (Salmonella, Paratyphoid, Typhoid) จึงเป็นข้อขัดแย้งทางโครงสร้างที่ไม่อาจแก้ไขได้

*Streptococcus pneumoniae* เป็นแบคทีเรียแกรมบวกที่เป็นสาเหตุหลักของปอดอักเสบในชุมชนและในโรงพยาบาลทั่วโลก เป้าหมายทางชีววิทยาของโรคตรงกับกลไกของยาโดยสมบูรณ์ โดยเฉพาะในกรณีที่เชื้อพัฒนาความดื้อต่อ penicillin หรือ cephalosporin รุ่นต่างๆ ซึ่งแนวทางการรักษาของ IDSA/ATS รับรองให้ Vancomycin เป็นยาทางเลือกที่ชัดเจน

สิ่งที่ทำให้การทำนายอันดับ 9 นี้แตกต่างจากอีก 9 รายการคือ มีหลักฐานการใช้งานจริงในทางคลินิกปรากฏในวรรณกรรมอย่างต่อเนื่องตั้งแต่ปี 1997 จนถึง 2024 และมีการศึกษา RCT เปรียบเทียบโดยตรง จึงถือเป็นการ "ขยายข้อบ่งใช้อย่างเป็นทางการ" มากกว่าการค้นพบทิศทางใหม่

## หลักฐานจากการทดลองทางคลินิก

| หมายเลขการทดลอง | ระยะ | สถานะ | จำนวนผู้เข้าร่วม | ผลลัพธ์หลัก |
|----------------|------|-------|----------------|------------|
| [NCT04464291](https://clinicaltrials.gov/study/NCT04464291) | N/A | เสร็จสิ้น | 500 | สำรวจ Serotype และความไวต่อยาของ *S. pneumoniae* ในรัสเซีย (ผู้มีสุขภาพดี + ผู้ติดเชื้อ) ให้ข้อมูลพื้นหลังด้านการดื้อยาที่เกี่ยวข้องกับ Vancomycin |
| [NCT05395520](https://clinicaltrials.gov/study/NCT05395520) | N/A | ไม่ทราบ | 146 | ประเมินว่า AUC monitoring ของ Vancomycin เหมาะสมสำหรับการติดเชื้อแกรมบวกนอกเหนือจาก MRSA หรือไม่ — ครอบคลุมการติดเชื้อ Streptococcal ด้วย |
| [NCT02538211](https://clinicaltrials.gov/study/NCT02538211) | N/A | เสร็จสิ้น | 63 | ศึกษาผลของ intestinal microbiota ต่อการตอบสนองภูมิคุ้มกันต่อวัคซีน — ให้ข้อมูลพื้นฐานเท่านั้น ไม่ได้ประเมินประสิทธิผลของ Vancomycin โดยตรง |

## หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|-----|--------|--------|------------|
| [10712318](https://pubmed.ncbi.nlm.nih.gov/10712318/) | 2000 | RCT | Am J Respir Crit Care Med | เปรียบเทียบ quinupristin/dalfopristin กับ **Vancomycin** ในการรักษาปอดอักเสบจากเชื้อแกรมบวกในโรงพยาบาล (N=298, multicenter) |
| [36028454](https://pubmed.ncbi.nlm.nih.gov/36028454/) | 2022 | Cohort | Indian J Med Microbiol | อัตราดื้อยาและ MIC distribution ของ penicillin ในผู้ป่วยปอดอักเสบจากสเตรปโตค็อกคัส ปี 2013–2019 |
| [37424548](https://pubmed.ncbi.nlm.nih.gov/37424548/) | 2023 | Cohort | Access Microbiology | ความไวต่อยาของ *S. pneumoniae* ในเด็กที่มีปอดอักเสบ (อินโดนีเซีย) — ให้ข้อมูลแนวโน้มการดื้อยาในเอเชีย |
| [38883355](https://pubmed.ncbi.nlm.nih.gov/38883355/) | 2024 | Cohort | Am J Translational Res | ความไวต่อยาปฏิชีวนะของ Group A Streptococcal infections ในสตรีตั้งครรภ์ |
| [35794077](https://pubmed.ncbi.nlm.nih.gov/35794077/) | 2022 | Cohort | J Perinat Med | ประเมินการใช้ Vancomycin ตามแนวทาง ACOG 2019 เพื่อป้องกัน Group B Streptococcal infections ในทารกแรกเกิด |
| [27161775](https://pubmed.ncbi.nlm.nih.gov/27161775/) | 2016 | Cohort | Clin Infect Dis | ความชุกและลักษณะทางคลินิกของปอดอักเสบจาก *S. aureus* ในชุมชน — ข้อมูลเปรียบเทียบสำหรับ gram-positive pneumonia |
| [10501315](https://pubmed.ncbi.nlm.nih.gov/10501315/) | 1999 | Review | Semin Respir Infect | การรักษาปอดอักเสบจากนิวโมค็อกคัส — ยืนยัน Vancomycin เป็นทางเลือกในเชื้อดื้อ penicillin |
| [9404765](https://pubmed.ncbi.nlm.nih.gov/9404765/) | 1997 | Cohort | Chest | แนวทางขนาดยาสำหรับปอดอักเสบจากนิวโมค็อกคัส พร้อมข้อกังวลเรื่องการใช้ Vancomycin มากเกินไปโดยไม่จำเป็น |
| [16341681](https://pubmed.ncbi.nlm.nih.gov/16341681/) | 2005 | Review | Eur J Clin Microbiol Infect Dis | การจัดการยาปฏิชีวนะในปอดอักเสบจากเครื่องช่วยหายใจ (VAP) ที่เกิดจากเชื้อแกรมบวกดื้อยา บทบาทของ Vancomycin |
| [11028185](https://pubmed.ncbi.nlm.nih.gov/11028185/) | 2000 | Review | Rev Med Suisse Romande | การดื้อยาปฏิชีวนะของนิวโมค็อกคัส — ครอบคลุมตำแหน่งของ Vancomycin ในบริบทการดื้อยา |

## ข้อมูลการวางจำหน่ายในประเทศไทย

ปัจจุบัน **Vancomycin ไม่ปรากฏในฐานข้อมูลทะเบียนยาของ TFDA** (ผลการค้นหา ณ วันที่ 10 มีนาคม 2026 พบ 0 รายการ) ซึ่งอาจหมายถึงว่ายาถูกนำเข้าผ่านช่องทางพิเศษหรือยังไม่ได้ยื่นขอขึ้นทะเบียนอย่างเป็นทางการ แนะนำให้ยืนยันสถานะนี้กับ TFDA โดยตรงก่อนดำเนินการใดๆ

## ข้อพิจารณาด้านความปลอดภัย

กรุณาดูข้อมูลความปลอดภัยในเอกสารกำกับยา

> ข้อมูลคำเตือน ข้อห้ามใช้ และปฏิกิริยาระหว่างยาจาก TFDA ยังไม่พร้อม — ระบุเป็น Blocking Data Gap (DG001) ต้องดาวน์โหลดและวิเคราะห์เอกสารกำกับยาก่อนเข้าสู่กระบวนการประเมินความปลอดภัย

## สรุปและขั้นตอนถัดไป

**การตัดสินใจ: Proceed with Guardrails** — เฉพาะข้อบ่งใช้ Streptococcal Pneumonia เท่านั้น

**เหตุผล:**
Vancomycin มีกลไกการออกฤทธิ์ที่ตรงกับเชื้อ *S. pneumoniae* อย่างชัดเจน มีหลักฐานระดับ L3 จากการศึกษาเชิงสังเกต วรรณกรรมทบทวน และ RCT เปรียบเทียบโดยตรง รวมถึงได้รับการรับรองจากแนวทาง IDSA/ATS ว่าเป็นยาทางเลือกที่เหมาะสม อย่างไรก็ตาม การที่ยาไม่มีทะเบียนใน TFDA และยังขาด safety profile ที่สมบูรณ์เป็นอุปสรรคสำคัญ

**หากต้องการดำเนินการต่อต้อง:**
- ตรวจสอบสถานะการนำเข้าและช่องทางจัดหา Vancomycin ที่ถูกกฎหมายในประเทศไทย หรือยื่นขอขึ้นทะเบียนกับ TFDA
- ดาวน์โหลดและวิเคราะห์เอกสารกำกับยาจากแหล่งอ้างอิงสากล (EMA, FDA, TGA) เพื่อปิด Blocking Data Gap DG001
- สืบค้นข้อมูล MOA และ pharmacokinetics อย่างสมบูรณ์จาก DrugBank (DB00512) เพื่อปิด High Data Gap DG002
- **ตัดการทำนาย 9 ใน 10 รายการออกจากการพิจารณา** เนื่องจากเป็น False Positive ที่มีข้อขัดแย้งทางกลไกพื้นฐาน — ไม่ควรนำไปสู่การทดลองทางคลินิกไม่ว่ากรณีใด
---

