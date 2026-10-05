# Een interface ontwerpen en de uitvoering beoordelen

## Plaats in de leerlijn

In deze laatste module ontwerp je een uitbreiding op de boekenplank. Je gebruikt
hiervoor de werkwijze uit modules 1 tot en met 5: een opdracht afbakenen, rollen afzonderlijk
inzetten, controles uitvoeren en de uitkomst beoordelen. De
[oefening](oefening.md) laat je deze onderdelen toepassen in een eigen
mini-project. Je kiest zelf welke interfacehandelingen je bouwt.

Voor de overdrachten gebruik je de uitleg over
[rollen en contracten](../02-begrijpen/les.md), de
[grenzen van testbewijs](../03-machine/les.md) en het
[menselijke besluit](../05-poort/les.md). Het
[praktijkvoorbeeld](../../praktijk/van-werkitem-naar-pull-request.md) toont hoe
je die overdrachten bij een issue en PR bewaart.

## Opbouw

### De opdracht ontwerpen en de bouw begeleiden

Stel dat je een interface wilt waarmee een medewerker een boek kan uitlenen.
Je moet dan vaststellen hoe de medewerker het boek en de lener kiest, en wat
zichtbaar wordt als uitlenen niet is toegestaan. Die keuzes komen in je werkitem
als gewenste uitkomsten. De planner kan vervolgens beschrijven hoe de interface
de bestaande uitleenmethode aanroept. Bij de beoordeling controleer je of de
handeling aan je criteria voldoet en of de bestaande regels behouden blijven.

Je begeleidt de bouw door de juiste invoer aan iedere rol te geven. De bouwer
krijgt de geldende opdracht, normen en relevante besluiten. De onafhankelijke
beoordelaar krijgt de oplevering en het bewijs, zonder het maakgesprek. Zo kan
die zelf nagaan of de uitkomst overeenkomt met de afspraken. De rolselectie en
route leg je vooraf vast volgens {core}`loop.md`.

### Projectafspraken kiezen en controleren

Het [kwaliteitsraamwerk](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md)
onderscheidt vastgelegde afspraken, automatische controles en contextueel
oordeel. Je kunt bijvoorbeeld besluiten dat alle Pythonbestanden dezelfde
opmaak moeten volgen. Je legt die keuze vast in een formatterconfiguratie en
laat de controle op de gewijzigde bestanden draaien. Dan is zichtbaar of de
opmaak aan de afgesproken regels voldoet.

De controle beantwoordt niet of de interface de uitleenlogica op de juiste
plaats gebruikt. Daarvoor moet een beoordelaar de aanroepen en de verdeling van
verantwoordelijkheden lezen. Sommige oordelen kun je later in een afspraak en
controle omzetten; andere blijven afhankelijk van het ontwerp en de
gebruikscontext.

Kies vóór de bouw welke afspraken nodig zijn. Geef voor stijl, type checking,
linting en formattering aan wat je inzet en waarom. Ook het weglaten van een
controle vraagt een reden: welke vraag blijft dan bij de beoordeling liggen?
Vage afspraken kunnen de bouwer ruimte geven voor verschillende keuzes. Een
vastgelegde afspraak biedt een beoordelingsbasis, maar bewijst nog geen naleving.

Stel dat je voor een demonstratie een kleine interface op in-memory-logica
maakt, zonder nieuwe externe afhankelijkheden of echte gebruikersgegevens.
Er is geen bestaande projectnorm die een dependencyscan verplicht stelt.
Je kunt dan een scan voor nieuw toegevoegde dependencies weglaten: er zijn
voor deze wijziging geen nieuwe pakketten om daarmee te onderzoeken. Leg die
scope en reden vast. Een beoordelaar moet nog steeds nagaan of de interface
invoer goed afhandelt, de juiste logica aanroept en passende foutmeldingen toont.
De weglating bewijst geen kwetsbaarheidsvrijheid en laat een al verplichte
projectcontrole niet vervallen. Gebruik deze afweging alleen als de beschreven
voorwaarden voor jouw uitbreiding gelden.

De [conventiepagina](../../conventies.md) van dit materiaal is een voorbeeld:
zij wijst de geldende normen en hun vindplaatsen aan. In je eigen project leg je
ook de gebruikte versies vast, zodat een latere beoordeling dezelfde basis
gebruikt.

### Werkwijze, medium en tool

Een C2 bevat een bouwplan, ongeacht of je het in een bestand of een issuereactie
bewaart. De **werkwijze** bepaalt welke rollen, informatie en besluiten nodig
zijn. Het **medium** is de opslagvorm, zoals een Markdown-bestand of een
issuebeschrijving. De **tool** beheert die informatie, bijvoorbeeld Git of een
projectomgeving met issues en een bord.

In deze oefening staat de opdracht in je issue. Het plan en menselijke besluit
staan in herkenbare reacties met verwijzingen naar de geldende versies. De
codecommit legt de wijziging vast; de PR bevat de oplevering en beoordeling. Het
bord toont de voortgang. Een bordstatus vervangt geen besluit over een plan.
De volledige {ref}`bronmapping <praktijk-bronmapping>`
uit het praktijkvoorbeeld helpt je deze bronnen aan elkaar te koppelen.

Weeg bij je toolkeuze mee wie de gegevens kan lezen, waar ze worden bewaard en
wat een verhuizing vraagt. Kun je behalve code ook besluiten, bijlagen en reviews
meenemen? Welke koppelingen en accountrechten moet je opnieuw inrichten? De
{ref}`exporttabel <praktijk-exporttabel>`
maakt dat concreet. Markdown-snapshots bewaren de inhoud van overdrachten; voor
historie, verbanden en voortgang zijn aanvullende gegevens nodig. Onderzoek die
kosten voor jouw project voordat je een toolwissel als uitvoerbaar beschrijft.

### Architectuur en onderhoudbaarheid beoordelen

De uitbreiding is een interface op je bestaande boekenplanklogica, bijvoorbeeld
een [Textual](https://textual.textualize.io/)-TUI. De interface leest invoer en
toont de uitkomst. De bestaande logica bepaalt bijvoorbeeld of een boek kan
worden uitgeleend.

Vergelijk twee mogelijke uitvoeringen. In de eerste roept de interface
`uitlenen` aan en toont de teruggegeven uitkomst. In de tweede kopieert zij de
controle op beschikbaarheid en past zij zelf de uitleenstatus aan. Bij die
tweede uitvoering moet een wijziging in de uitleenregel op twee plaatsen worden
verwerkt. Als één plaats wordt overgeslagen, kunnen de interfaces verschillend
gedrag vertonen.

Wijs bij je beoordeling daarom de relevante aanroepen en eventuele gekopieerde
regels aan. Leg uit welk gevolg de verdeling heeft voor een volgende wijziging.
Dat is de scheiding van verantwoordelijkheden uit je engineeringkennis,
toegepast op deze uitbreiding. Architectuur en onderhoudbaarheid krijgen hier
extra aandacht; aantoonbare fouten tegen de acceptatiecriteria blijven eveneens
bevindingen die moeten worden afgehandeld.

Je verantwoording steunt op het werkitem, de code en het uitgevoerde bewijs.
Verschillende stacks kunnen passende oplossingen opleveren. Een overtuigende
uitleg moet nog steeds overeenkomen met wat in het artefact is aan te wijzen.

## Werkvormen en toetsing

- Werkvormen: korte instructie, daarna het mini-project met tussentijdse
  bespreking van de dossiers.
- Toetsing: formatief, via het dossier en de verantwoordingsvragen van de
  [oefening](oefening.md).

## Bronnen

- [Kwaliteit als gedeelde verantwoordelijkheid](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md),
  de drie soorten mechanismen en "De drie samen".
- {core}`loop.md`, {core}`principles.md` en {core}`contracts/work-item.md` voor
  routing, verantwoordelijkheden en de vorm van het werkitem.
- De [projectconventies](../../conventies.md) en het
  [praktijkvoorbeeld](../../praktijk/van-werkitem-naar-pull-request.md) voor
  vastgelegde normen en vindbare overdrachten.

## Afronding

### Wat heb je geleerd

Een eigen interface-uitbreiding vraagt keuzes over functionaliteit, de
verdeling van code en de werkwijze. Je legt de gewenste uitkomst en normen vóór
de bouw vast. Automatische controles leveren bewijs voor de vragen die zij
toetsen; de onafhankelijke beoordeling onderzoekt ook architectuur en
onderhoudbaarheid. Als menselijke besluitnemer onderbouw je het planbesluit waar
dat nodig is en het uiteindelijke mergebesluit.

### Zelfcheck

Beantwoord de vragen uit je hoofd. De verwijzingen helpen je het antwoord te
controleren.

1. Kies één norm voor jouw project. Wat leg je vast, wat kun je automatisch
   controleren en welke beoordeling blijft nodig? Zie "Projectafspraken kiezen
   en controleren".
2. Waar vind je in jouw project de opdracht, geldende planversie en beoordeelde
   code? Welke informatie zou je bij een toolwissel meenemen? Zie "Werkwijze,
   medium en tool" en de exporttabel.
3. Hoe stel je vast of de interface de logica hergebruikt? Welk gevolg kan
   duplicatie hebben? Zie "Architectuur en onderhoudbaarheid beoordelen".
4. Wanneer neem je een C4-besluit en wanneer een mergebesluit? Zie
   [module 5](../05-poort/les.md) en de stappen van de [oefening](oefening.md).

### Afsluitende vooruitblik

Gebruik bij een volgend project dezelfde vragen om de werkwijze in te richten:
welke uitkomst is afgesproken, welke normen gelden en wie controleert welke
criteria? Bewaar bij ieder oordeel de bronnen en versies waarop het berust.
Daarmee kun je later terugvinden waarom een wijziging is toegelaten en welke
vragen bij een volgende uitbreiding opnieuw moeten worden beoordeeld.
