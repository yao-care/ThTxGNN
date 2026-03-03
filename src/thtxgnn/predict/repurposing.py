"""老藥新用預測 - 基於 TxGNN 知識圖譜"""

from pathlib import Path
from typing import Dict, Optional, Set

import pandas as pd


def load_drug_disease_relations(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 TxGNN 藥物-疾病關係

    Args:
        filepath: CSV 檔案路徑

    Returns:
        藥物-疾病關係 DataFrame
    """
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "drug_disease_relations.csv"

    return pd.read_csv(filepath)


def build_drug_indication_map(relations_df: pd.DataFrame) -> Dict[str, Set[str]]:
    """建立藥物 -> 適應症集合的映射

    Args:
        relations_df: 藥物-疾病關係 DataFrame

    Returns:
        {drug_name: {disease1, disease2, ...}}
    """
    # 只取 indication 和 off-label use
    indications = relations_df[relations_df["relation"].isin(["indication", "off-label use"])]

    drug_map = {}
    for _, row in indications.iterrows():
        drug = row["x_name"].upper()
        disease = row["y_name"]

        if drug not in drug_map:
            drug_map[drug] = set()
        drug_map[drug].add(disease)

    return drug_map


def find_repurposing_candidates(
    drug_mapping_df: pd.DataFrame,
    indication_mapping_df: pd.DataFrame,
    relations_df: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """找出老藥新用候選

    比較藥品的現有適應症與 TxGNN 知識圖譜中的適應症，
    找出可能的新適應症。

    Args:
        drug_mapping_df: 藥品 DrugBank 映射結果
        indication_mapping_df: 適應症疾病映射結果
        relations_df: TxGNN 藥物-疾病關係

    Returns:
        老藥新用候選 DataFrame
    """
    if relations_df is None:
        relations_df = load_drug_disease_relations()

    # 建立 TxGNN 藥物適應症映射
    kg_drug_map = build_drug_indication_map(relations_df)

    # 建立藥品的現有適應症（向量化操作）
    tw_diseases_df = indication_mapping_df[
        indication_mapping_df["disease_name"].notna()
    ][["license_id", "disease_name"]].copy()
    tw_diseases_df["disease_lower"] = tw_diseases_df["disease_name"].str.lower()
    tw_drug_diseases = tw_diseases_df.groupby("license_id")["disease_lower"].apply(set).to_dict()

    # 建立藥品資訊索引（向量化）
    valid_drugs = drug_mapping_df[drug_mapping_df["drugbank_id"].notna()].copy()

    if len(valid_drugs) == 0:
        # 沒有映射成功的藥物，返回空結果
        return pd.DataFrame(columns=[
            "license_id", "brand_name", "drug_ingredient",
            "drugbank_id", "potential_indication", "source"
        ])

    # 取得唯一的 (license_id, 藥物成分) 組合
    unique_pairs = valid_drugs[["license_id", "normalized_ingredient", "brand_name", "drugbank_id"]].drop_duplicates()

    candidates = []

    for _, row in unique_pairs.iterrows():
        license_no = row["license_id"]
        drug_name = row["normalized_ingredient"]

        # 查詢 TxGNN 中該藥物的所有適應症
        kg_diseases = kg_drug_map.get(drug_name, set())
        if not kg_diseases:
            continue

        # 取得現有適應症
        tw_diseases = tw_drug_diseases.get(license_no, set())

        # 找出潛在新適應症
        for disease in kg_diseases:
            disease_lower = disease.lower()

            # 快速檢查是否已存在
            is_new = all(
                tw_d not in disease_lower and disease_lower not in tw_d
                for tw_d in tw_diseases
            )

            if is_new:
                candidates.append({
                    "license_id": license_no,
                    "brand_name": row["brand_name"],
                    "drug_ingredient": drug_name,
                    "drugbank_id": row["drugbank_id"],
                    "potential_indication": disease,
                    "source": "TxGNN Knowledge Graph",
                })

    result_df = pd.DataFrame(candidates)

    # 去重
    if len(result_df) > 0:
        result_df = result_df.drop_duplicates(
            subset=["license_id", "drug_ingredient", "potential_indication"]
        )

    return result_df


def generate_repurposing_report(candidates_df: pd.DataFrame) -> dict:
    """生成老藥新用報告統計

    Args:
        candidates_df: 候選藥物 DataFrame

    Returns:
        統計報告字典
    """
    if len(candidates_df) == 0:
        return {
            "total_candidates": 0,
            "unique_drugs": 0,
            "unique_diseases": 0,
            "top_diseases": [],
            "top_drugs": [],
        }

    unique_drugs = candidates_df["drug_ingredient"].nunique()
    unique_diseases = candidates_df["potential_indication"].nunique()

    # 最常見的潛在新適應症
    top_diseases = candidates_df["potential_indication"].value_counts().head(10).to_dict()

    # 最多潛在新適應症的藥物
    drug_counts = candidates_df.groupby("drug_ingredient")["potential_indication"].nunique()
    top_drugs = drug_counts.sort_values(ascending=False).head(10).to_dict()

    return {
        "total_candidates": len(candidates_df),
        "unique_drugs": unique_drugs,
        "unique_diseases": unique_diseases,
        "top_diseases": top_diseases,
        "top_drugs": top_drugs,
    }
