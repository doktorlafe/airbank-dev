import unittest

from kurzy import cnb, fio, kb
from kurzy.compare import convert, spread_pct
from kurzy.models import Rate

SAMPLE = """26.11.2026 #229
země|měna|množství|kód|kurz
EMU|euro|1|EUR|24,300
Japonsko|jen|100|JPY|15,500
"""


class T(unittest.TestCase):
    def test_parse(self):
        r = cnb.parse(SAMPLE)
        self.assertAlmostEqual(r["EUR"].mid, 24.3)
        self.assertAlmostEqual(r["JPY"].mid, 0.155)  # přepočet na 1 jednotku

    def test_spread(self):
        self.assertAlmostEqual(spread_pct(25.0, 24.0), 4.1666, places=3)

    def test_convert(self):
        r = Rate("EUR", mid=24.5, buy=24.0, sell=25.0)
        self.assertEqual(convert(100, r, to_czk=True), 2400)

    def test_kb(self):
        t = ('"curencyIso": "JPY", "currencyUnit": 100, "cashSell": 1, '
             '"nonCashBuy": 13.5, "middleCNB": 14, "nonCashSell": 14.5')
        r = kb.parse(t)["JPY"]
        self.assertAlmostEqual(r.buy, 0.135)
        self.assertAlmostEqual(r.sell, 0.145)

    def test_fio(self):
        t = '{&quot;z&quot;:&quot;CZK&quot;,&quot;c&quot;:&quot;EUR&quot;,&quot;n&quot;:25.1,&quot;p&quot;:23.7}'
        r = fio.parse(t)["EUR"]
        self.assertEqual((r.buy, r.sell), (23.7, 25.1))


if __name__ == "__main__":
    unittest.main()
