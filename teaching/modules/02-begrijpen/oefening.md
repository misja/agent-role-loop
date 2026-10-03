# Verantwoord de loop als ontwerp

Gebruik je overdrachtslogboek uit oefening 1 om te onderzoeken welke informatie
iedere rol kreeg en hoe de verantwoordelijkheden waren verdeeld. Onderbouw je
analyse met de vastgelegde overdrachten. Ook als je geen voordeel van de
structuur hebt waargenomen, kun je onderzoeken hoe zij was ingericht.

**Duur:** circa 60 minuten.
**Nodig:** je overdrachtslogboek uit oefening 1, deel B, de bijbehorende contractdefinities en rolprompts.
**Inleveren:** twee overdrachtsanalyses en de beantwoorde verantwoordingsvragen.

## Worked example: één overdracht ontleed

De planner geeft C2-P1 aan de menselijke poort. Dit voorbeeld uit
[de ingevulde boekenplankoverdrachten](../../praktijk/overdrachten.md) laat zien
hoe je die overdracht kunt analyseren.

| Onderdeel | Wat je in dit voorbeeld kunt aanwijzen |
|---|---|
| Concrete eis | Een filter op beschikbare boeken behoudt de registratie van alle boeken. |
| Voorgenomen wijziging | `lijst(alleen_beschikbaar=False)` houdt het bestaande gedrag; met `True` wordt de teruggegeven lijst gefilterd. |
| Verificatieplan | Vergelijk het volledige overzicht vóór en na een gefilterde aanroep. Controleer ook welke boeken het filter teruggeeft. |
| Beperking | Het plan beschrijft een controle. Pas de uitvoering daarvan levert testbewijs; de gekozen voorbeelden dekken niet vanzelf alle situaties. |

De definitie van {core}`contracts/build-packet.md` is de **interface**: zij legt
vast welke informatie een plan moet bevatten. C2-P1 is het ingevulde artefact
voor deze taak. De planner-rolprompt geeft instructies om zo'n plan te maken en
vervult in de analogie de functie van **implementatie**. De feitelijke
verkenning en gekozen gereedschappen zijn de uitvoering van die instructies.

Het maakgesprek blijft **verborgen** voor de menselijke poort. De eisen,
relevante risico's en bronverwijzingen blijven beschikbaar. De poort kan zo de
voorgestelde wijziging onderzoeken zonder iedere verworpen poging te lezen.
Een onjuiste aanname die in C2-P1 terechtkomt, kan het besluit nog steeds
beïnvloeden. Het resultaat van het besluit staat apart in C4-P1; dat besluit
moet de bouwer vervolgens samen met de goedgekeurde planversie ontvangen.

## Jouw opdracht: analyseer twee andere overdrachten

1. Kies twee andere overdrachten uit je logboek, bijvoorbeeld van bouwer naar beoordelaar of van beoordelaar naar hoofdbeoordelaar. Noteer de bron en versie.
2. Wijs per overdracht de contractdefinitie en het ingevulde artefact aan. Welke vereiste informatie staat erin? Welke relevante informatie ontbreekt eventueel?
3. Benoem de rolprompt en de taak van de uitvoerende rol. Onderscheid de instructies van wat de rol in jouw uitvoering daadwerkelijk deed.
4. Noteer welke context buiten de overdracht bleef. Welke eisen, normen en besluiten waren wel toegankelijk? Beschrijf een risico van extra voorgeschiedenis en een risico van te weinig informatie.

Je analyse is compleet als een andere lezer deze onderdelen in beide
bronoverdrachten kan terugvinden. Markeer ontbrekende gegevens als ontbrekend;
vul ze niet achteraf in alsof ze destijds beschikbaar waren.

## Verantwoordingsvragen

Beantwoord schriftelijk, met voorbeelden uit je logboek:

1. **Beargumenteer** hoe de loop verantwoordelijkheden verdeelde. Welke rol droeg welke zorg? Welk risico ontstaat als één rol zowel bouwt als haar eigen werk beoordeelt?
2. Welk contract gebruikte je als **vastgelegde conventie**? **Verantwoord** wat de vaste vorm opleverde en welke invul- of leeslast zij gaf. Benoem het ook als je geen aantoonbaar voordeel zag.
3. Eén contract leek je in oefening 1 misschien te zwaar. **Weeg af** of je dat bij een groter of risicovoller werkitem nog steeds zou vinden. Gebruik de conventionele kwaliteitslaag uit het raamwerk.
4. Stel dat je één rol moest weghalen. **Beargumenteer** welke verantwoordelijkheid je het laatst zou opgeven en welke informatie je daarvoor nodig hebt.

## Variant zonder AI

Gebruik bij de rollenspelvariant het gezamenlijke overdrachtslogboek. Noteer
welke toelichting deelnemers buiten de artefacten wilden geven en of die
informatie nodig was voor de volgende rol. Als zulke toelichting niet voorkwam,
onderzoek dan welke informatie de schriftelijke overdrachten zelf bevatten.
