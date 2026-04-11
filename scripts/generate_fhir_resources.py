#!/usr/bin/env python3
"""
Generate FHIR R4 resources from ThTxGNN drug prediction data.

This script reads the search-index.json and generates:
- MedicationKnowledge resources for each drug
- ClinicalUseDefinition resources for each predicted indication
- A Bundle containing all resources
- A CapabilityStatement (metadata)
"""

import json
import re
from datetime import datetime
from pathlib import Path


def slugify(text: str) -> str:
    """Convert text to URL-safe slug."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def create_medication_knowledge(drug: dict, base_url: str) -> dict:
    """Create a FHIR MedicationKnowledge resource for a drug."""
    resource = {
        "resourceType": "MedicationKnowledge",
        "id": drug["slug"],
        "meta": {
            "profile": ["http://hl7.org/fhir/StructureDefinition/MedicationKnowledge"]
        },
        "status": "active",
        "code": {
            "coding": [
                {
                    "system": f"{base_url}/drugs",
                    "code": drug["slug"],
                    "display": drug["name"]
                }
            ],
            "text": drug["name"]
        },
        "intendedJurisdiction": [
            {
                "coding": [
                    {
                        "system": "urn:iso:std:iso:3166",
                        "code": "TW",
                        "display": "Taiwan"
                    }
                ]
            }
        ],
        "extension": [
            {
                "url": f"{base_url}/fhir/StructureDefinition/evidence-level",
                "valueCode": drug.get("level", "L5")
            }
        ]
    }

    # Add original indication if available
    if drug.get("original"):
        resource["indicationGuideline"] = [
            {
                "indication": [
                    {
                        "reference": {
                            "display": drug["original"][:200]  # Truncate if too long
                        }
                    }
                ]
            }
        ]

    # Add brand names if available
    if drug.get("brands"):
        resource["synonym"] = drug["brands"]

    return resource


def create_clinical_use_definition(
    drug: dict,
    indication: dict,
    base_url: str
) -> dict:
    """Create a FHIR ClinicalUseDefinition resource for a predicted indication."""
    ind_slug = slugify(indication["name"])
    resource_id = f"{drug['slug']}-{ind_slug}"[:64]  # Limit ID length

    resource = {
        "resourceType": "ClinicalUseDefinition",
        "id": resource_id,
        "meta": {
            "profile": ["http://hl7.org/fhir/StructureDefinition/ClinicalUseDefinition"]
        },
        "type": "indication",
        "status": {
            "coding": [
                {
                    "system": "http://hl7.org/fhir/publication-status",
                    "code": "draft",
                    "display": "Draft"
                }
            ]
        },
        "subject": [
            {
                "reference": f"MedicationKnowledge/{drug['slug']}"
            }
        ],
        "indication": {
            "diseaseSymptomProcedure": {
                "concept": {
                    "text": indication["name"]
                }
            }
        },
        "extension": [
            {
                "url": f"{base_url}/fhir/StructureDefinition/prediction-status",
                "valueCode": "predicted"
            },
            {
                "url": f"{base_url}/fhir/StructureDefinition/evidence-level",
                "valueCode": indication.get("level", "L5")
            },
            {
                "url": f"{base_url}/fhir/StructureDefinition/txgnn-score",
                "valueDecimal": indication.get("score", 0) / 100  # Convert to 0-1 scale
            }
        ]
    }

    return resource


def create_capability_statement(base_url: str, drug_count: int, indication_count: int) -> dict:
    """Create a FHIR CapabilityStatement (metadata)."""
    return {
        "resourceType": "CapabilityStatement",
        "id": "thtxgnn-fhir-server",
        "url": f"{base_url}/fhir/metadata",
        "version": "1.0.0",
        "name": "ThTxGNNFHIRServer",
        "title": "ThTxGNN FHIR Server",
        "status": "active",
        "experimental": True,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "publisher": "ThTxGNN",
        "contact": [
            {
                "telecom": [
                    {
                        "system": "url",
                        "value": base_url
                    }
                ]
            }
        ],
        "description": f"ThTxGNN drug repurposing prediction data exposed as FHIR resources. Contains {drug_count} drugs and {indication_count} predicted indications.",
        "kind": "instance",
        "software": {
            "name": "ThTxGNN Static FHIR API",
            "version": "1.0.0"
        },
        "implementation": {
            "description": "Static FHIR resources served from GitHub Pages",
            "url": f"{base_url}/fhir"
        },
        "fhirVersion": "4.0.1",
        "format": ["application/fhir+json"],
        "rest": [
            {
                "mode": "server",
                "documentation": "Static FHIR API - read-only access to drug repurposing predictions",
                "resource": [
                    {
                        "type": "MedicationKnowledge",
                        "profile": "http://hl7.org/fhir/StructureDefinition/MedicationKnowledge",
                        "interaction": [
                            {"code": "read"}
                        ],
                        "searchParam": [
                            {
                                "name": "_id",
                                "type": "token",
                                "documentation": "Drug identifier (slug)"
                            }
                        ]
                    },
                    {
                        "type": "ClinicalUseDefinition",
                        "profile": "http://hl7.org/fhir/StructureDefinition/ClinicalUseDefinition",
                        "interaction": [
                            {"code": "read"}
                        ],
                        "searchParam": [
                            {
                                "name": "subject",
                                "type": "reference",
                                "documentation": "Reference to MedicationKnowledge"
                            }
                        ]
                    }
                ]
            }
        ]
    }


def create_bundle(entries: list, base_url: str) -> dict:
    """Create a FHIR Bundle containing all resources."""
    return {
        "resourceType": "Bundle",
        "id": "all-predictions",
        "type": "collection",
        "timestamp": datetime.now().isoformat(),
        "total": len(entries),
        "link": [
            {
                "relation": "self",
                "url": f"{base_url}/fhir/Bundle/all-predictions.json"
            }
        ],
        "entry": [
            {
                "fullUrl": f"{base_url}/fhir/{entry['resourceType']}/{entry['id']}",
                "resource": entry
            }
            for entry in entries
        ]
    }


def main():
    """Main function to generate FHIR resources."""
    # Configuration
    base_url = "https://thtxgnn.yao.care"
    project_root = Path(__file__).parent.parent
    input_file = project_root / "docs" / "data" / "search-index.json"
    output_dir = project_root / "docs" / "fhir"

    print(f"Reading search index from {input_file}")

    # Load search index
    with open(input_file, "r", encoding="utf-8") as f:
        search_index = json.load(f)

    drugs = search_index.get("drugs", [])
    print(f"Found {len(drugs)} drugs")

    # Create output directories
    (output_dir / "MedicationKnowledge").mkdir(parents=True, exist_ok=True)
    (output_dir / "ClinicalUseDefinition").mkdir(parents=True, exist_ok=True)
    (output_dir / "Bundle").mkdir(parents=True, exist_ok=True)

    # Generate resources
    all_resources = []
    total_indications = 0

    for drug in drugs:
        # Create MedicationKnowledge
        med_knowledge = create_medication_knowledge(drug, base_url)
        all_resources.append(med_knowledge)

        # Save MedicationKnowledge
        output_file = output_dir / "MedicationKnowledge" / f"{drug['slug']}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(med_knowledge, f, ensure_ascii=False, indent=2)

        # Create ClinicalUseDefinition for each indication
        for indication in drug.get("indications", []):
            clinical_use = create_clinical_use_definition(drug, indication, base_url)
            all_resources.append(clinical_use)
            total_indications += 1

            # Save ClinicalUseDefinition
            output_file = output_dir / "ClinicalUseDefinition" / f"{clinical_use['id']}.json"
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(clinical_use, f, ensure_ascii=False, indent=2)

    print(f"Generated {len(drugs)} MedicationKnowledge resources")
    print(f"Generated {total_indications} ClinicalUseDefinition resources")

    # Create CapabilityStatement (metadata)
    capability = create_capability_statement(base_url, len(drugs), total_indications)
    with open(output_dir / "metadata", "w", encoding="utf-8") as f:
        json.dump(capability, f, ensure_ascii=False, indent=2)
    print("Generated CapabilityStatement (metadata)")

    # Create Bundle with all resources
    bundle = create_bundle(all_resources, base_url)
    with open(output_dir / "Bundle" / "all-predictions.json", "w", encoding="utf-8") as f:
        json.dump(bundle, f, ensure_ascii=False, indent=2)
    print(f"Generated Bundle with {len(all_resources)} resources")

    print(f"\nFHIR resources generated successfully in {output_dir}")


if __name__ == "__main__":
    main()
