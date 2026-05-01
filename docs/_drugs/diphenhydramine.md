---
layout: default
title: Diphenhydramine
parent: การคาดการณ์จากโมเดล (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
---

# Diphenhydramine
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

ใช้ `txgnn-pipeline` เพื่อตรวจสอบ context ก่อนสร้างรายงาน TxGNN Drug Repurposing Assessment ✓

---

# Diphenhydramine: จากยาต้านฮิสตามีน H1 สู่ Rosacea Conjunctivitis

## สรุปสั้นๆ

Diphenhydramine เป็นยาต้านฮิสตามีน H1 รุ่นแรก (first-generation antihistamine) ที่รู้จักในชื่อการค้า Benadryl ซึ่งใช้รักษาอาการแพ้ อาการคัน และนอนไม่หลับมาหลายทศวรรษ — แม้ยังไม่มีทะเบียนยาในประเทศไทย
โมเดล TxGNN คาดการณ์ **10 ข้อบ่งใช้ใหม่** โดยอันดับ 1 คือ **Rosacea Conjunctivitis** (99.20%) ซึ่งยังไม่มีหลักฐานสนับสนุน ขณะที่ **Rhinitis** (อันดับ 2) และ **Allergic Urticaria** (อันดับ 3) ต่างมีหลักฐานระดับ L2 พร้อมการทดลองทางคลินิก Phase 3–4 โดยตรง
ปัจจุบันพบ **การทดลองทางคลินิก 7 รายการ** และ **วรรณกรรม 18 ฉบับ** สำหรับ Rhinitis รวมถึง **3 รายการ** และ **19 ฉบับ** สำหรับ Allergic Urticaria ที่สนับสนุนแนวทางนี้

---

## ภาพรวมฉบับย่อ

| รายการ | เนื้อหา |
|------|------|
| ข้อบ่งใช้เดิม | ยาต้านฮิสตามีน H1 รุ่นแรก (ไม่มีทะเบียนในประเทศไทย) |
| ข้อบ่งใช้ใหม่ที่ทำนาย (อันดับ 1) | Rosacea Conjunctivitis |
| คะแนนการทำนาย TxGNN | 99.20% |
| ระดับหลักฐาน | L5 (อันดับ 1) |
| สถานะการวางจำหน่ายในไทย | ✗ ยังไม่มีทะเบียนในประเทศไทย |
| จำนวนใบอนุญาต | 0 รายการ |
| คำแนะนำในการตัดสินใจ | Hold (อันดับ 1) / Proceed with Guardrails (Rhinitis & Allergic Urticaria) |

---

## ข้อบ่งใช้ที่ทำนายทั้ง 10 รายการ

| อันดับ | ข้อบ่งใช้ | คะแนน TxGNN | ระดับหลักฐาน | คำแนะนำ |
|:---:|------|:---:|:---:|------|
| 1 | Rosacea Conjunctivitis | 99.20% | L5 | Hold |
| 2 | Rhinitis | 98.35% | L2 | Proceed with Guardrails |
| 3 | Allergic Urticaria | 98.24% | L2 | Proceed with Guardrails |
| 4 | Cold Urticaria | 95.92% | L5 | Hold |
| 5 | Cauda Equina Syndrome | 95.57% | L5 | Hold |
| 6 | Nasopharyngitis | 94.96% | L4 | Hold |
| 7 | Viral Conjunctivitis | 93.97% | L5 | Hold |
| 8 | Neuralgia | 92.30% | L4 | Hold |
| 9 | Trigeminal Autonomic Cephalalgia | 92.25% | L3 | Research Question |
| 10 | Glossodynia | 92.08% | L5 | Hold |

---

## ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

แม้ข้อมูล MOA อย่างเป็นทางการจาก DrugBank ยังไม่พร้อม แต่จากวรรณกรรมที่รวบรวมได้ Diphenhydramine ทำงานในฐานะ **H1 receptor antagonist แบบ competitive** จับกับตัวรับ H1 บนมาสตเซลล์ บาโซฟิล หลอดเลือด และเซลล์ประสาท ยับยั้งการตอบสนองทางภูมิแพ้ที่ฮิสตามีนเป็นตัวกลาง นอกจากนี้ยังมีฤทธิ์ต้านโคลิเนอร์จิก (anticholinergic) และกดประสาทส่วนกลาง ซึ่งทำให้เกิดผลข้างเคียงง่วงซึมที่เป็นที่รู้จักดี

**สำหรับ Rosacea Conjunctivitis (อันดับ 1):** การอักเสบของเยื่อบุตาในโรค Rosacea มีกลไกซับซ้อน รวมถึง innate immunity และ neurogenic inflammation ในทางทฤษฎี H1 blockade อาจยับยั้งฮิสตามีนจากมาสตเซลล์บริเวณเยื่อบุตา ลดอาการตาแดง น้ำตาไหล และไม่สบายตา อย่างไรก็ตาม การเชื่อมโยงนี้ยังเป็นเพียงการอนุมานทางกลไก ไม่มีหลักฐานทางคลินิกหรือวรรณกรรมรองรับโดยตรงในปัจจุบัน

**สำหรับ Rhinitis (อันดับ 2) และ Allergic Urticaria (อันดับ 3):** กลไกมีความชัดเจนและพิสูจน์แล้ว — Diphenhydramine บล็อก H1 receptors บนเยื่อบุจมูกและผิวหนัง ยับยั้งการขยายหลอดเลือด การหลั่งเมือก อาการคัน และการเกิดผื่นลมพิษ ซึ่งเป็นกลไกคลาสสิกที่ยืนยันด้วย RCT Phase 4 ขนาดใหญ่ (N=1,021) สำหรับ Rhinitis และ Phase 3 pilot สำหรับ Acute Urticaria ทั้งสองข้อบ่งใช้นี้คือการใช้งานที่ยอมรับสากลของ Diphenhydramine อยู่แล้ว — TxGNN กำลัง **ยืนยัน** การใช้งานที่มีอยู่ ไม่ใช่การค้นพบใหม่

---

## หลักฐานจากการทดลองทางคลินิก

### Rosacea Conjunctivitis (อันดับ 1)

ปัจจุบันยังไม่มีการลงทะเบียนการทดลองทางคลินิกที่เกี่ยวข้อง

---

### Rhinitis (อันดับ 2)

| หมายเลขการทดลอง | ระยะ | สถานะ | จำนวนผู้เข้าร่วม | ผลลัพธ์หลัก |
|---------|:---:|------|:---:|---------|
| [NCT00648973](https://clinicaltrials.gov/study/NCT00648973) | Phase 4 | เสร็จสิ้น | 1,021 | ประเมิน Diphenhydramine 25mg และ 50mg บรรเทาอาการคัดจมูกใน Seasonal Allergic Rhinitis เทียบกับ Pseudoephedrine และยาหลอก — ผลตรงตัวสำหรับยาและโรคนี้ |
| [NCT00599872](https://clinicaltrials.gov/study/NCT00599872) | Phase 3 | เสร็จสิ้น | 430 | ศึกษาขนาดยา SLIT สำหรับ Allergic Rhinoconjunctivitis จากละอองเกสร Ragweed (Diphenhydramine เป็น rescue medication) |
| [NCT05586477](https://clinicaltrials.gov/study/NCT05586477) | Phase 4 | เสร็จสิ้น | 20 | ผล Diphenhydramine ต่อการตอบสนองควบคุมอุณหภูมิระหว่างออกกำลังกาย ในกลุ่มผู้ป่วย Rhinitis (ข้อมูลพื้นหลังฤทธิ์ยา) |
| [NCT00762749](https://clinicaltrials.gov/study/NCT00762749) | Phase 1 | เสร็จสิ้น | 36 | เภสัชจลนศาสตร์ของ Diphenhydramine ในเด็ก (2–12 ปี) และวัยรุ่น (12–18 ปี) — ข้อมูลขนาดยา |
| [NCT06217367](https://clinicaltrials.gov/study/NCT06217367) | Phase 4 | ไม่ทราบ | 16 | ยาต้านฮิสตามีน OTC รวม Diphenhydramine กับการตอบสนองควบคุมอุณหภูมิระหว่างความร้อน |

---

### Allergic Urticaria (อันดับ 3)

| หมายเลขการทดลอง | ระยะ | สถานะ | จำนวนผู้เข้าร่วม | ผลลัพธ์หลัก |
|---------|:---:|------|:---:|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | เสร็จสิ้น | 36 | เปรียบเทียบ IV Cetirizine กับ **IV Diphenhydramine 50mg** โดยตรงสำหรับ Acute Urticaria ในแผนกฉุกเฉิน — ยาและโรคตรงประเด็นที่สุด |

---

### Trigeminal Autonomic Cephalalgia (อันดับ 9)

| หมายเลขการทดลอง | ระยะ | สถานะ | จำนวนผู้เข้าร่วม | ผลลัพธ์หลัก |
|---------|:---:|------|:---:|---------|
| [NCT01406860](https://clinicaltrials.gov/study/NCT01406860) | N/A | ยุติก่อนกำหนด | 19 | **Metoclopramide + Diphenhydramine** เทียบกับ Droperidol สำหรับปวดหัวปฐมภูมิในแผนกฉุกเฉิน — Diphenhydramine เป็นหนึ่งในยาที่ศึกษาโดยตรง แม้หยุดก่อนกำหนด |

---

## หลักฐานจากวรรณกรรม

### Rhinitis (อันดับ 2)

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|:---:|------|------|---------|
| [16680933](https://pubmed.ncbi.nlm.nih.gov/16680933/) | 2006 | RCT | Ann Allergy Asthma Immunol | Diphenhydramine มีประสิทธิผลบรรเทาอาการ Seasonal Allergic Rhinitis ระดับปานกลาง-รุนแรง เทียบได้กับ Desloratadine |
| [8634878](https://pubmed.ncbi.nlm.nih.gov/8634878/) | 1996 | RCT | Ann Allergy Asthma Immunol | Diphenhydramine บรรเทาอาการ SAR แต่ลดความสามารถการเรียนรู้เมื่อเทียบกับยาต้านฮิสตามีนไม่ทำให้ง่วง |
| [14582817](https://pubmed.ncbi.nlm.nih.gov/14582817/) | 2003 | RCT | Ann Allergy Asthma Immunol | Diphenhydramine ลดความตื่นตัวและสมรรถภาพทางปัญญาระหว่างรักษา Ragweed-induced Allergic Rhinitis เทียบกับ Desloratadine |
| [36420548](https://pubmed.ncbi.nlm.nih.gov/36420548/) | 2022 | Cohort | Tokai J Exp Clin Med | Diphenhydramine ผ่านผิวจมูก (transdermal nasal ala) มีประสิทธิผลและปลอดภัยสำหรับ Allergic Rhinitis ร่วมกับโรคหอบหืด |
| [40152721](https://pubmed.ncbi.nlm.nih.gov/40152721/) | 2025 | Review | Med Lett Drugs Ther | แนวทางการรักษา Allergic Rhinitis และ Allergic Conjunctivitis ปี 2025 |
| [31582993](https://pubmed.ncbi.nlm.nih.gov/31582993/) | 2019 | Review | Allergy Asthma Clin Immunol | CSACI Position Statement: H1-antihistamines รุ่นใหม่ปลอดภัยกว่าสำหรับ Allergic Rhinitis (Diphenhydramine มีผลข้างเคียงง่วง, anticholinergic สูง) |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | ทบทวนประสิทธิผลและความปลอดภัยของยาต้านฮิสตามีนรุ่นแรกและรุ่นใหม่สำหรับ Allergic Rhinitis และ CIU |
| [33848281](https://pubmed.ncbi.nlm.nih.gov/33848281/) | 2021 | Review | Med Lett Drugs Ther | แนวทางการใช้ยาสำหรับ Allergic Rhinitis และ Allergic Conjunctivitis |
| [40717751](https://pubmed.ncbi.nlm.nih.gov/40717751/) | 2025 | Review | J Pediatr Pharmacol Ther | ทบทวนการใช้งานทางคลินิกและโปรไฟล์ผลข้างเคียงของ Diphenhydramine ครอบคลุม Anaphylaxis, Urticaria และ Allergic Rhinitis |
| [36759413](https://pubmed.ncbi.nlm.nih.gov/36759413/) | 2023 | Animal | AAPS PharmSciTech | Diphenhydramine nasal nano-gel/nano-emulgel ปรับปรุงการซึมผ่านเยื่อจมูกและยับยั้งอาการ Allergic Rhinitis ในสัตว์ทดลอง |

---

### Allergic Urticaria (อันดับ 3)

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|:---:|------|------|---------|
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | ยาต้านฮิสตามีนรุ่นแรก (รวม Diphenhydramine) เคยเป็นยาหลักสำหรับ Chronic Idiopathic Urticaria ก่อนยุครุ่นใหม่ |
| [28913986](https://pubmed.ncbi.nlm.nih.gov/28913986/) | 2017 | Review | Allergy Asthma Immunol Res | Chronic Spontaneous Urticaria: Diphenhydramine เป็น H1-blocker แนวแรกในอดีต ปัจจุบันมักใช้ Second-generation AH สูงสุด 4 เท่า/วัน |
| [31582993](https://pubmed.ncbi.nlm.nih.gov/31582993/) | 2019 | Review | Allergy Asthma Clin Immunol | Diphenhydramine และ Hydroxyzine มีผลข้างเคียงสำคัญ (sedation, anticholinergic, cardiac risk) เมื่อใช้รักษา Urticaria |
| [34862952](https://pubmed.ncbi.nlm.nih.gov/34862952/) | 2022 | Review | Adv Ther | บทบาทของ IV Cetirizine เปรียบเทียบกับ IV Diphenhydramine — Diphenhydramine ยังคงเป็น IV antihistamine เพียงชนิดเดียวที่ FDA อนุมัติก่อน Cetirizine IV ปี 2019 |
| [40717751](https://pubmed.ncbi.nlm.nih.gov/40717751/) | 2025 | Review | J Pediatr Pharmacol Ther | Diphenhydramine ใช้รักษา Anaphylaxis, Urticaria และ Allergic Rhinitis เป็นหลัก พร้อมข้อควรระวังการให้ IV อย่างรวดเร็ว |
| [12113226](https://pubmed.ncbi.nlm.nih.gov/12113226/) | 2002 | Review | Clin Allergy Immunol | หลักฐานระดับ 1 สนับสนุนประสิทธิผล H1-antihistamines (รวม Diphenhydramine) ใน Allergic Rhinoconjunctivitis ทั้งเด็กและผู้ใหญ่ |

---

### Trigeminal Autonomic Cephalalgia (อันดับ 9)

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|:---:|------|------|---------|
| [29395690](https://pubmed.ncbi.nlm.nih.gov/29395690/) | 2018 | Review | J Emerg Med | แนวทางการจัดการปวดหัวไม่อันตรายในแผนกฉุกเฉิน รวมสูตร Metoclopramide + Diphenhydramine เป็นตัวเลือกหลัก |
| [14909468](https://pubmed.ncbi.nlm.nih.gov/14909468/) | 1952 | Case series | Lahey Clin Bull | รายงานทางคลินิก: Benadryl (Diphenhydramine) บรรเทา Histamine Headache ได้อย่างมีนัยสำคัญ |
| [20270600](https://pubmed.ncbi.nlm.nih.gov/20270600/) | 1947 | Animal | J Allergy | Benadryl แสดงฤทธิ์ป้องกัน Experimental Histamine Headache ในแบบจำลองสัตว์ — รากฐานกลไกทางประวัติศาสตร์ |
| [18123681](https://pubmed.ncbi.nlm.nih.gov/18123681/) | 1949 | Case series | US Naval Med Bull | กรณีศึกษา: Benadryl บรรเทา Histamine Headache — ข้อมูลประวัติศาสตร์สนับสนุน H1 blockade ต่อปวดหัวจากฮิสตามีน |

---

### Nasopharyngitis (อันดับ 6)

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|:---:|------|------|---------|
| [17560664](https://pubmed.ncbi.nlm.nih.gov/17560664/) | 2007 | RCT | Int J Pediatr Otorhinolaryngol | Antihistamine + Decongestant + Acetaminophen ไม่ได้มีประสิทธิผลเหนือกว่า Acetaminophen เดี่ยวในการรักษา Acute Nasopharyngitis ในเด็ก |

---

## ข้อพิจารณาด้านความปลอดภัย

กรุณาดูข้อมูลความปลอดภัยในเอกสารกำกับยา

> **หมายเหตุ:** ข้อมูลคำเตือน ข้อห้ามใช้ และปฏิกิริยาระหว่างยาจาก TFDA ยังไม่พร้อม ควรดาวน์โหลดเอกสารกำกับยาจาก FDA สหรัฐอเมริกา (DailyMed) หรือ EMA ก่อนพิจารณาใช้งาน โดยเฉพาะอย่างยิ่งข้อควรระวังเรื่องผลข้างเคียงง่วงซึม ฤทธิ์ต้านโคลิเนอร์จิก และความเสี่ยงในผู้สูงอายุ

---

## สรุปและขั้นตอนถัดไป

**การตัดสินใจ: Hold (อันดับ 1 — Rosacea Conjunctivitis) / Proceed with Guardrails (อันดับ 2–3 — Rhinitis & Allergic Urticaria)**

**เหตุผล:**
สำหรับ **Rosacea Conjunctivitis** กลไก H1 blockade มีความสมเหตุสมผลทางทฤษฎี แต่ยังไม่มีหลักฐานคลินิกหรือวรรณกรรมรองรับแม้แต่ฉบับเดียว การดำเนินการต้องรอหลักฐานเบื้องต้นก่อน สำหรับ **Rhinitis และ Allergic Urticaria** มีการทดลองทางคลินิก Phase 3–4 สนับสนุนโดยตรง อย่างไรก็ตามต้องคำนึงถึงข้อจำกัดของ Diphenhydramine (ง่วงซึม, anticholinergic) เมื่อเปรียบเทียบกับยาต้านฮิสตามีนรุ่นใหม่ที่ปลอดภัยกว่า รวมทั้งยังไม่มีทะเบียนในประเทศไทย

**หากต้องการดำเนินการต่อต้อง:**
- ยื่นขอทะเบียนยาต่อ อย. (TFDA) โดยรวบรวมเอกสารจากประเทศต้นทาง
- ดาวน์โหลดและวิเคราะห์เอกสารกำกับยา (สหรัฐฯ/EU) เพื่อประเมินคำเตือนและข้อห้ามใช้ (แก้ไข Data Gap DG001)
- สืบค้น MOA โดยละเอียดจาก DrugBank API (แก้ไข Data Gap DG002)
- สำหรับ **Rosacea Conjunctivitis**: ออกแบบการศึกษา Proof-of-Concept ขนาดเล็ก เพื่อประเมินประสิทธิผลในเยื่อบุตาก่อนพิจารณาดำเนินการทางคลินิก
- สำหรับ **Trigeminal Autonomic Cephalalgia** (L3, Research Question): พิจารณาออกแบบการศึกษาแบบ Observational เพื่อทดสอบสูตร Metoclopramide + Diphenhydramine ในโรคปวดหัวกลุ่มนี้โดยเฉพาะ
- เปรียบเทียบข้อได้เปรียบ-เสียเปรียบกับยาต้านฮิสตามีนรุ่นใหม่ที่มีทะเบียนในไทยแล้ว ก่อนพิจารณาการลงทุนพัฒนาตลาด
---

