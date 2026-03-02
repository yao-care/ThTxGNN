---
layout: default
title: API Reference
nav_order: 4
---

# API Reference

ThTxGNN provides FHIR R4 compliant APIs for drug repurposing predictions.

## FHIR Endpoints

### Capability Statement

```
GET /fhir/metadata
```

Returns the server's CapabilityStatement describing supported resources and operations.

### MedicationKnowledge

```
GET /fhir/MedicationKnowledge/{id}
```

Returns drug information including:
- Drug code (DrugBank ID)
- Drug name
- Regulatory status
- Known indications

**Example Response:**
```json
{
  "resourceType": "MedicationKnowledge",
  "id": "DB00381",
  "code": {
    "coding": [{
      "system": "https://www.drugbank.ca",
      "code": "DB00381",
      "display": "Amlodipine"
    }]
  },
  "status": "active"
}
```

### ClinicalUseDefinition

```
GET /fhir/ClinicalUseDefinition/{id}
```

Returns potential therapeutic use predictions including:
- Drug reference
- Indication reference
- Evidence sources
- Confidence score

**Example Response:**
```json
{
  "resourceType": "ClinicalUseDefinition",
  "id": "pred-DB00381-prinzmetal-angina",
  "type": "indication",
  "subject": [{
    "reference": "MedicationKnowledge/DB00381"
  }],
  "indication": {
    "diseaseSymptomProcedure": {
      "coding": [{
        "system": "http://purl.obolibrary.org/obo/DOID",
        "display": "Prinzmetal angina"
      }]
    }
  }
}
```

## Search Parameters

### MedicationKnowledge Search

| Parameter | Type | Description |
|-----------|------|-------------|
| code | token | DrugBank ID |
| status | token | active, inactive |

### ClinicalUseDefinition Search

| Parameter | Type | Description |
|-----------|------|-------------|
| subject | reference | MedicationKnowledge reference |
| type | token | indication, contraindication |

## SMART on FHIR

ThTxGNN supports SMART on FHIR launch for EHR integration.

### Launch URL

```
/smart/launch.html
```

### Supported Scopes

- `launch`
- `patient/MedicationKnowledge.read`
- `patient/ClinicalUseDefinition.read`

## Rate Limits

- No authentication required for read operations
- Rate limit: 100 requests per minute
- Response format: JSON only

## Status Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 404 | Resource not found |
| 429 | Rate limit exceeded |
| 500 | Server error |

## Disclaimer

This API is for research purposes only. Drug repurposing predictions require clinical validation before therapeutic application.
