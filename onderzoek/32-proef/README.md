# Bewijs bij de Claude Code-proef van #32

Dit is een nieuwe uitvoering op 6 oktober 2026, geen fictief casusdossier.
CLI/configuratie en grenzen staan in [run-config.json](run-config.json);
menselijke bronnen in [C4.md](C4.md). De ruwe providertranscripten blijven buiten
het gepubliceerde dossier. De run-JSON-bestanden bewaren alleen geselecteerde
technische gebeurtenissen, delegatie-invoer voor review en echte testuitkomsten.

[Hoofd-C5](C5-main.md) en [hoofd-C6](C6-main.md) horen bij de exacte lokale
proefcommit die zij noemen. De code staat in [boekenplank-build.py](boekenplank-build.py).
De gitgeschiedenis blijft in de tijdelijke proefrepository; de snapshots en
uitvoer blijven hier leesbaar wanneer die tijdelijke map verdwijnt.
[Negatieve C5](C5-negatief.md) en [negatieve C6](C6-negatief.md) beoordelen de
bewust geïnjecteerde [A-versie](boekenplank-negatief.py).
De [herstelstand](negatief-herstelstand.json) is vóór reparatie opgeslagen.
[Herstel-C5](C5-herstel.md) en [verse herstel-C6](C6-herstel.md) beoordelen
[de reparatie](boekenplank-herstel.py): SHIP WITH NITS, beide blockers opgelost.
De niet-blokkerende regressiepunten zijn vervolgwerk
[#58](https://github.com/misja/agent-role-loop/issues/58).

De aangeleverde [controle](controleer.py) is ongewijzigd.
[Extra controle](controleer_extra.py) voert de goedgekeurde AC5/6 uit; dit is
ondersteuning van de proef, geen wijziging van de aangeleverde productsuite.
Om een snapshot opnieuw te controleren: kopieer haar als `boekenplank.py` naar
een aparte tijdelijke map, voeg beide controlebestanden toe en voer daar
`python3 -B controleer.py werk volledig` en
`python3 -B controleer_extra.py` afzonderlijk uit. Groen verwacht voor de
hoofdsnapshot; de negatieve snapshot faalt op S4. Dit herhaalt Python-gedrag,
geen nieuwe provideruitvoering of menselijke toestemming.

De installatiecontrole haalt de snippets rechtstreeks uit de adapter-README:
`python3 onderzoek/32-proef/controleer_installatie.py`. Zij maakt eigen tijdelijke
fixtures en test behoud van bestaande bytes, conflicten, hashes en rollback.
[Installatieresultaten](installatie-resultaten.json) zijn echte observaties.
Geen studentwaarneming, productie-uitrol of native GitHub-review aangetoond.
