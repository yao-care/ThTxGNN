---
layout: default
title: คู่มือการใช้งาน
parent: SMART on FHIR
nav_order: 1
description: "สอนการใช้งาน ThTxGNN SMART App อ่านข้อมูลยาจากระบบเวชระเบียนอิเล็กทรอนิกส์และค้นหาข้อบ่งใช้ใหม่"
permalink: /smart/guide/
---

# คู่มือการใช้งาน SMART on FHIR

<p class="key-answer" data-question="จะใช้งาน ThTxGNN SMART App ได้อย่างไร?">
ThTxGNN SMART App สามารถอ่านข้อมูลยาของผู้ป่วยจากระบบเวชระเบียนอิเล็กทรอนิกส์ (EHR) และค้นหาข้อบ่งใช้ใหม่โดยอัตโนมัติ คู่มือนี้มีสองวิธีการใช้งาน: <strong>โหมดทดสอบอิสระ</strong> (แนะนำสำหรับผู้เริ่มต้น) และ <strong>SMART Launcher</strong>
</p>

---

## ยินดีต้อนรับสถานพยาบาลสำหรับการทดสอบการเชื่อมต่อ

<p class="key-answer" data-question="จะเชื่อมต่อ ThTxGNN เข้ากับระบบโรงพยาบาลได้อย่างไร?">
หากระบบ EHR ของโรงพยาบาลรองรับ SMART on FHIR ยินดีต้อนรับการทดสอบการเชื่อมต่อ เรามีสองโหมดทดสอบให้ทีม IT สามารถตรวจสอบการเชื่อมต่อได้อย่างรวดเร็ว
</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
  <div style="padding: 1.5rem; background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); border-radius: 12px; border: 2px solid #4caf50;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🎯</div>
    <strong style="font-size: 1.1rem; color: #2e7d32;">วิธีที่ 1: โหมดทดสอบอิสระ</strong>
    <p style="color: #555; margin: 0.5rem 0 1rem;">ไม่ต้องเชื่อมต่อ EHR ป้อนชื่อยาโดยตรงเพื่อทดสอบฟังก์ชัน</p>
    <span style="display: inline-block; padding: 4px 12px; background: #4caf50; color: white; border-radius: 16px; font-size: 0.85rem;">ทดลองใช้เร็ว</span>
  </div>
  <div style="padding: 1.5rem; background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); border-radius: 12px; border: 2px solid #2196f3;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔗</div>
    <strong style="font-size: 1.1rem; color: #1565c0;">วิธีที่ 2: SMART Launcher</strong>
    <p style="color: #555; margin: 0.5rem 0 1rem;">ทดสอบขั้นตอน OAuth และการเชื่อมต่อ EHR แบบครบถ้วน</p>
    <span style="display: inline-block; padding: 4px 12px; background: #2196f3; color: white; border-radius: 16px; font-size: 0.85rem;">ตรวจสอบการเชื่อมต่อ IT</span>
  </div>
</div>

---

## วิธีที่ 1: โหมดทดสอบอิสระ

<p class="key-answer" data-question="จะใช้โหมดทดสอบอิสระได้อย่างไร?">
โหมดทดสอบอิสระช่วยให้คุณไม่ต้องเชื่อมต่อระบบ EHR สามารถป้อนชื่อยาโดยตรงเพื่อทดสอบการแมปยาและการค้นหาข้อบ่งใช้ใหม่ของ ThTxGNN
</p>

### ขั้นตอนที่ 1: เปิดหน้าทดสอบอิสระ

<div style="background: #f8f9fa; border-radius: 8px; padding: 1.5rem; margin: 1rem 0;">
  <p style="margin-bottom: 1rem;">คลิกปุ่มด้านล่างเพื่อเปิดหน้าทดสอบอิสระ:</p>
  <div style="display: flex; flex-wrap: wrap; gap: 12px;">
    <a href="{{ '/smart/standalone.html' | relative_url }}?drugs=Famotidine,Docetaxel,Paclitaxel" target="_blank" style="display: inline-block; padding: 12px 24px; background: linear-gradient(135deg, #28a745 0%, #20c997 100%); color: white; text-decoration: none; border-radius: 8px; font-weight: 500;">🚀 ดูตัวอย่าง L1 โดยตรง ↗</a>
    <a href="{{ '/smart/standalone.html' | relative_url }}" target="_blank" style="display: inline-block; padding: 12px 24px; background: #e0e0e0; color: #333; text-decoration: none; border-radius: 8px; font-weight: 500;">เปิดหน้าว่าง ↗</a>
  </div>
  <p style="margin-top: 1rem; font-size: 0.9rem; color: #666;">💡 คลิก "ดูตัวอย่าง L1 โดยตรง" จะโหลดยา 3 ชนิดระดับหลักฐาน L1 (Famotidine, Docetaxel, Paclitaxel) และแสดงผลค้นหาโดยอัตโนมัติ</p>
</div>

### ขั้นตอนที่ 2: ดูหรือเพิ่มยา

เมื่อใช้ลิงก์ "ดูตัวอย่าง L1 โดยตรง" ระบบจะโหลดยา 3 ชนิดระดับหลักฐาน L1 โดยอัตโนมัติ คุณยังสามารถเพิ่มยาอื่นๆ ได้:

| ประเภทการป้อน | ตัวอย่าง |
|---------------|---------|
| ชื่อสามัญภาษาอังกฤษ | Famotidine, Docetaxel, Paclitaxel |
| รหัส RxCUI | 855332, 1161611 |

<div style="background: #e8f5e9; border-left: 4px solid #4caf50; padding: 1rem; margin: 1rem 0; border-radius: 0 8px 8px 0;">
  <strong>💡 คำแนะนำ:</strong> แนะนำให้ใช้ชื่อสามัญภาษาอังกฤษเพื่อผลการจับคู่ที่ดีที่สุด
</div>

### ขั้นตอนที่ 3: ดูข้อบ่งใช้ใหม่ที่คาดการณ์

หลังคลิกปุ่ม "ค้นหา" ระบบจะ:

<ol class="actionable-steps">
  <li><strong>แมปชื่อยา</strong>: จับคู่ชื่อที่ป้อนกับฐานข้อมูล ThTxGNN</li>
  <li><strong>ค้นหาผลคาดการณ์</strong>: ค้นหาข้อบ่งใช้ใหม่ที่มีศักยภาพสำหรับยานั้น</li>
  <li><strong>แสดงระดับหลักฐาน</strong>: แสดงระดับหลักฐาน L1-L5 สำหรับแต่ละการคาดการณ์</li>
</ol>

---

## วิธีที่ 2: SMART Launcher

<p class="key-answer" data-question="จะใช้ SMART Launcher ได้อย่างไร?">
SMART Launcher เป็นเครื่องมือทดสอบอย่างเป็นทางการที่จำลองขั้นตอนการเปิดใช้งาน SMART App จากระบบ EHR อย่างครบถ้วน รวมถึงการอนุญาต OAuth 2.0
</p>

### ขั้นตอนที่ 1: ไปที่ SMART Launcher

<div style="background: #f8f9fa; border-radius: 8px; padding: 1.5rem; margin: 1rem 0;">
  <p style="margin-bottom: 1rem;">คลิกลิงก์ด้านล่างเพื่อเปิด SMART Launcher ที่ตั้งค่าไว้แล้ว:</p>
  <a href="https://launch.smarthealthit.org/?launch_url=https%3A%2F%2Fthtxgnn.yao.care%2Fsmart%2Flaunch.html&launch=WzAsIiIsIiIsIkFVVE8iLDAsMCwwLCIiLCIiLCIiLCIiLCIiLCIiLCIiLDAsMSwiIl0" target="_blank" style="display: inline-block; padding: 12px 24px; background: #333; color: white; text-decoration: none; border-radius: 8px; font-weight: 500;">🚀 ไปที่ SMART Launcher (ตั้งค่าแล้ว) ↗</a>
  <p style="margin-top: 1rem; font-size: 0.9rem; color: #666;">💡 ลิงก์ตั้งค่า Launch URL โดยอัตโนมัติ เพียงเลือกผู้ป่วยเพื่อเริ่มทดสอบ</p>
</div>

### ขั้นตอนที่ 2: เลือกผู้ป่วยทดสอบ

หลังเปิด Launch URL จะถูกตั้งค่าโดยอัตโนมัติ ขั้นตอนต่อไป:

1. ขยายส่วน **Select Patient(s)**
2. ใช้เงื่อนไขกรองเพื่อค้นหาผู้ป่วยที่มีบันทึกการใช้ยา:
   - **Conditions**: เลือกผู้ป่วยที่มีโรคเรื้อรัง (เช่น Hypertension)
   - **Medications**: ยืนยันว่าผู้ป่วยมีบันทึกการใช้ยา

<div style="background: #fff3e0; border-left: 4px solid #ff9800; padding: 1rem; margin: 1rem 0; border-radius: 0 8px 8px 0;">
  <strong>⚠️ หมายเหตุ:</strong> SMART Launcher ใช้ข้อมูลสังเคราะห์ Synthea (ยาอเมริกัน) ยาบางชนิดอาจไม่สามารถจับคู่กับฐานข้อมูล ThTxGNN (ยาประเทศไทย) ได้ทั้งหมด
</div>

### ขั้นตอนที่ 3: เปิดใช้งานและอนุญาต

1. คลิกปุ่ม **Launch**
2. หน้าจะเปลี่ยนไปที่ ThTxGNN SMART App
3. หากมีหน้าอนุญาต คลิก **Authorize** เพื่ออนุญาตการเข้าถึง
4. ระบบจะอ่านข้อมูลยาผู้ป่วยและแสดงข้อบ่งใช้ใหม่โดยอัตโนมัติ

---

## เปรียบเทียบขั้นตอน

| รายการเปรียบเทียบ | 🎯 โหมดทดสอบอิสระ | 🔗 SMART Launcher |
|------------------|-------------------|-------------------|
| ต้องการการเชื่อมต่อ | ❌ ไม่ต้องการ | ✅ ต้องการ |
| OAuth Authorization | ❌ ไม่ทดสอบ | ✅ ทดสอบครบถ้วน |
| แหล่งที่มาของยา | ป้อนด้วยตนเอง | EHR อ่านอัตโนมัติ |
| อัตราการจับคู่ยา | ✅ สูง (ระบุได้) | ⚠️ ต่ำ (ยาอเมริกัน) |
| เหมาะสำหรับ | ผู้ใช้ทั่วไป | นักพัฒนา / ทีม IT |

---

## คำถามที่พบบ่อย

### ทำไมยาบางชนิดแสดง "ไม่สามารถจับคู่"?

ฐานข้อมูล ThTxGNN เน้น**ยาประเทศไทย** ในขณะที่ SMART Launcher ใช้**ข้อมูลสังเคราะห์ Synthea ของสหรัฐอเมริกา** ชื่อยาบางชนิดแตกต่างกันหรือไม่ได้รับอนุมัติในประเทศไทย จึงไม่สามารถจับคู่ได้

**วิธีแก้ไข**: ใช้โหมดทดสอบอิสระ ป้อนชื่อยาในฐานข้อมูล ThTxGNN โดยตรง

### จะใช้ในระบบ EHR จริงได้อย่างไร?

กรุณาติดต่อผู้ดูแลระบบ EHR ของคุณ และให้ข้อมูลต่อไปนี้สำหรับการตั้งค่า:

| รายการ | ค่า |
|--------|-----|
| Launch URL | `https://thtxgnn.yao.care/smart/launch.html` |
| Redirect URI | `https://thtxgnn.yao.care/smart/app.html` |
| Client ID | `thtxgnn-smart-app` |
| Scopes | `launch patient/MedicationRequest.read openid fhirUser` |

### ข้อมูลผู้ป่วยปลอดภัยหรือไม่?

ใช่ ThTxGNN SMART App:
- **ไม่จัดเก็บ**ข้อมูลผู้ป่วยใดๆ
- การประมวลผลทั้งหมดทำใน**เบราว์เซอร์ฝั่งไคลเอนต์**
- ใช้ **PKCE** เพื่อปกป้องขั้นตอน OAuth
- ขอเฉพาะ**สิทธิ์ขั้นต่ำที่จำเป็น**

---

## เอกสารเทคนิค

ต้องการข้อมูลเทคนิคเพิ่มเติม? กรุณาดู:

<div style="margin: 1rem 0;">
  <a href="{{ '/smart/' | relative_url }}" style="display: inline-block; padding: 10px 20px; background: #f5f5f5; color: #333; text-decoration: none; border-radius: 8px; border: 1px solid #e0e0e0;">📚 เอกสารเทคนิค SMART on FHIR</a>
</div>

---

<div class="disclaimer">
<strong>ข้อจำกัดความรับผิดชอบ</strong><br>
เนื้อหาในเว็บไซต์นี้มีไว้เพื่อการวิจัยเท่านั้น ไม่สามารถทดแทนคำแนะนำทางการแพทย์จากผู้เชี่ยวชาญ ผลการคาดการณ์การใช้ยาเก่าในข้อบ่งใช้ใหม่ทั้งหมดต้องผ่านการทดลองทางคลินิกก่อนนำไปใช้ หากมีปัญหาสุขภาพ กรุณาปรึกษาแพทย์หรือบุคลากรทางการแพทย์ที่มีคุณสมบัติ
</div>
