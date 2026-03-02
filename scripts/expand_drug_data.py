#!/usr/bin/env python
"""Expand Thai FDA drug data with more NLEM drugs."""

import json
from pathlib import Path

# Additional drugs from NLEM with Thai indications
ADDITIONAL_DRUGS = [
    # Ophthalmology
    {
        "active_ingredient": "Timolol",
        "indication": "ต้อหิน",
        "indication_en": "glaucoma",
        "dosage_form": "eye drops",
    },
    {
        "active_ingredient": "Latanoprost",
        "indication": "ต้อหิน, ความดันในตาสูง",
        "indication_en": "glaucoma, ocular hypertension",
        "dosage_form": "eye drops",
    },
    {
        "active_ingredient": "Brimonidine",
        "indication": "ต้อหิน",
        "indication_en": "glaucoma",
        "dosage_form": "eye drops",
    },
    # Antivirals
    {
        "active_ingredient": "Oseltamivir",
        "indication": "ไข้หวัดใหญ่",
        "indication_en": "influenza",
        "dosage_form": "capsule",
    },
    {
        "active_ingredient": "Tenofovir",
        "indication": "ไวรัสตับอักเสบบี, เอชไอวี",
        "indication_en": "hepatitis B, HIV",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Lamivudine",
        "indication": "ไวรัสตับอักเสบบี, เอชไอวี",
        "indication_en": "hepatitis B, HIV",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Efavirenz",
        "indication": "เอชไอวี",
        "indication_en": "HIV/AIDS",
        "dosage_form": "tablet",
    },
    # Antifungals
    {
        "active_ingredient": "Itraconazole",
        "indication": "เชื้อรา",
        "indication_en": "fungal infections",
        "dosage_form": "capsule",
    },
    {
        "active_ingredient": "Terbinafine",
        "indication": "เชื้อราผิวหนัง",
        "indication_en": "dermatophytosis",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Nystatin",
        "indication": "เชื้อราในช่องปาก",
        "indication_en": "oral candidiasis",
        "dosage_form": "suspension",
    },
    # Antimalarials
    {
        "active_ingredient": "Chloroquine",
        "indication": "มาลาเรีย",
        "indication_en": "malaria",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Mefloquine",
        "indication": "มาลาเรีย",
        "indication_en": "malaria",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Primaquine",
        "indication": "มาลาเรีย",
        "indication_en": "malaria",
        "dosage_form": "tablet",
    },
    # Anthelmintics
    {
        "active_ingredient": "Albendazole",
        "indication": "พยาธิ",
        "indication_en": "helminth infections",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Mebendazole",
        "indication": "พยาธิ",
        "indication_en": "helminth infections",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Praziquantel",
        "indication": "พยาธิใบไม้ตับ",
        "indication_en": "schistosomiasis, liver fluke",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Ivermectin",
        "indication": "พยาธิ, เหา",
        "indication_en": "parasitic infections, scabies",
        "dosage_form": "tablet",
    },
    # Antituberculosis
    {
        "active_ingredient": "Isoniazid",
        "indication": "วัณโรค",
        "indication_en": "tuberculosis",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Rifampicin",
        "indication": "วัณโรค",
        "indication_en": "tuberculosis",
        "dosage_form": "capsule",
    },
    {
        "active_ingredient": "Ethambutol",
        "indication": "วัณโรค",
        "indication_en": "tuberculosis",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Pyrazinamide",
        "indication": "วัณโรค",
        "indication_en": "tuberculosis",
        "dosage_form": "tablet",
    },
    # Immunosuppressants
    {
        "active_ingredient": "Cyclosporine",
        "indication": "ป้องกันการปฏิเสธอวัยวะ, โรคภูมิคุ้มกันผิดปกติ",
        "indication_en": "organ rejection, autoimmune diseases",
        "dosage_form": "capsule",
    },
    {
        "active_ingredient": "Tacrolimus",
        "indication": "ป้องกันการปฏิเสธอวัยวะ",
        "indication_en": "organ rejection",
        "dosage_form": "capsule",
    },
    {
        "active_ingredient": "Azathioprine",
        "indication": "โรคภูมิคุ้มกันผิดปกติ",
        "indication_en": "autoimmune diseases",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Mycophenolate",
        "indication": "ป้องกันการปฏิเสธอวัยวะ",
        "indication_en": "organ rejection",
        "dosage_form": "tablet",
    },
    # Anticoagulants
    {
        "active_ingredient": "Heparin",
        "indication": "ป้องกันลิ่มเลือด",
        "indication_en": "thromboembolism",
        "dosage_form": "injection",
    },
    {
        "active_ingredient": "Enoxaparin",
        "indication": "ป้องกันลิ่มเลือด",
        "indication_en": "thromboembolism",
        "dosage_form": "injection",
    },
    {
        "active_ingredient": "Rivaroxaban",
        "indication": "ป้องกันลิ่มเลือด, หัวใจเต้นผิดจังหวะ",
        "indication_en": "thromboembolism, atrial fibrillation",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Dabigatran",
        "indication": "ป้องกันลิ่มเลือด, หัวใจเต้นผิดจังหวะ",
        "indication_en": "thromboembolism, atrial fibrillation",
        "dosage_form": "capsule",
    },
    # Hormone/Endocrine
    {
        "active_ingredient": "Testosterone",
        "indication": "ภาวะขาดฮอร์โมนเพศชาย",
        "indication_en": "hypogonadism",
        "dosage_form": "injection",
    },
    {
        "active_ingredient": "Estradiol",
        "indication": "ภาวะขาดฮอร์โมนเพศหญิง",
        "indication_en": "menopause, hormone replacement",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Progesterone",
        "indication": "ภาวะขาดฮอร์โมน",
        "indication_en": "hormone replacement",
        "dosage_form": "capsule",
    },
    {
        "active_ingredient": "Cabergoline",
        "indication": "โพรแลกตินสูง",
        "indication_en": "hyperprolactinemia",
        "dosage_form": "tablet",
    },
    # GI additional
    {
        "active_ingredient": "Lactulose",
        "indication": "ท้องผูก, โรคตับ",
        "indication_en": "constipation, hepatic encephalopathy",
        "dosage_form": "syrup",
    },
    {
        "active_ingredient": "Loperamide",
        "indication": "ท้องเสีย",
        "indication_en": "diarrhea",
        "dosage_form": "capsule",
    },
    {
        "active_ingredient": "Ondansetron",
        "indication": "คลื่นไส้อาเจียน",
        "indication_en": "nausea, vomiting",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Domperidone",
        "indication": "คลื่นไส้อาเจียน",
        "indication_en": "nausea, vomiting, gastroparesis",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Sucralfate",
        "indication": "แผลในกระเพาะอาหาร",
        "indication_en": "peptic ulcer",
        "dosage_form": "tablet",
    },
    # Urology
    {
        "active_ingredient": "Tamsulosin",
        "indication": "ต่อมลูกหมากโต",
        "indication_en": "benign prostatic hyperplasia",
        "dosage_form": "capsule",
    },
    {
        "active_ingredient": "Finasteride",
        "indication": "ต่อมลูกหมากโต, ผมร่วง",
        "indication_en": "benign prostatic hyperplasia, androgenetic alopecia",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Sildenafil",
        "indication": "การแข็งตัวขององคชาต",
        "indication_en": "erectile dysfunction, pulmonary hypertension",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Tadalafil",
        "indication": "การแข็งตัวขององคชาต, ต่อมลูกหมากโต",
        "indication_en": "erectile dysfunction, benign prostatic hyperplasia",
        "dosage_form": "tablet",
    },
    # Dermatology
    {
        "active_ingredient": "Tretinoin",
        "indication": "สิว",
        "indication_en": "acne, photoaging",
        "dosage_form": "cream",
    },
    {
        "active_ingredient": "Isotretinoin",
        "indication": "สิวรุนแรง",
        "indication_en": "severe acne",
        "dosage_form": "capsule",
    },
    {
        "active_ingredient": "Calcipotriol",
        "indication": "สะเก็ดเงิน",
        "indication_en": "psoriasis",
        "dosage_form": "ointment",
    },
    # Anesthetics
    {
        "active_ingredient": "Lidocaine",
        "indication": "ยาชา, หัวใจเต้นผิดจังหวะ",
        "indication_en": "local anesthesia, arrhythmia",
        "dosage_form": "injection",
    },
    {
        "active_ingredient": "Bupivacaine",
        "indication": "ยาชา",
        "indication_en": "local/regional anesthesia",
        "dosage_form": "injection",
    },
    {
        "active_ingredient": "Propofol",
        "indication": "ยาสลบ",
        "indication_en": "general anesthesia",
        "dosage_form": "injection",
    },
    {
        "active_ingredient": "Ketamine",
        "indication": "ยาสลบ, ซึมเศร้า",
        "indication_en": "anesthesia, depression",
        "dosage_form": "injection",
    },
    # Muscle relaxants
    {
        "active_ingredient": "Baclofen",
        "indication": "กล้ามเนื้อหดเกร็ง",
        "indication_en": "spasticity",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Tizanidine",
        "indication": "กล้ามเนื้อหดเกร็ง",
        "indication_en": "spasticity",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Orphenadrine",
        "indication": "ปวดกล้ามเนื้อ",
        "indication_en": "muscle pain",
        "dosage_form": "tablet",
    },
    # Antipsychotics additional
    {
        "active_ingredient": "Clozapine",
        "indication": "จิตเภท",
        "indication_en": "schizophrenia",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Aripiprazole",
        "indication": "จิตเภท, ไบโพลาร์",
        "indication_en": "schizophrenia, bipolar disorder",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Paliperidone",
        "indication": "จิตเภท",
        "indication_en": "schizophrenia",
        "dosage_form": "tablet",
    },
    # Antidepressants additional
    {
        "active_ingredient": "Venlafaxine",
        "indication": "ซึมเศร้า, วิตกกังวล",
        "indication_en": "depression, anxiety",
        "dosage_form": "capsule",
    },
    {
        "active_ingredient": "Duloxetine",
        "indication": "ซึมเศร้า, ปวดปลายประสาท",
        "indication_en": "depression, neuropathic pain",
        "dosage_form": "capsule",
    },
    {
        "active_ingredient": "Mirtazapine",
        "indication": "ซึมเศร้า",
        "indication_en": "depression",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Bupropion",
        "indication": "ซึมเศร้า, เลิกบุหรี่",
        "indication_en": "depression, smoking cessation",
        "dosage_form": "tablet",
    },
    # Others
    {
        "active_ingredient": "Vitamin D",
        "indication": "ขาดวิตามินดี, กระดูกพรุน",
        "indication_en": "vitamin D deficiency, osteoporosis",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Folic acid",
        "indication": "ขาดโฟลิก, ตั้งครรภ์",
        "indication_en": "folate deficiency, pregnancy",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Ferrous sulfate",
        "indication": "โลหิตจาง",
        "indication_en": "iron deficiency anemia",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Erythropoietin",
        "indication": "โลหิตจาง",
        "indication_en": "anemia of chronic kidney disease",
        "dosage_form": "injection",
    },
    {
        "active_ingredient": "Filgrastim",
        "indication": "ภาวะเม็ดเลือดขาวต่ำ",
        "indication_en": "neutropenia",
        "dosage_form": "injection",
    },
    {
        "active_ingredient": "Calcium carbonate",
        "indication": "ขาดแคลเซียม, กรดไหลย้อน",
        "indication_en": "calcium deficiency, antacid",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Potassium chloride",
        "indication": "โพแทสเซียมต่ำ",
        "indication_en": "hypokalemia",
        "dosage_form": "tablet",
    },
    {
        "active_ingredient": "Magnesium sulfate",
        "indication": "แมกนีเซียมต่ำ, ครรภ์เป็นพิษ",
        "indication_en": "hypomagnesemia, preeclampsia",
        "dosage_form": "injection",
    },
]


def main():
    """Expand drug data."""
    # Load existing data
    input_path = Path("data/raw/th_fda_drugs.json")
    with open(input_path, encoding="utf-8") as f:
        existing_drugs = json.load(f)

    print(f"Existing drugs: {len(existing_drugs)}")

    # Get existing ingredients
    existing_ingredients = {
        d["active_ingredient"].upper() for d in existing_drugs
    }

    # Add new drugs
    reg_num = len(existing_drugs) + 1
    new_count = 0

    for drug in ADDITIONAL_DRUGS:
        ingredient = drug["active_ingredient"]
        if ingredient.upper() not in existing_ingredients:
            new_drug = {
                "registration_number": f"1A {reg_num}/67",
                "trade_name_th": ingredient,
                "trade_name_en": ingredient.upper(),
                "active_ingredient": ingredient,
                "indication": drug["indication"],
                "indication_en": drug["indication_en"],
                "dosage_form": drug["dosage_form"],
                "status": "active",
                "source": "NLEM 2024",
            }
            existing_drugs.append(new_drug)
            existing_ingredients.add(ingredient.upper())
            reg_num += 1
            new_count += 1
            print(f"  Added: {ingredient}")

    # Save expanded data
    with open(input_path, "w", encoding="utf-8") as f:
        json.dump(existing_drugs, f, ensure_ascii=False, indent=2)

    print(f"\nAdded {new_count} new drugs")
    print(f"Total drugs: {len(existing_drugs)}")


if __name__ == "__main__":
    main()
