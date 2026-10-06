# C6 - onafhankelijke strikte beoordeling #58

## Beoordelaar en toewijzing

Verse onafhankelijke strikte beoordelaar /root/review58. Alle AC1-5 zijn hier beoordeeld; geen criteria elders toegewezen. Begonnen met uitsluitend /tmp/arl58-C5.md, daarna de daarin aangewezen normen, C0/C2 en productbronnen. Geen maaktranscript of andere oordelen gelezen; geen provider gestart of repository/product gewijzigd.

## Modus en artefact

Initial. Exact beoordeelde productcommit: ab008365b78071730217bdec1418c5a01b32cb04; vergelijkingsbasis en normcommit b07b477c9fb8aa291753d0c99f70c2b29ee9c72d. Rechtstreeks gelezen: CLAUDE.md, core/loop.md, core/contracts/review-handoff.md, core/contracts/reviewer-verdict.md, core/roles/reviewer-strict.md, teaching/conventies.md, doelgroep.md, schrijfwijzer.md en begrippen.md op deze normbasis.

Scope: oorspronkelijke #58-body via gh issue view; C1/C2 onderzoek/58-plan.md op goedgekeurde commit 276a804a5ef723aba0e04800761e2cb4f3037128. C5 en onderzoek/58-uitvoering.md dragen het menselijke akkoord met bron https://github.com/misja/agent-role-loop/issues/58#issuecomment-6025714624. Geen afwijking of nieuwe normkeuze aangetroffen. Herstelstand ontwerp0/oplevering0 rechtstreeks gecontroleerd.

## Besluit

SHIP.

## Acceptatiecriteria

Alle onderstaande dekking is nieuw onderzocht, niet overgenomen uit een eerder oordeel.

### AC1 - pass

controleer_extra.py:test_e1_false_is_standaard maakt afzonderlijk een gemengde, lege en volledig uitgeleende plank. Beide aanroepen worden tegenover dezelfde verwachte volledige nummer/titel/lener-volgorde gecontroleerd; assertIs controleert dezelfde boekobjecten op iedere positie. De toestandvergelijking borgt ook lengte, zodat zip geen ontbrekend element verbergt. Onafhankelijke uitvoering van de exacte suite op B geeft drie geslaagde tests, exit0. De meegeleverde False-mutant is onafhankelijk gereconstrueerd op een tijdelijke B-kopie: E1 rood, exit1 (ook extra E2-errors en E3-falen, zoals eerlijk vermeld in de overdracht). Dit is foutgevoeligheidsbewijs, geen algemene correctheidsclaim.

### AC2 - pass

controleer_extra.py:test_e2_containers_veranderen_geen_opslag voert de negen combinaties standaard/False/gefilterd en clear/append/pop uit, ieder op een nieuwe gemengde plank. Nummer, titel, lener en volgorde worden vóór/na vergeleken; na een gefilterde vervolgaanroep wordt de volledige opslag nogmaals gecontroleerd. De controle vóór containermutatie ontdekt ook filteren dat zelf de opslag wijzigt. Onafhankelijk B groen; containeraliasmutant E2 rood met vier assertion failures en twee AttributeErrors na append(None), E1/E3 groen, exit1. De errors zijn daadwerkelijke detectie van vervuilde interne opslag en worden nergens als geslaagde assertions verkocht. Bekende A maakt E2 eveneens rood. De container/objectgrens is uitdrukkelijk beperkt tot containerwijziging.

### AC3 - pass

controleer_extra.py:test_e3_toevoegen_na_filteren filtert een gemengde plank en voegt Duin toe. Volledige toestand moet exact 1/Zee, 2/Atlas/Noor, 3/Bos, 4/Duin bevatten; uniciteit, behouden objectidentiteit en identiteit van het teruggegeven nieuwe boek worden apart gecontroleerd. Beschikbaarheidsvolgorde 1,3,4 en onveranderde uitleentoestand worden nagegaan. Onafhankelijke B- en werk/B-uitvoering groen; bestaande A E3 rood, exit1, door verloren uitgeleend boek en verkeerde vervolgnummering. Product-B is terecht niet gewijzigd.

### AC4 - pass

onderzoek/58-uitvoering.md legt de aparte optionele suite en validation-workflow uit: historische testaantallen blijven behouden; tijdelijke mutanten leveren nieuw rood zonder een fictieve productfix. onderzoek/58-proef bevat patches, afzonderlijke feitelijke uitvoer en resultaten.json. Ik heb de beschreven mutanten onafhankelijk gereconstrueerd en dezelfde exitcodes/foutcategorieën waargenomen.

Onafhankelijke bytevergelijking vanuit git-objecten bevestigt alle 113 hashes uit behoud.json tegen basis én productcommit. Daarbij zijn historische dossiers uitsluitend als bytes vergeleken, zonder oude oordelen te lezen. Zipvergelijking bevestigt uitsluitend toevoeging controleer_extra.py en wijziging README.md; alle overige bestaande entries bytegelijk. Beide nieuwe/gewijzigde entries zijn bytegelijk aan hun bronnen. docs/package_practice.py wijzigt uitsluitend de expliciete bestandslijst, zonder upgrade van de historische corebasis.

Oorspronkelijke CLI onafhankelijk herhaald: basis/basis 1 pass exit0; a/zwak 3 pass exit0; a/regressie 1 fail exit1; b/volledig 4 pass exit0. De nieuwe a/b/werk-keuze staat afzonderlijk. Ruwe bewijs-whitespace is expliciet verantwoord en raakt geen productcode of uitleg.

### AC5 - pass

Onafhankelijke agentleesgang van de volledige README en specifiek de nieuwe optionele sectie tegen de aangewezen onderwijsnormen: bekende Python/tests en de reeds uitgevoerde vier controles zijn het vertrekpunt. De invoer is dezelfde bestanden/omgeving en de concrete versie b, a of eigen boekenplank.py. De handelingen staan in drie genummerde stappen met commando’s. De reden voor afzonderlijke dekking is behoud van S1-S4 en het risico dat correct filterresultaat latere opslaghandelingen niet bewijst. Uitkomst is herkenbaar: B drie tests/exit0, A E2/E3 rood/exit1 en E1 groen; eigen gerepareerde versie hoort drie tests te laten slagen.

De nieuwe tussenstap wordt uitgelegd vóór het commando: een lijst bevat verwijzingen naar boekobjecten; wijzigingen aan de lijstcontainer raken de opgeslagen lijst niet, terwijl boekobjecten niet worden gekopieerd en boektitelmutatie buiten de controle valt. Geen onbenoemde LLM-voorkennis, normafwijking of begripsgarantie. Uitleg en instructies hebben herkenbare blokken; register, je-vorm en commandofences passen bij de doelgroep. Het modulestramien is niet vereist voor deze losse bundel-README.

Objectieve technische bewijsbronnen nieuw gelezen: onderzoek/58-proef/build.txt toont sphinx-build -b html -W --keep-going, inclusief kopiëren van de download, en build succeeded. links.txt meldt 187 lokale links/fragments inclusief inkomende links, nul fouten. Deze controles zijn geleverd bewijs, niet onafhankelijk herhaald; de bron- en bundelbytes zijn wel onafhankelijk gecontroleerd. README is geen eigen Sphinx-pagina, dus buildsucces bewijst de uitleg niet. Deze leesgang is agentlezing, geen studentwaarneming.

## Onafhankelijke uitvoering en grenzen

Exacte commit geëxporteerd naar /tmp/arl58-review. Lokale commandouitvoer en onafhankelijke byte/bundelresultaten staan in /tmp/arl58-review/independent-results.json. Alleen deze tijdelijke export kreeg gereconstrueerde werkmutanten; product en repository bleven onaangeraakt. De suite gebruikt alleen standaardbibliotheek en voldoet aan de Python 3.10-syntaxisgrens; daadwerkelijk uitgevoerd met de lokaal aanwezige Python. Geen provider/studentobservatie of algemene correctheid vastgesteld.

## Contractdrift

Geen. Nieuwe optionele CLI en extra zipbestand zijn gedeclareerd in C2/C5; oude CLI, oorspronkelijke casusimplementaties en historische gebundelde core zijn behouden.

## Must fix

Geen.

## Should fix

Geen.

## Nice to have

Geen.

## Hersteluitkomst

Geen: initial mode, geen voorafgaande blockers of hergebruikte dekking. Ontwerp0, oplevering0 blijven staan.

## Volgende actie

Klaar voor het menselijke mergebesluit. SHIP geeft geen automatische mergevrijgave.
