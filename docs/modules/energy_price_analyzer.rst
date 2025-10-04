Energy Price Analyzer
====================

The Energy Price Analyzer module provides comprehensive tools for analyzing energy price trends,
market dynamics, and cost forecasting based on data from the Polish Energy Regulatory Office.

.. currentmodule:: polish_energy_regulatory_office.energy_price_analyzer

Overview
--------

This module offers:

- **Real-time Price Tracking**: Access to current energy prices across different market segments
- **Historical Analysis**: Comprehensive analysis of historical price data and trends
- **Volatility Assessment**: Market volatility calculations and risk metrics
- **Forecasting**: Price prediction models based on historical patterns
- **Comparative Analysis**: Cross-market and cross-period comparisons

Core Classes
------------

EnergyPriceAnalyzer
~~~~~~~~~~~~~~~~~~~

.. autoclass:: EnergyPriceAnalyzer
   :members:
   :inherited-members:
   :show-inheritance:

AsyncEnergyPriceAnalyzer
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: AsyncEnergyPriceAnalyzer
   :members:
   :inherited-members:
   :show-inheritance:

Data Models
-----------

PriceData
~~~~~~~~~

.. autoclass:: PriceData
   :members:
   :show-inheritance:

PriceTrend
~~~~~~~~~~

.. autoclass:: PriceTrend
   :members:
   :show-inheritance:

MarketSegment
~~~~~~~~~~~~~

.. autoclass:: MarketSegment
   :members:
   :show-inheritance:

Usage Examples
--------------

Basic Price Analysis
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from polish_energy_regulatory_office.energy_price_analyzer import EnergyPriceAnalyzer
   from datetime import date, timedelta

   analyzer = EnergyPriceAnalyzer()

   # Get current prices
   current_prices = analyzer.get_current_prices()
   print(f"Current average price: {current_prices.average_price:.2f} PLN/MWh")

   # Analyze trends for the last 30 days
   end_date = date.today()
   start_date = end_date - timedelta(days=30)

   trends = analyzer.analyze_price_trends(start_date, end_date)
   print(f"30-day trend: {trends.trend_direction}")
   print(f"Volatility: {trends.volatility:.2f}%")

Historical Data Analysis
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get detailed historical data
   historical_data = analyzer.get_price_history(
       start_date=date(2023, 1, 1),
       end_date=date(2023, 12, 31),
       market_segment="day_ahead"
   )

   # Calculate statistics
   prices = [data.price_pln_mwh for data in historical_data]
   avg_price = sum(prices) / len(prices)
   max_price = max(prices)
   min_price = min(prices)

   print(f"2023 Statistics:")
   print(f"Average: {avg_price:.2f} PLN/MWh")
   print(f"Range: {min_price:.2f} - {max_price:.2f} PLN/MWh")

Price Forecasting
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Generate price forecast
   forecast = analyzer.forecast_prices(
       horizon_days=7,
       confidence_level=0.95
   )

   for day_forecast in forecast.daily_forecasts:
       print(f"{day_forecast.date}: {day_forecast.predicted_price:.2f} PLN/MWh "
             f"(±{day_forecast.confidence_interval:.2f})")

Async Operations
~~~~~~~~~~~~~~~~

.. code-block:: python

   import asyncio
   from polish_energy_regulatory_office.energy_price_analyzer import AsyncEnergyPriceAnalyzer

   async def analyze_multiple_periods():
       analyzer = AsyncEnergyPriceAnalyzer()

       # Analyze multiple periods concurrently
       tasks = [
           analyzer.analyze_price_trends(date(2023, 1, 1), date(2023, 3, 31)),
           analyzer.analyze_price_trends(date(2023, 4, 1), date(2023, 6, 30)),
           analyzer.analyze_price_trends(date(2023, 7, 1), date(2023, 9, 30)),
           analyzer.analyze_price_trends(date(2023, 10, 1), date(2023, 12, 31))
       ]

       results = await asyncio.gather(*tasks)

       for i, trend in enumerate(results, 1):
           print(f"Q{i} 2023: {trend.average_price:.2f} PLN/MWh, "
                 f"trend: {trend.trend_direction}")

   asyncio.run(analyze_multiple_periods())

Configuration
-------------

The analyzer can be configured through environment variables or a configuration object:

.. code-block:: python

   from polish_energy_regulatory_office.config import Config

   config = Config(
       cache_ttl_hours=6,        # Cache data for 6 hours
       request_timeout=30,       # 30 second timeout
       max_retries=3,           # Retry failed requests 3 times
       rate_limit_delay=1.0     # 1 second between requests
   )

   analyzer = EnergyPriceAnalyzer(config=config)

Environment Variables:

- ``PERO_CACHE_TTL_HOURS``: Cache time-to-live in hours (default: 6)
- ``PERO_REQUEST_TIMEOUT``: HTTP request timeout in seconds (default: 30)
- ``PERO_MAX_RETRIES``: Maximum number of retries (default: 3)
- ``PERO_RATE_LIMIT_DELAY``: Delay between requests in seconds (default: 1.0)

Error Handling
--------------

The module provides specific exceptions for different error scenarios:

.. code-block:: python

   from polish_energy_regulatory_office.exceptions import (
       PERODataError,
       PERONetworkError,
       PEROValidationError
   )

   try:
       trends = analyzer.analyze_price_trends(start_date, end_date)
   except PERONetworkError as e:
       print(f"Network error: {e}")
       # Handle network connectivity issues
   except PERODataError as e:
       print(f"Data error: {e}")
       # Handle data parsing or unavailability issues
   except PEROValidationError as e:
       print(f"Validation error: {e}")
       # Handle invalid input parameters

Performance Considerations
--------------------------

- **Caching**: Data is automatically cached to reduce API calls
- **Rate Limiting**: Built-in rate limiting respects server constraints
- **Async Support**: Use async operations for better concurrency
- **Batch Operations**: Group related operations to minimize overhead

Best Practices
--------------

1. **Use Appropriate Time Ranges**: Don't request unnecessarily large date ranges
2. **Handle Errors Gracefully**: Always implement proper error handling
3. **Respect Rate Limits**: Use the built-in rate limiting features
4. **Cache Appropriately**: Configure cache settings based on your use case
5. **Monitor Performance**: Use logging to track operation performance

API Reference
-------------

For detailed API documentation, see :doc:`../api/energy_price_analyzer`.
