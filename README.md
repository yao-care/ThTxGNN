# ThTxGNN - Thailand Drug Repurposing Predictions

Thailand drug repurposing prediction system using TxGNN knowledge graph.

## Overview

This project identifies potential new therapeutic uses for existing drugs approved in Thailand by leveraging the TxGNN (Therapeutic Target Graph Neural Network) knowledge graph.

## Installation

```bash
uv sync
```

## Usage

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

## Data Sources

- **Thai FDA**: Drug registration data from Thailand Food and Drug Administration
- **TxGNN**: Knowledge graph for drug-disease relationships
- **DrugBank**: Drug information and mappings
- **ClinicalTrials.gov**: Clinical trial evidence
- **PubMed**: Literature evidence

## Disclaimer

This project is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.

## License

MIT License
