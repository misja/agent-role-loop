# Kwaliteit als gedeelde verantwoordelijkheid

Softwarekwaliteit is geen eigenschap die je aan het eind toevoegt en geen enkele rol die één iemand vervult, maar een verzameling verantwoordelijkheden die over een werkproces verdeeld is. Dit raamwerk maakt die gedachte expliciet en biedt daarmee de grondslag waaraan lessen over concrete kwaliteitsthema's (coverage, CI/CD, security, branchingstrategie, codeconventies) zich ophangen.

Het bouwt voort op de rollenloop die in deze repository is uitgewerkt: een werkwijze waarin een taak door achtereenvolgende rollen gaat (triage, planner, bouwer, een aantal beoordelaars met elk een eigen invalshoek, en een menselijke poort tussen plannen en bouwen), waarbij elke overdracht via een vast contract verloopt. De werking daarvan staat in de vier werkingsprincipes (`core/principles.md`): contextisolatie, expliciete overdrachten, proportionaliteit en de menselijke poort. Dit raamwerk staat op een ander niveau. Het legt uit wat die werking betekent voor softwarekwaliteit, en waarom de loop daarmee meer is dan een handige manier om met AI-agents te werken.

Het bruikbare van de loop is dat hij de verdeling van verantwoordelijkheden zichtbaar maakt. Kwaliteitsdenken dat in de dagelijkse praktijk impliciet en verspreid blijft, wordt hier benoembaar en aanwijsbaar: je kunt per verantwoordelijkheid aanwijzen welke rol haar draagt.

## Kwaliteit is geen rol

In een onvolwassen beeld van software engineering is kwaliteit iets wat één persoon of één stap regelt. De tester. De review aan het eind. De linter die groen moet zijn. Dat beeld is begrijpelijk, want het is overzichtelijk, en veel mensen beginnen ermee.

De rollenloop laat een ander beeld zien. Kwaliteit is verdeeld over de hele keten, en verschillende rollen dragen er verschillende stukken van. De bouwer (`core/roles/builder.md`) is verantwoordelijk voor verifieerbaar werk: niet "het werkt op mijn machine", maar aantoonbaar bewijs dat de wijziging doet wat is afgesproken. De vier beoordelaars (de rolbestanden onder `core/roles/`) dragen elk één kwaliteitsperspectief, en die perspectieven spreken elkaar bewust tegen. De hoofdbeoordelaar (`core/roles/reviewer-boss.md`) weegt die tegenspraak en stelt een prioriteit vast. En de menselijke poort (`core/roles/human-gate.md`) draagt het oordeel dat aan geen enkele andere rol mag worden overgelaten: is dit nog steeds het juiste doel, en zijn de risico's omkeerbaar?

Het punt is niet dat dit een efficiënte werkverdeling is. Het is dat kwaliteit intrinsiek verdeeld is, en dat een proces dat doet alsof één stap haar regelt, een illusie in stand houdt. De loop maakt de verdeling expliciet in plaats van haar te verbergen achter een enkel groen vinkje.

## Kwaliteit spreekt zichzelf tegen

De vier beoordelaars zijn geen vier manieren om hetzelfde te zeggen. Ze vertegenwoordigen kwaliteitsdimensies die in de praktijk regelmatig botsen:

- De strikte beoordelaar wil correctheid en volledige dekking van de acceptatiecriteria.
- De pragmatische beoordelaar wil opleveren en weegt of het goed genoeg is voor nu.
- De adversariële beoordelaar zoekt de niet-afgevangen randgevallen, de aannames die breken onder druk, de beveiligingsgaten.
- De beoordelaar op onderhoudbaarheid kijkt voorbij vandaag: kan een ander dit over een jaar nog begrijpen en wijzigen?

Correctheid tegenover snelheid. Volledigheid tegenover opleveren. Veiligheid tegenover eenvoud. Onderhoudbaarheid tegenover de kortste weg. Dit zijn reële spanningen, geen schijntegenstellingen, en in een volwassen team worden ze door verschillende mensen met verschillende belangen vertegenwoordigd.

De hoofdbeoordelaar lost die spanning niet op door één perspectief gelijk te geven, maar door te prioriteren volgens een expliciete regel: correctheid en veiligheid eerst, dan onderhoudbaarheid, dan afwerking. Dat is een kwaliteitsmodel, geen smaakoordeel, en het maakt zichtbaar dat de afweging onvermijdelijk is. Er bestaat geen uitkomst waarin alle vier de beoordelaars tegelijk volledig hun zin krijgen.

Daarmee verschuift wat er te leren valt. Niet "gereedschap meet kwaliteit", maar: kwaliteitsdimensies spreken elkaar tegen, en iemand moet een verantwoorde keuze maken. Kwaliteit is dan geen objectieve eigenschap die je afleest, maar de uitkomst van een proces waarin belangen en prioriteiten tegen elkaar worden afgewogen. De loop verbergt die afweging niet; hij dwingt haar af en legt haar vast.

## Drie soorten kwaliteitsmechanismen

Wie "softwarekwaliteit" zegt, noemt al snel een bonte verzameling: codeconventies, coverage, SonarQube, CI/CD-pijplijnen, linters, securityscans, branchingstrategieën, definition of done, code review. Die op één hoop gooien verbergt een belangrijk onderscheid: ze werken op verschillende manieren en horen op verschillende plekken thuis. Dit raamwerk verdeelt ze in drie soorten, elk met een eigen plek in de loop en een eigen verantwoordelijke.

### 1. Geautomatiseerd en deterministisch

Coverage-drempels, SonarQube-gates, linters, type-checkers, securityscans (SAST, dependency-audits), de CI-pijplijn die test en bouwt. Dit zijn mechanismen die een machine objectief en herhaalbaar vaststelt. Er is geen oordeel nodig: de test slaagt of niet, de drempel wordt gehaald of niet.

Plek in de loop: deze checks horen vóór de menselijke en de geautomatiseerde beoordeling. Ze zijn een toegangsvoorwaarde tot de review, geen onderdeel ervan. De bouwer levert pas een overdracht aan de beoordelaars (`core/contracts/review-handoff.md`) nadat de geautomatiseerde poorten groen zijn. Schaarse beoordelingsaandacht besteden aan wat een machine al objectief kan vaststellen, is verspilling.

Verantwoordelijke: de bouwer levert het bewijs, de pijplijn handhaaft de drempel.

### 2. Conventioneel en vastgelegd

Codeconventies, commitconventies, branchingstrategie, de definition of done, naamgevingsafspraken. Dit zijn afspraken die je niet per taak opnieuw maakt. Ze liggen vast als gedeelde context en gelden voor iedereen.

Plek in de loop: deze afspraken zitten niet in één rol, maar in de gedeelde grondslag waarnaar meerdere rollen verwijzen, en in de vorm van de overdrachten (`core/contracts/`) zelf. Een contract is in feite een vastgelegde conventie over wat een overdracht moet bevatten. De branchingstrategie raakt de orkestratie: de manier waarop wijzigingen als afzonderlijke, beoordeelbare eenheden door de loop gaan.

Het inzicht hierachter: standaarden bestaan om denkruimte vrij te maken. Wie de conventie kent, hoeft niet elke keer opnieuw te bedenken hoe een commit eruitziet of wanneer iets af is, en houdt aandacht over voor het werkelijke probleem.

Verantwoordelijke: gedeeld, vastgelegd in de grondslag en bewaakt bij elke overdracht.

### 3. Oordeelsmatig en contextueel

Is dit de juiste abstractie? Past deze risicobereidheid bij deze wijziging? Is deze afwijking van de conventie hier gerechtvaardigd? Toetst deze test wel het juiste, of alleen dát er iets is uitgevoerd? Op dit soort vragen geeft geen drempel en geen scan antwoord.

Plek in de loop: dit is het domein van de beoordelaars en de menselijke poort, en het is precies wat zich niet laat automatiseren. De adversariële beoordelaar (`core/roles/reviewer-adversarial.md`) die naar het niet-afgevangen randgeval zoekt, doet iets wat een coverage-cijfer per definitie niet kan: coverage toont aan dat een regel is uitgevoerd, niet dat het juiste is getest.

Verantwoordelijke: de beoordelaars, en voor de onomkeerbare keuzes de mens bij de poort.

### De drie samen

De drie soorten vormen geen rangorde van belang, maar een opbouw. De geautomatiseerde laag is noodzakelijk maar niet voldoende. De conventionele laag neemt routinebeslissingen weg zodat de aandacht naar het moeilijke kan. De oordeelsmatige laag is waar het vakmanschap begint; die laag kan de andere twee niet overslaan, maar wordt er ook nooit door vervangen.

Hierin ligt het antwoord op een hardnekkig misverstand: dat hoge coverage of een groene SonarQube-gate samenvalt met kwaliteit. De drie lagen laten zien dat geautomatiseerde poorten tegelijk noodzakelijk en ontoereikend zijn, en dat juist in het verschil tussen die twee het oordeelsvermogen nodig wordt. Een groen vinkje is een voorwaarde om te mogen beoordelen, niet het bewijs dat de beoordeling al heeft plaatsgevonden.

## Hoe lessen zich hieraan ophangen

Dit raamwerk schrijft geen lessen voor. Het geeft elke kwaliteitsles een vaste plek om aan te haken, via steeds dezelfde vraag: welke rol draagt deze verantwoordelijkheid, en waarom juist daar?

Dat verandert het ontwerp van een les. Niet "een les over SonarQube", maar een les over wie de poortwachter is en waarom, met SonarQube als instrument. Niet "een les over Git branching", maar een les over hoe je werk in beoordeelbare eenheden opknipt en wie de samenhang bewaakt. Het mechanisme is dan nooit het onderwerp op zichzelf; het wordt begrepen vanuit zijn plaats in de verdeling van verantwoordelijkheden. Dat maakt het overdraagbaar in plaats van een losstaand weetje.

Een niet-uitputtende kaart van waar veelvoorkomende thema's aanhaken:

| Kwaliteitsthema | Soort (1/2/3) | Draagt vooral bij |
|---|---|---|
| Coverage en testdrempels | 1 | bouwer + pijplijn (poort), met de oordeelsvraag bij de adversariële beoordelaar: dekt dit het juiste? |
| CI/CD-pijplijn | 1 | pijplijn als toegangsvoorwaarde tot de review |
| Linters, type-checkers, formatters | 1 + 2 | pijplijn handhaaft, conventie bepaalt de regels |
| SonarQube en kwaliteitspoorten | 1 | pijplijn (poort); de oordeelslaag blijft bij de beoordelaars |
| Security (SAST, dependency-audit) | 1 | pijplijn voor het geautomatiseerde deel |
| Security (dreigingsmodel, ontwerpkeuzes) | 3 | adversariële beoordelaar + menselijke poort |
| Codeconventies en naamgeving | 2 | gedeelde grondslag, bewaakt bij elke overdracht |
| Commit- en branchingstrategie | 2 | orkestratie; wijzigingen als beoordeelbare eenheden |
| Definition of done | 2 | vastgelegd in de acceptatiecriteria van het bouwplan |
| Code review als oordeel | 3 | de vier beoordelaars en de hoofdbeoordelaar |
| Architectuur- en abstractiekeuzes | 3 | menselijke poort (onomkeerbaar) + onderhoudbaarheidsbeoordelaar |

De kolom "soort" verwijst naar de drie soorten hierboven. Dat sommige thema's in twee lagen staan, is geen slordigheid maar de kern van de zaak. Security is deels een scan die de pijplijn draait en deels een oordeel dat geen scan kan vellen. Wie alleen de scan ziet, mist de helft.

## Verbinding met de werkingsprincipes

Dit raamwerk staat niet los van de vier werkingsprincipes (`core/principles.md`); het rust erop.

Contextisolatie maakt de beoordeling betrouwbaar: een beoordelaar die het verkenningsverslag van de planner niet heeft gezien, oordeelt over wat er staat in plaats van over wat bedoeld was. Expliciete overdrachten zijn zelf de vastgelegde conventies van de tweede soort: een contract bepaalt wat een overdracht moet bevatten en maakt "het leek me wel goed" onmogelijk. Proportionaliteit voorkomt dat het kwaliteitsapparaat zwaarder wordt dan de taak rechtvaardigt: niet elke wijziging verdient vier beoordelaars, en de triage bewaakt dat. En de menselijke poort is precies de plek waar de oordeelsmatige laag onmisbaar blijft, omdat sommige verantwoordelijkheden niet aan een machine kunnen worden overgedragen.

De vier principes beschrijven hoe de loop werkt. Dit raamwerk beschrijft waarom die werking neerkomt op een eerlijk en daardoor leerzaam model van softwarekwaliteit: een model dat de verdeling toont in plaats van haar weg te poetsen.