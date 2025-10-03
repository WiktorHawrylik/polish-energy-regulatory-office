"""Models for energy efficiency audit."""

from dataclasses import dataclass


@dataclass
class AuditReport:
    report_id: str


@dataclass
class EfficiencyMetrics:
    score: float


@dataclass
class BuildingData:
    building_id: str
