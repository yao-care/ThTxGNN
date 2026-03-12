"""Test ingredient normalization module"""

import pytest

from thtxgnn.mapping.normalizer import (
    normalize_ingredient,
    extract_ingredients,
    extract_primary_ingredient,
    get_all_synonyms,
)


class TestNormalizeIngredient:
    """Test normalize_ingredient function"""

    def test_simple_name(self):
        assert normalize_ingredient("METRONIDAZOLE") == "METRONIDAZOLE"

    def test_removes_eq_to_synonym(self):
        result = normalize_ingredient("SODIUM BICARBONATE ( EQ TO SODIUM HYDROGEN CARBONATE)")
        assert result == "SODIUM BICARBONATE"

    def test_uppercase(self):
        assert normalize_ingredient("metronidazole") == "METRONIDAZOLE"

    def test_removes_extra_spaces(self):
        result = normalize_ingredient("SODIUM   BICARBONATE")
        assert result == "SODIUM BICARBONATE"

    def test_empty_string(self):
        assert normalize_ingredient("") == ""
        assert normalize_ingredient(None) == ""


class TestExtractIngredients:
    """Test extract_ingredients function"""

    def test_single_ingredient(self):
        result = extract_ingredients("METRONIDAZOLE")
        assert result == ["METRONIDAZOLE"]

    def test_multiple_ingredients(self):
        result = extract_ingredients("VITAMIN A;VITAMIN C;VITAMIN E")
        assert result == ["VITAMIN A", "VITAMIN C", "VITAMIN E"]

    def test_removes_duplicates(self):
        result = extract_ingredients("SUCROSE;;SUCROSE;;SUCROSE")
        assert result == ["SUCROSE"]


class TestExtractPrimaryIngredient:
    """Test extract_primary_ingredient function"""

    def test_returns_first(self):
        result = extract_primary_ingredient("VITAMIN A;;VITAMIN C")
        assert result == "VITAMIN A"

    def test_empty_returns_empty(self):
        assert extract_primary_ingredient("") == ""


class TestGetAllSynonyms:
    """Test get_all_synonyms function"""

    def test_no_synonyms(self):
        result = get_all_synonyms("METRONIDAZOLE")
        assert len(result) == 1
        assert result[0][0] == "METRONIDAZOLE"
