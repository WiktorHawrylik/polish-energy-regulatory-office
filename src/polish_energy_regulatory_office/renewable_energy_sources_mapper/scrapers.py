"""Scrapers for renewable energy sources data."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional

import requests
from bs4 import BeautifulSoup

from .models import InstallationType, RenewableInstallation


class RESRegistryScraper:
    """Scraper for renewable energy sources registry from URE."""

    BASE_URL = "https://www.ure.gov.pl"
    REGISTRY_ENDPOINTS = {
        "installations": (
            "/pl/oze/rejestry-i-bazy-danych-oze/5678," "Rejestr-wytworcow-energii-w-mikroinstalacjach.html"
        ),
        "producers": (
            "/pl/oze/rejestry-i-bazy-danych-oze/5677," "Rejestr-wytworcow-w-odnawialnych-zrodlach-energii.html"
        ),
    }

    def __init__(self, timeout: int = 30):
        """Initialize scraper with configuration."""
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/91.0.4472.124 Safari/537.36"
                ),
                "Accept": ("text/html,application/xhtml+xml," "application/xml;q=0.9,*/*;q=0.8"),
                "Accept-Language": "pl-PL,pl;q=0.9,en;q=0.8",
                "Accept-Encoding": "gzip, deflate",
                "Connection": "keep-alive",
            }
        )

    def fetch_installations(
        self,
        installation_type: Optional[InstallationType] = None,
        voivodeship: Optional[str] = None,
    ) -> List[RenewableInstallation]:
        """Fetch renewable energy installations from the registry."""
        # This is a placeholder implementation
        # In a real implementation, this would scrape the actual website
        return []

    def fetch_installation_details(self, installation_id: str) -> Dict[str, Any]:
        """Fetch detailed information for a specific installation."""
        try:
            url = f"{self.BASE_URL}/installation/{installation_id}"
            response = self.session.get(url, timeout=30)
            response.raise_for_status()

            # Placeholder parsing logic
            data = {
                "installation_id": installation_id,
                "name": "Sample Installation",
                "capacity_kw": 100.0,
                "status": "active",
            }

            return data

        except requests.exceptions.RequestException:
            return {"error": "Failed to fetch installation data"}
        except Exception:
            return {"error": "Unexpected error occurred"}

    def fetch_regional_summary(self, voivodeship: str) -> Dict[str, Any]:
        """Fetch summary statistics for a specific voivodeship."""
        installations = self.fetch_installations(voivodeship=voivodeship)

        total_capacity = sum(inst.capacity_kw for inst in installations)
        installation_count = len(installations)

        # Group by installation type
        by_type = {}
        for inst in installations:
            inst_type = inst.installation_type.value
            if inst_type not in by_type:
                by_type[inst_type] = {"count": 0, "capacity": 0.0}
            by_type[inst_type]["count"] += 1
            by_type[inst_type]["capacity"] += inst.capacity_kw

        return {
            "voivodeship": voivodeship,
            "total_capacity_kw": total_capacity,
            "installation_count": installation_count,
            "by_type": by_type,
            "last_updated": datetime.now().isoformat(),
        }

    def _parse_json_installations(self, data: Dict[str, Any]) -> List[RenewableInstallation]:
        """Parse installations from JSON response."""
        installations = []

        if "installations" in data:
            for item in data["installations"]:
                try:
                    installation = RenewableInstallation.from_dict(item)
                    installations.append(installation)
                except (KeyError, ValueError):
                    # Log parsing error and continue
                    continue

        return installations

    def _parse_html_installations(self, html_content: str) -> List[RenewableInstallation]:
        """Parse installations from HTML response."""
        installations = []
        soup = BeautifulSoup(html_content, "html.parser")

        # Find table rows or other structured data
        rows = soup.find_all("tr")

        for row in rows[1:]:  # Skip header row
            cells = row.find_all("td")
            if len(cells) >= 8:
                try:
                    installation_data = {
                        "installation_id": cells[0].get_text(strip=True),
                        "name": cells[1].get_text(strip=True),
                        "installation_type": "solar_pv",
                        "capacity_kw": float(cells[2].get_text(strip=True).replace(",", ".")),
                        "commissioning_date": datetime.strptime(cells[3].get_text(strip=True), "%Y-%m-%d").date(),
                        "voivodeship": cells[4].get_text(strip=True),
                        "municipality": cells[5].get_text(strip=True),
                        "operator": cells[6].get_text(strip=True),
                        "status": cells[7].get_text(strip=True),
                    }

                    installation = RenewableInstallation.from_dict(installation_data)
                    installations.append(installation)
                except (ValueError, IndexError):
                    # Log parsing error and continue
                    continue

        return installations

    def get_available_voivodeships(self) -> List[str]:
        """Get list of available voivodeships in the registry."""
        # Placeholder implementation
        return [
            "mazowieckie",
            "wielkopolskie",
            "malopolskie",
            "slaskie",
            "lubelskie",
            "dolnoslaskie",
            "podkarpackie",
            "lodzkie",
            "zachodniopomorskie",
            "kujawsko-pomorskie",
            "pomorskie",
            "warminsko-mazurskie",
            "swietokrzyskie",
            "podlaskie",
            "opolskie",
            "lubuskie",
        ]

    def __enter__(self) -> RESRegistryScraper:
        """Context manager entry."""
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Context manager exit."""
        self.session.close()
