# Oefening 1 - Ervaar context rot

Je gaat twee keer dezelfde middelgrote opdracht doen met een AI-assistent. De eerste keer in één lange chat, zonder structuur. De tweede keer met de rollenloop, waarbij jij de orkestrator bent. Het verschil is de leerstof.

**Duur:** deel A circa 90 minuten (vóór les 1), deel B circa 90 minuten (na les 1), reflectie 30 minuten.
**Nodig:** een chatgebaseerde AI-assistent naar keuze, het logboekformat hieronder, en voor deel B de bestanden uit `core/` en `adapters/manual/` van de repository.
**Inleveren:** je logboek uit deel A, je overdrachtslogboek uit deel B, en de beantwoorde reflectievragen.

## De opdracht (voor beide delen dezelfde)

Bouw een command-line-tool `boekenplank` voor een kleine bibliotheek, in een taal naar keuze. De requirements krijg je in drie porties; geef ze in deze volgorde aan je assistent en niet allemaal tegelijk. Dat is bewust: zo komen requirements in de echte wereld ook binnen, en het is precies de situatie waarin context rot toeslaat.

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

Houd naast je werk het logboek bij. Noteer elke keer dat je iets van dit lijstje ziet, met het requirement-nummer erbij:

- **Vergeten instructie** - de assistent breekt iets dat eerder al afgesproken of werkend was (requirement 9 en 12 zijn er gevoelig voor, maar het kan overal opduiken).
- **Scope-verschuiving** - er verschijnt functionaliteit waar je niet om vroeg, of een requirement wordt "verbeterd" tot iets anders dan er staat.
- **Zelfverzekerde brij** - de assistent beweert stellig iets dat niet klopt: verwijst naar code die niet (meer) bestaat, vat de stand van zaken verkeerd samen, of rapporteert iets als af dat niet af is.
- **Zelf de draad kwijt** - ook jou overkomt het: noteer wanneer jíj niet meer weet wat de actuele stand is zonder terug te scrollen.

Rond af met een eindcontrole: loop alle vijftien requirements langs en noteer per stuk werkt / werkt niet / weet ik niet.

## Deel B - Dezelfde opdracht, nu met de loop

Gooi je code uit deel A weg (bewaar het logboek!) en begin opnieuw, nu volgens de procedure in `adapters/manual/README.md`. Jij bent de orkestrator. Concreet:

1. Schrijf één werkitem (C0) per portie; de porties zijn je werkitems, de requirements van de portie zijn de acceptatiecriteria. Gebruik het format uit {core}`contracts/work-item.md`.
2. Kopieer `adapters/manual/handoff-log-template.md` naar een overdrachtslogboek per werkitem.
3. Doorloop per werkitem de pipeline: triage, planner, verhelderaar, **poort (dat ben jij, op papier)**, bouwer, vier beoordelaars in aparte verse vensters, hoofdbeoordelaar. Eén vers chatvenster per rol; alleen het artefact gaat mee.
4. De wijzigings-requirements (9, 12, 15) zijn in deze opzet nieuwe werkitems die op bestaande code landen; merk op hoe anders dat voelt dan in deel A.

Tip over kosten: met een gratis of beperkt abonnement is de volledige loop voor elke portie misschien te duur. Het is acceptabel om de loop volledig te draaien voor portie 2 en voor portie 1 en 3 het lichte pad te nemen (triage zegt `LIGHT`); noteer die keuze dan in je logboek. Dat is geen concessie maar proportionaliteit, en precies waar triage voor bestaat.

Rond af met dezelfde eindcontrole als in deel A: alle vijftien requirements, werkt / werkt niet / weet ik niet.

## Reflectievragen

Beantwoord schriftelijk, met voorbeelden uit je beide logboeken:

1. Vergelijk je twee eindcontroles. Waar zaten de verschillen, en waar zat vooral het verschil in hoe *zeker* je van je antwoorden was?
2. Op welk moment in deel A merkte je het eerste symptoom van context rot, en bij welke portie? Wat stond er op dat moment allemaal al in het gesprek?
3. Welk contract-artefact uit deel B heeft je het meeste opgeleverd, en welke vond je op het eerste gezicht overdreven? Zou je die laatste bij een groter werkitem nog steeds overdreven vinden?
4. Bij de poort (C4) moest je zelf beslissen in plaats van doorklikken. Heb je daar iets tegengehouden of aangepast? Zo nee, waar zou de poort wél waarde hebben gehad in deel A?
5. De beoordelaars zagen elkaars oordeel niet. Vergelijk de vier C6-oordelen: wat vond er maar één, en had je dat ook gevonden als ze één gezamenlijk gesprek hadden gedeeld?
6. Geef een voorbeeld uit je overdrachtslogboek waar het concreet hielp dat een rol de context van een andere rol niet zag. (In module 2 ontleed je dit tot het ontwerpverband: interface, implementatie en wat er verborgen wordt.)
7. Voor welke taken zou jij deze loop voortaan inzetten, en voor welke uitdrukkelijk niet? Onderbouw met de S/M/L-heuristiek én met je eigen tijdsbesteding in deel A en B.

## Variant zonder AI - rollenspel

Dezelfde oefening werkt zonder AI, met een groep van zes of zeven studenten. De opdracht blijft identiek, maar de rollen worden door mensen gespeeld: één triage, één planner, één verhelderaar, één poort, één bouwer, en één of twee beoordelaars die na de bouw elk afzonderlijk (zonder overleg!) een C6 schrijven; de docent of een zevende student is hoofdbeoordelaar.

Spelregels:

- Spelers mogen **uitsluitend** communiceren via de contract-artefacten, schriftelijk. Geen overleg, geen toelichting bij de overdracht, geen vragen buiten de artefacten om; wie iets mist, schrijft dat in het eigen artefact op (de verheldering heeft daar zelfs een veld voor).
- De bouwer bouwt echt (portie 1 volstaat binnen een lesuur).
- De orkestrator-taak rouleert niet: één student beheert het overdrachtslogboek en bewaakt dat niemand buiten de artefacten om praat.

De debriefing draait om dezelfde reflectievragen 3, 5 en 6. Deze variant maakt voelbaar wat de contracten dragen en wat er verloren gaat als de interface te smal is - zonder dat er een AI of abonnement aan te pas komt.
