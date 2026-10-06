# Boekenplankfilter: zelfstandig praktijkvoorbeeld

Dit materiaal hoort bij het hoofdstuk Van werkitem naar pull request van
agent-role-loop. Het is een bewerkt onderwijsvoorbeeld op basis van de
boekenplankcasus; er is geen echte historische agentrun nagespeeld.

Lees `overdrachten.md` voor W1, P1, besluiten, C5/C6 en herstel. De fictieve
besluiten zijn geen toestemming om aan een echt project te werken.
`overdrachtregister.csv` beschrijft hoe de informatie in de bundel is terug
te vinden. Platformobjecten zijn niet aangemaakt.

## Controleren

Python 3.10 of nieuwer, alleen standaardbibliotheek. Voer vanuit deze map uit:

```sh
python controleer.py basis basis
python controleer.py a zwak
python controleer.py a regressie
python controleer.py b volledig
```

Verwacht achtereenvolgens: 1 geslaagde test; 3 geslaagde tests; 1 falende test
(S4, uitgeleend boek verdwijnt); 4 geslaagde tests. Het derde commando geeft
bewust exitcode 1. `bewijs.txt` bevat uitgevoerde controles bij publicatie.

- `boekenplank_basis.py`: bestaande lijst zonder filter.
- `boekenplank_a.py`: geconstrueerde foutieve eerste oplevering.
- `boekenplank_b.py`: reparatie die de interne lijst behoudt.
- `basis-naar-a.patch` en `a-naar-b.patch`: toepasbaar op `boekenplank.py`.

Voor eigen Git-oefening: kopieer de basis naar `boekenplank.py` en leg die vast.
Pas `git apply basis-naar-a.patch` toe en voer `python controleer.py werk zwak`
uit. De regressiecontrole voor `werk` faalt. Pas daarna `git apply a-naar-b.patch`
toe: `python controleer.py werk volledig` slaagt. Commit en beoordeel de
werkelijke versies; vervang A/B-labels in eigen overdrachten door hun volledige
SHA's. Geef goedgekeurde plansnapshots aparte namen en vaste commitlinks.

De twee volledige codeversies zijn kleine vaste onderwijsartefacten, geen
parallel te onderhouden productvarianten. De cases van modules 3-5 zijn niet
gewijzigd. Dit voorbeeld bevat geen CLI, opslag of gebruikersbeheer.

## Aanvullende controles (optioneel)

Na de vier controles kun je onderzoeken wat er gebeurt wanneer een aanroeper
het filter expliciet uitschakelt, een ontvangen lijst wijzigt of na filteren een
boek toevoegt. Gebruik dezelfde Python-omgeving en bestanden als hierboven.
De aanvullende suite staat apart, zodat de oorspronkelijke S1-S4-controles en
hun verwachte uitkomsten behouden blijven.

Een lijst is hier de container met verwijzingen naar boekobjecten. Een nieuwe
lijst geeft de aanroeper ruimte om elementen te verwijderen of toe te voegen
zonder de opgeslagen lijst te wijzigen. De boekobjecten zelf worden niet
gekopieerd: een wijziging aan bijvoorbeeld een boektitel valt buiten deze
controle op lijstcontainers.

1. Voer vanuit deze map de aanvullende suite uit:

   ```sh
   python3 -B controleer_extra.py b
   ```

   Verwacht drie geslaagde tests en exitcode 0. E1 vergelijkt de standaardaanroep
   met expliciet `False`, ook bij een lege of volledig uitgeleende plank. E2
   wijzigt de ontvangen containers en controleert vervolgens de opgeslagen
   boeken en hun uitleentoestand. E3 filtert eerst en voegt daarna een boek toe;
   alle boeken moeten behouden blijven en ieder nummer moet uniek zijn.

2. Vergelijk met de geconstrueerde foutversie:

   ```sh
   python3 -B controleer_extra.py a
   ```

   Verwacht een falende suite en exitcode 1: E2 en E3 constateren dat A bij
   filteren de opslag wijzigt. E1 slaagt. Zo zie je dat een correcte lijst met
   beschikbare boeken nog niet bewijst dat volgende handelingen goed gaan.

3. Controleer desgewenst je eigen `boekenplank.py` met
   `python3 -B controleer_extra.py werk`. Na de reparatie hoort ook deze suite
   drie tests te laten slagen. Een foutmelding noemt het criterium waarvoor je
   de code opnieuw moet onderzoeken. Behoud daarnaast de oorspronkelijke
   S1-S4-controles: deze drie tests vervangen die controles niet.

Dit is aanvullende regressiedekking, geen herhaling van een eerdere agentrun.
`bewijs.txt` blijft de oorspronkelijke publicatie-uitvoer; nieuw bewijs voor
het toevoegen van deze suite staat in `onderzoek/58-proef/` in de bronrepository.

## Bundel en bronnen

De gepubliceerde zip bevat deze bestanden, `LICENSE`, `HERKOMST.md` en de
procesbasis onder `normen/core/`. Dat maakt de inhoud buiten GitHub leesbaar;
het reconstrueert geen native issues, reacties of reviews.

In de bronrepository maak je de zip opnieuw met
`python docs/package_practice.py`. Het script sluit caches en lokale werkbestanden
uit. De gegenereerde zip staat naast het praktijkhoofdstuk. Na een wijziging aan
de voorbeeldbestanden moet zij opnieuw worden opgebouwd en gecontroleerd.
