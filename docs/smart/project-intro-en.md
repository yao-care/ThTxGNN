---
layout: default
title: Project Introduction (English)
parent: SMART on FHIR
nav_order: 10
---

# ThTxGNN: AI-Powered Drug Repurposing for Thailand NHI Drugs

## Executive Summary

**ThTxGNN** is an open-source drug repurposing platform that leverages Harvard's TxGNN deep learning model to predict potential new indications for Thailand National Health Insurance (NHI) approved drugs. Unlike prediction-only tools, ThTxGNN provides a complete evidence validation pipeline, integrating clinical trials, literature, and safety data to generate actionable reports.

---

## Key Differentiators

| Feature | Description |
|---------|-------------|
| **Evidence-Based Predictions** | Every prediction is validated against ClinicalTrials.gov, PubMed, and other authoritative sources |
| **Five-Level Evidence Classification** | L1 (multiple Phase 3 RCTs) to L5 (AI prediction only) |
| **SMART on FHIR Integration** | Ready-to-use app for EHR integration |
| **FHIR R4 API** | Static FHIR resources for external system integration |
| **Comprehensive Safety Data** | 222,391 DDI records, 8,359 DDSI records |

---

## Data Overview

| Metric | Count |
|--------|-------|
| Drug Reports | 191 |
| Drug Repurposing Candidates | 142,328 |
| Predicted Indications | 1,268 |
| Drug-Drug Interactions (DDI) | 222,391 |
| Drug-Disease Contraindications (DDSI) | 8,359 |

### Evidence Distribution

| Level | Definition | Drug Count |
|-------|------------|------------|
| L1 | Multiple Phase 3 RCTs | 6 |
| L2 | Single RCT or Phase 2 trials | 12 |
| L3 | Observational studies | 16 |
| L4 | Preclinical / mechanistic | 19 |
| L5 | AI prediction only | 138 |

---

## Technology Stack

### Prediction Model

- **TxGNN**: Published in *Nature Medicine* (2023) by Harvard Zitnik Lab
- **Method**: Knowledge graph + deep learning for drug-disease relationship prediction
- **Source**: [TxGNN Paper](https://www.nature.com/articles/s41591-023-02233-x)

### Evidence Sources

| Source | Data Type |
|--------|-----------|
| ClinicalTrials.gov | Clinical trial data (NCT IDs) |
| PubMed | Biomedical literature (PMIDs) |
| DrugBank | Drug properties and interactions |
| TFDA | Thailand FDA approval status |
| DDInter 2.0 | Drug-drug interactions |
| Disease Ontology | Disease classification (DOIDs) |

### Technical Implementation

- **Frontend**: Static site (Jekyll) + JavaScript
- **FHIR Version**: R4 (4.0.1)
- **Data Format**: JSON, CSV
- **Hosting**: GitHub Pages
- **Open Source**: [GitHub Repository](https://github.com/yao-care/ThTxGNN)

---

## SMART on FHIR Integration

ThTxGNN provides a fully functional SMART on FHIR application that can be integrated into any FHIR R4-compliant EHR system.

### Capabilities

1. **Patient Medication Retrieval**: Reads MedicationRequest/MedicationStatement from EHR
2. **Drug Mapping**: Maps RxNorm codes to ThTxGNN database via RxNorm API
3. **Repurposing Lookup**: Displays predicted new indications for each medication
4. **Evidence Display**: Shows evidence level and supporting references

### Technical Specifications

| Item | Value |
|------|-------|
| FHIR Version | R4 |
| OAuth | OAuth 2.0 with PKCE |
| Scopes | `launch`, `patient/MedicationRequest.read`, `patient/MedicationStatement.read`, `openid`, `fhirUser` |
| Launch URI | `https://thtxgnn.yao.care/smart/launch.html` |
| Standalone URI | `https://thtxgnn.yao.care/smart/standalone.html` |

### FHIR API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/fhir/metadata` | CapabilityStatement |
| `/fhir/MedicationKnowledge/{drug-slug}.json` | Drug resource (189 drugs) |
| `/fhir/ClinicalUseDefinition/{drug-indication}.json` | Prediction resource (1,268 predictions) |
| `/fhir/Bundle/all-predictions.json` | Complete dataset |

---

## Collaboration Opportunities

We are seeking collaboration with:

### 1. EHR Vendors & Healthcare Institutions

- Pilot deployment of SMART App
- Integration with clinical decision support workflows
- Feedback for usability improvements

### 2. Clinical Trial Platforms

- Enrichment of clinical trial data with AI predictions
- Patient cohort identification

### 3. Drug-Drug Interaction Systems

- Integration of ThTxGNN predictions as supplementary data layer
- Combined DDI + repurposing alerts

### 4. Disease-Specific Research Teams

- Custom analysis for specific therapeutic areas
- Collaboration on validation studies

---

## Disease Coverage

ThTxGNN covers predictions across multiple therapeutic areas:

| Therapeutic Area | Example Indications |
|------------------|---------------------|
| Oncology | Breast carcinoma, colorectal cancer, lung cancer |
| Neurology | Epilepsy, migraine, Parkinson's disease |
| Cardiology | Hypertension, heart failure, arrhythmia |
| Infectious Disease | Viral infections, bacterial infections |
| Autoimmune | Rheumatoid arthritis, lupus, psoriasis |
| Metabolic | Diabetes, obesity, dyslipidemia |
| Rare Diseases | Various orphan diseases |

---

## How to Get Started

### For Developers

```bash
# Clone the repository
git clone https://github.com/yao-care/ThTxGNN.git

# Install dependencies
uv sync

# Run knowledge graph prediction
uv run python scripts/run_kg_prediction.py
```

### For Healthcare Institutions

1. **Test the SMART App**: Use [SMART Launcher](https://launch.smarthealthit.org/) with our launch URL
2. **Explore the Data**: Visit [thtxgnn.yao.care](https://thtxgnn.yao.care/) to browse drug reports
3. **Contact Us**: Reach out for integration discussions

### For Researchers

- **Download Data**: [CSV/JSON exports available](https://thtxgnn.yao.care/downloads/)
- **API Access**: Use FHIR endpoints for programmatic access
- **Cite Us**: Reference our methodology page

---

## Contact Information

- **Website**: [https://thtxgnn.yao.care/](https://thtxgnn.yao.care/)
- **GitHub**: [https://github.com/yao-care/ThTxGNN](https://github.com/yao-care/ThTxGNN)
- **Issues**: [GitHub Issues](https://github.com/yao-care/ThTxGNN/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yao-care/ThTxGNN/discussions)

---

## Disclaimer

This platform is intended for **research purposes only** and does not constitute medical advice. All drug repurposing predictions require clinical validation before application. Healthcare decisions should be made in consultation with qualified medical professionals.

---

*Last updated: 2026-03-01*
