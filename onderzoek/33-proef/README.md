# Bewijs bij de Codex-proef van #33

Nieuwe uitvoering op 6 oktober 2026, geen heretikettering van Claude-bewijs.
C0/C1, approved-design.md, echte planner-C2 en C4 bewaren de opdracht en
concrete vergelijking met het bestaande menselijke akkoord. Run-JSON bevat
threadidentificatie, sandbox, uitgevoerde commando's en letterlijke testuitkomsten.
Ruwe modelgesprekken en accountgegevens worden niet gepubliceerd.

De tijdelijke Git-repository en commits staan in basis.json en C5/C6. Duurzame
snapshots boekenplank-build.py en latere negatieve/herstelsnapshots houden het
Python-gedrag leesbaar wanneer die tijdelijke repository verdwijnt. Kopieer een
snapshot als boekenplank.py naar een aparte map met controleer.py en voer daar
`python3 -B controleer.py werk volledig` uit. Groen verwacht bij hoofdproduct;
negatieve versie faalt op S4. Dit is Python-reproductie, geen nieuwe modelrun.

review-incompleet.md/json bewaart de eerste gestopte review wegens een ontbrekend
commitveld, zonder verdict of onderzocht criterium. De gecorrigeerde C5 krijgt
een nieuwe initial reviewer; deze stop is geen geslaagde beoordeling.

Installatiecontrole: `python3 onderzoek/33-proef/controleer_installatie.py` maakt
eigen tijdelijke fixtures; installatie-resultaten.json bevat echte observaties.
AGENTS-proef.md bewaart de bytes van de tijdelijke AGENTS.md onder een
snapshotnaam; zij wordt hier niet als nieuwe projectingang geladen.
PROJECT.md bewaart de proefnormen, geen nieuwe repositorynormen.
Geen studentvalidatie, productie-installatie of native GitHub-review geclaimd.

[Hoofd-C5](C5-main.md)/[C6](C6-main.md): SHIP op exact genoemd productcommit.
[Negatieve C5](C5-negatief.md)/[C6](C6-negatief.md): echte BLOCK op S4.
[Herstelstand](negatief-herstelstand.json) vóór reparatie opgeslagen;
[herstel-C5](C5-herstel.md)/[C6](C6-herstel.md): verse repair-review SHIP,
B1 opgelost. Model-/configuratiegrenzen staan in [run-config.json](run-config.json);
expliciete afzonderlijke rolinvoer in [run-inputs.json](run-inputs.json).
