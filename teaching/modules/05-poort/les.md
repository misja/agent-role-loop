# Go of no-go op het onomkeerbare

> **Status:** outline met leeruitkomsten. De volledige lesuitwerking (slides, timing per werkvorm, docentennotities) is vervolgwerk.

## Plaats in de leerlijn

Vijfde module. In module 4 heb je geoordeeld: de vier perspectieven gewogen en geprioriteerd. Dit is de stap voordat werk doorgaat: de menselijke poort. Vereiste voorkennis: module 4 afgerond, en het kwaliteitsraamwerk.

De les hoort bij [oefening 5](oefening.md), waarin je als poort een go/no-go velt over een onomkeerbare operatie.

## Leeruitkomsten

De leeruitkomsten staan als "Wat ga je leren" op de [module-index](index.md).

## Opbouw

### De poort is menselijk

In de loop is er één beslismoment dat aan geen enkele andere rol wordt overgelaten: de menselijke poort ({core}`roles/human-gate.md`). De machine stelt vast dat de code werkt; de beoordelaars wegen de kwaliteit; maar of een change ook echt door mag, blijft een mens. De poort vraagt niet "is de code goed", maar "is dit nog steeds het juiste, en zijn de gevolgen aanvaardbaar".

### Onomkeerbaarheid verandert de vraag

Bij een omkeerbare wijziging is een fout te herstellen; bij een onomkeerbare niet. `verwijderen` wist een boek en zijn wachtlijst definitief, ook als er nog reserveringen openstaan. De machine bevestigt dat de operatie doet wat er staat, en toch is dat niet de vraag die telt. De poort weegt de kosten van een verkeerde go die je niet meer terugdraait: is het aanvaardbaar dat de reservering van een lener zonder waarschuwing verdwijnt, of moet er eerst iets (een bevestiging, een archief, een soft-delete)?

Dit is precies wat geen geautomatiseerde poort kan leveren. Een drempel of scan stelt objectief vast dat een regel is uitgevoerd of dat een test slaagt. Of het gevolg van een onomkeerbare operatie in deze context aanvaardbaar is, is geen eigenschap van de code maar een oordeel over waarde en risico. Dat oordeel hoort bij de mens.

### Proportionaliteit en triage

Niet elke beslissing verdient dezelfde poort. Een kleine, omkeerbare wijziging tegenhouden voor een zware afweging is net zo verkeerd als een onomkeerbare zonder nadenken doorlaten. De poort weegt de inzet tegen wat er op het spel staat: hoe omkeerbaar is dit, en hoe groot is de schade als het misgaat? Triage doet die weging vooraf, met de S/M/L-heuristiek en de kosten (tijd, tokens, aandacht) als maat. Proportionaliteit is zo zelf een poort-vaardigheid: het schaarse menselijke oordeel inzetten waar het telt.

### Wat dit is en wat niet

Deze module gaat over de poort-beslissing: go of no-go op het onomkeerbare, en waarom die bij de mens ligt. Niet over de kwaliteit van de code (dat was module 4, het oordeel), en niet over de architectuur of het ontwerp (dat is module 6). De vraag is smaller en zwaarder: mag dit zo door?

## Werkvormen en toetsing

- Werkvormen: korte instructie, gezamenlijke go/no-go op de verwijder-operatie (worked example), daarna zelf een poort-beslissing vellen in oefening 5.
- Toetsing: in deze fase formatief, via de poort-beslissing en de verantwoordingsvragen van oefening 5.

## Bronnen

- Het raamwerk [Kwaliteit als gedeelde verantwoordelijkheid](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md), sectie "Kwaliteit is geen rol" en de menselijke poort.
- De repository zelf: {core}`roles/human-gate.md` (de menselijke poort) en {core}`contracts/gate-decision.md` (de go/no-go, C4).

## Afronding

### Wat heb je geleerd

De menselijke poort is de beslissing die aan geen machine en geen beoordelaar wordt overgelaten: mag dit zo door? Bij een onomkeerbare operatie weegt de poort de kosten van een verkeerde go die niet terug te draaien is. Of dat gevolg aanvaardbaar is, is geen code-eigenschap maar een oordeel over waarde en risico, en dat hoort bij de mens. Proportionaliteit bepaalt hoe zwaar de poort mag wegen: stem de inzet af op wat er op het spel staat.

### Zelfcheck

Beantwoord uit je hoofd; de sleutel wijst alleen waar je het kunt nakijken.

1. Een machine bevestigt dat `verwijderen` werkt. Waarom is dat niet de vraag die de poort beantwoordt, en wie moet die vraag dan wel beantwoorden? (zie "De poort is menselijk" en "Onomkeerbaarheid verandert de vraag")
2. Waarom verandert onomkeerbaarheid de poort-beslissing, vergeleken met een wijziging die je kunt terugdraaien? (zie "Onomkeerbaarheid verandert de vraag")
3. Wanneer zou je een change juist niet door een zware poort halen, en waarmee weeg je dat af? (zie "Proportionaliteit en triage")

### Volgende stap

Tot nu beoordeelde en bewaakte je wat de AI bouwde. Module 6 (Ontwerpen en verantwoorden) draait het om: je ontwerpt zelf de volgende uitbreiding, regisseert en bewaakt de AI, en verantwoordt je keuzes tegen het kader. Daar landt de door AI gebouwde Textual-code, waar architectuur en onderhoudbaarheid de les zijn. Je gaat van poort naar ontwerper.
