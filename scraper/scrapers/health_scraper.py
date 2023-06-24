import requests
from dataclasses import dataclass
import json
import asyncio
from bs4 import BeautifulSoup
from .URLS import URLS
from .scraper_base import ScraperBase


class HealthStatistics(ScraperBase):
    def __init__(
        self, country: str = None, state: str = None, city: str = None
    ) -> None:
        super().__init__(country, state, city)
