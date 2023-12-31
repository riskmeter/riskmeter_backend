from .scraper_base import GoogleScraper


class FraudStatistics(GoogleScraper):
    def __init__(
        self, country: str = None, state: str = None, city: str = None
    ) -> None:
        super().__init__(country, state, city)
