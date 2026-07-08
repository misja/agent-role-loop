# De loop als scheiding van verantwoordelijkheden

## Plaats in de leerlijn

Tweede module van de leerlijn. In module 1 heb je context rot aan den lijve ervaren en heb je de rollenloop één keer gedraaid (oefening 1, deel B). Je weet nu hoe het voelt en *dát* structuur helpt. Deze les gaat over het waarom: waarom werkt die structuur, en welk ontwerpprincipe dat je al kent zit eronder? Vereiste voorkennis: module 1 afgerond, inclusief het overdrachtslogboek uit oefening 1.

De les hoort bij [oefening 2](oefening.md), waarin je dit begrip toepast op je eigen overdrachtslogboek.

## Leeruitkomsten

De leeruitkomsten staan als "Wat ga je leren" op de [module-index](index.md).

## Opbouw

### Van ervaren naar begrijpen

Korte terugblik op module 1: in deel A liep één lange chat vol en verrotte de kwaliteit; in deel B, met de loop, gebeurde dat niet. De vraag van deze les is wat de loop precies deed, en waarom dat geen toeval is maar een toepassing van iets wat je in software al kent.

### Scheiding van verantwoordelijkheden, nu op een werkproces

In code deel je een systeem op in onderdelen die elk één ding doen: scheiding van verantwoordelijkheden. De rollenloop doet hetzelfde, maar dan met een werkproces in plaats van met code. Triage weegt proportionaliteit, de planner plant, de bouwer bouwt, elke beoordelaar kijkt vanuit één invalshoek, de poort velt het menselijke oordeel. Geen enkele rol draagt alles; elke rol draagt één zorg. Dat is dezelfde gedachte, op een ander niveau toegepast.

```{mermaid}
:caption: De rollenloop. Elke rol draagt één zorg; tussen twee rollen gaat precies één contract heen (C0 tot en met C7). De beoordelaars werken parallel en zien elkaars oordeel niet.

flowchart TD
    W["Werkitem (C0)"] --> T[Triage]
    T -- C1 --> P[Planner]
    P -- C2 --> V[Verhelderaar]
    V -- C3 --> G[Menselijke poort]
    G -- C4 --> B[Bouwer]
    B -- C5 --> S
    subgraph S[Beoordelaars]
        direction LR
        R1[Strikt]
        R2[Pragmatisch]
        R3[Adversarieel]
        R4[Onderhoudbaarheid]
    end
    S -- "C6 (4x)" --> H[Hoofdbeoordelaar]
    H -- C7 --> E[Eindoordeel]
```

### Contracten als interface, rolprompts als implementatie

Tussen twee rollen gaat precies één ding heen: een contract. Dat contract is de interface. Het legt vast wat een overdracht moet bevatten, niet hoe de rol tot dat resultaat kwam. De rolprompt erachter is de implementatie: je kunt hem herschrijven, vervangen door een ander model of laten uitvoeren door een mens, zonder dat de rest van de loop het merkt, zolang het contract blijft staan.

Datzelfde geldt voor het medium waarin een contract leeft: een bestand op schijf, een issue-body op een projectbord of een kaartje op een muur zijn inwisselbare dragers, zolang de inhoud het contract draagt. De contracten van dit project leven inmiddels als issue-bodies op een projectbord, zonder dat de loop het merkt.

En wat niet in het contract staat, blijft verborgen. De bouwer ziet het verkenningsverslag van de planner niet; een beoordelaar ziet het oordeel van een andere beoordelaar niet. Dat verbergen is geen slordigheid maar precies de tegenmaatregel tegen de context rot die je in module 1 voelde: niemand sleept de hele geschiedenis mee, dus niets weegt mee dat allang niet meer klopt.

### Een contract is een vastgelegde conventie

Hiermee raakt de loop aan softwarekwaliteit. In het raamwerk [Kwaliteit als gedeelde verantwoordelijkheid](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md) is de tweede soort kwaliteitsmechanisme de conventionele: afspraken die je vastlegt en niet per taak opnieuw maakt. Een contract is precies zo'n vastgelegde conventie. Het bepaalt één keer wat een overdracht moet bevatten, zodat niemand dat per keer hoeft te heronderhandelen. Standaarden bestaan om denkruimte vrij te maken, en een contract doet dat voor de overdracht tussen rollen.

### Een echt werkitem als voorbeeld

Zo ziet een ingevuld werkitem ({core}`contracts/work-item.md`) eruit. Dit is een echt exemplaar uit de bouw van dit lesmateriaal: het werkitem dat de diagram-ondersteuning van deze site inschakelde. Het stroomdiagram hierboven rendert dankzij dit werkitem.

```md
# Schakel Mermaid-ondersteuning in

## Aanleiding

De schrijfwijzer wijst Mermaid aan als voorkeursvorm voor diagrammen, met een
expliciete technische voorwaarde: de ondersteuning vereist een extensie
(sphinxcontrib-mermaid) als dependency in pyproject.toml en een configuratie in
conf.py, en Mermaid mag pas in materiaal gebruikt worden nadat die ondersteuning
is ingeschakeld en de build er schoon mee is. Die voorwaarde bestond tot nu toe
alleen als kanttekening; dit werkitem materialiseert haar, omdat het
visualisatie-werkitem erop wacht.

## Gewenste uitkomst

Mermaid-diagrammen renderen in de site: sphinxcontrib-mermaid als dependency in
de docs-groep van pyproject.toml, extensie geconfigureerd in docs/conf.py, en
een rendercheck (een proefdiagram bouwt en toont correct, daarna weer verwijderd
of als eerste echt diagram benut).

## Acceptance criteria

1. sphinxcontrib-mermaid in de docs-dependency-groep; het lock-bestand is
   bijgewerkt.
2. Extensie in conf.py; de kale, portabele build blijft de volledige site
   produceren, ook in CI.
3. Docs-build schoon met een renderend Mermaid-diagram als bewijs.
4. Voldoet aan de conventies in teaching/conventies.md.

## Size guess

S
```

Merk op wat het contract afdwingt: een aanleiding (waarom bestaat dit werk), een gewenste uitkomst als waarneembaar resultaat, en toetsbare acceptatiecriteria. Wie dit werkitem oppakt, hoeft niets te heronderhandelen.

## Werkvormen en toetsing

- Werkvormen: korte instructie, gezamenlijke analyse van één voorbeeldoverdracht, daarna zelf toepassen in oefening 2.
- Toetsing: formatief, via de verantwoordingsvragen van oefening 2.

## Bronnen

- De repository zelf: {core}`principles.md` (vooral het tweede principe, expliciete overdrachten) en {core}`loop.md` zijn de normatieve teksten onder deze les.
- Het raamwerk [Kwaliteit als gedeelde verantwoordelijkheid](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md), sectie "2. Conventioneel en vastgelegd".

## Afronding

### Wat heb je geleerd

De rollenloop is scheiding van verantwoordelijkheden op een werkproces: elke rol draagt één zorg. Het contract tussen twee rollen is de interface (wat een overdracht moet bevatten), de rolprompt de implementatie (hoe de rol tot dat resultaat komt), en wat niet in het contract staat blijft bewust verborgen. Een contract is daarmee een vastgelegde conventie: één keer afgesproken, niet per taak heronderhandeld.

### Zelfcheck

Beantwoord uit je hoofd; de sleutel wijst alleen waar je het kunt nakijken.

1. Leg uit dat de rollenloop scheiding van verantwoordelijkheden is. Welke zorg draagt de bouwer, en welke de poort? (zie "Scheiding van verantwoordelijkheden, nu op een werkproces")
2. Wijs in een overdracht de interface, de implementatie en het verborgene aan. Waarom gaat dat verbergen context rot tegen? (zie "Contracten als interface, rolprompts als implementatie")
3. Waarom is een contract een vastgelegde conventie, en wat levert zo'n afspraak op? (zie "Een contract is een vastgelegde conventie")

### Volgende stap

Je begrijpt nu de conventionele laag: afspraken die mensen vastleggen. Module 3 (De machine vertrouwen en wantrouwen) gaat naar de geautomatiseerde laag: machines die objectief vaststellen of aan een afspraak is voldaan, met coverage, linters en CI. Dat is de levensloop van een norm zoals het kwaliteitsraamwerk die beschrijft: wat mensen vastleggen, dwingen machines af. De overgang maakt de kernvraag scherp: als de machine groen zegt, is het dan ook goed?
