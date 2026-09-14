# Overdrachten bij het boekenplankfilter

Dit is een geconstrueerd onderwijsvoorbeeld. De personen Mira (opdrachtgever),
Sam (bouwer) en Robin (beoordelaar) zijn fictief. Hun besluiten en beoordelingen
hieronder zijn geschreven voorbeeldteksten, geen uitgevoerde agentrun of echte
menselijke goedkeuring. De code en testuitkomsten zijn wel controleerbaar.

## Leeswijzer en versieregister

`W1` is de opdracht, `P1` het geaccepteerde plan. `A` en `B` zijn leeslabels voor
codebestanden in deze bundel, **geen commit-ID's**. De basis is
`boekenplank_basis.py`; A staat in `boekenplank_a.py`, B in `boekenplank_b.py`.
`basis-naar-a.patch` en `a-naar-b.patch` zijn de wijzigingen. Bij eigen uitvoering
vervang je deze labels in de overdrachten door de werkelijke volledige SHA's,
issue-/PR-URL's en besluitlinks. `git rev-parse HEAD` geeft de huidige SHA.

De procesbasis van dit voorbeeld is agent-role-loop commit
`ae561f50a45ca42967e4687434cf0d2e8d4f5827`: `core/loop.md` en de genoemde contracten.
De bundel bevat die core onder `normen/core/`. Projectafspraken voor dit
miniatuurvoorbeeld: Python 3.10 of nieuwer, alleen standaardbibliotheek,
S1-S4 hieronder, geen opslag of CLI. Dit document is versie 1 van het scenario;
het is geen backlog voor agent-role-loop. De echte werkitems blijven op GitHub.

| Moment | Geldige opdracht / besluit | Beoordeelde code | Volgende stap |
|---|---|---|---|
| P1 vrijgegeven | W1, C4-P1 hieronder | Nog geen | Bouwer voert P1 uit |
| Eerste oplevering | W1, C4-P1 | A, C5-A | Onafhankelijke beoordeling |
| Blokkade | W1, C4-P1 | A, C6-A BLOCK | Eén gerichte reparatie en herbeoordeling |
| Herstel gereed | W1, C4-P1 | B, C6-B SHIP | Mens beslist over merge |
| Merge in het verhaal | W1, C4-P1 en besluit M1 | B | Issue sluiten en voortgang bijwerken |
| Zijpad P2 | W2/P2 is voorstel, C4-P2 STOP | B is alleen tegen W1/P1 beoordeeld | Niet bouwen aan sortering; nieuw menselijk besluit nodig |

## C0-W1: Toon alleen beschikbare boeken

### Aanleiding

Een medewerker wil zien welke boeken nu kunnen worden uitgeleend. De bestaande
methode `lijst()` geeft ook uitgeleende boeken terug. De medewerker wil deze
kunnen wegfilteren zonder de registratie te veranderen.

### Gewenste uitkomst

De boekenplank kan een lijst van alleen beschikbare boeken geven. Het bestaande
overzicht van alle boeken blijft bruikbaar.

### Acceptatiecriteria

- S1: `lijst()` zonder argument geeft alle boeken in toevoegvolgorde terug.
- S2: `lijst(alleen_beschikbaar=True)` geeft alleen beschikbare boeken in toevoegvolgorde.
- S3: een lege plank of een plank zonder beschikbare boeken geeft een lege lijst.
- S4: filteren verandert de verzameling boeken en hun uitleenstatus niet.

### Randvoorwaarden en omvang

Behoud bestaande aanroepen van `lijst()`. Geen CLI, opslag, reserveringen of
extra dependencies. Omvang S.

## C1: Route en toewijzing

**Besluit:** PLANNED. Een optioneel argument wijzigt de publieke interface;
een klein plan legt gedrag en verificatie vast voordat er gebouwd wordt.

**Omvang:** S. **Risico:** het filter kan onbedoeld de interne verzameling wijzigen.
Andere afnemers of gedeelde systemen: geen in deze zelfstandige case.
**Proces-/projectbasis:** de vaste procescommit en projectafspraken in de leeswijzer.

**Verantwoordelijkheden:** orkestrator voert triage uit; planner onderzoekt de
basis en maakt P1; Sam bouwt; Robin beoordeelt onafhankelijk S1-S4. Geen aparte
verhelderaar: criteria, interface en testbare grens zijn afgebakend. Geen extra
perspectief of afzonderlijke feiteninventarisatie nodig.
**Toewijzing:** S1, S2, S3 en S4 naar Robin. Geen criteria elders.
**Menselijke poort:** Mira beslist over P1 vóór bouwen en later over merge.
**LIGHT-uitvoeringsbasis / afwijsadvies:** niet van toepassing.

**Herstelregistratie bij het issue:** bij start ontwerp 0, oplevering 0;
vóór reparatie A naar B ontwerp 0, oplevering 1. Deze twee historische standen
blijven herkenbaar. Een nieuwe sessie zet de teller niet terug.

## C2-P1: Bouwplan

**Samenvatting en doel:** voeg een optioneel filter aan `lijst()` toe dat alleen
de teruggegeven lijst beperkt. S1-S4 bepalen het gedrag.
**Buiten scope:** sortering, opslag, CLI en reserveringen.
**Huidige toestand:** `boekenplank_basis.py` retourneert een kopie van de lijst;
`Boek.uitgeleend_aan is None` betekent beschikbaar. Dit is in de meegeleverde
basiscode na te lezen.

**Aanpak:** `lijst(alleen_beschikbaar=False)` behoudt standaard het oude gedrag.
Bij `True` wordt de uitvoer geselecteerd op `uitgeleend_aan is None`, zonder
mutatie van de opgeslagen verzameling. Geen wijziging aan `Boek`.
**Interfacewijziging:** één optioneel argument; bestaande aanroepen blijven geldig.
**Bronnen en normen:** W1, basisbestand, proces-/projectbasis uit de leeswijzer.
**Herstelstand:** ontwerp 0, oplevering 0; bij herstel de C1-stand raadplegen.

### Eén wijziging: filter in lijst

**Bestanden:** `boekenplank.py` in de eigen oefenrepository en `controleer.py`.
De bundel bewaart de codeversies onder afzonderlijke namen voor vergelijking.

**Uitvoering:** voeg het argument toe, selecteer beschikbare boeken, controleer
het ongewijzigde gedrag en de toestand vóór/na filtering. Geen refactor buiten
deze methode.

**Criteria, controles en beoordelaar:**

| Criterium | Controle in controleer.py | Beoordelaar |
|---|---|---|
| S1 | test_s1_standaard_volgorde | Robin |
| S2 | test_s2_beschikbaar_in_volgorde | Robin |
| S3 | test_s3_leeg_of_alles_uitgeleend | Robin |
| S4 | test_s4_filter_verandert_geen_toestand | Robin |

**Verificatiemodel:** test-first bij eigen uitvoering: voer de relevante tests
vóór de wijziging uit, verklaar het falen, implementeer en controleer opnieuw.
De bundel bevat ook een bewust ontoereikende eerste oplevering A om te oefenen
met beoordeling. Dit is een afwijking in die voorbeeldoplevering, geen toegestaan
alternatief voor de S4-controle.

Commando's in de bundel: `python controleer.py a zwak` slaagt voor drie tests;
`python controleer.py a regressie` faalt op S4; `python controleer.py b volledig`
slaagt voor alle vier. In de eigen repository kies je `werk` als versie.
De controles onderzoeken alleen deze kleine in-memory-case.

**Risico:** een toewijzing aan `self._boeken` kan gegevens verwijderen. S4 moet
de toestand vergelijken, niet alleen controleren of de filteruitkomst klopt.
**Aannames/open vragen:** geen buiten de beschreven case.
**Terugdraaien:** herstel de basisversie; er wordt geen opgeslagen data gemigreerd.
**Gereed wanneer:** S1-S4 aantoonbaar voldoen en onafhankelijk zijn beoordeeld;
Mira beslist over merge.

## C4-P1: Menselijk besluit in het voorbeeld

**Bron:** fictieve reactie van Mira bij P1, opgenomen in dit scenario.
**Artefact:** C2-P1, C0-W1, proces-/projectbasis uit de leeswijzer; geen C3 gekozen.
**Besluit:** PROCEED.
**Reden:** het filter helpt bij het kiezen van een beschikbaar boek en laat het
bestaande overzicht intact. De optionele parameter en controles zijn passend.
**Besloten:** toevoegvolgorde behouden; geen extra sortering.
**Vereiste wijzigingen / uitgestelde vragen:** geen.

## C5-A: Eerste oplevering

### Kern voor de beoordelaar

**Artefact:** W1/P1, versie A in `boekenplank_a.py`; diff `basis-naar-a.patch`.
Voor een echte overdracht: volledige codecommit en basiscommit vastleggen.
**Normen en besluit:** vaste proces-/projectbasis, C4-P1 hierboven; geen afwijkend
menselijk besluit. Alle criteria S1-S4 naar Robin.

**Wijziging:** optioneel argument toegevoegd; uitgeleende boeken uit de lijst
gefilterd. **Bestanden:** `boekenplank.py`; controle-invoer in `controleer.py`.
**Contract geraakt:** optioneel argument van `lijst()`, zoals toegestaan in P1.

**Bewijs:** `python controleer.py a zwak`: drie tests slagen, exitcode 0.
S1, S2 en S3 zijn hiermee op A gecontroleerd. **S4 is niet vastgesteld**: de
eerste oplevering heeft de toestand na het filteren niet gecontroleerd.
`bewijs.txt` bevat de werkelijk uitgevoerde reproductiecommando's en uitkomsten.
Geen bewijs voor opslag, CLI of andere code. Geen complete test-first-historie
van deze geconstrueerde versie beschikbaar.

**Afwijking:** vereiste S4-verificatie ontbreekt; niet door Mira toegestaan.
**Herstelstand:** ontwerp 0, oplevering 0. **Uitgestelde werkzaamheden:** geen.

### Uitgebreide auteursbijlage

Geen maaktranscript of verkenningsgeschiedenis in dit onderwijsvoorbeeld.

## C6-A: Beoordeling van de eerste oplevering

**Beoordelaar/toewijzing:** Robin, S1-S4. **Modus:** initial.
**Artefact/normbasis:** A en de proces-/projectbasis uit C5-A.
**Besluit:** BLOCK.

**Dekking:** S1-S3 pass voor de in de zwakke suite uitgevoerde situaties; het
bewijs is bij deze eerste beoordeling onderzocht. S4 fail: na filteren bevat
`self._boeken` het uitgeleende boek niet meer. De toewijzing in `lijst()` en de
ontbrekende controle onderbouwen de bevinding. Geen criteria elders belegd.
**Contract drift:** geen niet-gedeclareerde interfacewijziging; de uitvoering
schendt wel het afgesproken gedrag S4.

**Moet worden hersteld, R1/S4:** maak een plank met een beschikbaar en een
uitgeleend boek, filter, vraag daarna alle boeken op. Het uitgeleende boek is
verdwenen. Laat de interne lijst intact en voeg een regressiecontrole toe die
boeken én uitleenstatus vóór en na filtering vergelijkt.
**Niet-blokkerende opmerkingen:** geen. **Hersteluitkomst:** nog niet van toepassing.
**Volgende stap:** één gerichte reparatie en onafhankelijke herbeoordeling.

## Herstelbijlage A naar B

**Bijgewerkte kern:** C5-B hieronder. **Reparatiediff:** `a-naar-b.patch`.
**Eerdere blokkade:** R1/S4 uit C6-A. **Herstelstand:** ontwerp 0, oplevering 1,
vastgelegd vóór reparatie. Geen extra vervolgautorisatie nodig voor deze eerste
automatische ronde.

**Eerder vastgestelde dekking:** S1-S3 op A, in de situaties van de zwakke suite.
Omdat dezelfde methode verandert, controleert Robin deze drie opnieuw op B.
De eerdere bevindingen blijven als historische dekking herkenbaar; zij worden
niet gepresenteerd als nieuw bewijs voor B.

**Herstel:** een lokale lijst teruggeven in plaats van `self._boeken` overschrijven.
Reproduceer rood met `python controleer.py a regressie`, daarna groen met
`python controleer.py b volledig`. Geen nieuw doel of normkeuze.

## C5-B: Oplevering na herstel

### Kern voor de herbeoordelaar

**Artefact:** W1/P1, B in `boekenplank_b.py`; reparatie A..B in `a-naar-b.patch`.
De totale wijziging is basis..A plus A..B. Bij eigen uitvoering noteer je alle
volledige SHA's. **Normen/besluit:** dezelfde vaste basis en C4-P1; geen nieuwe
scope of afwijking. **Toewijzing:** S1-S4 naar Robin.

**Wijziging:** het filter retourneert een aparte lijst; de geregistreerde boeken
blijven behouden. **Bestanden:** `boekenplank.py`, `controleer.py` met S4-controle.
**Contract geraakt:** dezelfde optionele parameter als P1.

**Bewijs:** regressie op A faalt doordat boek 2 ontbreekt; volledige suite op B
slaagt, vier tests, exitcode 0. S1-S4 hebben ieder een benoemde test in P1.
Zie `bewijs.txt` voor waargenomen uitvoer. Beperkt tot de beschreven case.
**Afwijkingen/follow-ups:** geen. **Herstelstand:** ontwerp 0, oplevering 1;
herstelbijlage hierboven. **Uitgebreide auteursbijlage:** geen.

## C6-B: Herbeoordeling

**Beoordelaar/toewijzing:** Robin, S1-S4. **Modus:** repair.
**Artefact:** B; A..B-diff en herstelbijlage hierboven; ongewijzigde normbasis.
**Besluit:** SHIP.
**Dekking:** S1-S4 pass, opnieuw onderzocht op B. De vier tests controleren de
volgorde, selectie, lege resultaten en ongewijzigde toestand. De codelezing
bevestigt dat de interne lijst niet meer wordt overschreven. Eerdere dekking van
A is alleen als historische bron meegenomen. Geen criteria elders belegd.
**Contract drift / resterende blokkades / nits:** geen.
**Hersteluitkomst R1/S4:** opgelost. S1-S3 opnieuw gecontroleerd wegens gedeelde methode.
**Volgende stap:** Mira beslist over merge van B. Bij nog een blokkade zou de
verbruikte herstelronde een menselijke keuze voor begrensd vervolg, splitsen of
stoppen vragen; geen automatische tweede ronde.

## M1: Merge en afsluiting in het verhaal

Mira besluit expliciet B samen te voegen op basis van C6-B tegen W1/P1.
Na de merge wordt het issue gesloten en krijgt de bordkaart de afgeronde status.
Dit beschrijft een fictieve afloop. In je eigen project bewaar je de echte
besluitreactie en mergecommit. SHIP is op zichzelf geen mergeautorisatie.

## Zijpad: een gewijzigde opdracht P2

Deze variant begint bij B vóór M1 en staat los van de bovenstaande afloop.
Een nieuwe wens is alfabetische sortering van de beschikbare boeken.

**W2/P2, voorgesteld:** vervang S2 door alfabetische titelvolgorde; S1, S3 en S4
blijven behouden. Wijzig de filtertak en vervang de volgordetest voor S2.
P1, C4-P1 en C6-B worden niet overschreven. Er is nog geen nieuwe codecommit.
**C4-P2:** fictief besluit van Mira: STOP. Eerst vaststellen hoe hoofdletters en
gelijke titels moeten worden behandeld. B is alleen tegen W1/P1 beoordeeld;
het groene oordeel is geen bewijs voor de nieuwe sorteerwens.

**Volgende stap:** de open sorteervragen beantwoorden, P2 concreet aanvullen en
een nieuw menselijk besluit vastleggen voordat aan deze wijziging wordt gebouwd.
C1 moet de gewijzigde criteriumbasis noemen. S2 vraagt nieuw bewijs; S1/S3/S4
vragen een impactbeoordeling. De eerdere herstelstand wordt niet stilzwijgend
teruggezet. Dit is een voorstelzijpad, geen tweede voltooide route.
