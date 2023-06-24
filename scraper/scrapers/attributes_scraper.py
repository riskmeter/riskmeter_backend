import json
import requests
from .scraper_base import GoogleScraper
from .URLS import URLS


class Attributes(GoogleScraper):
    def __init__(
        self, country: str = None, state: str = None, city: str = None
    ) -> None:
        super().__init__(country, state, city)

    def time_formed(self):
        return json.loads(requests.get(f"{URLS.TIME}/{self.country}/{self.city}").text)[
            "datetime"
        ]

    def time_ip(self):
        return json.loads(requests.get(f"{URLS.TIME_IP}").text)["datetime"]
