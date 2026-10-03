# Beoordeel een uitbreiding vanuit vier perspectieven

Je beoordeelt de reserveringscode van de boekenplank. Twee beoordelingen zijn gegeven; je werkt de strikte en pragmatische perspectieven zelf uit. Daarna schrijf je een eindoordeel dat bevindingen, bronnen en prioriteiten samenbrengt.

**Duur:** circa 90 minuten.
**Voorkennis:** [module 3](../03-machine/les.md), vooral het onderscheid tussen gecontroleerde gevallen en de afgesproken eisen; de [les over beoordelen](les.md).
**Nodig:** een lokale kopie van de repository, Python met `pytest`, de beoordelaarsrollen onder `core/roles/` en de contracten {core}`contracts/reviewer-verdict.md` (C6) en {core}`contracts/final-verdict.md` (C7).
**Inleveren:** de twee gegeven beoordelingen met bronverwijzing, twee eigen C6-beoordelingen, een C7-eindoordeel en de beantwoorde verantwoordingsvragen.

## Voorbereiding

1. Open `teaching/cases/module4-reserveringen/` in je lokale repository. Lees [boekenplank.py](https://github.com/misja/agent-role-loop/blob/main/teaching/cases/module4-reserveringen/boekenplank.py) en [test_boekenplank.py](https://github.com/misja/agent-role-loop/blob/main/teaching/cases/module4-reserveringen/test_boekenplank.py).
2. Voer vanuit die casusmap het volgende commando uit:

   ```bash
   python -m pytest
   ```

3. Noteer welke gevallen de vijf tests controleren en leg de onderzochte repositorycommit vast. Gebruik die commit als artefactversie in je beoordelingen. Bij de ongewijzigde casus worden vijf geslaagde tests verwacht. Onderzoek een andere uitkomst voordat je die als bewijs gebruikt.

De tests controleren onder meer direct uitlenen bij reserveren en uitlenen aan de eerste wachtende bij terugbrengen. Ze vormen geen volledige eisenbasis. De beschrijvingen bij de casus doen uitspraken over verdedigbare keuzes; controleer zulke uitspraken zelf aan code, tests en gebruiksdoel. De aangeleverde casus bevat geen CLI of verwijdermethode.

## Worked example: twee gegeven beoordelingen

De onderstaande beoordelingen zijn onderwijsvoorbeelden op de aangeleverde code. Er zijn hiervoor geen onafhankelijke agents uitgevoerd en er is geen volledige historische opdracht beschikbaar. Gebruik de gegeven criteria en bevindingen als invoer voor je eindoordeel. Voeg je eigen commit en testuitkomst toe als artefactbron; neem geen ontbrekend bewijs aan.

### G-A: adversarieel

**Toewijzing en basis:** criterium A1: onderzoek hoe reserveren en terugbrengen zich gedragen wanneer ophalen nog een afzonderlijke handeling moet zijn. Dit is een expliciet gebruiksscenario, geen aangetroffen eis van de casus. Modus: initial; artefact: jouw vastgelegde commit, `boekenplank.py` en de vijf tests. Alle dekking hieronder betreft een nieuwe lezing van dit voorbeeld. De strikte, pragmatische en onderhoudbaarheidscriteria worden elders beoordeeld.

**Dekking A1:** pass voor het onderzoeken van het scenario. `reserveren` zet bij een beschikbaar boek meteen `uitgeleend_aan`; `terug` neemt de eerste wachtende naam met `pop(0)` en registreert die als lener. De tests `test_reserveren_van_beschikbaar_boek_leent_meteen_uit` en `test_terug_leent_uit_aan_eerste_op_wachtlijst` controleren dit gedrag. Een afzonderlijke ophaalstap is niet aanwezig.

**Bevinding A1-F1, should fix:** als ophalen eerst moet plaatsvinden, lopen registratie en feitelijk lenen uiteen. Laat de verantwoordelijke mens bepalen of dit gebruiksdoel geldt. De bevinding is voor dit lesvoorbeeld een open gebruikskeuze; zij bewijst geen schending van een bestaande eis. Bij een afgesproken ophaaleis zou dit gedrag wel een blokkade opleveren.

**Decision:** SHIP WITH NITS voor het beoordelen van de aangeleverde demonstratie; geen toestemming voor toepassing in het ophaalscenario. **Contract drift:** geen vastgestelde contractwijziging; volledige eisenbasis niet beschikbaar. **Must fix:** geen aangetoonde blocker binnen deze demonstratie. **Nice to have:** geen. **Repair outcome:** niet van toepassing, initial. **Next action:** het gegeven oordeel meenemen in C7; de mens beslist over een latere toepassing.

### G-M: onderhoudbaarheid

**Toewijzing en basis:** criterium M1: wijs aan welke code en gegevensvorm relevant zijn als ophalen later afzonderlijk wordt vastgelegd of personen met dezelfde naam voorkomen. Dit zijn toekomstige gebruiksscenario’s. Modus: initial; dezelfde artefactversie en bronnen als G-A. Alle dekking hieronder betreft een nieuwe lezing van dit voorbeeld. De overige perspectiefcriteria worden elders beoordeeld.

**Dekking M1:** pass voor het aanwijzen van de wijzigingsplaatsen. `terug` maakt het boek beschikbaar en handelt de volgende uitlening af in dezelfde methode. `Boek.wachtlijst` is een `list[str]`; `reserveren` voegt alleen een naam toe. Twee verschillende personen die allebei Bob heten, worden in die lijst door dezelfde tekst weergegeven.

**Bevinding M1-F1, should fix:** bij een afzonderlijke ophaalstap moet de automatische uitlening in `terug` opnieuw worden ontworpen. Leg die wijzigingsplaats vast zodra dit scenario onderdeel van de opdracht wordt. **Bevinding M1-F2, should fix:** bij personen met dezelfde naam vraagt onderscheid tussen personen aanvullende identiteit. Voor deze demonstratie is niet vastgesteld dat zulke identificatie vereist is.

**Decision:** SHIP WITH NITS voor de demonstratie. **Contract drift:** geen vastgestelde contractwijziging; volledige eisenbasis niet beschikbaar. **Must fix:** geen aangetoonde blocker. **Nice to have:** geen. **Repair outcome:** niet van toepassing, initial. **Next action:** de bevindingen met hun voorwaarden meenemen in C7 en pas bij een gekozen gebruiksdoel als wijzigingsvereiste behandelen.

## Opdracht: twee eigen beoordelingen en een eindoordeel

Deze oefening gebruikt de arbitragevorm van C7 om de afweging expliciet te oefenen. Ook als je beoordelingen verenigbaar blijken, hoef je geen tegenspraak te verzinnen. Noteer dan dat er geen inhoudelijk geschil is; bij projectwerk volstaat in dat geval synthese volgens {core}`loop.md`.

1. Schrijf een C6 vanuit het **strikte perspectief**. Benoem je criterium: welke reserveringsafspraken zijn nodig om naleving te kunnen beoordelen? Maak onderscheid tussen een vastgelegde testverwachting en een ontbrekende gebruikseis. Formuleer een concrete vraag voor iedere ontbrekende afspraak; behandel ontbrekende informatie niet als een bewezen codefout.
2. Schrijf een C6 vanuit het **pragmatische perspectief**. Benoem welk beperkt gebruik je als beoordelingsbasis kiest en welke beperkingen daarbij aanvaardbaar zijn. Onderbouw welke bevindingen uit G-A en G-M kunnen wachten en welke voor dat gebruik eerst moeten worden opgelost.
3. Volg voor beide beoordelingen het C6-contract. Vermeld perspectief en criterium-ID’s, commit en normbasis, onderzochte waarneming met bron, gevolg en ernst, criteriumdekking en besluit. Benoem ontbrekend bewijs. Noteer contractwijzigingen, must/should/nice-bevindingen, initial-modus en de volgende stap. Een niet-geverifieerd toegewezen criterium mag niet slagen.
4. Schrijf een C7 als **hoofdbeoordelaar**. Gebruik G-A, G-M en beide eigen C6’s als invoer. Verwijs bij iedere gecombineerde bevinding en dekkingsclaim naar de bronbeoordeling en het criterium- of bevinding-ID. Leg eventuele tegenspraak en je oplossing vast. Prioriteer correctheid en veiligheid, daarna onderhoudbaarheid en afwerking. Los een onbesliste doel- of risicokeuze niet zelf op: leg haar aan de mens voor en houd haar als blocker zichtbaar.

Voor deze lescasus bestaat geen afzonderlijke C5-overdracht. Vermeld bij de C7-invoer daarom de casuscommit, testuitkomst en gegeven onderwijsbeoordelingen als beschikbare basis, en noteer dat een volledig project-C5 ontbreekt. Schrijf geen overdracht of agentuitvoering die niet heeft plaatsgevonden. Je eindresultaat is een onderwijsuitwerking van C6/C7, geen volledige opleveringsreview van een nieuw project.

Controleer vóór inleveren of je vier perspectieven herkenbaar zijn en of ieder eindoordeel te herleiden is tot een bron. Een eventuele BLOCK moet een concreet criterium, ontbrekend bewijs of aangetoond probleem en de benodigde vervolgstap noemen. Een SHIP betekent klaar voor een menselijk opleveringsbesluit, geen automatische merge.

## Verantwoordingsvragen

Beantwoord schriftelijk:

1. Welke bevinding berust op aangetoond codegedrag? Welke ontbrekende eis zou nodig zijn om dat gedrag als fout te beoordelen?
2. Welke twee perspectieven wegen dezelfde keuze verschillend, of ondersteunen juist dezelfde conclusie? Onderbouw dit met hun criteria en gebruiksvoorwaarden.
3. Verantwoord de prioriteit van één bevinding in je C7. Welke bron draagt je afweging en welke keuze moet eventueel nog naar de mens?

## Variant: beoordelingen door studenten

In deze variant schrijven vier studenten elk afzonderlijk een C6 vanuit een ander perspectief op dezelfde casuscommit en afgesproken gebruiksbasis. Zij lezen elkaars beoordelingen pas nadat alle vier klaar zijn. Een vijfde student schrijft de C7 als hoofdbeoordelaar. Deze vier eigen beoordelingen vervangen de twee gegeven en twee eigen beoordelingen uit de individuele opdracht. Bespreek daarna overeenkomsten, eventuele tegenspraak en de gebruikte bronnen; ook hier is een conflict geen verplichte uitkomst.
