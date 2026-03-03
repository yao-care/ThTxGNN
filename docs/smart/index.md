---
layout: default
title: SMART on FHIR
nav_order: 2
has_children: true
description: "แอปพลิเคชัน ThTxGNN SMART on FHIR - อ่านข้อมูลยาจาก EHR และค้นหาข้อบ่งใช้ใหม่"
permalink: /smart/
---

# แอปพลิเคชัน SMART on FHIR

ThTxGNN มีการเชื่อมต่อ SMART on FHIR ทำให้สถานพยาบาลสามารถอ่านข้อมูลยาของผู้ป่วยจากระบบเวชระเบียนอิเล็กทรอนิกส์ (EHR) และค้นหาข้อบ่งใช้ใหม่โดยอัตโนมัติ

---

## SMART on FHIR คืออะไร?

SMART on FHIR เป็นมาตรฐานเปิดที่ช่วยให้แอปพลิเคชันทางการแพทย์สามารถเข้าถึงข้อมูลจากระบบเวชระเบียนอิเล็กทรอนิกส์ได้อย่างปลอดภัย:

- แอปพลิเคชันสามารถรับอนุญาตจากระบบ EHR
- อ่านข้อมูลยาที่ผู้ป่วยใช้อยู่ การวินิจฉัย ฯลฯ
- เชื่อมต่อกับขั้นตอนการทำงานของ EHR ได้อย่างราบรื่น

---

## คุณสมบัติ

| คุณสมบัติ | คำอธิบาย |
|-----------|----------|
| **อ่านข้อมูลยาผู้ป่วย** | อ่านรายการยาที่ผู้ป่วยใช้อยู่จาก EHR โดยอัตโนมัติ |
| **แมปยา** | แปลงรหัสยา RxNorm เป็นฐานข้อมูล ThTxGNN |
| **ค้นหาข้อบ่งใช้ใหม่** | แสดงข้อบ่งใช้ใหม่ที่คาดการณ์สำหรับยาแต่ละตัว |
| **ระบุระดับหลักฐาน** | แสดงระดับหลักฐานแต่ละการคาดการณ์ (L1-L5) อย่างชัดเจน |
| **ค้นหาการทดลองทางคลินิก** | ค้นหา ClinicalTrials.gov แบบเรียลไทม์ |
| **ปฏิกิริยาระหว่างยา** | ตรวจสอบ DDI และแสดงคำเตือนโดยอัตโนมัติ |

---

## เริ่มต้นใช้งาน

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
  <div style="padding: 1.5rem; background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); border-radius: 12px; border: 2px solid #4caf50;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🎯</div>
    <strong style="font-size: 1.1rem; color: #2e7d32;">โหมดทดสอบอิสระ</strong>
    <p style="color: #555; margin: 0.5rem 0 1rem;">ทดสอบฟังก์ชันโดยไม่ต้องเชื่อมต่อ EHR ป้อนชื่อยาโดยตรง</p>
    <a href="standalone.html" style="display: inline-block; padding: 8px 16px; background: #4caf50; color: white; text-decoration: none; border-radius: 6px; font-size: 0.9rem;">ทดลองใช้ →</a>
  </div>
  <div style="padding: 1.5rem; background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); border-radius: 12px; border: 2px solid #2196f3;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">📖</div>
    <strong style="font-size: 1.1rem; color: #1565c0;">คู่มือการใช้งาน</strong>
    <p style="color: #555; margin: 0.5rem 0 1rem;">สอนการใช้งาน ThTxGNN SMART App พร้อมภาพประกอบ</p>
    <a href="guide/" style="display: inline-block; padding: 8px 16px; background: #2196f3; color: white; text-decoration: none; border-radius: 6px; font-size: 0.9rem;">ดูคู่มือ →</a>
  </div>
  <div style="padding: 1.5rem; background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); border-radius: 12px; border: 2px solid #ff9800;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚙️</div>
    <strong style="font-size: 1.1rem; color: #e65100;">เอกสารเทคนิค</strong>
    <p style="color: #555; margin: 0.5rem 0 1rem;">การตั้งค่า OAuth, FHIR API, ขั้นตอนการแมปยา</p>
    <a href="technical-docs/" style="display: inline-block; padding: 8px 16px; background: #ff9800; color: white; text-decoration: none; border-radius: 6px; font-size: 0.9rem;">ข้อมูลเทคนิค →</a>
  </div>
  <div style="padding: 1.5rem; background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%); border-radius: 12px; border: 2px solid #9c27b0;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔗</div>
    <strong style="font-size: 1.1rem; color: #7b1fa2;">ทรัพยากรการเชื่อมต่อ</strong>
    <p style="color: #555; margin: 0.5rem 0 1rem;">ClinicalTrials.gov, ตรวจสอบ DDI, CDS Hooks</p>
    <a href="integrations/" style="display: inline-block; padding: 8px 16px; background: #9c27b0; color: white; text-decoration: none; border-radius: 6px; font-size: 0.9rem;">ดูการเชื่อมต่อ →</a>
  </div>
</div>

---

## โครงสร้างเอกสาร

| หน้า | คำอธิบาย |
|------|----------|
| [คู่มือการใช้งาน](guide/) | สอนการใช้งานพร้อมภาพ เหมาะสำหรับผู้ใช้ทั่วไป |
| [เอกสารเทคนิค](technical-docs/) | การตั้งค่า FHIR, API endpoints สำหรับนักพัฒนา |
| [ทรัพยากรการเชื่อมต่อ](integrations/) | การเชื่อมต่อและลิงก์แหล่งข้อมูลภายนอก |

---

## ข้อจำกัดความรับผิดชอบ

<div style="background: #fff3cd; border: 1px solid #ffc107; border-radius: 8px; padding: 16px; margin: 20px 0;">
<strong>ข้อควรทราบ</strong><br>
เนื้อหาในเว็บไซต์นี้มีไว้เพื่อการวิจัยเท่านั้น ไม่สามารถทดแทนคำแนะนำทางการแพทย์จากผู้เชี่ยวชาญ ผลการคาดการณ์การใช้ยาเก่าในข้อบ่งใช้ใหม่ต้องผ่านการทดลองทางคลินิกก่อนนำไปใช้ หากมีปัญหาสุขภาพ กรุณาปรึกษาแพทย์หรือบุคลากรทางการแพทย์ที่มีคุณสมบัติ
</div>
