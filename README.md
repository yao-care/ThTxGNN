# ThTxGNN - Thailand Drug Repurposing Predictions

Thailand drug repurposing prediction system using TxGNN knowledge graph.

## Project Status (2026-03-03)

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 0 | Project initialization | ✅ Complete |
| Phase 1 | Thai FDA data integration | ✅ Complete |
| Phase 2 | Disease mapping (DISEASE_DICT) | ✅ Complete |
| Phase 3 | KG prediction | ✅ Complete (1,115 candidates) |
| Phase 4 | Website & FHIR | ✅ Complete |
| Phase 5 | Evidence collection | ✅ Complete |
| Phase 6 | News monitoring | ✅ Complete |
| Phase 7 | Validation & deployment | ✅ Complete |
| DL Prediction | TxGNN deep learning model | ⏳ Optional (in progress) |

### Quality Metrics

- **Drug mapping rate**: 151/155 drugs mapped to DrugBank (97.4%)
- **Repurposing candidates**: 1,115 (KG method)
- **Tests**: 16/16 passed

## Overview

This project identifies potential new therapeutic uses for existing drugs approved in Thailand by leveraging the TxGNN (Therapeutic Target Graph Neural Network) knowledge graph.

## Installation

```bash
uv sync
```

## Usage

### Knowledge Graph Prediction (Main Pipeline)

```bash
# Process Thai FDA data
uv run python scripts/process_fda_data.py

# Prepare vocabulary data
uv run python scripts/prepare_external_data.py

# Run KG predictions
uv run python scripts/run_kg_prediction.py

# Generate FHIR resources
uv run python scripts/generate_fhir_resources.py
```

### Deep Learning Prediction (Optional)

Requires separate conda environment with PyTorch and DGL:

```bash
# Setup conda environment (first time only)
conda create -n txgnn python=3.11 -y
conda activate txgnn
pip install torch==2.2.2 torchvision==0.17.2
pip install dgl==1.1.3
pip install git+https://github.com/mims-harvard/TxGNN.git
pip install pandas tqdm pyyaml pydantic ogb

# Run DL prediction
conda activate txgnn
python scripts/run_txgnn_prediction.py

# Resume from checkpoint (if interrupted)
python scripts/run_txgnn_prediction.py

# Restart from scratch
python scripts/run_txgnn_prediction.py --restart
```

**Required files for DL prediction:**
- `model_ckpt/` - TxGNN pretrained model (symlink to TwTxGNN)
- `data/edges.csv` - Edge data (symlink to TwTxGNN)

## Project Structure

```
ThTxGNN/
├── config/
│   └── fields.yaml          # Thai FDA field mapping
├── data/
│   ├── external/             # TxGNN vocabulary data
│   ├── processed/            # Prediction results
│   ├── raw/                  # Thai FDA raw data
│   └── news/                 # News monitoring keywords
├── docs/                     # Jekyll website
│   ├── fhir/                 # FHIR resources
│   └── smart/                # SMART on FHIR app
├── scripts/
│   ├── fetch_thaifda_drugs.py
│   ├── process_fda_data.py
│   ├── prepare_external_data.py
│   ├── run_kg_prediction.py
│   ├── run_txgnn_prediction.py  # DL prediction
│   └── generate_fhir_resources.py
├── src/thtxgnn/              # Main package
│   ├── collectors/           # Evidence collectors
│   ├── data/                 # Data loaders
│   ├── mapping/              # Drug/disease mapping
│   ├── predict/              # Prediction modules
│   └── review/               # LLM review
└── tests/
```

## Data Sources

- **Thai FDA**: Drug registration data from Thailand Food and Drug Administration
- **TxGNN**: Knowledge graph for drug-disease relationships
- **DrugBank**: Drug information and mappings
- **ClinicalTrials.gov**: Clinical trial evidence
- **PubMed**: Literature evidence
- **TCTR**: Thai Clinical Trials Registry (via ICTRP)

## Output Files

| File | Description |
|------|-------------|
| `data/processed/drug_mapping.csv` | Drug to DrugBank ID mapping |
| `data/processed/indication_mapping.csv` | Indication to disease mapping |
| `data/processed/repurposing_candidates.csv` | KG prediction results |
| `data/processed/txgnn_dl_predictions.csv` | DL prediction results (optional) |
| `docs/fhir/MedicationKnowledge/` | FHIR drug resources |
| `docs/fhir/ClinicalUseDefinition/` | FHIR indication resources |

## Disclaimer

This project is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.

## License

MIT License
