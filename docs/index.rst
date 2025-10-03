Polish Energy Regulatory Office Library
======================================

A comprehensive Python library for creating insights from publicly available data
on the Polish Energy Regulatory Office (Urząd Regulacji Energetyki) websites.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   modules/index
   api/index
   examples
   contributing
   changelog

Overview
--------

This library provides tools for:

* **Energy Price Analysis** - Track and analyze energy price trends
* **Renewable Energy Mapping** - Map and analyze renewable energy installations
* **Microinstallation Tracking** - Monitor small-scale renewable deployments
* **Energy Efficiency Auditing** - Analyze efficiency metrics and generate reports
* **Tariff Optimization** - Compare and optimize energy tariff selections
* **Auction Monitoring** - Track renewable energy auction results and trends

Key Features
-----------

* **Comprehensive Data Access**: Scrape and process data from URE websites
* **Advanced Analytics**: Built-in analysis tools for energy market insights
* **Geospatial Mapping**: Visualize energy installations and regional distribution
* **Flexible API**: Easy-to-use interfaces for all modules
* **Type Safety**: Full type hints and validation throughout
* **Well Tested**: Comprehensive test suite with high coverage

Quick Start
----------

.. code-block:: python

   from polish_energy_regulatory_office import energy_price_analyzer

   # Analyze energy price trends
   analyzer = energy_price_analyzer.EnergyPriceAnalyzer()
   trends = analyzer.analyze_price_trends(
       start_date=date(2023, 1, 1),
       end_date=date(2023, 12, 31)
   )

   print(f"Average price: {trends.average_price} PLN/MWh")
   print(f"Price trend: {trends.price_trend}")

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
