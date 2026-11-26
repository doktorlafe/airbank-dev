# 06 – PSD2 sandbox (průzkumný)

## O čem to je
Pokus vyzkoušet „opravdové“ open banking API – přihlášení klienta přes OAuth2
a čtení účtů/transakcí – na **testovacích** datech. Bez klientství Air Bank
je to možné jen pokud portál nabízí sandbox s fiktivními klienty.

## Krok 0 – ověřit dostupnost
- projít Documentation → AISP API: je tam sandbox URL / testovací uživatelé?
- jde v Applications registrovat aplikaci pro sandbox bez eIDAS certifikátu?
- pokud ne → přejít na sandbox jiné banky (Česká spořitelna, ČSOB, KB mají veřejné sandboxy)

## Funkce (pokud sandbox existuje)
- kompletní OAuth2 Authorization Code flow (redirect, výměna kódu za token, refresh)
- AISP: seznam účtů, zůstatky, transakce
- CISP: dotaz „je na účtu dost peněz na X Kč?“
- jednoduchý přehled výdajů podle kategorií z testovacích transakcí

## Technologie
- Python FastAPI (redirect endpoint pro OAuth)
- `authlib` pro OAuth2
- bezpečné uložení tokenů (ne v gitu, `.env`)

## Co se naučím
OAuth2 v praxi, PSD2/open banking standardy, práce s citlivými daty.

## Stav
☐ ověřit sandbox ☐ registrace aplikace ☐ OAuth flow ☐ AISP ☐ CISP
