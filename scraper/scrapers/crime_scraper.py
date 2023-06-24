import asyncio

from .scraper_base import GoogleScraper
from .utils import await_func


class CrimeStatistics(GoogleScraper):
    def __init__(
        self, country: str = None, state: str = None, city: str = None
    ) -> None:
        super().__init__(country, state, city)

    @await_func
    async def fetch_theft_links(self):
        await self.query_request("theft")
        return await self.get_links()

    @await_func
    async def fetch_murder_links(self):
        await self.query_request("murder")
        return await self.get_links()

    @await_func
    async def get_crime_rate(self):
        ...

    @await_func
    async def get_theft_rate(self):
        ...

    @await_func
    async def get_tourists_crimes(self):
        ...

    @await_func
    async def get_murder_rates(self):
        ...
