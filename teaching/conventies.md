---
orphan: true
---

# Projectconventies voor het onderwijsmateriaal

Dit document bindt de conventies die gelden voor al het materiaal onder
`teaching/`. Voor bestaande documenten (de schrijfwijzer, de begrippenlijst) wijst
het ze aan; het modulestramien hieronder legt het zelf vast. Zo hangt de toepassing
niet af van wie een taak schrijft.

## Welke conventies gelden

Voor al het werk onder `teaching/` gelden:

- de schrijfwijzer (`teaching/schrijfwijzer.md`) voor register, terminologie en
  opmaak;
- de begrippenlijst (`teaching/begrippen.md`) voor de vaste termen;
- het modulestramien (hieronder) voor de vaste structuur van elke module.

## Modulestramien

Elke module volgt een vast stramien: een herkenbare kop en staart die overal
gelden, met een hart dat vrij is naar de aard van de module. Zo neemt de vorm
routine-last weg en kan de student zijn aandacht op de inhoud richten.

### Vaste kop (in `index.md`)

- Een korte samenvatting van het onderwerp en de kwaliteitslaag die de module
  behandelt.
- Puntsgewijs "Wat ga je leren": de leeruitkomsten als advance organizer, zodat de
  student vooraf weet waar het heen gaat. Geformuleerd als kunnen-verantwoorden,
  niet als hebben-opgeleverd.

### Flexibel hart (in `les.md` en `oefening.md`)

Uitleg, worked example, ontwerpopdracht of een combinatie, naar de aard van de
module. Hier geldt onverkort de tekstsoorten-regel uit de schrijfwijzer: een
consequent en zichtbaar onderscheid tussen uitleg en handelingen, zodat de student
altijd weet of hij theorie leest of iets uitvoert.

### Vaste staart (aan het eind van `les.md`)

In deze volgorde:

1. **Wat heb je geleerd:** een korte terugblik op de kern van de module.
2. **Zelfcheck:** een aantal vragen waarmee de student actief toetst of hij de stof
   beheerst (retrieval practice; actief ophalen beklijft beter dan herlezen). Bij
   elke vraag een korte, verwijzende antwoordsleutel ("zie ..."), geen voorgekauwd
   antwoord, zodat het ophaal-effect behouden blijft.
3. **Volgende stap:** niet alleen welke module volgt, maar waaróm die op deze volgt.
   Maak de overgang tussen de kwaliteitslagen zichtbaar; dit is de tegenhanger van
   de advance organizer in de kop en maakt de leerlijn expliciet als lijn. Voor de
   laatste module, die geen vervolg heeft, wordt dit een afsluitende vooruitblik:
   toepassing in de praktijk of een vervolgvak, of een terugblik op de hele leerlijn.

## Scope

Deze conventies gelden uitsluitend voor `teaching/`. Niet-teaching-werk in deze
repository (`core/`, `adapters/`) valt er bewust buiten en houdt zijn eigen,
generieke en vendor-neutrale conventies. `core/` blijft taal-agnostisch en
Engelstalig.

## Hoe de conventie geborgd is

De afspraak is dat elk teaching-werkitem het volgende als vast acceptatiecriterium
opneemt:

> Voldoet aan de conventies in `teaching/conventies.md`.

Daarmee kan de gate niet groen zonder dat eraan getoetst is, ongeacht hoe het werk
wordt uitgevoerd. De teaching-werkitem-template (`teaching/_werkitem-template.md`)
heeft dit criterium al ingevuld. Een bouwende rol leest dit document daarnaast in
als onderdeel van de geldende projectconventies, zodat het materiaal er meteen aan
voldoet in plaats van achteraf. De generieke rol vraagt al om de geldende
conventies; dit document vult die voor teaching-werk concreet in.

## Een nieuwe conventie toevoegen

Komt er een conventie bij die voor `teaching/` moet gelden, voeg haar dan hier toe.
Dit document is de plek waar de gelding wordt vastgelegd; de inhoud van de conventie
hoort in haar eigen document.
