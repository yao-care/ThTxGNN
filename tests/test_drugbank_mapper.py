"""Test DrugBank mapping module"""

import pytest
import pandas as pd

from thtxgnn.mapping.drugbank_mapper import (
    load_drugbank_vocab,
    build_name_index,
    map_ingredient_to_drugbank,
    get_mapping_stats,
)


class TestLoadDrugbankVocab:
    """Test load_drugbank_vocab function"""

    def test_returns_dataframe(self):
        df = load_drugbank_vocab()
        assert isinstance(df, pd.DataFrame)

    def test_has_required_columns(self):
        df = load_drugbank_vocab()
        assert "drugbank_id" in df.columns
        assert "drug_name" in df.columns

    def test_has_drugs(self):
        df = load_drugbank_vocab()
        assert len(df) > 7000


class TestBuildNameIndex:
    """Test build_name_index function"""

    def test_returns_dict(self):
        df = load_drugbank_vocab()
        index = build_name_index(df)
        assert isinstance(index, dict)


class TestMapIngredientToDrugbank:
    """Test map_ingredient_to_drugbank function"""

    @pytest.fixture
    def name_index(self):
        df = load_drugbank_vocab()
        return build_name_index(df)

    def test_exact_match(self, name_index):
        result = map_ingredient_to_drugbank("METFORMIN", name_index)
        assert result is not None
        assert result.startswith("DB")

    def test_unmappable_returns_none(self, name_index):
        result = map_ingredient_to_drugbank("SOME_FAKE_DRUG_12345", name_index)
        assert result is None


class TestGetMappingStats:
    """Test get_mapping_stats function"""

    def test_returns_dict(self):
        df = pd.DataFrame({
            "ingredient": ["A", "B", "C"],
            "drugbank_id": ["DB001", None, "DB002"],
            "mapped": [True, False, True],
        })
        stats = get_mapping_stats(df)
        assert isinstance(stats, dict)
