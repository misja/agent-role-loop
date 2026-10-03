# Redactie van modules 1 tot en met 3 (#35)

## Basis en menselijk besluit

De inventarisatie benoemt twintig concrete ingrepen op de negen bestaande
pagina's, met vijf voor/na-voorstellen. Het
[bijgewerkte C2](https://github.com/misja/agent-role-loop/issues/35#issuecomment-5972783285)
is na één gerichte ontwerpreparatie verhelderd: de actuele bordcontrole en haar
gevolgen ontbraken in de eerste versie en zijn toegevoegd. De overige
planinhoud bleef gelijk. De
[C3 repair PASS](https://github.com/misja/agent-role-loop/issues/35#issuecomment-5972788745)
hergebruikt onaangetaste dekking expliciet als eerder vastgesteld.

Het [menselijke C4](https://github.com/misja/agent-role-loop/issues/35#issuecomment-5972801285)
geeft uitvoering vrij. Het besluit bevestigt behoud van leeruitkomstbetekenis
met correctie van absolute formuleringen, drie werkitems met de
wijzigingsrequirements binnen hun portie, zelfstandig leesbare lessen en
historische voorbeelden als gelabelde naslag. Het voert de schrijfwijzeraanvulling
uit de gemergede PR #43 voor dit werk in. Proces- en normbasis:
`51d7a61dcc3d2dd3f50f8d80b105aa5ac9fdeaf8`.

## Uitkomst en samenhang

Module 1 laat eigen waarnemingen toe en onderscheidt een fout van een verklaring
via context rot. De vijftien requirements zijn bytegelijk behouden; de procedure
gebruikt consequent drie C0's. Module 2 werkt eerst het boekenplankplan uit en
onderscheidt contractdefinitie, ingevuld artefact, rolprompt en uitvoering.
Module 3 maakt de uitspraken van tests, regeldekking en drempels afzonderlijk
zichtbaar. Het historische Mermaid-fragment blijft gelabelde naslag bij #21.

Casuscode, core, adapters en modulevolgorde zijn ongewijzigd. De ondersteuning
neemt nog steeds af: een uitgewerkte route, vervolgens eigen overdrachtsanalyses
en daarna een eigen controlekeuze. #36 behandelt modules 4–6 afzonderlijk;
#22 en #23 blijven eigenaar van slides/docentennotities en toetsmateriaal.

## Verificatie en grenzen

- Documentatiebuild met `make -C docs html`, onder `-W --keep-going`, geslaagd.
  Vier aanvankelijk ongeldige links naar adapterbestanden buiten de site zijn
  vóór review hersteld naar GitHub-bestandslinks.
- 647 lokale HTML-linkdoelen en fragments gecontroleerd: geen fouten. Dit is
  geen controle van de beschikbaarheid van alle externe bronnen.
- Negen pagina's lokaal in headless Chrome visueel gelezen met screenshots
  van boven-, midden- en eindgedeelten: bekeken koppen, tabellen, lijsten,
  codeblokken en vaste staarten zonder zichtbare layoutproblemen.
- Module3-casus in afzonderlijke kopie: zes tests slagen met 100% dekking;
  selectie zonder terugbrengtest geeft vijf geslaagde tests en 92,59% dekking;
  dezelfde selectie met drempel95 geeft exitcode1. Python3.14.4, pytest9.1.1,
  pytest-cov7.1.0, coverage7.16.2. Deze versies zijn proefgegevens, geen
  nieuw vastgepind curriculumbeleid. Casusbronnen ongewijzigd.
- Diffcontrole geslaagd; geen em/en-dash in de negen gewijzigde pagina's.

## Onafhankelijke beoordeling

Beide initial C6's beoordelen
`1de12620991caabf98ff803347fa561cfcc9c2a4` tegenover de normbasis.
De reviewers kregen C5-kern, criteria, plan, geldende besluiten en normen,
zonder maaktranscript of elkaars oordelen.

[Redactioneel/didactisch](https://github.com/misja/agent-role-loop/issues/35#issuecomment-5972937094):
SHIP, AC1/2/4/5 pass. Kernredenering en één opdracht per module zelfstandig
nagegaan; module3-proef en tegenassertie daadwerkelijk uitgevoerd. Module1 is
tekstueel doorlopen, geen volledige chatrun; module2 gebruikt gelabelde
voorbeeldbronnen en vervangt geen studentinlevering.

[Technisch](https://github.com/misja/agent-role-loop/issues/35#issuecomment-5972937263):
SHIP, AC3/6 pass. Routes, normen, links en casusproef zelfstandig gecontroleerd;
build en visuele lezing expliciet als aangeleverd bewijs gebruikt.

Geen blockers, nits of contract drift. De verenigbare beoordelingen worden door
de orkestrator in C7 samengevoegd; geen inhoudelijke arbitrage nodig.
Herstelstand: ontwerp1 verbruikt, oplevering0. Deze afrondingsregistratie wijzigt
geen beoordeelde moduletekst. [PR #44](https://github.com/misja/agent-role-loop/pull/44)
wacht op menselijke merge.

Dit is agentlezing en technisch controlebewijs, geen studentproef. Providerroute,
gemeten leereffect, tokens, totale agentduur en menselijke leestijd zijn niet
beschikbaar.
