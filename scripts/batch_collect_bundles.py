#!/usr/bin/env python3
"""Batch collect drug bundles (without LLM calls).

This script collects drug bundles including DDI data for multiple drugs.
It does NOT require an API key since it only collects data, no LLM generation.

Usage:
    # Collect top 10 drugs by prediction count
    python scripts/batch_collect_bundles.py --limit 10

    # Collect specific drugs
    python scripts/batch_collect_bundles.py --drugs "Amlodipine,Metformin,Aspirin"

    # Collect all drugs with high-confidence predictions
    python scripts/batch_collect_bundles.py --all --min-score 0.99

    # Parallel processing with offset (for running multiple instances)
    python scripts/batch_collect_bundles.py --all --offset 0 --limit 100 --skip-existing
    python scripts/batch_collect_bundles.py --all --offset 100 --limit 100 --skip-existing
"""

import argparse
import json
import sys
import time
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pandas as pd
from thtxgnn.collectors import DrugBundleAggregator
from thtxgnn.paths import get_bundles_dir, slugify


def get_prediction_drugs(
    predictions_path: Path | None = None,
    min_score: float = 0.99,
    offset: int = 0,
    limit: int | None = None,
) -> list[dict]:
    """Get list of drugs with predictions, sorted by prediction count."""
    if predictions_path is None:
        predictions_path = Path("data/processed/txgnn_dl_predictions.csv.gz")

    df = pd.read_csv(predictions_path)

    # Filter by score
    df = df[df["txgnn_score"] >= min_score]

    # Group by drug and count predictions
    drug_stats = df.groupby("drug_name").agg({
        "txgnn_score": ["count", "max", "mean"]
    }).reset_index()
    drug_stats.columns = ["drug_name", "prediction_count", "max_score", "mean_score"]
    drug_stats = drug_stats.sort_values("prediction_count", ascending=False)

    # Apply offset
    if offset > 0:
        drug_stats = drug_stats.iloc[offset:]

    # Apply limit
    if limit:
        drug_stats = drug_stats.head(limit)

    return drug_stats.to_dict("records")


def collect_single_drug(drug_name: str, top_n: int = 10, min_score: float = 0.99) -> dict:
    """Collect bundle for a single drug.

    Returns:
        dict with status, bundle_path, ddi_count, indication_count, error
    """
    result = {
        "drug": drug_name,
        "status": "pending",
        "bundle_path": None,
        "ddi_count": 0,
        "indication_count": 0,
        "error": None,
        "duration_seconds": 0,
    }

    start_time = time.time()

    try:
        aggregator = DrugBundleAggregator(save_collected=True)
        bundle = aggregator.collect(
            drug_name=drug_name,
            top_n=top_n,
            min_score=min_score,
        )

        # Save bundle
        bundle_path = bundle.save()

        # Get stats
        ddi_count = len(bundle.safety.get("ddi", []))
        indication_count = len(bundle.drug.predicted_indications)

        result.update({
            "status": "success",
            "bundle_path": str(bundle_path),
            "ddi_count": ddi_count,
            "indication_count": indication_count,
        })

    except Exception as e:
        result.update({
            "status": "error",
            "error": str(e),
        })

    result["duration_seconds"] = round(time.time() - start_time, 2)
    return result


def main():
    parser = argparse.ArgumentParser(description="Batch collect drug bundles")
    parser.add_argument("--drugs", type=str, help="Comma-separated list of drug names")
    parser.add_argument("--limit", type=int, help="Limit number of drugs to process")
    parser.add_argument("--offset", type=int, default=0, help="Start offset (for parallel processing)")
    parser.add_argument("--all", action="store_true", help="Process all drugs with predictions")
    parser.add_argument("--min-score", type=float, default=0.99, help="Minimum TxGNN score")
    parser.add_argument("--top-n", type=int, default=10, help="Top N predictions per drug")
    parser.add_argument("--output", type=str, help="Output JSON file for results")
    parser.add_argument("--skip-existing", action="store_true", help="Skip drugs with existing bundles")

    args = parser.parse_args()

    # Get drug list
    if args.drugs:
        drugs = [{"drug_name": d.strip()} for d in args.drugs.split(",")]
    elif args.all or args.limit:
        drugs = get_prediction_drugs(min_score=args.min_score, offset=args.offset, limit=args.limit)
    else:
        print("Please specify --drugs, --limit, or --all")
        sys.exit(1)

    # Filter out existing bundles if requested
    if args.skip_existing:
        bundles_dir = get_bundles_dir()
        original_count = len(drugs)
        drugs = [
            d for d in drugs
            if not (bundles_dir / slugify(d["drug_name"]) / "drug_bundle.json").exists()
        ]
        skipped = original_count - len(drugs)
        if skipped > 0:
            print(f"ข้าม {skipped} bundles ที่มีอยู่แล้ว")

    print(f"กำลังประมวลผล {len(drugs)} ยา (offset={args.offset})...")
    print("-" * 60)

    results = []
    for i, drug_info in enumerate(drugs, 1):
        drug_name = drug_info["drug_name"]
        print(f"[{i}/{len(drugs)}] {drug_name}...", end=" ", flush=True)

        result = collect_single_drug(
            drug_name=drug_name,
            top_n=args.top_n,
            min_score=args.min_score,
        )
        results.append(result)

        if result["status"] == "success":
            print(f"✓ DDI:{result['ddi_count']} Ind:{result['indication_count']} ({result['duration_seconds']}s)")
        else:
            print(f"✗ {result['error']}")

    # Summary
    print("-" * 60)
    success = sum(1 for r in results if r["status"] == "success")
    total_ddi = sum(r["ddi_count"] for r in results)
    total_ind = sum(r["indication_count"] for r in results)
    print(f"เสร็จสิ้น: {success}/{len(drugs)} สำเร็จ")
    print(f"รวม DDI: {total_ddi}, รวมข้อบ่งใช้: {total_ind}")

    # Save results
    if args.output:
        output_path = Path(args.output)
        output_path.write_text(json.dumps(results, indent=2, ensure_ascii=False))
        print(f"บันทึกผลลัพธ์: {output_path}")

    return results


if __name__ == "__main__":
    main()
