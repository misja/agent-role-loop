# Les 1 - Context rot

> **Status:** outline met leerdoelen. De volledige lesuitwerking (slides, timing per werkvorm, docentennotities) is vervolgwerk.

## Plaats in de leerlijn

Eerste les van de eenheid over werken met AI-agents in software engineering. Vereist voorkennis: studenten kunnen zelfstandig een middelgrote programmeeropdracht uitvoeren en hebben enige ervaring met een chatgebaseerde AI-assistent. Geen voorkennis over multi-agent-werkwijzen nodig; die bouwen we hier op.

De les hoort bij [oefening 1](oefening.md), die **vooraf** (deel A) en **erna** (deel B) gemaakt wordt.

## Leerdoelen

Na deze les kan de student:

1. **Uitleggen wat context rot is** - beschrijven hoe kwaliteit van AI-output verloopt naarmate één gesprek opdracht, verkenning, logs, mislukte pogingen en oude aannames opstapelt, en de symptomen herkennen (vergeten instructies, scope-verschuiving, zelfverzekerde brij).
2. **Beargumenteren wanneer een multi-agent-aanpak proportioneel is** - voor een gegeven werkitem onderbouwen of de volledige loop, een licht pad of helemaal geen loop passend is, met de S/M/L-heuristiek en de kosten (tijd, tokens, aandacht) als argumenten.

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
- Toetsing: in deze fase alleen formatief, via de reflectievragen van oefening 1. Summatieve toetsing is een placeholder (`_toetsing/`).

## Bronnen

- Andrew "Watts" Watkins, [Context isolation in coding agent loops](https://depot.dev/blog/context-isolation-in-coding-agent-loops) (depot.dev, mei 2026) - de oorspronkelijke beschrijving van de loop en de term context rot zoals hier gebruikt.
- Anthropic, [How we built our multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system) (2025) - waarom parallellisatie alleen bij echt onafhankelijke deeltaken loont.
- De repository zelf: {core}`principles.md` en {core}`loop.md` zijn de normatieve teksten waar deze les didactisch op leunt.
