"""
Polish Energy Regulatory Office Library

A comprehensive library for creating insights from publicly available data
on the Polish Energy Regulatory Office (Urząd Regulacji Energetyki) websites.
"""

__version__ = "0.1.0"
__author__ = "Wiktor Hawrylik"
__email__ = "wiktor.hawrylik@gmail.com"

# Import main modules for easy access
from . import (
    energy_efficiency_audit_tool,
    energy_price_analyzer,
    microinstallation_mapper,
    renewable_auctions_monitor,
    renewable_energy_sources_mapper,
    tariff_oracle,
)

__all__ = [
    "energy_price_analyzer",
    "renewable_energy_sources_mapper",
    "microinstallation_mapper",
    "energy_efficiency_audit_tool",
    "tariff_oracle",
    "renewable_auctions_monitor",
]
