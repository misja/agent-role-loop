# #33: Codex-adapter met één begrensde praktijkproef

## C1: route en grondslag

C0: [#33](https://github.com/misja/agent-role-loop/issues/33), volgende adapter
na gemergede #32/PR59. Bord gecontroleerd op 6 oktober 2026: #29/31/32/35/36/37,
#46/48–52 Done; #33/34/58 Backlog. #58 is geen afhankelijkheid van deze adapter.
Norm-/procesbasis: `a9864c8a0b8cc0acab38d31d47a4582e0886966f`.
Leesbare bronnen: CLAUDE.md, core/loop.md, core/contracts/, core/roles/,
teaching/conventies.md, doelgroep.md, schrijfwijzer.md en begrippen.md.
Geen normwijziging of afwijkend doelgroepbeeld.

Route PLANNED, omvang M. Root orkestreert/plant/bouwt; één verse onafhankelijke
review33 beoordeelt alle AC1–11, technisch en didactisch. Geen afzonderlijke C3:
kleine bestandsadapter zonder nieuw framework of gedeelde corewijziging.
Ontwerp- en opleveringsteller #33 beginnen beide op 0; oefenproeven hebben eigen
registers. Eén begrensde automatische herstelronde per soort volgens core,
registratie vóór herstel en verse repair-review met appendix. Eén C6 is final.
C4 op dit concrete plan vereist vóór bouwen; merge blijft afzonderlijk mensbesluit.

## C2 v1: concrete uitvoering

Maak `adapters/codex/README.md` als technische naslag en een kleine projectingang
plus herbruikbare opdrachtvorm voor afzonderlijke roluitvoering. Gebruik de
bestaande core rechtstreeks of als coherent gekopieerd pakket. Geen duplicatie
van generieke rolprompts, geen SDK, MCP-server of nieuw orkestratieframework.
De mens draagt lokale contractbestanden over en beheert Git/trackeracties.
De adapter maakt die handelingen en hun invoer concreet.

Hoofdroute: telkens een nieuwe `codex exec`-aanroep met expliciete rolbron,
contractinvoer en normen. Geen resume/fork bij initial review of repair-review.
Planner/reviewer krijgen read-only; builder workspace-write in een aparte
proefrepository. Geen add-dir naar productie of bypass van sandbox/approvals.
Read-only is een schrijfgrens, geen beperking tot uitsluitend aangewezen leesbestanden.
Inventariseer automatisch geladen globale/project-AGENTS, overrides, config,
rules, hooks, skills en MCP. Maakgeschiedenis en andere oordelen blijven buiten
instructies en reviewinvoer. Claude-configuratie geeft geen Codex-toolrechten.

Behoud bestaande AGENTS/projectafspraken/config bytegelijk. Nieuwe adapterbestanden
krijgen eigen paden, preflight op conflicten, manifest met herkomst/hashes en
gecontroleerde rollback. Waar een bestaande AGENTS een verwijzing nodig heeft,
toon de gerichte aanvulling apart; nooit blind vervangen. De tijdelijke proef
mag een eigen schone AGENTS-ingang krijgen. Geen globale configuratie aanpassen.

### Concrete oefen-C2 binnen dit plan

Nieuwe tijdelijke Git-repository met gedeelde boekenplank_basis.py als
boekenplank.py, ongewijzigde controleer.py, PROJECT.md, schone AGENTS en core.
C0: lijst krijgt alleen_beschikbaar=False. S1 standaard alle boeken in
invoegvolgorde; S2 True alleen uitgeleend_aan is None in dezelfde volgorde;
S3 leeg/alles uitgeleend geeft []; S4 filtering behoudt boeken en uitleenstatus.
Geen opslag, CLI, dependencies, sortering of keyword-only-interface.

Exact goedgekeurde ontwerpkeuze bij akkoord op dit plan:
`def lijst(self, alleen_beschikbaar=False)`; bij True een nieuwe gefilterde
lijst retourneren, anders bestaande `return list(self._boeken)` behouden.
Controleer.py blijft ongewijzigd. Commando `python3 -B controleer.py werk volledig`:
basis verwacht één pass en drie TypeErrors/exit1; product vier pass/exit0.
Geen nieuwe AC5/6 aan de productsuite toevoegen; dat vervolg is eigenaar #58.
De S4-test controleert waarden; objectidentiteit/diepe kopieën worden niet bewezen.

Laat echte Codex-planner deze invoer en normen onderzoeken en C2 teruggeven.
Dit plan bevat de concrete functionele keuzes zodat een overeenkomstige C2
hetzelfde menselijke akkoord kan gebruiken, met exacte verwijzing en vergelijking.
Stelt de planner een andere interface, doel, scope, norm of risico voor, leg dat
nieuwe concrete besluit eerst aan de mens voor; geen impliciete vrijgave.
Bewaar C1/C2/C4 vóór bouw. Bouw echte rood/groen-proef; Codex-orkestratie bewaart
exact productcommit en C5-kern voordat een nieuwe reviewer alle S1–4 beoordeelt.
Initial review krijgt geen planner-/bouwtranscript of ander oordeel.

Gerichte herstelproef: injecteer afzonderlijk de bekende A-versie als expliciete
negatieve fixture, geen spontaan modeldefect. Bewaar eigen commit en C5 met
zwakke-suite-groen versus volledige-suite-S4-rood. Verse reviewer verwacht BLOCK
op werkelijke fout. Leg NEG ontwerp0/oplevering1 en blockers vast vóór één
bouwerreparatie; bewaar rood/groen, herstelcommit en expliciete appendix.
Verse repair-review hercontroleert fix en afhankelijkheden. Geen reset van
hoofdproef/#33-tellers; geen defect of oefenmerge als geaccepteerd verzinnen.

### Tekstontwerp en bestanden

Nieuw `teaching/praktijk/codex.md`, directe praktijknavigatie in teaching/index.md.
Studentroute na module2 en gedeelde praktijk, derdejaars met terminal/Git/Python
maar aanvankelijk alleen webchatervaring. Model/programma/sessie/rol/context
uit teaching/van-chat-naar-agent.md en gedeelde praktijk. Nieuwe toepassing:
AGENTS laden, afzonderlijke Codex-aanroep, sandbox/approval, expliciete rolinvoer,
werkelijke tooluitvoer en exacte reviewcommit. Leg iedere stap uit bij gebruik,
met invoer/voorwaarde, uitvoerder, toegang, handeling, reden, herkenbare uitkomst/fout.
Technische Engelse README voor installatie/onderhoud apart van Nederlands studentpad.

Bewijsregister `onderzoek/33-uitvoering.md` plus kleine reproduceerbare fixtures,
contracten/snapshots en geselecteerde daadwerkelijke tooluitkomsten waar nodig.
Geen ruwe providertranscripten, credentials of accountidentiteit publiceren.
Core, bestaande adapters, modules en gedeelde casusbundle ongewijzigd houden.
Geen standaard screenshots bij dit tekstwerk.

## Feiten, bronnen en verificatie

Lokaal gelezen: codex-cli 0.160.0, exec --help (onder andere read-only,
workspace-write, --json, --ephemeral, stdin en output-last-message); loginstatus
meldt ChatGPT, zonder identiteit. Geen modelaanroep/quotumtest uitgevoerd in planfase;
werkelijk model-ID/configuratie pas bij run registreren. Geen vaste modelupgrade kiezen.
CLI geeft in huidige sandbox een waarschuwing over niet-schrijvbare PATH-aliases;
versie/help/loginstatus werken. Tijdens proef echte oorzaak/uitkomst registreren.

Officiële OpenAI-documentatie gelezen op 6 oktober 2026:
[non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode),
[AGENTS discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md),
[security](https://learn.chatgpt.com/docs/security).
Docs en lokale help ondersteunen nieuwe exec-aanroep, expliciete sandbox en
JSON-uitvoer. AGENTS worden per run opnieuw opgebouwd; verse conversatie
verwijdert die instructies niet. --ephemeral beperkt opgeslagen sessiebestanden,
geen OS-isolatieclaim. Werkelijke ondersteuning controleren tijdens uitvoering.
Markdownversies van bronpagina's konden niet door de webtool worden gelezen;
HTMLbronnen wel. Geen alternatieve onofficiële bron als gezag gebruikt.

Verificatiemodellen: validation-workflow voor installatie/configuratie met
verwachte bytes/hashes/conflictstop/rollback; test-first voor filtergedrag;
manual-with-expected-results voor tekstlezing en workflowgrenzen.
Docs-build -W --keep-going, lokale links inclusief inkomende navigatie,
diff --check en beschermde diff. Verse review33 voert eigen relevante checks uit
en leest het hoofdpad per stap tegen pinned onderwijsnormen.

## AC1–11: volledig aan review33

| AC | Toetsing en verwachte uitkomst |
|---|---|
| 1 | Codex-projectingang en echte afzonderlijke rollen met geldige core; geen Claude-rechtenclaim. |
| 2 | Inventaris, eigen bestanden/manifest, bestaande bytes behouden, conflicten stoppen, rollback aangetoond. |
| 3 | Aanbieder/tool/project herkenbaar; geladen instructies en echte sandbox/rechten; lokale issue-/PR-tekst met herkomst wanneer geen trackertoegang. |
| 4 | Werkelijke plan/mensbesluit/bouw/test/commit/verse C6/terugkoppeling; eigen negatieve herstelketen met persisted teller en verse appendixreview. |
| 5 | Concrete stapinvoer/commando/uitkomst, tijdelijke map, credentials buiten publicatie. |
| 6 | Werkelijke datum/CLI/model/config/tests, geweigerde of ontbrekende checks expliciet; geen volledig getest SHIP bij ontbrekend hoofdpad. |
| 7 | Core/casusbron behouden; docs/linkchecks schoon; teachingconventies toegepast. |
| 8 | Doelgroep en technische versus studentroute expliciet. |
| 9 | Nieuwe handelingen verklaard bij eerste gebruik, eerdere uitleg vindbaar. |
| 10 | Iedere stap input/handeling/uitvoerder/toegang/reden/uitkomst/fout zelfstandig afleidbaar. |
| 11 | Onafhankelijke hoofdpadlezing met concrete passages/begripsprongen; agentlezing niet als studentvalidatie. |

## Grenzen en besluit

Geen native GitHub-reviewintegratie, productie-installatie, providerbenchmark,
API-client, studentmeting of verplicht native subagentframework. Geen eerdere
Claude-uitvoer heretiketteren als Codex-proef. Account-/netwerkproblemen kunnen
proef blokkeren: registreer ontbrekende uitvoering en claim geen volledige afsluiting.
Bij C6 SHIP menselijke mergepoort; geregistreerde nits als eigen vervolgwerk.

C4-vraag: dit adapterplan inclusief bovenstaande concrete oefenkeuzes vrijgeven?
