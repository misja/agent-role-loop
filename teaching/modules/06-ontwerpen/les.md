# De synthese: het kader in eigen hand

> **Status:** outline met leeruitkomsten. De volledige lesuitwerking (slides, timing per werkvorm, docentennotities) is vervolgwerk.

## Plaats in de leerlijn

Laatste module. Tot nu toe kreeg je het kader aangereikt: je ervoer het probleem (module 1), begreep de loop (module 2), zette de machinepoorten in (module 3), oordeelde (module 4) en stond aan de poort (module 5). Nu draait het om: jij ontwerpt, en het kader is van jou. Vereiste voorkennis: modules 1 tot en met 5 afgerond.

De les hoort bij [oefening 6](oefening.md), een mini-project waarin je een interface-uitbreiding ontwerpt, de AI regisseert en de hele keten verantwoordt.

## Leeruitkomsten

De leeruitkomsten staan als "Wat ga je leren" op de [module-index](index.md).

## Opbouw

### Van bouwer naar regisseur

In de vorige modules bouwde de AI en beoordeelde jij. In deze module verschuift je rol verder: je ontwerpt de opdracht, stelt de kaders, delegeert de bouw en verifieert het resultaat. Dat is geen bijrol maar het werk zelf: wie met AI-agents werkt, verschuift van zelf schrijven naar delegeren, superviseren en integreren. De waarde daarvan hangt af van hoe goed je de werkstroom rond delegatie en verificatie inricht, en dat inrichten is precies wat je hier oefent.

### De drie lagen in eigen hand

Het [kwaliteitsraamwerk](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md) beschreef drie soorten kwaliteitsmechanismen en hun levensloop: een oordeel wordt een vastgelegde conventie, en een conventie wordt een geautomatiseerde poort. In de eerdere modules doorliep je die lagen als gebruiker; nu doorloop je ze als ontwerper. Jij velt de oordelen (welke normen gelden hier), jij legt ze vast als conventies, jij automatiseert wat te automatiseren is, en jij houdt het oordeel waar het hoort: bij de beoordeling en de poort. De synthese is dat je de verdeling van verantwoordelijkheden niet meer aangereikt krijgt, maar zelf inricht en verantwoordt.

### Randvoorwaarden als ontwerpdaad

Voordat er gebouwd wordt, beslis je wat "goed" in jouw project betekent: welke stijl, welke type checker, welke linter, welke formatter, welk projectbeheer. Zijn die randvoorwaarden vaag, dan heronderhandelt elke bijdrage ze opnieuw en verzint de AI ze zelf, inconsistent. Zijn ze scherp, dan is de agent begrensd en zijn output beoordeelbaar. Er is geen objectief juiste set: het vaststellen is een oordeel, het vastleggen een conventie, het afdwingen een poort. Een voorbeeld van zo'n binding is de [conventiepagina](../../conventies.md) van dit lesmateriaal zelf: een kort document dat vastlegt welke afspraken gelden en waar ze staan.

### Werkwijze, medium en tool

Om je project te beheren moet je drie niveaus uit elkaar houden. De **werkwijze** is stabiel en tool-onafhankelijk: rollen, contracten, poorten. Het **medium** is waar een werkitem leeft: een Markdown-bestand, een issue-body, een kaartje. De **tool** beheert dat medium: een bestandssysteem met git, een projectbord, een tracker. Wie deze niveaus niet scheidt, denkt dat "leren werken met tool X" het doel is en raakt verlamd door de keuze; wie ze scheidt, ziet de tool als inwisselbare drager en kan wisselen zonder de werkwijze te verliezen.

De toolkeuze zelf is daarmee niet onverschillig, maar een verantwoorde afweging. Zeggenschap over data hoort daarin expliciet mee: waar staat je werk, onder welk rechtsregime, hoe afhankelijk word je van een leverancier, en wat kost migreren? Voor wie in Europese organisaties gaat werken is dat een levensechte professionele vraag, geen theorie. De waarborg die migratie beheersbaar houdt, ken je al uit module 2: houd de inhoud portabel en het koppelvlak klein, dan is een toolwissel een ingreep en geen breuk.

### Architectuur als zwaartepunt van het oordeel

De uitbreiding van dit mini-project is een interface op je bestaande boekenplank-logica, bijvoorbeeld een [Textual](https://textual.textualize.io/)-TUI. Studenten denken hier vaak "de AI lost dat wel op", en dat is geen bezwaar maar de kern: om te beoordelen of de AI het goed deed, moet je er iets van snappen. Het beoordelingszwaartepunt ligt bij architectuur en onderhoudbaarheid, met als concrete kernvraag: **hergebruikt de AI je bestaande logica-laag, of dupliceert hij haar in de interface?** Dat is scheiding van verantwoordelijkheden, die je in module 2 op een werkproces zag, nu op een systeem: de interface hoort een laag bovenop de logica te zijn, geen tweede exemplaar ervan. Duplicatie werkt vandaag en wreekt zich bij elke volgende wijziging.

De beoordeling rust daarbij op je verantwoording, niet op het artefact. Twee studenten met verschillende stacks en verschillende uitkomsten kunnen allebei uitstekend werk leveren; het verschil zit in wie zijn keuzes kan verantwoorden.

## Werkvormen en toetsing

- Werkvormen: korte instructie, daarna het mini-project van oefening 6 met tussentijdse besprekingen van de dossiers.
- Toetsing: in deze fase formatief, via het dossier en de verantwoordingsvragen van oefening 6. Summatieve toetsing is een placeholder (`_toetsing/`).

## Bronnen

- Het raamwerk [Kwaliteit als gedeelde verantwoordelijkheid](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md), de drie soorten en "De drie samen"; onder "Verder lezen" onderbouwt de Codex-analyse de rolverschuiving naar delegeren en superviseren.
- De repository zelf: {core}`loop.md` en {core}`principles.md` als de werkwijze die je nu zelf inricht, en {core}`contracts/work-item.md` voor het werkitem dat je gaat schrijven.
- De [projectconventies](../../conventies.md) van dit materiaal als voorbeeld van een vastgelegde binding.

## Afronding

### Wat heb je geleerd

Je hebt de keten in eigen hand genomen: een uitbreiding ontworpen en als werkitem vastgelegd, de randvoorwaarden van je project vastgesteld en verantwoord, werkwijze, medium en tool gescheiden en een toolkeuze onderbouwd, de AI binnen die kaders geregisseerd, en het resultaat beoordeeld met architectuur als zwaartepunt. De drie kwaliteitslagen zijn niet langer aangereikt kader maar jouw ontwerp.

### Zelfcheck

Beantwoord uit je hoofd; de sleutel wijst alleen waar je het kunt nakijken.

1. Beschrijf de levensloop van één norm in jouw project: welk oordeel werd een conventie, en welke conventie werd een poort? (zie "Randvoorwaarden als ontwerpdaad" en het raamwerk, "De drie samen")
2. Wat is het verschil tussen werkwijze, medium en tool, en waarom overleeft de werkwijze een toolwissel? (zie "Werkwijze, medium en tool")
3. Waaraan zie je of de AI je bestaande logica hergebruikt of dupliceert, en waarom is dat het zwaartepunt van het oordeel? (zie "Architectuur als zwaartepunt van het oordeel")
4. Welke beslissing bleef in jouw project bij jou, en waarom kon geen machine of beoordelaar die overnemen? (zie module 5, "De poort is menselijk")

### Afsluitende vooruitblik

Hier eindigt de leerlijn. Je hebt het probleem gevoeld (context rot), het principe begrepen (scheiding van verantwoordelijkheden met contracten als interface), de machine leren vertrouwen én wantrouwen, geoordeeld waar perspectieven botsen, aan de poort gestaan waar de mens onvervangbaar is, en ten slotte zelf ontworpen en verantwoord. Wat overdraagt is niet de tool en niet de casus, maar het vermogen om bij elk volgend project, elke volgende stack en elke tool die nu nog niet bestaat dezelfde vragen te stellen: wat betekent kwaliteit hier, wie draagt welke verantwoordelijkheid, wat leg ik vast, wat automatiseer ik, en welk oordeel houd ik bij mezelf. Dat is wat je meeneemt naar de praktijk en naar de afsluitende opdracht van je opleiding.
