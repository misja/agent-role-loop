# Les 3 - De machine vertrouwen en wantrouwen

> **Status:** outline met leeruitkomsten. De volledige lesuitwerking (slides, timing per werkvorm, docentennotities) is vervolgwerk.

## Plaats in de leerlijn

Derde module van de leerlijn. In module 2 heb je de loop begrepen als scheiding van verantwoordelijkheden, met contracten als interface. Een van die contracten is de overdracht van de bouwer naar de beoordelaars. Deze les gaat over wat er vóór die overdracht moet kloppen: de geautomatiseerde poorten die een machine objectief vaststelt. Vereiste voorkennis: module 2 afgerond, en het kwaliteitsraamwerk, soort 1.

De les hoort bij [oefening 3](oefening.md), waarin je aan een groene boekenplank ontdekt dat volledige dekking en een fout samen kunnen gaan.

## Leeruitkomsten

De leeruitkomsten staan als "Wat ga je leren" op de [module-index](index.md).

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

Dat is het eerste gezicht van groen-maar-fout: de lat staat verkeerd. Er is een tweede, dat nog scherper is: er is geen lat. Dezelfde suite haalt "100% dekking", maar geen regel dwingt dat af - er is geen drempel ingesteld en geen linter of type-checker geconfigureerd. Die 100% is toevallig, niet vereist: schrap je de helft van de tests, dan zakt de dekking en faalt er tóch niets. De poort rapporteert een getal, maar eist er niets mee.

Zo werkt de conventionele laag onder de geautomatiseerde, precies zoals het raamwerk stelt: soort 2 parametriseert soort 1. Een poort dwingt alleen af wat een conventie heeft besloten. Waar niemand een norm koos, is de poort groen en leeg, want het vinkje betekent niets als niemand besloot wat het moet eisen.

### De brug naar het oordeel

Het gat dat de machine laat liggen, is geen tekortkoming van de tooling maar de grens ervan. Daar wordt de menselijke en de geautomatiseerde beoordeling onmisbaar: de adversariële beoordelaar die naar het niet-afgevangen geval zoekt, doet wat een coverage-cijfer niet kan. Die beoordeling is de stof van module 4. Deze les stopt bij de constatering dat de poort groen is en er tóch geoordeeld moet worden; het oordeel zelf doen we nog niet.

## Werkvormen en toetsing

- Werkvormen: korte instructie, gezamenlijke ontleding van de groene boekenplank (worked example), daarna zelf toepassen op de eigen boekenplank in oefening 3.
- Toetsing: in deze fase formatief, via de verantwoordingsvragen van oefening 3.

## Bronnen

- Het raamwerk [Kwaliteit als gedeelde verantwoordelijkheid](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md), sectie "1. Geautomatiseerd en deterministisch" en "De drie samen".
- De repository zelf: {core}`contracts/review-handoff.md` (de bouwer levert pas aan de beoordelaars nadat de poorten groen zijn) en {core}`roles/builder.md` (de bouwer is verantwoordelijk voor verifieerbaar werk).

## Afronding

### Wat heb je geleerd

De geautomatiseerde poorten (coverage, linters, type-checkers, scans, CI) zijn een toegangsvoorwaarde tot de review, niet de review zelf: ze staan ervóór. Elke poort meet iets echts en heeft een grens. En groen is noodzakelijk maar niet voldoende, op twee manieren: een test kan volledig dekken en toch het verkeerde toetsen (de lat staat verkeerd), en een poort kan groen zijn zonder iets te eisen omdat niemand een norm koos (er is geen lat). Wie de norm kiest, is een mens, niet de machine.

### Zelfcheck

Beantwoord uit je hoofd; de sleutel wijst alleen waar je het kunt nakijken.

1. Waarom staan de geautomatiseerde poorten vóór de beoordeling en niet erin? (zie "De machine als poortwachter")
2. Wat toont coverage wel en wat niet? Geef een geval waarin 100% dekking samengaat met een fout. (zie "Groen maar fout")
3. Een suite is groen met 100% dekking, maar er staat geen drempel ingesteld. Waarom bewijst die groene poort dan nog niets, en wie moet dat beslissen? (zie "Groen maar fout")
4. Waar wordt het menselijke oordeel onmisbaar, en waarom kan de machine dat niet leveren? (zie "De brug naar het oordeel")

### Volgende stap

De machine heeft de poort vrijgegeven, maar iemand moet nog steeds oordelen over wat de machine niet kan vaststellen. Module 4 (Oordelen) is die stap: je neemt zelf de rol van beoordelaar. Daarmee ga je van de geautomatiseerde laag naar de oordeelsmatige laag, het hart van het kwaliteitsraamwerk.
