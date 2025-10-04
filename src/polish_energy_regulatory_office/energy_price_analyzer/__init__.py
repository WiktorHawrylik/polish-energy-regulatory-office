"""
Energy Price Analyzer Module

This module provides functionality to analyze energy prices from URE data sources.
It includes tools for tracking price trends, comparing tariffs, and generating
price forecasts based on historical data.
"""

from .analyzer import EnergyPriceAnalyzer
from .models import PriceAnalysis, PriceData, TariffStructure
from .scrapers import UREPriceScraper
from .utils import format_currency

__version__ = "0.1.0"

__all__ = [
    "EnergyPriceAnalyzer",
    "PriceData",
    "TariffStructure",
    "PriceAnalysis",
    "UREPriceScraper",
    "format_currency",
]
