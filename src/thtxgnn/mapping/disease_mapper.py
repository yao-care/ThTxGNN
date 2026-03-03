"""疾病映射模組 - 泰文適應症映射至 TxGNN 疾病本體"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd


# 泰英文疾病/症狀對照表
# Thai → English disease mapping dictionary
DISEASE_DICT = {
    # === 心血管系統 (Cardiovascular) ===
    "ความดันโลหิตสูง": "hypertension",
    "ความดันสูง": "hypertension",
    "ความดันโลหิตต่ำ": "hypotension",
    "ความดันต่ำ": "hypotension",
    "โรคหัวใจ": "heart disease",
    "หัวใจวาย": "heart failure",
    "หัวใจล้มเหลว": "heart failure",
    "กล้ามเนื้อหัวใจตาย": "myocardial infarction",
    "หัวใจขาดเลือด": "myocardial ischemia",
    "เจ็บหน้าอก": "angina",
    "หัวใจเต้นผิดจังหวะ": "arrhythmia",
    "ใจสั่น": "palpitation",
    "หลอดเลือดแข็ง": "atherosclerosis",
    "เส้นเลือดขอด": "varicose veins",
    "ลิ่มเลือด": "thrombosis",
    "โรคหลอดเลือดสมอง": "stroke",
    "อัมพาต": "stroke",
    "อัมพฤกษ์": "stroke",

    # === 呼吸系統 (Respiratory) ===
    "หอบหืด": "asthma",
    "โรคหืด": "asthma",
    "หลอดลมอักเสบ": "bronchitis",
    "ปอดบวม": "pneumonia",
    "ปอดอักเสบ": "pneumonia",
    "วัณโรค": "tuberculosis",
    "ไอ": "cough",
    "ไข้หวัด": "common cold",
    "หวัด": "common cold",
    "ไข้หวัดใหญ่": "influenza",
    "โรคจมูกอักเสบ": "rhinitis",
    "ภูมิแพ้จมูก": "allergic rhinitis",
    "ไซนัสอักเสบ": "sinusitis",
    "หายใจลำบาก": "dyspnea",
    "หายใจไม่ออก": "dyspnea",
    "ถุงลมโป่งพอง": "emphysema",
    "ปอดอุดกั้นเรื้อรัง": "chronic obstructive pulmonary disease",

    # === 消化系統 (Gastrointestinal) ===
    "กระเพาะอักเสบ": "gastritis",
    "โรคกระเพาะ": "gastritis",
    "แผลกระเพาะอาหาร": "gastric ulcer",
    "แผลในกระเพาะ": "gastric ulcer",
    "แผลลำไส้เล็กส่วนต้น": "duodenal ulcer",
    "อาหารไม่ย่อย": "dyspepsia",
    "ท้องอืด": "dyspepsia",
    "ท้องเสีย": "diarrhea",
    "อุจจาระร่วง": "diarrhea",
    "ท้องผูก": "constipation",
    "ลำไส้อักเสบ": "enteritis",
    "ลำไส้ใหญ่อักเสบ": "colitis",
    "บิด": "dysentery",
    "ตับอักเสบ": "hepatitis",
    "ตับแข็ง": "cirrhosis",
    "นิ่วในถุงน้ำดี": "gallstone",
    "ถุงน้ำดีอักเสบ": "cholecystitis",
    "ตับอ่อนอักเสบ": "pancreatitis",
    "คลื่นไส้": "nausea",
    "อาเจียน": "vomiting",
    "กรดไหลย้อน": "gastroesophageal reflux",

    # === 神經系統 (Neurological) ===
    "โรคลมชัก": "epilepsy",
    "ลมบ้าหมู": "epilepsy",
    "ปวดศีรษะ": "headache",
    "ปวดหัว": "headache",
    "ไมเกรน": "migraine",
    "เวียนศีรษะ": "vertigo",
    "มึนหัว": "dizziness",
    "นอนไม่หลับ": "insomnia",
    "ปวดประสาท": "neuralgia",
    "ปวดเส้นประสาท": "neuralgia",
    "โรคพาร์กินสัน": "parkinson disease",
    "โรคอัลไซเมอร์": "alzheimer disease",
    "สมองเสื่อม": "dementia",
    "โรคปลอกประสาทอักเสบ": "multiple sclerosis",
    "เยื่อหุ้มสมองอักเสบ": "meningitis",

    # === 精神疾病 (Psychiatric) ===
    "โรคซึมเศร้า": "depression",
    "ซึมเศร้า": "depression",
    "โรควิตกกังวล": "anxiety disorder",
    "วิตกกังวล": "anxiety",
    "โรคอารมณ์สองขั้ว": "bipolar disorder",
    "โรคจิตเภท": "schizophrenia",
    "โรคตื่นตระหนก": "panic disorder",
    "โรคย้ำคิดย้ำทำ": "obsessive-compulsive disorder",

    # === 內分泌系統 (Endocrine) ===
    "เบาหวาน": "diabetes",
    "โรคเบาหวาน": "diabetes",
    "ไทรอยด์เป็นพิษ": "hyperthyroidism",
    "ต่อมไทรอยด์ทำงานมากเกิน": "hyperthyroidism",
    "ต่อมไทรอยด์ทำงานน้อย": "hypothyroidism",
    "อ้วน": "obesity",
    "โรคอ้วน": "obesity",
    "โรคเกาต์": "gout",
    "เกาต์": "gout",
    "ไขมันในเลือดสูง": "hyperlipidemia",
    "คอเลสเตอรอลสูง": "hypercholesterolemia",

    # === 肌肉骨骼系統 (Musculoskeletal) ===
    "ข้ออักเสบ": "arthritis",
    "โรคข้ออักเสบรูมาตอยด์": "rheumatoid arthritis",
    "กระดูกพรุน": "osteoporosis",
    "กระดูกหัก": "fracture",
    "ปวดกล้ามเนื้อ": "myalgia",
    "ปวดหลัง": "back pain",
    "ปวดเอว": "back pain",
    "ปวดไหล่": "shoulder pain",
    "ปวดคอ": "neck pain",
    "เคล็ดขัดยอก": "sprain",
    "ฟกช้ำ": "contusion",
    "เอ็นอักเสบ": "tendinitis",
    "ข้อเสื่อม": "osteoarthritis",

    # === 皮膚疾病 (Dermatological) ===
    "ผื่นแพ้": "eczema",
    "ลมพิษ": "urticaria",
    "โรคสะเก็ดเงิน": "psoriasis",
    "ผิวหนังอักเสบ": "dermatitis",
    "เชื้อราที่เท้า": "tinea pedis",
    "ฮ่องกงฟุต": "tinea pedis",
    "เชื้อราที่เล็บ": "onychomycosis",
    "สิว": "acne",
    "หิด": "scabies",
    "งูสวัด": "herpes zoster",
    "คัน": "pruritus",
    "ผิวหนังคัน": "pruritus",
    "แผลไฟไหม้": "burn",
    "น้ำร้อนลวก": "burn",

    # === 泌尿系統 (Urological) ===
    "ท่อปัสสาวะอักเสบ": "urethritis",
    "กระเพาะปัสสาวะอักเสบ": "cystitis",
    "ไตอักเสบ": "nephritis",
    "นิ่วในไต": "kidney stone",
    "ต่อมลูกหมากโต": "prostatic hyperplasia",
    "กลั้นปัสสาวะไม่อยู่": "urinary incontinence",
    "ปัสสาวะบ่อย": "urinary frequency",
    "ติดเชื้อทางเดินปัสสาวะ": "urinary tract infection",

    # === 眼科 (Ophthalmological) ===
    "ตาแดง": "conjunctivitis",
    "เยื่อบุตาอักเสบ": "conjunctivitis",
    "ต้อหิน": "glaucoma",
    "ต้อกระจก": "cataract",
    "ตาแห้ง": "dry eye",
    "สายตาสั้น": "myopia",
    "สายตายาว": "hyperopia",

    # === 耳鼻喉 (ENT) ===
    "หูชั้นกลางอักเสบ": "otitis media",
    "หูชั้นนอกอักเสบ": "otitis externa",
    "หูอื้อ": "tinnitus",
    "คออักเสบ": "pharyngitis",
    "เจ็บคอ": "pharyngitis",
    "ต่อมทอนซิลอักเสบ": "tonsillitis",

    # === 感染症 (Infectious) ===
    "ติดเชื้อแบคทีเรีย": "bacterial infection",
    "ติดเชื้อไวรัส": "viral infection",
    "ติดเชื้อรา": "fungal infection",
    "ติดเชื้อปรสิต": "parasitic infection",
    "โลหิตเป็นพิษ": "sepsis",
    "ไข้เลือดออก": "dengue fever",
    "มาลาเรีย": "malaria",
    "ไทฟอยด์": "typhoid fever",

    # === 過敏 (Allergic) ===
    "แพ้": "allergy",
    "ภูมิแพ้": "allergy",
    "แพ้อาหาร": "food allergy",
    "แพ้ยา": "drug allergy",
    "ไข้ละอองฟาง": "hay fever",

    # === 婦科 (Gynecological) ===
    "ประจำเดือนผิดปกติ": "menstrual disorder",
    "ปวดประจำเดือน": "dysmenorrhea",
    "วัยหมดประจำเดือน": "menopause syndrome",
    "วัยทอง": "menopause syndrome",
    "เยื่อบุโพรงมดลูกเจริญผิดที่": "endometriosis",
    "ช่องคลอดอักเสบ": "vaginitis",
    "เนื้องอกมดลูก": "uterine fibroid",

    # === 腫瘤/癌症 (Oncological) ===
    "มะเร็ง": "cancer",
    "เนื้องอก": "tumor",
    "เนื้องอกร้าย": "malignant tumor",
    "เนื้องอกธรรมดา": "benign tumor",
    "มะเร็งเม็ดเลือดขาว": "leukemia",
    "มะเร็งต่อมน้ำเหลือง": "lymphoma",
    "มะเร็งเต้านม": "breast cancer",
    "มะเร็งปอด": "lung cancer",
    "มะเร็งตับ": "liver cancer",
    "มะเร็งลำไส้": "colorectal cancer",

    # === 一般症狀 (General Symptoms) ===
    "ไข้": "fever",
    "มีไข้": "fever",
    "ปวด": "pain",
    "เจ็บ": "pain",
    "อักเสบ": "inflammation",
    "บวม": "edema",
    "บวมน้ำ": "edema",
    "อ่อนเพลีย": "fatigue",
    "เหนื่อยล้า": "fatigue",
    "โลหิตจาง": "anemia",
    "ซีด": "anemia",
    "เลือดออก": "bleeding",
    "ตะคริว": "cramp",
    "ชัก": "seizure",
    "ลดไข้": "fever",
    "แก้ปวด": "pain",
}


def load_disease_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 TxGNN 疾病詞彙表"""
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "disease_vocab.csv"
    return pd.read_csv(filepath)


def build_disease_index(disease_df: pd.DataFrame) -> Dict[str, Tuple[str, str]]:
    """建立疾病名稱索引（關鍵詞 -> (disease_id, disease_name)）"""
    index = {}

    for _, row in disease_df.iterrows():
        disease_id = row["disease_id"]
        disease_name = row["disease_name"]
        name_upper = row["disease_name_upper"]

        # 完整名稱
        index[name_upper] = (disease_id, disease_name)

        # 提取關鍵詞（按空格和逗號分割）
        keywords = re.split(r"[,\s\-]+", name_upper)
        for kw in keywords:
            kw = kw.strip()
            if len(kw) > 3 and kw not in index:  # 只保留較長的關鍵詞
                index[kw] = (disease_id, disease_name)

    return index


def extract_indications(indication_str: str) -> List[str]:
    """從適應症文字提取個別適應症

    使用泰文常見分隔符分割
    """
    if not indication_str:
        return []

    # 正規化
    text = indication_str.strip()

    # 泰文使用空格和逗號作為主要分隔符
    # 也可能使用英文句號或分號
    parts = re.split(r"[。；\n]", text)

    indications = []
    for part in parts:
        # 再用逗號和空格細分
        sub_parts = re.split(r"[,，、]", part)
        for sub in sub_parts:
            sub = sub.strip()
            # 移除常見的非疾病描述前綴（泰文）
            sub = re.sub(r"^(ใช้สำหรับ|ใช้รักษา|รักษา|บรรเทา|ป้องกัน|แก้)", "", sub)
            # 移除常見的後綴
            sub = re.sub(r"(เป็นต้น|และอื่นๆ)$", "", sub)
            sub = sub.strip()
            if sub and len(sub) >= 2:
                indications.append(sub)

    return indications


def translate_indication(indication: str) -> List[str]:
    """將泰文適應症翻譯為英文關鍵詞"""
    keywords = []

    for th, en in DISEASE_DICT.items():
        if th in indication:
            keywords.append(en.upper())

    return keywords


def map_indication_to_disease(
    indication: str,
    disease_index: Dict[str, Tuple[str, str]],
) -> List[Tuple[str, str, float]]:
    """將單一適應症映射到 TxGNN 疾病

    Returns:
        [(disease_id, disease_name, confidence), ...]
    """
    results = []

    # 翻譯為英文關鍵詞
    keywords = translate_indication(indication)

    for kw in keywords:
        # 完全匹配
        if kw in disease_index:
            disease_id, disease_name = disease_index[kw]
            results.append((disease_id, disease_name, 1.0))
            continue

        # 部分匹配
        for index_kw, (disease_id, disease_name) in disease_index.items():
            if kw in index_kw or index_kw in kw:
                results.append((disease_id, disease_name, 0.8))

    # 去重並按信心度排序
    seen = set()
    unique_results = []
    for disease_id, disease_name, conf in sorted(results, key=lambda x: -x[2]):
        if disease_id not in seen:
            seen.add(disease_id)
            unique_results.append((disease_id, disease_name, conf))

    return unique_results[:5]  # 最多返回 5 個匹配


def map_fda_indications_to_diseases(
    fda_df: pd.DataFrame,
    disease_df: Optional[pd.DataFrame] = None,
    indication_field: str = "indication",
    license_field: str = "registration_number",
    brand_field: str = "trade_name_th",
) -> pd.DataFrame:
    """將泰國 FDA 藥品適應症映射到 TxGNN 疾病"""
    if disease_df is None:
        disease_df = load_disease_vocab()

    disease_index = build_disease_index(disease_df)

    results = []

    for _, row in fda_df.iterrows():
        indication_str = row.get(indication_field, "")
        if not indication_str:
            continue

        # 提取個別適應症
        indications = extract_indications(indication_str)

        for ind in indications:
            # 翻譯並映射
            matches = map_indication_to_disease(ind, disease_index)

            if matches:
                for disease_id, disease_name, confidence in matches:
                    results.append({
                        "license_id": row.get(license_field, ""),
                        "brand_name": row.get(brand_field, ""),
                        "original_indication": indication_str[:100],
                        "extracted_indication": ind,
                        "disease_id": disease_id,
                        "disease_name": disease_name,
                        "confidence": confidence,
                    })
            else:
                results.append({
                    "license_id": row.get(license_field, ""),
                    "brand_name": row.get(brand_field, ""),
                    "original_indication": indication_str[:100],
                    "extracted_indication": ind,
                    "disease_id": None,
                    "disease_name": None,
                    "confidence": 0,
                })

    return pd.DataFrame(results)


def get_indication_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """計算適應症映射統計"""
    total = len(mapping_df)
    mapped = mapping_df["disease_id"].notna().sum()
    unique_indications = mapping_df["extracted_indication"].nunique()
    unique_diseases = mapping_df[mapping_df["disease_id"].notna()]["disease_id"].nunique()

    return {
        "total_indications": total,
        "mapped_indications": int(mapped),
        "mapping_rate": mapped / total if total > 0 else 0,
        "unique_indications": unique_indications,
        "unique_diseases": unique_diseases,
    }
