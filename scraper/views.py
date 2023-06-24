from django.http import HttpResponse, JsonResponse
from .scrapers.crime_scraper import CrimeStatistics
from .scrapers.attributes_scraper import Attributes
from .scrapers.health_scraper import HealthStatistics
from .scrapers.fraud_scraper import FraudStatistics


def index(request):
    if request.method == "GET":
        return HttpResponse("Hello, world. You're at the scraper index.", 200)


def time_formed(request):
    if request.method == "GET":
        return HttpResponse(
            f"time in brisbane: {Attributes(country='Australia', city='Brisbane', state='QLD').time_formed()}",
            200,
        )


def time_ip(request):
    if request.method == "GET":
        Attributes().time_ip()
        return HttpResponse(f"time in brisbane: {Attributes().time_ip()}", 200)


def crime(request, country, city):
    if request.method == "GET":
        crime = CrimeStatistics(country=country, city=city).all()

        return JsonResponse({"country": country, "city": city, "crime": crime})
