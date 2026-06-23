# Kwaliteit als gedeelde verantwoordelijkheid

Softwarekwaliteit is geen eigenschap die je aan het eind toevoegt, en geen enkele rol die iemand vervult, maar een verzameling verantwoordelijkheden die over een werkproces verdeeld is. Dit raamwerk maakt die gedachte expliciet en biedt daarmee de grondslag waaraan lessen over concrete kwaliteitsthema's (coverage, CI/CD, security, branchingstrategie, codeconventies) zich ophangen.

Het staat op een ander niveau dan de vier werkingsprincipes (`core/principles.md`). Die leggen uit *hoe* de rollenloop werkt: contextisolatie, expliciete overdrachten, proportionaliteit en de menselijke poort. Dit raamwerk legt uit wat die werking te zeggen heeft over kwaliteit, en waarom dat de loop tot didactisch waardevol materiaal maakt en niet slechts tot een handige manier om met AI-agents te werken.

De rollenloop maakt de verdeling van verantwoordelijkheden zichtbaar. Voor studenten is dat een zeldzame kans: kwaliteitsdenken dat normaal abstract en onzichtbaar blijft, wordt hier concreet en aanwijsbaar.

## Het centrale inzicht: kwaliteit is geen rol

In een onvolwassen beeld van software engineering is kwaliteit iets wat één persoon of één stap regelt. De tester. De review aan het eind. De linter die groen moet zijn. Studenten beginnen vaak met dit beeld, en het is begrijpelijk, want het is overzichtelijk.

De rollenloop laat een ander beeld zien. Kwaliteit is verdeeld over de hele keten, en verschillende rollen dragen er verschillende stukken van. De bouwer (`core/roles/builder.md`) is verantwoordelijk voor verifieerbaar werk: niet "het werkt op mijn machine", maar bewijs dat de change doet wat beloofd is. De vier beoordelaars (rolbestanden onder `core/roles/`) dragen elk één kwaliteitsperspectief, en die perspectieven spreken elkaar bewust tegen. De hoofdbeoordelaar (`core/roles/reviewer-boss.md`) weegt die tegenspraak en prioriteert. De menselijke poort (`core/roles/human-gate.md`) draagt de verantwoordelijkheid die niemand anders mag dragen: is dit nog steeds het juiste doel, zijn de risico's omkeerbaar.

Het didactische punt is niet dat dit een efficiënte werkverdeling is. Het is dat kwaliteit *intrinsiek* verdeeld is, en dat een proces dat doet alsof één stap het regelt, een illusie verkoopt. De loop maakt de verdeling expliciet in plaats van haar te verbergen achter een enkel groen vinkje.

## Kwaliteit spreekt zichzelf tegen

De vier beoordelaars zijn geen vier manieren om hetzelfde te zeggen. Ze belichamen kwaliteitsdimensies die in de praktijk regelmatig botsen:

- De strikte beoordelaar wil correctheid en volledige dekking van de acceptatiecriteria.
- De pragmatische beoordelaar wil opleveren en weegt of het goed genoeg is voor nu.
- De adversariële beoordelaar zoekt de niet-afgevangen randgevallen, de aannames die breken onder druk, de beveiligingsgaten.
- De beoordelaar op onderhoudbaarheid kijkt voorbij vandaag: kan een ander dit over een jaar nog begrijpen en wijzigen.

Correctheid tegen snelheid. Volledigheid tegen opleveren. Veiligheid tegen eenvoud. Onderhoudbaarheid tegen de kortste weg. Dit zijn echte spanningen, geen schijntegenstellingen, en in een volwassen team worden ze door verschillende mensen met verschillende posities vertegenwoordigd.

De hoofdbeoordelaar (`core/roles/reviewer-boss.md`) lost die spanning niet op door één perspectief gelijk te geven, maar door te prioriteren volgens een expliciete regel: correctheid en veiligheid eerst, dan onderhoudbaarheid, dan afwerking. Dat is een kwaliteitsmodel, geen smaakoordeel. En het is leerzaam juist omdat het zichtbaar maakt dat de afweging onvermijdelijk is. Er bestaat geen toestand waarin alle vier de beoordelaars tegelijk volledig hun zin krijgen.

Voor studenten is de te leren les daarom niet "gereedschap meet kwaliteit", maar iets ongemakkelijkers: kwaliteitsdimensies spreken elkaar tegen, en iemand moet verantwoord kiezen. Kwaliteit is geen objectieve eigenschap die je afleest, maar de uitkomst van een proces waarin posities en prioriteiten tegen elkaar afgewogen worden. De loop verbergt die afweging niet; hij dwingt haar af en schrijft haar op.

## Drie soorten kwaliteitsmechanismen

Wie "softwarekwaliteit" zegt, noemt al snel een bonte verzameling: codeconventies, coverage, SonarQube, CI/CD-pijplijnen, linters, securityscans, branchingstrategieën, definition of done, code review. Die op één hoop gooien is zelf een denkfout. Ze horen bij verschillende lagen, en het onderscheid is leerstof op zichzelf. Dit raamwerk verdeelt ze in drie soorten, elk met een eigen plek in de loop en een eigen verantwoordelijke.

### 1. Geautomatiseerd en deterministisch

Coverage-drempels, SonarQube-gates, linters, type-checkers, securityscans (SAST, dependency-audits), de CI-pijplijn die test en bouwt. Dit zijn mechanismen die een machine objectief en herhaalbaar vaststelt. Er is geen oordeel nodig: de test slaagt of niet, de drempel wordt gehaald of niet.

Waar in de loop: deze checks horen *vóór* de menselijke en de agentische beoordeling. Ze zijn een toegangsvoorwaarde tot review, geen onderdeel ervan. De bouwer (`core/roles/builder.md`) mag pas een overdracht naar de beoordelaars (`core/contracts/review-handoff.md`) produceren nadat de geautomatiseerde poorten groen zijn. Het zou verspilling zijn om dure menselijke aandacht te besteden aan wat een machine al objectief kan vaststellen.

Verantwoordelijke: de bouwer levert het bewijs, de pijplijn handhaaft de drempel.

### 2. Conventioneel en gestold

Codeconventies, commitconventies, branchingstrategie, de definition of done, naamgevingsafspraken. Dit zijn afspraken die je niet per taak heronderhandelt. Ze liggen vast als gedeelde context en gelden voor iedereen.

Waar in de loop: deze afspraken zitten niet in één rol, maar in de gedeelde grondslag waar meerdere rollen naar verwijzen, en in de vorm van de overdrachten (`core/contracts/`) zelf. Een contract is in feite een gestolde conventie over wat een overdracht moet bevatten. De branchingstrategie raakt de orkestratie en de manier waarop changes als afzonderlijke, beoordeelbare eenheden door de loop gaan.

Het te leren inzicht: standaarden bestaan om cognitieve last weg te nemen, niet om te pesten. Wie de conventie kent, hoeft niet elke keer opnieuw na te denken over hoe een commit eruitziet of wanneer iets af is, en kan die aandacht aan het echte probleem besteden.

Verantwoordelijke: gedeeld, vastgelegd in de grondslag en bewaakt bij elke overdracht.

### 3. Oordeelsmatig en contextueel

Is dit de juiste abstractie? Past deze risicobereidheid bij deze wijziging? Is deze afwijking van de conventie hier gerechtvaardigd? Test deze test wel het juiste, of alleen dát er iets uitgevoerd is? Dit zijn vragen waar geen drempel en geen scan antwoord op geven.

Waar in de loop: dit is het domein van de beoordelaars (`core/roles/reviewer-adversarial.md`) en de menselijke poort (`core/roles/human-gate.md`), en het is precies wat niet te automatiseren valt. De adversariële beoordelaar die naar het niet-afgevangen randgeval zoekt, doet iets wat een coverage-cijfer per definitie niet kan: coverage zegt dat een regel is uitgevoerd, niet dat het juiste getest is.

Verantwoordelijke: de beoordelaars en, voor de onomkeerbare keuzes, de mens bij de poort.

### De drie samen

De drie lagen vormen een opklimming, geen rangorde van belang. De geautomatiseerde laag is *noodzakelijk maar niet voldoende*. De conventionele laag neemt last weg zodat de aandacht naar het moeilijke kan. De oordeelsmatige laag is waar engineering-vakmanschap begint, en die laag kan de andere twee nooit overslaan, maar wordt er ook nooit door vervangen.

Hierin schuilt het krachtigste tegengif tegen een hardnekkig studentmisverstand: dat hoge coverage of een groene SonarQube-gate "kwaliteit" *is*. De loop laat zien dat geautomatiseerde poorten noodzakelijk zijn én ontoereikend, en dat het verschil tussen die twee precies de plek is waar oordeelsvermogen nodig wordt. Een groen vinkje is een voorwaarde om te mogen beoordelen, niet het bewijs dat de beoordeling al gedaan is.

## Hoe lessen zich hieraan ophangen

Dit document schrijft geen lessen voor. Het biedt elke toekomstige kwaliteitsles een vaste plek om zich aan te haken, via steeds dezelfde vraag: *welke rol draagt deze verantwoordelijkheid, en waarom juist daar?*

Dat verschuift het ontwerp van elke les. Niet "een les over SonarQube", maar "een les over wie de poortwachter is en waarom, met SonarQube als instrument". Niet "een les over Git branching", maar "een les over hoe je werk in beoordeelbare eenheden opknipt en wie de samenhang bewaakt". Het mechanisme is dan nooit het onderwerp op zichzelf; het wordt begrepen vanuit zijn plaats in een verantwoordelijkheidsverdeling. Dat is wat een mechanisme onthoudbaar en overdraagbaar maakt in plaats van een los weetje voor het tentamen.

Een niet-uitputtende kaart van waar veelvoorkomende thema's zich aanhaken:

| Kwaliteitsthema | Soort (1/2/3) | Draagt vooral bij |
|---|---|---|
| Coverage en testdrempels | 1 | bouwer + pijplijn (poort), met de oordeelsvraag bij de adversariële beoordelaar: dekt dit het juiste? |
| CI/CD-pijplijn | 1 | pijplijn als toegangsvoorwaarde tot review |
| Linters, type-checkers, formatters | 1 + 2 | pijplijn handhaaft, conventie bepaalt de regels |
| SonarQube en kwaliteitspoorten | 1 | pijplijn (poort); de oordeelslaag blijft bij de beoordelaars |
| Security (SAST, dependency-audit) | 1 | pijplijn voor het geautomatiseerde deel |
| Security (dreigingsmodel, ontwerpkeuzes) | 3 | adversariële beoordelaar + menselijke poort |
| Codeconventies en naamgeving | 2 | gedeelde grondslag, bewaakt bij elke overdracht |
| Commit- en branchingstrategie | 2 | orkestratie; changes als beoordeelbare eenheden |
| Definition of done | 2 | gestold in de acceptatiecriteria van het build packet |
| Code review als oordeel | 3 | de vier beoordelaars en de hoofdbeoordelaar |
| Architectuur- en abstractiekeuzes | 3 | menselijke poort (onomkeerbaar) + onderhoudbaarheidsbeoordelaar |

De kolom "soort" verwijst naar de drie soorten hierboven. Sommige thema's staan in twee lagen: dat is geen slordigheid maar de kern van de zaak. Security is deels een scan die de pijplijn draait en deels een oordeel dat geen scan kan vellen. Wie alleen de scan ziet, mist de helft.

## Verbinding met de werkingsprincipes

Dit raamwerk staat niet los van de vier werkingsprincipes (`core/principles.md`); het rust erop.

Contextisolatie maakt de beoordeling betrouwbaar: een beoordelaar die niet de verkenningstranscript van de planner heeft gezien, oordeelt over wat er staat, niet over wat bedoeld was. Expliciete overdrachten zijn zelf de gestolde conventies van laag 2: een contract legt vast wat een overdracht moet bevatten en maakt "het leek me wel goed" onmogelijk. Proportionaliteit voorkomt dat het kwaliteitsapparaat zwaarder wordt dan de taak rechtvaardigt: niet elke wijziging verdient vier beoordelaars, en triage bewaakt dat. En de menselijke poort is precies de plek waar de oordeelsmatige laag onmisbaar blijft, omdat sommige verantwoordelijkheden niet aan een machine overgedragen mogen worden.

De vier principes zeggen hoe de loop werkt. Dit document zegt waarom die werking neerkomt op een eerlijk, verdeeld, en daarom leerzaam model van softwarekwaliteit.
