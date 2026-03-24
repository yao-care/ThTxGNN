#!/usr/bin/env python3
"""Generate news monitoring keywords from drug repurposing predictions.

This script generates keyword patterns for monitoring health news
related to drug repurposing candidates.

Usage:
    uv run python scripts/generate_news_keywords.py

Output:
    data/news/keywords.json
"""

import json
from pathlib import Path
from typing import Any

import pandas as pd


def load_synonyms() -> dict:
    """Load drug and disease synonyms."""
    synonyms_path = Path(__file__).parent.parent / "data" / "news" / "synonyms.json"
    if synonyms_path.exists():
        with open(synonyms_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"diseases": {}, "drugs": {}, "keywords": {}}


def generate_drug_keywords(candidates: pd.DataFrame, synonyms: dict) -> list[dict]:
    """Generate keyword patterns for each drug."""
    keywords = []

    # Get unique drugs
    drugs = candidates["drug_ingredient"].dropna().unique()

    for drug in drugs:
        drug_lower = drug.lower()

        # Get synonyms for this drug
        drug_synonyms = synonyms.get("drugs", {}).get(drug_lower, [drug_lower])
        if drug_lower not in drug_synonyms:
            drug_synonyms.append(drug_lower)

        # Get indications for this drug
        drug_indications = candidates[
            candidates["drug_ingredient"] == drug
        ]["potential_indication"].dropna().unique().tolist()

        # Generate patterns
        patterns = []
        for syn in drug_synonyms:
            patterns.append(syn)
            # Add Thai transliteration patterns if available
            if syn.isascii():
                patterns.append(f'"{syn}"')

        keywords.append({
            "drug": drug,
            "drugbank_id": candidates[
                candidates["drug_ingredient"] == drug
            ]["drugbank_id"].iloc[0] if len(candidates[candidates["drug_ingredient"] == drug]) > 0 else None,
            "search_terms": list(set(patterns)),
            "indications": drug_indications[:10],  # Limit to top 10
        })

    return keywords


def generate_disease_keywords(candidates: pd.DataFrame, synonyms: dict) -> list[dict]:
    """Generate keyword patterns for each disease."""
    keywords = []

    # Get unique diseases
    diseases = candidates["potential_indication"].dropna().unique()

    for disease in diseases:
        disease_lower = disease.lower()

        # Get synonyms for this disease
        disease_synonyms = synonyms.get("diseases", {}).get(disease_lower, [disease_lower])
        if disease_lower not in disease_synonyms:
            disease_synonyms.append(disease_lower)

        # Get drugs for this disease
        disease_drugs = candidates[
            candidates["potential_indication"] == disease
        ]["drug_ingredient"].dropna().unique().tolist()

        keywords.append({
            "disease": disease,
            "search_terms": list(set(disease_synonyms)),
            "related_drugs": disease_drugs[:10],  # Limit to top 10
        })

    return keywords


def generate_repurposing_patterns(synonyms: dict) -> list[str]:
    """Generate general drug repurposing search patterns."""
    base_patterns = synonyms.get("keywords", {}).get("drug_repurposing", [])

    # Add Thai-specific patterns
    thai_patterns = [
        "ยาใหม่",
        "การค้นพบยา",
        "ประโยชน์ใหม่ของยา",
        "ข้อบ่งใช้ใหม่",
        "การนำยามาใช้ใหม่",
    ]

    # Add English patterns
    english_patterns = [
        "drug repurposing",
        "drug repositioning",
        "off-label use",
        "new indication",
        "therapeutic potential",
    ]

    all_patterns = list(set(base_patterns + thai_patterns + english_patterns))
    return all_patterns


def main():
    print("=" * 60)
    print("Generate News Monitoring Keywords")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent

    # Load predictions
    print("1. Loading predictions...")
    candidates_path = base_dir / "data" / "processed" / "repurposing_candidates.csv.gz"

    if not candidates_path.exists():
        print(f"   Predictions not found: {candidates_path}")
        print("   Please run run_kg_prediction.py first")
        return

    candidates = pd.read_csv(candidates_path)
    print(f"   Loaded {len(candidates)} predictions")

    # Load synonyms
    print("2. Loading synonyms...")
    synonyms = load_synonyms()
    print(f"   Drugs: {len(synonyms.get('drugs', {}))}")
    print(f"   Diseases: {len(synonyms.get('diseases', {}))}")

    # Generate keywords
    print("3. Generating keywords...")

    drug_keywords = generate_drug_keywords(candidates, synonyms)
    print(f"   Drug keywords: {len(drug_keywords)}")

    disease_keywords = generate_disease_keywords(candidates, synonyms)
    print(f"   Disease keywords: {len(disease_keywords)}")

    repurposing_patterns = generate_repurposing_patterns(synonyms)
    print(f"   Repurposing patterns: {len(repurposing_patterns)}")

    # Compile output
    output = {
        "version": "1.0.0",
        "generated_from": "repurposing_candidates.csv.gz",
        "drug_count": len(drug_keywords),
        "disease_count": len(disease_keywords),
        "drugs": drug_keywords,
        "diseases": disease_keywords,
        "repurposing_patterns": repurposing_patterns,
        "news_sources": [
            {
                "name": "Thai Health News",
                "type": "rss",
                "url": "https://www.hfocus.org/feed",
                "language": "th"
            },
            {
                "name": "Bangkok Post Health",
                "type": "web",
                "url": "https://www.bangkokpost.com/thailand/general/health",
                "language": "en"
            },
            {
                "name": "PubMed",
                "type": "api",
                "url": "https://pubmed.ncbi.nlm.nih.gov/",
                "language": "en"
            }
        ]
    }

    # Save output
    print("4. Saving keywords...")
    output_path = base_dir / "data" / "news" / "keywords.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"   Saved to: {output_path}")
    print()
    print("Done!")


if __name__ == "__main__":
    main()
