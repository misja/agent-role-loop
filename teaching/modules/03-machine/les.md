# Les 3 - De machine vertrouwen en wantrouwen

> **Status:** outline met leeruitkomsten. De volledige lesuitwerking (slides, timing per werkvorm, docentennotities) is vervolgwerk.

## Plaats in de leerlijn

Derde module van de leerlijn. In module 2 heb je de loop begrepen als scheiding van verantwoordelijkheden, met contracten als interface. Een van die contracten is de overdracht van de bouwer naar de beoordelaars. Deze les gaat over wat er vóór die overdracht moet kloppen: de geautomatiseerde poorten die een machine objectief vaststelt. Vereiste voorkennis: module 2 afgerond, en het kwaliteitsraamwerk, soort 1.

De les hoort bij [oefening 3](oefening.md), waarin je aan een groene boekenplank ontdekt dat volledige dekking en een fout samen kunnen gaan.

## Leeruitkomsten

Na deze les kan de student:

1. **Beargumenteren dat de geautomatiseerde poorten een toegangsvoorwaarde tot de review zijn, niet de review zelf** - de plek van coverage, linters, type-checkers, scans en de CI-pijplijn in de loop benoemen (vóór de overdracht naar de beoordelaars) en verantwoorden waarom beoordelingsaandacht besteden aan wat een machine al objectief vaststelt verspilling is.
2. **De soorten geautomatiseerde poorten onderscheiden en per soort afwegen wat hij wel en niet vaststelt** - uitleggen wat coverage, een linter, een type-checker en een securityscan elk meten, en verantwoorden waar de grens van elke poort ligt.
3. **Verantwoorden waarom groen noodzakelijk maar niet voldoende is** - aan een geval waarin alle poorten groen zijn terwijl de code het verkeerde doet, uitleggen dat coverage toont dát een regel is uitgevoerd en niet dat het juiste is getoetst, en benoemen waar daardoor het menselijke oordeel onmisbaar wordt.

## Opbouw

### De machine als poortwachter

In het kwaliteitsraamwerk is de eerste soort kwaliteitsmechanisme de [geautomatiseerde en deterministische](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md): coverage-drempels, linters, type-checkers, securityscans en de CI-pijplijn die test en bouwt. Een machine stelt ze objectief en herhaalbaar vast; er is geen oordeel nodig, de drempel wordt gehaald of niet.

Hun plek in de loop is scherp: deze poorten staan vóór de beoordeling, niet erin. De bouwer levert pas een overdracht aan de beoordelaars ({core}`contracts/review-handoff.md`) nadat de geautomatiseerde poorten groen zijn. Schaarse beoordelingsaandacht besteden aan wat een machine al kan vaststellen, is verspilling. Zo zijn de poorten een toegangsvoorwaarde tot de review.

### Wat elke poort wel en niet vaststelt

Elke poort meet iets echts, en elke poort heeft een grens.

- **Coverage** toont dat een regel is uitgevoerd tijdens de tests. Het toont niet dat het juiste is getoetst: een regel kan draaien onder een assertie die het verkeerde controleert.
- **Linters en formatters** bewaken vorm en stijl, niet of de code het juiste doet. Ze handhaven bovendien deels conventies (soort 2 uit het raamwerk).
- **Type-checkers** vangen een hele klasse fouten af, maar zeggen niets over of de bedoeling klopt: typecorrecte code kan het verkeerde berekenen.
- **Securityscans** (SAST, dependency-audits) vinden bekende patronen en kwetsbare afhankelijkheden, niet de ontwerpfout die geen bekend patroon is.

Het concrete voorbeeld in deze module is Python met pytest en coverage, maar de soorten poorten gelden in elke stack. De tooling is inwisselbaar; de soort poort en zijn grens zijn de leerstof.

### Groen maar fout

Hier ligt de kern van de module. Een agent levert moeiteloos groene tests bij code die het verkeerde doet. In de oefening zie je een boekenplank waarvan de testsuite groen is en 100% regeldekking haalt, en die toch een echt defect bevat: een al uitgeleend boek kan nogmaals worden uitgeleend. De test die requirement 6 lijkt te bewaken, controleert alleen dát het boek uitgeleend is, niet dat de tweede uitlening geweigerd werd. De regel draait, dus de dekking is volledig; de assertie is te zwak, dus de fout blijft staan.

Dit is precies de raamwerk-vraag: toetst deze test wel het juiste, of alleen dát er iets is uitgevoerd? Coverage kan die vraag per definitie niet beantwoorden. Een groen vinkje is een voorwaarde om te mogen beoordelen, niet het bewijs dat de beoordeling heeft plaatsgevonden.

### De brug naar het oordeel

Het gat dat de machine laat liggen, is geen tekortkoming van de tooling maar de grens ervan. Daar wordt de menselijke en de geautomatiseerde beoordeling onmisbaar: de adversariële beoordelaar die naar het niet-afgevangen geval zoekt, doet wat een coverage-cijfer niet kan. Die beoordeling is de stof van module 4. Deze les stopt bij de constatering dat de poort groen is en er tóch geoordeeld moet worden; het oordeel zelf doen we nog niet.

## Werkvormen en toetsing

- Werkvormen: korte instructie, gezamenlijke ontleding van de groene boekenplank (worked example), daarna zelf toepassen op de eigen boekenplank in oefening 3.
- Toetsing: in deze fase formatief, via de verantwoordingsvragen van oefening 3.

## Bronnen

- Het raamwerk [Kwaliteit als gedeelde verantwoordelijkheid](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md), sectie "1. Geautomatiseerd en deterministisch" en "De drie samen".
- De repository zelf: {core}`contracts/review-handoff.md` (de bouwer levert pas aan de beoordelaars nadat de poorten groen zijn) en {core}`roles/builder.md` (de bouwer is verantwoordelijk voor verifieerbaar werk).
