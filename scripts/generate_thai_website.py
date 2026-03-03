#!/usr/bin/env python3
"""Generate Thai website content for ThTxGNN."""

import json
import os
from datetime import datetime
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
DATA_DIR = PROJECT_ROOT / "data"


def load_data():
    """Load ThTxGNN data."""
    dl_predictions = pd.read_csv(DATA_DIR / "processed" / "txgnn_dl_predictions.csv")
    drug_mapping = pd.read_csv(DATA_DIR / "processed" / "drug_mapping.csv")
    indication_mapping = pd.read_csv(DATA_DIR / "processed" / "indication_mapping.csv")
    return dl_predictions, drug_mapping, indication_mapping


def get_evidence_level(score):
    """Determine evidence level based on score."""
    if score >= 0.999:
        return "L4"
    elif score >= 0.99:
        return "L4"
    else:
        return "L5"


def get_decision(evidence_level):
    """Get Thai decision text."""
    decisions = {
        "L1": "ผ่านการตรวจสอบ",
        "L2": "ดำเนินการต่อด้วยความระมัดระวัง",
        "L3": "ดำเนินการต่อด้วยความระมัดระวัง",
        "L4": "รอหลักฐานเพิ่มเติม",
        "L5": "รอหลักฐานเพิ่มเติม"
    }
    return decisions.get(evidence_level, "รอหลักฐานเพิ่มเติม")


def get_parent_nav(evidence_level):
    """Get Thai parent navigation."""
    parents = {
        "L1": "ผ่านการตรวจสอบทางคลินิก (L1)",
        "L2": "หลักฐานแข็งแกร่ง (L2)",
        "L3": "หลักฐานปานกลาง (L3)",
        "L4": "หลักฐานอ่อน (L4)",
        "L5": "การคาดการณ์จากโมเดล (L5)"
    }
    return parents.get(evidence_level, "การคาดการณ์จากโมเดล (L5)")


def generate_drug_page(drug_row, dl_predictions, indication_mapping):
    """Generate a Thai drug page."""
    drug_name = drug_row['brand_name']
    drugbank_id = drug_row['drugbank_id']
    license_id = drug_row['license_id']
    slug = drug_name.lower().replace(" ", "_").replace("-", "_")

    # Get predictions for this drug (top 10)
    drug_preds = dl_predictions[dl_predictions['drugbank_id'] == drugbank_id].nlargest(10, 'txgnn_score')

    # Get original Thai indication
    drug_ind = indication_mapping[indication_mapping['license_id'] == license_id]
    original_indication_thai = "ตามข้อบ่งใช้ที่ขึ้นทะเบียน"
    if len(drug_ind) > 0:
        original_indication_thai = drug_ind.iloc[0].get('original_indication', original_indication_thai)

    # Metrics
    indication_count = len(drug_preds)
    top_score = drug_preds['txgnn_score'].max() if len(drug_preds) > 0 else 0
    evidence_level = get_evidence_level(top_score)
    decision = get_decision(evidence_level)
    parent_nav = get_parent_nav(evidence_level)

    # Top prediction
    top_prediction = "ไม่มีการคาดการณ์"
    if len(drug_preds) > 0:
        top_prediction = drug_preds.iloc[0]['潛在新適應症']

    # Build predictions table
    predictions_table = ""
    if len(drug_preds) > 0:
        predictions_table = "| อันดับ | ข้อบ่งใช้ที่คาดการณ์ | คะแนน TxGNN |\n|:------:|---------------------|:-----------:|\n"
        for i, (_, row) in enumerate(drug_preds.iterrows(), 1):
            predictions_table += f"| {i} | {row['潛在新適應症']} | {row['txgnn_score']:.4f} |\n"

    content = f"""---
layout: default
title: "{drug_name}"
description: "รายงานการวิเคราะห์ศักยภาพการใช้ยา {drug_name} ในข้อบ่งใช้ใหม่ - ThTxGNN"
parent: {parent_nav}
nav_order: 1
drug_name: "{drug_name}"
drugbank_id: "{drugbank_id}"
evidence_level: "{evidence_level}"
indication_count: {indication_count}
---

# {drug_name}

<p class="fs-5 text-grey-dk-100">
ระดับหลักฐาน: <strong>{evidence_level}</strong> | ข้อบ่งใช้ที่คาดการณ์: <strong>{indication_count}</strong> รายการ
</p>

---

## สรุปภาพรวม

| รายการ | รายละเอียด |
|--------|------------|
| **DrugBank ID** | [{drugbank_id}](https://go.drugbank.com/drugs/{drugbank_id}) |
| **เลขทะเบียนยา** | {license_id} |
| **ข้อบ่งใช้เดิม** | {original_indication_thai} |
| **ข้อบ่งใช้ที่คาดการณ์อันดับ 1** | {top_prediction} |
| **คะแนน TxGNN สูงสุด** | {top_score:.4f} |
| **ระดับหลักฐาน** | {evidence_level} |
| **ขึ้นทะเบียนในประเทศไทย** | ✅ จดทะเบียนแล้ว |
| **การตัดสินใจแนะนำ** | {decision} |

## การคาดการณ์ข้อบ่งใช้ใหม่จาก TxGNN

{predictions_table if predictions_table else "ยังไม่มีการคาดการณ์สำหรับยานี้"}

## วิธีการคาดการณ์

การคาดการณ์นี้ใช้โมเดล TxGNN (Therapeutics-Centric Knowledge Graph for Drug Repurposing)
จาก Harvard ซึ่งวิเคราะห์ความสัมพันธ์ระหว่างยาและโรคจาก Knowledge Graph ที่ประกอบด้วย:

- ข้อมูลยาจาก DrugBank
- ข้อมูลโรคจาก Disease Ontology
- ความสัมพันธ์ยา-โรคที่ผ่านการตรวจสอบ

## ข้อควรพิจารณาด้านความปลอดภัย

⚠️ กรุณาอ้างอิงเอกสารกำกับยาฉบับเต็มและปรึกษาแพทย์หรือเภสัชกรก่อนใช้ยา

## สรุปและขั้นตอนถัดไป

**การตัดสินใจ: {decision}**

**เหตุผล:**
การคาดการณ์นี้อยู่ในระดับหลักฐาน {evidence_level} ซึ่งต้องการการวิจัยเพิ่มเติมเพื่อยืนยันประสิทธิภาพ

**สิ่งที่ต้องการเพื่อดำเนินการต่อ:**
- การศึกษากลไกการออกฤทธิ์ของยา (Mechanism of Action)
- การทดลองทางคลินิกเบื้องต้น (Phase I/II Clinical Trial)
- การศึกษาปฏิกิริยาระหว่างยา (Drug Interactions)

---

## แหล่งข้อมูล

- [DrugBank: {drug_name}](https://go.drugbank.com/drugs/{drugbank_id})
- [PubMed: {drug_name}](https://pubmed.ncbi.nlm.nih.gov/?term={drug_name.replace(' ', '+')})
- [ClinicalTrials.gov](https://clinicaltrials.gov/search?term={drug_name.replace(' ', '+')})

---

<div class="disclaimer" style="background-color: #fff3cd; padding: 1rem; border-radius: 0.5rem; margin-top: 2rem;">
<strong>⚠️ ข้อจำกัดความรับผิดชอบ</strong><br>
รายงานนี้มีไว้เพื่อการวิจัยทางวิชาการเท่านั้น <strong>ไม่ถือเป็นคำแนะนำทางการแพทย์</strong>
การใช้ยาต้องปฏิบัติตามคำแนะนำของแพทย์ ห้ามปรับเปลี่ยนการใช้ยาด้วยตนเอง
การตัดสินใจใช้ยาเก่าในข้อบ่งใช้ใหม่ต้องผ่านการตรวจสอบทางคลินิกและกฎระเบียบอย่างครบถ้วน
<br><br>
<small>ตรวจสอบล่าสุด: {datetime.now().strftime('%Y-%m-%d')} | ThTxGNN Research Team</small>
</div>
"""
    return slug, content, {
        "slug": slug,
        "name": drug_name,
        "drugbank_id": drugbank_id,
        "license_id": license_id,
        "evidence_level": evidence_level,
        "indication_count": indication_count,
        "original_indication": original_indication_thai,
        "predicted_indication": top_prediction,
        "txgnn_score": f"{top_score:.4f}" if top_score > 0 else "N/A",
        "thailand_approved": True,
        "decision": decision,
        "url": f"/drugs/{slug}/"
    }


def generate_all_drugs():
    """Generate all drug pages."""
    print("Loading data...")
    dl_predictions, drug_mapping, indication_mapping = load_data()

    drugs_dir = DOCS_DIR / "_drugs"
    drugs_dir.mkdir(exist_ok=True)

    # Get unique mapped drugs
    mapped_drugs = drug_mapping[drug_mapping['mapped'] == True].drop_duplicates(subset=['drugbank_id'])

    drugs_list = []
    print(f"Generating {len(mapped_drugs)} drug pages...")

    for _, drug in mapped_drugs.iterrows():
        slug, content, drug_info = generate_drug_page(drug, dl_predictions, indication_mapping)

        # Write drug page
        with open(drugs_dir / f"{slug}.md", 'w', encoding='utf-8') as f:
            f.write(content)

        drugs_list.append(drug_info)

    print(f"Generated {len(drugs_list)} drug pages")
    return drugs_list


def generate_data_files(drugs_list):
    """Generate data JSON files."""
    print("Generating data files...")
    data_dir = DOCS_DIR / "data"
    data_dir.mkdir(exist_ok=True)

    # drugs.json
    drugs_json = {
        "generated": datetime.now().strftime('%Y-%m-%d'),
        "total_count": len(drugs_list),
        "source": "ThTxGNN - https://thtxgnn.yao.care/",
        "description": "ข้อมูลยาที่ขึ้นทะเบียนในประเทศไทยพร้อมการคาดการณ์ข้อบ่งใช้ใหม่",
        "drugs": drugs_list
    }
    with open(data_dir / "drugs.json", 'w', encoding='utf-8') as f:
        json.dump(drugs_json, f, ensure_ascii=False, indent=2)

    # drugs-by-level.json
    drugs_by_level = {}
    for drug in drugs_list:
        level = drug['evidence_level']
        if level not in drugs_by_level:
            drugs_by_level[level] = []
        drugs_by_level[level].append(drug)

    with open(data_dir / "drugs-by-level.json", 'w', encoding='utf-8') as f:
        json.dump(drugs_by_level, f, ensure_ascii=False, indent=2)

    # search-index.json
    search_index = [
        {
            "title": drug['name'],
            "url": drug['url'],
            "content": f"{drug['name']} {drug['predicted_indication']} {drug['evidence_level']} {drug['original_indication']}"
        }
        for drug in drugs_list
    ]
    with open(data_dir / "search-index.json", 'w', encoding='utf-8') as f:
        json.dump(search_index, f, ensure_ascii=False, indent=2)

    # drugs.csv
    df = pd.DataFrame(drugs_list)
    df.to_csv(data_dir / "drugs.csv", index=False, encoding='utf-8')

    print("Generated data files")


def generate_downloads(drugs_list):
    """Generate download files."""
    print("Generating download files...")
    downloads_dir = DOCS_DIR / "downloads"
    downloads_dir.mkdir(exist_ok=True)

    df = pd.DataFrame(drugs_list)
    df.to_csv(downloads_dir / "thtxgnn_drugs_summary.csv", index=False, encoding='utf-8')

    with open(downloads_dir / "thtxgnn_drugs_summary.json", 'w', encoding='utf-8') as f:
        json.dump(drugs_list, f, ensure_ascii=False, indent=2)

    # High evidence
    high_evidence = [d for d in drugs_list if d['evidence_level'] in ['L1', 'L2', 'L3', 'L4']]
    df_high = pd.DataFrame(high_evidence)
    df_high.to_csv(downloads_dir / "thtxgnn_high_evidence.csv", index=False, encoding='utf-8')

    print("Generated download files")


def generate_nav_pages():
    """Generate Thai navigation pages."""
    print("Generating navigation pages...")

    # index.md
    index_content = """---
layout: default
title: หน้าแรก
nav_order: 1
description: "ThTxGNN - ระบบคาดการณ์การใช้ยาเก่าในข้อบ่งใช้ใหม่สำหรับประเทศไทย"
---

# ThTxGNN: ระบบคาดการณ์การใช้ยาเก่าในข้อบ่งใช้ใหม่

ยินดีต้อนรับสู่ **ThTxGNN** (Thailand TxGNN) ระบบคาดการณ์การใช้ยาเก่าในข้อบ่งใช้ใหม่สำหรับประเทศไทย

## ภาพรวมโครงการ

ThTxGNN ใช้โมเดล **TxGNN** (Therapeutics-Centric Knowledge Graph) จาก Harvard
เพื่อคาดการณ์ข้อบ่งใช้ใหม่สำหรับยาที่ขึ้นทะเบียนกับสำนักงานคณะกรรมการอาหารและยา (อย.) ประเทศไทย

### สถิติระบบ

| รายการ | จำนวน |
|--------|-------|
| ยาที่วิเคราะห์ | 151 รายการ |
| การคาดการณ์ทั้งหมด | 2.5+ ล้านคู่ |
| การคาดการณ์ความเชื่อมั่นสูง (≥0.9) | 11,000+ รายการ |
| แหล่งข้อมูล | Thai FDA, DrugBank, TxGNN |

## การเริ่มต้นใช้งาน

- [📖 คู่มือการใช้งาน]({{ "/guide/" | relative_url }})
- [💊 ค้นหายา]({{ "/nav-drugs/" | relative_url }})
- [📥 ดาวน์โหลดข้อมูล]({{ "/downloads/" | relative_url }})
- [🔗 FHIR API]({{ "/fhir/metadata" | relative_url }})

## ระดับหลักฐาน

| ระดับ | คำอธิบาย | การตัดสินใจ |
|:-----:|----------|-------------|
| L1 | ผ่านการตรวจสอบทางคลินิก | ผ่านการตรวจสอบ |
| L2 | หลักฐานแข็งแกร่ง (Clinical Trial + Literature) | ดำเนินการต่อด้วยความระมัดระวัง |
| L3 | หลักฐานปานกลาง | ดำเนินการต่อด้วยความระมัดระวัง |
| L4 | หลักฐานอ่อน (คะแนนโมเดลสูง) | รอหลักฐานเพิ่มเติม |
| L5 | การคาดการณ์จากโมเดลเท่านั้น | รอหลักฐานเพิ่มเติม |

## แหล่งข้อมูล

- **สำนักงานคณะกรรมการอาหารและยา (Thai FDA)**: ข้อมูลยาที่ขึ้นทะเบียนในประเทศไทย
- **DrugBank**: ฐานข้อมูลยาระดับโลก
- **TxGNN**: โมเดล Knowledge Graph จาก Harvard

---

<div class="disclaimer" style="background-color: #fff3cd; padding: 1rem; border-radius: 0.5rem;">
<strong>⚠️ ข้อจำกัดความรับผิดชอบ</strong><br>
ข้อมูลในเว็บไซต์นี้มีไว้เพื่อการวิจัยทางวิชาการเท่านั้น <strong>ไม่ถือเป็นคำแนะนำทางการแพทย์</strong>
กรุณาปรึกษาแพทย์หรือเภสัชกรก่อนใช้ยา
</div>
"""
    with open(DOCS_DIR / "index.md", 'w', encoding='utf-8') as f:
        f.write(index_content)

    # guide.md
    guide_content = """---
layout: default
title: คู่มือการใช้งาน
nav_order: 2
---

# คู่มือการใช้งาน ThTxGNN

## วิธีอ่านรายงานยา

แต่ละรายงานยาประกอบด้วยส่วนต่างๆ ดังนี้:

### 1. สรุปภาพรวม
- **DrugBank ID**: รหัสยาในฐานข้อมูล DrugBank
- **เลขทะเบียนยา**: เลขทะเบียนจาก Thai FDA
- **ข้อบ่งใช้เดิม**: ข้อบ่งใช้ที่ได้รับอนุมัติในประเทศไทย
- **ข้อบ่งใช้ที่คาดการณ์**: ข้อบ่งใช้ใหม่ที่โมเดลคาดการณ์
- **คะแนน TxGNN**: ความน่าจะเป็นของการคาดการณ์ (0-1)

### 2. ตารางการคาดการณ์
แสดงข้อบ่งใช้ที่คาดการณ์ 10 อันดับแรก พร้อมคะแนนความเชื่อมั่น

### 3. ระดับหลักฐาน

| ระดับ | คำอธิบาย |
|:-----:|----------|
| **L1** | มีหลักฐานทางคลินิกยืนยันแล้ว |
| **L2** | มี Clinical Trial และบทความวิจัยสนับสนุน |
| **L3** | มีบทความวิจัยหรือการศึกษาในระยะเริ่มต้น |
| **L4** | คะแนนโมเดลสูงแต่ยังไม่มีหลักฐานอื่น |
| **L5** | เฉพาะการคาดการณ์จากโมเดล |

## วิธีการค้นหายา

1. ไปที่หน้า [ค้นหายา](/nav-drugs/)
2. เลือกระดับหลักฐานที่ต้องการ
3. คลิกที่ชื่อยาเพื่อดูรายงานฉบับเต็ม

## การดาวน์โหลดข้อมูล

ข้อมูลทั้งหมดสามารถดาวน์โหลดได้ในรูปแบบ:
- **CSV**: สำหรับเปิดใน Excel หรือ Google Sheets
- **JSON**: สำหรับการประมวลผลด้วยโปรแกรม

ไปที่หน้า [ดาวน์โหลด](/downloads/) เพื่อดาวน์โหลดข้อมูล
"""
    with open(DOCS_DIR / "guide.md", 'w', encoding='utf-8') as f:
        f.write(guide_content)

    # nav-drugs.md
    nav_drugs_content = """---
layout: default
title: ค้นหายา
nav_order: 3
---

# ค้นหายา

เรียกดูรายงานยาตามระดับหลักฐาน:

## ตามระดับหลักฐาน

- [หลักฐานอ่อน (L4)](/evidence-l4/) - คะแนนโมเดลสูง
- [การคาดการณ์จากโมเดล (L5)](/evidence-l5/) - เฉพาะการคาดการณ์

## ดาวน์โหลดข้อมูล

- [ดาวน์โหลดทั้งหมด (CSV)](/downloads/thtxgnn_drugs_summary.csv)
- [ดาวน์โหลดทั้งหมด (JSON)](/downloads/thtxgnn_drugs_summary.json)
- [เฉพาะหลักฐานสูง (CSV)](/downloads/thtxgnn_high_evidence.csv)

## FHIR API

- [FHIR CapabilityStatement](/fhir/metadata)
- [MedicationKnowledge](/fhir/MedicationKnowledge/)
- [ClinicalUseDefinition](/fhir/ClinicalUseDefinition/)
"""
    with open(DOCS_DIR / "nav-drugs.md", 'w', encoding='utf-8') as f:
        f.write(nav_drugs_content)

    # downloads.md
    downloads_content = """---
layout: default
title: ดาวน์โหลด
nav_order: 4
---

# ดาวน์โหลดข้อมูล

## ไฟล์ที่พร้อมดาวน์โหลด

| ไฟล์ | รูปแบบ | คำอธิบาย |
|------|:------:|----------|
| [thtxgnn_drugs_summary.csv](/downloads/thtxgnn_drugs_summary.csv) | CSV | สรุปยาทั้งหมด |
| [thtxgnn_drugs_summary.json](/downloads/thtxgnn_drugs_summary.json) | JSON | สรุปยาในรูปแบบ JSON |
| [thtxgnn_high_evidence.csv](/downloads/thtxgnn_high_evidence.csv) | CSV | ยาที่มีหลักฐานระดับสูง |

## FHIR Resources

- [FHIR CapabilityStatement](/fhir/metadata)
- [MedicationKnowledge](/fhir/MedicationKnowledge/)
- [ClinicalUseDefinition](/fhir/ClinicalUseDefinition/)

## API

ดูเอกสาร [FHIR API](/api/) สำหรับการเข้าถึงข้อมูลผ่าน API

## ลิขสิทธิ์และการอนุญาต

ข้อมูลในเว็บไซต์นี้เผยแพร่ภายใต้สัญญาอนุญาต Creative Commons Attribution 4.0 International (CC BY 4.0)
"""
    with open(DOCS_DIR / "downloads.md", 'w', encoding='utf-8') as f:
        f.write(downloads_content)

    # Evidence level pages
    for level, thai_name in [("L4", "หลักฐานอ่อน"), ("L5", "การคาดการณ์จากโมเดล")]:
        evidence_content = f"""---
layout: default
title: {thai_name} ({level})
nav_order: {10 + int(level[1])}
has_children: true
---

# {thai_name} ({level})

รายการยาในระดับหลักฐาน {level}

{{% assign drugs = site.drugs | where: "evidence_level", "{level}" %}}
{{% for drug in drugs %}}
- [{{{{ drug.title }}}}]({{{{ drug.url | relative_url }}}}) - {{{{ drug.drugbank_id }}}}
{{% endfor %}}
"""
        with open(DOCS_DIR / f"evidence-{level.lower()}.md", 'w', encoding='utf-8') as f:
            f.write(evidence_content)

    print("Generated navigation pages")


def update_config():
    """Update _config.yml."""
    print("Updating _config.yml...")
    config_content = """# ThTxGNN Jekyll Configuration

title: "ThTxGNN: ระบบคาดการณ์การใช้ยาเก่าในข้อบ่งใช้ใหม่"
description: "Thailand Drug Repurposing Predictions using TxGNN Knowledge Graph"
url: "https://thtxgnn.yao.care"
baseurl: ""
lang: "th"

remote_theme: just-the-docs/just-the-docs@v0.10.1

plugins:
  - jekyll-remote-theme
  - jekyll-seo-tag
  - jekyll-sitemap

search_enabled: true
search:
  heading_level: 3

footer_content: "Copyright &copy; 2026 ThTxGNN Project | <a href='/privacy-policy/'>นโยบายความเป็นส่วนตัว</a>"

aux_links:
  "GitHub":
    - "https://github.com/yao-care/ThTxGNN"

back_to_top: true
back_to_top_text: "กลับขึ้นด้านบน"

collections:
  drugs:
    output: true
    permalink: /drugs/:name/

defaults:
  - scope:
      path: ""
      type: "drugs"
    values:
      layout: "default"

exclude:
  - Gemfile
  - Gemfile.lock
  - node_modules
  - vendor
  - "*.template"
"""
    with open(DOCS_DIR / "_config.yml", 'w', encoding='utf-8') as f:
        f.write(config_content)
    print("Updated _config.yml")


def main():
    """Main function."""
    print("=" * 60)
    print("ThTxGNN Thai Website Content Generator")
    print("=" * 60)

    drugs_list = generate_all_drugs()
    generate_data_files(drugs_list)
    generate_downloads(drugs_list)
    generate_nav_pages()
    update_config()

    print("=" * 60)
    print(f"✅ Generated {len(drugs_list)} Thai drug pages")
    print("=" * 60)


if __name__ == "__main__":
    main()
