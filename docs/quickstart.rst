Quick Start
===========

This guide will help you get started with the Polish Energy Regulatory Office library quickly.

Basic Usage
-----------

Energy Price Analysis
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from polish_energy_regulatory_office.energy_price_analyzer import EnergyPriceAnalyzer
   from datetime import date

   # Initialize the analyzer
   analyzer = EnergyPriceAnalyzer()

   # Analyze price trends for a specific period
   trends = analyzer.analyze_price_trends(
       start_date=date(2023, 1, 1),
       end_date=date(2023, 12, 31)
   )

   print(f"Average price: {trends.average_price} PLN/MWh")
   print(f"Price trend: {trends.price_trend}")

Renewable Energy Mapping
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from polish_energy_regulatory_office.renewable_energy_sources_mapper import RenewableMapper

   # Initialize the mapper
   mapper = RenewableMapper()

   # Get renewable installations in a specific region
   installations = mapper.get_installations_by_region("mazowieckie")

   for installation in installations:
       print(f"{installation.name}: {installation.capacity_mw} MW")

Microinstallation Tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from polish_energy_regulatory_office.microinstallation_mapper import MicroinstallationMapper

   # Initialize the mapper
   micro_mapper = MicroinstallationMapper()

   # Get microinstallations data
   micro_data = micro_mapper.get_recent_installations(days=30)

   print(f"New installations in last 30 days: {len(micro_data)}")

Energy Efficiency Auditing
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from polish_energy_regulatory_office.energy_efficiency_audit_tool import EnergyAuditor

   # Initialize the auditor
   auditor = EnergyAuditor()

   # Perform an audit
   audit_result = auditor.perform_audit(company_id="12345")

   print(f"Efficiency score: {audit_result.efficiency_score}")
   print(f"Recommendations: {audit_result.recommendations}")

Tariff Optimization
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from polish_energy_regulatory_office.tariff_oracle import TariffOracle

   # Initialize the oracle
   oracle = TariffOracle()

   # Find optimal tariff
   optimal_tariff = oracle.find_optimal_tariff(
       annual_consumption_kwh=5000,
       consumption_profile="residential"
   )

   print(f"Recommended tariff: {optimal_tariff.name}")
   print(f"Estimated annual cost: {optimal_tariff.estimated_cost} PLN")

Auction Monitoring
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from polish_energy_regulatory_office.renewable_auctions_monitor import AuctionMonitor

   # Initialize the monitor
   monitor = AuctionMonitor()

   # Get latest auction results
   results = monitor.get_latest_results()

   for result in results:
       print(f"Auction {result.auction_id}: {result.awarded_capacity_mw} MW awarded")

Configuration
-------------

The library can be configured through environment variables or a configuration file:

.. code-block:: python

   import os

   # Set data cache directory
   os.environ['PERO_CACHE_DIR'] = '/path/to/cache'

   # Set request timeout
   os.environ['PERO_REQUEST_TIMEOUT'] = '30'

Error Handling
--------------

The library provides comprehensive error handling:

.. code-block:: python

   from polish_energy_regulatory_office.exceptions import PERODataError, PERONetworkError

   try:
       analyzer = EnergyPriceAnalyzer()
       trends = analyzer.analyze_price_trends(start_date, end_date)
   except PERONetworkError as e:
       print(f"Network error: {e}")
   except PERODataError as e:
       print(f"Data processing error: {e}")

Next Steps
----------

* Read the :doc:`modules/index` for detailed module documentation
* Check out :doc:`examples` for more comprehensive examples
* Review the :doc:`api/index` for complete API reference
