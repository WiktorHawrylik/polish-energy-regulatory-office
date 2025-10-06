"""
Tariff Oracle Module

This module provides functionality to analyze and predict energy tariffs
based on URE data and market conditions. It includes tools for tariff
comparison, cost optimization, and tariff change predictions.
"""

from .models import CostAnalysis, TariffHistory, TariffPrediction
from .oracle import TariffOracle
from .scrapers import TariffDataScraper
from .utils import calculate_savings, optimize_tariff_selection

__all__ = [
    "TariffOracle",
    "TariffPrediction",
    "CostAnalysis",
    "TariffHistory",
    "TariffDataScraper",
    "optimize_tariff_selection",
    "calculate_savings",
]
