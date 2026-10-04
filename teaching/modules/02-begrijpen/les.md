# De loop als scheiding van verantwoordelijkheden

## Plaats in de leerlijn

In module 1 heb je een lange chat en de rollenloop vergeleken. Je logboek bevat
wat je daarbij hebt waargenomen. Deze les onderzoekt welke informatie bij een
overdracht meegaat en hoe de verantwoordelijkheden zijn verdeeld. Vereiste
voorkennis: module 1, inclusief het overdrachtslogboek. De [voorbereiding](../../van-chat-naar-agent.md)
legt uit hoe context aan een model wordt meegegeven en hoe een rol daarvan
gebruikmaakt.

De les hoort bij [oefening 2](oefening.md), waarin je je eigen overdrachten analyseert.

## Leeruitkomsten

De leeruitkomsten staan als “Wat ga je leren” op de [module-index](index.md).

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
toevoegvolgorde behouden moet blijven.

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

### Contracten als interface, rolprompts als implementatie

Bij een software-interface spreek je af welke invoer en uitvoer een onderdeel
heeft. De implementatie bepaalt hoe het onderdeel zijn taak uitvoert. In de
rollenloop beschrijft het contract de vorm en vereiste inhoud van een
overdracht. De rolprompt geeft instructies om die overdracht te produceren. De
uitvoering hangt daarnaast af van de mens of het model, de meegegeven context
en de gebruikte gereedschappen.

Je kunt een rolprompt wijzigen of een rol door een mens laten uitvoeren en
dezelfde contractvorm behouden. Controleer wel of de nieuwe uitvoering nog aan
de afspraken voldoet. De analogie maakt het onderscheid tussen afspraak en
uitvoering zichtbaar; zij bewijst geen uitwisselbaarheid van iedere uitvoering.

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

### Historische naslag: Mermaid-ondersteuning

Een eerder werkitem uit deze repository regelde de diagramondersteuning.
Hieronder staat een ongewijzigd fragment van dat historische artefact. Het is
naslag bij de contractvorm; de boekenplank blijft het hoofdvoorbeeld.
Bron: [werkitem #21](https://github.com/misja/agent-role-loop/issues/21),
met het oorspronkelijke artefact bij
[commit 0c4abd0](https://github.com/misja/agent-role-loop/commit/0c4abd0).

```md
## Gewenste uitkomst

Mermaid-diagrammen renderen in de site: sphinxcontrib-mermaid als dependency in
de docs-groep van pyproject.toml, extensie geconfigureerd in docs/conf.py, en
een rendercheck (een proefdiagram bouwt en toont correct, daarna weer verwijderd
of als eerste echt diagram benut).
```

Het fragment benoemt een waarneembaar resultaat en een controle. Voor uitvoering
zijn ook de overige onderdelen van het werkitem en de geldende besluiten nodig.

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
2. Wijs bij C2-P1 de contractdefinitie, het ingevulde artefact en de rolprompt aan. Wat is in deze analogie de interface? (zie “Een boekenplankoverdracht bekijken” en “Contracten als interface, rolprompts als implementatie”)
3. Welke context laat je buiten de beoordeling, en welke bronnen moeten beschikbaar blijven? Welke fout kan alsnog doorwerken? (zie “Welke informatie blijft buiten de overdracht?”)
4. Wat levert een vaste contractvorm op en welke kosten heeft zij? (zie “Een contract is een vastgelegde conventie”)

### Volgende stap

Een afspraak kan deels geautomatiseerd worden gecontroleerd. Een test kan
bijvoorbeeld vaststellen of het filter de geregistreerde boeken behoudt voor de
gekozen invoer. Module 3 onderzoekt wat zulke controles aantonen en wat zij
onbeslist laten. Daarmee ga je van de conventionele naar de geautomatiseerde laag.
