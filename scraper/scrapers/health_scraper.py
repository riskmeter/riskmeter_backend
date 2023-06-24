from .scraper_base import GoogleScraper
import requests
from bs4 import BeautifulSoup

from .URLS import URLS


class HealthStatistics(GoogleScraper):
    def __init__(
        self, country: str = None, state: str = None, city: str = None
    ) -> None:
        super().__init__(country, state, city)

    def corona_cases(self):
        return requests.get(f"{URLS.COVID}{self.country}?strict=true").json()

    def flu_cases(self):
        return requests.get(f"{URLS.COVID}{self.country}?strict=true").json()
