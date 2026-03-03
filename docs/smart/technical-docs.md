---
layout: default
title: เอกสารเทคนิค
parent: SMART on FHIR
nav_order: 2
description: ข้อกำหนดทางเทคนิคของ ThTxGNN SMART on FHIR รวมถึงการตั้งค่า OAuth, FHIR API endpoints และขั้นตอนการแมปยา
permalink: /smart/technical-docs/
---

# เอกสารเทคนิค SMART on FHIR

หน้านี้ให้ข้อกำหนดทางเทคนิคของ ThTxGNN SMART App สำหรับนักพัฒนาและเจ้าหน้าที่ IT

---

## ข้อกำหนดทางเทคนิค

### การตั้งค่า SMART on FHIR

| รายการ | ค่า |
|------|------|
| เวอร์ชัน FHIR | R4 |
| Client ID | `thtxgnn-smart-app` |
| Launch URI | `/smart/launch.html` |
| Redirect URI | `/smart/app.html` |
| วิธีการยืนยันตัวตน | OAuth 2.0 with PKCE |

### ขอบเขตการอนุญาต (Scopes)

```
launch
patient/MedicationRequest.read
patient/MedicationStatement.read
openid
fhirUser
```

### ขั้นตอนการแมปยา

<div style="display: flex; flex-direction: column; align-items: center; gap: 0; margin: 2rem 0;">
  <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 12px 24px; border-radius: 8px; font-weight: 600; text-align: center;">
    EHR MedicationRequest
  </div>
  <div style="width: 2px; height: 24px; background: #667eea;"></div>
  <div style="width: 0; height: 0; border-left: 8px solid transparent; border-right: 8px solid transparent; border-top: 10px solid #667eea;"></div>

  <div style="background: #f8f9fa; border: 2px solid #e0e0e0; padding: 12px 24px; border-radius: 8px; text-align: center; margin-top: -5px;">
    <strong>1. ดึง RxCUI</strong><br>
    <span style="color: #666; font-size: 0.9rem;">รหัสยา RxNorm</span>
  </div>
  <div style="width: 2px; height: 16px; background: #e0e0e0;"></div>
  <div style="width: 0; height: 0; border-left: 6px solid transparent; border-right: 6px solid transparent; border-top: 8px solid #e0e0e0;"></div>

  <div style="background: #f8f9fa; border: 2px solid #e0e0e0; padding: 12px 24px; border-radius: 8px; text-align: center; margin-top: -5px;">
    <strong>2. RxNorm API</strong><br>
    <span style="color: #666; font-size: 0.9rem;">รับชื่อสารออกฤทธิ์</span>
  </div>
  <div style="width: 2px; height: 16px; background: #e0e0e0;"></div>
  <div style="width: 0; height: 0; border-left: 6px solid transparent; border-right: 6px solid transparent; border-top: 8px solid #e0e0e0;"></div>

  <div style="background: #f8f9fa; border: 2px solid #e0e0e0; padding: 12px 24px; border-radius: 8px; text-align: center; margin-top: -5px;">
    <strong>3. มาตรฐานชื่อยา</strong><br>
    <span style="color: #666; font-size: 0.9rem;">ลบคำต่อท้ายเกลือ, เปรียบเทียบชื่อพ้อง</span>
  </div>
  <div style="width: 2px; height: 16px; background: #e0e0e0;"></div>
  <div style="width: 0; height: 0; border-left: 6px solid transparent; border-right: 6px solid transparent; border-top: 8px solid #e0e0e0;"></div>

  <div style="background: #f8f9fa; border: 2px solid #e0e0e0; padding: 12px 24px; border-radius: 8px; text-align: center; margin-top: -5px;">
    <strong>4. Fuse.js fuzzy matching</strong><br>
    <span style="color: #666; font-size: 0.9rem;">เปรียบเทียบกับฐานข้อมูล ThTxGNN</span>
  </div>
  <div style="width: 2px; height: 24px; background: #28a745;"></div>
  <div style="width: 0; height: 0; border-left: 8px solid transparent; border-right: 8px solid transparent; border-top: 10px solid #28a745;"></div>

  <div style="background: linear-gradient(135deg, #28a745 0%, #20c997 100%); color: white; padding: 12px 24px; border-radius: 8px; font-weight: 600; text-align: center; margin-top: -5px;">
    แสดงผลการคาดการณ์ข้อบ่งใช้ใหม่
  </div>
</div>

---

## FHIR API

ThTxGNN มี Static FHIR API สำหรับระบบอื่นในการสืบค้นข้อมูลการคาดการณ์ยา

### Endpoints

| Endpoint | คำอธิบาย |
|------|------|
| `/fhir/metadata` | CapabilityStatement |
| `/fhir/MedicationKnowledge/{id}.json` | ทรัพยากรยาเดี่ยว |
| `/fhir/Bundle/all-predictions.json` | ผลการคาดการณ์ทั้งหมด |

### ตัวอย่าง

```bash
# รับทรัพยากรความรู้ยา Warfarin
curl https://thtxgnn.yao.care/fhir/MedicationKnowledge/warfarin.json
```

---

## สภาพแวดล้อมทดสอบ

### ทดสอบด้วย SMART Health IT Launcher

1. ไปที่ [SMART Launcher](https://launch.smarthealthit.org/)
2. ตั้งค่า:
   - **Launch Type**: Provider EHR Launch
   - **FHIR Version**: R4
   - **App Launch URL**: `https://thtxgnn.yao.care/smart/launch.html`
3. เลือกผู้ป่วยทดสอบ
4. คลิก Launch เพื่อเริ่มทดสอบ

### ระบบ EHR ที่รองรับ

รองรับระบบ EHR ทั้งหมดที่เป็นไปตามมาตรฐาน SMART on FHIR R4:

- Epic
- Cerner (Oracle Health)
- Allscripts
- ระบบที่เข้ากันได้กับ FHIR R4 อื่นๆ

---

## ความเป็นส่วนตัวและความปลอดภัย

- **ไม่เก็บข้อมูล**: แอปพลิเคชันไม่เก็บข้อมูลผู้ป่วยบนเซิร์ฟเวอร์
- **ประมวลผลฝั่งไคลเอนต์**: การประมวลผลข้อมูลทั้งหมดทำในเบราว์เซอร์
- **การป้องกัน PKCE**: ใช้ OAuth 2.0 PKCE flow เพื่อความปลอดภัยในการยืนยันตัวตน
- **สิทธิ์ขั้นต่ำ**: ขอเฉพาะสิทธิ์อ่านที่จำเป็น

รายละเอียดเพิ่มเติมโปรดดู [นโยบายความเป็นส่วนตัว](/privacy-policy/)

---

## ลิงก์ที่เกี่ยวข้อง

- [เอกสาร SMART on FHIR อย่างเป็นทางการ](http://docs.smarthealthit.org/)
- [ข้อกำหนด HL7 FHIR](https://www.hl7.org/fhir/)
- [เอกสาร RxNorm API](https://lhncbc.nlm.nih.gov/RxNav/APIs/RxNormAPIs.html)
