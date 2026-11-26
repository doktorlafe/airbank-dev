"""Komerční banka – kurzovní lístek (JSON vložený ve stránce)."""
import re

from .http import get
from .models import Rate

NAME = "Komerční banka"
URL = "https://www.kb.cz/cs/kurzovni-listek"
ITEM = re.compile(
    r'"curencyIso":\s*"(?P<code>[A-Z]{3})",\s*"currencyUnit":\s*(?P<unit>\d+),'
    r'.*?"nonCashBuy":\s*(?P<buy>[\d.]+),.*?"nonCashSell":\s*(?P<sell>[\d.]+)', re.S)


def parse(text: str) -> dict[str, Rate]:
    rates = {}
    for m in ITEM.finditer(text):
        unit = int(m["unit"])
        buy, sell = float(m["buy"]) / unit, float(m["sell"]) / unit
        if buy and sell:
            rates[m["code"]] = Rate(m["code"], (buy + sell) / 2, buy, sell, NAME)
    return rates


def fetch() -> dict[str, Rate]:
    return parse(get(URL))
