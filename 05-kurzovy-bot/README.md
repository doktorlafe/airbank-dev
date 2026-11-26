# 05 – Kurzový Telegram bot

## O čem to je
Telegram bot, který hlídá kurzy měn (logika z projektu 01) a sám se ozve,
když kurz překročí nastavenou hranici. Praktické před dovolenou nebo nákupem v cizí měně.

## Příkazy
- `/kurz EUR` – aktuální kurz Air Bank + ČNB
- `/prevod 200 USD` – přepočet
- `/hlidej EUR < 24.50` – upozornění při dosažení hranice
- `/hlidani` – seznam aktivních hlídání, `/zrus <id>`
- `/denne 8:00` – ranní souhrn vybraných měn

## Technologie
- Python 3 + `python-telegram-bot` (nebo `aiogram`)
- plánovač (APScheduler) – kontrola kurzů každých N minut
- SQLite: uživatelé, hlídání, historie
- běh 24/7: Docker na VPS (systemd / docker compose)

## Zdroje dat
- Air Bank Public API – FX rates
- ČNB denní kurzy

## Co se naučím
Boti, asynchronní Python, plánované úlohy, provoz služby na serveru.

## Stav
☐ bot token (BotFather) ☐ /kurz ☐ hlídání ☐ denní souhrn ☐ nasazení
