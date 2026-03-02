#!/usr/bin/env python3
"""生成 FHIR R4 資源

從預測結果生成 FHIR 格式的資源檔案。

使用方法:
    uv run python scripts/generate_fhir_resources.py

前置條件:
    已執行 run_kg_prediction.py

產生檔案:
    docs/fhir/metadata
    docs/fhir/MedicationKnowledge/*.json
    docs/fhir/ClinicalUseDefinition/*.json
"""

import json
import re
from pathlib import Path
from datetime import datetime

import pandas as pd


# Thailand configuration
BASE_URL = "https://thtxgnn.github.io"

JURISDICTION = {
    "coding": [{
        "system": "urn:iso:std:iso:3166",
        "code": "TH",
        "display": "Thailand"
    }]
}


def slugify(text: str) -> str:
    """Convert text to URL-safe slug"""
    if not text:
        return ""
    text = str(text).lower()
    text = re.sub(r"[^\w\-]", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")[:50]


def generate_capability_statement() -> dict:
    """生成 CapabilityStatement (metadata)"""
    return {
        "resourceType": "CapabilityStatement",
        "id": "thtxgnn-fhir-server",
        "url": f"{BASE_URL}/fhir/metadata",
        "version": "1.0.0",
        "name": "ThTxGNNFHIRServer",
        "title": "Thailand TxGNN FHIR Server",
        "status": "active",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "publisher": "ThTxGNN Project",
        "description": "FHIR R4 server providing drug repurposing predictions for Thailand",
        "kind": "instance",
        "fhirVersion": "4.0.1",
        "format": ["json"],
        "rest": [{
            "mode": "server",
            "resource": [
                {
                    "type": "MedicationKnowledge",
                    "interaction": [{"code": "read"}, {"code": "search-type"}]
                },
                {
                    "type": "ClinicalUseDefinition",
                    "interaction": [{"code": "read"}, {"code": "search-type"}]
                }
            ]
        }]
    }


def generate_medication_knowledge(drug_name: str, drugbank_id: str, evidence_level: str) -> dict:
    """生成 MedicationKnowledge 資源"""
    slug = slugify(drug_name)
    return {
        "resourceType": "MedicationKnowledge",
        "id": slug,
        "status": "active",
        "code": {
            "coding": [
                {
                    "system": "https://go.drugbank.com/drugs",
                    "code": drugbank_id,
                    "display": drug_name
                }
            ]
        },
        "intendedJurisdiction": [JURISDICTION],
        "extension": [{
            "url": f"{BASE_URL}/fhir/StructureDefinition/evidence-level",
            "valueCode": evidence_level
        }]
    }


def generate_clinical_use_definition(
    drug_name: str,
    drugbank_id: str,
    indication: str,
    evidence_level: str
) -> dict:
    """生成 ClinicalUseDefinition 資源"""
    drug_slug = slugify(drug_name)
    indication_slug = slugify(indication)
    resource_id = f"{drug_slug}-{indication_slug}"

    return {
        "resourceType": "ClinicalUseDefinition",
        "id": resource_id,
        "type": "indication",
        "status": "active",
        "subject": [{"reference": f"MedicationKnowledge/{drug_slug}"}],
        "indication": {
            "diseaseSymptomProcedure": {
                "concept": {"text": indication}
            }
        },
        "extension": [
            {
                "url": f"{BASE_URL}/fhir/StructureDefinition/evidence-level",
                "valueCode": evidence_level
            },
            {
                "url": f"{BASE_URL}/fhir/StructureDefinition/source",
                "valueString": "TxGNN Knowledge Graph"
            }
        ]
    }


def main():
    print("=" * 60)
    print("生成 ThTxGNN FHIR R4 資源")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    fhir_dir = base_dir / "docs" / "fhir"

    # 建立目錄
    (fhir_dir / "MedicationKnowledge").mkdir(parents=True, exist_ok=True)
    (fhir_dir / "ClinicalUseDefinition").mkdir(parents=True, exist_ok=True)

    # 1. 生成 CapabilityStatement
    print("1. 生成 CapabilityStatement...")
    metadata = generate_capability_statement()
    with open(fhir_dir / "metadata", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    print(f"   已儲存: {fhir_dir / 'metadata'}")

    # 2. 載入預測結果
    print("2. 載入預測結果...")
    candidates_path = base_dir / "data" / "processed" / "repurposing_candidates.csv"

    if not candidates_path.exists():
        print(f"   找不到預測結果: {candidates_path}")
        print("   請先執行 run_kg_prediction.py")
        return

    candidates = pd.read_csv(candidates_path)
    print(f"   載入 {len(candidates)} 筆預測")

    if len(candidates) == 0:
        print("   沒有預測結果，跳過 FHIR 資源生成")
        return

    # 3. 生成 MedicationKnowledge
    print("3. 生成 MedicationKnowledge 資源...")
    drug_info = candidates[["drug_ingredient", "drugbank_id"]].drop_duplicates()
    drug_count = 0

    for _, row in drug_info.iterrows():
        drug_name = row["drug_ingredient"]
        drugbank_id = row["drugbank_id"]

        if not drug_name or pd.isna(drugbank_id):
            continue

        evidence_level = "L5"  # Knowledge graph level
        resource = generate_medication_knowledge(drug_name, drugbank_id, evidence_level)
        slug = slugify(drug_name)
        filepath = fhir_dir / "MedicationKnowledge" / f"{slug}.json"

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(resource, f, indent=2, ensure_ascii=False)
        drug_count += 1

    print(f"   生成 {drug_count} 個 MedicationKnowledge 資源")

    # 4. 生成 ClinicalUseDefinition
    print("4. 生成 ClinicalUseDefinition 資源...")
    cud_count = 0

    for _, row in candidates.iterrows():
        drug_name = row.get("drug_ingredient", "")
        drugbank_id = row.get("drugbank_id", "")
        indication = row.get("potential_indication", "")

        if not drug_name or not indication or pd.isna(drugbank_id):
            continue

        evidence_level = "L5"
        resource = generate_clinical_use_definition(drug_name, drugbank_id, indication, evidence_level)

        drug_slug = slugify(drug_name)
        indication_slug = slugify(indication)
        filename = f"{drug_slug}-{indication_slug}.json"
        filepath = fhir_dir / "ClinicalUseDefinition" / filename

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(resource, f, indent=2, ensure_ascii=False)
        cud_count += 1

    print(f"   生成 {cud_count} 個 ClinicalUseDefinition 資源")

    print()
    print("=" * 60)
    print("完成！")
    print("=" * 60)
    print(f"FHIR 資源已儲存至: {fhir_dir}")
    print(f"  - CapabilityStatement: 1")
    print(f"  - MedicationKnowledge: {drug_count}")
    print(f"  - ClinicalUseDefinition: {cud_count}")


if __name__ == "__main__":
    main()
