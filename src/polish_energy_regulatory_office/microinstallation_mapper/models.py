"""Data models for microinstallation mapping."""

from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class Microinstallation:
    """Represents a microinstallation."""

    installation_id: str
    capacity_kw: float
    commissioning_date: date
    voivodeship: str
    municipality: str


@dataclass
class ProsumerData:
    """Represents prosumer data."""

    prosumer_id: str
    installations: List[Microinstallation]


@dataclass
class GridConnection:
    """Represents grid connection data."""

    connection_id: str
    voltage_level: str
