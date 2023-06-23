import requests
from dataclasses import dataclass
import json
import asyncio
from bs4 import BeautifulSoup


@dataclass
class URLS:
    REST_COUNTRIES = "https://restcountries.com/v2/"
    GEONAMES = "http://api.geonames.org/"
    BANK = "https://data.worldbank.org/"
    TIME = "http://worldtimeapi.org/api/timezone/"
    TIME_IP = "http://worldtimeapi.org/api/ip"
    CRIME = "https://andruxnet-world-cities-v1.p.rapidapi.com/"
    GOOGLE = "https://www.google.com/search?q"


class ScraperBase:
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
            requests.get(query).content for query in self.google_query(news_target)
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


class HealthStatistics:
    ...


class FraudStatistics:
    ...
