---
layout: default
title: Home
nav_order: 1
---

# ThTxGNN - Thailand Drug Repurposing Predictions

Drug repurposing prediction system for Thailand using TxGNN knowledge graph.

## Overview

This project identifies potential new therapeutic uses for existing drugs approved in Thailand by leveraging the TxGNN (Therapeutic Target Graph Neural Network) knowledge graph.

## Quick Stats

| Metric | Value |
|--------|-------|
| Thai FDA Drugs (NLEM) | 155 |
| DrugBank Mapping Rate | 97.42% |
| Disease Mapping Rate | 83.63% |
| Repurposing Candidates | 1,115 |

## Features

- **Knowledge Graph Prediction**: Uses TxGNN to identify potential drug-disease relationships
- **FHIR R4 Compliant**: All predictions available as FHIR resources
- **SMART on FHIR**: EHR integration support
- **Evidence Collection**: Automatic literature and clinical trial search

## API Endpoints

| Resource | URL |
|----------|-----|
| FHIR Metadata | `/fhir/metadata` |
| MedicationKnowledge | `/fhir/MedicationKnowledge/{id}` |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/{id}` |

## Disclaimer

This project is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.

## Data Sources

- **Thai FDA**: Thailand Food and Drug Administration
- **TxGNN**: Knowledge graph for drug-disease relationships
- **DrugBank**: Drug information and mappings
- **ClinicalTrials.gov**: Clinical trial evidence
- **PubMed**: Literature evidence
