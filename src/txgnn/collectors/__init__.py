"""Data collectors for evidence gathering."""

from .base import BaseCollector, CollectorResult
from .bundle import BundleAggregator, CandidateInfo, EvidenceBundle
from .clinicaltrials import ClinicalTrialsCollector
from .ddinter import DDInterCollector
from .drugbank import DrugBankCollector
from .ictrp import ICTRPCollector
from .known_relations import KnownRelationsChecker
from .pharmacology import PharmacologyCollector
from .pubmed import PubMedCollector
from .thaifda import ThaiFDACollector, TCTRCollector

__all__ = [
    "BaseCollector",
    "BundleAggregator",
    "CandidateInfo",
    "ClinicalTrialsCollector",
    "CollectorResult",
    "DDInterCollector",
    "DrugBankCollector",
    "EvidenceBundle",
    "ICTRPCollector",
    "KnownRelationsChecker",
    "PharmacologyCollector",
    "PubMedCollector",
    "TCTRCollector",
    "ThaiFDACollector",
]
