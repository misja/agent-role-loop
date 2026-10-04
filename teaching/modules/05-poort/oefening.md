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

## Worked example: bron, voorwaarde en uitstel

De [begeleide uitvoering uit module 1](../01-ervaren/eerste-uitvoering.md)
toont het vastleggen van C4 bij een plan. Hier leer je de risicokeuze voor P1
registreren. Onderstaand fragment is een geconstrueerd registratievoorbeeld,
geen werkelijk genomen mensbesluit of toestemming voor jouw uitvoering.

```text
Artifact and source:
Voorstel P1, versie op repositorycommit
b6ddcd55fbb9de37db316a626d0ddee4afe703e9, in
teaching/modules/05-poort/oefening.md.
Procesbasis: core/loop.md op dezelfde commit.
Menselijke bron: student Sam, logboek sam-module5.md, besluit 1,
na het lezen van P1 en mijn controle-uitvoer.

Decision: REVISE.
Reason: Ik aanvaard in dit oefenscenario geen verlies van toegang tot
openstaande reserveringen zonder beschikbaar herstel. De publieke API
biedt dat herstel nu niet. Daarom geef ik toepassing van P1 niet vrij.

Required changes before build:
1. Planner: werk alleen P1 bij. Leg vóór toepassing vast welke gegevens
   bewaard blijven, hoe terugzetten mogelijk is en wie verantwoordelijk is.
   Leg het aangepaste voorstel opnieuw aan mij voor; voer P1 nog niet uit.
   Herstelstand: geen eerdere automatische ronde in dit voorbeeld;
   ontwerp 0, oplevering 0. Dit is menselijke revisie van dit voorstel.

Human decisions made:
Verlies van toegang tot openstaande reserveringen is hier zonder herstel
niet aanvaardbaar. Geen toepassing op echte gegevens toegestaan.

Open questions still deferred:
De exacte formulering van een bevestigingsmelding mag nu wachten:
REVISE geeft geen uitvoering vrij en eerst moet het herstelvoorstel
worden beoordeeld. Controleer deze vraag opnieuw vóór eventuele toepassing.
```

Sam en `sam-module5.md` zijn fictieve voorbeeldwaarden, geen beschikbare
besluitbron. De genoemde commit bevat de hier beoordeelde P1-tekst. Bij je eigen C4 neem jij de
mensrol op je en geef je jouw naam of identificatie, logboekvindplaats,
besluitnummer en werkelijk gelezen repositorycommit mee. Een andere rol moet
het besluit en het voorstel kunnen terugvinden; een niet-ingevulde verwijzing
naar “mijn logboek” volstaat dan niet.

In dit voorbeeld is herstel een noodzakelijke voorwaarde: zonder uitgewerkt
herstelvoorstel wordt P1 niet toegepast. De bevestigingstekst kan voor deze
huidige stap wachten omdat er nog niets wordt uitgevoerd. Een bevestiging
kan iemand waarschuwen, maar brengt na verwijdering geen boek of reservering
terug. De planner mag de herstelvoorwaarde dus niet door alleen een melding
vervangen. Onderbouw je eigen besluit vanuit P1 en je waargenomen feiten;
je hoeft dit voorbeeldbesluit niet over te nemen.

## Opdracht: schrijf je C4-besluit

Gebruik {core}`contracts/gate-decision.md` voor onderstaande invulstappen.
Bewaar het besluit als één artefact in je logboek, met versie en leesbare bron.

1. **Leg voorstel en bron vast:** vul Artifact and source in met P1 op deze
   oefenpagina, de werkelijk gebruikte repositorycommit en procesversie.
   Noteer jouw menselijke besluitbron met identiteit en logboekvindplaats.
   Jij neemt in deze oefening zelf de mensrol op je.
2. **Kies en motiveer:** vul Decision in met PROCEED, REVISE of STOP. Verbind
   bij Reason je keuze aan het doel, gecontroleerde gedrag en aanvaardbare risico.
3. **Leg je risicokeuzen vast:** vul Human decisions made in met de voorwaarden
   waaronder je het gevolg aanvaardt. Onderscheid feiten uit de code van gevolgen
   die bij het scenario horen; vul ontbrekend herstelbewijs niet zelf in.
4. **Geef noodzakelijke wijzigingen door:** bij REVISE nummer je de wijzigingen
   onder Required changes before build en adresseer je planner of bouwer.
   Begrens het vervolg tot P1, noteer de herstelstand en wat nog niet mag worden
   uitgevoerd. Gebruik `<none>` wanneer dit veld niet van toepassing is.
5. **Motiveer eventueel uitstel:** vul Open questions still deferred in met
   de vraag, waarom uitstel veilig is voor de huidige stap en wanneer zij weer
   beoordeeld moet worden. Gebruik `<none>` als er geen veilig uitgestelde vraag is.
6. **Controleer de overdracht:** kan de volgende rol het voorstel en besluit
   openen en aanwijzen wat mag doorgaan en wat eerst moet? Bewaar die verwijzingen
   bij je C4. Je ontwerpt of bouwt in deze opdracht geen hersteloplossing.

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
