---
layout: default
title: รายงานการตรวจสอบการใช้ยาเก่าในข้อบ่งใช้ใหม่
nav_order: 1
description: "ใช้ AI คาดการณ์ข้อบ่งใช้ใหม่สำหรับยาที่ขึ้นทะเบียนในประเทศไทย พร้อมรายงานการตรวจสอบหลักฐานทางคลินิก"
permalink: /
image: /assets/images/og-default.png
---

# การใช้ยาเก่าในข้อบ่งใช้ใหม่: จากข้อมูลสู่หลักฐาน

<p class="key-answer" data-question="ThTxGNN คืออะไร?">
<strong>ThTxGNN</strong> คือแพลตฟอร์มคาดการณ์การใช้ยาเก่าในข้อบ่งใช้ใหม่ โดยใช้โมเดล TxGNN จาก Harvard เราได้คาดการณ์ <strong>2,573,191</strong> คู่ยา-โรค และตรวจสอบหลักฐานสำหรับ <strong>151</strong> ยาที่ขึ้นทะเบียนกับ อย. ประเทศไทย
</p>

<div class="key-takeaway">
ไม่ใช่แค่บอกว่า "อาจมีประสิทธิผล" แต่ยังบอกว่า "หลักฐานอยู่ที่ไหน" ระบบจัดระดับหลักฐาน L1-L5 ช่วยให้นักวิจัยประเมินความน่าเชื่อถือของการคาดการณ์ได้อย่างรวดเร็ว
</div>

<p style="margin-top: 1.5rem;">
  <a href="{{ '/nav-drugs' | relative_url }}" style="display: inline-block; padding: 0.75rem 1.5rem; background: #2E7D32; color: white; text-decoration: none; border-radius: 4px; font-weight: 600; margin-right: 0.5rem;">ดูรายงานยา</a>
  <a href="{{ '/methodology' | relative_url }}" style="display: inline-block; padding: 0.75rem 1.5rem; background: #f5f5f5; color: #333; text-decoration: none; border-radius: 4px; font-weight: 500;">เรียนรู้วิธีการ</a>
</p>

---

## ค้นหายา

<p class="key-answer" data-question="จะค้นหายาหรือโรคได้อย่างไร?">
พิมพ์ <strong>ชื่อยา</strong> หรือ <strong>ชื่อโรค</strong> เพื่อค้นหาความเป็นไปได้ในการใช้ยาเก่าในข้อบ่งใช้ใหม่และหลักฐานทางคลินิก รองรับชื่อภาษาอังกฤษและภาษาไทย
</p>

<div class="drug-lookup-container">
  <div class="lookup-search-box">
    <div class="lookup-input-wrapper">
      <input type="text" id="lookup-input" placeholder="พิมพ์ชื่อยาหรือชื่อโรค..." autocomplete="off">
      <button id="lookup-clear" class="lookup-clear-btn" style="display: none;">✕</button>
    </div>
    <button id="lookup-search" class="lookup-search-btn">ค้นหา</button>
  </div>
  <div class="lookup-filters">
    <span class="filter-label">ระดับหลักฐาน:</span>
    <label><input type="checkbox" class="level-filter" value="L1" checked> L1</label>
    <label><input type="checkbox" class="level-filter" value="L2" checked> L2</label>
    <label><input type="checkbox" class="level-filter" value="L3" checked> L3</label>
    <label><input type="checkbox" class="level-filter" value="L4"> L4</label>
    <label><input type="checkbox" class="level-filter" value="L5"> L5</label>
  </div>
  <div id="lookup-results" class="lookup-results"></div>
</div>

<script src="https://cdn.jsdelivr.net/npm/fuse.js@7.0.0"></script>
<script>
  window.THTXGNN_CONFIG = {
    searchIndexUrl: '{{ "/data/search-index.json" | relative_url }}',
    drugsBaseUrl: '{{ "/drugs/" | relative_url }}'
  };
</script>
<script src="{{ '/assets/js/drug-lookup.js' | relative_url }}"></script>

---

## ความแตกต่างของเรา

<p class="key-answer" data-question="ThTxGNN แตกต่างจากเครื่องมือคาดการณ์อื่นอย่างไร?">
เครื่องมือคาดการณ์ส่วนใหญ่ให้เพียงคะแนน "อาจมีประสิทธิผล" นักวิจัยต้องค้นหาหลักฐานทางคลินิกเอง ThTxGNN แตกต่าง: เรารวบรวมข้อมูลจาก ClinicalTrials.gov, PubMed, ปฏิกิริยาระหว่างยา และอื่นๆ พร้อมจัดระดับหลักฐาน L1-L5 ให้คุณเห็นได้ทันทีว่าการคาดการณ์ใดควรตรวจสอบก่อน
</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;">
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #2E7D32;">
    <strong style="font-size: 1.1rem;">จากการคาดการณ์สู่หลักฐาน ครบในที่เดียว</strong><br>
    <span style="color: #666;">แต่ละรายงานรวมหมายเลขการทดลองทางคลินิก (NCT), ดัชนีบทความ (PMID), ข้อมูลการขึ้นทะเบียน อย. ประเทศไทย</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #1976D2;">
    <strong style="font-size: 1.1rem;">ระบบจัดระดับหลักฐาน 5 ระดับ</strong><br>
    <span style="color: #666;">จาก L1 (Phase 3 RCT หลายการศึกษา) ถึง L5 (การคาดการณ์จากโมเดลเท่านั้น) ช่วยให้ทีมวิจัยคัดกรองตัวเลือกที่มีคุณค่าได้รวดเร็ว</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #FB8C00;">
    <strong style="font-size: 1.1rem;">ครอบคลุมยาในประเทศไทย</strong><br>
    <span style="color: #666;">มุ่งเน้นยาที่ได้รับอนุมัติจาก อย. ครอบคลุม 151 ยา รายงานรวมสถานะการขึ้นทะเบียนในประเทศไทย</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #9B59B6;">
    <strong style="font-size: 1.1rem;">ข้อมูลปฏิกิริยาระหว่างยา</strong><br>
    <span style="color: #666;">รวม DDI (ยา-ยา), DDSI (ยา-โรค), DFI (ยา-อาหาร), DHI (ยา-สมุนไพร) ประเมินความปลอดภัยครบถ้วน</span>
  </div>
</div>

---

## สถิติโครงการ

| รายการ | จำนวน |
|--------|-------|
| **ยาที่วิเคราะห์** | 151 รายการ |
| **การคาดการณ์ทั้งหมด** | 2,573,191 คู่ |
| **การคาดการณ์ความเชื่อมั่นสูง (≥0.9)** | 11,033 รายการ |
| **FHIR Resources** | 1,255 รายการ |

---

## ระดับหลักฐาน

| ระดับ | คำอธิบาย | การตัดสินใจ |
|:-----:|----------|-------------|
| **L1** | Phase 3 RCT หลายการศึกษาหรือ Systematic Review | ผ่านการตรวจสอบ |
| **L2** | RCT เดี่ยวหรือ Phase 2 หลายการศึกษา | ดำเนินการต่อด้วยความระมัดระวัง |
| **L3** | การศึกษาเชิงสังเกต | ดำเนินการต่อด้วยความระมัดระวัง |
| **L4** | การศึกษา Preclinical หรือกลไก | รอหลักฐานเพิ่มเติม |
| **L5** | การคาดการณ์จากโมเดลเท่านั้น | รอหลักฐานเพิ่มเติม |

---

## แหล่งข้อมูล

- **Thai FDA (อย.)**: ข้อมูลยาที่ขึ้นทะเบียนในประเทศไทย
- **TxGNN**: Knowledge Graph สำหรับความสัมพันธ์ยา-โรค จาก Harvard
- **DrugBank**: ฐานข้อมูลยาระดับโลก
- **ClinicalTrials.gov**: หลักฐานการทดลองทางคลินิก
- **PubMed**: หลักฐานจากวรรณกรรม
- **TCTR**: Thai Clinical Trials Registry

---

<div class="disclaimer" style="background-color: #fff3cd; padding: 1rem; border-radius: 0.5rem; margin-top: 2rem;">
<strong>⚠️ ข้อจำกัดความรับผิดชอบ</strong><br>
รายงานนี้มีไว้เพื่อการวิจัยทางวิชาการเท่านั้น <strong>ไม่ถือเป็นคำแนะนำทางการแพทย์</strong>
การใช้ยาต้องปฏิบัติตามคำแนะนำของแพทย์ การตัดสินใจใช้ยาเก่าในข้อบ่งใช้ใหม่ต้องผ่านการตรวจสอบทางคลินิกและกฎระเบียบอย่างครบถ้วน
</div>
