"""Denní kurz ČNB – veřejný, bez klíče."""
import urllib.request
from datetime import date, datetime, timedelta

from .models import Rate

URL = ("https://www.cnb.cz/cs/financni-trhy/devizovy-trh/"
       "kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt")


def parse(text: str) -> dict[str, Rate]:
    lines = text.strip().splitlines()
    day = datetime.strptime(lines[0].split()[0], "%d.%m.%Y").date()
    rates = {}
    for line in lines[2:]:  # 0 = datum, 1 = hlavička
        _country, name, amount, code, rate = line.split("|")
        mid = float(rate.replace(",", ".")) / int(amount)
        rates[code] = Rate(code=code, mid=mid, source="ČNB", day=day,
                           name=name)
    return rates


def fetch(day: date | None = None, timeout: float = 10) -> dict[str, Rate]:
    url = URL + (f"?date={day:%d.%m.%Y}" if day else "")
    with urllib.request.urlopen(url, timeout=timeout) as r:
        return parse(r.read().decode("utf-8"))


def fetch_previous(current: date) -> dict[str, Rate]:
    """Poslední kurzovní lístek před `current` (přeskočí víkendy a svátky)."""
    for back in range(1, 8):
        rates = fetch(current - timedelta(days=back))
        if next(iter(rates.values())).day < current:
            return rates
    return {}
