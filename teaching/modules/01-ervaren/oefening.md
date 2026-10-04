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

- **Vergeten instructie** - de assistent breekt iets dat eerder al afgesproken of werkend was (requirement 9 en 12 zijn er gevoelig voor, maar het kan overal opduiken).
- **Scope-verschuiving** - er verschijnt functionaliteit waar je niet om vroeg, of een requirement wordt "verbeterd" tot iets anders dan er staat.
- **Zelfverzekerde brij** - de assistent beweert stellig iets dat niet klopt: verwijst naar code die niet (meer) bestaat, vat de stand van zaken verkeerd samen, of rapporteert iets als af dat niet af is.
- **Zelf de draad kwijt** - noteer wanneer je niet meer weet wat de actuele stand is zonder terug te scrollen.

Rond af met een eindcontrole: loop alle vijftien requirements langs en noteer per stuk werkt / werkt niet / weet ik niet, met de uitgevoerde controle erbij. Noteer ook wanneer je geen van de genoemde symptomen hebt waargenomen.

## Deel B - Dezelfde opdracht, nu met de loop

Bewaar je code en logboek uit deel A apart en begin opnieuw, nu met een nieuwe codebasis volgens de [manual adapter](https://github.com/misja/agent-role-loop/blob/main/adapters/manual/README.md). Jij bent de orkestrator. Concreet:

1. Schrijf een werkitem (C0) voor portie 1 met de vijf requirements als
   acceptatiecriteria. Gebruik {core}`contracts/work-item.md`.
2. Kopieer het [logboeksjabloon](https://github.com/misja/agent-role-loop/blob/main/adapters/manual/handoff-log-template.md)
   naar een overdrachtslogboek voor dit werkitem.
3. Leg in C1 de oefenkeuze vast: `PLANNED`, met planner, verhelderaar en vier
   beoordelaarsperspectieven. Wijs ieder acceptatiecriterium toe aan een passende
   beoordelaar. Dit aantal dient de oefening en is geen algemene verplichting.
4. Laat de planner C2 maken en de verhelderaar het plan beoordelen met C3. Geef
   de voorgeschreven invoer en normen uit {core}`loop.md` mee. Start deze rollen
   in afzonderlijke gesprekken. Noteer de artefactversies in het logboek.
5. Neem als mens een C4-besluit over het concrete plan. Bij `PROCEED` geef je
   het plan en besluit aan de bouwer. Bij `REVISE` of `STOP` volg je de
   beschreven vervolgactie voordat de bouw verdergaat.
6. Geef de geselecteerde beoordelaars C5-kern, de codeversie, eisen, normen en
   relevant bewijs. Zij zien het maakgesprek en elkaars oordelen niet. Wacht op
   alle C6-oordelen. Voeg verenigbare oordelen samen in C7; laat de
   hoofdbeoordelaar inhoudelijke tegenspraak behandelen.
7. Volg bij een blokkade de begrensde herstelprocedure uit de core. Leg de
   verbruikte herstelronde vast vóór herstel. Een overgebleven blokkade vraagt
   een menselijk vervolg; zij wordt niet door de rondelimiet opgeheven. Beslis
   zelf of je de beoordeelde code als basis voor de volgende portie accepteert.
8. Herhaal stappen 1 tot en met 7 voor portie 2 en 3, elk met een eigen C0 en logboek.
   Dit levert in totaal drie werkitems op. Requirements 9, 12 en 15 horen bij
   hun portie en wijzigen de eerder gebouwde code; maak er geen extra werkitems
   van. Neem de eerdere eisen die behouden moeten blijven in de controle op.

Je overdrachtslogboek bevat na elke portie de gebruikte artefacten, besluiten,
beoordeelde codeversie, controles en eventuele herstelstand.

Bij een beperkt abonnement kun je met de docent afspreken de vier perspectieven alleen bij portie 2 te gebruiken. Leg voor de andere porties in C1 vast welke beoordelaar alle criteria afdekt. Nieuwe functionaliteit en een datamigratie vragen nog steeds een plan en een menselijke beslissing; kosten alleen maken deze opdrachten niet geschikt voor `LIGHT`. Pas de omvang van de oefening aan als zij niet binnen het beschikbare budget past.

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
