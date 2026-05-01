---
layout: default
title: Azathioprine
parent: หลักฐานระดับสูง (L1-L2)
nav_order: 23
evidence_level: L1
indication_count: 10
---

# Azathioprine
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

# Azathioprine: จากการกดภูมิคุ้มกันสู่โรคลำไส้อักเสบ (Inflammatory Bowel Disease)

## สรุปสั้นๆ

Azathioprine เป็นยากดภูมิคุ้มกันในกลุ่มพิวรีนอนาล็อก ที่เดิมใช้ในการป้องกันการปฏิเสธการปลูกถ่ายอวัยวะและรักษาโรคภูมิแพ้ตัวเองหลายชนิด
โมเดล TxGNN คาดการณ์ว่ายานี้อาจมีผลต่อ **โรคลำไส้อักเสบ (Inflammatory Bowel Disease)** และ **โรคลำไส้ใหญ่อักเสบเรื้อรัง (Ulcerative Colitis)** ซึ่งทั้งสองมีระดับหลักฐาน L1
ปัจจุบันมี **การทดลองทางคลินิก Phase 3 มากกว่า 10 รายการ** รวมถึง **Cochrane systematic review 4 ฉบับ** และวรรณกรรมกว่า 20 ฉบับ ยืนยันประสิทธิผลของ Azathioprine ในการรักษาและคงสภาวะหายของ IBD/UC

---

## ภาพรวมฉบับย่อ

| รายการ | เนื้อหา |
|------|------|
| ข้อบ่งใช้เดิม | การกดภูมิคุ้มกัน / ป้องกันการปฏิเสธการปลูกถ่ายอวัยวะ |
| ข้อบ่งใช้ใหม่ที่ทำนาย | โรคลำไส้อักเสบ (Inflammatory Bowel Disease) |
| คะแนนการทำนาย TxGNN | 99.52% |
| ระดับหลักฐาน | L1 |
| สถานะการวางจำหน่ายในไทย | ✗ ยังไม่วางจำหน่าย |
| จำนวนใบอนุญาต | 0 รายการ |
| คำแนะนำในการตัดสินใจ | Proceed with Guardrails |

---

## ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

Azathioprine เป็นยาพิวรีนอนาล็อกที่ถูกเปลี่ยนรูปในร่างกายเป็นสารออกฤทธิ์หลัก 6-thioguanine nucleotides (6-TGN) ผ่านกลไกสองทางพร้อมกัน ได้แก่ (1) การแทรกเข้าไปใน DNA ของเซลล์ที่แบ่งตัวเร็ว และ (2) การยับยั้งกระบวนการสังเคราะห์พิวรีน de novo ทำให้ T lymphocyte ที่ถูกกระตุ้นเกิด apoptosis โดยเฉพาะผ่านเส้นทาง Rac1 นอกจากนี้หลักฐานใหม่ยังพบว่า Azathioprine กระตุ้น autophagy ผ่าน mTORC1 และ PERK ซึ่งมีความเกี่ยวข้องโดยตรงกับพยาธิสรีรวิทยาของโรคครอห์น

โรคลำไส้อักเสบ (IBD) ครอบคลุมทั้งโรคครอห์นและ UC โดยมีพยาธิสรีรวิทยาหลักคือการทำงานผิดปกติของระบบภูมิคุ้มกันที่เยื่อบุลำไส้ โดยเฉพาะการกระตุ้นผิดปกติของเส้นทาง Th1/Th17 ซึ่งตรงกับจุดมุ่งหมายหลักของ Azathioprine ที่มุ่งเป้าระงับ T lymphocyte โดยตรง ความสอดคล้องของกลไกนี้ทำให้เกิดการยับยั้งการอักเสบเรื้อรังของเยื่อบุลำไส้ได้อย่างมีประสิทธิผล

Cochrane systematic review ล่าสุด (ปี 2025) พร้อมกับฉบับก่อนหน้า (2012 และ 2016) ตลอดจน Phase 3 RCT หลายรายการ ยืนยันอย่างสม่ำเสมอว่า Azathioprine และ 6-mercaptopurine เป็น immunomodulator แนวหน้าในการรักษาคงสภาวะหาย (maintenance of remission) ทั้งในโรคครอห์นและ UC ความแข็งแกร่งของหลักฐานนี้ทำให้การคาดการณ์จาก TxGNN มีความน่าเชื่อถือสูงในเชิงคลินิก

---

## หลักฐานจากการทดลองทางคลินิก

| หมายเลขการทดลอง | ระยะ | สถานะ | จำนวนผู้เข้าร่วม | ผลลัพธ์หลัก |
|---------|------|------|------|---------|
| [NCT05040464](https://clinicaltrials.gov/study/NCT05040464) | Phase 3 | กำลังรับสมัคร | 166 | RCT เปิด เปรียบเทียบ Azathioprine กับ Methotrexate ร่วมกับ Adalimumab ในโรคครอห์น |
| [NCT00094458](https://clinicaltrials.gov/study/NCT00094458) | Phase 3 | เสร็จสิ้น | 508 | Infliximab vs Azathioprine vs IFX+AZA ในผู้ป่วยโรคครอห์นที่ไม่เคยใช้ immunomodulator มาก่อน |
| [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) | Phase 3 | ไม่ทราบ | 84 | Low-dose Azathioprine + Allopurinol vs Azathioprine เดี่ยวในผู้ป่วย Ulcerative Colitis |
| [NCT03185611](https://clinicaltrials.gov/study/NCT03185611) | Phase 3 | ไม่ทราบ | 120 | Rifaximin + Thiopurine vs Thiopurine เดี่ยวในการป้องกันการกลับเป็นซ้ำหลังผ่าตัดโรคครอห์น |
| [NCT02425852](https://clinicaltrials.gov/study/NCT02425852) | Phase 4 | เสร็จสิ้น | 65 | Early Infliximab+AZA vs Steroids+AZA ใน Acute Severe Ulcerative Colitis |
| [NCT00537316](https://clinicaltrials.gov/study/NCT00537316) | Phase 3 | ยุติก่อนกำหนด | 242 | Infliximab ± Azathioprine vs Azathioprine เดี่ยวใน Moderate-to-Severe Ulcerative Colitis |
| [NCT01564823](https://clinicaltrials.gov/study/NCT01564823) | Phase 3 | เสร็จสิ้น | 86 | Adalimumab vs Azathioprine ในการป้องกันการกลับเป็นซ้ำของโรคครอห์นหลังผ่าตัด (52 สัปดาห์) |
| [NCT00976690](https://clinicaltrials.gov/study/NCT00976690) | Phase 3 | เสร็จสิ้น | 83 | Azathioprine vs Mesalazine ในการป้องกันการกลับเป็นซ้ำหลังผ่าตัดโรคครอห์น |
| [NCT07424040](https://clinicaltrials.gov/study/NCT07424040) | N/A | ยังไม่รับสมัคร | 154 | Infliximab เดี่ยว vs Infliximab + Azathioprine ในโรคครอห์นในเด็ก: ประสิทธิผลและความปลอดภัยระยะยาว |
| [NCT07235904](https://clinicaltrials.gov/study/NCT07235904) | Phase 4 | กำลังรับสมัคร | 300 | Mirikizumab (top-down) vs Azathioprine (standard of care) ในผู้ป่วย UC ที่ได้รับการวินิจฉัยใหม่ |

---

## หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|-----|------|------|---------|
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | Meta-analysis | Cochrane Database Syst Rev | AZA/6-MP ในการรักษาคงสภาวะหายใน UC: Cochrane review อัปเดตล่าสุด ครอบคลุมหลักฐานจากหลาย RCT |
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | RCT | Gut | ACTIVE trial: Top-down IFX+AZA vs AZA เดี่ยวใน Acute Severe UC ที่ตอบสนองต่อ IV steroids |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | Meta-analysis | Cochrane Database Syst Rev | AZA/6-MP ในการรักษาคงสภาวะหายใน UC: Cochrane review ปี 2016 |
| [22972046](https://pubmed.ncbi.nlm.nih.gov/22972046/) | 2012 | Meta-analysis | Cochrane Database Syst Rev | AZA/6-MP ในการรักษาคงสภาวะหายใน UC: Cochrane review ปี 2012 |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | Meta-analysis | Aliment Pharmacol Ther | Meta-analysis ยืนยันประสิทธิผลของ AZA/6-MP ใน UC แม้หลักฐานก่อนหน้ายังมีข้อถกเถียง |
| [9412914](https://pubmed.ncbi.nlm.nih.gov/9412914/) | 1997 | RCT | J Clin Gastroenterol | AZA ใน UC ที่ดื้อ/พึ่งพา steroids จำนวน 56 ราย: ประสิทธิผลดี ติดตามเฉลี่ย 29 เดือน |
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | Cohort | Cell Reports Medicine | Blautia wexlerae ในลำไส้เพิ่มความเสี่ยง AZA therapy failure ใน IBD โดยลด 6-MP bioavailability |
| [36462311](https://pubmed.ncbi.nlm.nih.gov/36462311/) | 2023 | Cohort | Biomed Pharmacother | TPMT gene methylation ส่งผลต่อ AZA pharmacokinetics ในเด็กที่เป็น Very Early Onset IBD |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Review | J Crohn's Colitis | Thiopurines ใน IBD: ผลการวิจัยใหม่เกี่ยวกับ thioguanine, TPMT/NUDT15 และแนวทางปฏิบัติทางคลินิก |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | Review | Expert Rev Gastroenterol Hepatol | Azathioprine ใน IBD: กลไกโมเลกุลใหม่ที่เข้าใจ ได้แก่ Rac1 pathway และนัยยะทางคลินิก |

---

## ข้อพิจารณาด้านความปลอดภัย

กรุณาดูข้อมูลความปลอดภัยในเอกสารกำกับยา

---

## สรุปและขั้นตอนถัดไป

**การตัดสินใจ: Proceed with Guardrails**

**เหตุผล:**
Azathioprine มีหลักฐานระดับ L1 รองรับการใช้ใน IBD และ UC อย่างแข็งแกร่ง ประกอบด้วย Cochrane systematic review 4 ฉบับและ Phase 3 RCT หลายรายการที่ยืนยันประสิทธิผลในการรักษาคงสภาวะหาย อย่างไรก็ตาม ยายังไม่ได้ขึ้นทะเบียนในประเทศไทยและขาดข้อมูลความปลอดภัยจากสำนักงาน อย. จึงต้องดำเนินการอย่างระมัดระวัง

**หากต้องการดำเนินการต่อต้อง:**
- ยื่นขอขึ้นทะเบียนยากับ อย. ไทย หรือขอ special import permit สำหรับการนำไปใช้ทางคลินิก
- ดาวน์โหลดและวิเคราะห์เอกสารกำกับยา (package insert) เพื่อรวบรวมคำเตือน ข้อห้ามใช้ และปฏิกิริยาระหว่างยา
- ดำเนินการตรวจ TPMT และ NUDT15 R139C genotyping ก่อนเริ่มยา เพื่อลดความเสี่ยงต่อ thiopurine-induced leukopenia
- วางแผนติดตาม CBC (รวมแยกชนิด) การทำงานของตับไต และอิเล็กโทรไลต์อย่างสม่ำเสมอระหว่างการรักษา
- พิจารณาออกแบบการทดลองทางคลินิกในประชากรไทยสำหรับกลุ่ม IBD ที่ดื้อต่อ 5-ASA
---

