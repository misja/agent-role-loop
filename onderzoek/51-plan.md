# #51: eigen proces en praktijkvoorbeeld navolgbaar maken

Status: C1 en C2 v1, voorstel vóór bouw. C0 en overdracht:
[issue #51](https://github.com/misja/agent-role-loop/issues/51).

## C1: triage

- PLANNED, M: gerichte verduidelijking van module 6 en één praktijkhoofdstuk,
  één reviewbaar tekstpakket. Geen nieuwe providerarchitectuur.
- Proces-/normbasis: `9a89825f3de6aa3473e15cd8ec925a0d91b73cad`.
  Leesbare bronnen: CLAUDE.md, core/loop.md, rolprompts en contracten;
  teaching/conventies.md, doelgroep.md, schrijfwijzer.md, begrippen.md.
  Relevant: voortbouwen op eerdere uitleg, tekstfunctie, uitvoerbare stappen,
  onderbouwde claims, modulestramien en controles bij tekstwerk.
- Bord gecontroleerd: #46/#48/#49/#50 Done, #51 Backlog. Praktische
  overdrachts-, controle- en besluituitleg is gemerged. Geen bestaand C4 voor #51.
- Root orkestreert, onderzoekt, plant en bouwt na C4. Eén verse onafhankelijke
  reviewer `/root/review51` voor AC1–7: onderwijslezing, procescontracten,
  bewijs-/versieketen en technische controle. Geen criteria elders.
  Reviewer krijgt C5-kern, exacte productcommit, normen en besluiten zonder
  maaktranscript of andere oordelen.
- Geen aparte verhelderaar/inventarisatie: huidige passages en vier
  bronbevindingen geven voldoende afbakening voor dit concrete plan.
- Risico: opsplitsen kan een tweede procesroute maken; weglaten van een controle
  kan een bestaande verplichting suggereren te mogen overslaan; naslag kan als
  verplichte voortzetting worden gelezen. Behoud core als routingbron en
  benoem de geldende afspraken bij elke voorbeeldkeuze.
- Herstelstand ontwerp 0, oplevering 0; dit document en #51 bewaren de stand.
  Vóór herstel teller en criteriumbevindingen op #51 vastleggen.
- LIGHT-basis/afwijsadvies niet van toepassing. C4 vereist op concreet C2 vóór
  bouw, en apart menselijk mergebesluit na onafhankelijke review.

## Summary

Maak de route-, bouw-, review- en mergebeslissingen van module 6 afzonderlijk
vindbaar met hun invoer, eigenaar en bewaarde uitvoer. Het praktijkhoofdstuk
krijgt gerichte ingangen voor bronmapping en sessie-invoer; verhuizing en
historie zijn herkenbare naslag. De student blijft zelf ontwerpen en afwegen.

## Goals

1. De student kan op ieder beslismoment bepalen wie handelt, wat meegaat en
   welke versie of beslissing wordt bewaard.
2. De student kan een bewust weggelaten controle verantwoorden en de resterende
   vraag toewijzen aan beoordeling.
3. Een lezer kan één criterium door de volledige keten volgen en ontbrekend
   bewijs aanwijzen zonder maakgeschiedenis te reconstrueren.

## Non-goals

Geen code, cases, zipbundel, core/adapters, slides, toetsing of providerkoppeling.
Geen nieuwe verplichte stack, volwaardige GitHub-/Codeberg-migratie of echte
agentrun. Geen tweede volledige begeleide uitvoering naast module 1.
Geen gemeten duurclaim, studentvalidatie of routine-screenshots.

## Current state

Module-6-oefening stap 4 bundelt C1, routes, plannen, planreview en mensbesluit;
stap 6 bundelt initial review, synthese/arbitrage, herstel, merge en status.
C5-kern/herstelbijlage hebben bij die handelingen geen directe contractlink.
De les vraagt weglatingsredenen maar toont alleen een formattervoorbeeld.
Module-index, les en oefening linken bronmapping/beginstappen/exporttabel naar
het hele praktijkhoofdstuk.

Het praktijkhoofdstuk introduceert W1, P1 en C0/C1/C2/C4/C5/C6 tegelijk in de
eerste tabel. De sessie-invoertabel staat los van de eigen beginstappen.
Verhuizing/export en echte historie volgen na GitHub-afronding zonder expliciete
naslagroute. De opening verwijst voor model/agent/rol naar de oriënterende
inleiding, terwijl die uitleg nu in `van-chat-naar-agent.md` staat. Die
voorbereiding bevat de gevraagde sessie-invoer en overdracht al; de manual
adapter blijft ongewijzigd, met een geregistreerde grens van zijn oude leesadvies.

## Proposed approach

Tekstfunctie module-index: oriënteren; korte gerichte links zonder extra uitleg.
Les: één weglatingsafweging toevoegen bij projectnormen. Voorbeeld: een kleine
in-memory-interface zonder nieuwe externe afhankelijkheden of echte gegevens,
waar geen bestaande norm een dependencyscan verplicht stelt. Een scan voor
nieuw toegevoegde dependencies kan daar achterwege blijven; de beoordelaar
onderzoekt nog steeds invoerafhandeling, aanroepen en passende foutmeldingen.
Dit zegt niets over kwetsbaarheidsvrijheid en laat geen reeds verplichte scan
vervallen. Behoud de bestaande afwegingen voor stijl/types/lint/formattering.

Oefening: behoud de zes hoofdactiviteiten, drie basiskeuzen, terugval, eigen
scope en dossier. Splits binnen stap 4 in herkenbare onderdelen: C1 vastleggen,
route uitwerken, geselecteerd C2/C3 ontvangen, menselijk C4 waar vereist,
bouwvrijgave controleren. Benoem per onderdeel eigenaar, invoer en uitkomst.
Bij REJECT eerst verduidelijken/splitsen; LIGHT houdt eigen C4-grenzen.

Splits stap 6 in: onafhankelijke invoer samenstellen, C6's verzamelen en op
commit bewaren, eindoordeel bepalen (één C6 of passende C7), blokkadepad,
mensenbesluit en afronding. Initial reviewers krijgen geen maaktranscript of
andere initial oordelen. Bij blokkade staan ter plekke tellers, één ronde,
verse repair-review en expliciete herstelbijlage; geen reset of verdwenen
blocker. Planherstel hoort bij de eventuele C3-blokkade in stap 4.

Praktijkhoofdstuk: expliciete MyST-labels bij bronmapping, sessie-invoer,
beginstappen en exporttabel. Gebruik die links vanuit module 6 en vanuit de
praktijkbeginstap voor planner/bouwer/reviewer. Licht codes bij eerste gebruik
compact toe, met contractlinks; W1 is opdracht, P1 planversie, A/B zijn
bestandslabels en geen SHA. Maak verhuizing/export en projecthistorie twee
optionele naslagroutes met eigen leesdoel, zonder nuttige inhoud te verwijderen.
Corrigeer de voorbereidinglink naar de bestaande uitlegpagina en geef gerichte
vindplaatsen voor rol en overdracht. Geen wijziging aan manual adapter of
voorbereiding buiten de C0-scope; registreer zijn verouderde leesadvies als grens.

## Acceptance criteria

C0 AC1–7 behouden, allemaal naar `/root/review51`. AC7 wordt toegepast volgens
huidige conventie: inhoud/doelgroep/leesvolgorde, build en links; visuele controle
alleen bij vormgeving of een concreet weergaveprobleem.

| AC | Controle en verwachte uitkomst |
|---|---|
| 1 | Stap 4/6 hebben vindbare beslismomenten met eigenaar, invoer en uitkomst; directe C1/C5/C6-links en begrensd herstel bij de betreffende blokkade. |
| 2 | Les geeft een gemotiveerde weglating onder expliciete voorwaarden en concrete resterende reviewvraag, zonder verplichte controles te annuleren. |
| 3 | Gerichte bronmapping-/sessie-/exportlinks werken; codes bij eerste gebruik verklaard; verhuizing en historie als afzonderlijke naslagroutes. |
| 4 | Reviewer volgt S4 in het uitvoerbare praktijkvoorbeeld via W1/P1/C4, A/B, controles, C5/C6 en mensbesluit. Hij registreert ontbrekende echte run/commit/besluitbronnen en verricht ten minste één controle zelf. |
| 5 | Drie basiskeuzen, terugval, eigen ontwerp en zes dossierpunten behouden; geen providerarchitectuur toegevoegd. |
| 6 | Indexleeruitkomsten op betekenis vergeleken; casuscode/bundel bytegelijk; eigen afweging en afnemende steun behouden. Noodzakelijk inhoudelijk verschil eerst voorleggen. |
| 7 | Normgerichte leesvragen met passages; schone -W --keep-going-build, lokale links/fragmenten, diffcontrole. Bewijsgrenzen en herstelregistratie in onderzoek/51-uitvoering.md. |

## Basis and sources

Normbasis staat in C1. Gelezen product op die commit: module 6 index/les/oefening;
teaching/praktijk/van-werkitem-naar-pull-request.md; van-chat-naar-agent.md;
adapters/manual/README.md. Diagnoses: onderzoek/46-inventarisatie-en-plan.md,
bijlage modules 4–6 bevindingen 7–10, en onderzoek/46-inleidende-teksten-proef.md.
Overdracht op #51 en onderzoek/36-module-redactie.md voor casusbronbegrenzing.

Voorkennis: module 1 eerste-uitvoering.md (invoer en mensbesluiten), module 2
analysemodel (bron/versie/ontbrekend), module 3 (controles/bewijsgrenzen),
modules 4–5 (synthese/arbitrage, voorwaarden/uitstel). Het praktijkvoorbeeld
wordt ook eerder gebruikt; het behoudt daarom zijn zelfstandige voorbereiding.
Normatieve bronnen: core/loop.md en C1/C2/C3/C4/C5/C6/C7-contracten.

## Repair state

Ontwerp 0, oplevering 0; geen C3 geselecteerd of herstel gestart. Nieuwe sessie
reset deze stand niet. Registratie op #51 is persistent.

## Interfaces / contracts / data changes

Geen. Alleen tekststructuur en interne linklabels. Inhoudelijke samenhang tussen
module-6-links en praktijkingangen wordt in hetzelfde pakket onderhouden.

## Changes

### 1. Zelfstandige beslismomenten en controlekeuze

**Goal:** de student organiseert de uitvoering en verantwoordt eigen keuzes.
**Non-goals:** geen ingevuld eigen ontwerp of tweede module-1-keten.
**Files:** module 6 index.md, les.md, oefening.md.

**Implementation checklist:**

- [ ] Voeg concrete weglatingsafweging toe, met geldende norm en reviewgrens.
- [ ] Splits stap 4/6 intern met eigenaar/invoer/uitkomst en directe contractlinks.
- [ ] Zet plan-/opleveringsherstel bij de betreffende blokkade, inclusief tellers.
- [ ] Behoud basiskeuzen, criteria/dossier, individuele mensrol en eigen afweging.
- [ ] Maak praktijkverwijzingen gericht.

**Verification plan:** manual-with-expected-results. Reviewer doorloopt één
PLANNED-criterium op papier van C0 tot review/mensbesluit en beschrijft daarnaast
waar LIGHT/REJECT afwijken. Verwacht juiste invoer, passende bevoegdheid, behoud
van blocker/herstelgrens en geen onbenoemde voorkennis. Hij wijst bij weglating
normvoorwaarde en resterende beoordelingsvraag aan. Geen test-first voor proza;
er verandert geen codegedrag.
**Rollout/rollback:** tekst en ingangen samen aanbieden; revert documentatiepakket.
**Done when:** AC1/2/5/6 inhoudelijk gedekt.

### 2. Vindbare praktijkketen en naslag

**Goal:** de lezer kan een criterium en de geldende bronnen zelfstandig volgen.
**Non-goals:** geen echte platformverhuizing, nieuwe agentkoppeling of bundlewijziging.
**Files:** praktijkhoofdstuk en onderzoek/51-uitvoering.md.

**Implementation checklist:**

- [ ] Label bronmapping/sessie-invoer/beginstappen/exporttabel expliciet.
- [ ] Verklaar documentcodes bij eerste gebruik; behoud historische versies/labels.
- [ ] Link plannerstap naar sessie-invoer en voorbereiding naar bestaande uitleg.
- [ ] Markeer verhuizing en historie als aparte optionele naslag met leesvraag.
- [ ] Registreer S4-ketentoets, eigen controles en ontbrekende gegevens.

**Verification plan:** manual-with-expected-results voor S4-keten; reviewer
wijst eis, gekozen controle, planbesluit, A-blokkade, B-herstelbewijs en fictief
mensbesluit aan. Validation-workflow: bestaande controleer.py op A zwak verwacht
3 pass/exit0; A regressie verwacht 1 fail/exit1; B volledig verwacht 4 pass/exit0.
Reviewer reproduceert minstens één hiervan, vermeldt omgeving/versie en grenzen.
Controleer beschermde case-/zipdiff leeg, betekenis leeruitkomsten en dossier
behouden; make -C docs html onder -W --keep-going, lokale HTML-links/fragmenten
van gewijzigde pagina's en inkomende verwijzingen, git diff --check.
Verwacht geen waarschuwingen, kapotte links of ongeoorloofde betekeniswijziging.
Geen nieuwe repositorytests, screenshotcontrole of studentbegripsclaim.
**Rollout/rollback:** samen met wijziging 1; revert tekstpakket.
**Done when:** AC3/4/7 gedekt; C5 bevat exacte commit en objectief bewijs.

## Risks

Meer koppen kunnen de zelfstandige oefening fragmenteren: behoud zes
hoofdactiviteiten en zet details bij hun beslismoment. Praktijk is een ander
in-memory-filtervoorbeeld; de student moet eigen code/criteria gebruiken,
geen voorbeeld-SHIP of fictief akkoord overnemen. Screenshots bewijzen geen
leesbegrip; onafhankelijke agentlezing blijft begrensd.

## Assumptions

De student heeft modules 1–5 gevolgd voor module 6; het praktijkhoofdstuk mag
na module 2 al worden gelezen. Oefenduur, studentwaarnemingen en leereffect
zijn niet beschikbaar. Technische reproductie gebeurt op bestaande bundelcode.

## Open questions

C4: akkoord met dit tekstpakket, de interne opsplitsing van stap 4/6, het
weglatingsvoorbeeld en de gerichte praktijk-/naslagroutes? Geen nieuw doel,
leeruitkomst of casusgedrag voorgesteld. Nog geen bouw- of mergevrijgave.
