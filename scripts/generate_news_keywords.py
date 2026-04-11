#!/usr/bin/env python3
"""
สร้างรายการคำสำคัญสำหรับการติดตามข่าวสุขภาพ

ดึงข้อมูลจาก:
- ชื่อยา (อังกฤษ + ชื่อการค้าภาษาไทย)
- ข้อบ่งใช้ที่คาดการณ์ (อังกฤษ)

ผลลัพธ์: data/news/keywords.json
"""

import json
import re
from datetime import datetime
from pathlib import Path

# ไดเรกทอรีหลักของโปรเจค
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DOCS_DATA_DIR = PROJECT_ROOT / "docs" / "data"


def load_json(path: Path) -> dict | list:
    """โหลดไฟล์ JSON"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_thai_terms(text: str) -> list[str]:
    """แยกคำภาษาไทยจากข้อความ (แยกด้วยเครื่องหมายวรรคตอน)"""
    if not text:
        return []
    # ตัวแยก: จุลภาค, อัฒภาค, มหัพภาค, ทับ
    terms = re.split(r"[,;./·•]", text)
    # ลบช่องว่างและกรองสตริงว่าง
    return [t.strip() for t in terms if t.strip() and len(t.strip()) >= 2]


def get_brand_names_from_fda(fda_data: list, drug_name: str) -> list[str]:
    """ค้นหาชื่อการค้าภาษาไทยจากข้อมูล FDA"""
    brand_names = set()
    drug_name_lower = drug_name.lower()

    for item in fda_data:
        # ตรวจสอบตัวยาสำคัญ
        ingredient = item.get("ingredient", "") or item.get("INGREDIENT", "")
        if drug_name_lower in ingredient.lower():
            thai_name = item.get("trade_name_th", "") or item.get("TRADE_NAME_TH", "")
            if thai_name:
                # ดึงเฉพาะชื่อแบรนด์ (ก่อนตัวเลขหรือวงเล็บ)
                match = re.match(r"^([^\s\d๐-๙（(]+)", thai_name)
                if match:
                    brand = match.group(1).strip()
                    if len(brand) >= 2:
                        brand_names.add(brand)

    return list(brand_names)[:5]  # สูงสุด 5 ชื่อ


def load_synonyms(path: Path) -> dict:
    """โหลดตารางคำพ้องความหมายภาษาไทย"""
    if not path.exists():
        return {"indication_synonyms": {}, "drug_synonyms": {}}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


GENERIC_KEYWORD_PATTERNS = {
    "_generic_cancer": [
        "cancer", "carcinoma", "tumor", "tumour", "neoplasm", "malignant",
        "leukemia", "lymphoma", "melanoma", "sarcoma", "myeloma"
    ],
    "_cardiovascular": [
        "cardiovascular", "atherosclerosis", "arteriosclerosis",
        "coronary", "vascular disease"
    ],
    "_heart_disease": [
        "heart disease", "heart failure", "cardiac", "myocardial",
        "arrhythmia", "angina", "cardiomyopathy"
    ],
    "stroke": ["stroke", "ischemic stroke", "cerebrovascular"],
    "herpes zoster": ["herpes", "zoster", "varicella"],
    "dementia": ["dementia", "alzheimer", "cognitive impairment"],
    "pancreatic cancer": ["pancreatic cancer", "pancreatic carcinoma", "pancreatic neoplasm"],
    "menopause": ["menopause", "postmenopaus", "estrogen-receptor", "hormone-resistant"],
}


def build_indication_index(search_index: dict, synonyms: dict) -> dict:
    """สร้างดัชนีข้อบ่งใช้ บันทึกว่าแต่ละข้อบ่งใช้เกี่ยวข้องกับยาตัวใดบ้าง"""
    indication_map = {}
    indication_synonyms = synonyms.get("indication_synonyms", {})

    # เพิ่มรายการคำพ้องก่อน (รวมคำสำคัญทั่วไป เช่น _generic_cancer)
    for en_name, th_list in indication_synonyms.items():
        key = en_name.lower()
        if key not in indication_map:
            indication_map[key] = {
                "name": en_name.lstrip("_"),  # ลบเครื่องหมาย _ นำหน้า
                "keywords_en": [en_name] if not en_name.startswith("_") else [],
                "keywords_th": th_list.copy(),
                "related_drugs": []
            }
            # สร้างดัชนีสำหรับคำพ้องภาษาไทยแต่ละคำด้วย
            for th in th_list:
                th_key = th.lower()
                if th_key not in indication_map:
                    indication_map[th_key] = {
                        "name": th,
                        "keywords_en": [en_name] if not en_name.startswith("_") else [],
                        "keywords_th": [th],
                        "related_drugs": []
                    }

    for drug in search_index.get("drugs", []):
        drug_slug = drug.get("slug", "")

        # ประมวลผลข้อบ่งใช้ที่คาดการณ์
        for ind in drug.get("indications", []):
            ind_name = ind.get("name", "").lower()
            if ind_name:
                if ind_name not in indication_map:
                    # ค้นหาคำพ้อง
                    th_synonyms = indication_synonyms.get(ind.get("name", ""), [])
                    indication_map[ind_name] = {
                        "name": ind.get("name", ""),
                        "keywords_en": [ind.get("name", "")],
                        "keywords_th": th_synonyms.copy(),
                        "related_drugs": []
                    }
                # สร้างดัชนีแยกสำหรับคำพ้องภาษาไทย
                for th in indication_synonyms.get(ind.get("name", ""), []):
                    th_key = th.lower()
                    if th_key not in indication_map:
                        indication_map[th_key] = {
                            "name": th,
                            "keywords_en": [ind.get("name", "")],
                            "keywords_th": [th],
                            "related_drugs": []
                        }
                    if drug_slug not in indication_map[th_key]["related_drugs"]:
                        indication_map[th_key]["related_drugs"].append(drug_slug)

                if drug_slug not in indication_map[ind_name]["related_drugs"]:
                    indication_map[ind_name]["related_drugs"].append(drug_slug)

        # ข้อบ่งใช้ดั้งเดิม (ภาษาไทย)
        original = drug.get("original", "")
        if original:
            th_terms = extract_thai_terms(original)
            for term in th_terms:
                term_key = term.lower()
                if term_key not in indication_map:
                    indication_map[term_key] = {
                        "name": term,
                        "keywords_en": [],
                        "keywords_th": [term],
                        "related_drugs": []
                    }
                else:
                    if term not in indication_map[term_key]["keywords_th"]:
                        indication_map[term_key]["keywords_th"].append(term)

                if drug_slug not in indication_map[term_key]["related_drugs"]:
                    indication_map[term_key]["related_drugs"].append(drug_slug)

    # เชื่อมโยงคำสำคัญทั่วไปกับยาที่มีข้อบ่งใช้ที่เกี่ยวข้อง
    for generic_key, patterns in GENERIC_KEYWORD_PATTERNS.items():
        generic_key_lower = generic_key.lower()
        if generic_key_lower not in indication_map:
            continue

        # ค้นหายาทั้งหมดที่ตรงกับรูปแบบ
        for drug in search_index.get("drugs", []):
            drug_slug = drug.get("slug", "")
            for ind in drug.get("indications", []):
                ind_name = ind.get("name", "").lower()
                # ตรวจสอบว่าตรงกับรูปแบบใดบ้าง
                for pattern in patterns:
                    if pattern.lower() in ind_name:
                        if drug_slug not in indication_map[generic_key_lower]["related_drugs"]:
                            indication_map[generic_key_lower]["related_drugs"].append(drug_slug)
                        break

        # อัปเดตรายการคำพ้องภาษาไทยด้วย
        th_list = indication_synonyms.get(generic_key, [])
        for th in th_list:
            th_key = th.lower()
            if th_key in indication_map:
                for drug_slug in indication_map[generic_key_lower]["related_drugs"]:
                    if drug_slug not in indication_map[th_key]["related_drugs"]:
                        indication_map[th_key]["related_drugs"].append(drug_slug)

    return indication_map


def main():
    print("กำลังโหลดไฟล์ข้อมูล...")

    # โหลดข้อมูล
    search_index_path = DOCS_DATA_DIR / "search-index.json"
    fda_data_path = DATA_DIR / "raw" / "th_fda_drugs.json"
    synonyms_path = DATA_DIR / "news" / "synonyms.json"

    if not search_index_path.exists():
        print(f"ข้อผิดพลาด: ไม่พบ {search_index_path}")
        return

    search_index = load_json(search_index_path)

    fda_data = []
    if fda_data_path.exists():
        fda_data = load_json(fda_data_path)
        print(f"  - th_fda_drugs.json: {len(fda_data)} รายการ FDA")
    else:
        print(f"  - th_fda_drugs.json: ไม่พบไฟล์ (ข้าม)")

    synonyms = load_synonyms(synonyms_path)

    drug_count = len(search_index.get("drugs", []))
    print(f"  - search-index.json: {drug_count} ยา")
    print(f"  - synonyms.json: {len(synonyms.get('indication_synonyms', {}))} คำพ้องข้อบ่งใช้")

    # สร้างรายการคำสำคัญของยา
    drugs_keywords = []

    for drug in search_index.get("drugs", []):
        drug_name = drug.get("name", "")
        drug_slug = drug.get("slug", "")

        # คำสำคัญภาษาอังกฤษ
        keywords_en = [drug_name.lower()]

        # เพิ่มชื่อแบรนด์ (จาก search-index)
        for brand in drug.get("brands", []):
            if brand.lower() not in keywords_en:
                keywords_en.append(brand.lower())

        # ชื่อการค้าภาษาไทย (จากข้อมูล FDA)
        keywords_th = []
        if fda_data:
            keywords_th = get_brand_names_from_fda(fda_data, drug_name)

        drugs_keywords.append({
            "slug": drug_slug,
            "name": drug_name,
            "keywords": {
                "en": keywords_en,
                "th": keywords_th
            },
            "url": f"/drugs/{drug_slug}/"
        })

    print(f"\nประมวลผลคำสำคัญของยา: {len(drugs_keywords)} ยา")

    # สร้างรายการคำสำคัญของข้อบ่งใช้
    indication_map = build_indication_index(search_index, synonyms)

    # แปลงเป็นรายการ (เก็บเฉพาะที่มียาเกี่ยวข้อง)
    indications_keywords = []
    for key, data in indication_map.items():
        if data["related_drugs"]:
            indications_keywords.append({
                "name": data["name"],
                "keywords": {
                    "en": data["keywords_en"],
                    "th": data["keywords_th"]
                },
                "related_drugs": data["related_drugs"]
            })

    print(f"ประมวลผลคำสำคัญของข้อบ่งใช้: {len(indications_keywords)} ข้อบ่งใช้")

    # ผลลัพธ์
    output = {
        "generated": datetime.now().strftime("%Y-%m-%d"),
        "drug_count": len(drugs_keywords),
        "indication_count": len(indications_keywords),
        "drugs": drugs_keywords,
        "indications": indications_keywords
    }

    output_path = DATA_DIR / "news" / "keywords.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nผลลัพธ์: {output_path}")
    print(f"  - คำสำคัญของยา: {len(drugs_keywords)} รายการ")
    print(f"  - คำสำคัญของข้อบ่งใช้: {len(indications_keywords)} รายการ")


if __name__ == "__main__":
    main()
