"""
Microinstallation Mapper Module

This module provides functionality to map and analyze microinstallations
(small renewable energy installations up to 50kW) based on URE registry data.
It includes tools for tracking prosumer adoption, analyzing distributed generation,
and mapping small-scale renewable energy deployment.
"""

from .mapper import MicroinstallationMapper
from .models import GridConnection, Microinstallation, ProsumerData
from .scrapers import MicroinstallationScraper
from .utils import analyze_grid_impact, calculate_prosumer_growth

__version__ = "0.0.2"

__all__ = [
    "MicroinstallationMapper",
    "Microinstallation",
    "ProsumerData",
    "GridConnection",
    "MicroinstallationScraper",
    "calculate_prosumer_growth",
    "analyze_grid_impact",
]
