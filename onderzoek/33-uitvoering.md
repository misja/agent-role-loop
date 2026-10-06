# #33: Codex-adapter, uitvoering

## Grondslag en menselijke vrijgave

Norm-/procesbasis `a9864c8a0b8cc0acab38d31d47a4582e0886966f`;
[C2 v1](https://github.com/misja/agent-role-loop/issues/33#issuecomment-6017597771)
in [33-plan.md](33-plan.md),
[C4 PROCEED](https://github.com/misja/agent-role-loop/issues/33#issuecomment-6017668277).
Root orkestreert/plant/bouwt, verse review33 toetst straks AC1–11.
#33-tellers ontwerp0/oplevering0; geen mergebesluit.

## Installatie en lokale route

Gewone projectingang en invulvorm onder adapters/codex, geen native subagent-
configuratie of SDK. Helper voegt core en drie eigen bestanden toe onder
.codex/role-loop (23 bestanden), bestaande AGENTS/config blijven bytegelijk.
Manifest met source HEAD plus daadwerkelijke hashes; dev-adapter heeft gewijzigde
bytes, dus geen claim dat alle bronbestanden al uit die clean commit komen.
Nieuwe proef-AGENTS handmatig uit voorbeeld; rollback verwijdert die ingang niet.
Acht fixtures zelf uitgevoerd: schoon/bestaand installatie-hash-rollback pass;
conflict/symlink stoppen vóór schrijven; gewijzigd/missend bestand en ongeldige
owned/directorypaden laten rollback vóór verwijderen stoppen. Reproduceerbaar
met 33-proef/controleer_installatie.py; echte resultaten ernaast.
Geen backupherstel geclaimd, geen globale config gewijzigd.

## Werkelijke Codex-proef

Tijdelijke repository /tmp/arl33-smoke-3j2v4v41, basis
`99158040251d49e0cc186ce5625d518b469fcf56`, schone AGENTS/PROJECT en gedeelde
boekenplankbasis/controle. Core bytegelijk normbasis; installatie manifesteert
kopiebytes. Lokale C0/C1/C2/C4 met menselijke bron, geen fictieve casusoordelen.
Python3.14.8 lokaal gemeten; casus vraagt Python3.10 of nieuwer wegens union-types.
Codex-cli0.160.0; loginstatus ChatGPT zonder identiteit; werkelijke header van
een aparte same-config modelcontrole: gpt-6.1-sol/provider openai.
Planner/bouwer-JSON geeft geen modelveld: dat ontbreekt per aanroep, modelcontrole
is apart bewijs van de accountdefault. Review/herstel-aanroepen pinnen vervolgens
expliciet dat geobserveerde model, geen modelupgrade of benchmark.

Iedere fase eigen codex exec --ephemeral --no-daemon, approval never.
Planner/reviewer read-only, bouwer workspace-write in proefmap. Geen bypass,
add-dir, resume/fork of model-Git/tracker-mutatie. Read-only beperkt schrijven,
geen uitsluitend-aangewezen-leesbestanden-garantie. Globale/managed instructies
kunnen nog gelden; AGENTS bevat geen maakgeschiedenis of revieweruitvoer.

Eerste hostsandboxpoging faalde vóór modeluitvoering bij in-process app-server
initialisatie door read-only bestandssysteem; goedgekeurde herhaling slaagde,
de modelplanner bleef read-only. Geen hostfout als providerresultaat geclaimd.

Echte planner C2 bevestigt dezelfde signature/comprehension/non-goals/S1–4/
testcommand/riskkeuzes als de al goedgekeurde concrete oefen-C2. C4 vóór bouw
bewaart die vergelijking met de werkelijke menselijke bron; geen nieuw akkoord
verzonnen. Planner noemt bestaande-testhergebruik validation-workflow; outer
plan noemt het test-first. In beide blijft dezelfde verplichte basis-rood en
implementatie-groen, zonder testwijziging. Geen nieuwe eis of scopekeuze.

Echte bouwer: exact python3 -B controleer.py werk volledig vóór wijziging
één pass/drie TypeErrors exit1; daarna vier pass exit0. Alleen boekenplank.py
gewijzigd, controleer.py ongewijzigd. Productcommit
`3be0eaf3a734c1cb7094c3c137da9692700d976a`; Codex bewaart en bevestigt groen.
Snapshot/C5 in 33-proef, geselecteerde echte command-events/testuitvoer in
plan-run.json/build-run.json. Ruwe providerlogs blijven /tmp, niet in publicatie.
Bij overdrachtsopslag verdween de SHA door shellinterpretatie van backticks;
veld hersteld, maar de lopende reviewer kan de eerdere versie hebben gelezen.
De eerste reviewer stopte zonder verdict omdat de exacte commit ontbrak;
geen criteria onderzocht of tests uitgevoerd. review-incompleet.md/json bewaart
dit. De correcte C5 is opnieuw aan een verse initial context aangeboden. Geen
productreparatie of BLOCK-verdict: oefen-/#33-tellers blijven 0/0.

## Nog af te ronden en grenzen

Hoofdreview SHIP op 3be0eaf3a734c1cb7094c3c137da9692700d976a, S1–4
nieuw onderzocht, vier tests groen/exit0; C6-main.md en review-run.json.
Negatieve fixturecommit49f810f3fe1ecdd9bc89e5f763c7a7cefbf6c4b7 expliciet
geïnjecteerd. Zwak3pass/exit0 tegenover volledig S4FAIL/exit1. Verse review
BLOCK, B1 S4-opslagmutatie; reviewer heeft volledige suite zelf rood gemeten,
geen eigen Git-correspondentiecheck vanwege ruim gelezen verbod in taaktekst.
Codex heeft exact commit/worktree bewaard; geen eigen Git-check door reviewer geclaimd.
Vóór herstel opgeslagen: NEG ontwerp0/oplevering1, vóórcommit, B1 en bron in
negatief-herstelstand.json. Hoofdproef/#33 blijven 0/0. Nu één bouwerreparatie
en daarna verse repair-review met expliciete appendix.

Echte bouwer herstelt alleen de opslagtoewijzing. Vóór herstel drie pass en
S4FAIL/exit1, erna vier pass/exit0. Herstelcommit
`328555e0e4ebec7e5bae82d23634b8e6a57be240`; Codex bevestigt groen na commit.
Herstelsnapshot bytegelijk aan goede hoofdproduct. C5-herstel.md bevat exacte
revisies/diff, B1, eerder gevestigde S1–3-dekking, tellers en expliciete
toestemming voor read-only Git-correspondentiechecks. repair-run.json bewaart
daadwerkelijke rood/groen-commandresultaten, zonder makertranscript.

Verse repair-review SHIP: B1 opgelost, S1–4 opnieuw onderzocht en eigen volledige
suite vier pass/exit0 op exact herstelcommit; code/testcorrespondentie via Git
zelfstandig bevestigd. Eerdere negatieve run blijft eerder gevestigd bewijs,
geen nieuw rood door deze reviewer. C6-herstel.md en recheck-run.json bewaren
werkelijk oordeel en geselecteerde commandresultaten. NEG-teller blijft 0/1,
hoofdproef/#33 0/0; geen tweede ronde of automatische merge.

Docs-build make -C docs html met -W --keep-going slaagt; lokale controle
/tmp/arl33-links.py: 306 links/fragmenten inclusief inkomende navigatie, nul fouten.
Beschermde diff voor core/bestaande adapters/casus leeg; diff --check schoon.

Hoofdreview, gelabelde negatieve herstelproef en docs-/linkcontrole afgerond;
verse onafhankelijke #33-review nog uitvoeren. Geen volledige #33-SHIP/afsluiting of merge.
Geen native GitHub-review, interactieve UI, productieproef, studentwaarnemingen,
gemeten begrip, modelvergelijking of besparing vastgesteld.

Officiële installatie/login/permissionbronnen tijdens uitvoering gericht geopend:
https://learn.chatgpt.com/docs/codex/cli, /docs/auth en /docs/permissions.
De eerdere /docs/security-bron blijkt Codex Security te behandelen; voor
CLI-sandboxgrenzen gebruikt de naslag de gerichte permissionsbron.
