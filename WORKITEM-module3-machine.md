# Werkitem: module 3 (De machine vertrouwen en wantrouwen) uitwerken

> Type: C0-werkitem voor de leerlijn (uit WORKITEM-leerlijn-zesdeling.md).
> Komt terug ter gate vóór de planfase begint, zodat de afbakening en de
> didactische haak nog bijgestuurd kunnen worden vóór er gebouwd wordt. Dit is
> nog geen build packet. Doelgroep: derdejaars HBO-ICT Software Engineering.

## Context

Het zes-modulen-skelet staat; module 3 ("De machine vertrouwen en wantrouwen")
is nu een routekaart-stub met titel, leerdoel en kwaliteitslaag. De modules 1 en
2 zijn gevuld. Module 3 is de eerste module die een concrete kwaliteitslaag uit
het raamwerk "Kwaliteit als gedeelde verantwoordelijkheid" volledig in de
leerlijn brengt: de **geautomatiseerde en deterministische** laag (soort 1).

Het raamwerk heeft de inhoud van die laag al neergezet: coverage-drempels,
linters, type-checkers, securityscans en de CI-pijplijn zijn mechanismen die een
machine objectief en herhaalbaar vaststelt, en ze horen vóór de beoordeling als
toegangsvoorwaarde, niet als onderdeel ervan. De kernzin staat er ook al: een
groen vinkje is een voorwaarde om te mogen beoordelen, niet het bewijs dat de
beoordeling heeft plaatsgevonden. Module 3 maakt dat inzicht beleefbaar in plaats
van louter leesbaar.

## Probleem dat deze module oplost

Studenten kennen coverage, CI en linters meestal als "iets dat groen moet zijn".
Dat is precies het onvolwassen beeld dat het raamwerk benoemt: kwaliteit als één
vinkje. Bij het werken met AI-agents wordt dat beeld gevaarlijk, want een agent
levert moeiteloos groene tests bij code die het verkeerde doet. De module moet de
student van "groen dus goed" naar "groen is noodzakelijk maar niet voldoende, en
ik kan verantwoorden waar het gat zit" brengen.

## Desired outcome

- Module 3 bestaat als volwaardige eenheid (les + oefening) volgens worked
  example met fading, met de geautomatiseerde laag als onderwerp.
- De student kan de geautomatiseerde poorten (coverage, lint, type-check,
  securityscan, CI) plaatsen als **toegangsvoorwaarde tot de review**, niet als
  de review zelf, en dat verantwoorden vanuit de loop.
- De kernles "groen is noodzakelijk maar niet voldoende" is niet verteld maar
  **ervaren**: de student ziet of construeert een geval waarin alle poorten groen
  zijn terwijl de code het verkeerde doet, en kan benoemen waarom de machine dat
  per definitie niet vangt (coverage toont dat een regel is uitgevoerd, niet dat
  het juiste is getoetst).
- Module 3 motiveert module 4 (Oordelen) zonder het oordeel zelf al te doen: het
  gat dat de machine laat liggen is precies waar de menselijke beoordelaar nodig
  wordt.
- Alle leeruitkomsten zijn geformuleerd als kunnen-verantwoorden.

## Doorlopende casus

De groeiende boekenplank uit oefening 1. Module 3 voegt geen functionaliteit toe
maar legt een **geautomatiseerde poortlaag** om de bestaande boekenplank: een
testsuite met coverage-drempel, een linter en type-checker, en een CI-workflow
die die poorten handhaaft. De "groen maar fout"-haak grijpt op een concreet
requirement van de boekenplank (zie gate-vraag 1).

## Afbakening (voorstel voor de gate)

| Vraagstuk | Hoort in module 3 | Hoort elders |
|---|---|---|
| Wat de geautomatiseerde poorten zijn en waarom ze vóór review staan | ja | - |
| Poorten opzetten op de boekenplank (coverage, lint, CI) | ja | - |
| "Groen maar fout" herkennen en het gat benoemen | ja | - |
| Het gat daadwerkelijk dichten met een oordeel / review | nee | module 4 (Oordelen) |
| Welke beslissingen bij de mens blijven, onomkeerbaarheid | nee | module 5 (Poort) |
| Proportionaliteit: niet elke wijziging verdient alle poorten | aanstippen als doorkijk | uitwerking in module 5 |

De grens met module 4 is scherp: module 3 stopt bij "de machine heeft de poort
vrijgegeven, en nu moet een mens nog steeds oordelen". Het *waarom* van dat
oordeel en het oordeel zelf zijn module 4. Module 3 levert de motivatie, niet de
uitvoering.

## Gate-beslissingen (vastgesteld)

1. **Vorm van de oefening: combinatie.** Een aangeleverd, klein
   Python-boekenplank-repootje dient als worked example; de student doet de
   fading op zijn eigen boekenplank uit oefening 1 (deel B). Zo draagt het
   aangeleverde artefact het zware deel van de les en is de onderhoudslast
   minimaal. Voor wie de eigen code niet meer heeft, is er een terugvaloptie op
   het aangeleverde repootje.
2. **Tooling: vendor-neutraal met één Python-voorbeeld.** De les behandelt de
   *soorten* poorten (coverage, lint, type-check, securityscan, CI) taalonafhankelijk;
   het aangeleverde worked-example-artefact is concreet Python (pytest plus
   coverage), wat aansluit op de toolchain van de repository. De student past het
   toe in zijn eigen stack. Consistent met de lijn dat tooling inwisselbaar is en
   het principe de leerstof.
3. **Geen CI in het artefact.** Het worked-example-repootje gebruikt alleen
   lokale, groene tests met coverage, geen CI-pijplijn. CI, linters en scans
   komen in de les als *soorten* poorten aan bod (toegangsvoorwaarde tot review),
   maar het beleefbare deel beperkt zich tot coverage. De eigen CI-workflow van
   de repository (`.github/`) blijft hooguit een optioneel bijspoor.
4. **Aard van het defect: volledig gedekte code, zwakke assertie.** Het defect
   zit in code die de tests *volledig dekken* (100% regeldekking, alles groen),
   maar de assertie toetst het verkeerde: ze controleert dát er iets gebeurde, niet
   dat het juiste gebeurde. Concreet op requirement 6: een al uitgeleend boek kan
   nogmaals worden uitgeleend (de tweede uitlening overschrijft de lener stil),
   terwijl de test enkel controleert dat het boek "uitgeleend" is en daardoor groen
   blijft. Dit raakt exact de raamwerk-vraag "toetst deze test wel het juiste, of
   alleen dát er iets is uitgevoerd?". Sterker dan een ongedekt randgeval, want het
   ontkracht "100% dus goed".

Plek van het artefact: `teaching/cases/module3-boekenplank/`, bewust buiten de
Sphinx-build (zelfde lijn als `core/`: code is geen site-document). De oefening
verwijst ernaar als inline padverwijzing. `cases` wordt in `docs/conf.py` aan
`exclude_patterns` toegevoegd zodat materiaalmappen de `-W`-build nooit breken.

## Acceptance criteria

1. Module 3 heeft een les en een oefening (geen routekaart-stub meer), opgezet
   volgens worked example met fading.
2. De geautomatiseerde poorten staan in de les geplaatst als toegangsvoorwaarde
   tot de review, met expliciete verwijzing naar soort 1 van het
   kwaliteitsraamwerk en naar de plek in de loop (vóór de review-handoff).
3. De kernles "groen is noodzakelijk maar niet voldoende" is in de oefening
   beleefbaar gemaakt via een concreet "groen maar fout"-geval op de boekenplank,
   met een verantwoordingsvraag die de student het gat laat benoemen.
4. De grens met module 4 is expliciet: module 3 motiveert het menselijke oordeel
   maar voert het niet uit. Geen overlap met de oordeelslaag.
5. Alle leeruitkomsten zijn geformuleerd als kunnen-verantwoorden (kan
   beargumenteren, verantwoorden, afwegen), niet als hebben-opgeleverd.
6. Docs-build schoon onder `-W --keep-going`; geen em-dash of en-dash (AC7);
   Nederlandstalig; spatie-koppelteken-spatie.

## Constraints

- Nederlands; spatie-koppelteken-spatie, nooit em- of en-dash (D9 / AC7).
- Leeruitkomsten consequent als kunnen-verantwoorden (lijn vanaf module 2).
- Kwaliteitslaag van de module: geautomatiseerd en deterministisch (planschets).
- Doorlopende casus: de groeiende boekenplank; didactiek worked example met
  fading, met in module 3 meer zelf-invullen dan in module 2.
- `core/` blijft ongemoeid; bestandsverwijzingen volgen de bestaande conventie
  (`{core}`-rol voor bestanden, directory-refs inline code).

## Size guess

M (les plus oefening voor één module; geen wijziging aan eerdere modules nodig).
