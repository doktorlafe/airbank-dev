# 04 – Sazka terminály

## O čem to je
Air Bank umožňuje vkládat a vybírat hotovost na terminálech Sazka (trafiky, večerky).
Nástroj najde terminály v okolí a ukáže, kde se dá co udělat a kdy je otevřeno.

## Funkce
- vyhledání terminálů v okruhu X km od adresy / polohy
- filtr podle typu operace (vklad / výběr), pokud to API poskytuje
- otevírací doba provozovny, „otevřeno teď“
- porovnání: je blíž bankomat (projekt 02), nebo Sazka terminál?
- export do GPX/KML pro navigaci

## Technologie
- Python 3, sdílený kód s projektem 02 (geokódování, vzdálenosti)
- případně vyčlenit společnou knihovnu `common/`

## Zdroje dat
- Air Bank Public API – Sazka terminals
- Banking Extension API zmiňuje „Sazka codes“ – to je pro klienty, zde nevyužito

## Co se naučím
Znovupoužití kódu mezi projekty, export geodat.

## Stav
☐ stáhnout data ☐ vyhledávání v okruhu ☐ porovnání s bankomaty ☐ export GPX
