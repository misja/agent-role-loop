# Eerste bronlezing en voorstelteksten voor #46

## Opdracht en status

De gebruiker gaf in deze sessie opdracht tot een beperkte onderzoeksstap:
diagnose van de twee inleidende pagina's inclusief Verder lezen, een voorstel
voor de verdeling van uitleg, een korte opening en één literatuurtoelichting.
Dit document is dat voorbereidingsresultaat. Het voert geen nieuwe norm in en
wijzigt geen gepubliceerde onderwijsinhoud. #46 als geheel is hiermee niet af.

Leesbasis: `2f8b43f085053bdee4d6ccb9c75b23f4bb9663c9`.
Normen: `teaching/conventies.md`, `doelgroep.md`, `schrijfwijzer.md` en
`begrippen.md`. Startniveau volgens de gebruiker: derdejaars die in jaar 1/2 de
eerste softwareontwikkelprincipes hebben leren kennen; kennismaking bewijst
geen zelfstandige toepassing op een nieuw werkproces. Dat is hier een
onderzoeksuitgangspunt, nog geen gewijzigde normtekst.

## Bevindingen uit de twee pagina's

Vindplaatsen verwijzen naar de gelezen versie. Dit zijn tekstbevindingen en
verwachte leesproblemen, geen geobserveerde studentresultaten.

| Vindplaats | Concreet probleem | Gevolg en te onderzoeken ingreep |
|---|---|---|
| index.md, opening en subtitel | De pagina combineert oriëntatie met vrijwel alle procesbegrippen. Vóór navigatie staan 717 woorden. | De lezer moet veel uitleg verwerken voordat de oefening zichtbaar is. Geef de startpagina één doel: het probleem en de leeractiviteit laten herkennen. Woordenaantal is een aanwijzing, geen afkeurgrens. |
| index.md, CSV-voorbeeld | Orders die tijdens export bijkomen vragen begrip van een veranderende gegevensverzameling. Het verband met dubbele orders is niet uitgewerkt. | De voorbeeldcasus wordt een tweede leerprobleem. Gebruik voor deze proef een boekenplankhandeling, die aansluit op de oefeningen. Als CSV behouden blijft, moet het relevante gedrag eerst zichtbaar worden gemaakt. |
| index.md, “De taakverdeling maakt ruimte…” | Abstracte conclusie over oplossing/bewijs, zonder nieuwe waarneembare handeling. | De zin verklaart het voordeel niet. Laat zien welke vraag de tweede lezer stelt en welke controle daardoor ontbreekt. |
| index.md, webchat tot contract | LLM, context, API, gereedschap, agent, sessie, rol, contextisolatie en contract volgen in één aanloop. | Termuitleg alleen helpt nog niet ze te gebruiken. Introduceer ze bij de eerste handeling die erom vraagt; houd de verschillen tussen model, programma en rol wel intact. |
| raamwerk, openingsalinea's | “Exportreparatie”, “expliciete overdrachten” en de lijst coverage/CI/CD/security/branching verbinden veel onderwerpen vóór een uitgewerkte taak. | De student moet samenhang aannemen. Begin met een beperkt voorbeeld van opdracht, uitvoering en controle; voeg het vakbegrip daarna toe. |
| raamwerk, “Kwaliteit is geen rol” en “Kwaliteit spreekt zichzelf tegen” | De koppen bevatten retorische stellingen die de lezer eerst moet interpreteren. | Ze helpen niet voorspellen wat de sectie uitlegt. Probeer “Wie controleert de wijziging?” en “Waarom verschillen beoordelingen?”; beoordeel de sectie-inhoud vervolgens tegen die functie. |
| raamwerk, rolverdeling en werkingsprincipes | Uitleg springt naar orkestrator, hoofdbeoordelaar, menselijke poort en softwaremodulariteit; dezelfde grenzen keren terug. | Eerder behandelde principes moeten nu op samenwerking worden toegepast. Toon eerst wie welke informatie krijgt en welk besluit volgt; verklaar pas daarna de overeenkomst met engineeringprincipes. Schrap herhaling zonder nieuwe toepassing. |
| raamwerk, drie soorten en thematabel | De hoofdtekst bevat 2145 woorden vóór Verder lezen. De tabel voegt veel tools en numerieke soortlabels toe. | Als eerste kennismaking vraagt dit veel terugzoeken. Bewaar de drie verschillen, maar licht ze aan één handeling toe. Onderzoek of de uitgebreide thematabel beter als latere naslag werkt. |
| raamwerk, Verder lezen | De vier beschrijvingen tellen 173, 94, 195 en 57 woorden inclusief titel. Ze mengen leesadvies, samenvatting, rechtvaardiging van onze aanpak en bronkritiek. | De lezer kan moeilijk kiezen wat nu bruikbaar is. Geef per bron een concrete leesvraag, passend moment/voorkennis en relevante beperking. Bronkritiek blijft waar zij het brongebruik bepaalt. |

Vooral de Alenezi-toelichting stapelt onbekende Engelse competenties,
onderwijskundige conclusies en kritiek op de publicatie. De Codex-toelichting
gebruikt onder meer “onderzochte frontier” en “these”. De Farley-toelichting
vergelijkt twee complete stelsels voordat de student ons werkproces heeft
uitgeprobeerd. De kortere Sweller-toelichting verklaart “fading” niet in gewone
handelingen. Een korte toelichting kan dus eveneens te abstract zijn.

## Voorstel voor de verdeling van uitleg

Dit is een voorstel voor planning, geen opdracht om bestaande uitleg alvast te
verwijderen. De huidige les van module 1 verwijst naar de inleiding voor model,
context, agent en sessie; module 2 gebruikt diezelfde voorkennis. Die
verwijzingen moeten samen met een eventuele verplaatsing worden aangepast.

| Plek | Functie en inhoud | Waarom daar? |
|---|---|---|
| Startpagina | Eén boekenplanksituatie, de gemiste controle en wat de student gaat oefenen; verwijzing naar module 1. | Oriëntatie vraagt nog geen complete rol- of agentarchitectuur. |
| Voorbereiding/eerste chatopdracht module 1 | Wat de chat aan informatie meekrijgt, welke eisen gelden en wat in het logboek wordt bijgehouden. | De student heeft deze kennis nodig om eigen waarnemingen te begrijpen. |
| Uitleg vóór de eerste gescheiden uitvoering in module 1 | Verschil model/uitvoerend programma, agent/sessie/rol waar gebruikt; wie plant/bouwt/beoordeelt, welke invoer/uitvoer de gebruikte contracten vragen. | Deel B en de manual adapter gebruiken deze begrippen al. Niet doorschuiven naar module 2 als de eerste oefening ze nodig heeft. |
| Module 2 | Een ingevulde overdracht onderzoeken; van dat voorbeeld naar contract, scheiding van verantwoordelijkheden en informatie verbergen. | De student heeft eerst een uitvoering gezien waarop het principe kan worden toegepast. |
| Kwaliteitsraamwerk | Compact overzicht van afspraak, automatische controle en beoordeling aan één voorbeeld; duidelijk leesmoment bij de leerlijn. | Het overzicht kan de ervaring ordenen. Het hoeft niet vooraf alle latere rollen en uitzonderingen te onderwijzen. |
| Latere lessen en naslag | Toolvergelijking, volledige referentiecontracten, brede thematabel en gerichte literatuurverdieping. | Details blijven beschikbaar wanneer de student de bijbehorende vraag heeft. |

Een nieuwe pagina of nieuw leesmoment voor het raamwerk vraagt nog een
concreet plan. De doelgroepnorm zegt nu dat de inleiding de stap naar agents
opbouwt; een andere verdeling moet dus expliciet worden besloten. De leerlijn
mag door inkorten geen ontbrekende voorbereiding krijgen.

## Voorsteltekst A: opening van de startpagina

De onderstaande boekenplanksituatie is een geconstrueerd voorbeeld, geen verslag
van een uitgevoerd programma of agentrun. Alleen de opening is voorgesteld;
navigatie en de rest van de pagina vallen buiten deze proef.

> **De ontwikkelstraat**
>
> *AI laten programmeren en de code controleren*
>
> Je laat een AI-assistent een uitleenfunctie voor een boekenplank schrijven.
> De functie moet voorkomen dat een uitgeleend boek nogmaals wordt uitgeleend.
> De assistent levert code en tests. Alle tests slagen.
>
> Je medestudent leest de tests en ziet dat ze alleen beschikbare boeken
> gebruiken. Wat gebeurt er als je hetzelfde boek een tweede keer probeert
> uit te lenen? Dat is nog niet gecontroleerd.
>
> In deze leerlijn oefen je hoe je de opdracht vastlegt, AI code laat schrijven
> en de uitkomst laat controleren. Je onderzoekt welke tests nodig zijn en
> welke vragen iemand die de code beoordeelt moet stellen. Jij beslist of de
> wijziging mag worden overgenomen.
>
> Begin bij [module 1: Ervaren](../teaching/modules/01-ervaren/index.md).

Deze opening gebruikt bekende programmeerhandelingen en één gemist geval.
De derde alinea benoemt werk in plaats van de abstracte conclusie dat
“taakverdeling ruimte maakt”. Modelaanroepen, context en rolcontracten worden
nog niet gebruikt; hun uitleg moet vóór de afhankelijke oefenstappen komen.
De menselijke mergebeslissing blijft zichtbaar, zonder hier de volledige
C4-route te behandelen. Het leerdoel is niet gereduceerd tot meer tests: ook de
opdracht en het inhoudelijke oordeel blijven onderdeel van de leerlijn.

## Voorsteltekst B: één literatuurtoelichting

> **David Farley, Modern Software Engineering.** Lees hoofdstuk 5, *Feedback*,
> als je wilt weten waarom je tijdens het ontwikkelen tussentijds
> controleert wat je hebt gemaakt. Je hebt daarvoor ervaring met programmeren
> en tests nodig. De toepassing op onze AI-werkwijze werken we in deze leerlijn uit.

De [uitgeverspagina met inhoudsopgave](https://www.informit.com/store/modern-software-engineering-doing-what-works-to-build-9780137314782)
bevestigt hoofdstuk 5 en zijn onderwerpen, waaronder feedback bij code en
integratie en vroegtijdige feedback. Controle uitgevoerd op 3 oktober 2026.
De proef wijst één leesrichting aan in plaats van twee complete raamwerken
gelijk te stellen. De vergelijking met de rollenlus is onze toepassing; dit
fragment beweert niet dat het boek die aanpak valideert. Dit is een toets van
de toelichting en leeskeuze op basis van de uitgeversinformatie, geen volledige
herbeoordeling van het boek.

Farley is hier gekozen voor één beperkte leesvraag. De andere drie bronnen
zijn nog niet inhoudelijk geverifieerd of herschreven. Vooral hun empirische
claims en bronkritiek vragen broncontrole vóór een nieuwe gepubliceerde versie.

## Concrete vragen voor beoordeling van deze proef

1. Kan de lezer uit de opening aanwijzen wat moest werken, wat is gecontroleerd
   en welk geval ontbreekt? Vraag naar die drie concrete elementen.
2. Kan de lezer benoemen wat die zelf gaat doen en beslissen? Vraag niet alleen
   om definities van “kwaliteit” of “rol”.
3. Waar wordt kennis gebruikt die nog niet is aangeboden? Controleer ook de
   voorgestelde verplaatsingen tegen de eerste oefenstappen.
4. Kan de lezer bij de literatuurtoelichting bepalen waarom en wanneer die het
   hoofdstuk zou openen? Welke voorkennis is genoemd en welke claim wordt gedaan?
5. Welke zin geeft geen nieuwe uitleg of handeling? Schrap niet blind op lengte;
   motiveer wat de student na weglaten nog kan begrijpen.

Dit zijn voorgestelde leesvragen, geen al gemeten studentbegrip. Een afzonderlijke
agentlezing kan concrete ontbrekende stappen vinden, maar stelt niet vast dat
studenten de tekst begrijpen. Studentgegevens en gemeten leestijd ontbreken.

## Vervolg en afbakening

Deze bronlezing dekt alleen de twee inleidende pagina's en de verwijzingen naar
hen vanuit module 1 en 2. De inventarisatie van de hele leerlijn, voorstel voor
normverduidelijking, volledige raamwerkproef en vervolgwerkitems uit #46 blijven
open. Ook de definitieve plaats van technische uitleg en literatuur wordt nog
besloten. Geen docs-build nodig voor deze onderzoeksregistratie buiten de site;
de gepubliceerde pagina's zijn ongewijzigd.

## Onafhankelijke beperkte lezing

Een afzonderlijke agent las de beide pagina's, normen en noodzakelijke
module 1/2-afhankelijkheden zonder maaktranscript. De lezer kan uit de
voorstelopening de uitleeneis, tests met beschikbare boeken en het gemiste
tweede-uitleengeval aanwijzen. Dat ontbrekende geval toont nog geen bug aan;
het concrete resultaat is een gevonden leemte in het testbewijs. Voor de
oriënterende opening is geen complete hersteluitvoering nodig.

De Farley-toelichting geeft volgens de lezer een leesreden, hoofdstuk,
voorkennis en begrensde toepassing. De uitgeversinhoudsopgave draagt die
leesrichting; het volledige hoofdstuk is niet beoordeeld.

Te bewaken bij verdere uitwerking: deel B gebruikt contracten al, dus ook de
praktische contractinvoer/uitvoer moet vóór dat gebruik begrijpelijk zijn.
Alleen de theorie verdiepen in module 2 is niet voldoende. De voorgestelde
verdeling benoemt het risico; de nieuwe uitlegplaatsen en verwijzingen zijn
nog niet gerealiseerd. Verder moeten model/programma, contextgrenzen en het
verschil tussen afspraak/test/oordeel inhoudelijk behouden blijven.

Binnen deze beperkte proef vond de lezer geen ontbrekende stap die de twee
voorstelteksten onbruikbaar maakt. Dit is één agentlezing, geen volledig
C6-oordeel over #46 en geen studentvalidatie. Het onderzoeksresultaat en de
[volledige onafhankelijke lezing](https://github.com/misja/agent-role-loop/issues/46#issuecomment-5973880258)
zijn bij #46 bewaard.
