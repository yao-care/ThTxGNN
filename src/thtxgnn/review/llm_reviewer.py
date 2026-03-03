"""LLM-based reviewer for drug repurposing predictions.

This module provides AI-assisted review of drug repurposing candidates,
generating summaries and confidence assessments.
"""

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class ReviewResult:
    """Result of LLM review for a drug-disease prediction."""

    drug: str
    disease: str
    summary: str
    confidence: str  # "high", "medium", "low"
    key_evidence: list[str]
    limitations: list[str]
    recommendation: str
    raw_response: str | None = None


class LLMReviewer:
    """LLM-based reviewer for drug repurposing predictions.

    Supports multiple LLM providers:
    - OpenAI (gpt-4, gpt-3.5-turbo)
    - Anthropic (claude-3, claude-2)
    - Local (ollama)
    """

    SYSTEM_PROMPT = """You are a medical research assistant specializing in drug repurposing.
Your task is to evaluate drug repurposing predictions and provide evidence-based assessments.

For each drug-disease pair, analyze:
1. Mechanism of action relevance
2. Existing clinical evidence
3. Safety considerations
4. Practical feasibility

Provide responses in JSON format with these fields:
- summary: Brief overview (2-3 sentences)
- confidence: "high", "medium", or "low"
- key_evidence: List of supporting evidence points
- limitations: List of concerns or unknowns
- recommendation: Next steps for validation

IMPORTANT: This is for research purposes only. Always emphasize that clinical validation is required.
"""

    def __init__(
        self,
        provider: str = "openai",
        model: str | None = None,
        api_key: str | None = None,
    ):
        """Initialize the LLM reviewer.

        Args:
            provider: LLM provider ("openai", "anthropic", "ollama")
            model: Model name (defaults based on provider)
            api_key: API key (defaults to environment variable)
        """
        self.provider = provider
        self.api_key = api_key

        if model is None:
            if provider == "openai":
                self.model = "gpt-4-turbo-preview"
            elif provider == "anthropic":
                self.model = "claude-3-sonnet-20240229"
            elif provider == "ollama":
                self.model = "llama2"
            else:
                self.model = "gpt-3.5-turbo"
        else:
            self.model = model

    def _get_api_key(self) -> str:
        """Get API key from environment or instance."""
        if self.api_key:
            return self.api_key

        if self.provider == "openai":
            key = os.environ.get("OPENAI_API_KEY")
        elif self.provider == "anthropic":
            key = os.environ.get("ANTHROPIC_API_KEY")
        else:
            return ""

        if not key:
            raise ValueError(
                f"No API key found for {self.provider}. "
                f"Set {self.provider.upper()}_API_KEY environment variable."
            )
        return key

    def _call_openai(self, prompt: str) -> str:
        """Call OpenAI API."""
        try:
            from openai import OpenAI

            client = OpenAI(api_key=self._get_api_key())
            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                response_format={"type": "json_object"},
                temperature=0.3,
            )
            return response.choices[0].message.content or ""
        except ImportError:
            raise ImportError("openai package required. Install with: pip install openai")

    def _call_anthropic(self, prompt: str) -> str:
        """Call Anthropic API."""
        try:
            import anthropic

            client = anthropic.Anthropic(api_key=self._get_api_key())
            response = client.messages.create(
                model=self.model,
                max_tokens=2000,
                system=self.SYSTEM_PROMPT,
                messages=[{"role": "user", "content": prompt}],
            )
            return response.content[0].text
        except ImportError:
            raise ImportError(
                "anthropic package required. Install with: pip install anthropic"
            )

    def _call_ollama(self, prompt: str) -> str:
        """Call local Ollama API."""
        import requests

        url = os.environ.get("OLLAMA_URL", "http://localhost:11434")
        response = requests.post(
            f"{url}/api/generate",
            json={
                "model": self.model,
                "prompt": f"{self.SYSTEM_PROMPT}\n\n{prompt}",
                "stream": False,
                "format": "json",
            },
            timeout=120,
        )
        response.raise_for_status()
        return response.json().get("response", "")

    def _call_llm(self, prompt: str) -> str:
        """Call the configured LLM."""
        if self.provider == "openai":
            return self._call_openai(prompt)
        elif self.provider == "anthropic":
            return self._call_anthropic(prompt)
        elif self.provider == "ollama":
            return self._call_ollama(prompt)
        else:
            raise ValueError(f"Unknown provider: {self.provider}")

    def review_prediction(
        self,
        drug: str,
        disease: str,
        evidence: dict[str, Any] | None = None,
    ) -> ReviewResult:
        """Review a single drug-disease repurposing prediction.

        Args:
            drug: Drug name
            disease: Disease/indication name
            evidence: Optional evidence data (PubMed, trials, etc.)

        Returns:
            ReviewResult with AI-generated assessment
        """
        prompt = f"""Evaluate this drug repurposing candidate:

Drug: {drug}
Potential Indication: {disease}

"""
        if evidence:
            prompt += f"""Supporting Evidence:
{json.dumps(evidence, indent=2, ensure_ascii=False)}

"""

        prompt += """Based on your knowledge, provide an assessment in JSON format with:
- summary: Brief overview
- confidence: "high", "medium", or "low"
- key_evidence: Supporting points
- limitations: Concerns
- recommendation: Next steps

Remember: This is for research only. Clinical validation is required."""

        try:
            response = self._call_llm(prompt)
            data = json.loads(response)

            return ReviewResult(
                drug=drug,
                disease=disease,
                summary=data.get("summary", ""),
                confidence=data.get("confidence", "low"),
                key_evidence=data.get("key_evidence", []),
                limitations=data.get("limitations", []),
                recommendation=data.get("recommendation", ""),
                raw_response=response,
            )
        except json.JSONDecodeError:
            return ReviewResult(
                drug=drug,
                disease=disease,
                summary=response[:500] if response else "Failed to parse response",
                confidence="low",
                key_evidence=[],
                limitations=["Response parsing failed"],
                recommendation="Manual review required",
                raw_response=response,
            )
        except Exception as e:
            return ReviewResult(
                drug=drug,
                disease=disease,
                summary=f"Error: {str(e)}",
                confidence="low",
                key_evidence=[],
                limitations=[str(e)],
                recommendation="Review failed - check API configuration",
                raw_response=None,
            )

    def review_batch(
        self,
        predictions: list[dict],
        evidence_map: dict[str, dict] | None = None,
    ) -> list[ReviewResult]:
        """Review multiple predictions.

        Args:
            predictions: List of {"drug": str, "disease": str} dicts
            evidence_map: Optional map of "drug:disease" -> evidence

        Returns:
            List of ReviewResult objects
        """
        results = []
        for pred in predictions:
            drug = pred.get("drug", "")
            disease = pred.get("disease", "")
            key = f"{drug}:{disease}"
            evidence = evidence_map.get(key) if evidence_map else None

            result = self.review_prediction(drug, disease, evidence)
            results.append(result)

        return results

    def generate_report(
        self,
        results: list[ReviewResult],
        output_path: str | Path | None = None,
    ) -> str:
        """Generate a markdown report from review results.

        Args:
            results: List of ReviewResult objects
            output_path: Optional path to save report

        Returns:
            Markdown report content
        """
        report = """# Drug Repurposing Review Report

Generated by ThTxGNN LLM Reviewer

## Disclaimer

This report is for research purposes only and does not constitute medical advice.
All predictions require clinical validation before therapeutic application.

---

## Summary

| Drug | Indication | Confidence | Recommendation |
|------|------------|------------|----------------|
"""
        for r in results:
            report += f"| {r.drug} | {r.disease} | {r.confidence} | {r.recommendation[:50]}... |\n"

        report += "\n---\n\n## Detailed Reviews\n\n"

        for i, r in enumerate(results, 1):
            report += f"""### {i}. {r.drug} → {r.disease}

**Confidence:** {r.confidence.upper()}

**Summary:** {r.summary}

**Key Evidence:**
"""
            for ev in r.key_evidence:
                report += f"- {ev}\n"

            report += "\n**Limitations:**\n"
            for lim in r.limitations:
                report += f"- {lim}\n"

            report += f"\n**Recommendation:** {r.recommendation}\n\n---\n\n"

        if output_path:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(report)

        return report


def create_mock_reviewer() -> "MockLLMReviewer":
    """Create a mock reviewer for testing without API keys."""
    return MockLLMReviewer()


class MockLLMReviewer(LLMReviewer):
    """Mock LLM reviewer for testing without API calls."""

    def __init__(self):
        """Initialize mock reviewer."""
        self.provider = "mock"
        self.model = "mock-model"
        self.api_key = None

    def _call_llm(self, prompt: str) -> str:
        """Return mock response."""
        return json.dumps(
            {
                "summary": "This is a mock review for testing purposes.",
                "confidence": "medium",
                "key_evidence": [
                    "Mock evidence point 1",
                    "Mock evidence point 2",
                ],
                "limitations": [
                    "This is a mock review",
                    "No actual analysis performed",
                ],
                "recommendation": "Use real LLM provider for actual analysis",
            }
        )


if __name__ == "__main__":
    # Demo usage
    print("ThTxGNN LLM Reviewer Demo")
    print("=" * 50)

    # Create mock reviewer for demo
    reviewer = create_mock_reviewer()

    # Example predictions
    predictions = [
        {"drug": "Metformin", "disease": "Cancer prevention"},
        {"drug": "Aspirin", "disease": "Colorectal cancer"},
        {"drug": "Gabapentin", "disease": "Anxiety disorder"},
    ]

    print("\nReviewing predictions...")
    results = reviewer.review_batch(predictions)

    for r in results:
        print(f"\n{r.drug} → {r.disease}")
        print(f"  Confidence: {r.confidence}")
        print(f"  Summary: {r.summary}")

    # Generate report
    report = reviewer.generate_report(results)
    print("\n" + "=" * 50)
    print("Report generated successfully")
