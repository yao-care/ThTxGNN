---
layout: default
title: Drug Predictions
nav_order: 6
---

# Drug Repurposing Predictions

## Overview

ThTxGNN has analyzed 98 drugs from Thailand's National List of Essential Medicines (NLEM) and identified 939 potential repurposing candidates.

## Summary by Drug Category

| Category | Drugs | Predictions |
|----------|-------|-------------|
| Cardiovascular | 25 | ~280 |
| Diabetes/Metabolic | 12 | ~130 |
| Pain/Anti-inflammatory | 15 | ~160 |
| Antibiotics | 18 | ~150 |
| Respiratory | 8 | ~70 |
| CNS/Neurological | 10 | ~80 |
| Others | 10 | ~70 |

## Top Drugs by Prediction Count

| Drug | DrugBank ID | Predictions | Top Indication |
|------|-------------|-------------|----------------|
| Amlodipine | DB00381 | 6 | Prinzmetal angina |
| Metformin | DB00331 | 8 | Metabolic syndrome |
| Losartan | DB00678 | 5 | Heart failure |
| Atorvastatin | DB01076 | 7 | Cardiovascular disease |
| Omeprazole | DB00338 | 5 | Barrett esophagus |

## Search Predictions

Use the FHIR API to search for specific drugs:

```bash
# Get all predictions for Amlodipine
curl https://thtxgnn.github.io/fhir/ClinicalUseDefinition?subject=MedicationKnowledge/DB00381
```

## Evidence Status

| Status | Count | Description |
|--------|-------|-------------|
| Strong Evidence | ~50 | Clinical trials ongoing/completed |
| Moderate Evidence | ~200 | Literature support |
| Computational Only | ~689 | KG prediction only |

## Drug Categories

### Cardiovascular Drugs

- Amlodipine, Atenolol, Bisoprolol, Captopril, Carvedilol
- Digoxin, Diltiazem, Enalapril, Furosemide, Hydrochlorothiazide
- Isosorbide, Lisinopril, Losartan, Metoprolol, Nifedipine
- Propranolol, Ramipril, Simvastatin, Spironolactone, Valsartan
- Verapamil, Warfarin, Aspirin, Clopidogrel, Atorvastatin

### Diabetes/Metabolic Drugs

- Metformin, Glibenclamide, Gliclazide, Glimepiride, Insulin
- Pioglitazone, Sitagliptin, Empagliflozin, Dapagliflozin

### Antibiotics

- Amoxicillin, Ampicillin, Azithromycin, Ceftriaxone, Ciprofloxacin
- Clindamycin, Doxycycline, Erythromycin, Gentamicin, Metronidazole
- Penicillin, Tetracycline, Co-trimoxazole

### Pain/Anti-inflammatory

- Paracetamol, Ibuprofen, Diclofenac, Naproxen, Celecoxib
- Morphine, Tramadol, Codeine, Meloxicam

### Respiratory

- Salbutamol, Budesonide, Ipratropium, Theophylline
- Montelukast, Fluticasone

### CNS/Neurological

- Carbamazepine, Phenytoin, Valproic acid, Levetiracetam
- Diazepam, Lorazepam, Haloperidol, Risperidone
- Amitriptyline, Fluoxetine

## Disclaimer

All predictions are computational hypotheses. Drug repurposing candidates require clinical validation before therapeutic application.
