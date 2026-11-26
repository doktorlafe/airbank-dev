from .models import Rate


def spread_pct(bank_price: float, mid: float) -> float:
    """O kolik % je cena banky vzdálená od středu ČNB."""
    return (bank_price - mid) / mid * 100


def convert(amount: float, rate: Rate, to_czk: bool) -> float:
    """to_czk=True: prodávám cizí měnu bance (buy). Jinak kupuji (sell)."""
    if to_czk:
        return amount * (rate.buy or rate.mid)
    return amount / (rate.sell or rate.mid)
