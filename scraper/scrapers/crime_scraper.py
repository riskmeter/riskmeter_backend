import requests
from dataclasses import dataclass
import json
import asyncio
from bs4 import BeautifulSoup
from .URLS import URLS
from .scraper_base import ScraperBase


class CrimeStatistics(ScraperBase):
    """
    statistics pointing to crimes occurred within 2 months till DOQ
    - theft
    - gang activity
    - discriminatory activity
    lets just start with theft
    """

    def __init__(
        self, country: str = None, state: str = None, city: str = None
    ) -> None:
        super().__init__(country, state, city)

    async def fetch_links(self):
        target = ScraperBase(self.country, self.state, self.city)
        await target.query_request("theft")
        return await target.get_links()

    def all(self):
        return asyncio.run(self.fetch_links())
