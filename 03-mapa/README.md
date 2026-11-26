# 03 – Interaktivní mapa

## O čem to je
Webová stránka s mapou ČR, na které jsou všechny pobočky, bankomaty Air Bank
a Sazka terminály. Vizuální nadstavba nad projekty 02 a 04.

## Funkce
- mapa s barevně odlišenými značkami (pobočka / bankomat / Sazka)
- shlukování značek při oddálení (marker clustering)
- přepínače vrstev a filtr služeb
- tlačítko „moje poloha“ → zvýraznění nejbližších míst
- popup s adresou, otevírací dobou a navigací
- statistiky: počet míst po krajích

## Technologie
- Frontend: HTML + JS, Leaflet + OpenStreetMap, Leaflet.markercluster
- Backend: malý proxy server (Python FastAPI), který drží API klíč
  (klíč nesmí být ve frontendu!) a cachuje data
- nasazení: Docker, případně vlastní VPS

## Zdroje dat
- Air Bank Public API – branches, ATMs, Sazka terminals

## Co se naučím
Webové mapy, bezpečné skrytí API klíče za backend, Docker nasazení.

## Stav
☐ backend proxy ☐ mapa s body ☐ clustering ☐ filtry ☐ geolokace ☐ nasazení
