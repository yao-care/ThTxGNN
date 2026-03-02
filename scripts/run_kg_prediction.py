#!/usr/bin/env python3
"""執行知識圖譜方法預測

使用 TxGNN 知識圖譜進行老藥新用預測。

使用方法:
    uv run python scripts/run_kg_prediction.py

前置條件:
    1. 已執行 process_fda_data.py
    2. 已執行 prepare_external_data.py

產生檔案:
    data/processed/repurposing_candidates.csv
"""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pandas as pd
import yaml

from txgnn.data.loader import load_fda_drugs, filter_active_drugs, get_drug_summary
from txgnn.mapping.drugbank_mapper import map_fda_drugs_to_drugbank
from txgnn.mapping.disease_mapper import (
    map_fda_indications_to_diseases,
    get_indication_mapping_stats,
)
from txgnn.predict.repurposing import find_repurposing_candidates


def load_field_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    print("=" * 60)
    print("執行 ThTxGNN 知識圖譜方法預測")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    config = load_field_config()
    field_mapping = config["field_mapping"]

    # 1. 載入藥品資料
    print("1. 載入泰國 FDA 藥品資料...")
    try:
        fda_df = load_fda_drugs()
        print(f"   總藥品數: {len(fda_df)}")

        active_df = filter_active_drugs(fda_df)
        print(f"   有效藥品數: {len(active_df)}")

        summary = get_drug_summary(active_df)
        print(f"   有成分資料: {summary.get('with_ingredient', 0)}")
        print(f"   有適應症資料: {summary.get('with_indication', 0)}")
    except FileNotFoundError as e:
        print(f"   錯誤: {e}")
        print("   請先執行: uv run python scripts/process_fda_data.py")
        return
    print()

    # 2. DrugBank 映射
    print("2. 執行 DrugBank 映射...")
    ingredient_field = field_mapping.get("ingredients", "active_ingredient")
    license_field = field_mapping.get("license_id", "registration_number")

    drug_mapping = map_fda_drugs_to_drugbank(
        active_df,
        ingredient_field=ingredient_field,
        license_field=license_field,
    )
    mapped_count = drug_mapping["drugbank_id"].notna().sum()
    total_count = len(drug_mapping)
    print(f"   總成分數: {total_count}")
    print(f"   映射成功: {mapped_count}")
    print(f"   映射率: {mapped_count / total_count * 100:.2f}%")
    print()

    # 3. 疾病映射
    print("3. 執行疾病映射...")
    indication_field = field_mapping.get("indication", "indication")
    brand_field = field_mapping.get("brand_name_local", "trade_name_th")

    indication_mapping = map_fda_indications_to_diseases(
        active_df,
        indication_field=indication_field,
        license_field=license_field,
        brand_field=brand_field,
    )
    indication_stats = get_indication_mapping_stats(indication_mapping)
    print(f"   總適應症數: {indication_stats['total_indications']}")
    print(f"   映射成功: {indication_stats['mapped_indications']}")
    print(f"   映射率: {indication_stats['mapping_rate'] * 100:.2f}%")
    print(f"   唯一疾病數: {indication_stats['unique_diseases']}")
    print()

    # 4. 尋找老藥新用候選
    print("4. 尋找老藥新用候選...")
    candidates = find_repurposing_candidates(drug_mapping, indication_mapping)
    print(f"   候選數: {len(candidates)}")
    print()

    # 5. 儲存結果
    print("5. 儲存結果...")
    output_dir = base_dir / "data" / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 儲存各階段結果
    drug_mapping.to_csv(output_dir / "drug_mapping.csv", index=False)
    indication_mapping.to_csv(output_dir / "indication_mapping.csv", index=False)
    candidates.to_csv(output_dir / "repurposing_candidates.csv", index=False)

    print(f"   drug_mapping.csv: {len(drug_mapping)} 筆")
    print(f"   indication_mapping.csv: {len(indication_mapping)} 筆")
    print(f"   repurposing_candidates.csv: {len(candidates)} 筆")
    print()

    # 6. 摘要統計
    print("=" * 60)
    print("摘要統計")
    print("=" * 60)
    print(f"Thai FDA 藥品總數: {len(fda_df)}")
    print(f"有效藥品數: {len(active_df)}")
    print(f"DrugBank 映射率: {mapped_count / total_count * 100:.2f}%")
    print(f"疾病映射率: {indication_stats['mapping_rate'] * 100:.2f}%")
    print(f"老藥新用候選數: {len(candidates)}")
    print()
    print("完成！")
    print()
    print("下一步: 生成 FHIR 資源")
    print("  uv run python scripts/generate_fhir_resources.py")


if __name__ == "__main__":
    main()
