---
layout: default
title: ทรัพยากรการเชื่อมต่อ
parent: SMART on FHIR
nav_order: 3
description: ทรัพยากรภายนอกที่ ThTxGNN SMART App เชื่อมต่อ รวมถึงการค้นหาการทดลองทางคลินิก การตรวจสอบปฏิกิริยาระหว่างยา และบริการ CDS Hooks
permalink: /smart/integrations/
---

# ทรัพยากรการเชื่อมต่อ

ThTxGNN SMART App เชื่อมต่อกับทรัพยากรภายนอกหลายแห่งเพื่อให้การสนับสนุนการตัดสินใจทางคลินิกที่ครบถ้วนยิ่งขึ้น

---

## การค้นหาการทดลองทางคลินิก

แต่ละข้อบ่งใช้ที่คาดการณ์จะมีปุ่ม "การทดลองทางคลินิก" สำหรับค้นหาการทดลองทางคลินิกที่เกี่ยวข้องจาก ClinicalTrials.gov แบบเรียลไทม์

| ทรัพยากร | คำอธิบาย | ลิงก์ |
|------|------|------|
| **ClinicalTrials.gov API v2** | ฐานข้อมูลการทดลองทางคลินิกของ NIH สหรัฐอเมริกา ให้บริการค้นหาการทดลองทางคลินิกทั่วโลก | [เอกสาร API](https://clinicaltrials.gov/data-api/api) |

### รายละเอียดฟังก์ชัน

- ค้นหาการทดลองทางคลินิกที่เกี่ยวข้องกับยา + ข้อบ่งใช้แบบเรียลไทม์
- แสดงสถานะการทดลอง (กำลังรับสมัคร, ดำเนินการอยู่, เสร็จสมบูรณ์ ฯลฯ)
- แสดงระยะการทดลอง (Phase 1-4)
- ลิงก์โดยตรงไปยังหน้ารายละเอียดบน ClinicalTrials.gov

---

## การตรวจสอบปฏิกิริยาระหว่างยา

เมื่อค้นหายาหลายตัว ระบบจะตรวจสอบปฏิกิริยาระหว่างยา (DDI) โดยอัตโนมัติและแสดงคำเตือน

| ทรัพยากร | คำอธิบาย | ลิงก์ |
|------|------|------|
| **DDInter 2.0** | รวบรวมปฏิกิริยาระหว่างยา 222,391 รายการ ครอบคลุมยา 2,310 ชนิด | [เว็บไซต์ DDInter](https://ddinter2.scbdd.com/) |
| **Guide to PHARMACOLOGY** | คู่มือเภสัชวิทยา IUPHAR/BPS ข้อมูลปฏิกิริยาระหว่างยาที่ได้รับอนุมัติ | [เว็บไซต์อย่างเป็นทางการ](https://www.guidetopharmacology.org/) |

### ระดับคำเตือน

| ระดับ | คำอธิบาย | สีที่แสดง |
|------|------|----------|
| **Major (รุนแรง)** | ต้องการความสนใจทันที อาจเป็นอันตรายถึงชีวิต | แดง |
| **Moderate (ปานกลาง)** | ต้องการความสนใจ อาจต้องปรับเปลี่ยน | เหลือง |
| **Minor (เล็กน้อย)** | ความเสี่ยงเล็กน้อย แจ้งให้ทราบเพียงพอ | น้ำเงิน |

### ปฏิกิริยาสำคัญที่ครอบคลุม

- Warfarin + NSAIDs (ความเสี่ยงเลือดออก)
- Colchicine + สารยับยั้ง CYP3A4 (ความเสี่ยงพิษ)
- การใช้ยาร่วมกันที่ยืด QT (ความเสี่ยงหัวใจเต้นผิดจังหวะ)
- Digoxin + Amiodarone (พิษ Digoxin)
- SSRI + Tramadol (กลุ่มอาการเซโรโทนิน)

---

## บริการ CDS Hooks

ThTxGNN ให้บริการ CDS Hooks ที่สามารถรวมเข้ากับขั้นตอนการสั่งยาของระบบ EHR

### บริการที่มี

| Service ID | Hook | คำอธิบาย |
|---------|------|------|
| `thtxgnn-ddi-check` | order-sign | ตรวจสอบปฏิกิริยาระหว่างยาเมื่อสั่งยา |
| `thtxgnn-repurposing` | order-sign | แสดงการคาดการณ์ข้อบ่งใช้ใหม่ |
| `thtxgnn-trial-match` | patient-view | จับคู่การทดลองทางคลินิก |

### Service Endpoint

**Service Discovery Endpoint**: [/cds-hooks/cds-services.json](/cds-hooks/cds-services.json)

<div style="margin: 20px 0;">
  <a href="/cds-hooks/demo.html" style="display: inline-block; padding: 12px 24px; background: #17a2b8; color: white; text-decoration: none; border-radius: 8px; font-weight: 500;">ทดสอบ CDS Hooks Demo</a>
</div>

### วิธีการเชื่อมต่อ

1. ลงทะเบียน service discovery endpoint กับระบบ EHR ของคุณ
2. กำหนดค่า prefetch เพื่อให้ทรัพยากร MedicationRequest
3. เรียกใช้บริการเมื่อ order-sign hook ถูกเรียก
4. แสดง cards ที่ส่งกลับมาให้บุคลากรทางคลินิก

---

## เอกสารอ้างอิงมาตรฐาน

| มาตรฐาน | คำอธิบาย | ลิงก์ |
|------|------|------|
| **HL7 PDDI-CDS IG** | คู่มือการใช้งานการสนับสนุนการตัดสินใจทางคลินิกสำหรับปฏิกิริยาระหว่างยา | [GitHub](https://github.com/HL7/PDDI-CDS) |
| **CDS Hooks** | มาตรฐานการสนับสนุนการตัดสินใจทางคลินิก SMART on FHIR | [ข้อกำหนดอย่างเป็นทางการ](https://cds-hooks.org/) |
| **CQL (Clinical Quality Language)** | ภาษาคุณภาพทางคลินิก ใช้สำหรับกำหนดกฎการตัดสินใจ | [HL7 CQL](https://cql.hl7.org/) |

---

## คลัง CQL Rules

ThTxGNN มีกฎการตรวจสอบ DDI ในรูปแบบ CQL ที่สามารถใช้รวมเข้ากับระบบ CDS ที่เป็นไปตามมาตรฐาน

**ไฟล์ CQL**: [/cql/ThTxGNN_DDI_CDS.cql](/cql/ThTxGNN_DDI_CDS.cql)

### กฎที่รวมอยู่

- การตรวจสอบปฏิกิริยา Warfarin-NSAID
- การตรวจสอบปฏิกิริยา Metformin-สารทึบรังสี
- การตรวจสอบ Colchicine-สารยับยั้ง CYP3A4
- การตรวจสอบการใช้ยาร่วมกันที่ยืด QT
- การตรวจสอบความเสี่ยงกลุ่มอาการเซโรโทนิน

---

## ลิงก์ทรัพยากรภายนอก

| ทรัพยากร | คำอธิบาย | ลิงก์ |
|------|------|------|
| ClinicalTrials.gov | ค้นหาการทดลองทางคลินิก | [clinicaltrials.gov](https://clinicaltrials.gov/) |
| DDInter 2.0 | ฐานข้อมูลปฏิกิริยาระหว่างยา | [ddinter2.scbdd.com](https://ddinter2.scbdd.com/) |
| Guide to PHARMACOLOGY | ฐานข้อมูลเภสัชวิทยา | [guidetopharmacology.org](https://www.guidetopharmacology.org/) |
| HL7 PDDI-CDS IG | คู่มือการใช้งาน PDDI | [GitHub](https://github.com/HL7/PDDI-CDS) |
| CDS Hooks | มาตรฐานการสนับสนุนการตัดสินใจทางคลินิก | [cds-hooks.org](https://cds-hooks.org/) |
| HL7 CQL | ภาษาคุณภาพทางคลินิก | [cql.hl7.org](https://cql.hl7.org/) |
