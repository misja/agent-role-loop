# Sta aan de poort

In module 4 oordeelde je over de kwaliteit van een change. Nu sta je aan de poort. Een door AI gebouwde `verwijderen`-operatie staat klaar om door te gaan. De code werkt, de tests slagen. Jij beslist: mag dit zo door?

Let op het verschil met module 4. Je beoordeelt hier niet de kwaliteit van de code en je herontwerpt de operatie niet. De poort-vraag is smaller en zwaarder: mag deze onomkeerbare operatie door, zo niet wat eerst, en waarom is dat een menselijke beslissing?

**Duur:** circa 60 minuten.
**Nodig:** het materiaal in `teaching/cases/module5-verwijderen/` uit de repository, met `pytest`. Het contract {core}`contracts/gate-decision.md` (C4) en de rol {core}`roles/human-gate.md`.
**Inleveren:** je poort-beslissing (C4) en de beantwoorde verantwoordingsvragen.

## Worked example: de poort op verwijderen

Draai eerst de tests:

```
pytest
```

Alles slaagt. De machine bevestigt dat `verwijderen` doet wat er staat: het haalt een boek van de plank, ook een boek met een openstaande wachtlijst. Dat is precies waar de machine ophoudt en de poort begint.

De poort-beslissing gaat niet over of de code klopt, maar over of dit zo mag doorgaan. `verwijderen` is onomkeerbaar: geen bevestiging, geen archief, en de reservering van een lener verdwijnt zonder waarschuwing. Een verkeerde go is hier niet terug te draaien. Een verdedigbare uitkomst is **no-go met een voorwaarde**: eerst een bevestiging of een soft-delete voordat dit op gedeelde data losgaat. Een andere is een **conditionele go** voor een omgeving zonder echte lezers. Wat de poort niet mag doen, is de vraag aan de machine overlaten: die kan bevestigen dat het werkt, niet of het verlies aanvaardbaar is.

Merk op waarom dit bij de mens ligt: de aanvaardbaarheid van onomkeerbaar dataverlies is geen eigenschap van de code, maar een oordeel over waarde en context.

## Jouw opdracht: vel de poort-beslissing

Schrijf een poort-beslissing (C4, volg {core}`contracts/gate-decision.md`) over de `verwijderen`-operatie:

1. **PROCEED, REVISE of STOP.** Kies, en maak de keuze expliciet.
2. Bij REVISE of STOP: benoem **wat eerst moet** voordat dit door mag, zonder de code te herontwerpen. Je stelt een voorwaarde, je bouwt niet.
3. **Verantwoord waarom dit een menselijke beslissing is** en niet aan de machine of de beoordelaars kan worden overgelaten.
4. **Weeg proportionaliteit:** zou je oordeel anders zijn voor een kleine, omkeerbare wijziging? Waarom?

## Verantwoordingsvragen

Beantwoord schriftelijk:

1. **Beargumenteer** het verschil tussen "de operatie werkt" en "de operatie mag door". Wie stelt het eerste vast, wie het tweede?
2. **Verantwoord** waarom onomkeerbaarheid de poort-beslissing zwaarder maakt dan een oordeel over code-kwaliteit.
3. **Weeg af** wanneer een menselijke poort onevenredig is, en wat het kost als je hem overslaat waar hij wel nodig was.

## Variant zonder AI

Speel de poort met een groep: één student presenteert de verwijder-operatie als klaar om door te gaan, de anderen zijn de poort en vellen een gezamenlijke go/no-go met een expliciete verantwoording. De debriefing draait om waar de beslissing bij de mens lag en waarom.
