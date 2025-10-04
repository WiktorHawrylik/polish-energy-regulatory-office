Installation
============

Requirements
------------

* Python 3.8 or higher
* pip package manager

Installing from PyPI
---------------------

.. code-block:: bash

   pip install polish-energy-regulatory-office

Installing from Source
-----------------------

1. Clone the repository:

.. code-block:: bash

   git clone https://github.com/WiktorMadejski/polish-energy-regulatory-office.git
   cd polish-energy-regulatory-office

2. Install in development mode:

.. code-block:: bash

   pip install -e .

Development Installation
------------------------

For development work, install with additional dependencies:

.. code-block:: bash

   pip install -e ".[dev]"

This will install additional tools for testing, linting, and documentation building.

Verification
------------

To verify the installation, run:

.. code-block:: python

   import polish_energy_regulatory_office
   print(polish_energy_regulatory_office.__version__)
