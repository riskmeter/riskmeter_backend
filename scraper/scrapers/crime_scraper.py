import asyncio

from .scraper_base import GoogleScraper
from .utils import await_func


class CrimeStatistics(GoogleScraper):
    def __init__(
        self, country: str = None, state: str = None, city: str = None
    ) -> None:
        super().__init__(country, state, city)

    @await_func
    async def fetch_links(self):
        _ = GoogleScraper(self.country, self.state, self.city)
        await _.query_request("theft")
        return await _.get_links()

    @await_func
    async def get_crime_rate(self):
        ...
