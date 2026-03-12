"""Test disease mapping module"""

import pytest
import pandas as pd

from thtxgnn.mapping.disease_mapper import (
    load_disease_vocab,
    build_disease_index,
    map_term_to_disease,
    get_indication_mapping_stats,
)


class TestLoadDiseaseVocab:
    """Test load_disease_vocab function"""

    def test_returns_dataframe(self):
        df = load_disease_vocab()
        assert isinstance(df, pd.DataFrame)

    def test_has_required_columns(self):
        df = load_disease_vocab()
        assert "disease_id" in df.columns
        assert "disease_name" in df.columns

    def test_has_diseases(self):
        df = load_disease_vocab()
        assert len(df) > 10000


class TestMapTermToDisease:
    """Test map_term_to_disease function"""

    @pytest.fixture
    def disease_index(self):
        df = load_disease_vocab()
        return build_disease_index(df)

    def test_maps_hypertension(self, disease_index):
        results = map_term_to_disease("hypertension", disease_index)
        assert len(results) > 0

    def test_maps_diabetes(self, disease_index):
        results = map_term_to_disease("diabetes", disease_index)
        assert len(results) > 0

    def test_no_match_returns_empty(self, disease_index):
        results = map_term_to_disease("nonexistent_disease_xyz", disease_index)
        assert results == []


class TestGetIndicationMappingStats:
    """Test get_indication_mapping_stats function"""

    def test_returns_dict(self):
        df = pd.DataFrame({
            "indication": ["hypertension", "diabetes", "unknown"],
            "disease_id": ["D001", "D002", None],
            "disease_name": ["hypertension", "diabetes", None],
        })
        stats = get_indication_mapping_stats(df)
        assert isinstance(stats, dict)
