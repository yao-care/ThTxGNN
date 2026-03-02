"""End-to-end validation tests for ThTxGNN."""

import json
from pathlib import Path

import pytest


BASE_DIR = Path(__file__).parent.parent


class TestDataFiles:
    """Test that all required data files exist."""

    def test_txgnn_data_exists(self):
        """Check TxGNN knowledge graph data exists."""
        assert (BASE_DIR / "data" / "node.csv").exists(), "node.csv not found"
        assert (BASE_DIR / "data" / "kg.csv").exists(), "kg.csv not found"

    def test_external_vocab_exists(self):
        """Check external vocabulary files exist."""
        external_dir = BASE_DIR / "data" / "external"
        assert (external_dir / "drugbank_vocab.csv").exists()
        assert (external_dir / "disease_vocab.csv").exists()
        assert (external_dir / "drug_disease_relations.csv").exists()

    def test_processed_data_exists(self):
        """Check processed data files exist."""
        processed_dir = BASE_DIR / "data" / "processed"
        assert (processed_dir / "repurposing_candidates.csv").exists()
        assert (processed_dir / "drug_mapping.csv").exists()
        assert (processed_dir / "indication_mapping.csv").exists()


class TestFHIRResources:
    """Test FHIR resource generation."""

    def test_capability_statement_exists(self):
        """Check CapabilityStatement exists."""
        metadata_path = BASE_DIR / "docs" / "fhir" / "metadata"
        assert metadata_path.exists()

        with open(metadata_path) as f:
            data = json.load(f)

        assert data["resourceType"] == "CapabilityStatement"
        assert data["fhirVersion"] == "4.0.1"

    def test_medication_knowledge_exists(self):
        """Check MedicationKnowledge resources exist."""
        mk_dir = BASE_DIR / "docs" / "fhir" / "MedicationKnowledge"
        assert mk_dir.exists()
        assert len(list(mk_dir.glob("*.json"))) > 0

    def test_clinical_use_definition_exists(self):
        """Check ClinicalUseDefinition resources exist."""
        cud_dir = BASE_DIR / "docs" / "fhir" / "ClinicalUseDefinition"
        assert cud_dir.exists()
        assert len(list(cud_dir.glob("*.json"))) > 0


class TestNewsMonitoring:
    """Test news monitoring configuration."""

    def test_keywords_json_exists(self):
        """Check keywords.json exists and is valid."""
        keywords_path = BASE_DIR / "data" / "news" / "keywords.json"
        assert keywords_path.exists()

        with open(keywords_path, encoding="utf-8") as f:
            data = json.load(f)

        assert "drugs" in data
        assert "diseases" in data
        assert "repurposing_patterns" in data

    def test_synonyms_json_exists(self):
        """Check synonyms.json exists."""
        synonyms_path = BASE_DIR / "data" / "news" / "synonyms.json"
        assert synonyms_path.exists()


class TestConfiguration:
    """Test configuration files."""

    def test_fields_yaml_exists(self):
        """Check fields.yaml configuration exists."""
        fields_path = BASE_DIR / "config" / "fields.yaml"
        assert fields_path.exists()

    def test_pyproject_toml_exists(self):
        """Check pyproject.toml exists."""
        assert (BASE_DIR / "pyproject.toml").exists()


class TestDocs:
    """Test documentation files."""

    def test_jekyll_config_exists(self):
        """Check Jekyll config exists."""
        assert (BASE_DIR / "docs" / "_config.yml").exists()

    def test_index_page_exists(self):
        """Check index page exists."""
        assert (BASE_DIR / "docs" / "index.md").exists()

    def test_smart_launch_exists(self):
        """Check SMART App launch page exists."""
        assert (BASE_DIR / "docs" / "smart" / "launch.html").exists()


class TestQualityMetrics:
    """Test quality metrics meet thresholds."""

    def test_drugbank_mapping_rate(self):
        """Check DrugBank mapping rate is acceptable."""
        import pandas as pd

        mapping_path = BASE_DIR / "data" / "processed" / "drug_mapping.csv"
        df = pd.read_csv(mapping_path)

        mapped = df["drugbank_id"].notna().sum()
        total = len(df)
        rate = mapped / total if total > 0 else 0

        # Target: > 50%
        assert rate >= 0.5, f"DrugBank mapping rate {rate:.1%} < 50%"

    def test_disease_mapping_rate(self):
        """Check disease mapping rate is acceptable."""
        import pandas as pd

        mapping_path = BASE_DIR / "data" / "processed" / "indication_mapping.csv"
        df = pd.read_csv(mapping_path)

        mapped = df["disease_id"].notna().sum()
        total = len(df)
        rate = mapped / total if total > 0 else 0

        # Target: > 30%
        assert rate >= 0.3, f"Disease mapping rate {rate:.1%} < 30%"

    def test_candidates_generated(self):
        """Check repurposing candidates were generated."""
        import pandas as pd

        candidates_path = BASE_DIR / "data" / "processed" / "repurposing_candidates.csv"
        df = pd.read_csv(candidates_path)

        assert len(df) > 0, "No repurposing candidates generated"
