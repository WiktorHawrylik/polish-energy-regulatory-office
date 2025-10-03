"""
Data models for renewable energy sources mapping.
"""

from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Any, Dict, Optional


class InstallationType(Enum):
    """Types of renewable energy installations."""

    SOLAR_PV = "solar_pv"
    WIND = "wind"
    BIOGAS = "biogas"
    BIOMASS = "biomass"
    HYDRO = "hydro"
    OTHER = "other"


@dataclass
class RenewableInstallation:
    """Represents a renewable energy installation."""

    installation_id: str
    name: str
    installation_type: InstallationType
    capacity_kw: float
    commissioning_date: date
    voivodeship: str
    municipality: str
    operator: str
    technology: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    status: str = "active"

    def __post_init__(self) -> None:
        """Validate data after initialization."""
        if self.capacity_kw < 0:
            raise ValueError("Capacity cannot be negative")
        if not self.installation_id:
            raise ValueError("Installation ID is required")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RenewableInstallation":
        """Create RenewableInstallation from dictionary data."""
        return cls(
            installation_id=data["installation_id"],
            name=data["name"],
            installation_type=InstallationType(data["installation_type"]),
            capacity_kw=float(data["capacity_kw"]),
            commissioning_date=data["commissioning_date"],
            voivodeship=data["voivodeship"],
            municipality=data["municipality"],
            operator=data["operator"],
            technology=data.get("technology"),
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
            status=data.get("status", "active"),
        )


@dataclass
class RegionalData:
    """Regional statistics for renewable energy installations."""

    voivodeship: str
    total_capacity_kw: float
    installation_count: int
    type_distribution: Dict[str, int]
    average_installation_size: Optional[float] = None
    capacity_density_per_km2: Optional[float] = None

    def __post_init__(self) -> None:
        """Calculate derived metrics."""
        if self.installation_count > 0:
            self.average_installation_size = (
                self.total_capacity_kw / self.installation_count
            )


@dataclass
class CapacityGrowthAnalysis:
    """Results of capacity growth analysis."""

    period_start: date
    period_end: date
    total_capacity_added_kw: float
    installations_added: int
    growth_rate_percent: float
    dominant_technology: InstallationType
    regional_breakdown: Dict[str, float]

    def get_monthly_growth_rate(self) -> float:
        """Calculate monthly growth rate."""
        days = (self.period_end - self.period_start).days
        months = days / 30.44  # Average days per month
        if months > 0:
            return self.growth_rate_percent / months
        return 0.0


@dataclass
class GeospatialPoint:
    """Represents a point on the map with installation data."""

    latitude: float
    longitude: float
    installation_id: str
    capacity_kw: float
    installation_type: InstallationType
    name: str
    municipality: str
    voivodeship: str
