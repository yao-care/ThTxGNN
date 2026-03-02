#!/usr/bin/env python3
"""處理泰國 FDA 藥品資料

將下載的藥品資料檔案轉換為標準 JSON 格式。

使用方法:
    uv run python scripts/process_fda_data.py

前置條件:
    需要先下載 Thai FDA 資料檔案到 data/raw/ 目錄
    - 搜尋系統: https://pertento.fda.moph.go.th/FDA_SEARCH_DRUG/SEARCH_DRUG/FRM_SEARCH_DRUG.aspx
    - Web Service: https://catalog.fda.moph.go.th/dataset/web-service-drug-reg

產生檔案:
    data/raw/th_fda_drugs.json
"""

import json
import zipfile
from pathlib import Path
from typing import Any


def find_data_file(raw_dir: Path) -> Path | None:
    """在 raw 目錄中尋找資料檔案

    Args:
        raw_dir: data/raw/ 目錄路徑

    Returns:
        找到的資料檔案路徑，或 None 如果找不到
    """
    # 首先檢查是否有已生成的 Thai FDA 資料
    th_fda_file = raw_dir / "th_fda_drugs.json"
    if th_fda_file.exists():
        return th_fda_file

    # 依優先順序尋找不同格式
    for pattern in ["*.json", "*.zip", "*.csv", "*.xlsx"]:
        data_files = list(raw_dir.glob(pattern))
        # 排除 NLEM PDF 和其他非藥品資料
        data_files = [f for f in data_files if not f.name.endswith(".pdf")]
        if data_files:
            return data_files[0]

    return None


def process_json_file(input_path: Path) -> list[dict]:
    """處理 JSON 檔案"""
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, list):
        return data
    elif isinstance(data, dict):
        # 嘗試找出包含藥品列表的欄位
        for key in ["data", "records", "results", "items", "drugs"]:
            if key in data and isinstance(data[key], list):
                return data[key]
        return [data]

    return []


def process_zip_file(input_path: Path) -> list[dict]:
    """處理 ZIP 檔案"""
    print("解壓縮中...")
    with zipfile.ZipFile(input_path, 'r') as zf:
        json_files = [f for f in zf.namelist() if f.endswith('.json')]
        if not json_files:
            raise ValueError("ZIP 檔案中找不到 JSON 檔案")

        json_filename = json_files[0]
        print(f"找到資料檔案: {json_filename}")

        with zf.open(json_filename) as f:
            file_content = f.read().decode('utf-8')
            return json.loads(file_content)


def process_csv_file(input_path: Path) -> list[dict]:
    """處理 CSV 檔案"""
    import pandas as pd
    df = pd.read_csv(input_path)
    return df.to_dict(orient="records")


def process_xlsx_file(input_path: Path) -> list[dict]:
    """處理 Excel 檔案"""
    import pandas as pd
    df = pd.read_excel(input_path)
    return df.to_dict(orient="records")


def normalize_field_names(data: list[dict]) -> list[dict]:
    """將欄位名稱正規化為英文

    將泰文欄位名稱映射到英文標準欄位名稱
    """
    # 泰文欄位名稱到英文的映射
    field_mapping = {
        # 泰文欄位名稱
        "เลขทะเบียน": "registration_number",
        "ทะเบียนยา": "registration_number",
        "ชื่อการค้า": "trade_name_th",
        "ชื่อการค้าภาษาไทย": "trade_name_th",
        "ชื่อการค้าภาษาอังกฤษ": "trade_name_en",
        "ชื่อสามัญ": "generic_name",
        "ชื่อสามัญทางยา": "generic_name",
        "ตัวยาสำคัญ": "active_ingredient",
        "สารสำคัญ": "active_ingredient",
        "ข้อบ่งใช้": "indication",
        "สรรพคุณ": "indication",
        "รูปแบบยา": "dosage_form",
        "ลักษณะยา": "dosage_form",
        "ความแรง": "strength",
        "ผู้ผลิต": "manufacturer",
        "บริษัทผู้ผลิต": "manufacturer",
        "ผู้รับอนุญาต": "mah",
        "วันที่อนุมัติ": "approval_date",
        "วันที่ขึ้นทะเบียน": "approval_date",
        "วันหมดอายุ": "expiry_date",
        "สถานะ": "status",
        "ประเภทยา": "category",

        # 常見英文欄位名稱（保持不變但統一格式）
        "Registration Number": "registration_number",
        "Trade Name": "trade_name_en",
        "Generic Name": "generic_name",
        "Active Ingredient": "active_ingredient",
        "Indication": "indication",
        "Dosage Form": "dosage_form",
        "Strength": "strength",
        "Manufacturer": "manufacturer",
        "Status": "status",
        "Category": "category",
    }

    normalized_data = []
    for record in data:
        normalized_record = {}
        for key, value in record.items():
            # 尋找映射的欄位名稱
            new_key = field_mapping.get(key, key.lower().replace(" ", "_"))
            normalized_record[new_key] = value
        normalized_data.append(normalized_record)

    return normalized_data


def create_sample_data() -> list[dict]:
    """建立範例資料結構（用於測試）

    當無法取得實際資料時，建立範例資料以測試流程
    """
    print("警告：找不到 Thai FDA 資料檔案")
    print("建立範例資料以供測試...")
    print()
    print("要取得實際資料，請：")
    print("1. 訪問 Thai FDA 搜尋系統:")
    print("   https://pertento.fda.moph.go.th/FDA_SEARCH_DRUG/SEARCH_DRUG/FRM_SEARCH_DRUG.aspx")
    print("2. 或使用 Web Service API:")
    print("   https://catalog.fda.moph.go.th/dataset/web-service-drug-reg")
    print()

    # 範例藥品資料（使用常見泰國藥品）
    sample_drugs = [
        {
            "registration_number": "1A 1/50",
            "trade_name_th": "พาราเซตามอล",
            "trade_name_en": "PARACETAMOL",
            "generic_name": "Paracetamol",
            "active_ingredient": "Paracetamol 500 mg",
            "indication": "บรรเทาอาการปวดศีรษะ ปวดกล้ามเนื้อ ลดไข้",
            "dosage_form": "เม็ด",
            "strength": "500 mg",
            "manufacturer": "องค์การเภสัชกรรม",
            "status": "ใช้งาน",
            "category": "ยาสามัญประจำบ้าน"
        },
        {
            "registration_number": "1A 2/50",
            "trade_name_th": "ไอบูโพรเฟน",
            "trade_name_en": "IBUPROFEN",
            "generic_name": "Ibuprofen",
            "active_ingredient": "Ibuprofen 400 mg",
            "indication": "บรรเทาอาการปวด อักเสบ ลดไข้",
            "dosage_form": "เม็ด",
            "strength": "400 mg",
            "manufacturer": "องค์การเภสัชกรรม",
            "status": "ใช้งาน",
            "category": "ยาอันตราย"
        },
        {
            "registration_number": "1A 3/50",
            "trade_name_th": "อะม็อกซีซิลลิน",
            "trade_name_en": "AMOXICILLIN",
            "generic_name": "Amoxicillin",
            "active_ingredient": "Amoxicillin trihydrate 500 mg",
            "indication": "รักษาโรคติดเชื้อแบคทีเรีย",
            "dosage_form": "แคปซูล",
            "strength": "500 mg",
            "manufacturer": "องค์การเภสัชกรรม",
            "status": "ใช้งาน",
            "category": "ยาอันตราย"
        },
        {
            "registration_number": "1A 4/50",
            "trade_name_th": "เมทฟอร์มิน",
            "trade_name_en": "METFORMIN",
            "generic_name": "Metformin",
            "active_ingredient": "Metformin hydrochloride 500 mg",
            "indication": "รักษาโรคเบาหวานชนิดที่ 2",
            "dosage_form": "เม็ด",
            "strength": "500 mg",
            "manufacturer": "องค์การเภสัชกรรม",
            "status": "ใช้งาน",
            "category": "ยาอันตราย"
        },
        {
            "registration_number": "1A 5/50",
            "trade_name_th": "แอมโลดิพีน",
            "trade_name_en": "AMLODIPINE",
            "generic_name": "Amlodipine",
            "active_ingredient": "Amlodipine besylate 5 mg",
            "indication": "รักษาโรคความดันโลหิตสูง",
            "dosage_form": "เม็ด",
            "strength": "5 mg",
            "manufacturer": "องค์การเภสัชกรรม",
            "status": "ใช้งาน",
            "category": "ยาอันตราย"
        },
        {
            "registration_number": "1A 6/50",
            "trade_name_th": "ซิมวาสแตติน",
            "trade_name_en": "SIMVASTATIN",
            "generic_name": "Simvastatin",
            "active_ingredient": "Simvastatin 20 mg",
            "indication": "ลดระดับคอเลสเตอรอลในเลือด",
            "dosage_form": "เม็ด",
            "strength": "20 mg",
            "manufacturer": "องค์การเภสัชกรรม",
            "status": "ใช้งาน",
            "category": "ยาอันตราย"
        },
        {
            "registration_number": "1A 7/50",
            "trade_name_th": "โอเมพราโซล",
            "trade_name_en": "OMEPRAZOLE",
            "generic_name": "Omeprazole",
            "active_ingredient": "Omeprazole 20 mg",
            "indication": "รักษาโรคกรดไหลย้อน แผลในกระเพาะอาหาร",
            "dosage_form": "แคปซูล",
            "strength": "20 mg",
            "manufacturer": "องค์การเภสัชกรรม",
            "status": "ใช้งาน",
            "category": "ยาอันตราย"
        },
        {
            "registration_number": "1A 8/50",
            "trade_name_th": "ลอราทาดีน",
            "trade_name_en": "LORATADINE",
            "generic_name": "Loratadine",
            "active_ingredient": "Loratadine 10 mg",
            "indication": "บรรเทาอาการภูมิแพ้ ลมพิษ",
            "dosage_form": "เม็ด",
            "strength": "10 mg",
            "manufacturer": "องค์การเภสัชกรรม",
            "status": "ใช้งาน",
            "category": "ยาสามัญประจำบ้าน"
        },
        {
            "registration_number": "1A 9/50",
            "trade_name_th": "ดิโคลฟีแนค",
            "trade_name_en": "DICLOFENAC",
            "generic_name": "Diclofenac",
            "active_ingredient": "Diclofenac sodium 50 mg",
            "indication": "บรรเทาอาการปวด อักเสบ ข้อเสื่อม",
            "dosage_form": "เม็ด",
            "strength": "50 mg",
            "manufacturer": "องค์การเภสัชกรรม",
            "status": "ใช้งาน",
            "category": "ยาอันตราย"
        },
        {
            "registration_number": "1A 10/50",
            "trade_name_th": "แอสไพริน",
            "trade_name_en": "ASPIRIN",
            "generic_name": "Aspirin",
            "active_ingredient": "Acetylsalicylic acid 81 mg",
            "indication": "ป้องกันการเกิดลิ่มเลือด โรคหัวใจ",
            "dosage_form": "เม็ด",
            "strength": "81 mg",
            "manufacturer": "องค์การเภสัชกรรม",
            "status": "ใช้งาน",
            "category": "ยาอันตราย"
        },
    ]

    return sample_drugs


def process_data_file(input_path: Path | None, output_path: Path) -> Path:
    """處理資料檔案並轉換為 JSON

    Args:
        input_path: 輸入檔案路徑，若為 None 則建立範例資料
        output_path: 輸出 JSON 檔案路徑

    Returns:
        輸出檔案路徑
    """
    if input_path is None:
        data = create_sample_data()
    else:
        print(f"讀取資料檔案: {input_path}")
        print(f"檔案大小: {input_path.stat().st_size / 1024 / 1024:.1f} MB")

        suffix = input_path.suffix.lower()
        if suffix == ".json":
            data = process_json_file(input_path)
        elif suffix == ".zip":
            data = process_zip_file(input_path)
        elif suffix == ".csv":
            data = process_csv_file(input_path)
        elif suffix in [".xlsx", ".xls"]:
            data = process_xlsx_file(input_path)
        else:
            raise ValueError(f"不支援的檔案格式: {suffix}")

        # 正規化欄位名稱
        data = normalize_field_names(data)

    # 確保輸出目錄存在
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 儲存 JSON
    print(f"儲存至: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"完成！共 {len(data)} 筆藥品資料")
    return output_path


def main():
    print("=" * 60)
    print("處理泰國 FDA 藥品資料")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    raw_dir = base_dir / "data" / "raw"
    output_path = raw_dir / "th_fda_drugs.json"

    # 確保 raw 目錄存在
    raw_dir.mkdir(parents=True, exist_ok=True)

    # 尋找資料檔案
    input_path = find_data_file(raw_dir)

    # 處理資料
    process_data_file(input_path, output_path)

    print()
    print("下一步: 準備詞彙表資料")
    print("  uv run python scripts/prepare_external_data.py")


if __name__ == "__main__":
    main()
