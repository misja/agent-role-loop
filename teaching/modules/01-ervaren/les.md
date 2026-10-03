# Context rot

## Plaats in de leerlijn

Je kunt zelfstandig een programmeeropdracht uitvoeren en hebt ervaring met een
AI-assistent via een chatinterface. Lees eerst de [inleiding](../../index.md)
voor het onderscheid tussen een taalmodel, context, een agent en een sessie.
Voor deze oefening gebruik je losse chats; een agentomgeving met toegang tot je
bestanden is niet nodig.

Bij deze les hoort [de oefening](oefening.md). Maak deel A vooraf en deel B erna.
De leeruitkomsten staan op de [module-index](index.md).

## Wat staat er in je logboek?

In deel A geef je de assistent steeds nieuwe requirements voor de boekenplank.
Het gesprek bevat daardoor niet alleen de actuele opdracht, maar ook eerdere
voorstellen, foutmeldingen en aanpassingen. De toepassing neemt gespreksinhoud
mee bij volgende modelaanroepen. Welke berichten zij precies opneemt, hangt af
van de toepassing en de beschikbare ruimte voor context.

Vergelijk je logboek met dat van een medestudent. Kijk naar drie soorten fouten:

- **Vergeten instructies:** een afgesproken eis ontbreekt in een later voorstel.
- **Scope-verschuiving:** het voorstel verandert de opdracht of voegt ongevraagde
  functionaliteit toe.
- **Zelfverzekerde brij:** een stellig antwoord bevat onjuiste informatie,
  bijvoorbeeld over de huidige code of uitgevoerde controles.

Een mogelijk voorbeeld: bij requirement 12 verandert de assistent het
opslagformaat. Daarna worden verwijderde boeknummers opnieuw gebruikt, terwijl
requirement 13 dat verbiedt. De eindcontrole toont dan welke afspraak ontbreekt.
Dit is een illustratie, geen voorspelling van jouw oefenresultaat.

Wanneer opgebouwde context tot kwaliteitsverlies leidt, spreken we hier van
*context rot*. Een eerdere aanname kan bijvoorbeeld in latere voorstellen
blijven terugkomen. Een fout op zichzelf bewijst die verklaring niet: een
onduidelijke opdracht of een verkeerd begrepen eis kan ook een oorzaak zijn.
Noteer welke informatie in je gesprek de verklaring ondersteunt. Als je geen
van deze fouten hebt waargenomen, leg dat ook vast.

## Informatie overdragen aan een andere rol

Voor deel B verdeel je het werk over afzonderlijke opdrachten. Een planner werkt
de aanpak uit, een bouwer voert haar uit en een beoordelaar onderzoekt de
wijziging. De beoordelaar begint met een eigen gesprek. Je geeft de eisen, de
gewijzigde code en de verificatieresultaten mee. Het maakgesprek met verworpen
voorstellen gaat niet mee.

Bij de opslagwijziging moet de eis dat nummers niet worden hergebruikt wel in
de overdracht staan. Een eigen gesprek helpt die eis niet terug te vinden als
niemand haar heeft meegegeven. De contracten beschrijven daarom welke informatie
de volgende rol nodig heeft. In module 2 onderzoek je deze overdracht als
interface tussen verantwoordelijkheden.

De [manual adapter](https://github.com/misja/agent-role-loop/blob/main/adapters/manual/README.md) beschrijft hoe je de
rollenlus met losse chats uitvoert. De triage legt vooraf vast welke
verantwoordelijkheden en beoordelingen een wijziging nodig heeft. Dat is een
taak van jou als orkestrator; er hoeft geen aparte triage-agent te zijn.
De route staat in {core}`loop.md`.

In deze oefening maak je planning, verheldering, de menselijke poort en vier
beoordelaarsperspectieven zichtbaar. Dat is een oefenkeuze om de
verantwoordelijkheden te leren kennen. Vier beoordelaars zijn geen algemene
uitvoerplicht. Iedere geselecteerde beoordelaar begint onafhankelijk en ziet
pas na zijn eigen oordeel de andere beoordelingen. Jij beslist bij de
menselijke poort of het concrete plan uitgevoerd mag worden.

## Beginnen met deel B

Bewaar de uitkomsten van deel A en begin met een nieuwe codebasis. Gebruik een
werkitem voor iedere portie requirements. Het tweede en derde werkitem wijzigen
de code die de vorige portie heeft opgeleverd. Noteer in het overdrachtslogboek
welke eisen, besluiten en codeversies je aan iedere rol meegeeft.

Een andere chattoepassing kan dezelfde procedure ondersteunen. De
verantwoordelijkheden en overdrachten blijven de leerstof; de vensters zijn het
middel waarmee je ze hier uitvoert.

## Werkvormen en toetsing

Bespreek de logboeken in tweetallen en vergelijk de gevonden symptomen in de
groep. Gebruik een demonstratie van de manual adapter om de eerste overdracht
te volgen. De reflectievragen van de oefening vormen de formatieve toetsing.

## Bronnen

- De oorspronkelijke beschrijving van de lus en de term context rot zoals hier
  gebruikt {cite}`watkins2026context`.
- Onderzoek naar parallel werk bij onafhankelijke deeltaken
  {cite}`anthropic2025multiagent`.
- De normatieve procedure: {core}`principles.md` en {core}`loop.md`.

## Afronding

### Wat heb je geleerd

Je hebt onderzocht welke instructies en aannames in je gesprek behouden bleven
of uit beeld raakten. Je kunt zulke waarnemingen gebruiken om een mogelijke
verklaring te geven voor kwaliteitsverlies. In deel B leg je de informatie voor
elke volgende verantwoordelijkheid in een overdracht vast.

### Zelfcheck

Beantwoord uit je hoofd; de sleutel wijst waar je het kunt nakijken.

1. Wat noemen we hier context rot? Welke waarnemingen kunnen die verklaring
   ondersteunen? (zie Wat staat er in je logboek?)
2. Waarom is een fout in een lang gesprek op zichzelf onvoldoende om context
   rot vast te stellen? (zie Wat staat er in je logboek?)
3. Welke informatie moet de beoordelaar van een opslagwijziging ontvangen?
   Waarom volstaat een nieuw gesprek niet? (zie Informatie overdragen)

### Volgende stap

[Module 2](../02-begrijpen/index.md) onderzoekt welke informatie de rollen
uitwisselen en welke zij weglaten. Je verbindt die keuzes met scheiding van
verantwoordelijkheden en interfaces. Daarmee kom je bij de conventionele
kwaliteitslaag: afspraken over wat een overdracht moet bevatten.
