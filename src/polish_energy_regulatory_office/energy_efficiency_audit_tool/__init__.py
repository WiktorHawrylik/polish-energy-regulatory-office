"""
Energy Efficiency Audit Tool Module

This module provides functionality to analyze energy efficiency data and
perform audits based on URE regulations and standards. It includes tools
for calculating efficiency metrics, generating audit reports, and tracking
efficiency improvements over time.
"""

from .auditor import EnergyEfficiencyAuditor
from .models import AuditReport, BuildingData, EfficiencyMetrics
from .scrapers import EfficiencyDataScraper
from .utils import calculate_efficiency_score, generate_recommendations

__version__ = "0.1.0"

__all__ = [
    "EnergyEfficiencyAuditor",
    "AuditReport",
    "EfficiencyMetrics",
    "BuildingData",
    "EfficiencyDataScraper",
    "calculate_efficiency_score",
    "generate_recommendations",
]
