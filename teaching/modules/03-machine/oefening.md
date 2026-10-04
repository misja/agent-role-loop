# Groen, volledig gedekt, en toch fout

Je meet eerst de uitkomst van een bestaande testsuite en vergelijkt daarna de
asserties met het vereiste gedrag. Vervolgens onderzoek je wat een
dekkingsdrempel verandert en pas je de analyse toe op je eigen code.

**Duur:** circa 60 minuten.
**Nodig:** een lokale kopie van deze repository, Python 3.10 of nieuwer en `uv`. Voor het tweede deel je boekenplank uit oefening 1, deel B, of de terugvalroute hieronder.
**Inleveren:** je ontleding van het defect, een poortoverzicht met gemeten uitkomsten en onderbouwde coverage-drempel, één blinde vlek en de beantwoorde verantwoordingsvragen.

## Voorbereiding

De commando's gebruiken een POSIX-shell, bijvoorbeeld Bash op Linux, macOS of
Windows met WSL. Installeer zo nodig `uv` met de
[installatiehandleiding](https://docs.astral.sh/uv/getting-started/installation/).
De installatie van pakketten vraagt internettoegang. Werk met oefengegevens
in een afzonderlijke map.

Bewaar bij elke controle: codeversie, omgeving/configuratie, invoer, commando,
verwachting, waargenomen uitvoer, exitcode en wat je daarmee niet hebt
vastgesteld. `echo "$?"` toont in deze shell de exitcode van het direct
voorafgaande commando; voer daartussen geen ander commando uit.

## Opdracht: meet de aangeleverde boekenplank

### 1. Maak een werkkopie en voer de suite uit

Voer vanuit de hoofdmap van deze repository uit. Bewaar eerst de broncommit;
de werkkopie is geen nieuwe repositoryversie.

```sh
git rev-parse HEAD
module3_werkmap=$(mktemp -d)
cp teaching/cases/module3-boekenplank/*.py "$module3_werkmap/"
cd "$module3_werkmap"
uv venv --python '>=3.10' .venv
uv pip install --python .venv/bin/python pytest pytest-cov
.venv/bin/python --version
uv pip list --python .venv/bin/python
.venv/bin/python -m pytest --cov=boekenplank --cov-report=term-missing
echo "$?"
```

Verwacht zes geslaagde tests en exitcode `0`; het rapport bevat gemeten regels,
ontbrekende regels en het dekkingspercentage. Noteer wat jouw uitvoering toont.
Als de setup faalt, leg de fout vast en herstel eerst de omgeving voordat je
conclusies over de code trekt. De volgende commando's gebruiken steeds deze
`.venv` en werkkopie.

### 2. Vergelijk één test met de eis

Requirement 6 uit module 1 verbiedt een tweede uitlening van een al uitgeleend
boek en vraagt een nette foutmelding. Open
`test_uitlenen_voorkomt_dubbele_uitlening` en `uitlenen()` in de werkkopie.
De casuscommentaren wijzen het bedoelde defect aan; dit is een begeleide analyse,
geen onbeïnvloede zoektocht.

1. Noteer de twee aanroepen, hun invoer en wat de bestaande assertie controleert.
2. Noteer welke waarde na de tweede aanroep in `uitgeleend_aan` staat. Voer zo
   nodig de twee aanroepen zelf uit in een Pythonconsole.
3. Vergelijk die uitkomst met requirement 6. Welke vereiste uitkomst ontbreekt
   in de assertie? Benoem ook welke uitgevoerde regel meetelt voor coverage.

Je ontleding is klaar als een andere lezer de eis, de assertie en het gemiste
gedrag in de code kan aanwijzen. De verklaring staat na de volgende meting.

### 3. Vergelijk dekking zonder en met drempel

`-k` selecteert tests. Onderstaand commando slaat de terugbrengtest over,
zonder haar uit het bestand te verwijderen. Voorspel vóór uitvoering welke
regels daardoor niet worden uitgevoerd en of het commando zal slagen.

```sh
.venv/bin/python -m pytest --cov=boekenplank --cov-report=term-missing -k 'not terug_maakt_boek_weer_beschikbaar'
echo "$?"
```

Voeg vervolgens aan dezelfde selectie een drempel toe:

```sh
.venv/bin/python -m pytest --cov=boekenplank --cov-report=term-missing -k 'not terug_maakt_boek_weer_beschikbaar' --cov-fail-under=95
echo "$?"
```

Vul met je eigen uitvoer onderstaande vergelijking in. Een mislukte
dekkingseis hoeft geen falende testassertie te betekenen; zoek in de uitvoer
welk onderdeel faalt.

| Uitvoering | Geslaagde/falende tests | Gemeten dekking | Ingesteld minimum | Exitcode en reden |
|---|---|---|---|---|
| Volledige suite | | | Geen via dit commando | |
| Zonder terugbrengtest | | | Geen via dit commando | |
| Dezelfde selectie met drempel | | | 95% | |

Voer het eerste testcommando zonder selectie opnieuw uit. Verwacht dezelfde
zes geslaagde tests als bij de start; bewaar ook dit resultaat. Lees nu de
verklaring en vergelijk haar met jouw metingen. Een afwijking vraagt onderzoek
naar versie, configuratie en omgeving; vul de verwachte cijfers niet als
waarneming in.

(module3-verklaring)=
## Uitleg na de metingen

### De assertie mist de tweede uitlening

De bestaande test leent boek 1 uit aan Misja, daarna aan Bob, en controleert:

```python
assert plank.boek(1).is_uitgeleend
```

De tweede uitlening overschrijft Misja door Bob. De assertie blijft waar: het
boek is nog steeds uitgeleend. `boek.uitgeleend_aan = naam` wordt uitgevoerd en
telt mee voor coverage. De assertie controleert geen weigering of behoud van
de eerste lener. Daardoor kunnen zes tests slagen bij 100% regeldekking,
terwijl requirement 6 wordt geschonden.

Een assertie op behoud van Misja als lener zou hier falen. Zij onderzoekt een
vereiste uitkomst zonder extra regeldekking nodig te hebben. Alleen die
assertie bewijst nog niet dat ook de gevraagde foutmelding correct is.

### De drempel stelt een afzonderlijke eis

Zonder terugbrengtest worden twee regels van `terug()` niet uitgevoerd. Voor
deze casus verwacht je vijf geslaagde tests, één niet-geselecteerde test en
ongeveer 93% dekking. Zonder minimum blijft de exitcode `0`. Met dezelfde
selectie en een minimum van 95% slagen de vijf tests nog steeds, maar mislukt
het commando wegens onvoldoende dekking.

95% is hier een proefkeuze boven de verlaagde dekking, geen onderbouwde
projectnorm. Zonder drempel blijven de testasserties van kracht; het rapport
stelt alleen geen minimum. Een drempel handhaaft een gekozen afspraak en
beoordeelt de betekenis van de asserties niet.

## Opdracht: verantwoord een eigen drempel

1. Noteer welke minimumdekking je voor de aangeleverde boekenplank zou verlangen.
   Motiveer dit met de requirements en de regels die je daadwerkelijk onderzocht.
2. Benoem een fout die ondanks die drempel kan blijven bestaan.
3. Leg apart vast: de gemeten dekking, jouw gekozen minimum en de 95%-proefkeuze.
   Zo kan de ontvanger onderscheiden wat is gemeten en wat jij verlangt.

(module3-setup)=
## Setup voor je eigen stack

Gebruik voor eigen Pythoncode pytest-cov als je tests met pytest draaien.
De [configuratiehandleiding](https://pytest-cov.readthedocs.io/en/latest/config.html)
legt uit hoe je de gemeten bron en drempel instelt. Vervang `boekenplank` in de
coveragecommando's door jouw modulenaam of bronmap en gebruik de bestaande
projectconfiguratie als uitgangspunt.

Voor Python kun je in je werkkopie een linter en type-checker installeren en
starten met onderstaande commando's. Vervang `boekenplank.py` door jouw
bronbestand of bronmap. Deze installatie verandert de omgeving, niet de code.

```sh
uv pip install --python .venv/bin/python ruff mypy
.venv/bin/python -m ruff check boekenplank.py
echo "$?"
.venv/bin/python -m mypy boekenplank.py
echo "$?"
```

[Ruff](https://docs.astral.sh/ruff/installation/) controleert ingestelde
lintregels; leg de gebruikte regels en configuratie vast.
[Mypy](https://mypy.readthedocs.io/en/stable/getting_started.html) gebruikt
typeannotaties en onderzoekt standaard de inhoud van ongetypeerde functies
niet volledig. Vermeld die grens wanneer je een groene uitslag bewaart.

Voor een andere taal gebruik je de test- en coveragegereedschappen van jouw
stack en een passende linter/type-checker. Zoek in hun officiële
installatiehandleiding de setup voor jouw versie en besturingssysteem. Leg
bron, installatie, meetbereik en startcommando vast voordat je ze uitvoert.
Vraag de docent om een stackgerichte startaanwijzing als die selectie ontbreekt;
de bovenstaande Pythoncommando's werken niet voor andere talen.

## Jouw opdracht: onderzoek je eigen boekenplank

Werk op een afzonderlijke branch of kopie van je boekenplank uit oefening 1,
deel B. Bewaar de uitgangsversie en de eerste uitvoer. Gebruik de setup hierboven
voor jouw stack. De uitgebreide begeleiding bij de casus blijft als naslag
beschikbaar; bepaal nu zelf welk geval en bewijs jouw code nodig heeft.

1. Zet ten minste tests met coverage op. Gebruik daarnaast een linter en, als
   je stack dat ondersteunt, een type-checker. Maak een poortoverzicht met
   controles, configuratie, commando's en wat elke uitslag wel en niet vaststelt.
   Dit zijn gekozen controles voor deze oefening, geen algemene verplichting
   om ieder gereedschap voor ieder werkitem te gebruiken.
2. Kies een coverage-drempel en motiveer die vanuit relevante requirements en
   ongedekte code. Leg dekking, ingestelde drempel en exitcodes vast. Deze stap
   is klaar als de controles aan jouw afspraken voldoen, of als je een
   resterende blokkade met oorzaak vastlegt.
3. Zoek één geval dat groen en gedekt is maar een requirement mist, of waarvan
   je de assertie onvoldoende vindt. Vind je er geen, construeer dan in je
   werkkopie een zwakke assertie. Noteer welke regel draait en welke vereiste
   uitkomst de assertie niet controleert.
4. Schrijf voor dat geval een gerichte assertie en voer haar uit. Noteer vóór
   uitvoering je verwachting, daarna je waarneming. Een falende assertie kan
   een defect of onjuiste verwachting tonen; vergelijk met de requirement.
   Bewaar de wijziging en uitvoer apart met een label, of herstel je tijdelijke
   testwijziging na registratie. Een volledige review volgt in module 4.

### Terugval: je eigen code ontbreekt

Gebruik een nieuwe kopie van de aangeleverde casus en dezelfde setup.
Voer stappen 1 en 2 daarop uit. Voor stappen 3 en 4 gebruik je het al besproken
dubbele-uitleningsgeval. Voeg in de bestaande test, na de tweede uitlening,
onderstaande assertie toe en voer de volledige suite opnieuw uit:

```python
assert plank.boek(1).uitgeleend_aan == "Misja"
```

Verwacht dat deze test faalt doordat Bob de eerste lener heeft overschreven.
Bewaar de testwijziging, jouw uitvoer en bewijsgrens apart. Deze terugval vraagt
geen nieuwe zoekfunctie of CLI. Je hebt zelf de gerichte controle uitgevoerd;
het bekende defect is geen eigen ontdekking en toont geen zelfstandige
analyse van je ontbrekende code aan.

## Verantwoordingsvragen

Beantwoord schriftelijk, met voorbeelden uit je werk:

1. **Beargumenteer** waarom de gekozen verplichte controles vóór beoordeling
   staan. Wat moet de beoordelaar nog aan de geschiktheid van het bewijs onderzoeken?
2. **Verantwoord** met je blinde vlek waarom 100% regeldekking niet samenvalt
   met correctheid. Welke uitspraak ondersteunt het getal wel?
3. **Verantwoord** jouw coverage-drempel voor het aangeleverde artefact. Welke
   afspraak laat haar handhaven en welke defecten kan zij doorlaten?
4. Je liet in oefening 1 een agent code schrijven. **Weeg af** welk vertrouwen
   de geleverde testsuite rechtvaardigt. Welke vergelijking met de requirements
   blijft nodig? Benoem ontbrekend eigen bewijs als je de terugvalroute gebruikte.
5. **Beargumenteer** welke controles jouw werkitem nodig heeft en welke je bij
   een kleine, omkeerbare wijziging zou kunnen overslaan. Onderscheid gekozen
   controles van een algemene verplichting om ieder gereedschap te gebruiken.
