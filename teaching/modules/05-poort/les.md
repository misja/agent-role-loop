# Beslissen over risico en herstel

## Plaats in de leerlijn

In [module 4](../04-oordelen/index.md) heb je bevindingen gewogen en een
eindoordeel onderbouwd. Een oordeel over kwaliteit levert informatie voor een
besluit over de gevolgen. Deze module behandelt dat menselijke besluit: mag een
voorstel worden uitgevoerd, en onder welke voorwaarden?

Je gebruikt de rollen en contracten uit [module 2](../02-begrijpen/index.md) en het
[kwaliteitsraamwerk](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md).
In de [oefening](oefening.md) neem je zelf de menselijke poort op je voor een
voorstel om de bestaande verwijderlogica toe te passen.

## Leeruitkomsten

De leeruitkomsten staan onder “Wat ga je leren” op de [module-index](index.md).

## Opbouw

### Een planbesluit en een mergebesluit

Een test kan laten zien dat een verwijderd boek niet meer via `boek(nummer)`
wordt gevonden. Een beoordelaar kan nagaan of dat gedrag overeenkomt met de
eisen. Om te besluiten of verwijderen met openstaande reserveringen is
toegestaan, zijn ook het gebruiksdoel en de gevolgen voor de betrokkenen nodig.
In deze werkwijze draagt de mens de verantwoordelijkheid voor die keuze.

De menselijke poort ({core}`roles/human-gate.md`) beslist bij C4 over een
concreet plan, vóór de bouwer ermee aan het werk gaat. De mens leest het doel,
de scope, het verwachte gevolg en de voorgestelde controles. Die kan bijvoorbeeld
besluiten dat eerst een herstelvoorziening nodig is. Het besluit en de
voorstelversie worden vastgelegd in {core}`contracts/gate-decision.md`.

Na de bouw levert de bouwer bewijs en beoordelen de geselecteerde onafhankelijke
beoordelaars de oplevering. Daarna neemt de mens het mergebesluit. Een C4 met
PROCEED geeft toestemming voor het afgesproken werk; het is geen voorafgaande
goedkeuring van de nog te beoordelen oplevering.

### Een gepubliceerd historisch poortbesluit

Bij de ontwikkeling van module 4 waren vier didactische beslispunten aan de
mens voorgelegd:

1. Reserveringen en een wachtlijst gebruiken als casus voor verschillende oordelen.
2. De code aanleveren, zodat studenten hetzelfde artefact beoordelen.
3. De ondersteuning afbouwen en een geprioriteerd eindoordeel vragen.
4. Het risicobesluit bewaren voor module 5.

Het volgende fragment staat letterlijk in de
[historische lespublicatie op commit 80d2ea5](https://github.com/misja/agent-role-loop/blob/80d2ea5/teaching/modules/05-poort/les.md).
Een [reactie op issue #13](https://github.com/misja/agent-role-loop/issues/13#issuecomment-4853496381)
bevestigt PROCEED met de aanscherping. Het volledige oorspronkelijke menselijke
gesprek is niet afzonderlijk teruggevonden; de publicatie is de bron voor dit
citaat.

```md
PROCEED, met een aanscherping op 2 en een aandachtspunt bij 3.

1 (reserveringen/wachtlijst): akkoord, de vier-weg-tabel draagt het.

2 (aangeleverd AI-gebouwd artefact): akkoord, maar het beslissende argument is
didactische controle, niet "proportioneel want CLI". Bij eigen code hangt de
leerervaring af van de toevallige kwaliteit van het studentwerk; een aangeleverd
artefact garandeert dat elke student dezelfde rijke, oordeelswaardige situatie
heeft. Accepteer wel bewust de prijs: het is een te onderhouden artefact. Bouw
het met dezelfde discipline als module 3, zo klein en inert mogelijk.

Aanscherping op 2: de ingebouwde spanningen moeten verdedigbare keuzes zijn die
botsen, geen verstopte bugs. Als het "vind de vier fouten" wordt, is het een
verstopte lat. De oordeelslaag gaat er juist over dat redelijke mensen het
oneens zijn over code die niet simpelweg fout is. De wachtlijst die pragmatisch
prima is maar onderhoudbaarheid-verstrengeling geeft, is geen fout maar een
legitieme keuze. Dat moet de aard van de spanningen zijn.

3 (fading en verdictvorm): akkoord. Bewaak dat de eindsynthese het prioriteren
expliciet vraagt (correctheid eerst, dan onderhoudbaarheid, dan afwerking), niet
blijft hangen bij vier losse oordelen. Het prioriteren is de oordeelsvaardigheid.

4 (grens met module 5): akkoord.
```

Bij punt 2 wordt een keuze toegestaan onder een voorwaarde: de aangeleverde
spanningen moeten verdedigbaar zijn. Bij punt 3 staat waarop de bouwer in de
uitwerking moet letten. Zo blijven het besluit en de voorwaarden samen
beschikbaar voor de volgende rol.

Dit fragment beschrijft de toenmalige ontwerpkeuzes. De uitspraak over een
gegarandeerde leerervaring is geen gemeten onderwijseffect. Ook de eis dat
perspectieven moeten botsen geldt niet als huidige norm: beoordelingen kunnen
verenigbaar zijn en een aangetoonde fout blijft een fout. Voor de actuele
routing geldt {core}`loop.md`.

### Wat verwijderen doet en welk risico je beoordeelt

De voorbeeldcode bewaart boeken in een lijst in het geheugen. `verwijderen`
haalt een boek uit die lijst, ook als het uitgeleend is of een wachtlijst heeft.
Daarna is het boek via de boekenplank niet meer opvraagbaar. De publieke API
biedt geen methode om de verwijdering ongedaan te maken.

Dat is geen bewijs dat alle gegevens uit het geheugen vernietigd zijn. Een
andere verwijzing naar hetzelfde Boek-object kan de lener en wachtlijst nog
bevatten. De casus levert ook geen gedeelde of permanente opslag. In de oefening
beoordeel je daarom een geconstrueerd gebruiksscenario: dezelfde operatie
beschikbaar maken waar reserveringen waarde hebben en nog geen herstelvoorziening
is afgesproken.

Voor dat scenario moet vóór toepassing duidelijk zijn wie verlies van
reserveringen mag accepteren en welk herstel beschikbaar is. Een bevestiging
kan een vergissing verminderen doordat iemand de gevolgen eerst te zien krijgt.
Zij maakt een uitgevoerde verwijdering niet herstelbaar. Een archief of
soft-delete kan herstel ondersteunen als de benodigde gegevens bewaard blijven
en terugzetten is geregeld. Dit zijn voorbeelden van voorwaarden; deze module
vraagt je geen hersteloplossing te bouwen.

### Proportionaliteit en triage

Triage weegt vooraf welke inzet past bij de taak. Een kleine tekstcorrectie met
heldere criteria kan LIGHT krijgen. Voor een samenhangende wijziging met open
ontwerpkeuzes past PLANNED; een onduidelijke of te grote taak gaat met REJECT
terug voor verheldering of splitsing. De omvang wordt aangeduid met XS, S, M, L
of XL. XL moet eerst worden opgesplitst.

Bij PLANNED besluit de mens bij C4 over het concrete C2, met C3 als een
verhelderaar is geselecteerd. LIGHT slaat de planstappen en de gebruikelijke C4
over. Bij nieuwe doel-, contract- of normkeuzes of onomkeerbare gevolgen vraagt
ook LIGHT eerst C4. Beide routes houden onafhankelijke opleveringsbeoordeling en
een menselijke mergebeslissing. Zie {core}`loop.md` voor deze grenzen.

De weging omvat omvang, risico, beschikbare herstelmogelijkheden en de kosten
van uitvoering en beoordeling. Een korte codewijziging kan grote gevolgen
hebben. Het aantal gewijzigde regels alleen bepaalt daarom de route niet.

### De beslissing in deze module

Je oefent een besluit over doel en risico op een afgebakend voorstel. De
codelezing levert daarvoor feiten. Je geeft voorwaarden aan de verantwoordelijke
bouwer of planner als het voorstel nog niet uitgevoerd mag worden. Het eigen
ontwerp en de architectuurverantwoording volgen in module 6.

## Werkvormen en toetsing

- Werkvormen: een kort uitgewerkt poortvoorbeeld, gevolgd door een eigen besluit op het verwijdervoorstel.
- Toetsing: formatief, via het C4-besluit en de verantwoordingsvragen in de oefening.

## Bronnen

- [Kwaliteit als gedeelde verantwoordelijkheid](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md), over de menselijke poort.
- {core}`roles/human-gate.md`, {core}`contracts/gate-decision.md` en {core}`loop.md`.
- De historische lespublicatie en bevestigende issue-reactie bij het geciteerde poortbesluit hierboven.

## Afronding

### Wat heb je geleerd

Een poort-besluit koppelt een concrete voorstelversie aan een menselijke keuze
over doel, scope en aanvaardbare risico’s. Je hebt het ontbreken van herstel in
de voorbeeld-API onderscheiden van vernietiging van gegevens. Die feiten helpen
je voorwaarden te stellen voor een voorgenomen toepassing. De gekozen route
bepaalt welke planstappen nodig zijn; de mergebeslissing volgt na de oplevering
en beoordeling.

### Zelfcheck

Beantwoord uit je hoofd; de sleutel wijst waar je het kunt nakijken.

1. Wat kan de verwijdertest aantonen, en welke informatie heeft de mens daarnaast nodig voor C4? (zie “Een planbesluit en een mergebesluit”)
2. Waarom bewijst het ontbreken van een herstelmethode niet dat alle boekgegevens zijn vernietigd? (zie “Wat verwijderen doet en welk risico je beoordeelt”)
3. Welke C4-grenzen gelden voor LIGHT, en wanneer vindt de menselijke mergebeslissing plaats? (zie “Proportionaliteit en triage”)

### Volgende stap

In [module 6](../06-ontwerpen/index.md) ontwerp je zelf een uitbreiding. Je
bepaalt de functionaliteit en randvoorwaarden, laat afgesproken werk uitvoeren
en verantwoordt de architectuur. Het poort-besluit uit deze module helpt je daar
open doel- en risicokeuzes vast te leggen voordat de bouw begint.
