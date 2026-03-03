---
layout: default
title: About
nav_order: 5
---

# About ThTxGNN

## Project Overview

ThTxGNN (Thailand Therapeutic Graph Neural Network) is an open-source drug repurposing prediction system adapted for Thailand's healthcare context.

## Objectives

1. **Identify Repurposing Candidates**: Discover potential new therapeutic uses for drugs approved in Thailand
2. **FHIR Integration**: Provide predictions in HL7 FHIR R4 format for healthcare system integration
3. **Evidence Aggregation**: Collect supporting evidence from clinical trials and literature
4. **Local Context**: Focus on drugs available in Thailand's National List of Essential Medicines (NLEM)

## Key Features

### Knowledge Graph Prediction
- Uses TxGNN knowledge graph with 50,000+ biomedical entities
- Maps Thai FDA drugs to international drug databases
- Predicts drug-disease relationships based on graph structure

### FHIR R4 Compliance
- All predictions available as FHIR resources
- MedicationKnowledge and ClinicalUseDefinition resources
- SMART on FHIR support for EHR integration

### Multi-Source Evidence
- PubMed literature search
- ClinicalTrials.gov integration
- Thai Clinical Trial Registry (TCTR)
- Thai FDA registration data

### Thai Language Support
- Thai disease term mappings
- Thai drug name normalization
- Bilingual documentation

## Technology Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.11+ |
| Package Manager | uv |
| Web Framework | Jekyll |
| Data Format | FHIR R4 JSON |
| Hosting | GitHub Pages |

## Related Projects

- **TxGNN**: Original knowledge graph neural network ([Paper](https://www.nature.com/articles/s41591-023-02233-x))
- **ThTxGNN**: Thailand implementation (reference implementation)

## License

This project is open-source and available for research purposes.

## Contact

- GitHub: [ThTxGNN Repository](https://github.com/thtxgnn)
- Issues: Report issues on GitHub

## Disclaimer

ThTxGNN is a research tool and does not provide medical advice. All drug repurposing candidates identified through this system are computational predictions that require rigorous clinical validation before any therapeutic application. Healthcare decisions should be made in consultation with qualified medical professionals.

## Acknowledgments

- TxGNN research team at Harvard
- Thai FDA for drug registration data
- DrugBank for drug information
- NCBI for PubMed access
