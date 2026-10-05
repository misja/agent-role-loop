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

Bij de uitleenfunctie geldt een afspraak: een uitgeleend boek mag niet nogmaals
worden uitgeleend. Een test kan een tweede poging uitvoeren en de uitkomst
vergelijken met die afspraak. Een beoordelaar onderzoekt of de aangeleverde
tests deze situatie werkelijk afdekken. Afspraak, automatische controle en
beoordeling dragen zo ieder op een andere manier bij aan dezelfde wijziging.

### 1. Geautomatiseerd en deterministisch

De bouwer richt een test in met één beschikbaar boek. De test leent dat boek
uit, probeert het opnieuw uit te lenen en controleert twee verwachtingen: de
tweede poging wordt afgewezen en de eerste uitlening blijft behouden. Bij
uitvoering vergelijkt de test de werkelijke uitkomst met die verwachtingen.
Een afwijking laat de test falen. Bij gelijke invoer en uitvoeromstandigheden
past de test dezelfde vergelijkingsregels toe. Dat bedoelen we hier met een
deterministische controle.

Een geslaagde test levert bewijs voor de ingerichte situatie. Een test die
alleen de eerste uitlening uitvoert, kan ook slagen, maar onderzoekt de tweede
poging niet. Het coverage-rapport laat zien welke code tijdens de tests is
uitgevoerd. Uit het percentage alleen blijkt niet of beide pogingen en de
bijbehorende verwachtingen zijn gecontroleerd.

De bouwer voert de toepasselijke controles uit en bewaart de resultaten bij de
overdracht ({core}`contracts/review-handoff.md`). De pijplijn voert de ingestelde
controles opnieuw uit op de aangeboden codeversie en handhaaft de afgesproken
voorwaarden. Dat geeft de beoordelaar een vindbaar resultaat om naast de eis
en de code te leggen. De keuze van de controles blijft een vraag voor het team.

### 2. Conventioneel en vastgelegd

Het team legt de uitleenafspraak vast als eis. Daarmee kan de bouwer bepalen
welke uitkomst de test moet verwachten. Het team kan ook afspreken dat een
reparatie wordt overgedragen met de codeversie, de uitgevoerde tests, hun
resultaten en bekende beperkingen. Het contract beschrijft welke informatie
de volgende rol ontvangt.

Deze gedeelde afspraken geven richting aan het werk. Een gevulde overdracht
bewijst nog niet dat het testresultaat bij de genoemde codeversie hoort of dat
een belangrijk geval is onderzocht. De beoordelaar vergelijkt die informatie
met de bronnen.

Het team houdt de afspraken bij. Sommige afspraken kunnen automatisch worden
gecontroleerd: een linter kan bijvoorbeeld afwijkingen van afgesproken
naamgevingsregels melden. Andere vragen om inhoudelijke lezing. Een ingevuld
veld voor beperkingen laat bijvoorbeeld niet zien of de ontbrekende test van
de tweede uitleenpoging is genoemd.

### 3. Oordeelsmatig en contextueel

De beoordelaar leest de eis en de test met alleen de eerste uitlening. Hij kan
nu aanwijzen wat ontbreekt: deze test zegt niets over een tweede poging. Hij
vraagt de bouwer om de aanvullende controle en de uitgevoerde uitkomst. De
bevinding verwijst naar de uitleeneis en het ontbrekende geval. De
adversariële beoordelaar ({core}`roles/reviewer-adversarial.md`) zoekt expliciet
naar zulke randgevallen en aannames die kunnen falen.

Een agent die deze taak uitvoert, interpreteert de aangeboden informatie.
Hij kan een geval missen of een ongegrond bezwaar maken. Daarom moeten zijn
bevindingen herleidbaar zijn tot de eis, code of bewijs. Bij inhoudelijke
tegenspraak onderzoekt de hoofdbeoordelaar de onderbouwing; verenigbare
beoordelingen kunnen worden samengevoegd. De volledige route staat in
{core}`loop.md`.

Niet iedere open vraag is een defect. Als het team nog niet heeft bepaald wat
een gebruiker bij een geweigerde uitlening moet zien, kan de beoordelaar die
ontbrekende keuze aanwijzen. De verantwoordelijke mens besluit over het gewenste
gedrag. Verandert die keuze het goedgekeurde plan, dan wordt zij vastgelegd
voordat de bouwer erop verdergaat. De beoordeling levert informatie voor dat
besluit; zij vervangt het niet.

### De drie samen

De drie bijdragen zijn bij dezelfde uitleenhandeling terug te vinden:

| Bijdrage | Concrete handeling | Wat de uitkomst toelaat |
|---|---|---|
| Afspraak | Het team legt vast dat een tweede uitlening wordt afgewezen en de eerste behouden blijft. | De bouwer kan verwachte testuitkomsten bepalen. |
| Automatische controle | De bouwer voert een test met twee pogingen uit en bewaart het resultaat. | De beoordelaar kan zien of deze ingerichte situatie aan de verwachtingen voldoet. |
| Beoordeling | De beoordelaar vergelijkt eis, codeversie, tests en resultaten. | Hij kan ontbrekende dekking of een afwijking onderbouwen en de resterende vraag aan de mens voorleggen. |

Een beoordeling kan zo een ontbrekend geval aanwijzen dat de bouwer vervolgens
als test vastlegt. Bij volgende wijzigingen kan de pijplijn die verwachting
opnieuw controleren. Deze samenhang verklaart waarom zowel afspraken als
uitgevoerde controles en beoordeling nodig zijn.

Soms ontbreekt een afspraak over een gemeten waarde. Een coverage-rapport kan
bijvoorbeeld een percentage geven terwijl het team geen drempel heeft gekozen.
Het rapport meet dan dekking, maar geeft geen afgesproken afwijzingsgrens.
Heeft het team een drempel vastgelegd, dan kan de pijplijn die handhaven. Een
gehaald percentage beantwoordt nog steeds niet of de tests de tweede
uitleenpoging onderzoeken. Groen betekent dat de ingestelde controles slagen;
de beoordeling onderzoekt ook hun geschiktheid voor de wijziging.

## Verbinding met de werkingsprincipes

De werkingsprincipes ({core}`principles.md`) organiseren wie deze informatie
krijgt en wie beslist. Bij de uitleenfunctie kun je hun toepassing aanwijzen:

- **Contextisolatie:** de beoordelaar ontvangt de eis, codeversie en testbewijs
  in een eigen sessie. Het maakgesprek gaat niet mee. Zo beoordeelt hij de
  aangeleverde bronnen zonder de eerdere redenering van de bouwer over te nemen.
  Ontbrekende eisen worden hierdoor niet aangevuld.
- **Expliciete overdracht:** de bouwer noemt de gecontroleerde pogingen en
  bewaart hun verwachte en waargenomen uitkomst. De beoordelaar kan daardoor
  een ontbrekend geval aanwijzen. Een volledig ingevuld contract garandeert
  niet dat de inhoud juist is.
- **Proportionaliteit:** een typefout in een melding vraagt minder onderzoek
  dan een wijziging die de uitleenstatus verandert. De triage kiest passende
  taken en wijst ieder criterium aan een onafhankelijke beoordelaar toe.
- **Menselijke poort:** de mens beslist vooraf of het concrete plan aanvaardbaar
  is. Na uitvoering en beoordeling beslist hij afzonderlijk over merge.

Gebruik dit overzicht om de taakverdeling te herkennen. De routes, gekozen
rollen en begrensde herstelregels volgen uit {core}`loop.md`.

## Naslag: kwaliteitsthema's

Gebruik deze kaart wanneer je een projectcontrole kiest, bijvoorbeeld in
[module 6](modules/06-ontwerpen/les.md). Zoek een thema dat je al gebruikt en
bepaal welke afspraak het nodig heeft, wat het automatisch controleert en
welke vraag voor beoordeling overblijft. De kaart introduceert geen verplichte
gereedschapsset. Voor de eerste uitleg volstaat de uitleenhandeling hierboven.

| Thema | Afspraak of automatische controle | Vraag voor beoordeling en eigenaar |
|---|---|---|
| Coverage en testdrempels | Het team kiest een drempel; de pijplijn meet dekking en handhaaft die grens. | De beoordelaar onderzoekt welke relevante gevallen en verwachtingen ontbreken. |
| CI/CD-pijplijn | Het team bepaalt verplichte controles; de pijplijn voert ze op de codeversie uit. | De beoordelaar vergelijkt de resultaten met de criteria en bekende beperkingen. |
| Linters, type-checkers en formatters | Het team kiest regels voor stijl en typen; gereedschap meldt of herstelt ingestelde afwijkingen. | De beoordelaar onderzoekt wat de regels over het bedoelde gedrag openlaten. |
| SonarQube en kwaliteitspoorten | Het team kiest regels en grenzen; de pijplijn handhaaft de ingestelde poort. | De beoordelaar onderzoekt de geschiktheid en ontbrekende dekking van die controles. |
| Securityscans en dependency-audits | Een scan controleert code of gebruikte pakketten volgens regels en beschikbare kwetsbaarheidsgegevens. | De adversariële beoordelaar onderzoekt risico's van gebruik en ontwerp die de scan niet afdekt. Nieuwe gegevens kunnen de scanuitkomst veranderen. |
| Codeconventies en naamgeving | Het team legt afspraken vast; een linter kan een deel automatisch controleren. | Bouwer en beoordelaar vergelijken het werk met de overige afspraken. |
| Commit- en branchingstrategie | Het team bepaalt hoe een wijziging afzonderlijk beschikbaar komt. | De orkestrator bewaakt welke versie wordt beoordeeld en haar samenhang met ander werk. |
| Definition of done | Het team legt vast waaraan opgeleverd werk moet voldoen. | De beoordelaar onderzoekt bewijs voor de toepasselijke voorwaarden. |
| Code review | De geselecteerde beoordelaars onderzoeken toegewezen criteria. | Bij inhoudelijke tegenspraak onderzoekt de hoofdbeoordelaar de onderbouwing. |
| Architectuur en abstracties | Het plan beschrijft de gekozen verdeling van verantwoordelijkheden. | De onderhoudbaarheidsbeoordelaar onderzoekt wijzigbaarheid; de mens beslist over doel, scope en risico. |

Een thema kan meerdere bijdragen hebben. Een naamgevingsafspraak is vastgelegd
én gedeeltelijk automatisch te controleren. Bij security kan het team daarnaast
een dreigingsmodel maken: een beschrijving van mogelijke aanvallers, hun doelen
en wat zij kunnen bereiken. De adversariële beoordelaar gebruikt dat model om
risico's te onderzoeken. Een scanresultaat alleen beantwoordt die ontwerpvraag
niet.

## Verder lezen

Kies een bron op de vraag die je wilt onderzoeken. De toelichtingen noemen
welke eerdere uitleg helpt en wat je uit de bron kunt afleiden.

- **The shift to agentic AI: evidence from Codex.** {cite}`johnston2026codex`
  Lees de introductie en conclusie als je na de voorbereiding wilt onderzoeken
  hoe gebruikers taken aan agents delegeren en resultaten beoordelen. De studie
  beschrijft gebruik van Codex bij individuele gebruikers, organisaties en
  OpenAI-medewerkers. Het is onderzoek van OpenAI over het eigen product;
  de interne werkomgeving is volgens de auteurs niet representatief voor een
  doorsnee organisatie. Gebruik het als beschrijving van waargenomen werkpraktijken,
  niet als bewijs dat onze rollenlus betere software oplevert.
- **David Farley, Modern Software Engineering.** {cite}`farley2021modern` Lees hoofdstuk 5, *Feedback*, als je wilt weten waarom je tijdens het ontwikkelen tussentijds controleert wat je hebt gemaakt. Je hebt daarvoor ervaring met programmeren en tests nodig. De toepassing op onze AI-werkwijze werken we in deze leerlijn uit.
- **Alenezi, Rethinking Software Engineering for Agentic AI Systems.**
  {cite}`alenezi2026rethinkingsoftwareengineeringagentic` Lees secties 4 en 5.1
  nadat je een overdracht en beoordeling hebt uitgevoerd. Welke taken moet een
  ontwikkelaar volgens de auteur zelf blijven beheersen? Het artikel verbindt
  literatuur en praktijkperspectieven aan voorstellen voor vaardigheden en
  onderwijs. Het is een preprint, een onderzoeksversie zonder hier vastgestelde
  peer review. De auteur noemt het voorgestelde raamwerk conceptueel en nog te
  toetsen. Bovendien bevatten bronverwijzingen onvolledige nummers, zoals
  `2503.XXXXX`. Gebruik het voor discussie over de voorstellen; controleer
  claims over gemeten effecten in de oorspronkelijke studies voordat je ze
  overneemt.
- **Sweller, Cognitive load during problem solving: Effects on learning.**
  {cite}`sweller1988cognitive` Lees het abstract als je na de oefeningen wilt
  onderzoeken waarom zelfstandig een oplossing zoeken niet vanzelf tot leren
  leidt. Je kunt daarbij je ervaring met een uitgewerkt voorbeeld gebruiken.
  Sweller bespreekt hoe de aandacht die probleemoplossen vraagt het opbouwen
  van bruikbare kennis kan hinderen. De afnemende begeleiding in onze modules,
  waarbij je steeds meer zelf invult, is een ontwerpkeuze van dit materiaal.
  Het abstract toont geen leereffect van deze AI-oefeningen aan.
