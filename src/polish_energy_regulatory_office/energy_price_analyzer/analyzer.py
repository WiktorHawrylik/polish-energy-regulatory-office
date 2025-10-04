"""Main analyzer class for energy price analysis."""

from datetime import date
from typing import Any, Dict, List, Optional

import pandas as pd

from .models import PriceAnalysis, PriceData, TariffStructure
from .scrapers import UREPriceScraper
from .utils import calculate_average_price


class EnergyPriceAnalyzer:
    """Main class for analyzing energy prices from URE data sources."""

    def __init__(self, scraper: Optional[UREPriceScraper] = None):
        """Initialize the analyzer with optional custom scraper."""
        self.scraper = scraper or UREPriceScraper()
        self._cache: Dict[str, Any] = {}

    def analyze_price_trends(self, start_date: date, end_date: date, energy_type: str = "electricity") -> PriceAnalysis:
        """Analyze price trends for a given period."""
        # Implementation placeholder
        price_data = self.scraper.fetch_price_data(start_date, end_date, energy_type)

        # Convert list of PriceData to pandas DataFrame for analysis
        if not price_data:
            return PriceAnalysis(
                period_start=start_date,
                period_end=end_date,
                energy_type=energy_type,
                average_price=0.0,
                price_trend="stable",
                volatility=0.0,
            )

        # Convert to DataFrame
        df_data = [
            {
                "date": item.date,
                "price": float(item.price),
                "energy_type": item.energy_type,
            }
            for item in price_data
        ]
        df = pd.DataFrame(df_data)

        # Calculate analysis metrics
        prices = [float(item.price) for item in price_data]
        average_price = calculate_average_price(prices)
        volatility = float(df["price"].std()) if len(df) > 1 else 0.0

        # Determine trend
        if len(prices) < 2:
            trend = "stable"
        else:
            first_half_avg = sum(prices[: len(prices) // 2]) / (len(prices) // 2)
            second_half_avg = sum(prices[len(prices) // 2 :]) / (len(prices) - len(prices) // 2)
            if second_half_avg > first_half_avg * 1.05:
                trend = "increasing"
            elif second_half_avg < first_half_avg * 0.95:
                trend = "decreasing"
            else:
                trend = "stable"

        return PriceAnalysis(
            period_start=start_date,
            period_end=end_date,
            energy_type=energy_type,
            average_price=average_price,
            price_trend=trend,
            volatility=volatility,
            min_price=min(prices) if prices else None,
            max_price=max(prices) if prices else None,
        )

    def compare_tariffs(
        self,
        tariff_ids: List[str],
        consumption_profile: Optional[Dict[str, float]] = None,
    ) -> Dict[str, TariffStructure]:
        """Compare multiple tariff structures."""
        # Implementation placeholder
        tariffs = {}
        for tariff_id in tariff_ids:
            tariff_data = self.scraper.fetch_tariff_data(tariff_id)
            tariffs[tariff_id] = TariffStructure.from_dict(tariff_data)

        return tariffs

    def forecast_prices(self, historical_data: List[PriceData], forecast_days: int = 30) -> List[PriceData]:
        """Generate price forecasts based on historical data."""
        # Implementation placeholder - would use ML models
        # For now, return empty list
        return []
