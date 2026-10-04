# Kwaliteit als gedeelde verantwoordelijkheid

Je laat een AI-assistent een uitleenfunctie voor een boekenplank schrijven. De
functie moet voorkomen dat een uitgeleend boek nogmaals wordt uitgeleend. De
assistent levert code en tests. De tests gebruiken beschikbare boeken en slagen.
Een beoordelaar ziet dat een tweede uitleenpoging voor hetzelfde boek ontbreekt.
Daarmee is een leemte in het bewijs gevonden; of de code deze poging terecht
afwijst, is nog niet vastgesteld.

Dit raamwerk laat aan die situatie zien wie de wijziging controleert en wat een
afspraak, een automatische controle en een beoordeling bijdragen. De
[voorbereiding: van chat naar agent](van-chat-naar-agent.md) legt uit hoe een
agent een rol uitvoert en welke informatie een aparte beoordelaar krijgt. Hier
passen we die taakverdeling toe op de kwaliteit van een wijziging.

## Wie controleert de wijziging?

De bouwer ({core}`roles/builder.md`) voert de wijziging uit volgens het
goedgekeurde plan. Voor de uitleenfunctie maakt en voert hij tests uit. Hij
legt vast welke situaties zijn gecontroleerd, wat de verwachte uitkomsten zijn
en welke resultaten de uitvoering oplevert. Bij het beschikbare boek is de
verwachting dat de uitlening slaagt en het boek daarna als uitgeleend staat.
Dat resultaat geeft nog geen antwoord op de tweede uitleenpoging.

De beoordelaar vergelijkt de eis, de code en het testbewijs. In dit voorbeeld
vraagt hij om een test die hetzelfde boek eerst uitleent en daarna nogmaals
probeert uit te lenen. De tweede poging moet worden afgewezen en de eerste
uitlening moet behouden blijven. De bouwer voegt die test toe, voert haar uit
en draagt de verwachte en waargenomen uitkomst over. Alleen de aanwezigheid
van de test toont nog niet aan dat de code aan de eis voldoet. Accepteert de
functie bij uitvoering toch een tweede uitlening, dan is een defect aangetoond.

De rol beschrijft een taak. De bouwer levert code en bewijs; de beoordelaar
onderzoekt of dat bewijs de eis afdekt. Een rol kan door een mens of een agent
worden uitgevoerd. Aparte beoordelingsopdrachten vragen niet verplicht om
verschillende modellen. Een overdrachtscontract legt vast welke informatie de
volgende rol krijgt, maar garandeert niet dat die informatie juist of volledig
is. Zo pas je scheiding van verantwoordelijkheden toe op het samenwerken met AI:
code maken en de onderbouwing ervan beoordelen krijgen ieder een eigen taak.

Vóór het bouwen beoordeelt de verantwoordelijke mens het plan bij de
menselijke poort ({core}`roles/human-gate.md`). Hij beslist of doel, afbakening
en risico's aanvaardbaar zijn. Een onduidelijke uitleenafspraak moet daar worden
opgehelderd voordat de bouwer erop verdergaat. Dat planbesluit geeft toestemming
om te bouwen. Na uitvoering en beoordeling beslist de mens afzonderlijk over
merge: het overnemen van de wijziging. Testresultaten en beoordelingen leveren
de informatie voor dat latere besluit.

## Waarom verschillen beoordelingen?

Een beoordeling kan vaststellen dat gedrag afwijkt van een eis. Als de tweede
uitleenpoging slaagt terwijl zij moet worden afgewezen, moet dat defect worden
hersteld. De bevinding verwijst dan naar de uitleeneis, de test en de afwijkende
uitkomst. Een geslaagde test met alleen een beschikbaar boek is onvoldoende om
dit bezwaar te weerleggen.

Een beoordeling kan ook een ontwerpafweging onderzoeken. Stel dat de bouwer
in de uitleenfunctie een controle toevoegt die elders al voorkomt. Een
pragmatische beoordelaar kan die beperkte wijziging passend vinden binnen de
scope. Een beoordelaar op onderhoudbaarheid kan voorstellen om de controles
samen te brengen, zodat een latere wijziging op één plek kan worden uitgevoerd.
Dat vergroot de huidige wijziging. Beide keuzes kunnen verdedigbaar zijn;
urgentie, risico en de afgesproken scope bepalen welke afweging nodig is.

De loop kent vier beoordelaarsperspectieven. De triage kiest welke taken voor
de wijziging nodig zijn; in de oefeningen onderzoek je ze alle vier:

- De strikte beoordelaar toetst correctheid en dekking van de acceptatiecriteria.
- De pragmatische beoordelaar weegt of het resultaat binnen de afgesproken scope voldoende is om op te leveren.
- De adversariële beoordelaar zoekt randgevallen, kwetsbaarheden en aannames die kunnen falen.
- De beoordelaar op onderhoudbaarheid onderzoekt of een ander de oplossing later kan begrijpen en wijzigen.

Die opdrachten mogen tot hetzelfde oordeel leiden. Zowel de pragmatische
beoordelaar als de beoordelaar op onderhoudbaarheid kan bijvoorbeeld instemmen
met een kleine wijziging die de gedeelde controle gebruikt. Meerdere
perspectieven garanderen geen verschil van inzicht en evenmin dat elk probleem
wordt gevonden.

Bij verenigbare oordelen brengt de orkestrator de bevindingen met hun bronnen
samen. Alleen bij inhoudelijke tegenspraak onderzoekt de hoofdbeoordelaar
({core}`roles/reviewer-boss.md`) de onderbouwing. Daarbij gaan correctheid en
veiligheid vóór onderhoudbaarheid, en onderhoudbaarheid vóór afwerking. De
ontwerpafweging over gedeelde controles mag dus geen aangetoond uitleendefect
laten voortbestaan. De vastgelegde afweging laat de mens zien welke bezwaren
zijn opgelost en welke keuzes voor het mergebesluit overblijven.

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

Een agent kan deze beoordeling uitvoeren, maar agentreview werkt anders dan een deterministische controle. Het model interpreteert de aangeboden informatie en formuleert bevindingen. Het kan een relevant geval missen of een ongegrond bezwaar maken. Een bevinding moet daarom verwijzen naar de eis, de wijziging of het bewijs dat haar ondersteunt; bij tegenspraak onderzoekt de hoofdbeoordelaar die onderbouwing. Verenigbare oordelen kunnen zonder afzonderlijke hoofdbeoordelaar worden samengevoegd.

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
| Code review als oordeel | 3 | de gekozen beoordelaars; bij tegenspraak de hoofdbeoordelaar |
| Architectuur- en abstractiekeuzes | 3 | menselijke poort (doel, scope en risico) + onderhoudbaarheidsbeoordelaar |

De kolom "soort" verwijst naar de drie soorten hierboven. Een thema kan meerdere soorten omvatten. Bij security controleert een scan bijvoorbeeld op bekende kwetsbaarheden, terwijl een dreigingsmodel vraagt om beoordeling van het gebruik en mogelijke aanvallers. De gekozen scan en de interpretatie van zijn uitkomst horen daardoor bij dezelfde kwaliteitsverantwoordelijkheid.

## Verbinding met de werkingsprincipes

De vier werkingsprincipes ({core}`principles.md`) helpen om deze verantwoordelijkheden in het proces te organiseren: contextisolatie, expliciete overdrachten, proportionaliteit en de menselijke poort.

Bij de export krijgt de beoordelaar de eisen, de wijziging en het testbewijs in een eigen context. Het maakgesprek met de aanvankelijke aanname over een vaste verzameling orders gaat niet mee. Contextisolatie beperkt zo de invloed van die voorgeschiedenis. De overdracht moet wel voldoende informatie bevatten om het werk te kunnen beoordelen; ontbrekende eisen worden door isolatie niet hersteld.

Een expliciet contract maakt controleerbaar welke informatie in de overdracht wordt verwacht. Een beoordelaar kan daardoor aanwijzen dat het testbewijs of een bekende beperking ontbreekt. Het contract kan niet garanderen dat alles wat is ingevuld ook juist of volledig is. Daarvoor blijft inhoudelijke beoordeling nodig.

Proportionaliteit vraagt om een afweging vóór het werk begint. Een typefout in een melding vraagt doorgaans minder onderzoek dan een wijziging in de selectie van orders voor een financieel overzicht. De triage legt vast wie ieder acceptatiecriterium onafhankelijk beoordeelt. Bij een kleine correctie kan één beoordelaar volstaan; bij een wijziging aan een gedeeld datatype kunnen twee verschillende perspectieven nodig zijn. De uitgangsroutes en de regels voor herstel staan in {core}`loop.md`. Pragmatisch afwegen hoort bij iedere rol, ook wanneer geen aparte pragmatische beoordelaar is gekozen.

De menselijke poort bewaakt vóór het bouwen of doel, scope en risico's aanvaardbaar zijn. De mens leest het plan en laat open keuzes beantwoorden, herzien of expliciet uitstellen. Later blijft de beslissing over het samenvoegen bij de mens. De rollen en controles leveren informatie voor die beslissingen. Hun waarde moet blijken uit het uitgevoerde werk en de bevindingen, niet uit het aantal rollen of de aanwezigheid van een ingevuld contract.

## Verder lezen

- The shift to agentic AI: evidence from Codex {cite}`johnston2026codex`. Grootschalige analyse van gebruiksdata die laat zien dat agentisch werken niet "een betere chatbot" is maar een andere manier om werk te organiseren: intensieve gebruikers verschuiven hun eigen rol naar delegeren, superviseren en integreren, en de waarde ervan hangt af van het herontwerpen van workflows rond delegatie en verificatie. Het onderbouwt de these van dit raamwerk dat kwaliteit naar oordeel, supervisie en review verschuift, en laat tegelijk zien dat die volwassen werkwijze nog schaars is: de meeste gebruikers buiten de onderzochte frontier organiseren hun werk nog niet zo, wat steun geeft aan de gedachte dat dit een aan te leren praktijk is en geen vanzelfsprekendheid. Let bij gebruik op de herkomst: het is een publicatie van OpenAI over het eigen product, die de auteurs zelf als niet-representatief voor de typische organisatie kenschetsen. Die herkomst maakt de bron niet minder bruikbaar als beschrijving van hoe volwassen agentisch werk eruitziet, maar wel als iets om bewust mee te wegen, en daarmee meteen een voorbeeld van bronkritiek.
- **David Farley, Modern Software Engineering.** {cite}`farley2021modern` Lees hoofdstuk 5, *Feedback*, als je wilt weten waarom je tijdens het ontwikkelen tussentijds controleert wat je hebt gemaakt. Je hebt daarvoor ervaring met programmeren en tests nodig. De toepassing op onze AI-werkwijze werken we in deze leerlijn uit.
- Alenezi, Rethinking Software Engineering for Agentic AI Systems {cite}`alenezi2026rethinkingsoftwareengineeringagentic`. Multivocal literatuurstudie die vier kerncompetenties voor het werken met agentic AI destilleert: intent articulation, systematic verification, multi-agent orchestration, en human judgment and accountability. Die vier vallen vrijwel samen met de opbouw van deze leerlijn: het verwoorden van intentie (planner en build packet), verificatie als infrastructuur (module 3), orkestratie (de loop zelf) en het menselijke oordeel met expliciete poorten op kritieke momenten (module 5). Voor het onderwijs bepleit het paper een verschuiving van artefact-beoordeling naar procestransparantie, mondelinge verdediging en bewijs van redeneren over AI-gegenereerde output, en het beschrijft hoe AI ervaren ontwikkelaars versnelt maar beginners zonder stuur- en verificatie-ervaring juist remt; beide punten onderbouwen de didactische keuzes van dit materiaal. Let bij gebruik op de herkomst: het is een niet peer-reviewed preprint van één auteur, en de referentielijst bevat slordigheden (placeholder-nummers, vrijwel identieke titels onder verschillende auteurs), een bekend waarschuwingssignaal. Gebruik het daarom als synthese en begrippenkader, en citeer voor harde empirische claims de onderliggende studies zelf, zoals het gecontroleerde experiment van Borg e.a. waarnaar het verwijst (onderhoudbaarheid hangt af van de omringende procesinfrastructuur, niet van het generatieve model alleen). Ook dat is een oefening in bronkritiek.
- Sweller, Cognitive load during problem solving {cite}`sweller1988cognitive`. De cognitieve-belasting-theorie onderbouwt de didactische vorm die dit materiaal gebruikt: worked examples met fading, waarin vroege modules een volledig voorbeeld tonen en latere de student steeds meer zelf laten invullen. Dat verlaagt de belasting waar die niet leerzaam is en houdt haar over voor waar het oordeel geoefend moet worden.
