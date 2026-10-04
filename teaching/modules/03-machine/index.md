# 3. De machine vertrouwen en wantrouwen

**Leerdoel:** Je verantwoordt hoe gekozen geautomatiseerde controles als toegangsvoorwaarde tot review werken. Groen is noodzakelijk voor de ingestelde verplichte controles; de uitslag bewijst geen algehele correctheid.

**Kwaliteitslaag:** Geautomatiseerd en deterministisch.

**Wat ga je leren**

Na deze module kun je:

1. **Verantwoorden waarom de gekozen geautomatiseerde controles vóór de review staan.** Je benoemt de plaats van coverage, linters, type-checkers, scans en CI in de loop. Je legt uit welke controle zij overnemen en welke beoordeling nodig blijft.
2. **De soorten geautomatiseerde poorten onderscheiden.** Je legt uit wat iedere soort controle vaststelt en verantwoordt waar haar grens ligt.
3. **Beargumenteren waarom groen geen algehele correctheid bewijst.** Je herkent een test met een te zwakke assertie en een coveragecontrole zonder ingestelde drempel. Je verantwoordt wat de uitslag in beide gevallen aantoont en waar een mens een norm moet kiezen of de bedoeling moet beoordelen.

Deze module bestaat uit de les en de bijbehorende oefening.

```{toctree}
:maxdepth: 1

les
oefening
```

## Praktijkvoorbeeld

Lees bij “Een groene controle, toch een blokkade” in
[Van werkitem naar pull request](../../praktijk/van-werkitem-naar-pull-request.md)
hoe een geslaagde controle samengaat met een beschadigde registratie.
Dat defect verschilt van de dubbele uitlening in deze module. Beide voorbeelden
laten zien waarom je moet nagaan welke eis een geslaagde controle daadwerkelijk
toetst.
