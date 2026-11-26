# 02 – Bankomaty a pobočky

## O čem to je
Vyhledávač nejbližšího bankomatu nebo pobočky Air Bank. Zadám adresu nebo souřadnice
a dostanu seřazený seznam podle vzdálenosti, s otevírací dobou a službami.

## Funkce
- `najdi "Dejvická 10, Praha"` – 5 nejbližších míst
- filtr: jen bankomaty / jen pobočky / bankomaty s vkladem
- výpočet vzdálenosti (haversine) a odkaz do Mapy.cz / Google Maps
- info „je teď otevřeno?“ podle otevírací doby
- lokální cache dat (mění se zřídka) – méně volání API

## Technologie
- Python 3 + `httpx`
- geokódování adresy: Nominatim (OpenStreetMap) nebo Mapy.cz API
- JSON cache s expirací 24 h

## Zdroje dat
- Air Bank Public API – branches, ATMs

## Co se naučím
Geodata, výpočet vzdáleností, cachování, práce s otevírací dobou a časovými zónami.

## Stav
☐ stáhnout data ☐ geokódování ☐ řazení podle vzdálenosti ☐ filtry ☐ „otevřeno teď“
