---
layout: default
title: วิธีการคาดการณ์
parent: คำอธิบาย
nav_order: 1
---

# วิธีการคาดการณ์

## Knowledge Graph Prediction

ThTxGNN uses the TxGNN (Therapeutic Target Graph Neural Network) knowledge graph to predict potential drug-disease relationships.

### TxGNN Knowledge Graph

The TxGNN knowledge graph contains:
- **17,081 diseases** mapped to DOID (Disease Ontology)
- **7,958 drugs** mapped to DrugBank
- **80,127 drug-disease relationships** including indications and contraindications

### Prediction Process

1. **Drug Mapping**: Thai FDA-approved drugs are mapped to DrugBank IDs using:
   - Generic name matching
   - Brand name normalization
   - Active ingredient extraction

2. **Disease Mapping**: Thai indications are mapped to English disease terms using:
   - Direct translation
   - Medical terminology lookup
   - DISEASE_DICT mapping table

3. **KG Query**: For each mapped drug, query the knowledge graph for:
   - Known indications (existing approvals)
   - Potential new indications (repurposing candidates)

4. **Evidence Collection**: For promising candidates, collect supporting evidence from:
   - PubMed literature
   - ClinicalTrials.gov
   - Thai Clinical Trial Registry (TCTR)

### Scoring

Predictions include confidence scores based on:
- Graph structure (node connectivity)
- Relationship strength in knowledge graph
- Supporting evidence count

## Limitations

- Predictions are computational hypotheses requiring clinical validation
- Knowledge graph data may not include recent drug approvals
- Thai-specific drug formulations may not have DrugBank mappings
- Disease terminology translation may lose clinical nuance

## Disclaimer

This methodology is for research purposes only. Drug repurposing candidates identified through this system require rigorous clinical validation before any therapeutic application.
