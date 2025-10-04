"""Data models for energy price analysis."""

from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from typing import Any, Dict, Optional


@dataclass
class PriceData:
    """Represents energy price data for a specific date and type."""

    date: date
    price: Decimal
    energy_type: str
    unit: str = "PLN/MWh"
    source: Optional[str] = None

    def __post_init__(self) -> None:
        """Validate data after initialization."""
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        if not self.energy_type:
            raise ValueError("Energy type is required")


@dataclass
class TariffStructure:
    """Represents a tariff structure with various pricing components."""

    tariff_id: str
    name: str
    base_price: Decimal
    energy_price: Decimal
    network_fee: Decimal
    valid_from: date
    valid_to: Optional[date] = None
    currency: str = "PLN"
    energy_type: str = "electricity"

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TariffStructure":
        """Create TariffStructure from dictionary data."""
        return cls(
            tariff_id=data["tariff_id"],
            name=data["name"],
            base_price=Decimal(str(data["base_price"])),
            energy_price=Decimal(str(data["energy_price"])),
            network_fee=Decimal(str(data["network_fee"])),
            valid_from=data["valid_from"],
            valid_to=data.get("valid_to"),
            currency=data.get("currency", "PLN"),
            energy_type=data.get("energy_type", "electricity"),
        )

    def calculate_total_cost(self, consumption_kwh: float) -> Decimal:
        """Calculate total cost for given consumption."""
        return self.base_price + (self.energy_price * Decimal(str(consumption_kwh))) + self.network_fee


@dataclass
class PriceAnalysis:
    """Results of price analysis for a given period."""

    period_start: date
    period_end: date
    energy_type: str
    average_price: float
    price_trend: str  # "increasing", "decreasing", "stable"
    volatility: float
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    analysis_date: Optional[datetime] = None

    def __post_init__(self) -> None:
        """Set analysis date if not provided."""
        if self.analysis_date is None:
            self.analysis_date = datetime.now()
