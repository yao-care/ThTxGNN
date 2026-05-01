---
layout: default
title: Primaquine
parent: การคาดการณ์จากโมเดล (L5)
nav_order: 129
evidence_level: L5
indication_count: 10
---

# Primaquine
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

---

# Primaquine: จากมาลาเรียสู่ปอดอักเสบ Pneumocystis jirovecii (PCP)

## สรุปสั้นๆ

Primaquine เป็นยาต้านมาลาเรียกลุ่ม 8-aminoquinoline ที่ใช้เป็นมาตรฐานสากลสำหรับการรักษาแบบรากถอนโคน (*radical cure*) ของ *Plasmodium vivax* และ *P. ovale* รวมถึงยับยั้งการแพร่เชื้อไปยังยุงผ่านฤทธิ์ gametocytocidal แม้ยังไม่มีทะเบียนยาในประเทศไทย โมเดล TxGNN คาดการณ์ว่า Primaquine อาจมีประสิทธิผลต่อ **ปอดอักเสบ Pneumocystis jirovecii (Pneumocystosis/PCP)** ซึ่งเป็นโรคฉวยโอกาสร้ายแรงในผู้ป่วยภูมิคุ้มกันบกพร่อง ปัจจุบันมี **การทดลองทางคลินิก 6 รายการ** รวม Phase 3 RCT โดยตรง และ **วรรณกรรม 20 ฉบับ** รวม meta-analysis ปี 2025 ที่สนับสนุนการใช้ Clindamycin + Primaquine เป็น second-line therapy สำหรับ PCP อย่างชัดเจน

> **หมายเหตุด้านวิธีวิทยา**: TxGNN ให้คะแนนสูงสุดแก่กลุ่ม myiasis (สกอร์ 99.75%, อันดับ 1–4) แต่การทำนายนี้เป็นผลจากความใกล้ชิดในกราฟเครือข่าย (network proximity artifact) โดยปราศจากพื้นฐานกลไกหรือหลักฐานใดๆ รายงานฉบับนี้จึงมุ่งเน้นที่ **pneumocystosis** (อันดับ 8, สกอร์ 99.32%) ซึ่งมีหลักฐานทางคลินิกระดับ L1 และความสมเหตุสมผลทางชีวเคมีที่พิสูจน์แล้ว

---

## ภาพรวมฉบับย่อ

| รายการ | เนื้อหา |
|--------|---------|
| ข้อบ่งใช้เดิม | มาลาเรีย (*P. vivax/ovale* radical cure, gametocytocidal) — รับรองระดับสากล ยังไม่มีทะเบียนในไทย |
| ข้อบ่งใช้ใหม่ที่ทำนาย | Pneumocystosis (ปอดอักเสบจาก *Pneumocystis jirovecii*) |
| คะแนนการทำนาย TxGNN | 99.32% |
| ระดับหลักฐาน | L1 (มี Phase 3 RCT ที่เสร็จสมบูรณ์หลายรายการ) |
| สถานะการวางจำหน่ายในไทย | ✗ ยังไม่มีทะเบียนยา |
| จำนวนใบอนุญาต | 0 รายการ |
| คำแนะนำในการตัดสินใจ | Proceed with Guardrails |

---

## ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

Primaquine ออกฤทธิ์โดยหลักผ่านการรบกวนห่วงโซ่การลำเลียงอิเล็กตรอนในไมโทคอนเดรียของปรสิต (mitochondrial electron transport chain) ทำให้เกิดสารออกซิไดซ์ที่เป็นพิษเฉพาะต่อเซลล์เป้าหมาย กลไกนี้อธิบายฤทธิ์ต้าน *Plasmodium* ทั้งในระยะ hypnozoite ในตับและระยะ gametocyte ในกระแสเลือด

*Pneumocystis jirovecii* แม้จัดจำแนกเป็นเชื้อราในปัจจุบัน แต่มีชีววิทยาหลายด้านที่แตกต่างจากเชื้อราทั่วไป โดยเฉพาะการพึ่งพาพลังงานจากไมโทคอนเดรียในระยะ trophic form ที่เกาะผนังถุงลม การทดสอบ in vitro ปี 1988 (PMID 3261959) พบว่า Primaquine เพียงตัวเดียวสามารถลดจำนวน *Pneumocystis* ในการเพาะเลี้ยงได้ถึง >93% เทียบกับกลุ่มควบคุม และเมื่อผสมกับ Clindamycin จะเกิดฤทธิ์เสริมแบบ additive synergy ซึ่ง Clindamycin ยับยั้งการสังเคราะห์โปรตีนผ่าน 80S ribosome ของ *P. jirovecii*

ในทางคลินิก Phase 3 RCT (NCT00000640, n=290) ยืนยันว่า Clindamycin + Primaquine มีประสิทธิผลเทียบเท่า TMP-SMX มาตรฐานสำหรับ PCP ระดับเล็กน้อยถึงปานกลางในผู้ป่วย AIDS ผลนี้ได้รับการยืนยันซ้ำจากการศึกษาหลายรายการและ meta-analysis ปี 2025 (PMID 39732393) ปัจจุบัน ECIL, British HIV Association, และ IDSA ต่างบรรจุ Clindamycin/Primaquine ไว้เป็น second-line therapy อย่างเป็นทางการ เมื่อ TMP-SMX ใช้ไม่ได้

---

## หลักฐานจากการทดลองทางคลินิก

| หมายเลขการทดลอง | ระยะ | สถานะ | จำนวนผู้เข้าร่วม | ผลลัพธ์หลัก |
|----------------|------|--------|-----------------|------------|
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Phase 3 | เสร็จสิ้น | 290 | เปรียบเทียบ Dapsone/TMP, **Clindamycin/Primaquine** และ TMP-SMX ใน PCP ระดับเล็กน้อย-ปานกลางในผู้ป่วย AIDS |
| [NCT00000717](https://clinicaltrials.gov/study/NCT00000717) | N/A | เสร็จสิ้น | 50 | ประเมินความปลอดภัยและประสิทธิผลของ **Clindamycin + Primaquine** ใน PCP ระดับเล็กน้อยในผู้ป่วย AIDS |
| [NCT07357103](https://clinicaltrials.gov/study/NCT07357103) | Phase 4 | ยังไม่เปิดรับสมัคร | 416 | ประเมินตำแหน่งของ PCP second-line therapies (รวม **Clindamycin/Primaquine**) เมื่อ TMP-SMX ใช้ไม่ได้ — ผลลัพธ์จะกำหนดมาตรฐานใหม่ |
| [NCT04328688](https://clinicaltrials.gov/study/NCT04328688) | N/A | เสร็จสิ้น | 30 | ประสิทธิผล Clindamycin-TMP/SMX ใน PCP หลังปลูกถ่ายอวัยวะแข็ง (non-HIV immunocompromised) |
| [NCT06691321](https://clinicaltrials.gov/study/NCT06691321) | N/A | กำลังรับสมัคร | 60 | ประเมิน Caspofungin เป็นทางเลือกรักษา PCP ใน HIV/AIDS (บริบทการเปรียบเทียบกับ standard care) |
| [NCT00636935](https://clinicaltrials.gov/study/NCT00636935) | Phase 4 | ถอนออก (enrolled=0) | 0 | ผลของ Corticosteroid ต่อพังผืดในปอดใน PCP ระดับเล็กน้อย |

---

## หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|-----|--------|--------|------------|
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Meta-analysis | Clin Microbiol Infect | Network meta-analysis ของ RCTs ทั้งหมดสำหรับ PCP ใน HIV: ยืนยัน Clindamycin+Primaquine เป็น alternative ที่มีประสิทธิผลและ safety profile ที่ยอมรับได้ |
| [9770152](https://pubmed.ncbi.nlm.nih.gov/9770152/) | 1998 | RCT (double-blind) | Clin Infect Dis | CTN 004 (n=87, multicenter): Clindamycin/Primaquine ประสิทธิผลโดยรวมเทียบเท่า TMP-SMZ ใน AIDS-related PCP |
| [2060532](https://pubmed.ncbi.nlm.nih.gov/2060532/) | 1991 | Cohort | Eur J Clin Microbiol Infect Dis | Primary treatment: 91% (20/22 ราย) ของผู้ป่วย AIDS ที่ใช้ Clindamycin IV + Primaquine ปากมีอาการดีขึ้นชัดเจน |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Review | Expert Opin Pharmacother | ทบทวนการป้องกันและรักษา PCP: Clindamycin+Primaquine แนะนำเป็น second-line ทั้งใน HIV และ non-HIV immunocompromised |
| [27550993](https://pubmed.ncbi.nlm.nih.gov/27550993/) | 2016 | Guidelines | J Antimicrob Chemother | ECIL guidelines: บรรจุ Clindamycin/Primaquine เป็น second-line อย่างเป็นทางการในผู้ป่วยโลหิตวิทยาที่แพ้ TMP-SMX |
| [36969352](https://pubmed.ncbi.nlm.nih.gov/36969352/) | 2023 | Review | Avicenna J Med | ทบทวน PCP management ใน HIV และ non-HIV: incidence กำลังเพิ่มในกลุ่ม non-HIV; Clindamycin+Primaquine เป็น alternative สำคัญ |
| [8086551](https://pubmed.ncbi.nlm.nih.gov/8086551/) | 1994 | Cohort | Clin Infect Dis | ACTG 044: Clindamycin IV + Primaquine ปากปลอดภัยและมีประสิทธิผลเป็น primary therapy ใน AIDS-related PCP |
| [18971152](https://pubmed.ncbi.nlm.nih.gov/18971152/) | 2008 | Review | J Formos Med Assoc | ทบทวน PCP จากมุมมองไต้หวัน: ยืนยัน Clindamycin+Primaquine เป็น alternative ในกรณีแพ้หรือดื้อ TMP-SMX |
| [3261959](https://pubmed.ncbi.nlm.nih.gov/3261959/) | 1988 | In vitro | Antimicrob Agents Chemother | หลักฐานพื้นฐาน: Primaquine ลด *Pneumocystis* ≥93% ในหลอดทดลอง; Clindamycin+Primaquine เกิด additive synergy |
| [36160421](https://pubmed.ncbi.nlm.nih.gov/36160421/) | 2022 | Review | Front Pharmacol | การรักษา PCP ในผู้ขาด G6PD: Primaquine เป็นสารออกซิไดซ์ที่ต้องใช้ด้วยความระมัดระวังหรือหลีกเลี่ยง |

---

## ข้อพิจารณาด้านความปลอดภัย

กรุณาดูข้อมูลความปลอดภัยฉบับสมบูรณ์ในเอกสารกำกับยา (DrugBank DB01087, WHO Essential Medicines, FDA Label)

**ข้อพิจารณาวิกฤตที่ปรากฏซ้ำในวรรณกรรมทุกฉบับ และต้องคำนึงถึงก่อนใช้ยา:**

- **ความเสี่ยงหลัก**: ภาวะเม็ดเลือดแดงแตกเฉียบพลัน (acute hemolytic anemia) ในผู้ขาดเอนไซม์ Glucose-6-Phosphate Dehydrogenase (G6PD) — อัตราการขาด G6PD ในประชากรไทยอยู่ที่ประมาณ 3–15% ขึ้นกับกลุ่มชาติพันธุ์
- **ข้อกำหนดก่อนใช้**: **ต้องตรวจ G6PD ทุกรายก่อนเริ่มยา** — ห้ามใช้ในผู้ขาด G6PD ระดับรุนแรง

---

## สรุปและขั้นตอนถัดไป

**การตัดสินใจ: Proceed with Guardrails**

**เหตุผล:**
Clindamycin + Primaquine มี Phase 3 RCT และ meta-analysis ปี 2025 รับรองประสิทธิผลเทียบเท่า TMP-SMX สำหรับ PCP และถูกบรรจุในแนวทางคลินิกนานาชาติชั้นนำ (ECIL, IDSA) อย่างเป็นทางการแล้ว แต่ยาไม่มีทะเบียนในไทยและมีความเสี่ยง hemolysis เฉพาะกลุ่มที่ขาด G6PD ซึ่งพบได้บ่อยในประชากรเอเชียตะวันออกเฉียงใต้

**หากต้องการดำเนินการต่อต้อง:**
- ยื่นขอนำเข้ายาเฉพาะราย (Special Import Authorization) หรือ Compassionate Use ผ่าน อย. ไทย
- กำหนดโปรโตคอล **ตรวจ G6PD บังคับ** ก่อนเริ่มยาในผู้ป่วยทุกราย (Point-of-care test แนะนำ)
- วางแผนติดตาม CBC, Hemoglobin, Reticulocyte count ระหว่างการรักษา
- จัดทำ Risk Management Plan (RMP) ครอบคลุมความเสี่ยง hemolytic anemia
- ดาวน์โหลดและวิเคราะห์ TFDA package insert หากมีการยื่นขึ้นทะเบียนในอนาคต
- ประสานงานกับแพทย์เฉพาะทางโรคติดเชื้อและเภสัชกรผู้เชี่ยวชาญก่อนนำไปใช้ในทางคลินิก
---

