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
{ref}`beginstappen <praktijk-beginnen>`
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
{ref}`bronmapping <praktijk-bronmapping>`.

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

4. **Kies de route en geef zo nodig C4.** Jij organiseert deze stap als
   orkestrator en neemt zelf het eventuele menselijke besluit. Gebruik de
   route uit {core}`loop.md`.

   **C1 vastleggen.** Neem C0 en je projectnormen als invoer. Leg volgens
   {core}`contracts/triage-decision.md` omvang, risico, normversie, uitvoerders,
   criteriatoewijzing en herstelstand vast. Ieder criterium krijgt een passende
   onafhankelijke beoordelaar. Bewaar C1 bij je issue.

   **De gekozen route uitvoeren.** Bij `REJECT` verduidelijk of splits je C0
   voordat je verdergaat. Bij `PLANNED` krijgt de planner C0, C1, basiscode en
   leesbare normen; bewaar zijn concrete {core}`contracts/build-packet.md` (C2)
   met versie. Laat alleen een verhelderaar werken als C1 die selecteert:
   geef C0, C1, C2 en normen mee en bewaar
   {core}`contracts/clarifier-result.md` (C3). Bij `LIGHT` zijn C2 en C3 niet nodig.

   **Als C3 FAIL geeft.** Begin nog niet te bouwen. Noteer vóór planherstel de
   verbruikte ontwerpronde, de planversie en criteriumgebonden bevindingen bij
   het werkitem. Hoogstens één automatische ontwerpherstelronde met herreview
   is toegestaan. Een verse verhelderaar krijgt het bijgewerkte C2, reparatiediff,
   eerdere blockers en eerder vastgestelde onaangetaste dekking in repair-modus.
   Na een resterende FAIL kiest de mens een begrensd vervolg, splitsen of stoppen.
   Een nieuwe sessie reset de stand niet. Volg {core}`loop.md` voor deze grenzen.

   **Menselijk besluiten.** Lees bij `PLANNED` C2 en de geselecteerde C3 voordat
   je {core}`contracts/gate-decision.md` (C4) vastlegt. Bewaar de exacte
   planversie met vaste commitlink en je eigen bron, besluit en reden. Bij
   `LIGHT` is C4 vooraf nodig bij een nieuw doel, contract- of normkeuze of
   onomkeerbare gevolgen; anders sla je de routinematige C4 over. `PROCEED`
   geeft het beschreven werk vrij. Bij `REVISE` of `STOP` volg je het
   vastgelegde menselijke vervolg en de begrensde scope; begin nog niet te bouwen.

   Klaar wanneer C1 leesbaar is, ieder criterium is toegewezen en de route
   uitvoering toestaat: bij `PLANNED` verwijst C4 PROCEED naar het juiste plan;
   bij `LIGHT` is voldaan aan de eventuele C4-plicht. Een nieuwe doel- of
   risicokeuze vraagt een nieuw menselijk besluit.

5. **Laat bouwen en verzamel bewijs.** Werk op een branch vanaf de basiscommit.
   Geef de bouwer C0 en C1 bij `LIGHT`, of het goedgekeurde C2 met C1 en C4 bij
   `PLANNED`, plus code en normen. Laat de afgesproken verificatie uitvoeren.
   Bij gedragwijzigingen in geteste code is test-first de standaard: de eerste
   test mag falen voordat de implementatie volgt. Groen is nodig voor de
   afgesproken opleveringscontroles, niet vóór iedere bouwstap. Bewaak de scope
   en noteer je ingrepen. Open een PR met {core}`contracts/review-handoff.md` (C5), de exacte codecommit, basiscommit,
   bewijs en links naar de besluiten en het issue.

   Klaar wanneer de criteria met passend bewijs zijn onderbouwd en de
   oplevering vermeldt welke controles zijn uitgevoerd en wat niet is
   vastgesteld.

6. **Laat onafhankelijk beoordelen en beslis over merge.** Jij verzamelt
   de overdrachten; de geselecteerde beoordelaars onderzoeken de oplevering.
   Neem daarna zelf het menselijke merge- of vervolg-/stopbesluit.

   **Onafhankelijke invoer samenstellen.** Geef iedere beoordelaar zijn rolprompt,
   de {core}`contracts/review-handoff.md`-kern (C5), toegewezen criteria,
   relevante besluiten, code en leesbare normen op de afgesproken versies.
   Het maakgesprek en andere initial oordelen gaan niet mee. Laat architectuur
   en onderhoudbaarheid expliciet onderzoeken: welke aanroepen hergebruiken de
   logica en welke regels zijn gekopieerd?

   **C6's bewaren.** Iedere geselecteerde beoordelaar levert
   {core}`contracts/reviewer-verdict.md` (C6), met bron en exacte reviewcommit.
   Bewaar alle geselecteerde oordelen voordat je een eindoordeel bepaalt.
   Een ontbrekend oordeel is geen pass.

   **Het eindoordeel bepalen.** Eén C6 is het eindoordeel. Bij meerdere
   verenigbare oordelen maak jij als orkestrator een bronherleidbare synthese
   in {core}`contracts/final-verdict.md` (C7). Inhoudelijke tegenspraak gaat naar
   de hoofdbeoordelaar met alle C6's en volledige C5. Die onderzoekt argumenten
   en bewijs en maakt een arbitration-C7. Open doel- of risicokeuzes blijven
   bij de mens; een blocker verdwijnt niet door stemmen of samenvoegen.

   **Als het eindoordeel BLOCK is.** Bewaar vóór herstel de opleveringsteller,
   productversie en criteriumgebonden blockers bij het werkitem. Hoogstens één
   automatische opleveringsherstelronde met herreview is toegestaan; de
   ontwerpteller staat daar los van en blijft bewaard. Geef de auteur de
   blockers voor gerichte reparatie aan hetzelfde artefact. De verse
   herbeoordelaar krijgt bijgewerkte C5-kern plus de expliciete herstelbijlage
   uit {core}`contracts/reviewer-verdict.md`: voor/na-commits, reparatiediff,
   eerdere blockers en eerder vastgestelde onaangetaste dekking. Label die
   laatste dekking als eerder vastgesteld, niet als nieuw onderzocht.
   Bewaar de herstel-C6 en bepaal daarna het eindoordeel volgens de gekozen
   bezetting. Bij een resterende blokkade na de ronde kiest de mens begrensd
   vervolg, splitsen of stoppen; geen automatische tweede ronde of merge.
   Volg {core}`loop.md` als scope of afhankelijkheden bewijs ongeldig maken.

   **Menselijk besluiten en afronden.** `SHIP` of `SHIP WITH NITS` maakt de
   wijziging gereed voor jouw menselijke mergebesluit. Lees oordeel en bewijs
   op de beoordeelde commit, verantwoord je keuze en bewaar het besluit apart
   van het agentoordeel. Wijs vervolgwerk voor eventuele nits aan. Na merge
   bewaar je de mergeverwijzing en controleer je issue- en bordstatus. Bij BLOCK
   bewaar je het menselijke vervolg- of stopbesluit zonder merge.

   Klaar wanneer alle oordelen, je eigen architectuuranalyse en je menselijke
   merge- of vervolg-/stopbesluit met bronnen zijn vastgelegd.

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
