"""Fio banka – devizové konverze (JSON vložený ve stránce)."""
import html
import re

from .http import get
from .models import Rate

NAME = "Fio banka"
URL = "https://www.fio.cz/akcie-investice/dalsi-sluzby-fio/devizove-konverze"
# {"z":"CZK","c":"EUR","n":25.17,"p":23.73}  → 1 EUR: banka prodává za n, kupuje za p
PAIR = re.compile(r'\{"z":"CZK","c":"([A-Z]{3})","n":([\d.]+),"p":([\d.]+)\}')


def parse(text: str) -> dict[str, Rate]:
    rates = {}
    for code, sell, buy in PAIR.findall(html.unescape(text)):
        buy, sell = float(buy), float(sell)
        rates[code] = Rate(code, (buy + sell) / 2, buy, sell, NAME)
    return rates


def fetch() -> dict[str, Rate]:
    return parse(get(URL))
