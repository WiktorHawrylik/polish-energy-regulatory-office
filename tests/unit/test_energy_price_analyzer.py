"""
Unit tests for energy price analyzer module.
"""

from datetime import date
from decimal import Decimal

import pytest

from polish_energy_regulatory_office.energy_price_analyzer import EnergyPriceAnalyzer
from polish_energy_regulatory_office.energy_price_analyzer.models import (
    PriceData,
    TariffStructure,
)
from polish_energy_regulatory_office.energy_price_analyzer.utils import format_currency


class TestEnergyPriceAnalyzer:
    """Test cases for EnergyPriceAnalyzer class."""

    def test_analyzer_initialization(self):
        """Test analyzer initialization."""
        analyzer = EnergyPriceAnalyzer()
        assert analyzer is not None
        assert hasattr(analyzer, "scraper")

    def test_analyze_price_trends_with_mock_data(
        self, mock_ure_scraper, sample_price_data
    ):
        """Test price trend analysis with mock data."""
        mock_ure_scraper.fetch_price_data.return_value = sample_price_data

        analyzer = EnergyPriceAnalyzer(scraper=mock_ure_scraper)
        result = analyzer.analyze_price_trends(
            start_date=date(2023, 1, 1), end_date=date(2023, 1, 31)
        )

        assert result is not None
        assert hasattr(result, "period_start")
        assert hasattr(result, "period_end")
        assert hasattr(result, "average_price")

    def test_compare_tariffs(self, mock_ure_scraper):
        """Test tariff comparison functionality."""
        mock_tariff_data = {
            "tariff_id": "G11",
            "name": "Test Tariff",
            "base_price": 45.0,
            "energy_price": 0.65,
            "network_fee": 25.0,
            "valid_from": date.today(),
        }

        mock_ure_scraper.fetch_tariff_data.return_value = mock_tariff_data

        analyzer = EnergyPriceAnalyzer(scraper=mock_ure_scraper)
        result = analyzer.compare_tariffs(["G11", "G12"])

        assert isinstance(result, dict)
        assert len(result) > 0


class TestPriceData:
    """Test cases for PriceData model."""

    def test_price_data_creation(self):
        """Test creating price data instance."""
        price_data = PriceData(
            date=date(2023, 1, 1), price=Decimal("250.50"), energy_type="electricity"
        )

        assert price_data.date == date(2023, 1, 1)
        assert price_data.price == Decimal("250.50")
        assert price_data.energy_type == "electricity"
        assert price_data.unit == "PLN/MWh"  # default value

    def test_price_data_validation(self):
        """Test price data validation."""
        with pytest.raises(ValueError, match="Price cannot be negative"):
            PriceData(
                date=date(2023, 1, 1),
                price=Decimal("-100.0"),
                energy_type="electricity",
            )

        with pytest.raises(ValueError, match="Energy type is required"):
            PriceData(date=date(2023, 1, 1), price=Decimal("250.50"), energy_type="")


class TestTariffStructure:
    """Test cases for TariffStructure model."""

    def test_tariff_structure_creation(self):
        """Test creating tariff structure."""
        tariff = TariffStructure(
            tariff_id="G11",
            name="Test Tariff",
            base_price=Decimal("45.0"),
            energy_price=Decimal("0.65"),
            network_fee=Decimal("25.0"),
            valid_from=date(2023, 1, 1),
        )

        assert tariff.tariff_id == "G11"
        assert tariff.name == "Test Tariff"
        assert tariff.currency == "PLN"  # default value

    def test_calculate_total_cost(self):
        """Test total cost calculation."""
        tariff = TariffStructure(
            tariff_id="G11",
            name="Test Tariff",
            base_price=Decimal("45.0"),
            energy_price=Decimal("0.65"),
            network_fee=Decimal("25.0"),
            valid_from=date(2023, 1, 1),
        )

        total_cost = tariff.calculate_total_cost(100.0)  # 100 kWh
        expected_cost = (
            Decimal("45.0") + (Decimal("0.65") * Decimal("100.0")) + Decimal("25.0")
        )

        assert total_cost == expected_cost


class TestUtils:
    """Test cases for utility functions."""

    def test_format_currency_pln(self):
        """Test PLN currency formatting."""
        result = format_currency(Decimal("123.45"), "PLN")
        assert result == "123.45 PLN"

    def test_format_currency_other(self):
        """Test other currency formatting."""
        result = format_currency(Decimal("123.45"), "EUR")
        assert result == "123.45 EUR"
