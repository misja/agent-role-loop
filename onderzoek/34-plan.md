# #34: Mistral via Vibe, met expliciete gereedschapsgrenzen

## C1: route en grondslag

C0: https://github.com/misja/agent-role-loop/issues/34.
Norm-/procesbasis: `04c087cee43ef074f1e132686688cbf01014f2ce`.
Leesbare bronnen: CLAUDE.md, core/loop.md, core/contracts/, core/roles/,
teaching/conventies.md, doelgroep.md, schrijfwijzer.md en begrippen.md.
Bord gecontroleerd op 6 oktober 2026: #29–33/35–37/46/48–52 Done;
#34 en #58 Backlog. Overdracht #33/PR60 gelezen. #58 blijft apart.
Geen normwijziging of afwijkend doelgroepbeeld.

PLANNED, M. Root plant, bouwt en orkestreert. Eén verse onafhankelijke review34
beoordeelt alle AC1–11, met technische én didactische opdracht. Geen C3: één
begrensde adapter zonder corewijziging of framework. C6 is final, geen C7.
Ontwerp- en opleveringsteller starten op 0; maximaal één automatische herstelronde
per soort, registratie vóór herstel en verse repair-review met appendix.
C4 op dit concrete C2 is vereist vóór bouwen; merge vraagt een afzonderlijk
menselijk besluit. De negatieve oefenproef heeft een eigen tellerregister.

## C2 v1: gekozen route en kleinste hulpmiddel

Werk `adapters/openai-compatible/README.md` bij en voeg binnen die adapter een
Mistral/Vibe-route toe. Een losse chat-completions-aanroep ontvangt aangeleverde
tekst en heeft op zichzelf geen repositorygereedschappen. Vibe is het uitvoerende
CLI-programma dat Mistral aanroept en toegestane lokale bestanden leest/bewerkt.
De mens beheert contractoverdracht, tests, Git, issue/PR en beslismomenten.
Geen algemene API-client, SDK, MCP-server of orkestratieframework bouwen.

Kleinste hulpmiddel: een lokale installer voor een coherent corepakket, een
projectingang en herbruikbare rolopdracht; gewone bestanden onder een eigen
`.vibe/role-loop/`-pad. Geen native subagentconfiguratie verplicht. Nieuwe Vibe-
processen krijgen expliciete rolbron, contractinvoer en projectnormen.
Planner/reviewer krijgen uitsluitend `read_file` en `grep`; bouwer daarnaast
`write_file` en `search_replace`. Controleer deze namen en effectieve selectie
tegen geïnstalleerde bron en daadwerkelijke uitvoer. Geen bash, task, connectors,
MCP of resume/continue in de proef. Toolselectie is geen OS-sandbox: een aparte
proefmap beperkt de gekozen opdracht; leesbereik en geladen globale instructies
moeten afzonderlijk worden geïnventariseerd en vermeld.

Gebruik expliciet `--agent plan` voor lezen en een eigen begrensd bouwerprofiel
of `accept-edits` met genoemde allow-list voor bewerken. Leg de werkende variant
vóór publicatie vast. Geen algemene `--auto-approve` of impliciete defaultrechten.
De mens voert `python3 -B controleer.py werk volledig` uit en levert volledige
uitvoer plus exitcode aan de rol; de bouwer heeft geen shell nodig. Reviewtests
worden opnieuw door de mens uitgevoerd op de exacte reviewcommit en leesbaar
meegegeven, zonder te beweren dat Vibe zelf tests uitvoerde. Indien een rol andere
bevoegdheden nodig acht, stop en leg de gewijzigde risicokeuze aan de mens voor.

Inventariseer bestaande AGENTS, `.vibe`-configuratie, globale profielen/prompts,
skills, hooks, providers, tools en trust. Een verse conversatie verwijdert geladen
instructies niet. Behoud bestaande bestanden bytegelijk; installer krijgt
conflictpreflight, manifest met herkomst/hashes en gecontroleerde rollback.
Een eventuele verwijzing in bestaande projectinstructies is een afzonderlijke
zichtbare handmatige aanvulling. Geen globale configuratie of credential wijzigen.
De proef gebruikt alleen een schone tijdelijke Git-repository en eigen instructies.
Issue-/PR-tekst wordt als lokaal artefact met bron en exact commit overgedragen;
Vibe krijgt geen trackerrechten. Trust voor eigen proefbestanden alleen per run.

### Concrete oefenkeuzes waarvoor akkoord wordt gevraagd

Gebruik de gedeelde boekenplank_basis.py als boekenplank.py, ongewijzigde
controleer.py en een PROJECT.md. De opdracht is `lijst(alleen_beschikbaar=False)`:
S1 standaard alle boeken in invoegvolgorde; S2 True uitsluitend boeken waarvan
uitgeleend_aan None is, in dezelfde volgorde; S3 leeg/alles uitgeleend geeft [];
S4 filteren behoudt opslag en uitleenstatus. Geen CLI-, opslag- of dependencywerk.
Exact ontwerp: `def lijst(self, alleen_beschikbaar=False)`; True retourneert een
nieuwe gefilterde lijst, False behoudt `return list(self._boeken)`.
De aangeleverde controleer.py blijft ongewijzigd; geen uitbreiding met #58.
Verwacht basis één pass/drie TypeErrors/exit1; product vier pass/exit0.
S4 bewijst waarden, geen diepe kopieën of objectidentiteit.

Laat een echte nieuwe Vibe-planner C2 maken op deze invoer en normen. Vergelijk
zijn keuzes expliciet met dit goedgekeurde ontwerp; alleen een overeenkomstige
C2 gebruikt hetzelfde menselijke akkoord met bronverwijzing. Afwijkende interface,
scope, norm of risicokeuze vraagt eerst een nieuw mensbesluit. Bewaar C0/C1/C2/C4
vóór bouwen, test rood/groen, leg exact productcommit en C5 vast en laat een nieuwe
Vibe-beoordelaar S1–4 lezen zonder maaktranscript of eerder oordeel. Bewaar
werkelijke gereedschapsuitvoer, modelidentificatie en terugkoppeling.

Injecteer daarnaast de bekende negatieve A-fixture als afzonderlijke oefencommit,
uitdrukkelijk geen spontaan modeldefect. Zwakke suite verwacht groen, volledige
suite S4 rood. Verse Vibe-review verwacht BLOCK op opslagmutatie. Registreer
NEG ontwerp0/oplevering1 en blockers vóór één bouwerreparatie. Nieuwe repair-review
krijgt actuele C5, diff, eerdere blockers en herkenbaar eerder vastgestelde dekking.
Geen reset van hoofdproef- of #34-tellers. Geen fictieve menselijke oefenmerge.

### Tekstfunctie, voorkennis en bestanden

Technische Engelse naslag in adapters/openai-compatible/, waaronder een concrete
Mistral-pagina, projectingang, rolopdracht en installer. Studentroute in nieuw
`teaching/praktijk/mistral.md`, met navigatie in teaching/index.md. Bewijs in
`onderzoek/34-uitvoering.md` en geselecteerde contracten/fixtures/rungegevens.
Bewaar instruction-snapshots onder niet-actieve namen zoals AGENTS-proef.md.

Studentroute na module2 en gedeelde praktijk: derdejaars met terminal/Git/Python,
geen zelfstandig inrichten van agentomgevingen als aangenomen voorkennis.
Model/programma/sessie/rol/context sluiten aan op van-chat-naar-agent.md en
het gedeelde praktijkvoorbeeld. Nieuwe toepassing uitleggen bij eerste gebruik:
Vibe-installatie en accounttoegang, provider versus CLI versus project,
configuratie/trust, gereedschapsselectie, nieuwe sessie, bestanden als overdracht,
menselijke testuitvoer en exacte reviewcommit. Elke stap noemt voorwaarden/invoer,
uitvoerder, toegang, concrete handeling, reden, herkenbare uitkomst en fout.
Technische onderhoudsnaslag en Nederlandse studentinstructies blijven herkenbaar.
Core, bestaande casus en modules blijven ongewijzigd; geen routinescreenshots.

## Routeverificatie en grenzen van de planfase

6 oktober 2026: lokaal Vibe 2.19.0; versie/help succesvol na hosttoestemming omdat
Vibe zijn logbestand buiten de werkmap opent. Configuratiealias
`mistral-medium-3.5` gevonden. MISTRAL_API_KEY niet in procesomgeving of lokale
.env; keyring meldt uitsluitend aanwezigheid=True. Geen credential/identiteit
getoond. Aanwezigheid bewijst geen geldige toegang, modelbeschikbaarheid of quotum.
Nog geen modelaanroep in de planfase. Bij uitvoering werkelijk provider/model-ID,
versie en uitkomsten vastleggen; geen modelupgrade of providerbenchmark.

Officiële bronnen gelezen:
- https://github.com/mistralai/mistral-vibe/blob/main/README.md
- https://docs.mistral.ai/vibe/code/safety-approvals-permissions
- https://docs.mistral.ai/vibe/code/cli/configuration-reference
- https://docs.mistral.ai/resources/migration-guides
- https://docs.mistral.ai/studio/conversations/chat-completion

De API volgt dezelfde basisstructuur voor model/messages, maar dat bewijst geen
agenttoegang. Vibe heeft programmatic mode, expliciete profielen en toolselectie.
Online pagina's verschillen onderling en met lokale help over defaultrechten in
programmatic mode. Daarom geen defaultclaim: expliciet profiel en allow-list,
controle tegen de geïnstalleerde 2.19.0-bron en daadwerkelijke toolruns. Werkt deze
begrensde route niet, registreer het probleem; geen stille verruiming van rechten.
Geen bestaande globale login/configuratie overschrijven en geen account aankopen.
Ontbrekende toegang of externe uitvoering blijft niet beschikbaar/niet geverifieerd;
zonder echte hoofdproef wordt #34 niet als volledig getest afgesloten.

## Verificatie en onafhankelijke AC-toewijzing

Validation-workflow voor installatie: behouden bytes, complete corehashes,
conflictstop, onveilige paden, gecontroleerde rollback. Test-first voor oefenproduct:
werkelijk rood/groen met ongewijzigde suite. Manual-with-expected-results voor
rolgrenzen, contractketen en tekstlezing. Docs-build onder -W --keep-going,
lokale links inclusief nieuwe navigatie en gerichte beschermde diffcontrole.

Review34 ontvangt uitsluitend C5-kern, exacte productcommit, leesbare normbasis,
mensbesluiten en objectief bewijs met beperkingen. Hij toetst alle AC1–11:

| AC | Concrete beoordeling |
|---|---|
| 1 | Geactualiseerde adapter, Mistral/Vibe werkelijk gebruikt; API versus agent en menshandelingen helder. |
| 2 | Inventaris, behoud, installer/manifest/conflictstop/check/rollback zelfstandig herhaalbaar. |
| 3 | Provider/tool/project, contextisolatie, daadwerkelijke rechten en artefacttoegang aantoonbaar. |
| 4 | Echte volledige hoofdketen en gerichte negatieve herstelketen met menselijke poort en opgeslagen teller. |
| 5 | Concrete commando's/uitkomsten; eigen proefmap; geen credentials in publicatie. |
| 6 | Datum/versies/werkelijke model-ID/controles; ontbrekende toegang correct begrensd. |
| 7 | Core/casusnorm ongewijzigd, geraakte documentatie/build/links schoon, teachingconventies. |
| 8 | Voorkennis en studentroute versus onderhoudsnaslag expliciet. |
| 9 | Nieuwe begrippen en handelingen functioneel uitgelegd bij eerste afhankelijkheid. |
| 10 | Per stap invoer/uitvoerder/toegang/handeling/reden/succes/fout afleidbaar. |
| 11 | Onafhankelijke leesgang per stap met passages en concrete leemten; agentlezing geen studentvalidatie. |

Onafhankelijke reviewer voert eigen installercontroles en docs/linkchecks uit en
leest het studenthoofdpad tegen genoemde voorkennis. Providerproefbewijs krijgt
expliciete herkomst; geen eerdere Claude/Codex-run als Mistral-bewijs heretiketteren.
Studentwaarnemingen niet beschikbaar. Bij SHIP volgt de menselijke mergepoort.

C4-vraag: dit plan inclusief Vibe-route, genoemde rechten en concrete oefenkeuzes
vrijgeven voor uitvoering?
