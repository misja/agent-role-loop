# #49: uitvoering en bewijsgrenzen

## Besluit en normbasis

[C4 PROCEED](https://github.com/misja/agent-role-loop/issues/49#issuecomment-5983853764)
legt het gebruikersantwoord “akkoord” op C2 v1 in `onderzoek/49-plan.md` vast.
Het besluit geeft het tekstpakket voor modules 2–3 vrij, inclusief de
terugvalroute via de bestaande casus. Geen mergebesluit.

Proces- en projectnormbasis: `a94218adbe2ee03eb6476582fbae5ab9e9ceca85`.
C1/C2 en bronnen staan in `onderzoek/49-plan.md` en de
[startregistratie](https://github.com/misja/agent-role-loop/issues/49#issuecomment-5983772739).
Root plant en bouwt; één verse onafhankelijke reviewer beoordeelt AC1–7.
Herstelstand vóór initial review: ontwerp 0, oplevering 0.

## Gerichte wijzigingen

| Bronbevinding #46 | Uitvoering | Gevolg voor de lezer |
|---|---|---|
| 8–9: abstracte driedeling; prompt lijkt uitvoering | Module 2 organizer en les onderscheiden afspraak, prompt, werkelijke handeling en uitkomst. Concrete controle op voorbereide versie B. | De student kan instructie en werkelijk controlebewijs apart aanwijzen. |
| 10–11: tweede casus en dubbele analyse | Mermaid als optionele dropdown; één C5-A-analyse in de les, oefening verwijst ernaar en vraagt twee eigen analyses. | Bron, versie, vereiste, aangetroffen en ontbrekende informatie staan één keer uitgewerkt. |
| 12: groen als algemene verplichting | Module 3 index/les/oefening koppelen groen aan ingestelde verplichte controles. | Geen onvoorwaardelijke verplichting om ieder gereedschap te gebruiken. |
| 13: antwoorden vóór metingen | Les bevat conceptuitleg en kleine assertie; volledige defect-/drempelverklaring volgt in de oefening na de meetopdrachten. | De student bewaart eigen waarnemingen vóór vergelijking met de uitwerking. |
| 14: noteerhandeling onder uitleg, setup ontbreekt | Aparte drempelopdracht; Pythonstart met coverage, Ruff en mypy plus officiële bronnen; andere stacks selecteren eigen gereedschappen. | Handeling, startpunt en interpretatie blijven afzonderlijk vindbaar. |
| 15: zwaardere terugval | Nieuwe kopie van dezelfde casus, eigen poortoverzicht/drempel en gerichte lenerassertie. | Geen nieuwe zoekfunctie; bekende fout en kleinere bewijsreikwijdte expliciet. |

Module 1 is gerichte voorkennis. Het filtervoorbeeld is een in-memory-case,
geen CLI/opslaguitvoering van de eigen boekenplank. Rollen, besluiten en A/B
labels blijven geconstrueerd; werkelijk uitgevoerde controles krijgen afzonderlijk
waarnemingen. De les verwijst naar de historische C5-definitie op de procesbasis
van de bundel, naast de actuele referentie. Die historische definitie is gericht
via GitHub geraadpleegd en bevat de in de analysetabel genoemde bewijsvelden.

## Controlebewijs vóór onafhankelijke beoordeling

Verificatie: manual-with-expected-results voor passagelezing;
validation-workflow voor uitvoerbare controles, build en links. Geen nieuw
codegedrag of repositorytests: tijdelijke testwijziging controleert het reeds
bestaande onderwijsdefect. Voor/na betreft de leesroute hierboven, geen bewezen
verandering in studentbegrip.

Uitgevoerd in een afzonderlijke werkkopie, met de getoonde uv-setup:
Linux, Python 3.14.8, pytest 9.1.1, pytest-cov 7.1.0, coverage 7.16.2,
Ruff 0.16.10, mypy 2.4.0. Script en volledige uitvoer:
`/tmp/arl49-verify.py` en `/tmp/arl49-evidence.json` (tijdelijke sessielogs).
De onderstaande uitkomsten zijn het blijvende beknopte bewijsregister.

| Invoer/actie | Verwachting | Waarneming |
|---|---|---|
| Originele casuskopie, pytest --cov=boekenplank --cov-report=term-missing | Zes pass, 100%, exit 0 | Zes pass, 27/27 regels, 100%, exit 0. |
| Dezelfde suite met -k 'not terug_maakt_boek_weer_beschikbaar' | Vijf pass, twee ontbrekende regels, ongeveer 93%, exit 0 | Vijf pass, één deselected, regels 52–53 ontbreken, 25/27 regels, rapport 93%, exit 0. |
| Dezelfde selectie met --cov-fail-under=95 | Vijf pass, coverageblokkade, niet-nul exit | Vijf pass, 92,59% onder 95%, exit 1. |
| Volledige suite opnieuw | Oorspronkelijke zes pass | Zes pass, 100%, exit 0. |
| Ruff check boekenplank.py; mypy boekenplank.py | Tool kan code onderzoeken en uitslag tonen | Beide exit 0; lint/typechecks vinden geen problemen binnen hun configuratie. |
| Tijdelijke extra assertie op uitgeleend_aan == "Misja" na tweede uitlening | Falende assertie door Bob | Eén fail, vijf pass, exit 1; 'Bob' != 'Misja', dekking nog 100%. |
| python3 teaching/cases/praktijk-projectomgeving/controleer.py b volledig | Vier pass, OK | S1 tot en met S4 pass, OK, exit 0. |

De eerste sandboxpoging kon niet naar de uv-cache schrijven; de uitvoering is
met goedgekeurde escalatie herhaald. Pakketinstallatie slaagde met een
hardlink-waarschuwing en terugval naar kopiëren. Dat is geen docs-buildwaarschuwing
of defect in de oefencontrole. De casusbestanden in de repository zijn intact.

Docs-build: `make -C docs html`, standaard `-W --keep-going`, geslaagd zonder
waarschuwingen. Lokale HTML-links/fragmenten van de zes gewijzigde pagina's:
`/tmp/arl49-links.py`, 463 controles, nul fouten. Finale productversie wordt in
C5 vastgelegd. `git diff --check` schoon. Casuscode, module 1, core en adapters
zijn bytegelijk aan de basis. Geen em/en-dash in gewijzigde moduleteksten.

Indexleeruitkomsten blijven op kunnen-verantwoorden gericht. Module 2
concretiseert de modulariteitsanalogie; module 3 preciseert de voorwaarde van
groen. Vaste lesstaarten en overgangen blijven, met aangepaste vindplaatsen.
Eigen oefening blijft twee analyses respectievelijk keuze van eigen geval;
terugval heeft een expliciet kleinere bewijsreikwijdte.

## Setupbronnen en grenzen

Officiële documentatie geraadpleegd op 4 oktober 2026:
[uv-installatie](https://docs.astral.sh/uv/getting-started/installation/),
[pytest-cov-configuratie](https://pytest-cov.readthedocs.io/en/latest/config.html),
[Ruff-installatie](https://docs.astral.sh/ruff/installation/) en
[mypy-start](https://mypy.readthedocs.io/en/stable/getting_started.html).
De commando's voor de Pythoncasus zijn daadwerkelijk uitgevoerd. Setup voor
andere talen/besturingssystemen is niet uitgevoerd; de tekst vraagt expliciet
stackgerichte documentatie of hulp van de docent vóór uitvoering.

Metingen vóór uitleg zijn geen onbeïnvloed experiment: casuscommentaren wijzen
het defect aan, en de les geeft conceptuele steun. De terugval bewijst uitvoering
van een bekende controle, geen zelfstandige ontdekking of toetsing van verdwenen
code. Behoud van de eerste lener bewijst niet de vereiste foutmelding. Groen
lint/typebewijs vindt het uitleendefect niet en bewijst geen algehele correctheid.
Studentwaarnemingen, leereffect en gemeten oefenduur zijn niet beschikbaar.
Geen echte modelrun, volledige review van studentcode of integrale externe
linkaudit uitgevoerd. Geen vormgeving gewijzigd of concreet weergaveprobleem:
geen screenshots, conform de geldende conventie.

## Onafhankelijke beoordeling

Volgt als C6 op een exacte productcommit. AC5 vraagt een eigen overdrachtsanalyse
én werkelijk uitgevoerde controle van de reviewer, met invoer, actie, verwachting,
waarneming en bewijsgrens. Dit is agentlezing, geen studentvalidatie.

## Finale C6

De verse onafhankelijke reviewer `/root/review49` geeft **SHIP** op
`cda455e238ca553d3668586e63b80ca44623f078`. AC1–7 zijn nieuw onderzocht,
zonder blockers of nits. De reviewer analyseerde zelfstandig C5-B tegen de
historische C5-contracttekst en voerde `controleer.py b volledig` werkelijk uit:
S1 tot en met S4 pass, OK, exit 0 op Linux/Python 3.14.8.

Invoer, actie, verwachting, waarneming en bewijsgrens zijn in de volledige C6
op #49 geregistreerd. De reviewer onderscheidt ontbrekende echte agentrun,
code-SHA en menselijke goedkeuring van de uitvoerbare voorbereide case.
De eigen linkcontrole bevestigt 463 lokale links/fragmenten zonder fouten;
diffcontrole schoon. Buildbewijs is door de reviewer gelezen, geen eigen
buildreproductie. Geen studentvalidatie of bewijs voor alle alternatieve stacks.

Herstelstand blijft ontwerp 0, oplevering 0; geen herstelronde nodig.
Met één reviewer is C6 finaal, zonder C7. PR #54 is gereed voor het menselijke
mergebesluit. GitHub meldt geen CI-checks; de docs-build is lokaal uitgevoerd.
Deze afrondingsregistratie wijzigt geen beoordeelde onderwijstekst.
