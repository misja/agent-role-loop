# Schrijfwijzer voor het onderwijsmateriaal

Deze schrijfwijzer legt de conventies vast voor al het teaching-materiaal in deze
repository: lessen, oefeningen, raamwerken en cases. Het doel is professioneel,
consistent onderwijsmateriaal. De regels gelden voor alle modules en voor elke
nieuwe bijdrage; ze worden niet per document opnieuw afgewogen.

Wie materiaal schrijft of laat schrijven, verwijst naar deze schrijfwijzer als
constraint. Wie materiaal beoordeelt, toetst eraan.

## Register en aanspreekvorm

- Het register is dat van professioneel onderwijsmateriaal voor derdejaars
  hbo-studenten: zakelijk, helder, niet populair en niet joviaal.
- De student wordt aangesproken met **je**. Instructies staan in de gebiedende
  wijs ("Clone de repository", "Voer de tests uit").
- Geen verkleinwoorden voor vakinhoud. Niet "een repootje", "een scriptje", "een
  testje"; wel "een repository", "een script", "een test".
- Geen populaire of spreektalige wendingen ("even snel", "gewoon", "lekker",
  "hartstikke", uitroepen, knipogen naar de lezer).
- Geen overdreven enthousiasme of aanmoediging. Het materiaal legt uit en
  instrueert; het cheerleadt niet.
- Vermijd de herkenbare stijltrekjes van AI-gegenereerde tekst. Veel van het
  materiaal wordt met AI-ondersteuning geschreven, en dat mag, maar het resultaat
  moet niet als zodanig leesbaar zijn. Let op terugkerende tells: de
  tegenstellingsconstructie "het gaat niet om X, maar om Y", drieslagen ("helder,
  consistent en professioneel"), holle bezwerende slotzinnen die niets toevoegen,
  en overmatig gebruik van "juist", "immers" en "simpelweg". Dit is een
  richtlijn, geen mechanische toets: schrijf zoals een vakdocent schrijft, niet
  zoals een model. Eén tell is wel hard en toetsbaar, zie interpunctie: geen em-
  of en-dash.

## Vaktermen: Nederlands of Engels

- Gebruik de Engelse vakterm waar die in het vakgebied gangbaarder is dan een
  Nederlandse vertaling. Forceer geen Nederlandse vertaling waar de Engelse term
  de norm is.
- Vervoeg Engelse termen niet tot Nederlands-Engelse hybriden. Gebruik de term
  als imperatief commando of als zelfstandig naamwoord, niet als vernederlandst
  werkwoord.
- Introduceer een Engelse term bij eerste gebruik kort in het Nederlands waar dat
  het begrip dient; daarna volstaat de Engelse term. Voor derdejaars hoeft niet
  elke gangbare term te worden toegelicht.
- Wees consistent: kies per term één vorm en houd die in al het materiaal aan.

### Wel / niet (groeiende lijst)

| Niet | Wel | Reden |
|---|---|---|
| cloneert, clonen | clone de repository | geen vernederlandst Engels werkwoord |
| mergen, merget | merge de branch | idem |
| committen, commit (als NL ww) | commit de wijziging | idem |
| repo (als standaard) | repository | voluit als standaard; "repo" alleen in commandocontext |
| een repootje, scriptje, testje | een repository, script, test | geen verkleinwoorden voor vakinhoud |
| dependency'tje | dependency | idem |
| de straat (jargon) | de ontwikkelstraat | geen interne verkorting in lesmateriaal |

Vul deze tabel aan zodra nieuwe gevallen opduiken. De tabel is normatief: wat
hier staat, is de afspraak.

## Terminologie-consistentie

- Eén begrip, één term. Wissel niet ongemerkt tussen synoniemen (bijvoorbeeld
  niet afwisselend "beoordelaar" en "reviewer" voor dezelfde rol).
- Sluit aan op de begrippenlijst (`begrippen.md`). Staat een term daar, gebruik
  die vorm. Ontbreekt een term die je vaker gebruikt, voeg hem toe.
- Verwijs naar de rollen en contracten met hun vastgelegde naam, niet met
  wisselende omschrijvingen.

## Structuur en signalering van tekstsoorten

Materiaal is opgebouwd in herkenbare, expliciet benoemde onderdelen. De lezer
moet altijd weten of hij uitleg leest, een opdracht uitvoert of reflecteert.

- Maak per onderdeel expliciet wat het is. Gebruik heldere kopjes die de
  tekstsoort benoemen, bijvoorbeeld "Inleiding", "Wat je gaat doen", "Opdracht",
  "Stappen", "Reflectie".
- Meng tekstsoorten niet binnen één blok. Inleidende uitleg, instructie en
  reflectievraag staan in eigen, gescheiden onderdelen.
- Werk stap voor stap. Een opdracht met meerdere handelingen wordt een genummerde
  reeks stappen, niet één doorlopende alinea.
- Een opdracht maakt expliciet wat het eindresultaat is en waaraan de student kan
  zien dat de stap geslaagd is.
- Leerdoelen en leeruitkomsten staan apart en zijn geformuleerd als wat de
  student kan en kan verantwoorden, niet als wat is opgeleverd.

## Expressiemiddelen

Materiaal hoeft niet uit lopende tekst alleen te bestaan. Zeker bij langere
stukken mag je het palet aan expressiemiddelen benutten dat Markdown en
Sphinx/MyST bieden. De leidende regel is steeds: een middel wordt ingezet waar
het het begrip dient, niet als versiering. Spaarzaam en functioneel, niet
decoratief.

De volgende middelen zijn welkom waar ze meerwaarde hebben. De lijst is niet
uitputtend; wat het begrip aantoonbaar verheldert, is toegestaan.

- **Admonitions** (MyST `note`, `tip`, `warning`, `important`). Voor een
  terzijde, een valkuil of een waarschuwing die de hoofdlijn niet moet
  onderbreken. Niet voor gewone tekst die ook in een alinea kan staan.
- **Mermaid-diagrammen** voor stroomschema's, processen, toestandsovergangen en
  andere structuren die zich slecht in proza laten vangen. De voorkeur gaat uit
  naar Mermaid boven een gevonden afbeelding, omdat een diagram eigen werk is,
  versievast en aanpasbaar. Mermaid vereist een extensie in de build; zie de
  technische voorwaarde hieronder.
- **Afbeeldingen** waar een visueel voorbeeld iets toont wat tekst niet
  efficiënt kan (een screenshot van een interface, een schematische weergave).
  Voorwaarden: voorzie elke afbeelding van een alt-tekst; plaats het bestand op
  de afgesproken plek in de repository; en gebruik uitsluitend eigen werk,
  publiek domein, of materiaal met een licentie die verenigbaar is met de
  licentie van deze repository (CC BY-NC-SA 4.0), met bronvermelding. Plak geen
  afbeeldingen van onbekende herkomst.
- **Code- en commandoblokken** met taalaanduiding voor syntax highlighting.
  Onderscheid code (wat de student leest of schrijft) van commando's (wat de
  student uitvoert).
- **Tabellen** voor vergelijkingen en overzichten waar de structuur tweedimensionaal
  is. Niet voor wat een opsomming ook aankan.

> **Technische voorwaarde Mermaid.** Mermaid-ondersteuning vereist een extensie
> (`sphinxcontrib-mermaid`) als dependency in `pyproject.toml` en een
> configuratie in `conf.py`. Dit is een aparte technische wijziging, los van deze
> schrijfwijzer. Gebruik Mermaid pas in materiaal nadat die ondersteuning is
> ingeschakeld en de build er schoon mee is.

## Opmaak en interpunctie

- Markdown, geschreven voor publicatie via Sphinx/MyST.
- Nederlandse interpunctie. Gebruik spatie-koppelteken-spatie ( - ) waar een
  gedachtestreep nodig is. Gebruik geen em-dash en geen en-dash. Dit is de harde,
  toetsbare uitwerking van het register-principe dat het materiaal niet de
  trekjes van AI-gegenereerde tekst draagt; de em-dash is daarvan de meest
  herkenbare.
- Spaarzaam met opsommingen en vetgedrukte tekst; alleen waar het de structuur
  echt verheldert.
- Verwijzingen naar bronbestanden volgen de vastgestelde conventie (klikbare
  links naar bestanden, mappen als inline code).
