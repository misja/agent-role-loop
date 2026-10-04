# De loop als scheiding van verantwoordelijkheden

## Plaats in de leerlijn

In module 1 heb je een lange chat en de rollenloop vergeleken. Je logboek bevat
wat je daarbij hebt waargenomen. Deze les onderzoekt welke informatie bij een
overdracht meegaat en hoe de verantwoordelijkheden zijn verdeeld. Vereiste
voorkennis: module 1, inclusief het overdrachtslogboek. De [voorbereiding](../../van-chat-naar-agent.md)
legt uit hoe context aan een model wordt meegegeven en hoe een rol daarvan
gebruikmaakt.

De [begeleide uitvoering](../01-ervaren/eerste-uitvoering.md) toont de eerdere
chatinvoer en overdrachten. Deze les verdiept die uitvoering; in
[oefening 2](oefening.md) analyseer je daarna je eigen overdrachten.

## Opbouw

### Een boekenplankoverdracht bekijken

Een medewerker wil alleen beschikbare boeken zien. De geregistreerde boeken
moeten daarbij behouden blijven: een filter mag een uitgeleend boek niet uit de
boekenplank verwijderen. De planner beschrijft in plan C2-P1 dat
`lijst(alleen_beschikbaar=False)` het bestaande overzicht blijft geven. Met
`True` krijgt de aanroeper een gefilterde lijst terug. Het plan noemt ook de
controle: vraag na het filteren opnieuw alle boeken op en vergelijk die met de
registratie van vóór het filteren.

Dit is een bewerkt onderwijsvoorbeeld uit
[Van werkitem naar pull request](../../praktijk/van-werkitem-naar-pull-request.md).
De [ingevulde overdrachten](../../praktijk/overdrachten.md) bevatten het plan en
het menselijke besluit C4-P1. Dat besluit bevestigt onder meer dat de
toevoegvolgorde behouden moet blijven. Personen, plannen en besluiten zijn
geconstrueerd; de code en controles zijn uitvoerbaar. Dit filtervoorbeeld werkt
in het geheugen, zonder de CLI en opslag uit jouw module-1-opdracht.

Voor de bouwer zijn verschillende bronnen nodig. De definitie van
{core}`contracts/build-packet.md` beschrijft welke onderdelen een plan moet
bevatten. Het ingevulde C2-P1 bevat de gegevens voor deze wijziging. C4-P1 legt
vast welke planversie de mens heeft goedgekeurd. De bouwer krijgt daarnaast de
code, geldende normen en de {core}`roles/builder.md`-rolprompt. Die prompt
beschrijft de verantwoordelijkheid en werkwijze van de bouwer. Een contract is
dus geen vervanging voor de opdracht of het besluit.

### Scheiding van verantwoordelijkheden op een werkproces

Je kent scheiding van verantwoordelijkheden uit software: onderdelen krijgen
een afgebakende taak, zodat een wijziging gericht kan worden onderzocht. In het
boekenplankvoorbeeld bepaalt de planner hoe het filter wordt toegevoegd; de
bouwer voert het goedgekeurde plan uit. Een onafhankelijke beoordelaar
controleert vervolgens of de registratie behouden blijft en of het bewijs die
uitspraak ondersteunt.

De rollenloop past het principe daarmee toe op een werkproces. De triage kiest
de benodigde verantwoordelijkheden en wijst de criteria aan onafhankelijke
beoordelaars toe. De menselijke poort beslist over uitvoering van het plan.
De vier beoordelingsperspectieven uit oefening 1 zijn een oefenkeuze. Bij één
passende beoordelaar kan diens C6 volstaan; een hoofdbeoordelaar onderzoekt
inhoudelijke tegenspraak tussen meerdere beoordelingen. Het actuele schema
staat in {core}`loop.md`.

De verdeling maakt zichtbaar wie waarvoor verantwoordelijk is. Zij garandeert
geen juiste uitkomst: een ontbrekende eis in het werkitem kan ook in het plan en
de beoordeling ontbreken.

### Contract, instructie en uitvoering

Bij een software-interface spreek je af welke invoer en uitvoer een onderdeel
heeft. Een contract doet dat voor een overdracht. De rolprompt instrueert de
uitvoerder; pas de handelingen laten zien hoe die instructie is uitgevoerd.

De bouwer ontvangt C1, C2-P1, C4-P1, W1, de basiscode en de leesbare normen.
Naast {core}`roles/builder.md` kan de opdracht in dit voorbeeld luiden:

```text
Voer C2-P1 uit binnen C4-P1. Behoud de registratie bij het filteren (S4).
Voer de geplande controles uit en bewaar de codeversie en werkelijke uitvoer
voor C5. Deze chat kan geen bestanden wijzigen: geef het voorstel en de
commando's; gebruik alleen mijn teruggestuurde resultaten als testbewijs.
```

Dit is een voorbeeldinstructie, geen verslag van een uitgevoerd gesprek. Bij
losse chats neemt de student het voorstel over en voert de controles uit.
Bij een agent met gereedschappen kan het programma die handelingen uitvoeren.
Het ontvangen van de prompt is in beide gevallen nog geen bewijs van uitvoering.

(module2-controle)=
### Opdracht: voer één controle uit

De praktijkbundel bevat voorbereide codeversies A en B. Voer vanuit de hoofdmap
van deze repository onderstaande controle op B uit. Gebruik Python 3.10 of
nieuwer; de standaardbibliotheek volstaat. `python3` heet op Windows vaak `python`.

```sh
python3 teaching/cases/praktijk-projectomgeving/controleer.py b volledig
```

Verwacht vier geslaagde controles en `OK`. Bewaar het commando, de uitvoer en de
repositorycommit (`git rev-parse HEAD`) in je logboek. Zoek vervolgens
`test_s4_filter_verandert_geen_toestand` in `controleer.py`: de controle bewaart
boeken en uitleenstatus vóór het filteren en vergelijkt ze met de toestand erna.
Je hebt nu zelf een controle uitgevoerd op voorbereide code. Dat toont geen
uitgevoerde bouwersessie aan en bewijst alleen de onderzochte gevallen.

### Uitleg: de overeenkomst en de grens

Je kunt andere instructies gebruiken of een mens dezelfde taak laten uitvoeren
terwijl de contractvorm gelijk blijft. Daarmee lijkt de overdracht op een
software-interface. Een rolprompt is echter geen software-implementatie: het
model, de context, de gereedschappen en de feitelijke handelingen bepalen mede
de uitvoering. De contractvorm garandeert geen juiste inhoud of vaste uitkomst.
Controleer daarom het geproduceerde artefact en het bewijs.

(module2-analyse)=
### Eén overdracht ontleed

Bekijk C5-A, de overdracht van bouwer naar beoordelaar in de
[ingevulde overdrachten](../../praktijk/overdrachten.md). De volgende analyse
gebruikt de [C5-contractversie uit de bundel](https://github.com/misja/agent-role-loop/blob/ae561f50a45ca42967e4687434cf0d2e8d4f5827/core/contracts/review-handoff.md).
De actuele definitie staat bij {core}`contracts/review-handoff.md`. De procesversie van
de bundel staat in haar leeswijzer; gebruik voor een historische analyse de
bijbehorende contractversie, niet stilzwijgend een nieuwere.

| Analyseveld | Wat je bij C5-A kunt aanwijzen |
|---|---|
| Bron en versie | `teaching/cases/praktijk-projectomgeving/overdrachten.md`, scenario versie 1, C5-A; A is het leeslabel voor `boekenplank_a.py`, geen SHA. Noteer daarnaast de commit van jouw repositorykopie. |
| Ontvanger en handeling | De onafhankelijke beoordelaar onderzoekt S1 tot en met S4 tegen code, eisen en controlebewijs. |
| Vereiste informatie | C5 vraagt onder meer artefact/versie, normbasis, besluit, criteriadekking en werkelijk verificatiebewijs. |
| Aangetroffen informatie | C5-A noemt W1/P1, C4-P1, bestand A, diff en drie geslaagde controles voor S1 tot en met S3. |
| Ontbrekende informatie | Bewijs voor S4 ontbreekt in deze oplevering; een echte codecommit en agentrun zijn niet beschikbaar in het geconstrueerde scenario. |
| Gevolg | De drie geslaagde controles ondersteunen geen uitspraak over behoud van de registratie. Daarvoor is de afzonderlijke S4-controle nodig. |

De eerder uitgevoerde controle op B levert nieuw bewijs voor B, niet achteraf
voor A. Dat onderscheid voorkomt dat een ontvanger ontbrekende resultaten
uit een andere versie invult. Bij je eigen analyse gebruik je je werkelijke
artefacten; noteer ontbrekende gegevens als ontbrekend.

### Welke informatie blijft buiten de overdracht?

De beoordelaar krijgt de eisen, het besluit, de gewijzigde code en de
verificatieresultaten. Het maakgesprek met eerdere pogingen gaat niet mee. Zo
krijgt een eerdere aanname minder gelegenheid om het oordeel te sturen.
Wanneer die aanname ook in het plan staat, kan zij nog steeds doorwerken.

Het weglaten van het maakgesprek betekent niet dat bronnen ontoegankelijk
worden. De geldende normen, relevante risico's en besluiten blijven leesbaar;
de beoordelaar kan oorspronkelijke bronnen gericht raadplegen. De
orkestrator stelt de invoer samen en bewaakt de juiste versies. Een pad naar
een lokaal bestand volstaat alleen als de ontvangende rol dat bestand kan lezen.

### Een contract is een vastgelegde conventie

Het [kwaliteitsraamwerk](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md)
noemt afspraken die mensen vastleggen de conventionele kwaliteitslaag. Een
contract hoort bij die laag. De vaste onderdelen helpen de bouwer bijvoorbeeld
het gekozen verificatiemodel en de geldende beslissing terug te vinden zonder
iedere keer een nieuwe overdrachtsvorm af te spreken.

Dat heeft ook kosten: iemand moet de velden invullen, actualiseren en lezen.
Een ingevuld contract kan bovendien onduidelijkheden bevatten. De afgesproken
vorm vervangt het onderzoek naar de inhoud niet.

```{admonition} Optionele naslag: Mermaid-ondersteuning
:class: dropdown

Lees dit fragment als je de contractvorm bij een andere soort wijziging wilt
herkennen: een controle op documentatie in plaats van boekenplankgedrag.

Een eerder werkitem uit deze repository regelde de diagramondersteuning.
Hieronder staat een ongewijzigd fragment van dat historische artefact. Het is
naslag bij de contractvorm; de boekenplank blijft het hoofdvoorbeeld.
Bron: [werkitem #21](https://github.com/misja/agent-role-loop/issues/21),
met het oorspronkelijke artefact bij
[commit 0c4abd0](https://github.com/misja/agent-role-loop/commit/0c4abd0).

~~~md
## Gewenste uitkomst

Mermaid-diagrammen renderen in de site: sphinxcontrib-mermaid als dependency in
de docs-groep van pyproject.toml, extensie geconfigureerd in docs/conf.py, en
een rendercheck (een proefdiagram bouwt en toont correct, daarna weer verwijderd
of als eerste echt diagram benut).
~~~

Het fragment benoemt een waarneembaar resultaat en een controle. Voor uitvoering
zijn ook de overige onderdelen van het werkitem en de geldende besluiten nodig.

```

## Werkvormen en toetsing

- Werkvormen: korte instructie, gezamenlijke analyse van één voorbeeldoverdracht, daarna zelf toepassen in oefening 2.
- Toetsing: formatief, via de verantwoordingsvragen van oefening 2.

## Bronnen

- {core}`principles.md` en {core}`loop.md` zijn de normatieve teksten onder deze les.
- Het raamwerk [Kwaliteit als gedeelde verantwoordelijkheid](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md), sectie “2. Conventioneel en vastgelegd”.
- Parnas, On the Criteria To Be Used in Decomposing Systems into Modules {cite}`parnas1972criteria`, over interfaces en het verbergen van implementatiebeslissingen. De les gebruikt dit als analogie voor overdrachten.
- Brooks, The Mythical Man-Month {cite}`brooks1975mythical`, over communicatiekosten bij softwareontwikkeling.

## Afronding

### Wat heb je geleerd

De rollenloop verdeelt verantwoordelijkheden over een werkproces. Contracten
beschrijven de afgesproken overdrachten; de rolprompts instrueren de uitvoering.
Eisen, normen en besluiten gaan mee, terwijl het maakgesprek buiten de
beoordelingscontext blijft. Die selectie kan beïnvloeding door eerdere aannames
beperken. De inhoud en volledigheid van de overdracht blijven controle vragen.

### Zelfcheck

Beantwoord uit je hoofd; de sleutel wijst waar je het kunt nakijken.

1. Welke verantwoordelijkheid draagt de bouwer, en welke de menselijke poort? (zie “Scheiding van verantwoordelijkheden op een werkproces”)
2. Wijs bij C2-P1 de contractdefinitie, het ingevulde artefact en de rolprompt aan. Wat is in deze analogie de interface? (zie “Een boekenplankoverdracht bekijken” en “Contract, instructie en uitvoering” en “Uitleg: de overeenkomst en de grens”)
3. Welke context laat je buiten de beoordeling, en welke bronnen moeten beschikbaar blijven? Welke fout kan alsnog doorwerken? (zie “Welke informatie blijft buiten de overdracht?”)
4. Wat levert een vaste contractvorm op en welke kosten heeft zij? (zie “Een contract is een vastgelegde conventie”)

### Volgende stap

Een afspraak kan deels geautomatiseerd worden gecontroleerd. Een test kan
bijvoorbeeld vaststellen of het filter de geregistreerde boeken behoudt voor de
gekozen invoer. Module 3 onderzoekt wat zulke controles aantonen en wat zij
onbeslist laten. Daarmee ga je van de conventionele naar de geautomatiseerde laag.
