# Kwaliteit als gedeelde verantwoordelijkheid

Bij de exportreparatie uit de [inleiding](index.md) zijn verschillende kwaliteitsvragen aan de orde. Het team moet afspreken welke orders in het bestand horen. De bouwer moet aantonen dat de reparatie die afspraak volgt. De beoordelaar onderzoekt of de tests daarvoor voldoende bewijs leveren. Als tijdens een export orders kunnen bijkomen, kan een geslaagde test met een vaste verzameling orders een relevante situatie onbesproken laten.

Dit raamwerk gebruikt die werkverdeling om kwaliteitsthema's als coverage, CI/CD, security, branchingstrategie en codeconventies met elkaar te verbinden. De rollenloop organiseert het werk met afzonderlijke opdrachten en expliciete overdrachten. De inleiding legt uit hoe een agent een rol kan uitvoeren en waarom elke rol een eigen context krijgt. Hier onderzoeken we welke verantwoordelijkheid bij welke rol hoort en wat afspraken, automatische controles en beoordeling elk bijdragen.

## Kwaliteit is geen rol

De bouwer ({core}`roles/builder.md`) levert verifieerbaar werk. Bij de exportreparatie betekent dat: de wijziging uitvoeren volgens het goedgekeurde plan, de afgesproken controles uitvoeren en vastleggen wat daarmee wel en niet is onderzocht. Een testresultaat dat alleen meldt dat alles slaagt, is voor de volgende rol minder bruikbaar dan bewijs waaruit ook blijkt welke situatie is getest.

De beoordelaars onderzoeken het resultaat vanuit verschillende kwaliteitsperspectieven. Zij kunnen bijvoorbeeld vaststellen dat een acceptatiecriterium ontbreekt in de tests of dat de reparatie moeilijk te onderhouden wordt. De hoofdbeoordelaar ({core}`roles/reviewer-boss.md`) brengt hun bevindingen samen, behandelt eventuele meningsverschillen en geeft één eindoordeel over het werk.

Aan die uitvoering gaat een menselijke keuze vooraf. Bij de menselijke poort ({core}`roles/human-gate.md`), tussen plannen en bouwen, beoordeelt de verantwoordelijke mens het doel, de afbakening en de risico's van het plan. Voor de export kan nog onduidelijk zijn of het bestand alleen de orders van het startmoment moet bevatten. De mens laat dit met gebruikers afstemmen en vastleggen voordat de bouwer een oplossing op een aanname baseert. Deze werkwijze veronderstelt dat die mens voldoende zicht heeft op het gebruik en de bevoegdheid heeft om de keuze te maken. Zo nodig moet eerst iemand anders worden geraadpleegd.

Deze verdeling past bekende engineeringprincipes toe op het proces. Scheiding van verantwoordelijkheden geeft de bouwer en de beoordelaar ieder een eigen taak. Contracten vormen hun interfaces. Informatie verbergen begrenst wat van het ene werkproces naar het andere gaat. Parnas behandelt informatie verbergen bij het opdelen van software in modules {cite}`parnas1972criteria`; hier passen we dat principe toe op rollen en overdrachten. De overeenkomst helpt om het proces te ontwerpen, maar bewijst op zichzelf geen kwaliteitsverbetering.

## Kwaliteit spreekt zichzelf tegen

Een reparatie kan correct werken en tegelijk extra onderhoud vragen. Stel dat de bouwer voor de export een aparte controle op dubbele orders toevoegt, terwijl elders al vergelijkbare logica bestaat. Een beperkte reparatie kan snel beschikbaar zijn; het samenbrengen van de logica kan toekomstige wijzigingen eenvoudiger maken, maar vergroot de huidige wijziging. Welke keuze passend is, hangt onder meer af van de urgentie en het risico van die uitbreiding.

De vier beoordelaars in de volledige loop onderzoeken zulke vragen vanuit een eigen opdracht:

- De strikte beoordelaar toetst de correctheid en de dekking van de acceptatiecriteria.
- De pragmatische beoordelaar weegt of het resultaat binnen de afgesproken scope voldoende is om op te leveren.
- De adversariële beoordelaar zoekt randgevallen, kwetsbaarheden en aannames die kunnen falen.
- De beoordelaar op onderhoudbaarheid onderzoekt of een ander de oplossing later kan begrijpen en wijzigen.

Die perspectieven kunnen botsen. De pragmatische beoordelaar kan de beperkte reparatie aanvaarden, terwijl de beoordelaar op onderhoudbaarheid de dubbele logica wil laten herstellen. Ze kunnen ook tot dezelfde conclusie komen, bijvoorbeeld wanneer een kleine aanpassing beide bezwaren wegneemt. Vier opdrachten garanderen geen verschil van inzicht en evenmin dat alle problemen worden gevonden.

De hoofdbeoordelaar behandelt meningsverschillen aan de hand van de bevindingen en het bewijs. De vaste prioriteit is correctheid en veiligheid, daarna onderhoudbaarheid, daarna afwerking. Bij de export moet dus eerst duidelijk zijn of de reparatie het afgesproken gedrag ondersteunt. Een voorstel om de code verder op te schonen wordt vervolgens binnen de goedgekeurde scope gewogen. De vastgelegde afweging maakt voor de mens zichtbaar waarom een bevinding wel of niet tot herstel leidt.

## Drie soorten kwaliteitsmechanismen

Een codeconventie, een test in de pijplijn en een beoordeling kunnen allemaal over dezelfde wijziging gaan. Toch beantwoorden ze verschillende vragen. De conventie legt een verwachting vast, de test controleert een vooraf bepaalde situatie en de beoordeling onderzoekt onder meer of die verwachting en controle passend zijn. Dit raamwerk onderscheidt daarom drie soorten mechanismen.

### 1. Geautomatiseerd en deterministisch

Een test kan voor een gegeven verzameling orders controleren of iedere order eenmaal in het exportbestand voorkomt. Bij gelijke invoer en uitvoeromstandigheden vergelijkt hij het resultaat volgens dezelfde regels met de verwachte uitkomst. Ook linters, type-checkers en ingestelde coverage-drempels voeren vooraf bepaalde controles uit. Securityscans en dependency-audits controleren op basis van hun regels en beschikbare gegevens; een gewijzigde kwetsbaarhedendatabase kan hun uitkomst veranderen.

Het oordeel over wat gecontroleerd moet worden, gaat aan die uitvoering vooraf. Een geslaagde exporttest met een vaste verzameling orders levert bewijs voor die ingerichte situatie. Hij vertelt niet wat er gebeurt als tijdens de export orders bijkomen. Coverage laat zien welke code tijdens tests is uitgevoerd; uit het cijfer alleen blijkt niet of het relevante gebruiksgeval is onderzocht.

In de loop voert de bouwer de toepasselijke automatische controles uit voordat hij het werk overdraagt aan de beoordelaars ({core}`contracts/review-handoff.md`). De bouwer levert het bewijs en de pijplijn handhaaft de ingestelde voorwaarden. Daardoor kunnen beoordelaars zich richten op vragen waarvoor de uitkomst van die controles alleen onvoldoende is, zoals de geschiktheid van de tests.

### 2. Conventioneel en vastgelegd

Het team kan afspreken dat iedere reparatie testbewijs bij de overdracht bevat. Die afspraak maakt duidelijk wat de bouwer moet aanleveren en wat de beoordelaar mag verwachten. Het contract legt de vorm van die overdracht vast. Dat er testbewijs aanwezig is, zegt nog niet of een belangrijk gebruiksgeval is afgedekt.

Ook codeconventies, een branchingstrategie en een definition of done zijn gedeelde afspraken. Ze voorkomen dat iedere taak opnieuw begint met de vraag hoe werk wordt aangeleverd. De branchingstrategie bepaalt bijvoorbeeld hoe de exportreparatie als afzonderlijke wijziging beschikbaar komt voor beoordeling. Meerdere rollen gebruiken dezelfde grondslag en controleren bij hun overdracht of eraan is voldaan.

Het team is verantwoordelijk voor het vastleggen en bijhouden van deze afspraken. Sommige zijn automatisch te controleren, zoals naamgevingsregels met een linter. Andere vragen om lezing, zoals de afspraak dat bekende beperkingen in een overdracht staan: een gevuld tekstveld toont nog niet aan dat de relevante beperking is genoemd.

### 3. Oordeelsmatig en contextueel

De beoordelaar leest de exporttest en merkt op dat de verzameling orders onveranderd blijft. Omdat gebruikers tijdens een export orders kunnen invoeren, vraagt hij om aanvullend bewijs. Hier bepaalt de beoordeling welke situatie nog onderzocht moet worden. De adversariële beoordelaar ({core}`roles/reviewer-adversarial.md`) heeft expliciet de opdracht zulke randgevallen en aannames te zoeken.

Een agent kan deze beoordeling uitvoeren, maar agentreview werkt anders dan een deterministische controle. Het model interpreteert de aangeboden informatie en formuleert bevindingen. Het kan een relevant geval missen of een ongegrond bezwaar maken. Een bevinding moet daarom verwijzen naar de eis, de wijziging of het bewijs dat haar ondersteunt; de hoofdbeoordelaar weegt haar bij het samenvoegen van de oordelen.

Er kan ook een vraag ontstaan waarvoor de eis zelf nog onvoldoende is bepaald: moeten later toegevoegde orders in deze export terechtkomen of in de volgende? Een agent kan opties en gevolgen beschrijven. De verantwoordelijke mens beoordeelt het gewenste gedrag met kennis van het gebruik. Als die keuze het goedgekeurde plan verandert, moet zij eerst worden vastgelegd voordat de bouwer daarop verdergaat. De menselijke verantwoordelijkheid omvat dus ook het doel en de afbakening, naast keuzes met onomkeerbare gevolgen.

### De drie samen

Een oordeel kan aanleiding geven tot een afspraak en vervolgens tot een automatische controle. Het team besluit bijvoorbeeld dat de export alleen orders bevat die bij de start aanwezig waren. Het legt dat gedrag vast als eis. De bouwer maakt vervolgens een test waarin tijdens de export een order wordt toegevoegd, met een verwachte uitkomst die uit die eis volgt. Bij volgende wijzigingen kan de pijplijn dezelfde verwachting opnieuw controleren.

```mermaid
:caption: Van een inhoudelijke keuze naar een vastgelegde en controleerbare verwachting.

flowchart LR
    O["Oordeel<br>welke orders horen in de export?"] --> C["Conventie<br>het afgesproken gedrag ligt vast"] --> A["Automatisering<br>een test controleert dat gedrag"]
```

Deze beweging sluit aan bij Farleys nadruk op leren via feedback en kleine, verifieerbare stappen {cite}`farley2021modern`. De toepassing op de rollenloop is die van dit materiaal; Farley beschrijft geen werkwijze voor AI-agents. Niet elke afweging laat zich volledig in een test vastleggen. Bovendien kan veranderd gebruik aanleiding geven om de afspraak opnieuw te beoordelen.

Soms is er nog geen norm. Een coverage-rapport kan bijvoorbeeld een percentage geven terwijl het team geen drempel heeft afgesproken. Het rapport meet dan wel de dekking, maar bepaalt niet of de wijziging daarop mag worden afgewezen. Na een afgesproken drempel kan de pijplijn die voorwaarde handhaven. Ook dan blijft de vraag of de tests zinvolle verwachtingen controleren. Een groen resultaat betekent dat de ingestelde controles slagen; de beoordeling van de wijziging volgt daarna.

## Hoe lessen zich hieraan ophangen

Bij elk kwaliteitsthema kun je onderzoeken welke verantwoordelijkheid het ondersteunt en wie die draagt. In een les over SonarQube gaat het bijvoorbeeld om de keuze van regels, de handhaving door de pijplijn en de vragen die voor beoordeling overblijven. Bij Git branching onderzoek je hoe een wijziging afzonderlijk beoordeelbaar wordt en wie de samenhang met ander werk bewaakt. Zo kun je de werkwijze ook toepassen wanneer een team ander gereedschap gebruikt.

De volgende kaart verbindt veelvoorkomende thema's met de drie soorten mechanismen:

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
| Architectuur- en abstractiekeuzes | 3 | menselijke poort (doel, scope en risico) + onderhoudbaarheidsbeoordelaar |

De kolom "soort" verwijst naar de drie soorten hierboven. Een thema kan meerdere soorten omvatten. Bij security controleert een scan bijvoorbeeld op bekende kwetsbaarheden, terwijl een dreigingsmodel vraagt om beoordeling van het gebruik en mogelijke aanvallers. De gekozen scan en de interpretatie van zijn uitkomst horen daardoor bij dezelfde kwaliteitsverantwoordelijkheid.

## Verbinding met de werkingsprincipes

De vier werkingsprincipes ({core}`principles.md`) helpen om deze verantwoordelijkheden in het proces te organiseren: contextisolatie, expliciete overdrachten, proportionaliteit en de menselijke poort.

Bij de export krijgt de beoordelaar de eisen, de wijziging en het testbewijs in een eigen context. Het maakgesprek met de aanvankelijke aanname over een vaste verzameling orders gaat niet mee. Contextisolatie beperkt zo de invloed van die voorgeschiedenis. De overdracht moet wel voldoende informatie bevatten om het werk te kunnen beoordelen; ontbrekende eisen worden door isolatie niet hersteld.

Een expliciet contract maakt controleerbaar welke informatie in de overdracht wordt verwacht. Een beoordelaar kan daardoor aanwijzen dat het testbewijs of een bekende beperking ontbreekt. Het contract kan niet garanderen dat alles wat is ingevuld ook juist of volledig is. Daarvoor blijft inhoudelijke beoordeling nodig.

Proportionaliteit vraagt om een afweging vóór het werk begint. Een typefout in een melding vraagt doorgaans minder onderzoek dan een wijziging in de selectie van orders voor een financieel overzicht. De triage bepaalt welk pad bij de omvang en het risico past; de volledige bezetting met vier beoordelaars is niet voor elke taak nodig.

De menselijke poort bewaakt vóór het bouwen of doel, scope en risico's aanvaardbaar zijn. De mens leest het plan en laat open keuzes beantwoorden, herzien of expliciet uitstellen. Later blijft de beslissing over het samenvoegen bij de mens. De rollen en controles leveren informatie voor die beslissingen. Hun waarde moet blijken uit het uitgevoerde werk en de bevindingen, niet uit het aantal rollen of de aanwezigheid van een ingevuld contract.

## Verder lezen

- The shift to agentic AI: evidence from Codex {cite}`johnston2026codex`. Grootschalige analyse van gebruiksdata die laat zien dat agentisch werken niet "een betere chatbot" is maar een andere manier om werk te organiseren: intensieve gebruikers verschuiven hun eigen rol naar delegeren, superviseren en integreren, en de waarde ervan hangt af van het herontwerpen van workflows rond delegatie en verificatie. Het onderbouwt de these van dit raamwerk dat kwaliteit naar oordeel, supervisie en review verschuift, en laat tegelijk zien dat die volwassen werkwijze nog schaars is: de meeste gebruikers buiten de onderzochte frontier organiseren hun werk nog niet zo, wat steun geeft aan de gedachte dat dit een aan te leren praktijk is en geen vanzelfsprekendheid. Let bij gebruik op de herkomst: het is een publicatie van OpenAI over het eigen product, die de auteurs zelf als niet-representatief voor de typische organisatie kenschetsen. Die herkomst maakt de bron niet minder bruikbaar als beschrijving van hoe volwassen agentisch werk eruitziet, maar wel als iets om bewust mee te wegen, en daarmee meteen een voorbeeld van bronkritiek.
- Farley, Modern Software Engineering {cite}`farley2021modern`. Het hoofdanker onder de werkwijze. De twee pijlers van dit boek, optimaliseren voor het beheersen van complexiteit (modulariteit, scheiding van verantwoordelijkheden, informatie verbergen) en optimaliseren voor leren (feedback, kleine stappen, empirie), vallen vrijwel samen met de fundamenten van de loop: contextisolatie en contracten als interface enerzijds, changes als kleine, beoordeelbare eenheden met verificatiebewijs anderzijds. De these is niet dat dit een nieuwe methodologie is, maar dat het gevestigde principes toepast op een nieuwe situatie, een AI als bouwer. Farley schreef niet over AI-agents; juist daarom is de overeenkomst veelzeggend.
- Alenezi, Rethinking Software Engineering for Agentic AI Systems {cite}`alenezi2026rethinkingsoftwareengineeringagentic`. Multivocal literatuurstudie die vier kerncompetenties voor het werken met agentic AI destilleert: intent articulation, systematic verification, multi-agent orchestration, en human judgment and accountability. Die vier vallen vrijwel samen met de opbouw van deze leerlijn: het verwoorden van intentie (planner en build packet), verificatie als infrastructuur (module 3), orkestratie (de loop zelf) en het menselijke oordeel met expliciete poorten op kritieke momenten (module 5). Voor het onderwijs bepleit het paper een verschuiving van artefact-beoordeling naar procestransparantie, mondelinge verdediging en bewijs van redeneren over AI-gegenereerde output, en het beschrijft hoe AI ervaren ontwikkelaars versnelt maar beginners zonder stuur- en verificatie-ervaring juist remt; beide punten onderbouwen de didactische keuzes van dit materiaal. Let bij gebruik op de herkomst: het is een niet peer-reviewed preprint van één auteur, en de referentielijst bevat slordigheden (placeholder-nummers, vrijwel identieke titels onder verschillende auteurs), een bekend waarschuwingssignaal. Gebruik het daarom als synthese en begrippenkader, en citeer voor harde empirische claims de onderliggende studies zelf, zoals het gecontroleerde experiment van Borg e.a. waarnaar het verwijst (onderhoudbaarheid hangt af van de omringende procesinfrastructuur, niet van het generatieve model alleen). Ook dat is een oefening in bronkritiek.
- Sweller, Cognitive load during problem solving {cite}`sweller1988cognitive`. De cognitieve-belasting-theorie onderbouwt de didactische vorm die dit materiaal gebruikt: worked examples met fading, waarin vroege modules een volledig voorbeeld tonen en latere de student steeds meer zelf laten invullen. Dat verlaagt de belasting waar die niet leerzaam is en houdt haar over voor waar het oordeel geoefend moet worden.
