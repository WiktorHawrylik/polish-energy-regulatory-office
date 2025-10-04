API Reference
=============

Complete API reference for all modules in the Polish Energy Regulatory Office library.

Overview
--------

This section provides detailed API documentation for all public classes, methods,
and functions in the library. Each module's API is documented with:

- Class definitions and inheritance
- Method signatures and parameters
- Return types and values
- Exception handling
- Usage examples

API Design Principles
---------------------

The library follows these API design principles:

**Consistency**
  All modules follow similar naming conventions and method signatures.

**Type Safety**
  Full type hints are provided for all public APIs.

**Documentation**
  Comprehensive docstrings with examples for all public methods.

**Error Handling**
  Clear exception hierarchies with meaningful error messages.

**Backward Compatibility**
  Semantic versioning ensures backward compatibility within major versions.

Common Patterns
---------------

Data Models
~~~~~~~~~~~

All modules use Pydantic models for data validation and serialization:

.. code-block:: python

   from pydantic import BaseModel
   from datetime import date
   from typing import Optional

   class EnergyPrice(BaseModel):
       date: date
       price_pln_mwh: float
       market_segment: str
       region: Optional[str] = None

Configuration
~~~~~~~~~~~~~

Modules accept configuration through environment variables or config objects:

.. code-block:: python

   from polish_energy_regulatory_office.config import Config

   config = Config(
       cache_dir="/tmp/pero_cache",
       request_timeout=30,
       max_retries=3
   )

Error Handling
~~~~~~~~~~~~~~

All modules raise specific exceptions from the exceptions hierarchy:

.. code-block:: python

   from polish_energy_regulatory_office.exceptions import (
       PEROError,
       PERODataError,
       PERONetworkError
   )

   try:
       result = analyzer.analyze_trends()
   except PERONetworkError:
       # Handle network issues
       pass
   except PERODataError:
       # Handle data processing issues
       pass

Async Support
~~~~~~~~~~~~~

Many operations support async execution for better performance:

.. code-block:: python

   import asyncio
   from polish_energy_regulatory_office.energy_price_analyzer import AsyncEnergyPriceAnalyzer

   async def analyze_prices():
       analyzer = AsyncEnergyPriceAnalyzer()
       return await analyzer.analyze_price_trends(start_date, end_date)

   results = asyncio.run(analyze_prices())
