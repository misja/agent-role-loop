# Worked example: een groene boekenplank die niets bewijst

Dit voorbeeld hoort bij module 3 (De machine vertrouwen en wantrouwen).
Het is een minimale boekenplank met een testsuite die groen is en 100%
regeldekking haalt. En toch zit er een echt defect in.

## Draaien

Je hebt `pytest` en `pytest-cov` nodig.

```
pytest --cov=boekenplank --cov-report=term-missing
```

Je ziet: alle tests slagen, en de dekking is 100%. Geen enkele regel ontbreekt.

## De opdracht

De machine zegt: groen, volledig gedekt. Toch doet de code iets fout dat een
gebruiker zou opvallen. Zoek het defect, en let vooral op wat de tests
*beweren* te toetsen tegenover wat ze werkelijk controleren.

De uitwerking, de verantwoordingsvragen en de eigen opdracht staan in
oefening 3 van module 3.
