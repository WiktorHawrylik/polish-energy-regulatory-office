# Polish Energy Regulatory Office Library

[![CI](https://github.com/WiktorHawrylik/polish-energy-regulatory-office/workflows/CI/badge.svg)](https://github.com/WiktorHawrylik/polish-energy-regulatory-office/actions)
[![codecov](https://codecov.io/gh/WiktorHawrylik/polish-energy-regulatory-office/branch/main/graph/badge.svg)](https://codecov.io/gh/WiktorHawrylik/polish-energy-regulatory-office)
[![PyPI version](https://badge.fury.io/py/polish-energy-regulatory-office.svg)](https://badge.fury.io/py/polish-energy-regulatory-office)
[![Python versions](https://img.shields.io/pypi/pyversions/polish-energy-regulatory-office.svg)](https://pypi.org/project/polish-energy-regulatory-office/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive Python library for creating insights from publicly available data on the Polish Energy Regulatory Office (Urząd Regulacji Energetyki) websites:
- [ure.gov.pl](https://ure.gov.pl)
- [bip.ure.gov.pl](https://bip.ure.gov.pl)

## 🚀 Features

This mono-repository contains 6 specialized Python modules for energy market analysis:

### 📊 Energy Price Analyzer
- Track and analyze energy price trends
- Compare tariff structures
- Generate price forecasts
- Historical price analysis

### 🗺️ Renewable Energy Sources Mapper
- Map renewable energy installations across Poland
- Analyze regional distribution of renewable sources
- Track capacity growth over time
- Visualize installation density by voivodeship

### ⚡ Microinstallation Mapper
- Monitor small-scale renewable energy deployments (≤50kW)
- Track prosumer adoption rates
- Analyze distributed generation patterns
- Grid impact assessment

### 🏢 Energy Efficiency Audit Tool
- Analyze energy efficiency metrics
- Generate comprehensive audit reports
- Track efficiency improvements over time
- Regulatory compliance checking

### 💰 Tariff Oracle
- Optimize energy tariff selection
- Predict tariff changes
- Calculate potential savings
- Compare multiple tariff options

### 🎯 Renewable Auctions Monitor
- Track renewable energy auction results
- Analyze bid patterns and clearing prices
- Monitor market trends
- Support mechanism analysis

## 📦 Installation

### From PyPI (recommended)
```bash
pip install polish-energy-regulatory-office
```

### From source
```bash
git clone https://github.com/WiktorHawrylik/polish-energy-regulatory-office.git
cd polish-energy-regulatory-office
pip install -e .
```

### Development installation

#### Option 1: Standard setup (Linux/Windows)
```bash
git clone https://github.com/WiktorHawrylik/polish-energy-regulatory-office.git
cd polish-energy-regulatory-office
./setup_dev.sh
```

#### Option 2: macOS with pyenv (recommended for macOS)
```bash
git clone https://github.com/WiktorHawrylik/polish-energy-regulatory-office.git
cd polish-energy-regulatory-office
./setup_dev_macos.sh
```

#### Option 3: Manual installation
```bash
git clone https://github.com/WiktorHawrylik/polish-energy-regulatory-office.git
cd polish-energy-regulatory-office
pip install -e ".[dev,test,docs]"
```

## 🔧 Quick Start

### Energy Price Analysis
```python
from polish_energy_regulatory_office.energy_price_analyzer import EnergyPriceAnalyzer
from datetime import date

# Initialize analyzer
analyzer = EnergyPriceAnalyzer()

# Analyze price trends
trends = analyzer.analyze_price_trends(
    start_date=date(2023, 1, 1),
    end_date=date(2023, 12, 31),
    energy_type="electricity"
)

print(f"Average price: {trends.average_price} PLN/MWh")
print(f"Price trend: {trends.price_trend}")
print(f"Volatility: {trends.volatility}")
```

### Renewable Energy Mapping
```python
from polish_energy_regulatory_office.renewable_energy_sources_mapper import RenewableEnergyMapper
from polish_energy_regulatory_office.renewable_energy_sources_mapper.models import InstallationType

# Initialize mapper
mapper = RenewableEnergyMapper()

# Get solar installations in Mazowieckie voivodeship
solar_installations = mapper.get_installations_by_region(
    voivodeship="mazowieckie",
    installation_type=InstallationType.SOLAR_PV
)

print(f"Found {len(solar_installations)} solar installations")

# Generate regional statistics
regional_stats = mapper.generate_regional_statistics()
for voivodeship, stats in regional_stats.items():
    print(f"{voivodeship}: {stats.total_capacity_kw:.2f} kW total capacity")
```

### Microinstallation Analysis
```python
from polish_energy_regulatory_office.microinstallation_mapper import MicroinstallationMapper

# Initialize mapper
micro_mapper = MicroinstallationMapper()

# Get microinstallations by region
installations = micro_mapper.get_microinstallations_by_region("śląskie")
print(f"Microinstallations in Śląskie: {len(installations)}")
```

### Tariff Optimization
```python
from polish_energy_regulatory_office.tariff_oracle import TariffOracle

# Initialize oracle
oracle = TariffOracle()

# Compare tariff options
tariff_comparison = oracle.compare_tariffs(
    tariff_ids=["G11", "G12", "G21"],
    annual_consumption_kwh=3500
)

best_tariff = oracle.recommend_optimal_tariff(
    consumption_profile={"peak": 1200, "off_peak": 2300}
)
print(f"Recommended tariff: {best_tariff}")
```

## 📋 Module Structure

```
src/polish_energy_regulatory_office/
├── energy_price_analyzer/
│   ├── analyzer.py          # Main analysis engine
│   ├── models.py           # Data models
│   ├── scrapers.py         # Web scraping utilities
│   └── utils.py            # Helper functions
├── renewable_energy_sources_mapper/
│   ├── mapper.py           # Mapping and analysis
│   ├── models.py           # Installation models
│   ├── scrapers.py         # Registry scrapers
│   └── utils.py            # Geospatial utilities
├── microinstallation_mapper/
│   ├── mapper.py           # Micro-installation analysis
│   ├── models.py           # Prosumer data models
│   ├── scrapers.py         # Microinstallation scrapers
│   └── utils.py            # Analysis utilities
├── energy_efficiency_audit_tool/
│   ├── auditor.py          # Audit engine
│   ├── models.py           # Audit data models
│   ├── scrapers.py         # Efficiency data scrapers
│   └── utils.py            # Audit utilities
├── tariff_oracle/
│   ├── oracle.py           # Tariff prediction engine
│   ├── models.py           # Tariff data models
│   ├── scrapers.py         # Tariff data scrapers
│   └── utils.py            # Optimization utilities
└── renewable_auctions_monitor/
    ├── monitor.py          # Auction monitoring
    ├── models.py           # Auction data models
    ├── scrapers.py         # Auction data scrapers
    └── utils.py            # Analysis utilities
```

## 🧪 Testing

Run tests with pytest:
```bash
# Run all tests
make test

# Run with coverage
pytest --cov=polish_energy_regulatory_office

# Run specific test file
pytest tests/unit/test_energy_price_analyzer.py

# Run tests across all Python versions
make test-all
```

## 🔍 Code Quality

This project maintains high code quality standards:

```bash
# Format code
make format

# Run linting
make lint

# Type checking
mypy src

# Pre-commit hooks
make pre-commit
```

## 📚 Documentation

Build documentation locally:
```bash
make docs
```

Or visit the [online documentation](https://polish-energy-regulatory-office.readthedocs.io) (when available).

## 🛠️ Development

### Setting up development environment

**Quick Setup (Recommended):**

For **macOS users with pyenv**:
```bash
git clone https://github.com/WiktorHawrylik/polish-energy-regulatory-office.git
cd polish-energy-regulatory-office
./setup_dev_macos.sh
```

For **Linux/Windows users**:
```bash
git clone https://github.com/WiktorHawrylik/polish-energy-regulatory-office.git
cd polish-energy-regulatory-office
./setup_dev.sh
```

**Manual Setup:**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/WiktorHawrylik/polish-energy-regulatory-office.git
   cd polish-energy-regulatory-office
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install development dependencies**:
   ```bash
   make install-dev
   ```

4. **Install pre-commit hooks**:
   ```bash
   make pre-commit
   ```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for your changes
5. Ensure tests pass (`make test`)
6. Ensure code quality (`make lint`)
7. Commit your changes (`git commit -m 'Add amazing feature'`)
8. Push to the branch (`git push origin feature/amazing-feature`)
9. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

- **Issues**: [GitHub Issues](https://github.com/WiktorHawrylik/polish-energy-regulatory-office/issues)
- **Discussions**: [GitHub Discussions](https://github.com/WiktorHawrylik/polish-energy-regulatory-office/discussions)
- **Email**: wiktor.hawrylik@gmail.com

## 📈 Roadmap

- [ ] Add support for historical data analysis
- [ ] Implement machine learning models for price prediction
- [ ] Add real-time data streaming capabilities
- [ ] Create interactive web dashboard
- [ ] Add support for European energy market data
- [ ] Implement automated report generation

## 🙏 Acknowledgments

- Polish Energy Regulatory Office (URE) for providing public data access
- Contributors and the open-source community
- Python data science ecosystem (pandas, requests, BeautifulSoup, etc.)

---

**Made with ❤️ for the Polish energy market analysis community**
