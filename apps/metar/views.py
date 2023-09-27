import requests
import re
from django.core.cache import cache
from apps.metar.http import MetarJsonResponse
from nws.env import CACHE_TIMEOUT_SECONDS, NWS_ROOT_URL


def get_metar_data(request) -> MetarJsonResponse:
    station = request.GET.get("scode")
    no_cache = request.GET.get("no-cache")
    if not station:
        metar_data = "Something awesome coming in"  # TODO: This must list the stations. Use:fetch_live_station_list()
    else:
        cached_metar = cache.get(f"station-{station}")
        if not cached_metar or no_cache == "1":
            metar_data = fetch_live_metar(station)
            if metar_data:
                cache.set(
                    f"station-{station}", metar_data, timeout=CACHE_TIMEOUT_SECONDS
                )
            else:
                return MetarJsonResponse(504, error="Could not fetch Live data!")
        else:
            metar_data = cached_metar
    return MetarJsonResponse(200, metar_data)


def fetch_live_metar(station) -> dict:
    try:
        api_url = NWS_ROOT_URL + f"{station}.TXT"
        response = requests.get(api_url)
        if response.status_code in [200, 304]:
            response_data = parse_metar(response.text)
        return response_data
    except Exception as e:
        return {}


def fetch_live_station_list():
    """
    Implement in V2
    """

    try:
        api_url = NWS_ROOT_URL
        response = requests.get(api_url)
        if response.status_code in [200, 304]:
            response_data = None
        return response_data
    except Exception as e:
        return None


def parse_metar(metar_string):
    """Parses a METAR string into a Python Dict

    Args:
      metar_string: A string containing the METAR data to be parsed.

    Returns:
      A Python dictionary containing the parsed METAR data.
    """
    parsed_metar = {}

    metar = metar_string.split("\n")
    date, metar = metar[0], metar[1].split(" ")

    parsed_metar["last_observation"] = date + "GMT"
    parsed_metar["station"] = metar[0]

    temperature_match = re.search(r"(\d{2})/(\d{2})", metar_string)
    if temperature_match:
        temperature_celsius = int(temperature_match.group(1))
        temperature_fahrenheit = temperature_celsius * 9 / 5 + 32
        parsed_metar[
            "temperature"
        ] = f"{temperature_celsius} C ({temperature_fahrenheit} F)"

    wind_match = re.search(r"(\d{3})(G\d{3})?KT", metar_string)
    if wind_match:
        wind_direction = wind_match.group(1)
        wind_speed = int(wind_match.group(2) or wind_match.group(1))
        wind_speed_mph = wind_speed * 1.1507794
        wind_speed_knots = wind_speed
        parsed_metar[
            "wind"
        ] = f"{wind_direction} at {wind_speed_mph} mph ({wind_speed_knots} knots)"

    return parsed_metar
