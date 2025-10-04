Contributing
============

We welcome contributions to the Polish Energy Regulatory Office library! This guide will help you get started with contributing to the project.

Getting Started
---------------

Setting Up Development Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Fork the repository on GitHub
2. Clone your fork locally:

.. code-block:: bash

   git clone https://github.com/your-username/polish-energy-regulatory-office.git
   cd polish-energy-regulatory-office

3. Set up the development environment:

.. code-block:: bash

   # On macOS
   ./setup_dev_macos.sh

   # On Linux
   ./setup_dev.sh

4. Install the package in development mode:

.. code-block:: bash

   pip install -e ".[dev]"

5. Set up pre-commit hooks:

.. code-block:: bash

   pre-commit install

Development Workflow
--------------------

Creating a Feature Branch
~~~~~~~~~~~~~~~~~~~~~~~~~~

Always create a new branch for your work:

.. code-block:: bash

   git checkout -b feature/your-feature-name
   # or
   git checkout -b bugfix/issue-description

Making Changes
~~~~~~~~~~~~~~

1. Make your changes following the code style guidelines
2. Add tests for new functionality
3. Update documentation as needed
4. Run the test suite to ensure everything works

Running Tests
~~~~~~~~~~~~~

.. code-block:: bash

   # Run all tests
   pytest

   # Run tests with coverage
   pytest --cov=src/polish_energy_regulatory_office

   # Run specific test file
   pytest tests/unit/test_energy_price_analyzer.py

   # Run integration tests
   pytest tests/integration/

Code Quality
~~~~~~~~~~~~

We use several tools to maintain code quality:

.. code-block:: bash

   # Format code with black
   black src/ tests/

   # Sort imports with isort
   isort src/ tests/

   # Lint with flake8
   flake8 src/ tests/

   # Type check with mypy
   mypy src/

   # Run all quality checks
   make lint

Documentation
~~~~~~~~~~~~~

Update documentation when making changes:

.. code-block:: bash

   # Build documentation locally
   cd docs/
   make html

   # View documentation
   open _build/html/index.html

Code Style Guidelines
---------------------

Python Code Style
~~~~~~~~~~~~~~~~~~

We follow PEP 8 with some specific guidelines:

- **Line Length**: Maximum 88 characters (Black default)
- **Imports**: Use absolute imports, sort with isort
- **Type Hints**: All public functions must have type hints
- **Docstrings**: Use Google-style docstrings

Example:

.. code-block:: python

   from typing import List, Optional
   from datetime import date

   def analyze_price_trends(
       start_date: date,
       end_date: date,
       region: Optional[str] = None
   ) -> List[PriceTrend]:
       """Analyze energy price trends for a given period.

       Args:
           start_date: Start date for analysis
           end_date: End date for analysis
           region: Optional region filter

       Returns:
           List of price trend objects

       Raises:
           PERODataError: If data is invalid or unavailable
       """
       pass

Documentation Style
~~~~~~~~~~~~~~~~~~~

- Use reStructuredText for documentation
- Include code examples in docstrings
- Update API documentation for new features
- Write user-friendly guides and tutorials

Testing Guidelines
------------------

Test Structure
~~~~~~~~~~~~~~

We use pytest with the following structure:

- `tests/unit/`: Unit tests for individual components
- `tests/integration/`: Integration tests for full workflows
- `tests/conftest.py`: Shared test fixtures

Writing Tests
~~~~~~~~~~~~~

.. code-block:: python

   import pytest
   from polish_energy_regulatory_office.energy_price_analyzer import EnergyPriceAnalyzer
   from polish_energy_regulatory_office.exceptions import PERODataError

   class TestEnergyPriceAnalyzer:
       def test_analyze_price_trends_success(self, sample_price_data):
           analyzer = EnergyPriceAnalyzer()
           trends = analyzer.analyze_price_trends(
               start_date=date(2023, 1, 1),
               end_date=date(2023, 1, 31)
           )
           assert trends.average_price > 0
           assert trends.trend_direction in ["up", "down", "stable"]

       def test_analyze_price_trends_invalid_date_range(self):
           analyzer = EnergyPriceAnalyzer()
           with pytest.raises(PERODataError):
               analyzer.analyze_price_trends(
                   start_date=date(2023, 1, 31),
                   end_date=date(2023, 1, 1)  # End before start
               )

Test Coverage
~~~~~~~~~~~~~

- Aim for at least 80% code coverage
- Test both success and error cases
- Include edge cases and boundary conditions
- Mock external dependencies

Pull Request Process
--------------------

Before Submitting
~~~~~~~~~~~~~~~~~

1. Ensure all tests pass
2. Verify code style compliance
3. Update documentation
4. Add changelog entry
5. Rebase on latest main branch

Submitting a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Push your branch to your fork
2. Create a pull request with:
   - Clear title describing the change
   - Detailed description of what was changed and why
   - References to related issues
   - Screenshots for UI changes (if applicable)

Pull Request Template:

.. code-block:: markdown

   ## Description
   Brief description of changes

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Breaking change
   - [ ] Documentation update

   ## Testing
   - [ ] Added tests for new functionality
   - [ ] All tests pass
   - [ ] Tested manually

   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Self-review completed
   - [ ] Documentation updated
   - [ ] Changelog updated

Review Process
~~~~~~~~~~~~~~

1. Automated checks must pass
2. At least one maintainer review required
3. Address feedback and update as needed
4. Maintainer will merge when approved

Reporting Issues
----------------

Bug Reports
~~~~~~~~~~~

Use the bug report template and include:

- Python version and operating system
- Library version
- Minimal code example reproducing the issue
- Expected vs actual behavior
- Complete error traceback

Feature Requests
~~~~~~~~~~~~~~~~

For new features, please:

- Describe the use case
- Explain why existing functionality doesn't work
- Provide examples of the desired API
- Consider backwards compatibility

Security Issues
~~~~~~~~~~~~~~~

For security vulnerabilities:

- Do NOT create a public issue
- Email security@example.com directly
- Include details and proof of concept
- Allow time for patch development before disclosure

Release Process
---------------

Versioning
~~~~~~~~~~

We use Semantic Versioning (SemVer):

- MAJOR: Breaking changes
- MINOR: New features (backwards compatible)
- PATCH: Bug fixes (backwards compatible)

Changelog
~~~~~~~~~

Update CHANGELOG.md with:

- Version number and date
- Added features
- Changed functionality
- Fixed bugs
- Removed features

Community Guidelines
--------------------

Code of Conduct
~~~~~~~~~~~~~~~

We follow the Contributor Covenant Code of Conduct. In summary:

- Be respectful and inclusive
- Welcome newcomers
- Provide constructive feedback
- Focus on what's best for the community

Getting Help
~~~~~~~~~~~~

- Read the documentation first
- Search existing issues
- Ask questions in discussions
- Join our community chat (if available)

Recognition
~~~~~~~~~~~

Contributors are recognized in:

- Git commit history
- Release notes
- Contributors file
- Annual contributor appreciation

Thank you for contributing to the Polish Energy Regulatory Office library!
