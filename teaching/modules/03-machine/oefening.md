# Oefening 3 - Groen, volledig gedekt, en toch fout

Een machine kan je vertellen dat alle tests slagen en dat elke regel code is gedekt. Deze oefening laat zien dat dat allebei waar kan zijn terwijl de code het verkeerde doet. Je begint met een aangeleverd voorbeeld dat we samen ontleden, en past het daarna toe op je eigen boekenplank.

**Duur:** circa 60 minuten.
**Nodig:** het materiaal in `teaching/cases/module3-boekenplank/` uit de repository, met `pytest` en `pytest-cov`. Voor het tweede deel je eigen boekenplank uit oefening 1, deel B.
**Inleveren:** je ontleding van het defect, je eigen poortopstelling en groen-maar-fout-geval, en de beantwoorde verantwoordingsvragen.

## Worked example: een groene boekenplank met een blinde vlek

In `teaching/cases/module3-boekenplank/` staat een minimale boekenplank met een testsuite. Draai eerst de poort:

```
pytest --cov=boekenplank --cov-report=term-missing
```

Je ziet twee dingen die geruststellend lijken: alle tests slagen, en de dekking is 100%. Geen regel ontbreekt. De geautomatiseerde poort staat op groen, en in de loop zou dit boek dus toegelaten worden tot de review.

Toch zit er een fout in. Bekijk `test_uitlenen_voorkomt_dubbele_uitlening`. De naam belooft requirement 6 te bewaken: een al uitgeleend boek kan niet nogmaals worden uitgeleend. De test leent boek 1 uit aan Misja, leent het daarna uit aan Bob, en controleert dan:

```python
assert plank.boek(1).is_uitgeleend
```

Die assertie slaagt, want het boek *is* uitgeleend, alleen nu aan Bob. De tweede uitlening had geweigerd moeten worden en is dat niet; de eerste lener is stil verdwenen. De regel `boek.uitgeleend_aan = naam` in `uitlenen` draait, dus de dekking is volledig, maar de assertie controleert dát er iets gebeurde, niet dat het juiste gebeurde.

Merk op hoe precies dit de raamwerk-vraag is: toetst deze test wel het juiste? Coverage kan die vraag niet beantwoorden. Een sterkere assertie zou de tweede uitlening hebben afgewezen, of hebben gecontroleerd dat boek 1 nog steeds aan Misja is uitgeleend. Dat is geen extra regel dekking; het is een ander oordeel over wat de test moet bewijzen.

## Het tweede gezicht: een poort die niets eist

De worked example liet zien dat een groene poort het verkeerde kan toetsen. Er is een tweede geval, en dat is scherper. Draai de poort nog eens:

```
pytest --cov=boekenplank
```

De dekking is 100%, maar niets dwingt dat af: er staat geen `--cov-fail-under`-drempel, en er draait geen linter of type-checker. Haal een paar tests weg en draai opnieuw - de dekking zakt, en tóch faalt er niets. De poort rapporteert een getal, maar eist er niets mee.

Je kunt de poort laten bijten met een drempel, bijvoorbeeld `pytest --cov=boekenplank --cov-fail-under=90`. Doe dat, en kijk wat er verandert. Maar daar begint de eigenlijke vraag, en de vlag lost hem niet op: **waarom 90, en niet 80 of 100?** De 100% van dit artefact is toevallig gehaald, geen bewijs, en er is geen objectief juist getal. Zodra je een drempel kiest, kies jij een norm, en die moet je kunnen verantwoorden: wat betekent dit getal, wat laat het door en wat houdt het tegen? De machine kan die keuze niet voor je maken. Dat is het punt van dit tweede gezicht: niet "zet de vlag en klaar", maar het besef dat iemand moet besluiten wat de poort eist. Voel het ongemak dat die norm van jou komt en niet van de machine.

## Jouw opdracht: doe het op je eigen boekenplank

Neem je eigen boekenplank uit oefening 1, deel B (je AI-gebouwde versie). Zet er de geautomatiseerde poorten omheen en zoek je eigen blinde vlek:

1. Zet ten minste een testsuite met coverage op. Laat een linter en, als je stack die heeft, een type-checker meedraaien. Noteer welke poorten je hebt en wat elke poort wel en niet vaststelt.
2. Breng de dekking zo hoog als je redelijk kunt. Noteer het cijfer.
3. Zoek of construeer in je eigen code een geval dat **groen en gedekt** is en tóch fout, of waarvan je niet zeker bent dat de test het juiste toetst. Beschrijf die blinde vlek in dezelfde termen als het worked example: welke regel draait, en wat de assertie wel en niet controleert.

Heb je je boekenplank uit oefening 1 niet meer, gebruik dan het aangeleverde voorbeeld: voeg requirement 7 (`zoek` in titel en auteur, hoofdletterongevoelig) toe, schrijf er een test bij die groen is en 100% blijft, en beredeneer of die test het juiste toetst.

## Verantwoordingsvragen

Beantwoord schriftelijk, met voorbeelden uit je werk:

1. **Beargumenteer** waarom de geautomatiseerde poorten vóór de beoordeling horen en niet erin. Wat zou er misgaan als je beoordelingsaandacht zou besteden aan wat de poort al vaststelt?
2. **Verantwoord** aan je eigen groen-maar-fout-geval waarom 100% coverage niet samenvalt met correctheid. Welke vraag beantwoordt coverage wel, en welke niet?
3. **Verantwoord** welke coverage-drempel je op het aangeleverde artefact zou zetten, en waarom dat getal en geen ander. Leg uit waarom de 100% hier toevallig is en geen bewijs, en waarom het kiezen van de norm een menselijk oordeel is dat de machine niet kan maken.
4. Je had bij oefening 1 deel B een agent code laten schrijven. **Weeg af** hoe betrouwbaar een door een agent geleverde groene testsuite is, en wat je daarom zelf moet blijven controleren.
5. Wat de machine liet liggen, is in module 4 het werk van de beoordelaars. **Beargumenteer** welke van je poorten je niet zou durven weglaten en welke je bij een klein, omkeerbaar werkitem wél proportioneel zou kunnen overslaan.
