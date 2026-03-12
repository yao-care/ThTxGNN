"""Test repurposing prediction module"""

import pytest
import pandas as pd
from pathlib import Path

from thtxgnn.predict.repurposing import (
    load_drug_disease_relations,
    find_repurposing_candidates,
)


class TestLoadDrugDiseaseRelations:
    """Test load_drug_disease_relations function"""

    def test_returns_dataframe(self):
        relations_path = Path("data/external/drug_disease_relations.csv")
        if relations_path.exists():
            df = load_drug_disease_relations()
            assert isinstance(df, pd.DataFrame)
        else:
            pytest.skip("drug_disease_relations.csv not found")


class TestFindRepurposingCandidates:
    """Test find_repurposing_candidates function"""

    def test_returns_dataframe(self):
        relations_path = Path("data/external/drug_disease_relations.csv")
        mapping_path = Path("data/processed/drug_mapping.csv")

        if relations_path.exists() and mapping_path.exists():
            drug_mapping = pd.read_csv(mapping_path)
            candidates = find_repurposing_candidates(drug_mapping)
            assert isinstance(candidates, pd.DataFrame)
        else:
            pytest.skip("Required data files not found")
