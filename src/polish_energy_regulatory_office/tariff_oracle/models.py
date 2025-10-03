"""Models for tariff oracle."""

from dataclasses import dataclass


@dataclass
class TariffPrediction:
    prediction_id: str


@dataclass
class CostAnalysis:
    analysis_id: str


@dataclass
class TariffHistory:
    history_id: str
