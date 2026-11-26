from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Rate:
    """Kurz za 1 jednotku cizí měny v CZK."""
    code: str
    mid: float                   # střed (ČNB)
    buy: float | None = None     # banka od vás kupuje (dostanete CZK)
    sell: float | None = None    # banka vám prodává (platíte CZK)
    source: str = ""
    name: str = ""
    day: date | None = None
