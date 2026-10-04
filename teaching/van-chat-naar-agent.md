# Van chat naar agent

Deze voorbereiding legt uit welke informatie een AI-assistent gebruikt en wie
code wijzigt en controleert. Lees vóór module 1 deel A tot en met “Een rol is een
taak”. Lees vóór deel B ook de overdracht en contractwijzer. De voorbeelden zijn
geconstrueerd; de genoemde testuitkomst is geen verslag van een uitgevoerde run.

## Wat krijgt de chat mee?

Je vraagt een assistent om een uitleenfunctie te schrijven. Je geeft de eis mee:
een uitgeleend boek mag niet nogmaals worden uitgeleend. Je plakt ook de
bestaande code in het bericht. Achter de chat werkt een groot taalmodel, een
*large language model* (LLM). Het model maakt een antwoord op basis van de
informatie die het krijgt.

Die informatie noemen we hier **context**. Het chatprogramma stelt haar samen:
je opdracht, meegegeven code en eerdere berichten die het bij de aanroep opneemt.
Het model ziet niet vanzelf alle bestanden op je computer. Ook een eis uit een
ander gesprek is pas beschikbaar als het programma of jij die meegeeft.
Een eerdere aanname kan in latere antwoorden terugkomen als zij in de context
blijft staan. Een fout bewijst op zichzelf niet dat gespreksgeschiedenis de oorzaak is.

## Wie past de code toe en voert de tests uit?

Een losse chat geeft tekst terug. Jij neemt het codevoorstel over in je
bestanden en voert de tests uit. Je stuurt de waargenomen uitvoer terug, zodat
de assistent een mislukte test kan onderzoeken. “De tests slagen” in een
chatantwoord is zonder uitgevoerde controle nog geen testresultaat.

Een programma kan het model ook aanroepen via een API, een interface waarmee
programma's communiceren. Het programma kan gereedschappen aanbieden om
bestanden te lezen, code te wijzigen en tests uit te voeren. Als het model zo'n
actie kiest, voert het programma die binnen de toegestane rechten uit en geeft
het de uitkomst mee bij de volgende modelaanroep.

Een systeem dat met modelaanroepen vervolgstappen kiest en via gereedschappen
uitvoert om een taak te volbrengen, noemen we hier een **agent**. Het omvat het
programma, de modelaanroepen en de gereedschappen. Een **sessie** houdt het werk
en de context bij, bijvoorbeeld als een afzonderlijk gesprek. Hetzelfde
agentsysteem kan meerdere sessies uitvoeren.

## Een rol is een taak

Je kunt de assistent opdracht geven om code te bouwen of om haar te beoordelen.
Dat zijn verschillende **rollen**. De bouwer voert de afgesproken wijziging uit
en verzamelt bewijs. De beoordelaar vergelijkt eisen, code en bewijs. Voor een
andere rol is geen ander model nodig; de opdracht en aangeboden informatie
veranderen.

Laat de beoordeling beginnen in een eigen gesprek met de eisen, de codeversie
en de controle-uitkomsten. Het maakgesprek gaat niet mee. Deze **contextisolatie**
beperkt de voorgeschiedenis die het oordeel kan sturen. Een ontbrekende eis
kan nog steeds worden gemist. Daarom leg je vast welke informatie wordt
uitgewisseld. Zo'n afspraak over invoer en uitvoer heet hier een **contract**.
Het contract is de interface tussen de rollen. Module 2 onderzoekt hoe deze
werkverdeling aansluit op scheiding van verantwoordelijkheden en informatie
verbergen.

## Een overdracht aan de beoordelaar

Stel dat je een goedgekeurd plan voor de uitleenfunctie hebt uitgevoerd. Jij
hebt het voorstel in de bestanden toegepast en de tests uitgevoerd. Bewaar de
codeversie en feitelijke uitvoer. De bouwer maakt daarmee een overdracht volgens
{core}`contracts/review-handoff.md` (C5). Daarin horen ook de normversie en het
menselijke planbesluit. Het volgende fragment toont alleen het testbewijs en
de beperking; het vervangt niet de volledige C5.

```text
Eis: een uitgeleend boek mag niet nogmaals worden uitgeleend.
Codeversie: boekenplank, versie B1 (bewaarde snapshot voor dit voorbeeld).
Uitgevoerde controle: leen een beschikbaar boek uit.
Verwacht: status wordt uitgeleend en de lener wordt bewaard.
Waargenomen: deze test slaagt.
Beperking: een tweede uitleen van hetzelfde boek is niet getest.
```

De beoordelaar krijgt een eigen sessie met de volledige C5, de eis, het
planbesluit, de leesbare normen en codeversie B1. Gebruik de rolprompt
{core}`roles/reviewer-strict.md` en voeg een concrete taak toe, bijvoorbeeld:

```text
Beoordeel de uitleeneis tegen codeversie B1 en het meegegeven testbewijs.
Controleer welke situaties zijn onderzocht en welke nog ontbreken.
Onderbouw je bevindingen met de eis, code of testuitvoer.
Geef je oordeel in de vorm van C6.
```

De prompt beschrijft wat de beoordelaar moet doen. De ingevulde C6 bevat wat
hij heeft onderzocht en gevonden. In dit voorbeeld kan hij om een extra
controle vragen: leen hetzelfde boek opnieuw uit en controleer dat de functie
die tweede uitleen weigert. Het ontbreken van die test bewijst nog geen fout
in de functie. De uitvoering en waargenomen uitkomst moeten duidelijk maken
of de eis wordt nageleefd.

## Welke documenten gebruik je in deel B?

Jij organiseert de overdrachten als **orkestrator**. De codes benoemen
verschillende documenten. Deze wijzer helpt je de documenten te vinden;
de route en herstelregels staan in {core}`loop.md`.

| Document | Wie maakt het en met welke invoer? | Wat ontvangt de volgende stap? |
|---|---|---|
| {core}`contracts/work-item.md` (C0) | Jij beschrijft de opdracht en criteria. | Een afgebakende opdracht. |
| {core}`contracts/triage-decision.md` (C1) | Jij kiest op basis van C0 en normen de route en verantwoordelijken. | Bezetting, normbasis en toewijzing van criteria. |
| {core}`contracts/build-packet.md` (C2) | De planner krijgt C0, C1 en relevante bronnen. | Het concrete uitvoeringsplan en controles. |
| {core}`contracts/clarifier-result.md` (C3) | De geselecteerde verhelderaar krijgt C0, C1, C2 en normen. | PASS of concrete noodzakelijke planwijzigingen. |
| {core}`contracts/gate-decision.md` (C4) | Jij beoordeelt het concrete plan en de geselecteerde planreview. | Het vastgelegde PROCEED-, REVISE- of STOP-besluit. |
| {core}`contracts/review-handoff.md` (C5) | De bouwer krijgt de vrijgegeven opdracht, plan en besluiten en voert het werk uit. | Codeversie, bewijs, beperkingen en grondslag voor review. |
| {core}`contracts/reviewer-verdict.md` (C6) | Iedere geselecteerde beoordelaar krijgt C5-kern en toegewezen criteria. | Onderbouwde bevindingen en een oordeel. |
| {core}`contracts/final-verdict.md` (C7) | Bij meerdere oordelen voegt de orkestrator verenigbare C6's samen; de hoofdbeoordelaar behandelt inhoudelijke tegenspraak. | Een herleidbaar eindoordeel voor de mens. |

Je beslist bij C4 of het plan uitgevoerd mag worden. Later beslis je of de
beoordeelde wijziging mag worden overgenomen. Een positief agentoordeel voert
geen merge uit. De [manual adapter](https://github.com/misja/agent-role-loop/blob/main/adapters/manual/README.md)
beschrijft hoe je rolprompt, invoer en uitvoer met losse chats gebruikt en hoe
je herstel vastlegt. De [begrippenlijst](begrippen.md) is naslag voor de termen.

Ga verder met [module 1](modules/01-ervaren/index.md).
