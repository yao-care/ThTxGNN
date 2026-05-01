---
layout: default
title: Dexamethasone
parent: หลักฐานระดับสูง (L1-L2)
nav_order: 52
evidence_level: L2
indication_count: 10
---

# Dexamethasone
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

ใช้ `txgnn-pipeline` เพื่อตรวจสอบบริบทการทำงาน — skill นี้ครอบคลุมการ deploy หลายประเทศรวมถึง Thailand (Th) แต่ไม่ได้กำหนดรูปแบบรายงาน ซึ่ง prompt ในระบบได้ระบุ format ไว้แล้วอย่างละเอียด จึงดำเนินการสร้างรายงานได้เลย

---

# Dexamethasone: จากยาต้านการอักเสบและกดภูมิคุ้มกันสู่โรคผมร่วงเป็นหย่อม

## สรุปสั้นๆ

Dexamethasone เป็นยากลุ่มคอร์ติโคสเตียรอยด์สังเคราะห์ที่ใช้กันอย่างแพร่หลายในฐานะยาต้านการอักเสบและกดภูมิคุ้มกัน โมเดล TxGNN คาดการณ์ว่าอาจมีผลในการรักษา **โรคผมร่วงเป็นหย่อม (Alopecia Areata)** ปัจจุบันมี **การทดลองทางคลินิก 13 รายการ** และ **วรรณกรรม 20 ฉบับ** สนับสนุนแนวทางนี้

---

## ภาพรวมฉบับย่อ

| รายการ | เนื้อหา |
|------|------|
| ข้อบ่งใช้เดิม | ยาคอร์ติโคสเตียรอยด์ (ต้านการอักเสบ / กดภูมิคุ้มกัน) — ไม่มีทะเบียนยาในประเทศไทย |
| ข้อบ่งใช้ใหม่ที่ทำนาย | โรคผมร่วงเป็นหย่อม (Alopecia Areata) |
| คะแนนการทำนาย TxGNN | 99.99% |
| ระดับหลักฐาน | L2 |
| สถานะการวางจำหน่ายในไทย | ❌ ยังไม่มีทะเบียนยาในประเทศไทย |
| จำนวนใบอนุญาต | 0 รายการ |
| คำแนะนำในการตัดสินใจ | Proceed with Guardrails |

---

## ทำไมการคาดการณ์นี้จึงสมเหตุสมผล?

Dexamethasone เป็นคอร์ติโคสเตียรอยด์สังเคราะห์ที่ออกฤทธิ์โดยยับยั้งไซโตไคน์กระตุ้นการอักเสบ โดยเฉพาะ IL-2 และ IFN-γ ซึ่งเป็นตัวกระตุ้นหลักของเซลล์ T อัตโนภูมิที่ล้อมรอบรูขุมขน การยับยั้งนี้ช่วยปกป้องเยื่อบุรูขุมขนจากการถูกทำลายโดยกระบวนการภูมิคุ้มกัน ซึ่งเป็นกลไกพื้นฐานของโรคผมร่วงเป็นหย่อม

โรคผมร่วงเป็นหย่อม (Alopecia Areata) เป็นโรคผิวหนังอัตโนภูมิที่เซลล์ T ตรงเข้าโจมตีรูขุมขนโดยเฉพาะ กลไกนี้สอดคล้องโดยตรงกับการออกฤทธิ์กดภูมิคุ้มกันของ Dexamethasone โดยเฉพาะในรูปแบบการบริหารยาแบบ **oral mini-pulse** (รับประทาน 5 มก. 2 วันติดต่อกันต่อสัปดาห์) ซึ่งออกแบบมาเพื่อให้ได้ระดับการกดภูมิคุ้มกันสูงชั่วคราวในขณะที่ลดผลข้างเคียงสะสมจากการใช้คอร์ติโคสเตียรอยด์ต่อเนื่อง

หลักฐานทางคลินิกที่รองรับการใช้งานนี้มีทั้ง RCT โดยตรงในกลุ่มเด็กที่เปรียบเทียบ dexamethasone mini-pulse กับ DPCP (PMID 36086930) รวมถึง network meta-analysis ที่นำ systemic steroids มาเปรียบเทียบกับ JAK inhibitors (PMID 39042154) และ cohort studies ระยะยาวอีกหลายชิ้น จึงมีทั้งพื้นฐานเชิงกลไกและหลักฐานทางคลินิกรองรับอย่างสมเหตุสมผล

---

## หลักฐานจากการทดลองทางคลินิก

> ⚠️ **หมายเหตุ:** การทดลองที่สืบค้นได้จาก ClinicalTrials.gov เป็นการทดลองยาต้านมะเร็งที่มี Dexamethasone ในฐานะยาสนับสนุน (supportive medication / premedication) **ไม่ใช่** การทดลองสำหรับโรคผมร่วงเป็นหย่อมโดยตรง หลักฐานจากการทดลองที่เกี่ยวข้องโดยตรงกับ alopecia areata อยู่ในส่วนวรรณกรรมด้านล่าง

| หมายเลขการทดลอง | ระยะ | สถานะ | จำนวนผู้เข้าร่วม | ผลลัพธ์หลัก |
|---------|------|------|------|---------|
| [NCT02004275](https://clinicaltrials.gov/study/NCT02004275) | Phase 1/2 | ไม่ทราบ | 118 | Pomalidomide + Dexamethasone ± Ixazomib สำหรับ multiple myeloma ที่กลับเป็นซ้ำ; Dexamethasone เป็นองค์ประกอบหลักของสูตรยา — ให้ข้อมูลขนาดยาและความปลอดภัยที่สามารถอ้างอิงได้ |
| [NCT02288078](https://clinicaltrials.gov/study/NCT02288078) | Phase 2 | ไม่ทราบ | 74 | ประเมินผล prophylactic dexamethasone สำหรับอาการอ่อนเพลียจาก regorafenib ในมะเร็งลำไส้ใหญ่ระยะแพร่กระจาย |
| [NCT02685826](https://clinicaltrials.gov/study/NCT02685826) | Phase 1/2 | เสร็จสิ้น | 56 | Durvalumab + Lenalidomide ± Dexamethasone สำหรับ newly diagnosed multiple myeloma |
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | N/A | เสร็จสิ้น | 380 | ผลของ steroid metabolome ที่ผิดปกติต่อคุณภาพกระดูกและองค์ประกอบร่างกายในผู้ป่วย MACS; ให้ข้อมูล systemic dexamethasone exposure ขนาดใหญ่ |
| [NCT01866449](https://clinicaltrials.gov/study/NCT01866449) | Phase 2 | เสร็จสิ้น | 24 | Cabazitaxel สำหรับ glioblastoma; Dexamethasone เป็นยาร่วมมาตรฐาน |
| [NCT01126736](https://clinicaltrials.gov/study/NCT01126736) | Phase 1/2 | เสร็จสิ้น | 98 | Eribulin + Pemetrexed สำหรับ NSCLC; Dexamethasone เป็น premedication |
| [NCT01055496](https://clinicaltrials.gov/study/NCT01055496) | Phase 1 | เสร็จสิ้น | 103 | R-CVP หรือ R-GDP + Inotuzumab ozogamicin สำหรับ CD22+ non-Hodgkin's lymphoma; R-GDP regimen มี Dexamethasone เป็นองค์ประกอบ |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | เสร็จสิ้น | 19 | Cisplatin + Imatinib + Pemetrexed สำหรับ malignant mesothelioma; Dexamethasone เป็น premedication |
| [NCT01215916](https://clinicaltrials.gov/study/NCT01215916) | Phase 1 | เสร็จสิ้น | 39 | LY573636 + Pemetrexed สำหรับ solid tumors; Dexamethasone เป็นยาสนับสนุน |
| [NCT00282087](https://clinicaltrials.gov/study/NCT00282087) | Phase 2 | เสร็จสิ้น | 47 | Gemcitabine/Docetaxel ตามด้วย Doxorubicin สำหรับ uterine leiomyosarcoma หลังผ่าตัด; Dexamethasone เป็น premedication |

---

## หลักฐานจากวรรณกรรม

| PMID | ปี | ประเภท | วารสาร | ผลลัพธ์หลัก |
|------|-----|------|------|---------|
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | RCT | Dermatologic Therapy | เปรียบเทียบ dexamethasone oral mini-pulse กับ DPCP contact sensitization ใน 30 เด็กที่มี severe AA; ประเมินประสิทธิผลและความปลอดภัยโดยตรง |
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | Meta-analysis | Archives of Dermatological Research | Network meta-analysis เปรียบเทียบ systemic steroids, oral JAK inhibitors และ contact immunotherapy ใน severe AA (SALT ≥ 50%) ตาม PRISMA |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | Cohort | Journal of Clinical Medicine | Prospective cohort ประเมินประสิทธิผลและผลข้างเคียงของ dexamethasone mini-pulse ใน AA ในสถานการณ์จริง พร้อมวิเคราะห์ปัจจัยที่ทำนายการตอบสนอง |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | Cohort | Dermatologic Therapy | Multicentric study ของ oral dexamethasone mini-pulse ใน moderate-severe AA ในยุโรป ประเมินผลลัพธ์และอัตรา relapse |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | Cohort | Dermatologic Therapy | เปรียบเทียบ 1-day กับ 3-day IV dexamethasone pulse ร่วมกับ topical clobetasol ใน 73 เด็กที่มี severe AA (>30% ของหนังศีรษะ) |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | Cohort | Dermatologic Therapy | Long-term follow-up (median 96 เดือน) ของ oral dexamethasone pulse + topical corticosteroid ใน 65 เด็กที่มี severe AA |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | Case series | Journal of Dermatological Treatment | รายงาน durable remission ของ severe AA ด้วย dexamethasone oral mini-pulse พร้อม focused review สำหรับกรณีที่ไม่สามารถใช้ JAK inhibitors ได้ |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatric Dermatology | ทบทวนขนาดยาและวิธีบริหาร pulse dose corticosteroid therapy ในเด็กที่มี AA รวมถึงผลข้างเคียงที่พบบ่อย |
| [23960401](https://pubmed.ncbi.nlm.nih.gov/23960401/) | 2013 | Case series | International Journal of Trichology | รักษา AA ด้วย phenolisation ร่วมกับ IV dexamethasone pulses; บันทึกการตอบสนองและผลข้างเคียง |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | Case series | The Journal of Dermatology | Dexamethasone 5 มก. oral pulse 2 วันต่อเนื่องต่อสัปดาห์ ใน 30 ผู้ป่วย extensive AA; ติดตาม terminal hair growth ขั้นต่ำ 12 สัปดาห์ |

---

## ข้อพิจารณาด้านความปลอดภัย

กรุณาดูข้อมูลความปลอดภัยในเอกสารกำกับยา

---

## สรุปและขั้นตอนถัดไป

**การตัดสินใจ: Proceed with Guardrails**

**เหตุผล:**
มี RCT โดยตรงและ cohort studies ระยะยาวหลายชิ้นรองรับการใช้ dexamethasone mini-pulse ใน alopecia areata รวมถึง network meta-analysis ที่วางตำแหน่งไว้ในบริบทของการรักษา severe AA เปรียบกับ JAK inhibitors; กลไกการกดภูมิคุ้มกันผ่าน IL-2/IFN-γ มีความสมเหตุสมผลทางชีววิทยาสูง และยาถูกใช้จริงในทางคลินิกอยู่แล้ว แม้ยังไม่มีทะเบียนยาในประเทศไทย

**หากต้องการดำเนินการต่อต้อง:**
- ดาวน์โหลดและวิเคราะห์ข้อมูล MOA โดยละเอียดจาก DrugBank API (แก้ไข Data Gap DG002)
- ขอข้อมูลคำเตือนและข้อห้ามใช้จาก TFDA หรือ FDA/EMA (แก้ไข Data Gap DG001 ซึ่งเป็น Blocking)
- ตรวจสอบทะเบียนยาในประเทศไทยซ้ำ เนื่องจาก Dexamethasone เป็นยาหลักในบัญชียาที่ควรมีทะเบียน — ผลการค้นหา 0 รายการอาจเกิดจากปัญหาการสืบค้น
- กำหนดแผนติดตามความปลอดภัยสำหรับผลข้างเคียงของ systemic corticosteroid ในระยะยาว เช่น ภาวะน้ำตาลในเลือดสูง ความดันโลหิตสูง และภาวะกระดูกพรุน
- พิจารณาขอ import license หรือ special access สำหรับการใช้ในบริบท alopecia areata ในประเทศไทย
---

