import asyncio

import requests
from bs4 import BeautifulSoup

from .URLS import URLS


class GoogleScraper:
    def __init__(
        self, country: str = None, state: str = None, city: str = None
    ) -> None:
        self.country = country
        self.state = state
        self.city = city
        self.data: list = []

    def google_query(self, news_target):
        country_crime_query = f"{URLS.GOOGLE}={self.country}+{news_target}"
        city_crime_query = f"{URLS.GOOGLE}={self.city}+{news_target}"
        state_crime_query = f"{URLS.GOOGLE}={self.state}+{news_target}"
        return [country_crime_query, city_crime_query, state_crime_query]

    async def query_request(self, news_target):
        self.data = [
            requests.get(
                query,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-US,en;q=0.9,lt;q=0.8,et;q=0.7,de;q=0.6",
                },
            ).content
            for query in self.google_query(news_target)
        ]
        self.news_target = news_target

        await asyncio.sleep(2)

    async def get_links(self):
        records: set[dict[str, str]] = []
        for response in self.data:
            html = BeautifulSoup(response, "html.parser")
            all_links = html.find_all("a")
            for links in all_links:
                if h3 := links.find("h3"):
                    records.append(
                        {
                            "link": (links["href"]).strip("/url?q="),
                            "title": h3.text,
                        }
                    )
        return records
