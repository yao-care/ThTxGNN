"""Thai FDA 藥品資料載入與過濾"""

import json
from pathlib import Path
from typing import Optional

import pandas as pd
import yaml


def load_field_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent.parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_fda_drugs(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入泰國 FDA 藥品資料

    Args:
        filepath: JSON 檔案路徑，預設為 data/raw/th_fda_drugs.json

    Returns:
        包含所有藥品的 DataFrame

    Raises:
        FileNotFoundError: 找不到資料檔案時，提供下載指引
    """
    config = load_field_config()

    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "raw" / "th_fda_drugs.json"

    if not filepath.exists():
        raise FileNotFoundError(
            f"找不到 Thai FDA 藥品資料: {filepath}\n"
            f"請先執行以下步驟：\n"
            f"1. 從 Thai FDA 網站下載資料:\n"
            f"   https://pertento.fda.moph.go.th/FDA_SEARCH_DRUG/SEARCH_DRUG/FRM_SEARCH_DRUG.aspx\n"
            f"   或 https://catalog.fda.moph.go.th/dataset/web-service-drug-reg\n"
            f"2. 放到 data/raw/ 目錄\n"
            f"3. 執行: uv run python scripts/process_fda_data.py"
        )

    with open(filepath, "r", encoding=config.get("encoding", "utf-8")) as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    return df


def convert_buddhist_year(date_str: str) -> str:
    """將泰國佛曆年份轉換為西元年份

    Args:
        date_str: 佛曆日期字串 (例如 2567-01-15)

    Returns:
        西元日期字串 (例如 2024-01-15)
    """
    if not date_str or pd.isna(date_str):
        return date_str

    try:
        parts = str(date_str).split("-")
        if len(parts) >= 1:
            year = int(parts[0])
            # 佛曆年份通常 > 2500，西元年份 < 2100
            if year > 2500:
                parts[0] = str(year - 543)
                return "-".join(parts)
    except (ValueError, TypeError):
        pass

    return date_str


def filter_active_drugs(df: pd.DataFrame) -> pd.DataFrame:
    """過濾有效藥品（排除已註銷）

    Args:
        df: 原始藥品 DataFrame

    Returns:
        僅包含有效藥品的 DataFrame
    """
    config = load_field_config()
    field_mapping = config["field_mapping"]
    withdrawn_statuses = config.get("withdrawn_statuses", [])

    # 取得狀態欄位名稱
    status_field = field_mapping.get("status", "")

    if status_field and status_field in df.columns:
        # 過濾未註銷的藥品
        active = df[~df[status_field].isin(withdrawn_statuses)].copy()
    else:
        active = df.copy()

    # 過濾有主成分的藥品（TxGNN 需要）
    ingredients_field = field_mapping.get("ingredients", "")
    if ingredients_field and ingredients_field in df.columns:
        active = active[active[ingredients_field].notna() & (active[ingredients_field] != "")]

    # 重設索引
    active = active.reset_index(drop=True)

    return active


def get_drug_summary(df: pd.DataFrame) -> dict:
    """取得藥品資料摘要統計

    Args:
        df: 藥品 DataFrame

    Returns:
        摘要統計字典
    """
    config = load_field_config()
    field_mapping = config["field_mapping"]

    ingredients_field = field_mapping.get("ingredients", "")
    indication_field = field_mapping.get("indication", "")
    dosage_form_field = field_mapping.get("dosage_form", "")

    summary = {"total_count": len(df)}

    if ingredients_field and ingredients_field in df.columns:
        summary["with_ingredient"] = int(df[ingredients_field].notna().sum())
        summary["unique_ingredients"] = int(df[ingredients_field].nunique())

    if indication_field and indication_field in df.columns:
        summary["with_indication"] = int(df[indication_field].notna().sum())

    if dosage_form_field and dosage_form_field in df.columns:
        summary["dosage_forms"] = df[dosage_form_field].value_counts().head(10).to_dict()

    return summary


def normalize_ingredient_name(name: str) -> str:
    """正規化成分名稱

    Args:
        name: 原始成分名稱

    Returns:
        正規化後的成分名稱
    """
    if not name or pd.isna(name):
        return ""

    # 轉小寫
    name = str(name).lower().strip()

    # 移除常見的鹽類後綴變體
    salt_suffixes = [
        " hydrochloride", " hcl", " sodium", " potassium",
        " calcium", " magnesium", " sulfate", " sulphate",
        " acetate", " citrate", " phosphate", " maleate",
        " fumarate", " tartrate", " succinate", " mesylate",
        " besylate", " bromide", " chloride", " nitrate"
    ]

    for suffix in salt_suffixes:
        if name.endswith(suffix):
            name = name[:-len(suffix)]
            break

    return name.strip()
