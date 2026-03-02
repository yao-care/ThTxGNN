#!/usr/bin/env python
"""Run LLM review on drug repurposing predictions.

Usage:
    # Mock mode (no API key needed)
    uv run python scripts/run_llm_review.py --mock

    # With OpenAI
    export OPENAI_API_KEY=your-key
    uv run python scripts/run_llm_review.py --provider openai

    # With Anthropic
    export ANTHROPIC_API_KEY=your-key
    uv run python scripts/run_llm_review.py --provider anthropic

    # With local Ollama
    uv run python scripts/run_llm_review.py --provider ollama --model llama2
"""

import argparse
import csv
import json
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from txgnn.review import LLMReviewer, create_mock_reviewer


def load_predictions(path: str, limit: int = 10) -> list[dict]:
    """Load predictions from CSV file."""
    predictions = []

    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        seen = set()

        for row in reader:
            drug = row.get("drug_ingredient", "")
            disease = row.get("potential_indication", "")
            key = f"{drug}:{disease}"

            if key not in seen and drug and disease:
                seen.add(key)
                predictions.append({
                    "drug": drug,
                    "disease": disease,
                    "drugbank_id": row.get("drugbank_id", ""),
                })

            if len(predictions) >= limit:
                break

    return predictions


def main():
    parser = argparse.ArgumentParser(description="Run LLM review on predictions")
    parser.add_argument(
        "--input",
        "-i",
        default="data/processed/repurposing_candidates.csv",
        help="Input predictions CSV",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="data/reports/llm_review.md",
        help="Output report path",
    )
    parser.add_argument(
        "--provider",
        "-p",
        default="openai",
        choices=["openai", "anthropic", "ollama"],
        help="LLM provider",
    )
    parser.add_argument(
        "--model",
        "-m",
        help="Model name (optional)",
    )
    parser.add_argument(
        "--limit",
        "-l",
        type=int,
        default=10,
        help="Max predictions to review",
    )
    parser.add_argument(
        "--mock",
        action="store_true",
        help="Use mock reviewer (no API calls)",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("ThTxGNN LLM Review")
    print("=" * 60)

    # Load predictions
    print(f"\n1. Loading predictions from {args.input}...")
    predictions = load_predictions(args.input, args.limit)
    print(f"   Loaded {len(predictions)} unique predictions")

    # Create reviewer
    print(f"\n2. Creating reviewer...")
    if args.mock:
        print("   Using mock reviewer (no API calls)")
        reviewer = create_mock_reviewer()
    else:
        print(f"   Provider: {args.provider}")
        print(f"   Model: {args.model or 'default'}")
        reviewer = LLMReviewer(
            provider=args.provider,
            model=args.model,
        )

    # Review predictions
    print(f"\n3. Reviewing {len(predictions)} predictions...")
    results = []
    for i, pred in enumerate(predictions, 1):
        print(f"   [{i}/{len(predictions)}] {pred['drug']} → {pred['disease']}")
        result = reviewer.review_prediction(pred["drug"], pred["disease"])
        results.append(result)
        print(f"       Confidence: {result.confidence}")

    # Generate report
    print(f"\n4. Generating report...")
    report = reviewer.generate_report(results, args.output)
    print(f"   Saved to: {args.output}")

    # Summary
    print("\n5. Summary:")
    confidence_counts = {"high": 0, "medium": 0, "low": 0}
    for r in results:
        confidence_counts[r.confidence] = confidence_counts.get(r.confidence, 0) + 1

    print(f"   High confidence: {confidence_counts['high']}")
    print(f"   Medium confidence: {confidence_counts['medium']}")
    print(f"   Low confidence: {confidence_counts['low']}")

    # Save JSON results
    json_path = Path(args.output).with_suffix(".json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(
            [
                {
                    "drug": r.drug,
                    "disease": r.disease,
                    "confidence": r.confidence,
                    "summary": r.summary,
                    "key_evidence": r.key_evidence,
                    "limitations": r.limitations,
                    "recommendation": r.recommendation,
                }
                for r in results
            ],
            f,
            ensure_ascii=False,
            indent=2,
        )
    print(f"   JSON saved to: {json_path}")

    print("\nDone!")


if __name__ == "__main__":
    main()
