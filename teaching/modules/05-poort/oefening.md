# Beslis over het verwijdervoorstel

## Inleiding

In module 4 heb je bevindingen gewogen. Hier neem je de mensrol op je en besluit
je over voorstel P1 hieronder. Het voorstel gaat over toepassing van bestaande
voorbeeldcode. Je oefent C4 vóór die toepassing; je geeft geen mergebesluit over
een nieuwe codewijziging.

**Duur:** circa 60 minuten.

**Nodig:** de voorkennis uit [module 4](../04-oordelen/index.md), Python met
`pytest`, en de repository met `teaching/cases/module5-verwijderen/`. Gebruik
{core}`contracts/gate-decision.md` (C4) en {core}`roles/human-gate.md`.

**Inleveren:** je C4-besluit op P1 en de beantwoorde verantwoordingsvragen.

## Voorbereiding: controleer het gedrag

1. Open de [voorbeeldcode](https://github.com/misja/agent-role-loop/blob/main/teaching/cases/module5-verwijderen/boekenplank.py) en de [tests](https://github.com/misja/agent-role-loop/blob/main/teaching/cases/module5-verwijderen/test_boekenplank.py).
2. Voer vanuit de root van de repository uit:

   ```bash
   cd teaching/cases/module5-verwijderen
   python -m pytest
   ```

3. Lees `test_verwijderen_wist_ook_een_openstaande_wachtlijst`. Wijs aan welk boek is uitgeleend, wie op de wachtlijst staat en wat de assert na verwijderen controleert.
4. Vergelijk die controle met `verwijderen`, `boek` en `lijst`. Leg vast hoe het boek uit de boekenplank verdwijnt en welke publieke herstelmethode ontbreekt.

De verwachte uitkomst is drie geslaagde tests. De genoemde test controleert dat
alleen het andere boek in de lijst staat; hij bewijst niet dat alle verwijzingen
naar het verwijderde object zijn vernietigd. De beschrijvingen in de README,
docstrings en testnaam spreken van definitief wissen. Gebruik het daadwerkelijk
gecontroleerde gedrag als bewijs voor je besluit. De code bewaart de toestand
in het geheugen en bevat geen gedeelde of permanente opslag.

## Voorstel P1 voor deze oefening

P1 is een geconstrueerd voorstel, geen aanvraag om echte bibliotheekgegevens te
verwijderen. De boekenplank zal in een oefenscenario worden gebruikt door mensen
met openstaande reserveringen. Voor hen telt het behoud van hun reservering.
De gedeelde gebruikssituatie is scenario-invoer; de aangeleverde code implementeert
die omgeving niet.

- **Scope:** de bestaande operatie `verwijderen(nummer)` beschikbaar stellen om boeken uit de boekenplank te halen, ook wanneer ze uitgeleend zijn of een wachtlijst hebben. Besluit vóór die toepassing over de voorwaarden; er is nog niets vrijgegeven.
- **Voorzien gevolg:** het boek, de lener en de wachtlijst zijn daarna niet meer via de boekenplank opvraagbaar. De publieke API biedt geen hersteloperatie.
- **Open risicokeuze:** is dat gevolg toegestaan bij openstaande reserveringen? Voor P1 is nog geen herstelvoorziening afgesproken. Wie het verlies mag aanvaarden en welke voorwaarden nodig zijn, moet de menselijke poort beslissen.
- **Grenzen:** geen bouw van gedeelde opslag of herstelcode in deze opdracht. PROCEED geldt uitsluitend voor het afgesproken oefenscenario en verleent geen toestemming voor toepassing op echte gegevens.

## Worked example: een voorwaarde stellen

Een mens kan op P1 **REVISE** kiezen met als reden dat verlies van de toegang tot
openstaande reserveringen in het scenario niet aanvaardbaar is zonder beschikbaar
herstel. Een concrete opdracht aan de planner is dan: “Pas P1 vóór toepassing aan
zodat vastligt welke gegevens bewaard blijven, hoe herstel kan plaatsvinden en
wie daarvoor verantwoordelijk is.” De poort stelt een grens; de planner werkt
een uitvoerbaar voorstel uit.

Alleen een bevestigingsvraag toevoegen beantwoordt die herstelvraag niet. Zij
kan iemand waarschuwen voor de gevolgen, maar geeft na uitvoering geen boek of
reservering terug. Of zo’n waarschuwing toch voldoende is, hangt af van de
risicokeuze die de mens verantwoordt. Onderbouw je eigen besluit vanuit P1 en de
waargenomen feiten.

## Opdracht: schrijf je C4-besluit

1. Noteer bij **Artifact and source**: “Voorstel P1, de versie op deze oefenpagina”, de gebruikte versie van deze repository en de bron van je menselijke besluit. Jij neemt in deze oefening zelf de mensrol op je. Verwijs naar de geldende {core}`loop.md` als procesbasis.
2. Kies bij **Decision** PROCEED, REVISE of STOP. Schrijf bij **Reason** één alinea die je keuze verbindt aan het doel, het aangetoonde gedrag en het aanvaardbare risico.
3. Vul de overige velden van C4 in. Bij REVISE geef je genummerde wijzigingen vóór toepassing, gericht aan de planner of bouwer en begrensd tot P1. Noteer welke risicokeuzen je hebt gemaakt en welke vragen je expliciet veilig kunt uitstellen. Gebruik `<none>` waar een veld niet van toepassing is.
4. Controleer of een volgende rol uit je besluit kan afleiden op welk voorstel het slaat, wat mag doorgaan en wat eerst moet. Je ontwerpt of bouwt geen hersteloplossing.

Het resultaat is een herkenbaar C4 met voorstelversie, menselijke bron, besluit,
reden en concrete voorwaarden waar nodig. Een PROCEED op P1 is een besluit vóór
toepassing in het oefenscenario. Als uit een vervolgvoorstel codewijzigingen
volgen, vragen die hun eigen opleveringsbewijs en geselecteerde onafhankelijke
beoordeling. De mens beslist daarna afzonderlijk over merge.

## Verantwoordingsvragen

Beantwoord schriftelijk:

1. Welke gevolgen heb je daadwerkelijk in code en tests vastgesteld? Welk risico heb je op basis van het scenario verwacht?
2. Welke informatie of voorwaarde moet volgens jouw besluit beschikbaar zijn vóór toepassing, en waarom?
3. Welke route past bij een kleine, omkeerbare wijziging met heldere criteria? Wat verandert er bij een nieuwe normkeuze of onomkeerbare gevolgen? Gebruik {core}`loop.md` voor je afweging.
4. Waarover beslist C4, en welke beoordeling en menselijke beslissing volgen als er later een codewijziging wordt opgeleverd?

## Variant zonder AI

Eén student presenteert P1 en de gecontroleerde feiten. De anderen nemen de
menselijke poort op zich en schrijven gezamenlijk het C4-besluit volgens dezelfde
stappen. Bespreek welke feiten het besluit dragen, welke gevolgen uit het
scenario volgen en wie verantwoordelijkheid voor de gekozen voorwaarden neemt.
