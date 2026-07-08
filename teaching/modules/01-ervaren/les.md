# Context rot

## Plaats in de leerlijn

Eerste les van de eenheid over werken met AI-agents in software engineering. Vereist voorkennis: studenten kunnen zelfstandig een middelgrote programmeeropdracht uitvoeren en hebben enige ervaring met een chatgebaseerde AI-assistent. Geen voorkennis over multi-agent-werkwijzen nodig; die bouwen we hier op.

De les hoort bij [oefening 1](oefening.md), die **vooraf** (deel A) en **erna** (deel B) gemaakt wordt.

## Leeruitkomsten

De leeruitkomsten staan als "Wat ga je leren" op de [module-index](index.md).

Het conceptuele verband met scheiding van verantwoordelijkheden en interfaces komt bewust pas in module 2: eerst ervaren dat de loop helpt, dan begrijpen waarom.

## Opbouw (probleem, dan principe, dan tooling)

De volgorde is een bewuste ontwerpbeslissing van dit materiaal: wie eerst tooling krijgt, leert een recept; wie eerst het probleem voelt, begrijpt waarom het recept werkt.

### Deel A - Het probleem (terugblik op oefening 1, deel A)

- Studenten brengen hun logboek mee: waar ging de lange chat mis?
- Inventarisatie op het bord, clusteren naar de drie symptoomgroepen: vergeten instructies, scope-verschuiving, zelfverzekerde brij.
- Kernvraag aan de groep: *waarom* gebeurt dit? Werk toe naar: alles staat in één context, en alles weegt mee, ook wat allang niet meer waar of relevant is.

### Deel B - De loop als antwoord

- Context rot benoemen en definiëren; de term komt uit de bronartikelen hieronder.
- De rollenloop introduceren als één mogelijke uitwerking: triage, planner, verhelderaar, menselijke poort, bouwer, vier beoordelaars, hoofdbeoordelaar - met de contracten C0 t/m C7 als de enige dingen die rolgrenzen passeren. Hier blijft het bij wát de loop is en hoe je hem draait; waaróm die opzet werkt, is de stof van module 2.
- Expliciet stilstaan bij de twee asymmetrieën: beoordelaars draaien parallel en geïsoleerd, en de poort is principieel menselijk.
- Proportionaliteit: de loop loont voor S/M/L-werk en is te zwaar of ontoereikend daarbuiten; triage is daarom zelf een rol.

### Deel C - De tooling (doorkijk naar oefening 1, deel B)

- Demonstratie van de manual adapter: verse chatvensters, alleen artefacten kopiëren, het overdrachtslogboek.
- Nadrukkelijk gepositioneerd als één van meerdere adapters: het principe is de leerstof, de tooling is inwisselbaar.
- Instructie voor deel B van de oefening.

## Werkvormen en toetsing

- Werkvormen: logboekbespreking in tweetallen, plenaire clustering, instructie, demonstratie.
- Toetsing: formatief, via de reflectievragen van oefening 1.

## Bronnen

- Andrew "Watts" Watkins, [Context isolation in coding agent loops](https://depot.dev/blog/context-isolation-in-coding-agent-loops) (depot.dev, mei 2026) - de oorspronkelijke beschrijving van de loop en de term context rot zoals hier gebruikt.
- Anthropic, [How we built our multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system) (2025) - waarom parallellisatie alleen bij echt onafhankelijke deeltaken loont.
- De repository zelf: {core}`principles.md` en {core}`loop.md` zijn de normatieve teksten waar deze les didactisch op leunt.

## Afronding

### Wat heb je geleerd

Je hebt context rot aan den lijve ervaren: in één lange chat stapelt alles op en verrot de kwaliteit, terwijl de rollenloop dat tegenhoudt door elke rol een verse, afgebakende context te geven. En je hebt geoefend met proportionaliteit: niet elke taak verdient de volledige loop.

### Zelfcheck

Beantwoord uit je hoofd; de sleutel wijst alleen waar je het kunt nakijken.

1. Wat is context rot, en aan welke drie symptomen herken je het? (zie deel A en oefening 1, deel A)
2. Waarom verrot de kwaliteit juist in één lang, ongestructureerd gesprek? (zie deel A, de kernvraag)
3. Wanneer is de volledige loop proportioneel en wanneer niet? Noem een taak waarvoor je hem niet zou inzetten. (zie deel B, proportionaliteit)

### Volgende stap

In deze module heb je gevóéld dat structuur helpt, maar nog niet waaróm. Module 2 (Begrijpen) legt dat uit: de loop als scheiding van verantwoordelijkheden, met contracten als interface. Daarmee stap je van het probleem (nog geen kwaliteitslaag) naar de conventionele laag van het kwaliteitsraamwerk, waarin een contract een vastgelegde conventie is.
