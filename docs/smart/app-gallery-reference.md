---
layout: default
title: แหล่งอ้างอิง SMART App Gallery
parent: SMART on FHIR
nav_order: 5
---

# แหล่งอ้างอิงแอปพลิเคชัน SMART App Gallery

เอกสารนี้รวบรวมข้อมูลจาก [SMART App Gallery](https://apps.smarthealthit.org/apps?sort=name-asc) รวม 143 แอปพลิเคชัน SMART on FHIR เพื่อใช้เป็นแหล่งอ้างอิงสำหรับการพัฒนา ThTxGNN

**วันที่ดึงข้อมูล**: 2026-02-27

---

## สารบัญ

- [จำแนกตามประเภทฟังก์ชัน](#จำแนกตามประเภทฟังก์ชัน)
- [จำแนกตามเวอร์ชัน FHIR](#จำแนกตามเวอร์ชัน-fhir)
- [รายการแอปพลิเคชันทั้งหมด](#รายการแอปพลิเคชันทั้งหมด)
- [ฟีเจอร์ที่น่าสนใจ](#ฟีเจอร์ที่น่าสนใจ)

---

## จำแนกตามประเภทฟังก์ชัน

### การคำนวณความเสี่ยง (Risk Calculation)

| ชื่อแอปพลิเคชัน | ผู้พัฒนา | ฟังก์ชัน | FHIR |
|---------|--------|------|------|
| ASCVD Risk Calculator | Cerner | คะแนนความเสี่ยงหัวใจ 10 ปี/ตลอดชีวิต | DSTU2 |
| BP Centiles v1/v2 | Boston Children's / Interopion | เปอร์เซ็นไทล์ความดันโลหิตในเด็ก | DSTU2 |
| Cardiac Risk | Boston Children's | คะแนนความเสี่ยง Reynolds (โรคหัวใจ/โรคหลอดเลือดสมอง) | DSTU2 |
| CHF Predictive Analytics | SFO Technologies | การระบุความเสี่ยงภาวะหัวใจล้มเหลวเรื้อรัง | DSTU2 |
| CRC SCORE | Gradiant | การทำนายการตรวจคัดกรองมะเร็งลำไส้ใหญ่ | DSTU2, STU3 |
| Diabetes Predictive Analytics | SFO Technologies | การคำนวณความเสี่ยงเบาหวานชนิดที่ 2 | DSTU2 |
| GrowSmart | U Delaware & Nemours | การทำนายความเสี่ยงโรคอ้วนในเด็ก (1-3 ปี) | R4 |
| HealthConnect: AI Cardiovascular Risk | Mindbowser | การประเมินความเสี่ยงหัวใจและหลอดเลือดด้วย AI | R4 |
| HEART Pathway | Impathiq | เครื่องมือตัดสินใจสำหรับผู้ป่วยเจ็บหน้าอก | DSTU2, STU3 |
| MoleCare | 2AY Ltd | การประเมินความเสี่ยงสุขภาพผิวหนัง | R4 |
| Population Cardiac Risk | Boston Children's | การคำนวณความเสี่ยง ASCVD สำหรับการจัดการประชากร | STU3 |
| SMART - PreciseHBR calculator | โรงพยาบาลจางกุง | การคำนวณความเสี่ยงโรคหัวใจอัตโนมัติ | R4 |
| SRDC QRISK2 | SRDC | อัลกอริทึมความเสี่ยงหัวใจและหลอดเลือด QRISK2 | R4 |
| Stone LogiK | Translational Analytics | การทำนายแผนการรักษานิ่วในทางเดินปัสสาวะ | STU3 |
| YouScript | YouScript Inc. | คำแนะนำความเสี่ยงยาตามจีโนไทป์ | DSTU2 |

### การจัดการยา (Medication)

| ชื่อแอปพลิเคชัน | ผู้พัฒนา | ฟังก์ชัน | FHIR |
|---------|--------|------|------|
| CDS Connect: Pain Management | AHRQ/MITRE | แดชบอร์ดการตัดสินใจการจัดการความเจ็บปวด | DSTU2, R4 |
| Colchicine DDI-CDS App | DDI-CDS.org | การแจ้งเตือนปฏิกิริยาระหว่างยา Colchicine | R4 |
| COSRI | มหาวิทยาลัยวอชิงตัน | การสนับสนุนการตัดสินใจเกี่ยวกับยาเสพติด + ข้อมูล PDMP | R4 |
| DDInteract | DDI-CDS.org | การแจ้งเตือนความเสี่ยงเลือดออก Warfarin+NSAIDs | R4 |
| DoseMeRx | DoseMe | การคำนวณการให้ยาที่แม่นยำ | DSTU2 |
| Duke PillBox | Duke Medicine | การฝึกใช้ยาเพื่อเพิ่มการยึดมั่นต่อการรักษา | DSTU2 |
| Fullscript | Fullscript Inc. | แพลตฟอร์มแผนการรักษาส่วนบุคคล | R4 |
| Handtevy Hospital | Pediatric Emergency Standards | ระบบช่วยชีวิตเด็ก/ผู้ใหญ่อย่างรวดเร็ว | DSTU2 |
| HIE Incontext | CRISP | การรวมข้อมูลยา HIE | STU3 |
| Meducation RS | First Databank | คำแนะนำการใช้ยาหลายภาษาสำหรับผู้ป่วย | DSTU2, STU3 |
| Meducation TimeView | First Databank | การแสดงประวัติการยึดมั่นต่อการใช้ยา | DSTU2 |
| Meds Price Compare | Technosoft | การเปรียบเทียบราคายาตามใบสั่งยา | DSTU2 |
| MedTrue | Geisinger & Merck | การตรวจสอบยาและการยึดมั่น | STU3 |
| MPR Monitor | Boston Children's | การทำนายอัตราการครอบครองยาและการยึดมั่น | DSTU2 |
| RxOrbit InWorkflow | Leap Orbit | การฝังรายการยา PDMP ใน EHR | DSTU2, STU3 |
| RxPrime | AESOP Technology | ML การวิเคราะห์ยาเพื่อระบุข้อผิดพลาดในการใช้ยา | R4 |
| Rx Studio | Rx Studio Inc. | การสนับสนุนการตัดสินใจทางคลินิกการให้ยาที่แม่นยำ | STU3 |
| Tizanidine DDI-CDS App | DDI-CDS.org | ปฏิกิริยาระหว่างยา Tizanidine | R4 |

### การจัดการโรค (Disease Management)

| ชื่อแอปพลิเคชัน | ผู้พัฒนา | ฟังก์ชัน | FHIR |
|---------|--------|------|------|
| Bilirubin Chart | Intermountain | การรักษาภาวะบิลิรูบินสูงในทารกแรกเกิด | DSTU2 |
| Chest Pain Application | Regenstrief | การดึงและแสดงข้อมูลที่เกี่ยวข้องกับอาการเจ็บหน้าอก | DSTU2 |
| ClinDat | Health Report Services | การติดตามและให้คะแนนอาการโรคไขข้อ | DSTU2 |
| Diabetes Monograph | Boston Children's | มุมมองเอกสารเฉพาะโรคเบาหวาน | DSTU2 |
| Lupus Advisor | Aditus | บริการช่วยเหลือ EHR สำหรับการดูแลโรคลูปัส | R4 |
| Premier AKI Staging | Premier Inc. | การปฏิบัติตามแนวทางทางคลินิกสำหรับไตวายเฉียบพลัน | DSTU2 |
| Rimidi | Rimidi | การจัดการโรคหัวใจและเมตาบอลิกอย่างต่อเนื่อง | DSTU2-R4 |
| Sepsis Watch | GA Tech/Emory | โมเดลการทำนายภาวะติดเชื้อในกระแสเลือด | STU3 |

### การประสานงานการดูแล (Care Coordination)

| ชื่อแอปพลิเคชัน | ผู้พัฒนา | ฟังก์ชัน | FHIR |
|---------|--------|------|------|
| 1upHealth | 1upHealth | การรวมข้อมูลผู้ป่วยจากระบบสุขภาพภายนอก | DSTU2, STU3 |
| ACT.md | ACT.md | การขยายเวชระเบียนอิเล็กทรอนิกส์ข้ามชุมชน | DSTU2 |
| AristaMD | AristaMD | การปรึกษาแพทย์ผู้เชี่ยวชาญทางอิเล็กทรอนิกส์ | STU3 |
| Current Health | Current Health | แพลตฟอร์มการดูแลที่บ้านแบบบูรณาการ | R4 |
| DMEscripts | DMEscripts LLC | การสั่งซื้ออุปกรณ์ทางการแพทย์ที่ง่ายขึ้น | STU3, R4 |
| Doximity on FHIR | Doximity | ข้อมูลผู้ให้บริการทางการแพทย์+การสื่อสารที่ปลอดภัย | DSTU2 |
| Fasten Health | Fasten Health | การรวมบันทึกทางการแพทย์ส่วนบุคคลแบบโอเพนซอร์ส | R4 |
| Guava | Guava Health | แอปพลิเคชันจัดการสุขภาพส่วนบุคคล | DSTU2-R4 |
| Hale Health | Hale Health | การปรึกษาผ่านวิดีโอ+ข้อความที่ปลอดภัย | DSTU2 |
| HealthConnect: Patient Referral Manager | Mindbowser | การลดขั้นตอนกระบวนการส่งต่อ | DSTU2-R4 |
| Major Depression Outcomes App | OM1 | การติดตามคะแนน PHQ-9 | DSTU2-R4 |
| MazikCare Timeline | MazikGlobal | มุมมองไทม์ไลน์การรักษาผู้ป่วย | DSTU2 |
| Medocity MD | Medocity | แพลตฟอร์มเชื่อมต่อ ติดตาม และเฝ้าระวังผู้ป่วย | DSTU2, STU3 |
| Physician Sign Out | ET Labs | แอปพลิเคชันส่งมอบงานทางคลินิก | DSTU2, STU3 |
| SigmaMD | Sigmoid Health | การจัดการและรวบรวมข้อมูลสุขภาพ | R4 |
| T System SMART App | CorroHealth | เนื้อหาทางคลินิกสำหรับห้องฉุกเฉิน | DSTU2-R4 |
| Verata Pathway | Verata Health | การอนุมัติล่วงหน้าอัตโนมัติ | DSTU2-R4 |

### การแสดงข้อมูล (Data Visualization)

| ชื่อแอปพลิเคชัน | ผู้พัฒนา | ฟังก์ชัน | FHIR |
|---------|--------|------|------|
| Abstractive Health | Abstractive Health | สรุปทางคลินิกที่สร้างโดย AI | R4 |
| AI-Powered Health Chart | Prairie Byte | ความเข้าใจข้อมูลสุขภาพด้วย AI | R4 |
| Avatachart | KeyOn / Visual Terminology | การแสดงข้อมูลทางคลินิกแบบ 3D | R4 |
| DS Patient Care | Dotsquares | ค่าสังเกตและกราฟของผู้ป่วย | R4 |
| explain my notes | shutdownhook | AI อธิบายเอกสารทางคลินิก | R4 |
| Growth Chart | Boston Children's | การดูข้อมูลการเจริญเติบโตของเด็กแบบโต้ตอบ | DSTU2, STU3 |
| Growth Chart for Infants | Georgia Tech | การเจริญเติบโตของทารก 0-36 เดือน | DSTU2 |
| JindalX | JindalX | การวิเคราะห์การเรียกร้องสิทธิ์ผู้ป่วยด้วย AI | R4 |
| PatientShare | Patient Centric Solutions | การดูและแชร์ข้อมูลทางคลินิก | R4 |
| Pediatric Growth Chart | Boston Children's | การติดตามการเจริญเติบโตเด็ก (iOS) | DSTU2 |
| Records | MedVertical | การดึงและตรวจสอบข้อมูล FHIR | DSTU1-R4 |
| Risk Benefit | Ratio Health | ฐานข้อมูลการสื่อสารขั้นตอนทางการแพทย์ | R4 |
| seeCOLe | seeCOLe LLC | การเข้าถึง EHR แบบเรียลไทม์ด้วย AR | DSTU1-R4 |
| SMART- PopHealth | Boston Children's | ตัวชี้วัดสุขภาพประชากรที่แบ่งปัน | DSTU2 |

### การมีส่วนร่วมของผู้ป่วย (Patient Engagement)

| ชื่อแอปพลิเคชัน | ผู้พัฒนา | ฟังก์ชัน | FHIR |
|---------|--------|------|------|
| Aidbox Forms | Health Samurai | การรวมแบบสอบถามพอร์ทัล EHR/ผู้ป่วย | R4 |
| AppScript on FHIR | IQVIA | ใบสั่งอิเล็กทรอนิกส์สำหรับเครื่องมือการมีส่วนร่วมของผู้ป่วยดิจิทัล | DSTU2, STU3 |
| Atrial Fibrillation Treatment Options | DynaMed Decisions | การแสดงตัวเลือกการรักษาภาวะหัวใจเต้นผิดจังหวะ | DSTU2 |
| CarePassport Portal | CarePassport Corp. | พอร์ทัลผู้ป่วยแบบรวม | DSTU2 |
| Carefluence Patient Portal | Carefluence | การรวมบันทึกทางการแพทย์หลายสถานพยาบาล | DSTU2 |
| CommonHealth | The Commons Project | การรวบรวม จัดการ แบ่งปันข้อมูลสุขภาพ | DSTU2, R4 |
| Health Wizz | Health Wizz | การควบคุมและจัดการข้อมูลสุขภาพ | STU3 |
| Kickcall AI | Kickcall AI | พนักงานต้อนรับ AI อัตโนมัติรับสายผู้ป่วย | R4 |
| Krames On FHIR | Krames | การรวมทรัพยากรการศึกษาผู้ป่วย | DSTU2 |
| Mere | Mere Medical | บันทึกสุขภาพส่วนบุคคลแบบโอเพนซอร์ส | DSTU2 |
| Meta Care AI | Metacare.ai | แอปพลิเคชันสุขภาพสำหรับผู้สูงอายุ/ทหารผ่านศึก | R4 |
| MyFHR | CareEvolution | บันทึกสุขภาพผู้ป่วยเต็มรูปแบบ | DSTU2, STU3 |
| MyLinks | PatientLink | PHR 36,000+ คลินิก | DSTU2-R4 |
| OneRecord | OneRecord | การรวมข้อมูลสุขภาพข้ามอุปกรณ์ | DSTU2-R4 |
| PatientWisdom | PatientWisdom Inc. | การรวมสรุปข้อมูลผู้ป่วย | STU3 |
| Primary Record | Primary Record Inc. | การจัดระเบียบและการทำงานร่วมกันข้อมูลสุขภาพครอบครัว | R4 |
| Visiontree | Visiontree Software | การรวบรวมข้อมูลผู้ป่วย ePRO | DSTU2-R4 |

### การวิจัยทางคลินิก (Clinical Research)

| ชื่อแอปพลิเคชัน | ผู้พัฒนา | ฟังก์ชัน | FHIR |
|---------|--------|------|------|
| AutoMed Query | AutoMed Health | การสืบค้นข้อมูลผู้ป่วยด้วยภาษาธรรมชาติ | R4 |
| Caren mHealth | Caren LLC | การรวบรวมข้อมูลสุขภาพในโลกจริง | DSTU2, R4 |
| Clinical Pipe | Protocol First | ข้อมูลการทดลองทางคลินิก EHR→EDC | DSTU2 |
| Clinical Trials Search | ShutdownHook | ค้นหาการทดลองทางคลินิกที่ตรงกับเงื่อนไข | DSTU2, R4 |
| eDocSS | Across Healthcare | การบันทึกเอกสารหลักฐานการผ่าตัด | R4 |
| HealthCheck AI | HealthCheck Inc | การสนับสนุนการตัดสินใจสรุปทางการแพทย์ด้วย AI | R4 |
| HR-pQCT Data Accession | Georgia Tech | ข้อมูลการวิจัยโรคกระดูกในเด็ก | R4 |
| LHC-Forms SDC Questionnaire | Lister Hill Center | การกำหนดค่าแบบสอบถาม FHIR SDC | R4, STU3 |
| mTuitive OpNote | mTuitive Inc. | การปฏิบัติตามรายงานหลังการผ่าตัด | R4 |
| NLP2FHIR | Mayo Clinic | ท่อข้อมูลทางคลินิกมาตรฐาน | STU3 |
| RTI Wellmine | RTI International | การรวบรวมข้อมูลผู้ป่วยโรคหายาก | R4 |

### จีโนมิกส์ (Genomics)

| ชื่อแอปพลิเคชัน | ผู้พัฒนา | ฟังก์ชัน | FHIR |
|---------|--------|------|------|
| NGS Quality Reporting | Samsung Medical Center | รายงานคุณภาพการจัดลำดับยีนรุ่นถัดไป | R4 |
| Precision Medicine Genes + AI | grinformatics | การจัดระเบียบผลลัพธ์ทางพันธุกรรมใน EHR | DSTU2 |
| SMART Precision Cancer Medicine | Vanderbilt | การวิเคราะห์การกลายพันธุ์ยีนโซมาติกของมะเร็ง | DSTU2 |

### แอปพลิเคชันขับเคลื่อนด้วย AI

| ชื่อแอปพลิเคชัน | ผู้พัฒนา | ฟังก์ชัน | FHIR |
|---------|--------|------|------|
| Abstractive Health | Abstractive Health | การสร้างสรุปทางคลินิกด้วย AI | R4 |
| AI-Powered Health Chart | Prairie Byte | ความเข้าใจข้อมูลสุขภาพด้วย AI | R4 |
| AutoMed Query | AutoMed Health | การสืบค้นข้อมูลผู้ป่วยด้วยภาษาธรรมชาติ | R4 |
| DxPrime | AESOP Technology | ML แนะนำรหัสการวินิจฉัย/ขั้นตอน | R4 |
| explain my notes | shutdownhook | AI อธิบายเอกสารทางคลินิก | R4 |
| HealthCheck AI | HealthCheck Inc | สรุปทางการแพทย์ด้วย AI | R4 |
| HealthConnect series | Mindbowser | AI ทำนายความเสี่ยง/สรุป/วิเคราะห์อาการ | R4 |
| iAnswer Health | iAnswer Health | ข้อมูลเชิงลึกทางการแพทย์ตามหลักฐานด้วย AI | DSTU1-R4 |
| Muen Liver/Lung Detection | Muen Biomedical | การตรวจจับเนื้องอก/ก้อนเนื้อด้วย AI | R4 |
| RxPrime | AESOP Technology | ML ระบุข้อผิดพลาดในการใช้ยา | R4 |
| Tri-Service AI ECG Analyzer | โรงพยาบาลสามกองทัพ | การตีความคลื่นไฟฟ้าหัวใจด้วย AI | R4 |

### เครื่องมือ FHIR

| ชื่อแอปพลิเคชัน | ผู้พัฒนา | ฟังก์ชัน | FHIR |
|---------|--------|------|------|
| Convergent | Leap Orbit | การค้นหา FHIR API ไดเรกทอรีผู้ให้บริการ | R4 |
| EBMcalc FHIR App | EBMcalc LLC | เครื่องคำนวณการแพทย์ตามหลักฐาน | R4 |
| EBM_FHIR | EBM Technologies | การรับข้อมูลผู้ป่วย | R4 |
| LACE Index Scoring | Leapfrog Tech | การป้องกันการกลับเข้ารักษา 30 วัน | STU3 |
| OntoCommand | CSIRO | แดชบอร์ดเซิร์ฟเวอร์คำศัพท์ FHIR | STU3, R4 |
| pCom | Endpoint Technologies | การสื่อสารผู้ให้บริการที่ปฏิบัติตาม HIPAA | R4 |
| PDemo | CareEvolution | การสืบค้นข้อมูลประชากรผู้ป่วย | DSTU2 |
| Shrimp | CSIRO | เบราว์เซอร์คำศัพท์ FHIR | STU3, R4 |
| Smart Forms | CSIRO | ตัวเรนเดอร์แบบฟอร์มทางคลินิก React | R4 |

---

## จำแนกตามเวอร์ชัน FHIR

### รองรับเฉพาะ R4

- Abstractive Health
- AI-Powered Health Chart
- Aidbox Forms
- AutoMed Query
- Avatachart
- Colchicine DDI-CDS App
- COSRI
- Cozeva
- Current Health
- DDInteract
- DxPrime
- EBMcalc FHIR App
- EBM_FHIR
- eDocSS
- explain my notes
- Fasten Health
- Flexpa
- Fullscript
- GrowSmart
- HealthCheck AI
- HR-pQCT Data Accession
- JindalX
- Kickcall AI
- Lupus Advisor
- Meta Care AI
- MoleCare
- Muen Liver/Lung Detection
- mTuitive OpNote
- NGS-QR App
- PatientShare
- pCom
- Primary Record
- Risk Benefit
- RxPrime
- SigmaMD
- Smart Forms
- SMART - PreciseHBR calculator
- SMART on FHIR Appointment Scheduler
- SRDC QRISK2
- Tri-Service AI ECG Analyzer

### รองรับหลายเวอร์ชัน (DSTU2-R4)

- 1upHealth
- Caren mHealth
- Clinical Trials Search
- CommonHealth
- Guava
- HealthConnect series
- iAnswer Health
- MyLinks
- OneRecord
- Records
- Rimidi
- seeCOLe
- T System SMART App
- Verata Pathway
- Visiontree

---

## ฟีเจอร์ที่น่าสนใจ

### ทิศทางฟังก์ชันที่เกี่ยวข้องกับ ThTxGNN

#### 1. การแจ้งเตือนปฏิกิริยาระหว่างยา (DDI-CDS)

DDI-CDS.org พัฒนาแอปพลิเคชันปฏิกิริยาระหว่างยาหลายตัว:
- **Colchicine DDI-CDS App**: Colchicine + สารยับยั้ง CYP3A4
- **DDInteract**: ความเสี่ยงเลือดออก Warfarin + NSAIDs
- **Tizanidine DDI-CDS App**: Tizanidine + สารยับยั้ง CYP1A2

**คุณค่าในการอ้างอิง**: ThTxGNN มีข้อมูล DDI (DDInter + Guide to PHARMACOLOGY) อยู่แล้ว สามารถพิจารณารวมเข้าเป็นฟังก์ชันการแจ้งเตือน CDS ที่คล้ายกัน

#### 2. การแสดงการคำนวณความเสี่ยง

แอปพลิเคชันหลายตัวมีการแสดงคะแนนความเสี่ยง:
- **Cardiac Risk**: การแสดงคะแนนความเสี่ยง Reynolds แบบโต้ตอบ
- **ASCVD Risk Calculator**: ความเสี่ยงหัวใจและหลอดเลือด 10 ปี/ตลอดชีวิต
- **SMART - PreciseHBR calculator**: การคำนวณความเสี่ยงโรคหัวใจพัฒนาโดยโรงพยาบาลจางกุง

**คุณค่าในการอ้างอิง**: ผลการคาดการณ์ข้อบ่งใช้ใหม่สามารถเพิ่มการแสดงความเสี่ยง/ประโยชน์

#### 3. สรุปทางคลินิกด้วย AI

- **Abstractive Health**: การสร้างสรุปทางคลินิกด้วย AI
- **explain my notes**: AI อธิบายเอกสารทางคลินิกที่ซับซ้อน
- **HealthConnect series**: ฟังก์ชันทางคลินิกหลากหลายขับเคลื่อนด้วย AI

**คุณค่าในการอ้างอิง**: สามารถพิจารณาให้ฟังก์ชันอธิบายด้วย AI สำหรับผู้สมัครข้อบ่งใช้ใหม่

#### 4. การรวมบันทึกสุขภาพส่วนบุคคล

- **MyLinks**: รองรับ 36,000+ คลินิก
- **Fasten Health**: PHR แบบโฮสต์เองโอเพนซอร์ส
- **OneRecord**: การรวมข้อมูลสุขภาพข้ามอุปกรณ์

**คุณค่าในการอ้างอิง**: สามารถขยาย SMART App เพื่อรองรับการรวมแหล่งข้อมูลเพิ่มเติม

#### 5. แอปพลิเคชันที่พัฒนาโดยสถาบันไทย

- **SMART - PreciseHBR calculator** (โรงพยาบาลจางกุง)
- **Tri-Service AI ECG Analyzer** (โรงพยาบาลสามกองทัพ)
- **Muen Liver/Lung Detection** (Muen Biomedical)

**คุณค่าในการอ้างอิง**: สามารถอ้างอิงประสบการณ์การพัฒนาและกลยุทธ์การแปลเป็นภาษาท้องถิ่นของสถาบันไทย

---

## แหล่งข้อมูล

- SMART App Gallery: https://apps.smarthealthit.org/apps?sort=name-asc
- วันที่ดึงข้อมูล: 2026-02-27
- จำนวนแอปพลิเคชันทั้งหมด: 143

---

<div class="disclaimer">
<strong>ข้อจำกัดความรับผิดชอบ</strong>: เอกสารนี้รวบรวมข้อมูลสาธารณะเพื่อใช้เป็นแหล่งอ้างอิงภายในเท่านั้น ไม่ถือเป็นการแนะนำหรือรับรองแอปพลิเคชันใดๆ
</div>
