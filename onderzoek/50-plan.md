# #50: oordelen en menselijke besluiten concreet maken

Status: C1 en C2 v1, voorstel vóór bouw. C0 en overdrachten:
[issue #50](https://github.com/misja/agent-role-loop/issues/50).

## C1: triage

- Route PLANNED, omvang M: twee samenhangende modules met zes concrete
  bronbevindingen; één reviewbaar tekstpakket.
- Proces-/normbasis: `b6ddcd55fbb9de37db316a626d0ddee4afe703e9`.
  Leesbare grondslag: `CLAUDE.md`, `core/loop.md`, rolprompts en contracten;
  `teaching/conventies.md`, `doelgroep.md`, `schrijfwijzer.md`, `begrippen.md`.
  Relevante secties: voortbouwen op eerdere uitleg, nieuwe toepassing,
  tekstfuncties, bewijsgrenzen, modulestramien en controles bij tekstwerk.
- Bord gelezen: #46/#48/#49 Done; #50 Backlog. Modules 1–3 en hun nieuwe
  contract-/bewijsuitleg zijn gemerged. Geen bestaand bouwbesluit voor #50.
- Root orkestreert, onderzoekt, plant en bouwt na C4. Eén verse onafhankelijke
  reviewer `/root/review50` voor AC1–7: onderwijslezing, C6/C7-routing,
  menselijke besluitgrenzen en technische casuslezing. Alle criteria aan deze
  reviewer; geen criteria elders. Hij krijgt C5, exacte productcommit, normen
  en besluiten zonder maaktranscript of andere oordelen.
- Geen aparte verhelderaar of inventarisatie: bronbevindingen zijn concreet;
  onderstaande scenario's en verificatie begrenzen de ontwerpkeuzes.
- Risico: pass op een onderzoeksopdracht kan softwaregoedkeuring suggereren;
  een verzonnen gebruikseis kan als historische eis worden gelezen;
  arbitrage kan een menselijke doelkeuze gaan overnemen.
- Herstelstand ontwerp 0, oplevering 0; dit document en #50 bewaren de stand.
  Vóór eventuele ronde teller en criteriumgebonden bevindingen op #50 vastleggen.
- LIGHT-basis/afwijsadvies niet van toepassing. C4 op dit C2 vereist vóór bouw;
  menselijk mergebesluit na onafhankelijke beoordeling blijft afzonderlijk.

## Summary

Werk bestaande reserveringsbeoordelingen uit tot concrete voorbeelden van
synthese en arbitrage, en verduidelijk waarom onderzoeksdekking geen
softwaregoedkeuring is. Maak in module 5 de besluitbron, noodzakelijke
voorwaarden en veilig uitstelbare vragen zichtbaar. Historische uitleg wordt
naslag; de eigen beoordeling en het eigen mensbesluit blijven bij de student.

## Goals

1. De student kan per beoordeling criterium, waarneming, bewijsgrens en
   resterende gebruikskeuze aanwijzen.
2. De student kan verenigbare oordelen herleidbaar samenbrengen en een echt
   inhoudelijk geschil met bewijs aan de hoofdbeoordelaar geven.
3. De student kan C4 koppelen aan een voorstelversie en menselijke bron, met
   een begrensde herstelopdracht en gemotiveerde uitstelkeuze.

## Non-goals

Geen casuscode, README/docstring/testnaamredactie, core, adapters, slides,
beoordelingsrubrics of module-6-uitwerking. Geen volledige C5 voor de lescasus
verzinnen. Geen herstelvoorziening bouwen of echte gegevens verwijderen.
Geen nieuwe norm, gemeten leereffect, echte agentrun of routine-screenshots.

## Current state

Module 4 les benoemt synthese en arbitrage abstract. De oefening geeft G-A/G-M
met pass op het onderzoeken van scenario's, SHIP WITH NITS voor de demonstratie
en ontbrekende volledige eisenbasis. Het verschil met softwaregoedkeuring is
wel begrensd maar nog niet als redeneerstap uitgewerkt. Eén lange stap vraagt
alle C6-velden. De oefening laat iedereen de arbitragevorm gebruiken, ook bij
verenigbare beoordelingen, als onderwijskeuze; core routeert dan naar synthese.

Module 5 hoofdlezing bevat het hele historische poortfragment vóór de
verwijdercasus. De bronbeperkingen zijn correct en moeten mee naar de naslag.
De oefening vraagt besluitbron en veilig uitgestelde vragen, maar geeft daarvoor
nog geen ingevulde bron of afweging. P1 is geconstrueerd; code is in-memory,
zonder publieke herstelmethode, gedeelde of permanente opslag. Verdwijning uit
de boekenplank bewijst geen vernietiging van alle verwijzingen naar het object.

## Proposed approach

### Module 4: van bevinding naar eindoordeel

Tekstfunctie les: uitleggen met korte uitgewerkte voorbeelden. Gebruik G-A en
G-M op dezelfde demonstratiebasis als verenigbaar paar. Toon wat een
synthesis-C7 overneemt met bron-/criterium-ID's; de open ophaalkeuze wordt geen
nieuw feit of toestemming voor toepassing. Een C7 mag blockers niet wegstemmen.

Voeg daarnaast een gelabeld geconstrueerd geschil toe op dezelfde code en een
expliciet aanvullende scenario-eis: na terugbrengen wacht het gereserveerde
boek op ophalen, zonder al een nieuwe lener te registreren. Eén reviewer
beweert dat de code hieraan voldoet en alleen de wachtende naam bewaart; de
ander wijst op de automatische toewijzing aan `uitgeleend_aan` in `terug`.
De hoofdbeoordelaar beslecht die tegenstrijdige uitspraak met code/testbewijs
onder deze expliciete eis: de eis wordt niet gehaald. Het uiteindelijke
voorbeeld blijft BLOCK voor dat scenario; arbitrage verandert geen eis om
een groene uitkomst te bereiken. Dit is een geconstrueerde beoordelingsfout,
geen historische agentwaarneming. De aanvullende eis geldt uitsluitend voor
dit lesvoorbeeld. Een onbesliste gebruikskeuze in de eigen oefening blijft
bij de mens en blokkeert toepassing onder die keuze.

Annoteer G-A direct in de oefening: A1 vraagt onderzoek; code en tests tonen
automatisch uitlenen; pass betekent dat die vraag is onderzocht; de keuze of
het ophaalscenario moet gelden is nog niet goedgekeurd. Het gegeven SHIP WITH
NITS blijft beperkt tot de demonstratie, geen softwarevrijgave voor dat gebruik.

Splits eigen C6-invulling in: artefact/normen/criteria, waarneming/bewijs/grens,
bevinding/ernst/dekking, oordeel/vervolg. Geef bij elke stap gerichte
contractverwijzing. Daarna samenbrengen: eerst wachten op alle vier oordelen,
verenigbaar → orkestratorsynthese; inhoudelijk geschil → hoofdbeoordelaar.
Het lesvoorbeeld oefent arbitrage zonder een conflict in eigen uitkomsten te
verplichten. Vier perspectieven, twee gegeven/twee eigen C6's, bronherleiding
 en prioritering blijven behouden; groepsvariant volgt dezelfde keuze.

### Module 5: een besluit doorgeven

Tekstfunctie les: uitleggen vanuit één voorwaarde en concreet gevolg voor de
volgende rol. Houd uit het historische voorbeeld één voorwaarde in de
hoofdroute: aangeleverde spanningen moeten verdedigbare keuzes zijn, en een
fout mag niet als voorkeur worden gepresenteerd. Leg het gevolg voor de bouwer
uit. Maak van het volledige oude fragment optionele dropdown-naslag met bron,
ontbrekend oorspronkelijke gesprek en grenzen van oude garantie-/botsingsclaims.

Tekstfunctie oefening: voordoen van de besluitregistratie, daarna eigen besluit.
Toon een minimaal ingevuld Artifact and source met fictieve studentnaam,
logboek/besluitnummer, P1 en repositoryversie. Label dit als registratievoorbeeld,
geen echt mensbesluit. De student vervangt de waarden door eigen bron en versie.

Toon REVISE met noodzakelijk herstelplan vóór toepassing: vastleggen welke
gegevens bewaard blijven, hoe terugzetten mogelijk is en wie verantwoordelijk
is. Een bevestigingsvraag vervangt dit niet. Een concreet uitstelbare vraag is
bijvoorbeeld de formulering van de bevestigingstekst: bij dit REVISE wordt niets
uitgevoerd en het herstelvoorstel moet eerst worden beoordeeld. Het uitstel is
veilig voor die huidige stap, geen toestemming voor later onbeperkt uitstel.
Geen herstelkeuze of gevaarlijke uitvoering voor de student vooraf beslissen.

Splits C4-invulling in bron/versie, besluit/reden, menselijke risicokeuzes,
noodzakelijke wijzigingen, expliciet uitgestelde vragen en ontvangercontrole.
Module-5-index kan proportionaliteit kort verbinden aan verloren toegang tot
reserveringen, zonder nieuwe leeruitkomst of extra procesles.

## Acceptance criteria

C0 AC1–7 behouden, alle naar `/root/review50`. AC7 controlekeuze volgt de
vastgelegde normbasis: inhoud, doelgroep en leesvolgorde, build en links;
visuele controle alleen bij vormgeving of een concreet weergaveprobleem.

| AC | Passage en verwachte verificatie-uitkomst |
|---|---|
| 1 | Module 4 les bevat verenigbaar paar met herleidbare synthese en gelabeld inhoudelijk geschil met bewijsgerichte arbitrage. Geen verplicht conflict in eigen oefening. |
| 2 | Annotatie G-A wijst vraag, bewijs, reden voor pass en open gebruiksbesluit aan. Lezer kan onderzoeksdekking van softwaregoedkeuring onderscheiden. |
| 3 | C6/C7- en C4-stappen noemen per beslismoment invoer, handeling, broncontract en bewaarde uitvoer. |
| 4 | Hoofdlezing module 5 heeft één voorwaarde plus gevolg; volledig historisch citaat bytegelijk in naslag, inclusief bronbeperkingen. |
| 5 | Voorbeeldbron en REVISE tonen noodzakelijke voorwaarde en gemotiveerd uitstel. Individueel menselijk plan-/mergebesluit en technische verwijdergrenzen blijven. |
| 6 | Leeruitkomsten op betekenis vergeleken; casusbestanden bytegelijk. Twee eigen beoordelingen/eindoordeel en eigen C4 behouden minder steun dan lesvoorbeelden. |
| 7 | Passagelezing tegen normen met concrete leesvragen; schone -W --keep-going-build, lokale links/fragmenten en diffcontrole. Onderzoek registreert bewijsgrenzen/herstel. |

## Basis and sources

C1 noemt de exacte grondslag. Gelezen product: index/les/oefening onder
`teaching/modules/04-oordelen/` en `05-poort/` op de normbasis.
Brononderzoek: `onderzoek/46-inventarisatie-en-plan.md`, bijlage modules 4–6,
bevindingen 1–6; `onderzoek/46-inleidende-teksten-proef.md`.
Bronbegrenzing: `onderzoek/36-module-redactie.md` en overdracht op #50.
Voorkennis: module 1 `eerste-uitvoering.md` voor C4/C6/C7, module 2
`les.md` (analysemodel) en module 3 `les.md`/`oefening.md` (bewijsgrenzen).
Routing: `core/loop.md`, C6/C7/C4-contracten en reviewer-boss/human-gate.
De historische publicatie en #13-reactie zijn reeds aangewezen bronnen;
hergebruik citeert de bestaande bronbeperking, zonder nieuwe historische claim.

## Repair state

Ontwerp 0, oplevering 0; geen C3 geselecteerd of reparatie uitgevoerd.
Registratie op #50 blijft behouden bij een vervolgsessie.

## Interfaces / contracts / data changes

Geen. Tekst/links tussen les en oefening veranderen samen. De onderwijskeuze
voor altijd-arbitrage wordt vervangen door de actuele keuze synthese/arbitrage,
met expliciet arbitragevoorbeeld. Geen nieuwe route naast core.

## Changes

### 1. Beoordelingen invullen en samenbrengen

**Goal:** concrete overgang van bewijs naar dekking, bevinding en eindoordeel.
**Non-goals:** geen volledige opleveringsreview of nieuwe scenariofunctionaliteit.
**Files:** module 4 les/oefening; index alleen voor gerichte voorkennislink indien nodig.

**Implementation checklist:**

- [ ] Leg nodige eerdere uitleg vindbaar bij C6/C7 uit.
- [ ] Toon verenigbaar paar en inhoudelijk geschil, dezelfde versie en expliciete basis.
- [ ] Annoteer G-A en splits eigen invulstappen met contractlinks.
- [ ] Pas samenbrengstap en groepsvariant aan op synthese/arbitrage-keuze.
- [ ] Behoud vier perspectieven, eigen uitwerking en bewijsgrenzen.

**Verification plan:** manual-with-expected-results. Onafhankelijke lezer wijst
per paar invoer, criteria, argumenten en gekozen uitvoerder aan; schrijft een
korte bronherleidbare synthese en legt uit welk codebewijs het geschil beslecht.
Bij G-A benoemt hij wat pass betekent en welke toepassing niet is vrijgegeven.
Verwacht geen verzonnen eis, tegenspraak, verdwenen blocker of ontbrekende stap.
Geen test-first: tekstwijziging, geen codegedrag. Bestaande casustests en gerichte
codelezing toetsen de gebruikte feiten, geen nieuwe tekstspiegeltests.
**Rollout/rollback:** les/oefening samen; revert van documentatiepakket.
**Done when:** AC1/2/3/6 inhoudelijk onderbouwd.

### 2. Menselijke voorwaarden registreren

**Goal:** een volgende rol kan besluitbron, vrijgegeven werk en voorwaarden terugvinden.
**Non-goals:** geen herstelcode of toestemming voor echte verwijdering.
**Files:** module 5 index/les/oefening; onderzoek/50-uitvoering.md als bewijsregister.

**Implementation checklist:**

- [ ] Houd één historische voorwaarde in de hoofdroute; volledig fragment als naslag.
- [ ] Toon bronregistratie, noodzakelijke herstelvoorwaarde en veilige uitstelreden.
- [ ] Splits eigen C4-handelingen en behoud individuele mensrol en later mergebesluit.
- [ ] Behoud verdwijnen-uit-lijst versus objectvernietiging en scenario versus code.
- [ ] Leg voor/na, technische controles en grenzen vast.

**Verification plan:** manual-with-expected-results voor besluitgang: reviewer
kan één C4 op P1 op papier voorbereiden met echte velden en voorbeeldstatus,
zonder die agentuitwerking een menselijk besluit te noemen. Hij benoemt waarom
herstel vóór toepassing nodig is in het voorbeeld, en waarom bevestigingstekst
nu kan wachten. Validation-workflow: bestaande casustests in gescheiden kopieën
(module 4 vijf pass, module 5 drie pass), gericht feitelijk terug-/verwijdergedrag,
historisch citaat exact vergelijken, beschermde casusdiff leeg,
`make -C docs html` onder -W --keep-going, lokale links en `git diff --check`.
Verwacht intacte casus/leeruitkomstbetekenis, geen waarschuwingen/kapotte links.
Geen test-first voor tekst; geen screenshots zonder concreet weergaveprobleem.
**Rollout/rollback:** met wijziging 1; revert van tekstpakket.
**Done when:** AC3–7 onderbouwd; C5 pinnt exacte productcommit en bewijsgrenzen.

## Risks

Meer invulsteun kan zelfstandige afweging verdringen: voorbeelden blijven in
les/annotatie, eigen besluiten worden niet ingevuld. Een feitelijk geschil is
geconstrueerde oefeninvoer, geen aangetroffen echte agentspanning. Onvolledige
historische bronnen behouden hun beperking; oude casusclaims blijven buiten
scope en worden niet door nieuwe tekst bevestigd.

## Assumptions

De lezer heeft modules 1–3 gevolgd; nieuwe teksten maken de nodige vindplaatsen
expliciet. Geen studentwaarnemingen, gemeten duur of leereffect beschikbaar.
De huidige casusuitslagen worden bij uitvoering opnieuw gemeten.

## Open questions

C4: akkoord met dit pakket, inclusief het vervangen van altijd-arbitrage in de
eigen oefening door synthese bij verenigbare oordelen en arbitrage bij een echt
geschil? Het uitgewerkte lesgeschil houdt het leren arbitreren zichtbaar; de
bestaande leeruitkomsten en eigen beoordeling blijven behouden.
Nog geen bouw- of mergevrijgave.
