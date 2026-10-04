# Kwaliteit beoordelen vanuit verschillende perspectieven

## Plaats in de leerlijn

In [module 3](../03-machine/les.md) onderzocht je welke gevallen automatische controles toetsen en welke conclusies hun uitkomsten toelaten. Hier beoordeel je ook de keuzes die deze controles openlaten. Je gebruikt de oordeelsmatige kwaliteitsmechanismen uit het [kwaliteitsraamwerk](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md).

De {ref}`overdrachtsanalyse uit module 2 <module2-analyse>` helpt bron, versie
en ontbrekend bewijs te onderscheiden. De
[begeleide uitvoering uit module 1](../01-ervaren/eerste-uitvoering.md) toont
hoe C6-oordelen naar een C7 en een menselijk besluit gaan. Hier leer je de
inhoud van die oordelen te wegen.

De les hoort bij [oefening 4](oefening.md). Daar gebruik je vier perspectieven om het afwegen te oefenen. Bij projectwerk bepaalt de triage welke beoordelingen nodig zijn; vier beoordelaars zijn geen vaste bezetting. De route staat in {core}`loop.md`.

## Opbouw

### Dezelfde keuze, verschillende belangen

De reserveringscode bevat de methode `terug`. Die maakt een boek beschikbaar en leent het vervolgens meteen uit aan de eerste naam op de wachtlijst. Een test controleert dat gedrag. Daarmee is nog niet bepaald of een bibliotheek automatisch wil uitlenen of eerst wil wachten totdat iemand het boek ophaalt.

Een pragmatische beoordelaar kan automatische afhandeling voldoende vinden voor een eerste versie. Een onderhoudbaarheidsbeoordelaar vraagt welke aanpassing nodig is als ophalen later een afzonderlijke stap wordt. Zij beoordelen dezelfde keuze vanuit verschillende belangen. Hun conclusies kunnen verschillen, maar kunnen ook verenigbaar zijn: nu opleveren en de latere wijziging als aandachtspunt vastleggen.

Afspraken, automatische controles en oordeel vullen elkaar hier aan. Een afspraak bepaalt het gewenste reserveringsgedrag; een test kan dat gedrag controleren. Een beoordelaar onderzoekt of de afspraak toereikend is voor het gebruik en of de code eraan voldoet.

### Vier perspectieven op de reserveringen

De casus staat in `teaching/cases/module4-reserveringen/`. Lees de [code](https://github.com/misja/agent-role-loop/blob/main/teaching/cases/module4-reserveringen/boekenplank.py) en [tests](https://github.com/misja/agent-role-loop/blob/main/teaching/cases/module4-reserveringen/test_boekenplank.py) voor de feitelijke werking. De beschrijvingen bij de casus vervangen die controle niet. Er is hier geen CLI of verwijdermethode.

De vier perspectieven richten de aandacht op verschillende vragen:

- **Strikt:** welke eis bepaalt wat reserveren betekent? `reserveren` leent een beschikbaar boek meteen uit. De test legt dit gedrag vast, maar is geen volledige opdrachtbeschrijving. Is direct uitlenen afgesproken, of ontbreekt die keuze nog?
- **Pragmatisch:** welk gebruik moet de eerste versie ondersteunen? Voor een beperkte demonstratie kan de wachtlijst voldoende zijn. Voor dat oordeel moet duidelijk zijn welke beperkingen worden aanvaard.
- **Adversarieel:** wat gebeurt er buiten de geteste voorbeelden? De wachtlijst heeft geen vervaltermijn en `terug` registreert direct een nieuwe lener. Als het gebruik eerst ophalen vereist, ontbreekt daarvoor een afzonderlijke stap. Onderzoek het gevolg; de code toont niet dat een reservering het boek blijvend blokkeert.
- **Onderhoudbaarheid:** waar moet een toekomstige wijziging worden verwerkt? `terug` handelt zowel terugbrengen als opnieuw uitlenen af. Ook bewaart de wachtlijst alleen namen. In een scenario met twee verschillende personen die allebei Bob heten, kan deze gegevensvorm hen niet onderscheiden.

Leg bij iedere bevinding vast waarop zij berust. Gedrag dat een afgesproken eis schendt is een fout. Ontbreekt de eis, beschrijf dan de open keuze en de gebruikssituatie die nodig is om haar te besluiten. Een groene testsuite sluit fouten in andere gevallen niet uit.

### Beoordelingen samenbrengen en prioriteren

Een beoordeling volgens {core}`contracts/reviewer-verdict.md` (C6) vermeldt de toegewezen criteria, het onderzochte artefact, bewijs en een besluit. Een bevinding moet laten zien wat er gebeurt en waarom dat voor een criterium relevant is. Een voorkeur zonder gebruiksdoel is onvoldoende grond voor een blokkade.

Bij meerdere verenigbare C6-beoordelingen maakt de orkestrator een herleidbare synthese in C7. Die voegt geen nieuwe bevindingen toe en stemt blokkerende bevindingen niet weg. Inhoudelijke tegenspraak gaat naar de hoofdbeoordelaar ({core}`roles/reviewer-boss.md`), die argumenten en bewijs onderzoekt. Beide vormen staan in {core}`contracts/final-verdict.md`.

Bij arbitrage krijgen correctheid en veiligheid voorrang, daarna onderhoudbaarheid en afwerking. Dat betekent bijvoorbeeld dat een bewezen schending van een uitleeneis eerst moet worden opgelost. Een mogelijke toekomstige opsplitsing van `terug` is niet automatisch een blocker. De hoofdbeoordelaar legt per bevinding uit welke prioriteit volgt uit het criterium, bewijs en gebruik. Blijft een doel- of risicokeuze onbeslist, dan legt die haar aan de mens voor en blijft het oordeel geblokkeerd.

(module4-samenbrengen)=
### Uitleg: twee verenigbare oordelen samenbrengen

De gegeven G-A en G-M in de [oefening](oefening.md) onderzoeken dezelfde
reserveringscode voor een demonstratie. G-A onderzoekt bij A1 de gevolgen van
een afzonderlijke ophaalstap; G-M wijst bij M1 de daarvoor relevante code en
gegevensvorm aan. Beide geven SHIP WITH NITS voor de demonstratie. Hun
bevindingen zijn verenigbaar: zij stellen geen tegengestelde eisen en erkennen
dat het toekomstige gebruik nog moet worden gekozen.

Een orkestrator kan dit paar als volgt samenbrengen. Dit is een fragment van
een geconstrueerde onderwijs-C7, geen echte agentreview of volledig project-C7.

| C7-veld | Ingevuld fragment |
|---|---|
| Mode and producer | synthesis, orkestrator. |
| Inputs | Dezelfde vastgelegde casuscommit, eigen testuitvoer, G-A en G-M. Voor dit paar zijn beide oordelen aanwezig; bij de eigen vier perspectieven wacht je op alle vier. Een project-C5 ontbreekt in deze lescasus. |
| Source traceability | A1 pass volgens G-A: automatisch uitlenen en ontbrekende ophaalstap onderzocht. M1 pass volgens G-M: wijzigingsplaatsen en naamidentificatie aangewezen. Dit is onderzoeksdekking, geen nalevingsbewijs voor een ophaaleis. |
| Findings and decision | A1-F1 en M1-F1: laat het gebruiksdoel kiezen vóór toepassing die ophalen vereist; M1-F2: aanvullende identiteit onderzoeken als personen met dezelfde naam moeten worden onderscheiden. SHIP WITH NITS uitsluitend voor de demonstratie. |
| Reviewer disagreements | Geen; geen arbitrage nodig. |
| Next action | De mens beslist over eventuele toepassing. De toekomstige ophaaleis is niet door deze synthese goedgekeurd. |

De synthese bewaart de bronnen en hun voorwaarden. Zij maakt geen nieuwe
bevindingen en kan een blocker niet laten verdwijnen doordat meer beoordelaars
SHIP zeggen. Als je eigen beoordelingen verschillende gebruiksbases hanteren,
maak dat zichtbaar: een groene demonstratie-uitkomst en een blokkade voor een
andere toepassing zijn niet zonder meer tegenspraak over dezelfde vraag.

### Uitleg: een inhoudelijk geschil met bewijs beslechten

Voor dit tweede voorbeeld geldt een **aanvullende scenario-eis O1**: na
terugbrengen wacht een gereserveerd boek op ophalen; er mag nog geen nieuwe
lener geregistreerd staan. O1 is voor deze uitleg toegevoegd en is geen
historische eis van de aangeleverde casus. Beide onderstaande beoordelaars
beoordelen naleving van O1 op dezelfde codeversie.

| C6-fragment | Uitspraak over hetzelfde criterium O1 |
|---|---|
| G-X, O1 pass, SHIP | “Na terugbrengen blijft Bob alleen als wachtende genoteerd; er is nog geen nieuwe lener.” |
| G-Y, O1 fail, BLOCK, bevinding Y1 | “`terug` zet `uitgeleend_aan` op de eerste naam met `wachtlijst.pop(0)`. Bob wordt dus direct lener. O1 wordt niet gehaald.” |

Dit is een geconstrueerde beoordelingsfout, geen verslag van twee echte agents.
De uitspraken kunnen onder dezelfde eis niet allebei juist zijn. De
hoofdbeoordelaar onderzoekt de argumenten met de code en
`test_terug_leent_uit_aan_eerste_op_wachtlijst`. Die test leent uit aan Misja,
laat Bob en Carla reserveren en brengt het boek terug. De asserties verlangen
dan `uitgeleend_aan == "Bob"` en `wachtlijst == ["Carla"]`.

Een arbitration-C7 wijst daarom G-X af op O1 en neemt Y1 over: de bestaande
code schendt de aanvullende ophaaleis. Het oordeel blijft BLOCK voor het
O1-scenario; eerst moet het gedrag worden aangepast en gecontroleerd als de
mens die toepassing wil laten bouwen. Dat de bestaande tests slagen verandert
O1 niet: hun verwachting betreft juist automatisch uitlenen. De
hoofdbeoordelaar kan deze feitenstrijd beslechten. Hij mag niet namens de mens
besluiten dat ophalen toch onnodig is. Blijft het gebruiksdoel open, dan blijft
die doelkeuze bij de mens.

### Grenzen van de beoordeling

In deze module oefen je het onderbouwen en samenbrengen van beoordelingen. Je kunt daarmee aangeven dat een reserveringsregel nog moet worden gekozen. De keuze welke gevolgen aanvaardbaar zijn, vraagt een besluit van de verantwoordelijke mens. Module 5 werkt dat beslismoment uit aan een verwijderoperatie.

## Werkvormen en toetsing

- Werkvormen: gezamenlijke ontleding van twee gegeven beoordelingen, daarna eigen beoordelingen vanuit de overige perspectieven en een eindoordeel in oefening 4.
- Toetsing: formatief, via de beoordelingen en de verantwoordingsvragen van oefening 4.

## Bronnen

- Het raamwerk [Kwaliteit als gedeelde verantwoordelijkheid](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md), de oordeelsmatige kwaliteitsmechanismen.
- De beoordelaarsrollen onder `core/roles/`, {core}`roles/reviewer-boss.md` en de contracten {core}`contracts/reviewer-verdict.md` (C6) en {core}`contracts/final-verdict.md` (C7).
- Fagan, Design and code inspections {cite}`fagan1976design`. Formele inspectie is een achtergrond bij het oefenen met afzonderlijke beoordelingen. Het artikel bepaalt geen optimale bezetting voor LLM-agents.

## Afronding

### Wat heb je geleerd

Een beoordeling verbindt een waarneming aan een criterium en het beoogde gebruik. Je onderscheidt een aangetoonde fout van een ontbrekende eis of ontwerpkeuze. Verschillende perspectieven kunnen dezelfde keuze ondersteunen of verschillend wegen. Het eindoordeel maakt de bronnen en prioriteiten zichtbaar; een onbesliste doel- of risicokeuze blijft bij de mens.

### Zelfcheck

Beantwoord uit je hoofd; de sleutel wijst waar je het kunt nakijken.

1. Welke vraag over `terug` blijft open nadat de bijbehorende test slaagt? (zie "Dezelfde keuze, verschillende belangen")
2. Noem een bevinding uit de reserveringscode, haar bron en de gebruiksvoorwaarde waaronder zij een fout zou aantonen. (zie "Vier perspectieven op de reserveringen")
3. Wanneer volstaat synthese en wanneer is arbitrage nodig? Verantwoord de prioriteit van één bevinding. (zie "Beoordelingen samenbrengen en prioriteren")

### Volgende stap

In [module 5](../05-poort/index.md) onderzoek je de gevolgen van verwijderen en neem je een menselijk besluit over een voorstel. Je gebruikt je beoordeling om te bepalen welke risico’s aanvaardbaar zijn en welke voorwaarden eerst moeten worden vervuld.
