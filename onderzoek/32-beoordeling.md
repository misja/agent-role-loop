# C6 initial — #32 Claude Code-adapter

## Reviewer en toewijzing

review32, onafhankelijke technische en didactische reviewer. AC1–AC11 allemaal aan mij toegewezen; niets aan andere reviewers. Eén reviewer: deze C6 is final volgens core/loop.md. Dit is een agentlezing, geen studentwaarneming.

## Modus, artefact en grondslag

Initial; uitsluitend C5-kern /tmp/arl32-c5.md, aangewezen product, pinned normen, geaccepteerd plan en noodzakelijke objectieve proefbewijzen onderzocht. Geen maaktranscript of ander #32-oordeel gelezen. Oefen-C6's zijn alleen als AC4-productbewijs gelezen.

Productcommit 52d84cd2a9949931fec82704abe260a1e15b17c8; basis b7aad138c18809c747a1e020590e0ad905903514. HEAD op deze productcommit, werkboom schoon. Exacte diff tussen deze SHAs beoordeeld. Procesgrondslag: CLAUDE.md, core/loop.md, core/contracts/review-handoff.md en reviewer-verdict.md, core/roles/reviewer-strict.md. Onderwijsgrondslag: teaching/conventies.md, doelgroep.md, schrijfwijzer.md en begrippen.md. Alle negen normbestanden zelfstandig bytegelijk aan basiscommit gecontroleerd.

Toegepast: concrete scope in onderzoek/32-plan.md en daarin/C5 vastgelegde C4-bronnen 6001713335 (outer) en 6016426784 (oefen-C2/V1–V4). Geen nieuwe normafwijking, doelgroepkeuze of mergevrijgave. Besluitbronnen zijn beoordeeld via de aangewezen lokale registratie; externe identiteit/commentgeschiedenis niet opnieuw geauthenticeerd. #32-tellers ontwerp0, oplevering0; NEG heeft een afzonderlijk geregistreerde oplevering1.

## Besluit

**SHIP.** Geen blocker. De installatie, uitvoeringsroute en begrensde daadwerkelijke proef zijn aantoonbaar; het studenthoofdpad biedt de benodigde overgang van de eerdere leerlijn naar Claude Code. Gereed voor het afzonderlijke menselijke mergebesluit, niet voor automatische merge.

## Acceptatiecriteriadekking

Alle onderstaande criteria zijn **nieuw onderzocht** in deze initial review; geen eerder #32-oordeel of eerder vastgestelde #32-dekking hergebruikt.

| AC | Uitkomst | Eigen onderzoek en bewijs |
|---|---|---|
| AC1 | pass | README, alle negen wrappers en commands/orc.md gelezen. Wrappers verwijzen naar dezelfde geïnstalleerde core; alle negen hebben omitClaudeMd:true. plan-run.json bevat echte Agent(role-loop-planner), success en CLI/modelidentificatie. build-run.json bevat echte bouwerdelegatie en rood/groen; review-run.json en recheck-run.json echte reviewer-delegaties en uitgevoerde suites. Geen nieuw corepad. Niet alle negen rollen worden in deze proportionele oefening geselecteerd; niet-geselecteerde rollen zijn geen live bewezen roluitvoering. |
| AC2 | pass | Zelf python3 onderzoek/32-proef/controleer_installatie.py uitgevoerd, exit0, fixtures in /tmp/arl32-install-check-o78byxoa. Clean/existing kopiëren 30 bestanden, juiste manifesthashes, rollback behoudt eerdere bytes. Collision, orc-skill, dangling orc-skill en symlinkouder stoppen vóór schrijven; gewijzigd eigen bestand en ongeldig directorypad stoppen rollback vóór verwijderen. Beide README-snippets zelf gelezen: controle vóór kopiëren/verwijderen, begrensde eigendomspaden, symlink- en hashcontrole. Geen eerdere installatie overschreven; backupherstel wordt daarom terecht niet als uitgevoerd geclaimd. |
| AC3 | pass | README onderscheidt aanbieder, uitvoerend programma en repository; projectnorm is geen permissieverlening. run-config.json registreert dontAsk/project-settings/lege strikte MCP-config, geen add-dir/fork/resume/bypass. review-run.json geeft exact exclusieve initial-invoer en gelezen paden; geen C1/C2/maakgesprek. recheck-run.json heeft expliciete REPAIR-opdracht met alleen repair-C5/appendix; geen hervatting. Bash-rechten zijn benoemd als echte uitvoeringsrechten, wrappers niet als OS-sandbox. Lege read_paths van recheck betekent geen onafhankelijke complete leesaudit; de delegatie/testuitvoer en het teruggegeven repair-contract ondersteunen de beperktere procesclaim. |
| AC4 | pass | C1/C2/C4, hoofd-C5/C6, NEG-C5/C6, persisted herstelstand, herstel-C5/appendix en herstel-C6 gelezen. Gekozen PLANNED-keten heeft concreet C4 vóór bouw. build-run.json bewaart werkelijke TypeErrors vóór bouw en vier passes erna. Negatieve fixture expliciet geïnjecteerd; S4-mutatie statisch en via eigen uitvoering bevestigd. NEG-review had geen eigen testuitvoering en claimt die ook niet. Teller1 staat als pre-repair registratie; repair-run.json bevat echte rood/groen-tooluitvoer, recheck-run.json nieuwe reviewer en groen. Zelf duurzame build/NEG/herstelsnapshots opnieuw gecontroleerd, zie hieronder. Geen menselijk oefenmergebesluit geclaimd. |
| AC5 | pass | Studentvoorbereiding en stappen1–7 bieden invoer, handeling en controleerbare uitkomst; gedetailleerde dekking hieronder. Aparte oefenrepository, geen echte gebruikersgegevens; accountgegevens/tokens niet bewaren. Duurzame geselecteerde bewijsbestanden bevatten geen zichtbare credentials/accountidentiteit. Geen ruwe providerlogs als reviewinvoer gelezen of gepubliceerd bewijs genoemd. |
| AC6 | pass | onderzoek/32-uitvoering.md en run-config.json noemen datum 6 oktober2026, CLI2.1.289, resolved claude-opus-5-5, werkelijk gebruikte print-mode en concrete grenzen. Geselecteerde tooluitvoer bewijst uitgevoerde tests in plaats van slechts voorgestelde commando's. Weigeringen worden als niet uitgevoerd geregistreerd. Geen tokenmeting, studentbegrip, interactive UI of productieproef uit deze data afgeleid. |
| AC7 | pass | Beschermde diff voor core, andere betrokken adapters, modules/casus leeg; normbestanden bytegelijk. git diff --check basis..product exit0. Zelf .venv/bin/sphinx-build -b html -W --keep-going -c docs teaching /tmp/arl32-review-docs uitgevoerd, exit0. Eigen HTMLParser-controle van alle opgebouwde lokale hrefs/fragmenten: 4018 links, nul fouten, inclusief inkomende navigatie. Externe links niet integraal geaudit. |
| AC8 | pass | Studentpagina regels3–12 positioneert vervolg op module2/gedeelde praktijk met terminal/Git/Python; technische README noemt expliciet installation and maintenance reference en verwijst beginners naar het Nederlandse pad. doelgroep.md laat engineeringkennis toe, maar veronderstelt geen agentervaring; voorbereiding legt die uit. Modulestramien niet verplicht voor deze losse praktijkpagina. |
| AC9 | pass | Regels8–12 verwijzen naar uitleg over model/programma/sessie/rol; eerdere voorbereiding daadwerkelijk gelezen en context/gereedschapsactie/contract daar uitgelegd. Nieuwe adaptertoepassing introduceert manifest bij stap1, rolbestand versus werkitem en orc bij stap2, norm-/codeversie bij stappen2/5, permissie versus C4 bij4, echte tooluitvoer bij5, versheid en grenzen bij6. Geen noodzakelijke nieuwe LLM-kennis alleen naar een begrippenlijst doorgeschoven. |
| AC10 | pass | Eigen staplezing hieronder wijst per stap uitvoerder, invoer, toegang, reden, geslaagde/foutuitkomst aan. Python/modelaccount voorbereid; falende accountcontrole of API-call heeft expliciet stop/fallback. Geen onbenoemde essentiële begripsprong gevonden binnen de afgesproken voorkennis. |
| AC11 | pass | Onafhankelijke technische én didactische hoofdpadlezing tegen dezelfde pinned conventies uitgevoerd. Concreet per stap vastgelegd hieronder; installatie en reproductie zelfstandig uitgevoerd. Dit oordeel stelt tekstdekking en uitvoeringsbewijs vast, geen zelfstandig studentgebruik of gemeten begrip. |

## Zelfstandig uitgevoerde controles

Naast installatie, normbytes, beschermde diff, diff-check, Sphinx en lokale links heb ik de drie duurzame snapshots in aparte tijdelijke mappen als boekenplank.py aangeboden. In /tmp/arl32-review-repro-5f98fwuy/build en /herstel: python3 -B controleer.py werk volledig geeft vier passes/exit0; python3 -B controleer_extra.py geeft M1 True / M2 True True/exit0. In /negatief: volledige suite drie passes/S4 FAIL/exit1, extra controle M1 True gevolgd door de verwachte M2 AssertionError/exit1. Dit bevestigt zelfstandig het Python-gedrag en de aard van de injectie/reparatie. Het is geen nieuwe provideruitvoering en bewijst geen studentgebruik. De hoofd- en herstelsnapshot zijn inhoudelijk dezelfde goede implementatie: selectie retourneren, opgeslagen collectie niet vervangen.

## Didactische hoofdpadlezing

Probleem dat de lezer onderzoekt: hetzelfde beschikbare-boekenfilter uit de gedeelde praktijk uitvoeren met een programma dat gereedschappen en rolcontexten organiseert. Engineeringkennis over tests/Git is toegestaan; kennis van modelaanroepen, context en agents komt uit de expliciet vereiste voorbereiding. Die legt uit dat het programma de context samenstelt en gereedschappen uitvoert, dat rollen verschillende taken zijn en dat eigen context geen garantie op correctheid is. Het gedeelde voorbeeld verklaart C0–C6, de vier criteria, normbesluit en exacte codeversies. De nieuwe pagina verwijst hiernaar vóór zij ervan afhankelijk is.

- **Voorbereiden, regels14–39.** Invoer: bundel/basiscode/testbestand, Git/Python/CLI en bestaand modelaccount. Student pakt uit, neemt basis over, legt Git-basis vast en draait basis/version/auth. Reden: werkplek en toegang aantonen vóór orchestration; standaardbibliotheek maakt dependencybehoefte expliciet. Uitkomst: basiscontrole groen, CLI-versie zichtbaar en accountstatus; auth is terecht geen quotum- of modelcallbewijs. Bij ontbrekende toegang oplossen of gelabelde handmatige fallback. Git-initialisatie kan de afgesproken doelgroep uitvoeren; accountinstallatie heeft een gerichte externe hulpbron.
- **Stap1, regels43–58.** Invoer: bestaande projectinstructies/config en coherent gekozen broncheckout. Student inventariseert en voert de gelinkte kopieerprocedure uit. Reden: bestaande normen behouden en naamconflicten niet overschrijven. Nieuwe begrippen zijn verbonden aan bestanden: rolbestanden/commando/core worden gekopieerd, manifest bewaart eigen bestanden. Uitkomst: eigen bestanden aanwezig, eerdere afspraken ongewijzigd, diff/manifest controleerbaar; conflict stopt. De README vult technische inventaris en rollback concreet in. Deze technische naslag vereist Python/Git die in voorbereiding zijn genoemd; de student hoeft niet zelf het installatiescript te ontwerpen.
- **Stap2, regels60–73.** Invoer: volledige C0 met vier bekende filtercriteria, PROJECT.md, basiscommit/coreversie. Student schrijft de vindbare bestanden; orc draagt opdracht/rol/normen over. Reden: rolprompt zegt hoe, C0 zegt wat, normen begrenzen; eerdere chat of een onbereikbare URL geeft geen leesbare invoer. Uitkomst: elke rol kan opdracht en normen zelfstandig lezen. Exacte versie versus veranderlijke branch is verklaard en bouwt op eerder Git-voorbeeld. Geen stille eis van trackertoegang.
- **Stap3, regels75–91.** Student begint nieuwe CLI-sessie in oefenmap en geeft volledig concrete orc-invoer met normbron, dossierplaats en stopvoorwaarde. Orkestrator maakt C1, planner C2; criteriatoewijzing en interfacebesluit benoemd. Reden voor PLANNED is de optionele parameter en behoud van bestaand gedrag/opslag. Uitkomst: daadwerkelijk C2 waarop student die keuzes controleert; API-/toolfout is geen plan. Een issue openen is dus niet verward met het starten van een agent.
- **Stap4, regels93–99.** Invoer: concrete C2 en eventueel geselecteerde C3. Student beslist met reden en exacte versie, bewaart C4/bron. Bouwer ontvangt vrijgegeven plan/C1/normen/besluit bij PROCEED. Reden: inhoudelijke vrijgave van de interfacekeuze; permissiegoedkeuring geeft alleen toegang. Uitkomst: controleerbare vrijgave of stop/revisie vóór bouw. De rollen- en contractwijzer uit voorbereiding draagt de C-codes; zij worden niet als onverklaarde agentconcepten gebruikt.
- **Stap5, regels101–123.** Invoer: approved pakket, basiscode en concrete volledige suite. Bouwer meet eerst rood, implementeert en meet vier groene controles; student controleert feitelijke tooluitvoer en commit de code. Reden: falend bewijs toont ontbrekend filter, groen toetst criteria, exacte SHA voorkomt een onvaste beoordeling. Tooltoegang is beperkt tot benodigde bestanden/tests; gecombineerde commando's kunnen weigeren, -B-variant moet vastgelegd. Uitkomst: code-diff, echte commit en C5 met besluiten/testuitvoer/grenzen. Geen aanname dat het model zelf tests uitvoert zonder toegestaan gereedschap.
- **Stap6, regels125–138.** Invoer: C5-kern/criteria/commit/normen; reviewer begint vers zonder maakgesprek/ander initial oordeel. Student/orkestrator controleert geladen instructies en bewaart C6. Reden: beperkte voorgeschiedenis, met expliciete beperking dat leesbare bestanden toch toegankelijk zijn. Bij BLOCK eerst blocker/herstelstand, daarna gerichte repair en nieuwe reviewer met voor/na-diff/blockers/geldige dekking. Uitkomst: commitgebonden oordeel en begrensd herstel; core blijft de enige bron van de rondegrens. De tekst introduceert geen garantie dat een rolprompt OS-toegang blokkeert.
- **Stap7, regels140–159.** Invoer: SHIP/oordeel plus exacte commit. Mens neemt afzonderlijk overnamebesluit en bewaart bron; bij issue/PR contractuitkomsten volgens bestaande bronmapping, daarna voortgang bijwerken. Reden: oordeel en status zijn geen menselijk besluit. Uitkomst: volledig lokaal dossier met opdracht/route/planbesluit/code/test/oordeel/vervolgkeuze en gelabelde ontbrekende externe stappen. De slotpassage onderscheidt daadwerkelijke run, agentlezing en studentwaarneming expliciet.

Concrete begripsprongen beoordeeld: chat naar uitvoerend programma; bestandsinstallatie naar geladen rol/commando; instructies naar echte permissies; agentantwoord naar werkelijk toolresultaat; verse context naar beperkte onafhankelijkheid; groene C6 naar afzonderlijk mensbesluit. Elke sprong heeft eerdere uitleg of uitleg bij de handeling. Geen ontbrekende essentiële invoer of redeneerstap gevonden. Kleine redactionele verfijning mogelijk bij stap7: maak 'Werk daarna de bordstatus bij' expliciet voorwaardelijk voor een gekozen bord; uit de voorafgaande issue/PR-voorwaarde en lokale dossierroute is de huidige bedoeling al afleidbaar.

## Contract drift

<none>. Bestaande core-route/contracten intact; wrapper-aanpassing verklaart expliciete norminvoer en grenzen. Geen gewijzigde module/casus/andere-adaptercontracten. Werkelijke proef gebruikt de goedgekeurde interface- en -B-keuzes en heeft geen tracker-/merge-autorisatie toegevoegd.

## Must fix

<none>.

## Should fix

<none> voor dit werkitem. Oefenproductsuite- en nummeringsvervolg is expliciet apart geregistreerd als #58; het door C4 behouden controlebestand alsnog veranderen is geen vereiste reparatie van deze adapteroplevering.

## Nice to have

Maak de bordstatuszin in studentstap7 voorwaardelijk als er een bord is gebruikt. Dit verhindert de lokale hoofdroute nu niet en is geen blocker.

## Repair outcome

<none>: initial #32-review. NEG-repair is uitsluitend objectief bewijs onder AC4 en geen eerdere #32-reparatie of verbruik van de #32-teller.

## Bewijsgrenzen en volgende actie

Eigen installatie/reproductie/docs/linkchecks; opgeslagen geselecteerde echte providergebeurtenissen en oefencontracten gelezen. Geen nieuwe provideraccount-run, interactive UI, studentwaarneming, productie-installatie, volledige externe-linkaudit, modelbenchmark of tokenmeting. Geselecteerde registraties bewijzen niet elke ruwe providergebeurtenis; geen volledig OS-/leestoegangsonderzoek geclaimd. Authentieke menselijke bronregistratie toegepast zonder externe accountidentiteit opnieuw te onderzoeken. Geen Git-/productmutatie of merge uitgevoerd.

Volgende actie: registreer deze volledige C6 bij exact beoordeelde commit en leg het product voor aan de mens voor het mergebesluit. Een uitsluitend latere registeraanvulling is nog geen door deze C6 beoordeelde productcommit; houd het onderscheid met 52d84cd expliciet.
