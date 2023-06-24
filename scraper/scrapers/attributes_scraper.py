import requests
from dataclasses import dataclass
import json
import asyncio
from bs4 import BeautifulSoup
from .URLS import URLS
from .scraper_base import ScraperBase


class Attributes(ScraperBase):
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
