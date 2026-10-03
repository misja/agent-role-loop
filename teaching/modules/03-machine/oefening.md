# Groen, volledig gedekt, en toch fout

Deze oefening onderzoekt een boekenplank waarvan alle tests slagen en alle
gemeten regels zijn uitgevoerd. Je vergelijkt de asserties met het vereiste
gedrag. Daarna onderzoek je wat een coverage-drempel toevoegt en pas je de
analyse toe op je eigen code.

**Duur:** circa 60 minuten.
**Nodig:** een lokale kopie van deze repository, Python en `uv`. Voor het tweede deel je boekenplank uit oefening 1, deel B.
**Inleveren:** je ontleding van het defect, een poortoverzicht met gemeten uitkomsten en onderbouwde coverage-drempel, één blinde vlek en de beantwoorde verantwoordingsvragen.

## Worked example: een groene boekenplank met een blinde vlek

### Opdracht: maak een afzonderlijke werkkopie

Voer vanuit de hoofdmap van deze repository de volgende commando's uit. Ze
maken een tijdelijke werkkopie en een eigen Pythonomgeving. De originele
casusbestanden blijven beschikbaar om te vergelijken.

```sh
module3_werkmap=$(mktemp -d)
cp teaching/cases/module3-boekenplank/*.py "$module3_werkmap/"
cd "$module3_werkmap"
uv venv .venv
uv pip install --python .venv/bin/python pytest pytest-cov
.venv/bin/python -m pytest --cov=boekenplank --cov-report=term-missing
echo "$?"
```

De installatie vraagt internettoegang. De omgeving staat in `.venv` binnen je
werkkopie; de commando's hieronder gebruiken die omgeving expliciet. Verwachte
uitkomst: zes geslaagde tests, 100% dekking en exitcode `0`. Bewaar de uitvoer en
noteer de Python- en pakketversies, bijvoorbeeld met `.venv/bin/python --version`
en `uv pip list --python .venv/bin/python`.

### Uitleg: de assertie mist de tweede uitlening

Bekijk `test_uitlenen_voorkomt_dubbele_uitlening` in de werkkopie. Requirement 6
zegt dat een al uitgeleend boek niet nogmaals mag worden uitgeleend. De test
leent boek 1 uit aan Misja, daarna aan Bob, en controleert:

```python
assert plank.boek(1).is_uitgeleend
```

Die assertie slaagt, want het boek is uitgeleend. In de implementatie is de
naam van Misja echter overschreven door Bob. De regel
`boek.uitgeleend_aan = naam` is uitgevoerd en telt mee voor de dekking. De test
controleert niet dat de tweede uitlening wordt geweigerd en de eerste lener
behouden blijft.

Een test die de weigering controleert, zou het defect zichtbaar maken. Ook een
assertie op het behoud van Misja als lener zou hier falen. Dit verandert de
betekenis van de controle, zonder dat er extra regeldekking nodig is.

## Een dekkingrapport zonder drempel

### Opdracht: sla één test over

Voer in dezelfde werkkopie uit:

```sh
.venv/bin/python -m pytest --cov=boekenplank --cov-report=term-missing -k 'not terug_maakt_boek_weer_beschikbaar'
echo "$?"
```

`-k` selecteert de tests; hier wordt alleen de terugbrengtest overgeslagen.
Verwacht vijf geslaagde tests, één niet-geselecteerde test, ongeveer 93% dekking
en exitcode `0`. De twee regels van `terug()` zijn niet uitgevoerd. De originele
testsuite is behouden; een volgende uitvoering zonder `-k` gebruikt alle tests.

Voeg nu een drempel toe:

```sh
.venv/bin/python -m pytest --cov=boekenplank --cov-report=term-missing -k 'not terug_maakt_boek_weer_beschikbaar' --cov-fail-under=95
echo "$?"
```

De vijf tests slagen nog steeds, maar het commando mislukt met een niet-nul
exitcode omdat de dekking onder 95% ligt. Bewaar beide uitkomsten. Voer tot slot
het eerste testcommando zonder selectie opnieuw uit: alle zes tests moeten
weer slagen met 100% dekking.

### Uitleg: wie kiest de drempel?

De drempel van 95% is voor deze proef gekozen omdat zij boven de verlaagde
dekking ligt. Daarmee kun je het verschil in exitcode waarnemen. Het getal is
nog geen onderbouwde projectnorm. Noteer welke dekking je voor deze boekenplank
zou verlangen en waarom. Benoem een fout die ondanks die dekking kan blijven
bestaan. De dubbele uitlening is daarvan al een voorbeeld.

Zonder drempel controleert de testsuite haar asserties nog steeds. Alleen het
dekkingrapport stelt dan geen minimum. Een gekozen drempel maakt dat minimum
een geautomatiseerde toegangsvoorwaarde; zij beoordeelt de kwaliteit van de
asserties niet.

## Jouw opdracht: onderzoek je eigen boekenplank

Werk op een afzonderlijke branch of kopie van je boekenplank uit oefening 1,
deel B. Bewaar de uitgangsversie en de eerste uitvoer.

1. Zet ten minste tests met coverage op. Gebruik daarnaast een linter en, als je stack dat ondersteunt, een type-checker. Maak een overzicht van de controles, hun commando's en wat elke uitslag wel en niet vaststelt.
2. Kies een coverage-drempel en motiveer die vanuit de relevante requirements en ongedekte code. Leg de gemeten dekking, ingestelde drempel en exitcodes vast. Je bent klaar met deze stap als de controles aan je gekozen afspraken voldoen, of als je een resterende blokkade met oorzaak vastlegt.
3. Zoek één geval dat groen en gedekt is maar een requirement mist, of waarvan je de assertie onvoldoende vindt. Als je er geen aantreft, construeer dan in je werkkopie een zwakke assertie. Noteer welke regel draait en welke vereiste uitkomst de assertie niet controleert.
4. Schrijf voor dat geval een gerichte assertie die het vereiste gedrag controleert en vergelijk de uitkomst. Een falende assertie toont een defect in de implementatie of een onjuiste verwachting; lokaliseer dat verschil aan de hand van de requirement. Herstel daarna je tijdelijke testwijziging of bewaar haar apart met een label. Een volledige review hoort pas bij module 4.

Heb je je eigen boekenplank niet meer, gebruik dan de werkkopie van het
voorbeeld. Voeg requirement 7 toe: `zoek` zoekt hoofdletterongevoelig in titel
en auteur. Schrijf een test waarmee alle toegevoegde regels worden uitgevoerd
en onderzoek welke invoer of assertie desondanks ontbreekt. Gebruik dit geval
voor stap 3 en 4.

## Verantwoordingsvragen

Beantwoord schriftelijk, met voorbeelden uit je werk:

1. **Beargumenteer** waarom de gekozen geautomatiseerde controles vóór de beoordeling worden uitgevoerd. Wat moet de beoordelaar nog over de geschiktheid van het bewijs onderzoeken?
2. **Verantwoord** met je blinde vlek waarom 100% regeldekking niet samenvalt met correctheid. Welke uitspraak ondersteunt het getal wel?
3. **Verantwoord** welke coverage-drempel je voor het aangeleverde artefact kiest. Welke eis dwingt die drempel af en welke defecten kan zij doorlaten?
4. Je liet in oefening 1 een agent code schrijven. **Weeg af** welk vertrouwen de geleverde testsuite rechtvaardigt. Welke vergelijking met de requirements blijft nodig?
5. **Beargumenteer** welke controles je voor jouw werkitem nodig vindt en welke je bij een kleine, omkeerbare wijziging zou kunnen overslaan. Maak onderscheid tussen een gekozen controle en een algemene verplichting om ieder gereedschap te gebruiken.
