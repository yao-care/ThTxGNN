---
layout: default
title: Data Sources
nav_order: 3
---

# Data Sources

## Primary Data Sources

### Thailand NLEM (National List of Essential Medicines)

- **Source**: Thai FDA / Ministry of Public Health
- **Coverage**: 98 essential medicines
- **Update Frequency**: Biennial
- **Language**: Thai and English
- **Reference**: [WHO Essential Medicines](https://list.essentialmeds.org/)

### TxGNN Knowledge Graph

- **Source**: Harvard Dataverse
- **Version**: 2024
- **Nodes**: ~50,000 (drugs, diseases, genes, pathways)
- **Edges**: ~4.6 million relationships
- **Reference**: [TxGNN Paper](https://www.nature.com/articles/s41591-023-02233-x)

### DrugBank

- **Source**: DrugBank 5.1.10
- **Coverage**: 7,958 approved drugs
- **Data**: Drug properties, targets, interactions
- **Reference**: [DrugBank](https://www.drugbank.com/)

## Evidence Sources

### PubMed

- **API**: NCBI E-utilities
- **Coverage**: 35+ million citations
- **Search Strategy**: Drug name + disease + Thailand affiliation
- **Rate Limit**: 3 requests/second (with API key: 10/second)

### ClinicalTrials.gov

- **API**: ClinicalTrials.gov API v2
- **Coverage**: 500,000+ registered trials
- **Search Strategy**: Drug name + condition + Thailand location
- **Reference**: [ClinicalTrials.gov](https://clinicaltrials.gov/)

### Thai Clinical Trial Registry (TCTR)

- **Source**: thaiclinicaltrials.org
- **Coverage**: Thailand-registered clinical trials
- **Integration**: Part of WHO ICTRP
- **Reference**: [TCTR](https://www.thaiclinicaltrials.org/)

### Thai FDA (NDI)

- **Source**: ndi.fda.moph.go.th
- **Coverage**: Registered drugs in Thailand
- **Data**: Registration status, approvals

## Data Quality

| Source | Mapping Rate | Coverage |
|--------|-------------|----------|
| DrugBank | 96.94% | 95/98 drugs |
| Disease Ontology | 92.74% | Most indications |
| PubMed | Variable | Depends on drug |
| ClinicalTrials.gov | Variable | Depends on drug |

## Data Updates

- Knowledge graph: Quarterly review
- Drug mappings: On NLEM updates
- Evidence: On-demand collection

## Disclaimer

All data sources are used for research purposes only. Medical decisions should not be based solely on this data.
