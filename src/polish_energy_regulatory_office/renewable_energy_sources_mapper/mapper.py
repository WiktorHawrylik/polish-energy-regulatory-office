"""
Main mapper class for renewable energy sources analysis.
"""

from datetime import date
from typing import Any, Dict, List, Optional, Tuple

from .models import InstallationType, RegionalData, RenewableInstallation
from .scrapers import RESRegistryScraper
from .utils import calculate_capacity_growth, generate_geospatial_data


class RenewableEnergyMapper:
    """Main class for mapping and analyzing renewable energy sources."""

    def __init__(self, timeout: int = 30):
        """Initialize the mapper with a registry scraper."""
        self.scraper = RESRegistryScraper(timeout=timeout)

    def get_installations_by_region(
        self,
        voivodeship: Optional[str] = None,
        installation_type: Optional[InstallationType] = None,
    ) -> List[RenewableInstallation]:
        """Get installations filtered by region and/or type."""
        installations = self.scraper.fetch_installations(voivodeship=voivodeship)

        if installation_type:
            installations = [
                inst
                for inst in installations
                if inst.installation_type == installation_type
            ]

        return installations

    def get_installations_by_municipality(
        self, municipality: str, voivodeship: str
    ) -> List[RenewableInstallation]:
        """Get installations for a specific municipality."""
        installations = self.get_installations_by_region(voivodeship=voivodeship)
        return [
            inst
            for inst in installations
            if inst.municipality.lower() == municipality.lower()
        ]

    def analyze_capacity_trends(self) -> Dict[str, float]:
        """Analyze capacity growth trends across all installations."""
        installations = self.scraper.fetch_installations()
        return calculate_capacity_growth(installations)

    def generate_regional_statistics(self) -> Dict[str, RegionalData]:
        """Generate statistics for each voivodeship."""
        installations = self.scraper.fetch_installations()
        regional_stats = {}

        by_voivodeship: Dict[str, List[RenewableInstallation]] = {}
        for inst in installations:
            if inst.voivodeship not in by_voivodeship:
                by_voivodeship[inst.voivodeship] = []
            by_voivodeship[inst.voivodeship].append(inst)

        for voivodeship, inst_list in by_voivodeship.items():
            total_capacity = sum(inst.capacity_kw for inst in inst_list)
            installation_count = len(inst_list)

            type_distribution = {}
            for inst_type in InstallationType:
                type_count = len(
                    [inst for inst in inst_list if inst.installation_type == inst_type]
                )
                type_distribution[inst_type.value] = type_count

            regional_stats[voivodeship] = RegionalData(
                voivodeship=voivodeship,
                total_capacity_kw=total_capacity,
                installation_count=installation_count,
                type_distribution=type_distribution,
            )

        return regional_stats

    def create_geospatial_map(
        self, installation_type: Optional[InstallationType] = None
    ) -> Dict[str, Any]:
        """Create geospatial data for mapping installations."""
        installations = self.get_installations_by_region(
            installation_type=installation_type
        )
        geospatial_data = generate_geospatial_data(installations)
        return {"geospatial_points": geospatial_data}

    def get_top_municipalities(
        self, limit: int = 10, sort_by: str = "capacity"
    ) -> List[Dict[str, Any]]:
        """Get top municipalities by capacity or installation count."""
        installations = self.scraper.fetch_installations()

        by_municipality: Dict[Tuple[str, str], List[RenewableInstallation]] = {}
        for inst in installations:
            key = (inst.municipality, inst.voivodeship)
            if key not in by_municipality:
                by_municipality[key] = []
            by_municipality[key].append(inst)

        municipality_stats = []
        for (municipality, voivodeship), inst_list in by_municipality.items():
            total_capacity = sum(inst.capacity_kw for inst in inst_list)
            municipality_stats.append(
                {
                    "municipality": municipality,
                    "voivodeship": voivodeship,
                    "total_capacity_kw": total_capacity,
                    "installation_count": len(inst_list),
                }
            )

        if sort_by == "capacity":
            municipality_stats.sort(key=lambda x: x["total_capacity_kw"], reverse=True)
        else:
            municipality_stats.sort(key=lambda x: x["installation_count"], reverse=True)

        return municipality_stats[:limit]

    def generate_summary_report(self) -> Dict[str, Any]:
        """Generate a comprehensive summary report."""
        installations = self.scraper.fetch_installations()

        total_capacity = sum(inst.capacity_kw for inst in installations)
        total_count = len(installations)

        by_type = {}
        for inst_type in InstallationType:
            type_installations = [
                inst for inst in installations if inst.installation_type == inst_type
            ]
            by_type[inst_type.value] = {
                "count": len(type_installations),
                "capacity_kw": sum(inst.capacity_kw for inst in type_installations),
            }

        return {
            "total_installations": total_count,
            "total_capacity_kw": total_capacity,
            "average_capacity_per_installation": (
                total_capacity / total_count if total_count > 0 else 0
            ),
            "by_type": by_type,
            "report_date": date.today().isoformat(),
        }
