# Onderzoek context rot

Je gaat twee keer dezelfde middelgrote opdracht doen met een AI-assistent. De eerste keer in één lange chat, zonder structuur. De tweede keer met de rollenloop, waarbij jij de orkestrator bent. Vergelijk daarna de resultaten en de informatie die je bij iedere stap gebruikte.

**Duur:** deel A circa 90 minuten (vóór les 1), deel B circa 90 minuten (na les 1), reflectie 30 minuten.
**Nodig:** een chatgebaseerde AI-assistent naar keuze, een logboek met de velden hieronder, de [voorbereiding](../../van-chat-naar-agent.md) over model, context en agent, en voor deel B de bestanden uit `core/` en de [manual adapter](https://github.com/misja/agent-role-loop/blob/main/adapters/manual/README.md).
**Inleveren:** je logboek uit deel A, je overdrachtslogboek uit deel B, en de beantwoorde reflectievragen.

## De opdracht (voor beide delen dezelfde)

Bouw een command-line-tool `boekenplank` voor een kleine bibliotheek, in een taal naar keuze. De requirements krijg je in drie porties; geef ze in deze volgorde aan je assistent en niet allemaal tegelijk. Zo onderzoek je wat er gebeurt als nieuwe eisen eerdere afspraken aanvullen of veranderen.

**Portie 1 (begin van het gesprek):**

1. `boekenplank toevoegen <titel> <auteur>` registreert een boek; elk boek krijgt een oplopend nummer.
2. `boekenplank lijst` toont alle boeken met nummer, titel, auteur en status (aanwezig of uitgeleend).
3. `boekenplank uitlenen <nummer> <naam>` zet een boek op uitgeleend aan die persoon.
4. `boekenplank terug <nummer>` meldt een boek terug.
5. Gegevens blijven bewaard tussen aanroepen (bestand, formaat vrij).

**Portie 2 (nadat portie 1 werkt):**

6. Een boek dat al uitgeleend is, kan niet nogmaals uitgeleend worden; geef een nette foutmelding.
7. `boekenplank zoek <term>` zoekt in titel én auteur, hoofdletterongevoelig.
8. `boekenplank lijst --uitgeleend` toont alleen uitgeleende boeken, met de naam van de lener.
9. Wijziging op requirement 1: titels met spaties moeten tussen aanhalingstekens kunnen; pas zo nodig je aanpak aan.
10. Elke uitlening krijgt een datum; `terug` toont hoeveel dagen het boek weg was.

**Portie 3 (nadat portie 2 werkt):**

11. `boekenplank top` toont de drie vaakst uitgeleende boeken.
12. Wijziging op requirement 5: het opslagformaat moet leesbare platte tekst zijn die een mens met een editor kan repareren; migreer bestaande data als jouw formaat dat nog niet is.
13. `boekenplank verwijderen <nummer>` mag alleen als het boek aanwezig is; nummers worden nooit hergebruikt.
14. Foutmeldingen gaan naar stderr en de exitcode is dan niet 0.
15. Wijziging op requirement 7: `zoek` toont ook uitleenstatus, in dezelfde kolomopmaak als `lijst`.

## Deel A - Eén lange chat

Werk de drie porties af in **één doorlopend gesprek** met je assistent. Plak code, foutmeldingen en testuitvoer in datzelfde gesprek; vraag om aanpassingen in datzelfde gesprek; alles in één venster. Begin tussendoor geen vers gesprek.

Houd naast je werk het logboek bij. Gebruik per waarneming de velden moment/portie, requirement, gespreksfragment, verwacht gedrag, waargenomen gedrag en uitgevoerde controle. Noteer elke keer dat je iets van dit lijstje ziet:

- **Vergeten instructie** - de assistent breekt iets dat eerder al afgesproken of werkend was.
- **Scope-verschuiving** - er verschijnt functionaliteit waar je niet om vroeg, of een requirement wordt "verbeterd" tot iets anders dan er staat.
- **Zelfverzekerde brij** - de assistent beweert stellig iets dat niet klopt: verwijst naar code die niet (meer) bestaat, vat de stand van zaken verkeerd samen, of rapporteert iets als af dat niet af is.
- **Zelf de draad kwijt** - noteer wanneer je niet meer weet wat de actuele stand is zonder terug te scrollen.

Rond af met een eindcontrole: loop alle vijftien requirements langs en noteer per stuk werkt / werkt niet / weet ik niet, met de uitgevoerde controle erbij. Noteer ook wanneer je geen van de genoemde symptomen hebt waargenomen.

(module1-deel-b)=

## Deel B - Dezelfde opdracht, nu met de loop

Lees na de les de [begeleide uitvoering van portie 1](eerste-uitvoering.md).
Bewaar de code en het logboek uit deel A apart. Begin met een nieuwe codebasis;
jij organiseert de gesprekken en overdrachten als orkestrator.

### Kies de uitvoering

Bij een beperkt abonnement kun je met de docent afspreken de vier perspectieven alleen bij portie 2 te gebruiken. Leg voor de andere porties in C1 vast welke beoordelaar alle criteria afdekt. Nieuwe functionaliteit en een datamigratie vragen nog steeds een plan en een menselijke beslissing; kosten alleen maken deze opdrachten niet geschikt voor `LIGHT`. Pas de omvang van de oefening aan als zij niet binnen het beschikbare budget past.

### Voer iedere portie uit

Gebruik de [manual adapter](https://github.com/misja/agent-role-loop/blob/main/adapters/manual/README.md)
en het [overdrachtslogboek](https://github.com/misja/agent-role-loop/blob/main/adapters/manual/handoff-log-template.md).
De begeleide uitvoering toont per stap ingevulde voorbeelden; voor je eigen
werk gebruik je de contracten en feitelijke uitkomsten.

1. **Leg de opdracht vast.** Schrijf C0 voor portie 1 met de vijf requirements als
   acceptatiecriteria. Noteer in C1 de normversies, `PLANNED`, planner,
   verhelderaar en geselecteerde beoordelaars. Wijs ieder criterium toe aan een
   passende beoordelaar. Vier perspectieven zijn hier een oefenkeuze.
2. **Laat een plan maken en beoordelen.** Open voor planner en verhelderaar
   afzonderlijke gesprekken met hun rolprompt en de invoer uit {core}`loop.md`.
   Bewaar C2 en C3 met hun versies. Volg bij een noodzakelijke planwijziging de
   begrensde herstelprocedure; leg de teller vast vóór herstel.
3. **Beslis over het plan.** Lees als mens het concrete plan en de planreview.
   Leg C4 vast met je reden en de planversie. Geef bij `PROCEED` de bouwer C1,
   C2, C4 en de leesbare normen. Bij `REVISE` of `STOP` volg je eerst de
   vastgelegde vervolgactie.
4. **Pas de code toe en controleer haar.** Open het bouwergesprek met zijn
   rolprompt. Bij een losse chat neem jij het codevoorstel over in de bestanden
   en voer jij de controles uit. Stuur de waargenomen uitvoer terug. Bewaar de
   codeversie en laat de bouwer C5 maken met criteria, bewijs en beperkingen.
5. **Laat onafhankelijk beoordelen.** Open één nieuw gesprek per geselecteerde
   beoordelaar. Geef rolprompt, C5-kern, codeversie, normen, besluiten en
   toegewezen criteria mee. Het maakgesprek en andere initial oordelen gaan
   niet mee. Bewaar alle C6's voordat je ze vergelijkt.
6. **Breng de oordelen samen en beslis.** Voeg verenigbare oordelen herleidbaar
   samen in C7. Geef alleen inhoudelijke tegenspraak aan de hoofdbeoordelaar.
   Bij `BLOCK` volg je de herstelregels uit {core}`loop.md` en registreer je de
   teller vóór herstel. Een resterende blokkade vraagt een menselijk vervolg;
   de rondelimiet heft haar niet op. Beslis na beoordeling zelf of je de code
   als basis voor de volgende portie accepteert en bewaar dat besluit.
7. **Ga door met de volgende portie.** Maak voor portie 2 en 3 elk een eigen
   C0 en logboek. Geef de geaccepteerde codeversie en de behouden eerdere eisen
   mee. Requirements 9, 12 en 15 wijzigen code binnen hun portie; maak daarvoor
   geen extra werkitems. Controleer ook of eerdere eisen nog werken.

Zo heb je na afloop precies drie werkitems. De rolprompts en contracten staan
in de [referentiesectie](../../referentie/index.md); de route blijft die van de core.

Je overdrachtslogboek bevat na elke portie de gebruikte artefacten, besluiten,
beoordeelde codeversie, controles en eventuele herstelstand.

Rond af met dezelfde eindcontrole als in deel A: alle vijftien requirements, werkt / werkt niet / weet ik niet.

## Reflectievragen

Beantwoord schriftelijk, met voorbeelden uit je beide logboeken:

1. Vergelijk je twee eindcontroles en hun bewijs. Welke verschillen zie je en
   welke uitkomsten zijn gelijk? Waar blijft je zekerheid beperkt?
2. Heb je in deel A een symptoom waargenomen? Zo ja, bij welke portie en welke
   gespreksinhoud kan eraan hebben bijgedragen? Zo nee, wat kun je uit deze run
   wel en niet afleiden over context rot?
3. Welke informatie uit een overdracht was bruikbaar, overbodig of ontbrak?
   Onderbouw met een concrete handeling van de ontvangende rol.
4. Welk besluit nam je bij C4? Wat heb je beoordeeld, gewijzigd of bewust
   aanvaard? Een ongewijzigd plan kan ook een gemotiveerd besluit zijn.
5. Vergelijk de afzonderlijke C6-oordelen waar je meerdere perspectieven
   gebruikte. Welke bevindingen verschillen of komen overeen? Kun je uit deze
   oefening afleiden wat een gezamenlijk gesprek zou hebben opgeleverd?
6. Kies één overdracht. Welke maakgeschiedenis bleef buiten de volgende context
   en welke relevante eisen gingen wel mee? Beschrijf het waargenomen gevolg,
   of leg uit waarom je geen gevolg kunt vaststellen.
7. Welke taken zou je met deze procedure uitvoeren? Weeg de vastgelegde
   tijdsbesteding en gevonden problemen mee. De formele proportionaliteitskeuze
   komt in module 5.

Dit is geen gecontroleerde vergelijking van twee methoden. In deel B ken je de
opdracht al en begin je met andere gesprekscontext. Ook modeluitvoer kan tussen
runs verschillen. Benoem daarom waarnemingen uit je eigen werk en de grenzen
van je verklaring; een betere of gelijke uitkomst bewijst geen algemeen effect.

## Variant zonder AI - rollenspel

Voer dezelfde opdracht uit met zes of zeven studenten. Verdeel planning,
verheldering, menselijke poort, bouwen en één of twee onafhankelijke
beoordelingen over de groep. Eén student krijgt bovendien de
orkestratieverantwoordelijkheid: C1 en het logboek bijhouden en de overdrachten
bewaken. Een afzonderlijke triagespeler is niet nodig. De docent kan bij
inhoudelijke tegenspraak de hoofdbeoordelaar zijn.

Spelregels:

- Wissel taakinhoud uitsluitend schriftelijk uit via de toepasselijke
  contractartefacten. Ontbrekende informatie komt als vraag of bevinding in het
  artefact; geef geen mondelinge toelichting buiten de overdracht.
- De bouwer bouwt de code. Binnen één lesuur kun je je beperken tot portie 1.
- De beoordelaars werken zonder overleg en leveren afzonderlijk C6 op. Met één
  beoordelaar is C6 het eindoordeel; met meerdere maakt de orkestrator C7 nadat
  alle oordelen beschikbaar zijn.
- Houd ook in het rollenspel relevante eisen en besluiten toegankelijk en leg
  eventuele herstelrondes vast.

Bespreek reflectievragen 3, 5 en 6. Wijs aan welke informatie de contracten
meegaven en welke informatie ontbrak. Noteer het gevolg voor de uitgevoerde
handelingen, zonder een bepaald probleem of voordeel vooraf te veronderstellen.
