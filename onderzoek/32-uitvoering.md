# #32: Claude Code-adapter, lopende uitvoering

## Menselijk besluit en normbasis

[C4 PROCEED voor #32](https://github.com/misja/agent-role-loop/issues/32#issuecomment-6001713335)
registreert “akkoord” op [C2 v1](https://github.com/misja/agent-role-loop/issues/32#issuecomment-6001700750),
vastgelegd in `32-plan.md`. Norm-/procesbasis:
`b7aad138c18809c747a1e020590e0ad905903514`.
Root orkestreert/plant/bouwt; verse review32 krijgt later AC1–11.
Herstelstand #32: ontwerp 0, oplevering 0. Onafhankelijke #32-C6 nog niet beschikbaar; geen mergebesluit.

## Uitgevoerd tot de oefenpoort

Op 5–6 oktober 2026: negen wrappers krijgen `omitClaudeMd: true`; normen en
besluiten moeten expliciet mee. Het orc-commando benoemt dat, verse initial/
repair-contexten en het bewaren van artefacten vóór menselijke poorten.
Core is ongewijzigd. README/studentpad zijn concepten totdat de volledige
proef en onafhankelijke beoordeling zijn afgerond.

Installatiesnippets uit README werkelijk uitgevoerd op acht tijdelijke fixtures:
clean en existing installeren 30 bestanden met juiste hashes en rollen terug
zonder bestaande bytes te wijzigen. Wrappernaamconflict, bestaande orc-skill
en symlinkouder stoppen vóór schrijven. Een dangling orc-skill stopt eveneens vóór schrijven; een ongeldig directorypad
in het manifest laat rollback vóór enige verwijdering stoppen. Gewijzigd eigen bestand laat rollback
stoppen vóór enige verwijdering. Reproduceerbaar met
`python3 onderzoek/32-proef/controleer_installatie.py`;
observaties in `32-proef/installatie-resultaten.json`.
Geen bestaande installatie overschreven; daardoor geen backupherstel geclaimd.

Docs-build `make -C docs html` met -W --keep-going slaagt na herstel van één
fragmentverwijzing, log `/tmp/arl32-build.log`. Eerste sandboxpoging kon de
uv-cache niet openen; goedgekeurde herhaling uitgevoerd. Lokale linkcontrole
`/tmp/arl32-links.py`: 303 links/fragmenten inclusief inkomende verwijzingen,
nul fouten. Dit is tussentijds bewijs, geen volledige C5/C6.

## Echte Claude Code-planproef

Tijdelijke repository: `/tmp/arl32-smoke-p93pwtwx`.
Basiscommit: `33f88927165475fc2e6f8c513ef6f76741569969`.
Alleen minimale boekenplank, bestaande controles, expliciete PROJECT.md,
CLAUDE.md, C0 en adapter/core. Geïnstalleerde core bytegelijk aan normbasis;
wrappers/command zijn de ontwikkelversie, niet de ongemodificeerde broncommit.
Geen add-dir, geen GitHub-mutatie door Claude, geen privésleutel gebruikt voor
de oefencommit. De mens blijft de C4-besluitnemer; Codex bewaart artefacten.

CLI 2.1.289; accountstatus alleen op niet-identificerende velden gecontroleerd.
Live run gebruikt bestaand account, resolved model `claude-opus-5-5`, print-mode,
dontAsk, project settings, lege strikte MCP-config en alleen lees-/delegatietools.
Geen bypass. `/orc` staat in de geladen commandlijst; de orc-opdracht gaf C1
en een echte Agent-aanroep aan role-loop-planner, die C2 terugleverde.
Resultaat success; geen builder/reviewer gestart. Product en tests zijn
bytegelijk aan de basis. Tijdelijke ruwe uitvoer:
`/tmp/arl32-plan-run-live.jsonl`; niet integraal publiceren als reviewinvoer.
Beperkte technische registratie in `32-proef/plan-run.json`.

Eerste sandboxrun bleef bij netwerkretries zonder planresultaat en is gestopt.
Goedgekeurde netwerkrun slaagde. De daemononderbreking leverde geen eerdere
live run op; vóór hervatting bestanden/processen gecontroleerd.
Er wordt geen toets-, bouw- of herstelresultaat uit de planfase afgeleid.

C1/C2 exact bewaard in `32-proef/C1.md` en `C2.md` en bij de tijdelijke W1.
[Concreet oefenplan en voorgestelde C4-keuzes](https://github.com/misja/agent-role-loop/issues/32#issuecomment-6014171470):
controleer.py behouden; -B-variant toestaan tegen bytecodecache; gewone optionele
parameter; afgeleide AC5/AC6 met dezelfde reviewer. Oefentellers ontwerp 0,
oplevering 0. [Oefen-C4 PROCEED](https://github.com/misja/agent-role-loop/issues/32#issuecomment-6016426784)
legt het echte akkoord op C2 en V1–V4 vast; `32-proef/C4.md` bewaart de bron.

## Hoofdproef: bouw en onafhankelijke review

Echte Claude-bouwer gestart via Agent(role-loop-builder). Op de basis geeft de
volledige suite één pass en drie TypeErrors (exit 1); na de filterwijziging vier
passes (exit 0). De extra AC5/6-controle geeft eerst TypeError en daarna
`M1 True` / `M2 True True`. Codex heeft groen afzonderlijk bevestigd.
Productcommit: `fbab9c207dd1e08cef8d9566d49169c8c056895d`, alleen boekenplank.py.
Code, bestaande test en extra ondersteuning bewaard in `32-proef/`;
`build-run.json` bevat geselecteerde objectieve tooluitkomsten, geen maaktranscript.

Verse CLI-run met verse role-loop-reviewer-strict, geen fork/resume. Alleen
C5-kern, aangewezen normen/besluit en exact codecommit aangeboden; geen
planner-/bouwgesprek of ander oordeel. `review-run.json` bewaart delegatie-invoer,
gelezen paden en werkelijke testuitvoer; `C5-main.md` en `C6-main.md` de contracten.
Review: SHIP WITH NITS, alle S1–4 en AC5/6 nieuw onderzocht en pass.
Eigen hoofdproeftellers blijven ontwerp 0 / oplevering 0.

Niet-blokkerend vervolgpunt: AC5/6 zitten in ongetrackte oefenondersteuning en
beschermen het tijdelijke product later niet automatisch. Ondersteuning wordt
hier duurzaam bewaard; toevoegen aan producttests vergt een vervolgkeuze omdat
C4 de aangeleverde controle ongewijzigd houdt. Reviewer noemt ook truthiness
van het optionele argument en ontbrekend afzonderlijk contractveld als nits.
Geen reparatie nodig voor het bestaande akkoord.

Beperking: gecombineerde shellcommando's en een aanvullende python -c-check
werden door dontAsk geweigerd. De afzonderlijk toegestane suite en extra
controle draaiden wel. Geen bypass toegepast; de studentroute benoemt dit.
De reviewer onderzocht groen zelf; rood is eerder bouwbewijs, niet opnieuw
door hem gemeten. Boekobjecten worden gedeeld; onafhankelijke lijstcontainers
zijn de goedgekeurde AC6, geen diepe kopieën.

## Vervolg en bewijsgrenzen

Negatieve fixturecommit `2b24d15d00b34e43b1b2020675d6bffd9c0e82fa` is
expliciet geïnjecteerd uit de bestaande A-versie, geen spontaan modeldefect.
Codex: zwak drie pass/exit 0; volledig S4 FAIL/exit 1.
Verse Claude-review: BLOCK op S4 en volledige-groen-bewijs; S1–3 statisch
onderzocht met de S4-afhankelijkheid benoemd. Reviewer gebruikte een andere
commandovariant zonder toegestane -B en kon tests niet zelf uitvoeren;
geen heruitvoering geclaimd. `C6-negatief.md` bewaart dit exact.
Vóór de reparatie vastgelegd: NEG ontwerp 0, oplevering 1 verbruikt,
`negatief-herstelstand.json`, beide blockers en vóórcommit. Hoofdproef/#32
tellers blijven 0/0. Nu één begrensde bouwerreparatie plus verse repair-review.
De suggestie in de provideruitvoer om de reviewer te hervatten wordt niet
gevolgd; core schrijft een verse repair-context voor.

Echte bouwerreparatie: uitsluitend de opslagtoewijzing vervangen door een
teruggegeven selectie. Bouwuitvoer vóór herstel volledig S4 FAIL/exit 1 en
extra M2 assertion/exit 1; na herstel vier pass/exit 0 en M1/M2 groen/exit 0.
Herstelcommit `e96df75c919981123fa8728a6238afb87d91e823`; Codex bevestigt groen
op deze opgeslagen commit. Snapshot bytegelijk aan het goede hoofdproduct.
`repair-run.json`, `boekenplank-herstel.py` en `C5-herstel.md` bewaren bewijs,
exacte diff en expliciete repair-appendix. De bouwer kon eigen Git-inspectie
en versiemeting niet uitvoeren; Codex deed de commit/diffcontrole.

Verse repair-review geeft SHIP WITH NITS: beide blockers opgelost, S1–4
opnieuw onderzocht, volledige suite vier pass en aanvullende M1/M2 groen op
de exacte herstelcommit. Geen eerdere pass uitsluitend hergebruikt; rood bleef
eerder bewijs. `C6-herstel.md` en `recheck-run.json` bewaren oordeel en nieuwe
delegatie/testuitvoer. Niet-blokkerend vervolg: nummering na filteren plus
toevoegen alleen statisch onderzocht, geen gerichte regressiecontrole.
Beide reviewvervolgpunten staan in [#58](https://github.com/misja/agent-role-loop/issues/58)
op het projectbord, zonder nieuwe bouwvrijgave of blocker voor #32.

Hoofdproef en negatieve herstelproef gereed voor menselijk vervolg; onafhankelijke
#32-review nog afronden. Geen volledige afsluiting van #32. Oefenmerge en
adaptermerge blijven mensbesluiten.

Geen studentwaarnemingen, gemeten begrip/duur of tokenbesparing beschikbaar.
Geen productie-installatie, providerbenchmark, native GitHub-oefenreview of
integrale externe-linkaudit. Screenshots niet nodig voor dit tekstwerk.
