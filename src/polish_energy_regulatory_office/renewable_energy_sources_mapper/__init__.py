"""
Renewable Energy Sources Mapper Module

This module provides functionality to map and analyze renewable energy sources
in Poland based on URE registry data. It includes tools for visualizing
renewable installations, tracking capacity growth, and analyzing regional
distribution.
"""

from .mapper import RenewableEnergyMapper
from .models import InstallationType, RegionalData, RenewableInstallation
from .scrapers import RESRegistryScraper
from .utils import calculate_capacity_growth, generate_geospatial_data

__all__ = [
    "RenewableEnergyMapper",
    "RenewableInstallation",
    "InstallationType",
    "RegionalData",
    "RESRegistryScraper",
    "calculate_capacity_growth",
    "generate_geospatial_data",
]
