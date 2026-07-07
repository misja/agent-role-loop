# Ontwerp, regisseer en verantwoord (mini-project)

In de eerdere oefeningen kreeg je de opdracht, het artefact of de beslissing aangereikt. Nu is alles van jou: je ontwerpt een interface-uitbreiding op je boekenplank, stelt de randvoorwaarden vast, kiest je werkwijze en tooling, laat de AI bouwen binnen die kaders, en beoordeelt en verantwoordt het geheel. Het resultaat is een dossier waarin elke keuze verantwoord is.

**Duur:** circa 4 uur, verdeeld over twee sessies (ontwerp en kaders; bouw en oordeel).
**Nodig:** je boekenplank uit de eerdere modules (zie "Vooraf: kies je basis"), een AI-assistent, en de referentie: {core}`loop.md`, {core}`contracts/work-item.md` en het [kwaliteitsraamwerk](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md).
**Inleveren:** het dossier (zie onderaan) en de repository met je code.

## Vooraf: kies je basis

De uitbreiding bouwt voort op een **bestaande logica-laag**; dat is de voorwaarde die de kernvraag van deze module mogelijk maakt (hergebruikt de AI die laag, of dupliceert hij haar?). Wie zonder bestaande laag begint, omzeilt ongemerkt die kern. Kies een van drie:

1. **Je eigen boekenplank** uit oefening 1 (deel B), in Python: bouw er een [Textual](https://textual.textualize.io/)-interface op. Dit is de standaardroute.
2. **Je eigen stack:** een andere taal of interface-vorm mag, zolang je voortbouwt op je bestaande logica-laag. Het principe is de leerstof; de tooling is inwisselbaar.
3. **Terugvaloptie:** heb je je eigen boekenplank niet meer, bouw dan voort op de boekenplank uit `teaching/cases/module5-verwijderen/` (logica met reserveringen en verwijderen).

## Stappen

1. **Ontwerp de uitbreiding en schrijf het werkitem.** Bepaal wat je interface moet kunnen (bijvoorbeeld: lijst tonen, uitlenen, reserveren, terugbrengen; wees selectief). Schrijf een werkitem volgens {core}`contracts/work-item.md`, met toetsbare acceptatiecriteria. Klaar wanneer: het werkitem beschrijft de gewenste uitkomst, niet de implementatie.
2. **Stel de randvoorwaarden vast.** Beslis welke stijl, type checker, linter, formatter en welk projectbeheer gelden, leg ze vast in een kort conventiedocument in je repository, en automatiseer wat te automatiseren is. Verantwoord per keuze waarom deze norm, en herken de levensloop: jouw oordeel wordt conventie, jouw conventie wordt poort. Klaar wanneer: een buitenstaander kan uit je document aflezen wat "goed" in jouw project betekent en welke poorten dat afdwingen.
3. **Kies je werkwijze en tool, en verantwoord de keuze.** Bepaal waar je werkitems en artefacten leven (bestanden in de repository, een projectbord, iets anders). Benoem daarbij de drie niveaus (werkwijze, medium, tool) en weeg expliciet de zeggenschap over je data mee: waar staat het, onder welk regime, hoe kom je er weg? Klaar wanneer: je kunt uitleggen wat er bij een toolwissel verloren gaat en wat niet.
4. **Kies hoeveel van de loop je inzet, en verantwoord die keuze.** Volledige loop, licht pad, of iets ertussenin: dit is een expliciete beslissing, geen standaardinstelling. Onderbouw met omvang, risico en omkeerbaarheid van je uitbreiding. Klaar wanneer: je inzet volgt aantoonbaar uit je afweging, niet uit gemak.
5. **Regisseer de bouw.** Laat de AI de interface bouwen binnen je werkitem en je randvoorwaarden. Bewaak de scope, houd de poorten als toegangsvoorwaarde (bouw gaat pas door bij groen), en noteer waar je moest ingrijpen. Klaar wanneer: de acceptatiecriteria zijn aantoonbaar gehaald en de poorten staan op groen.
6. **Beoordeel en besluit.** Beoordeel het resultaat met architectuur en onderhoudbaarheid als zwaartepunt: wijs concreet aan waar de AI je bestaande logica hergebruikt en waar hij haar dupliceert, en wat dat betekent voor de volgende wijziging. Vel daarna je eigen poort-beslissing over oplevering: mag dit zo door, en zo niet, wat eerst? Klaar wanneer: je oordeel en je beslissing zijn geschreven en onderbouwd.

## Verantwoordingsvragen

Beantwoord schriftelijk, als sluitstuk van het dossier:

1. **Verantwoord de keten als geheel:** welke kwaliteitslaag droeg in jouw project welke verantwoordelijkheid, en waar in de levensloop (oordeel, conventie, automatisering) zat elke norm die je stelde?
2. Je hebt ergens een conventie gesteld die een ander redelijkerwijs anders had gekozen. **Beargumenteer** je keuze, en beschrijf wat er zou veranderen als je de andere had genomen.
3. **Verantwoord** je loop-inzet uit stap 4 achteraf: bleek je afweging te kloppen, en wat zou je bij een volgende, grotere uitbreiding anders doen?
4. Wat kon in dit project alleen door jou worden vastgesteld, en wat had je met een strengere poort of een extra beoordelaar alsnog niet afgevangen? **Beargumenteer** waarom dat oordeel bij de mens blijft.

## Inleveren: het dossier

Het dossier bestaat uit zes onderdelen; de code hoort in je repository:

1. het werkitem (stap 1);
2. het conventiedocument met verantwoording (stap 2);
3. de werkwijze- en toolkeuze met verantwoording (stap 3);
4. de loop-inzet-beslissing met verantwoording (stap 4);
5. je beoordeling en je poort-beslissing (stap 6);
6. de beantwoorde verantwoordingsvragen.

```{note}
Terzijde: dit lesmateriaal is zelf volgens deze werkwijze gebouwd. De repository
waarin het leeft gebruikt dezelfde contracten, dezelfde poort-momenten en een
projectbord met werkitems; de commit-geschiedenis toont de beslissingen. Wie wil
zien hoe de werkwijze er in het echt uitziet, kan daar rondkijken.
```
