"""
Pytest configuration and fixtures for the Polish Energy Regulatory Office library.
"""

from datetime import date
from decimal import Decimal
from unittest.mock import Mock

import pytest


@pytest.fixture
def sample_price_data():
    """Sample price data for testing."""
    from polish_energy_regulatory_office.energy_price_analyzer.models import PriceData

    return [
        PriceData(
            date=date(2023, 1, 1),
            price=Decimal("250.50"),
            energy_type="electricity",
            unit="PLN/MWh",
        ),
        PriceData(
            date=date(2023, 1, 2),
            price=Decimal("255.75"),
            energy_type="electricity",
            unit="PLN/MWh",
        ),
    ]


@pytest.fixture
def sample_installation_data():
    """Sample renewable installation data for testing."""
    from polish_energy_regulatory_office.renewable_energy_sources_mapper.models import (
        InstallationType,
        RenewableInstallation,
    )

    return [
        RenewableInstallation(
            installation_id="TEST001",
            name="Test Solar Farm",
            installation_type=InstallationType.SOLAR_PV,
            capacity_kw=1000.0,
            commissioning_date=date(2023, 6, 15),
            voivodeship="mazowieckie",
            municipality="Warszawa",
            operator="Test Energy Ltd",
        )
    ]


@pytest.fixture
def mock_ure_scraper():
    """Mock URE scraper for testing."""
    return Mock()


@pytest.fixture
def test_date_range():
    """Standard date range for testing."""
    return {"start_date": date(2023, 1, 1), "end_date": date(2023, 12, 31)}
