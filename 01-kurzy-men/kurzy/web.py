"""Jednoduchý web: python3 -m kurzy.web  → http://localhost:8000"""
import json
import os
import string
import time
from pathlib import Path
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from . import airbank, cnb, fio, kb
from .compare import spread_pct

CACHE_TTL = 600  # s – ČNB vydává kurz 1× denně, nezatěžujeme zdroje
_cache = {"t": 0.0, "data": None}
BANKS = [kb, fio, airbank]
POPULAR = ["EUR", "USD", "GBP", "CHF", "PLN", "HUF", "JPY"]
TEMPLATE = string.Template(
    (Path(__file__).parent / "templates" / "index.html").read_text("utf-8"))


def get_rates():
    if _cache["data"] is None or time.time() - _cache["t"] > CACHE_TTL:
        c = cnb.fetch()
        try:
            prev = cnb.fetch_previous(next(iter(c.values())).day)
        except OSError:
            prev = {}
        a = {}
        for bank in BANKS:
            try:
                a[bank.NAME] = bank.fetch()
            except airbank.NotConfigured:
                pass
            except Exception as e:  # výpadek jedné banky nesmí shodit web
                print(f"{bank.NAME}: {e!r}", flush=True)
        _cache.update(t=time.time(), data=(c, prev, a))
    return _cache["data"]


def rows(c, prev, a):
    codes = POPULAR + sorted(set(c) - set(POPULAR))
    out = []
    for code in codes:
        if code not in c:
            continue
        r, p = c[code], prev.get(code)
        banks = {name: {"buy": round(b.buy, 4), "sell": round(b.sell, 4),
                        "spread": round(spread_pct(b.sell, r.mid), 2)}
                 for name, rates in a.items() if (b := rates.get(code))}
        out.append({"code": code, "name": r.name, "cnb": round(r.mid, 4),
                    "change": p and round(spread_pct(r.mid, p.mid), 2),
                    "banks": banks})
    return out


def render(c, prev, a):
    day = next(iter(c.values())).day
    prev_day = next(iter(prev.values())).day if prev else None
    meta = {"day": day.strftime("%-d. %-m. %Y"),
            "prevDay": prev_day and prev_day.strftime("%-d. %-m."),
            "banks": list(a)}
    js = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
    return TEMPLATE.substitute(data=js(rows(c, prev, a)), meta=js(meta))


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            c, prev, a = get_rates()
        except Exception:
            return self._send(503, "text/plain", "Zdroj kurzů je nedostupný.")
        if self.path == "/api/rates":
            return self._send(200, "application/json", json.dumps(rows(c, prev, a), ensure_ascii=False))
        if self.path in ("/", "/index.html"):
            return self._send(200, "text/html", render(c, prev, a))
        if self.path == "/health":
            return self._send(200, "text/plain", "ok")
        self._send(404, "text/plain", "Nenalezeno")

    def _send(self, code, ctype, text):
        b = text.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Cache-Control", "public, max-age=300")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)


def main():
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "8000"))
    print(f"http://{host}:{port}")
    ThreadingHTTPServer((host, port), Handler).serve_forever()


if __name__ == "__main__":
    main()
