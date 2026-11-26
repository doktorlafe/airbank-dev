# 01 – Kurzy měn

## O čem to je
Nástroj, který stáhne aktuální kurzovní lístek Air Bank a porovná ho s oficiálním kurzem ČNB.
Ukáže, jakou přirážku (spread) banka účtuje, a spočítá, kolik dostanu při směně konkrétní částky.

## Funkce
- `kurzy` – tabulka všech měn (nákup / prodej / střed / ČNB)
- `kurzy EUR` – detail jedné měny
- `kurzy prevod 500 EUR` – přepočet částky oběma směry
- výpočet spreadu v % oproti ČNB
- ukládání historie do SQLite → jednoduchý graf vývoje

## Technologie
- Python 3 + `httpx`, `rich` (hezký výpis v terminálu)
- ČNB: veřejný denní kurz (`cnb.cz/.../denni_kurz.txt`)
- SQLite pro historii

## Zdroje dat
- Air Bank Public API – FX rates
- ČNB denní kurzy (bez klíče)

## Co se naučím
Práce s REST API, autentizace API klíčem, parsování JSON, CLI aplikace.

## Stav
☐ API klíč ☐ prozkoumat endpoint ☐ CLI výpis ☐ porovnání s ČNB ☐ historie

## Spuštění
```bash
python3 -m kurzy              # tabulka všech měn
python3 -m kurzy list EUR     # jedna měna
python3 -m kurzy prevod 100 USD
python3 -m unittest tests/test_kurzy.py
```
Bez závislostí (jen standardní knihovna Pythonu 3.10+).

Air Bank: `export AIRBANK_API_KEY=... AIRBANK_BASE_URL=...` a doplnit TODO v `kurzy/airbank.py`.

## Web
```bash
python3 -m kurzy.web                 # http://127.0.0.1:8000
docker compose up -d --build         # produkce, poslouchá jen na 127.0.0.1:8000
```
Endpointy: `/` stránka, `/api/rates` JSON, `/health`.

### Nasazení přes Cloudflare (doporučeno Tunnel – bez otevřených portů)
```bash
cloudflared tunnel login
cloudflared tunnel create kurzy
cloudflared tunnel route dns kurzy kurzy.mojedomena.cz   # vytvoří DNS záznam
cloudflared tunnel run --url http://127.0.0.1:8000 kurzy
```
Alternativa: A záznam na VPS (proxied, oranžový mráček) + Caddy/nginx → 127.0.0.1:8000.

### Právní poznámky
- Kurzy ČNB jsou veřejné, zobrazovat je smíš.
- Air Bank data: před zveřejněním si přečti podmínky užití developer portálu.
- Nepoužívej logo/název Air Bank v doméně ani designu – web nesmí vypadat oficiálně.
