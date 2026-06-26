# Les 2 - Begrijpen: de loop als scheiding van verantwoordelijkheden

> **Status:** outline met leeruitkomsten. De volledige lesuitwerking (slides, timing per werkvorm, docentennotities) is vervolgwerk.

## Plaats in de leerlijn

Tweede module van de leerlijn. In module 1 heb je context rot aan den lijve ervaren en heb je de rollenloop één keer gedraaid (oefening 1, deel B). Je weet nu hoe het voelt en *dát* structuur helpt. Deze les gaat over het waarom: waarom werkt die structuur, en welk ontwerpprincipe dat je al kent zit eronder? Vereiste voorkennis: module 1 afgerond, inclusief het overdrachtslogboek uit oefening 1.

De les hoort bij [oefening 2](oefening.md), waarin je dit begrip toepast op je eigen overdrachtslogboek.

## Leeruitkomsten

Na deze les kan de student:

1. **Beargumenteren dat de rollenloop scheiding van verantwoordelijkheden op een werkproces is** - uitleggen dat elke rol één zorg draagt, net zoals je een softwaresysteem in onderdelen met elk één verantwoordelijkheid opdeelt, en verantwoorden waarom dat de kwaliteit ten goede komt.
2. **In een concrete overdracht de interface, de implementatie en het verborgene aanwijzen** - in een gegeven handoff benoemen wat het contract (de interface) vastlegt, wat de rolprompt (de implementatie) daarachter doet, en welke context bewust verborgen blijft, en verantwoorden hoe dat verbergen context rot tegengaat.
3. **Verantwoorden dat een contract een vastgelegde conventie is** - uitleggen waar contracten passen in de conventionele kwaliteitslaag van het kwaliteitsraamwerk, en afwegen wat een afspraak die je niet per taak heronderhandelt oplevert en wat ze kost.

## Opbouw

### Van ervaren naar begrijpen

Korte terugblik op module 1: in deel A liep één lange chat vol en verrotte de kwaliteit; in deel B, met de loop, gebeurde dat niet. De vraag van deze les is wat de loop precies deed, en waarom dat geen toeval is maar een toepassing van iets wat je in software al kent.

### Scheiding van verantwoordelijkheden, nu op een werkproces

In code deel je een systeem op in onderdelen die elk één ding doen: scheiding van verantwoordelijkheden. De rollenloop doet hetzelfde, maar dan met een werkproces in plaats van met code. Triage weegt proportionaliteit, de planner plant, de bouwer bouwt, elke beoordelaar kijkt vanuit één invalshoek, de poort velt het menselijke oordeel. Geen enkele rol draagt alles; elke rol draagt één zorg. Dat is dezelfde gedachte, op een ander niveau toegepast.

### Contracten als interface, rolprompts als implementatie

Tussen twee rollen gaat precies één ding heen: een contract. Dat contract is de interface. Het legt vast wat een overdracht moet bevatten, niet hoe de rol tot dat resultaat kwam. De rolprompt erachter is de implementatie: je kunt hem herschrijven, vervangen door een ander model of laten uitvoeren door een mens, zonder dat de rest van de loop het merkt, zolang het contract blijft staan.

En wat niet in het contract staat, blijft verborgen. De bouwer ziet het verkenningsverslag van de planner niet; een beoordelaar ziet het oordeel van een andere beoordelaar niet. Dat verbergen is geen slordigheid maar precies de tegenmaatregel tegen de context rot die je in module 1 voelde: niemand sleept de hele geschiedenis mee, dus niets weegt mee dat allang niet meer klopt.

### Een contract is een vastgelegde conventie

Hiermee raakt de loop aan softwarekwaliteit. In het raamwerk [Kwaliteit als gedeelde verantwoordelijkheid](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md) is de tweede soort kwaliteitsmechanisme de conventionele: afspraken die je vastlegt en niet per taak opnieuw maakt. Een contract is precies zo'n vastgelegde conventie. Het bepaalt één keer wat een overdracht moet bevatten, zodat niemand dat per keer hoeft te heronderhandelen. Standaarden bestaan om denkruimte vrij te maken, en een contract doet dat voor de overdracht tussen rollen.

## Werkvormen en toetsing

- Werkvormen: korte instructie, gezamenlijke analyse van één voorbeeldoverdracht, daarna zelf toepassen in oefening 2.
- Toetsing: in deze fase formatief, via de verantwoordingsvragen van oefening 2.

## Bronnen

- De repository zelf: {core}`principles.md` (vooral het tweede principe, expliciete overdrachten) en {core}`loop.md` zijn de normatieve teksten onder deze les.
- Het raamwerk [Kwaliteit als gedeelde verantwoordelijkheid](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md), sectie "2. Conventioneel en vastgelegd".
