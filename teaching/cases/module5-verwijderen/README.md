# Handoff naar de poort: een onomkeerbare operatie

Dit voorbeeld hoort bij module 5 (De menselijke poort). Het is een door AI
gebouwde uitbreiding van de boekenplank: `verwijderen`. De code werkt en de tests
slagen.

Je beoordeelt in deze module niet de kwaliteit van de code. Je staat aan de
poort: de operatie staat klaar om door te gaan, en jij beslist go of no-go.

## Wat is gebouwd

- `verwijderen <nummer>` haalt een boek definitief van de plank.
- De operatie is onomkeerbaar: er is geen bevestiging, geen archief, geen
  ongedaan maken.
- Een boek met een openstaande wachtlijst wordt zonder waarschuwing gewist; de
  reserveringen zijn dan weg.

## Draaien

Je hebt `pytest` nodig.

```
pytest
```

Alle tests slagen. De machine kan bevestigen dat `verwijderen` doet wat er staat.
Ze kan niet beslissen of dit zo mag. Dat is de poort-vraag, en die staat in
oefening 5.
