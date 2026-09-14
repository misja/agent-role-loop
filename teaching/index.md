# De ontwikkelstraat

*kwaliteit bewaken als AI bouwt*

Je werkt met een medestudent aan een applicatie die orders naar een CSV-bestand exporteert. Een gebruiker meldt dat een order soms tweemaal in het bestand staat. Je schrijft een reparatie en draagt die met de testresultaten over aan je medestudent. De tests slagen, maar bij de beoordeling blijkt dat ze steeds een vaste verzameling orders gebruiken. In de applicatie kunnen tijdens een export orders bijkomen. Je medestudent vraagt of de reparatie ook in die situatie werkt. De taakverdeling maakt ruimte om de gekozen oplossing en het bewijs opnieuw te onderzoeken.

Misschien gebruik je voor zo'n reparatie al een webchat. Je plakt code in een bericht, stelt een vraag en krijgt een voorstel terug. Achter die chat werkt een groot taalmodel, een *large language model* (LLM), dat op basis van de aangeboden informatie tekst genereert. Die informatie heet hier de context: onder meer je opdracht, meegegeven code en eerdere berichten die de toepassing bij de aanroep opneemt. Een vroege aanname, bijvoorbeeld dat de orders tijdens de export niet veranderen, kan daardoor ook in latere antwoorden doorwerken.

Een programma kan zo'n model ook aanroepen via een API, een interface voor communicatie tussen programma's. Het programma stelt de context samen en verstuurt die naar het model. Het kan bovendien gereedschappen beschikbaar stellen, zoals bestanden lezen, code wijzigen of tests uitvoeren. Als het model vraagt om een test uit te voeren, voert het programma die actie uit binnen de toegestane rechten. Het geeft de uitkomst mee bij een volgende modelaanroep. Zo kan het model op een mislukte test reageren met een aangepast voorstel, zonder dat jij elke tussenstap in de webchat overneemt.

Een systeem dat op deze manier met een model vervolgstappen kiest en via gereedschappen uitvoert om een taak te volbrengen, noemen we hier een agent. De agent omvat dus het programma, de modelaanroepen en de beschikbare gereedschappen. Een gesprek of sessie is een manier om het werk en de context ervan bij te houden. Hetzelfde agentsysteem kan verschillende sessies uitvoeren en daarin verschillende opdrachten krijgen.

Voor de exportreparatie kun je de agent de rol van bouwer geven: de opdracht om de afgesproken wijziging uit te voeren en bewijs te verzamelen. Een afzonderlijke opdracht laat een agent als beoordelaar onderzoeken of dat bewijs de eisen afdekt. Dat is scheiding van verantwoordelijkheden (*separation of concerns*), toegepast op een werkproces. Een rol benoemt de taak en de grenzen van de verantwoordelijkheid; je hebt er geen ander model voor nodig.

Je laat de beoordeling beginnen met een eigen context: de afgesproken eisen, de wijziging en het testbewijs. Het voorafgaande gesprek van de bouwer, met zijn vroege aannames en verworpen pogingen, gaat niet mee. Deze contextisolatie past informatie verbergen (*information hiding*) toe op de samenwerking. Ze beperkt welke voorgeschiedenis de beoordeling kan sturen. Ontbreekt in de overdracht een relevante eis, dan kan ook een beoordelaar met een eigen context die missen.

Daarom leg je in een contract vast wat de overdracht moet bevatten. Dat contract vormt de interface tussen de rollen: de bouwer levert bijvoorbeeld de wijziging, de bijbehorende verificatieresultaten en de bekende beperkingen. De beoordelaar kan daarmee aan het werk zonder het maakgesprek te reconstrueren. De toepassing van zulke engineeringprincipes op het proces sluit aan bij Farleys aandacht voor complexiteitsbeheersing en leren via feedback {cite}`farley2021modern`. Zijn boek gaat niet over AI-agents; hier gebruiken we die principes om het werk met agents te organiseren.

Deze werkwijze veronderstelt dat een mens het doel en de aanvaardbare risico's kan beoordelen en daarvoor verantwoordelijkheid neemt. Vóór de bouwer begint, beslist die mens bij de menselijke poort of het plan voldoende is uitgewerkt. Bij de export hoort daar bijvoorbeeld de vraag bij welke orders het bestand moet bevatten. Later kunnen tests en een agentbeoordeling helpen om de uitvoering te beoordelen. De mens beslist over het samenvoegen van de wijziging.

In deze leerlijn onderzoek je eerst hoe eerdere aannames en instructies in een langer gesprek kunnen doorwerken. Wanneer dat tot kwaliteitsverlies leidt, spreken we hier van context rot. Daarna werk je met afzonderlijke rollen en contracten als interface. Vanuit die ervaring leer je kiezen welke gereedschappen, controles en beoordelingen een wijziging nodig heeft. De rolprompts en contracten staan in het Engels onder `core/` en zijn op deze site opgenomen als [referentiesectie](referentie/index.md); de [begrippenlijst](begrippen.md) verbindt de Engelse termen met de Nederlandse uitleg.

```{toctree}
:maxdepth: 1
:caption: Raamwerken

kwaliteit-als-gedeelde-verantwoordelijkheid
```

```{toctree}
:maxdepth: 2
:caption: Leerlijn

modules/01-ervaren/index
modules/02-begrijpen/index
modules/03-machine/index
modules/04-oordelen/index
modules/05-poort/index
modules/06-ontwerpen/index
```

```{toctree}
:maxdepth: 1
:caption: Praktijk

praktijk/van-werkitem-naar-pull-request
```

```{toctree}
:maxdepth: 1
:caption: Naslag

begrippen
literatuur
```

```{toctree}
:maxdepth: 1
:caption: Referentie - rollen en contracten (Engels)

referentie/index
```

## Opzet van dit materiaal

De leerlijn bestaat uit zes modules, van *ervaren* naar *ontwerpen en verantwoorden*, elk met een les en een oefening. Daarboven ligt een raamwerken-laag, met "Kwaliteit als gedeelde verantwoordelijkheid" als eerste raamwerk: de grondslag die zich over de modules verdeelt.
