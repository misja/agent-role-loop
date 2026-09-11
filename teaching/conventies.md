---
orphan: true
---

# Projectconventies voor het onderwijsmateriaal

Dit document wijst de geldende afspraken voor het onderwijsmateriaal aan.
De doelgroep en schrijfregels staan in eigen documenten; het modulestramien
staat hieronder. Werkitems verwijzen naar deze grondslag en beschrijven alleen
hun eigen toepassing of een expliciet te besluiten afwijking.

## Welke conventies gelden

Voor al het werk onder `teaching/` gelden:

- [doelgroep en voorkennis](doelgroep.md) voor wat de lezer al kent en wat
  eerst moet worden uitgelegd;
- de [schrijfwijzer](schrijfwijzer.md) voor uitlegtempo, register, claims en
  opmaak;
- de [begrippenlijst](begrippen.md) voor de vaste termen;
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

Deze afspraken gelden voor alle onderwijsteksten onder `teaching/`, inclusief
docentmateriaal en toetsmateriaal. Het modulestramien geldt voor modules, niet
voor iedere losse pagina.

Ook uitleg buiten `teaching/` die expliciet voor studenten is bedoeld, volgt het
doelgroepbeeld en de regels voor uitleg en onderbouwde claims. Het werkitem noemt
die passages. Voor Nederlandstalige uitleg gelden bovendien de Nederlandse
taal- en opmaakafspraken. Engelstalige technische documentatie wordt niet naar
het Nederlands omgezet; generieke rolprompts, contracten en API-voorbeelden in
`core/` en `adapters/` krijgen geen onderwijsstramien opgelegd. Bepalend is het
doel van de passage, niet alleen de directory waarin zij staat.

## Hoe de conventie geborgd is

De afspraak is dat elk teaching-werkitem het volgende als vast acceptatiecriterium
opneemt:

> Voldoet aan de conventies in `teaching/conventies.md`.

Het [werkitemsjabloon](https://github.com/misja/agent-role-loop/blob/main/teaching/_werkitem-template.md) bevat deze verwijzing. Omdat het
sjabloon niet wordt gepubliceerd, staat het als bestand in de repository.
De verwijzing alleen bewijst geen naleving; ook een geslaagde docs-build kan
geen begripstoets vervangen.

Gebruik binnen de gekozen route de volgende projectgebonden verantwoordelijkheden.
Dit zijn aanvullingen op de invoer en uitvoer van bestaande rollen, geen extra
agents of processtappen:

| Verantwoordelijkheid | Wat wordt vastgelegd of gecontroleerd? |
|---|---|
| Orkestratie | Noteer bij de start de normversie (commit), relevante normsecties en eventuele menselijke afwijkingsbesluiten op het issue. Geef diezelfde basis leesbaar mee aan elke betrokken rol. |
| Ontwerp | Benoem benodigde voorkennis, nieuwe begrippen en de vindplaatsen van eerdere uitleg. Wijs aan waar een ontbrekende stap wordt uitgelegd en welke passages de beoordelaar moet toetsen. |
| Uitvoering | Lees de aangewezen normen en werk de uitleg uit. Vermeld bij overdracht de gewijzigde passages, relevante uitlegkeuzes en bekende beperkingen. Kopieer geen volledige normteksten in het werkitem. |
| Onafhankelijke beoordeling | Lees de gewijzigde passages tegen dezelfde normversie. Benoem concrete begripsprongen, ontbrekende redeneerstappen en ongefundeerde claims, of leg met passages vast hoe die eisen zijn afgedekt. Laat zien wat de lezer uit de tekst kan afleiden. |

Een beoordelaar ontvangt de relevante normen en geldende besluiten, maar geen
maaktranscript. Hij kan de oorspronkelijke bronnen gericht raadplegen. Bij een
korte route blijven deze verantwoordelijkheden gelden voor zover de wijziging
ze raakt; maak geen lege ontwerpdocumenten voor een spellingcorrectie.

## Een nieuwe conventie toevoegen

Stel een wijziging voor op GitHub, met aanleiding, concrete normtekst, getroffen
materiaal en beoogde invoering. De mens beslist over de wijziging. Leg dat besluit
vast op het issue en verwerk de norm op haar aangewezen plek; deze pagina wijst
nieuwe normdocumenten aan. Noteer bewijs en gevolgen in `onderzoek/` wanneer een
structurele bevinding aanleiding gaf tot de wijziging.

Nieuwe werkitems gebruiken bij de start de dan geldende normcommit. Een norm die
nog in een PR staat, is niet door de aanwezigheid van die PR al ingevoerd.
Een lopend werkitem behoudt zijn geregistreerde normbasis. Moet een nieuwe afspraak
ook daar gelden, leg dan eerst een menselijk besluit vast met de nieuwe basis,
geraakte criteria en gevolgen voor al uitgevoerd werk. Een beoordelaar verandert de
beoordelingsbasis niet onderweg. Een bestaand expliciet besluit hoeft niet nogmaals
te worden gevraagd; neem het met zijn bron in de overdracht op.
