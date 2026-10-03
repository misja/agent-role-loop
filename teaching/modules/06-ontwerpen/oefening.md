# Ontwerp en verantwoord een interface-uitbreiding

## Wat je gaat doen

Je ontwerpt een interface op je bestaande boekenplanklogica en laat de AI de
uitbreiding bouwen. Je legt zelf de gewenste functionaliteit, normen en
werkwijze vast. Daarna laat je het resultaat onafhankelijk beoordelen en
onderbouw je je menselijke besluit over de merge.

**Duur:** circa vier uur, verdeeld over een ontwerpsessie en een bouw- en
beoordelingssessie. Dit is een tijdindicatie; je gekozen scope en voorbereiding
bepalen hoeveel werk nodig is.
**Inleveren:** de repository met je code en het dossier onderaan deze pagina.

## Voorbereiding

Rond modules 1 tot en met 5 af. Gebruik de uitleg over
[overdrachten en contextisolatie](../02-begrijpen/les.md),
[testbewijs](../03-machine/les.md) en de
[menselijke poort](../05-poort/les.md). Houd {core}`loop.md`,
{core}`contracts/work-item.md` en het
[kwaliteitsraamwerk](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md) bij de
hand.

Je hebt Git, werkende boekenplanklogica met de bijbehorende tests en een
AI-omgeving nodig waarin je afzonderlijke sessies kunt starten. Geef een
beoordelingssessie de vereiste bronnen, zonder het maakgesprek. Zoek voor je
gekozen interface de installatie- en aanroepinstructies op in de officiële
documentatie van die stack; deze oefening schrijft geen complete toolstack voor.

### Kies je basis

Je uitbreiding bouwt voort op een bestaande logica-laag. Daardoor kun je later
beoordelen of de interface de regels hergebruikt of opnieuw implementeert.

1. **Standaard:** gebruik je eigen Pythonboekenplank uit oefening 1, deel B, en
   bouw er een [Textual](https://textual.textualize.io/)-interface op.
2. **Eigen stack:** kies een andere taal of interfacevorm, zolang je voortbouwt
   op je bestaande logica-laag.
3. **Terugvaloptie:** gebruik de
   [boekenplankcode](https://github.com/misja/agent-role-loop/blob/main/teaching/cases/module5-verwijderen/boekenplank.py)
   en [tests](https://github.com/misja/agent-role-loop/blob/main/teaching/cases/module5-verwijderen/test_boekenplank.py)
   uit `teaching/cases/module5-verwijderen/`. De
   [oefening van module 5](../05-poort/oefening.md) beschrijft hoe je deze tests
   uitvoert en welke grenzen het geheugenmodel heeft.

Controleer vóór je uitbreiding dat de bestaande tests uitvoerbaar zijn. Bewaar
de basiscommit en de uitkomsten voor de vergelijking met je latere versie.

### Richt je projectomgeving in

Werk standaard in een eigen repository met een issue, PR en gekoppeld
projectbord. Gebruik de
[beginstappen](../../praktijk/van-werkitem-naar-pull-request.md)
uit het praktijkvoorbeeld voor de handelingen op GitHub. Neem hier je eigen
boekenplank als basis en schrijf je eigen opdracht; de voorbeeldbundel en
filterpatch zijn geen onderdeel van dit mini-project.

In het praktijkvoorbeeld beslist een medestudent over het plan. In deze
individuele oefening ben je zelf de menselijke besluitnemer bij C4 en bij de
merge. De geselecteerde opleveringsbeoordeling gebeurt in een afzonderlijke
agentcontext. Bewaar die C6 als agentbeoordeling en je eigen besluit als een
apart, herkenbaar menselijk besluit. Een eigen mergebesluit is iets anders dan
je eigen PR met de GitHub-reviewhandeling *Approve* goedkeuren.

Een andere projectomgeving mag als zij dezelfde functies beschikbaar maakt:
opdracht en versies bewaren, besluiten en bewijs koppelen, de code vergelijken,
onafhankelijk beoordelen en voortgang tonen. Controleer vooraf je rechten en
de vindplaatsen van die bronnen. Leg de overeenkomst vast met de
[bronmapping](../../praktijk/van-werkitem-naar-pull-request.md).

## Stappen

1. **Ontwerp de uitbreiding en schrijf C0 in je issue.** Kies een beperkt aantal
   interfacehandelingen, bijvoorbeeld boeken tonen en één uitleenhandeling.
   Schrijf zelf de gewenste uitkomsten en toetsbare acceptatiecriteria volgens
   {core}`contracts/work-item.md`. Geef aan welke bestaande regels behouden
   moeten blijven. Koppel het issue aan je bord.

   Klaar wanneer de gewenste functionaliteit en scope te beoordelen zijn zonder
   al één implementatie voor te schrijven.

2. **Leg je projectnormen vast.** Schrijf een conventiedocument in je repository
   met keuzes voor stijl, type checking, linting, formattering en projectbeheer.
   Verantwoord ook welke middelen je achterwege laat. Configureer de gekozen
   controles of leg vast wanneer dat in het bouwplan gebeurt. Bewaar de normversie
   en geef haar leesbaar mee aan de rollen.

   Klaar wanneer een beoordelaar kan aanwijzen welke regels gelden, welke
   automatische controles ze toetsen en welke vragen een oordeel nodig hebben.

3. **Leg de bronnen en toolkeuze vast.** Wijs in je issue aan waar opdracht,
   planversies, besluiten en code staan. Gebruik de PR voor oplevering en review,
   en het bord voor status. Onderbouw je toolkeuze met toegang, opslag en de
   gegevens die bij een verhuizing mee moeten.

   Klaar wanneer een andere lezer de geldende bronnen kan vinden en je kunt
   uitleggen welke gegevens een Git-clone of Markdown-kopie niet bewaart.

4. **Kies de route en geef zo nodig C4.** Leg in C1 omvang, risico, normversie,
   uitvoerders en de toewijzing van ieder criterium aan een beoordelaar vast.
   Gebruik `LIGHT`, `PLANNED` of `REJECT` volgens {core}`loop.md`. Bij `REJECT`
   verduidelijk of splits je de opdracht voordat je verdergaat. Bij `PLANNED`
   laat je de planner C2 maken en, als C1 dat selecteert, een afzonderlijke
   verhelderaar C3. Beslis als mens over het concrete plan vóór de bouw. Bewaar
   de planversie met een vaste commitlink en leg je C4 met reden vast. Bij
   `LIGHT` is C4 vooraf nodig bij een nieuw doel, contract- of normkeuze of
   onomkeerbare gevolgen; routinematige C4, C2 en C3 worden overgeslagen.

   Klaar wanneer de route onderbouwd is, ieder criterium een bevoegde
   onafhankelijke beoordelaar heeft en het vereiste menselijke besluit naar het
   juiste artefact verwijst. Een nieuwe doel- of risicokeuze vraagt een nieuw
   menselijk besluit.

5. **Laat bouwen en verzamel bewijs.** Werk op een branch vanaf de basiscommit.
   Geef de bouwer C0 en C1 bij `LIGHT`, of het goedgekeurde C2 met C1 en C4 bij
   `PLANNED`, plus code en normen. Laat de afgesproken verificatie uitvoeren.
   Bij gedragwijzigingen in geteste code is test-first de standaard: de eerste
   test mag falen voordat de implementatie volgt. Groen is nodig voor de
   afgesproken opleveringscontroles, niet vóór iedere bouwstap. Bewaak de scope
   en noteer je ingrepen. Open een PR met C5, de exacte codecommit, basiscommit,
   bewijs en links naar de besluiten en het issue.

   Klaar wanneer de criteria met passend bewijs zijn onderbouwd en de
   oplevering vermeldt welke controles zijn uitgevoerd en wat niet is
   vastgesteld.

6. **Laat onafhankelijk beoordelen en beslis over merge.** Geef iedere
   geselecteerde beoordelingssessie C5-kern, de toegewezen criteria, relevante
   besluiten, code en leesbare normen. Geef het maakgesprek en andere oordelen
   niet mee. Laat architectuur en onderhoudbaarheid expliciet beoordelen:
   welke aanroepen hergebruiken de logica en welke regels zijn gekopieerd?
   Bewaar iedere C6 met de exacte reviewcommit. Eén C6 is het eindoordeel; bij
   meerdere oordelen volgt C7. Voeg verenigbare oordelen samen; laat inhoudelijke
   tegenspraak door de hoofdbeoordelaar onderzoeken.

   Handel blokkades af volgens de vastgelegde herstelgrenzen: hoogstens één
   automatische ontwerp- en één opleveringsherstelronde per werkitem. Bewaar de
   stand vóór herstel; herbeoordeling krijgt de expliciete herstelbijlage. Een
   resterende blokkade vraagt daarna een menselijk besluit over begrensd vervolg,
   splitsen of stoppen. `SHIP` of `SHIP WITH NITS` maakt de wijziging gereed voor
   jouw menselijke mergebesluit. Leg dat besluit afzonderlijk vast voor de
   beoordeelde commit en wijs vervolgwerk voor eventuele nits aan. Na merge
   controleer je de issue- en bordstatus.

   Klaar wanneer je de beoordelingen, je eigen architectuuranalyse en je
   mergebesluit met bronnen hebt vastgelegd. Bij een blokkade eindigt deze stap
   met het vastgelegde vervolg- of stopbesluit, zonder merge.

## Verantwoordingsvragen

Beantwoord schriftelijk:

1. Welke verantwoordelijkheid lag bij afspraken, automatische controles en
   oordeel? Wijs voor één norm de keuze, vastlegging en eventuele automatisering
   aan.
2. Welke projectafspraak had je anders kunnen kiezen? Onderbouw jouw keuze en
   beschrijf het gevolg van het alternatief.
3. Bleek je routekeuze passend bij de omvang en risico's? Wat zou je bij een
   grotere uitbreiding aanpassen?
4. Welk doel of risico moest jij als menselijke besluitnemer afwegen? Welke
   informatie leverden de controles en beoordelingen daarvoor, en welke vraag
   bleef open?

## Inleveren: het dossier

Lever de repository en een dossier met de volgende vindplaatsen in:

1. C0 en het conventiedocument met je normkeuzes en hun versies.
2. De bronmapping en je onderbouwde toolkeuze, inclusief de gegevens voor een
   eventuele verhuizing.
3. C1 met route, uitvoerders, criteriatoewijzing en herstelstand; waar nodig C2,
   C3 en het menselijke C4 op de exacte planversie.
4. De PR en C5 met basis- en codecommit, uitgevoerde controles en bewijsgrenzen.
5. De onafhankelijke C6, zo nodig C7 en herstelbijlage, je eigen
   architectuuranalyse en je menselijke merge- of vervolg-/stopbesluit. Neem na
   merge ook de mergeverwijzing en afgeronde issue- en bordstatus op.
6. De beantwoorde verantwoordingsvragen.

Controleer het dossier door één criterium vanaf de opdracht tot het bewijs,
oordeel en besluit te volgen. Die keten moet leesbaar zijn zonder jouw
maakgesprek. Het [praktijkvoorbeeld](../../praktijk/van-werkitem-naar-pull-request.md)
bevat een uitgewerkte keten als vergelijkingsmateriaal.
