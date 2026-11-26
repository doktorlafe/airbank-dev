"""Air Bank Public API – FX rates.

TODO: doplnit podle dokumentace na developers.airbank.cz (Public API):
  - BASE_URL a cestu k endpointu kurzů
  - název hlavičky s API klíčem
  - mapování JSON odpovědi v parse()
"""
import json
import os
import urllib.request

from .models import Rate

NAME = "Air Bank"
BASE_URL = os.environ.get("AIRBANK_BASE_URL", "")      # TODO
RATES_PATH = "/TODO/fx-rates"                          # TODO
API_KEY_HEADER = "apiKey"                              # TODO ověřit


class NotConfigured(RuntimeError):
    pass


def parse(data) -> dict[str, Rate]:
    # TODO: upravit podle skutečného tvaru odpovědi
    rates = {}
    for item in data:
        code = item["currency"]
        buy, sell = float(item["buy"]), float(item["sell"])
        rates[code] = Rate(code=code, mid=(buy + sell) / 2,
                           buy=buy, sell=sell, source="Air Bank")
    return rates


def fetch(timeout: float = 10) -> dict[str, Rate]:
    key = os.environ.get("AIRBANK_API_KEY")
    if not key or not BASE_URL or "TODO" in RATES_PATH:
        raise NotConfigured("Air Bank API není nastavené "
                            "(AIRBANK_API_KEY, AIRBANK_BASE_URL, endpoint).")
    req = urllib.request.Request(BASE_URL + RATES_PATH,
                                 headers={API_KEY_HEADER: key,
                                          "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return parse(json.load(r))
