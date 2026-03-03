---
layout: default
title: ข้อมูลความปลอดภัย
nav_order: 5
has_children: true
description: "ฐานข้อมูลปฏิกิริยาระหว่างยา 4 ประเภท: DDI, DDSI, DFI, DHI สำหรับประเมินความเสี่ยงด้านความปลอดภัย"
---

# ข้อมูลความปลอดภัย

<p style="font-size: 1.1rem; color: #666; margin-bottom: 1.5rem;">
รวบรวม <strong>4 ประเภทปฏิกิริยา</strong> เพื่อประเมินความเสี่ยงด้านความปลอดภัยในการใช้ยาเก่าในข้อบ่งใช้ใหม่
</p>

<style>
.safety-dist-container {
  margin: 2rem 0;
}
.safety-dist-bar {
  display: flex;
  height: 32px;
  border-radius: 16px;
  overflow: hidden;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
.safety-dist-bar a {
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 0.75rem;
  text-decoration: none;
  transition: filter 0.2s, transform 0.2s;
}
.safety-dist-bar a:hover {
  filter: brightness(1.1);
  transform: scaleY(1.1);
}
.dist-ddi { background: linear-gradient(135deg, #1565C0, #42A5F5); }
.dist-ddsi { background: linear-gradient(135deg, #7B1FA2, #BA68C8); }
.dist-dfi { background: linear-gradient(135deg, #388E3C, #66BB6A); }
.dist-dhi { background: linear-gradient(135deg, #E65100, #FF9800); }

.safety-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1rem;
}
.safety-card {
  display: flex;
  align-items: center;
  padding: 1.25rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.08);
  text-decoration: none;
  color: inherit;
  transition: transform 0.2s, box-shadow 0.2s;
  border-left: 5px solid;
}
.safety-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.12);
}
.safety-card.ddi { border-color: #1565C0; }
.safety-card.ddsi { border-color: #7B1FA2; }
.safety-card.dfi { border-color: #388E3C; }
.safety-card.dhi { border-color: #E65100; }

.safety-card-icon {
  width: 56px;
  height: 56px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 1rem;
  flex-shrink: 0;
  font-size: 1.5rem;
}
.safety-card.ddi .safety-card-icon { background: #E3F2FD; }
.safety-card.ddsi .safety-card-icon { background: #F3E5F5; }
.safety-card.dfi .safety-card-icon { background: #E8F5E9; }
.safety-card.dhi .safety-card-icon { background: #FFF3E0; }

.safety-card-count {
  font-size: 1.25rem;
  font-weight: 700;
  line-height: 1;
}
.safety-card.ddi .safety-card-count { color: #1565C0; }
.safety-card.ddsi .safety-card-count { color: #7B1FA2; }
.safety-card.dfi .safety-card-count { color: #388E3C; }
.safety-card.dhi .safety-card-count { color: #E65100; }

.safety-card-info {
  flex: 1;
}
.safety-card-title {
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
  color: #333;
}
.safety-card-desc {
  font-size: 0.8rem;
  color: #666;
}
.safety-card-badge {
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.7rem;
  font-weight: 600;
  margin-left: auto;
  white-space: nowrap;
}
.safety-card.ddi .safety-card-badge { background: #E3F2FD; color: #1565C0; }
.safety-card.ddsi .safety-card-badge { background: #F3E5F5; color: #7B1FA2; }
.safety-card.dfi .safety-card-badge { background: #E8F5E9; color: #388E3C; }
.safety-card.dhi .safety-card-badge { background: #FFF3E0; color: #E65100; }
</style>

<div class="safety-dist-container">
  <div class="safety-dist-bar">
    <a href="{{ '/ddi/' | relative_url }}" class="dist-ddi" style="width: 97%;" title="ปฏิกิริยาระหว่างยากับยา: 302,516 รายการ">DDI 30 หมื่น</a>
    <a href="{{ '/ddsi/' | relative_url }}" class="dist-ddsi" style="width: 2.7%;" title="ข้อควรระวังยากับโรค: 8,359 รายการ"></a>
    <a href="{{ '/dfi/' | relative_url }}" class="dist-dfi" style="width: 0.3%;" title="ปฏิกิริยาระหว่างยากับอาหาร: 857 รายการ"></a>
  </div>

  <div class="safety-cards">
    <a href="{{ '/ddi/' | relative_url }}" class="safety-card ddi">
      <div class="safety-card-icon">
        <span class="safety-card-count">30หมื่น</span>
      </div>
      <div class="safety-card-info">
        <div class="safety-card-title">ปฏิกิริยาระหว่างยากับยา</div>
        <div class="safety-card-desc">ความเสี่ยงจากการใช้ยา 2,310 ชนิดร่วมกัน</div>
      </div>
      <span class="safety-card-badge">DDI</span>
    </a>

    <a href="{{ '/ddsi/' | relative_url }}" class="safety-card ddsi">
      <div class="safety-card-icon">
        <span class="safety-card-count">8,359</span>
      </div>
      <div class="safety-card-info">
        <div class="safety-card-title">ข้อควรระวังยากับโรค</div>
        <div class="safety-card-desc">ข้อห้ามใช้ยา 115 ชนิด</div>
      </div>
      <span class="safety-card-badge">DDSI</span>
    </a>

    <a href="{{ '/dfi/' | relative_url }}" class="safety-card dfi">
      <div class="safety-card-icon">
        <span class="safety-card-count">857</span>
      </div>
      <div class="safety-card-info">
        <div class="safety-card-title">ปฏิกิริยาระหว่างยากับอาหาร</div>
        <div class="safety-card-desc">ผลกระทบจากอาหาร 29 ชนิด</div>
      </div>
      <span class="safety-card-badge">DFI</span>
    </a>

    <a href="{{ '/dhi/' | relative_url }}" class="safety-card dhi">
      <div class="safety-card-icon">
        <span class="safety-card-count">35</span>
      </div>
      <div class="safety-card-info">
        <div class="safety-card-title">ปฏิกิริยาระหว่างยากับสมุนไพร</div>
        <div class="safety-card-desc">ความเสี่ยงจากสมุนไพร 10 ชนิด</div>
      </div>
      <span class="safety-card-badge">DHI</span>
    </a>
  </div>
</div>

---

## แหล่งข้อมูล

ข้อมูลปฏิกิริยาทั้งหมดมาจาก [DDInter 2.0](https://ddinter2.scbdd.com/) ซึ่งเป็นฐานข้อมูลปฏิกิริยาระหว่างยาที่ครอบคลุมที่สุดในปัจจุบัน

| ประเภท | แหล่งข้อมูล | จำนวนรายการ | อัพเดทล่าสุด |
|--------|-------------|-------------|--------------|
| DDI | DDInter 2.0 | 302,516 | 2026-02-08 |
| DDSI | DDInter 2.0 | 8,359 | 2026-02-21 |
| DFI | DDInter 2.0 | 857 | 2026-02-21 |
| DHI | ชุดข้อมูลที่คัดเลือก | 35 | 2026-02-21 |
