# #49: overdrachten onderzoeken en controles uitvoeren

Status: C1 en C2 v1, voorstel vóór bouw. C0 en overdracht staan op
[issue #49](https://github.com/misja/agent-role-loop/issues/49).

## C1: triage

- Route: PLANNED, omvang M. Twee verbonden modules, afgebakend tot de acht
  bevindingen 8–15 uit #46; één reviewbaar tekstpakket.
- Proces- en normbasis: `a94218adbe2ee03eb6476582fbae5ab9e9ceca85`.
  Leesbare bronnen: `CLAUDE.md`, `core/loop.md`, contracten en rolprompts;
  `teaching/conventies.md`, `doelgroep.md`, `schrijfwijzer.md`, `begrippen.md`.
  Relevant: nieuwe toepassing van bekende principes, tekstfuncties, uitvoerbare
  instructies, onderbouwde claims, afnemende steun en controles bij tekstwerk.
- Afhankelijkheden: #46 en #48 staan Done; #53 is gemerged op deze basis.
  De eerste uitvoering van module 1 is beschikbare voorkennis. #49 staat Backlog
  bij de bordlezing. Er is geen eerder C4 voor dit werkitem.
- Uitvoerders: root orkestreert, onderzoekt, plant en bouwt na C4. Eén verse
  onafhankelijke reviewer `/root/review49` beoordeelt AC1–7, met expertise in
  onderwijslezing, rolcontracten en Python/pytest-verificatie. Hij ontvangt C5,
  exacte productversie, leesbare normen en besluiten, zonder maaktranscript.
  Geen afzonderlijke verhelderaar of inventarisatie: concrete bronbevindingen
  en onderstaande aanpak maken de keuzes toetsbaar voor het mensbesluit.
- Risico: uitleg weghalen kan noodzakelijke eerste steun verwijderen; voorbeeld
  kan worden verward met echte uitvoering; groen kan een algemene toolplicht
  suggereren. Behoud uitleg bij de handeling en benoem bewijsstatus.
- Herstelstand: ontwerp 0, oplevering 0; dit document en #49 bewaren de stand.
  Verbruik en bevindingen vóór herstel op #49 vastleggen; geen sessiereset.
- LIGHT-basis/afwijsadvies: niet van toepassing. C4 op dit concrete C2 is nodig
  vóór bouw; de mens beslist later afzonderlijk over merge.

## Summary

Module 2 bouwt voort op de begeleide uitvoering uit module 1 en toont één
overdrachtsanalyse met bron, versie, vereiste informatie en bewijsgrens.
Module 3 verklaart de betekenis van ingestelde controles in de les en laat
de student in de oefening eerst meten, vervolgens verklaren en gericht toetsen.
De bestaande casus blijft intact en biedt tevens de uitvoerbare terugvalroute.

## Goals

1. De student onderscheidt rolprompt, uitgevoerde handeling en bewaarde uitvoer,
   en kan ontbrekende informatie in een overdracht aanwijzen.
2. De student onderscheidt geslaagde asserties, gemeten regeldekking en een
   ingestelde minimumdrempel met eigen vastgelegde waarnemingen.
3. De eigen toepassing blijft uitvoerbaar met minder steun dan het voorbeeld,
   ook als eerdere eigen code ontbreekt.

## Non-goals

Geen nieuwe leeruitkomsten, casuscode, CLI-eisen, procesnormen, adapters,
providerkeuze, slides of toetsing. Geen volledige review uit module 4.
Geen studentvalidatie, echte LLM-run of gemeten duurclaim. Geen routinematige
screenshots. De praktijkbundel en module 1 worden niet herschreven.

## Current state

Module 2 les en oefening werken hetzelfde C2-P1-filtervoorbeeld uit. De kop
“rolprompts als implementatie” is stelliger dan de uitleg over feitelijke
uitvoering. De oefening vraagt bron/versie en ontbrekende gegevens, maar toont
die nog niet als volledig analysemodel. De Mermaid-naslag staat in de hoofdlezing.
De nieuwe module-1-pagina toont nu wél chatinvoer, werkelijk toe te passen code,
controles en bewaarde uitvoer, maar is uitdrukkelijk geconstrueerd.

Module 3 les en oefening geven beide de dubbele-uitleningsuitkomst en de
93%/95%-proef vooraf. De noteeropdracht voor de drempel staat onder “Uitleg”.
De eigen opdracht noemt linter/type-checker zonder setup-ingang. De terugval
vraagt zelf een zoekfunctie met test te bouwen, een zwaardere extra toepassing.
De aangeleverde casus bevat een bestaand defect en zes tests; Python vereist
ten minste 3.10 door de gebruikte typeannotaties. De casus mist CLI/opslag en
is dus geen volledige vervanging van de eerdere eigen boekenplank.

## Proposed approach

Gebruik de begeleide module-1-uitvoering als gerichte voorkennislink, zonder
haar voorbeeldwaarnemingen als feitelijke agentuitvoering te presenteren.
Behoud het beschikbare-boekenfilter als uitgewerkt analysevoorbeeld in de les.
Toon rolprompt/opdracht en een controle die de lezer zelf kan uitvoeren tegen
de meegeleverde code, met verwachte uitvoer en een apart waar te nemen resultaat.
De bronstatus van fictieve personen en contracten blijft zichtbaar. De analogie
wordt: contract als interface, rolprompt als instructie, handeling als uitvoering.
Een prompt is geen software-implementatie; modellen garanderen geen vaste uitkomst.

Het lesvoorbeeld krijgt een compact analysemodel: bron en versie, ontvanger,
contractvereiste, aangetroffen informatie, ontbrekende informatie en gevolg voor
de volgende handeling. De oefening verwijst daarnaar en vraagt twee eigen
analyses; verwijder de dubbele uitwerking. Mermaid blijft optionele, gerichte
naslag in een ingeklapte sectie met leesdoel, oorspronkelijke bron en status.

De les van module 3 houdt het onderscheid tussen assertie, coverage en
normkeuze, met een klein assertievoorbeeld. Zij geeft niet vooraf het volledige
defectantwoord of de meettabel van de oefening. De oefening bevat afzonderlijk:
voorbereiden, meten, waarnemingen bewaren, vergelijken met requirement 6,
verklaren en een gerichte assertie uitvoeren. Geef verwachte kenmerken waar
nodig voor setup, maar pas de volledige interpretatie na de meetopdrachten.
De drempelproef laat eerst exitcodes/dekking invullen; daarna volgt uitleg.
95% blijft een proefkeuze boven de gemeten lagere dekking, geen nieuwe norm.

Voor de eigen stack krijgt de opdracht gerichte officiële setup-ingangen voor
coverage, linter en beschikbare typecontrole. Python krijgt een concreet
commando-pad passend bij de bestaande uv-omgeving. Voor andere talen selecteert
de student eerst de gereedschappen voor zijn taal en legt configuratie en
commando vast; geen nieuwe verplichte taal. Controleer externe technische
aanwijzingen aan officiële documentatie vóór opname.

Bij ontbrekende eigen code gebruikt de student dezelfde casus in een nieuwe
kopie: eigen poortoverzicht en drempelkeuze, vervolgens een zelf uitgevoerde
gerichte assertie op behoud van de eerste lener. Geen zoekfunctie toevoegen.
De al bekende fout wordt geen onafhankelijke ontdekking genoemd; deze route
verifieert de betekenis en grens van bewijs, zonder zelfstandige transfer of
volledige eigen-codebeoordeling te claimen.

## Acceptance criteria

C0 AC1–7 blijven gelden. AC7 wordt toegepast volgens de geldende conventie en
de expliciete overdracht: inhoudelijke lezing, build en links; visuele controle
alleen bij vormgeving of een concreet weergaveprobleem. Dit voert geen normwijziging in.
Alle criteria gaan naar `/root/review49`.

| AC | Concrete controle en verwachte uitkomst |
|---|---|
| 1 | Module 2 lezing: prompt én uitvoerbare handeling aanwijzen; overeenkomst/grens van analogie en bron/versie/vereist/ontbrekend terugvinden. |
| 2 | Leesvolgorde: één uitgewerkt analysemodel; module 3 metingen vóór volledige verklaring; Mermaid alleen gerichte naslag. Eerste uitvoering houdt voorbereiding en verwachtingen. |
| 3 | Index/les/oefening verbinden groen aan ingestelde verplichte checks. Asserties, dekking en drempel zijn onderscheiden; 95% is gelabelde proefkeuze. |
| 4 | Noteerhandelingen staan als opdracht. Setup-ingangen zijn passend voor gekozen stack. Terugval is met bestaande code uitvoerbaar zonder nieuwe functie. |
| 5 | Reviewer voert één overdrachtsanalyse en één controle uit. Log bevat invoer, actie, verwachting, waarneming, versie/omgeving en bewijsgrens; afwezige informatie blijft ontbrekend. |
| 6 | Vergelijk indexleeruitkomsten op betekenis en casusbestanden bytegelijk met basis. Eigen analyses en eigen-codeopdracht behouden afnemende steun. Noodzakelijk inhoudelijk verschil eerst aan mens voorleggen. |
| 7 | Concrete normlezing; schone docs-build onder -W --keep-going, lokale links/fragmenten zonder fouten, diffcontrole. Bewijsgrenzen en herstelacties in onderzoek/49-uitvoering.md. |

## Basis and sources

Exacte proces-/normbasis staat in C1. Bronnen op die commit: de zes pagina's
onder `teaching/modules/02-begrijpen/` en `03-machine/`;
`teaching/modules/01-ervaren/eerste-uitvoering.md` en oefening deel B;
`teaching/cases/module3-boekenplank/`;
`teaching/cases/praktijk-projectomgeving/overdrachten.md`, code en controles.
Voor uitleg over context: `teaching/van-chat-naar-agent.md`.
Voor kwaliteitslagen: `teaching/kwaliteit-als-gedeelde-verantwoordelijkheid.md`.

Diagnose: `onderzoek/46-inventarisatie-en-plan.md`, bijlage modules 1–3,
bevindingen 8–15 en afhankelijkheden 3–5;
`onderzoek/46-inleidende-teksten-proef.md`, verdeling van uitleg;
`onderzoek/48-uitvoering.md` en de overdrachten op #49.
Historische regelverwijzingen uit #46 worden tegen de actuele basis gelezen.

## Repair state

Ontwerp 0, oplevering 0. Geen C3 geselecteerd of herstel uitgevoerd. Registratie
op #49 blijft leidend bij vervolgsessies; maximaal één automatische ronde per fase.

## Interfaces / contracts / data changes

Geen code-, data- of generieke contractwijziging. Tekstverwijzingen tussen les
en oefening worden samen bijgewerkt. De module-2-leeruitkomst kan concretere
woorden krijgen, maar behoudt het bestaande onderscheid en verantwoordingsniveau.

## Changes

### 1. Eén overdracht analyseren, daarna zelf toepassen

**Goal:** de student kan de afspraken en feitelijke uitvoering apart onderzoeken.
**Non-goals:** geen tweede volledige rollenketen of herbouw van de praktijkcasus.
**Files:** module 2 index.md, les.md en oefening.md.

**Implementation checklist:**

- [ ] Voeg gerichte voorkennislink naar module 1 toe en benoem het verschil
  tussen de CLI-opdracht en het in-memory-filtervoorbeeld.
- [ ] Toon één prompt/instructie, concrete controlehandeling en bewaarde uitvoer;
  onderscheid geconstrueerde roluitvoering van werkelijk gereproduceerde controle.
- [ ] Werk bron/versie/vereiste/ontbrekend één keer uit in de les.
- [ ] Begrens analogie; pas kop en organizer aan zonder leeruitkomst te veranderen.
- [ ] Maak Mermaid optionele naslag; behoud bron en unieke leesvraag.
- [ ] Laat oefening twee eigen analyses maken met herkenbaar resultaat; formuleer
  kosten/schaalvraag ook voor studenten zonder ervaren invullast.

**Verification plan:** manual-with-expected-results. Reviewer kiest één overdracht,
vult de analysevelden met vindplaatsen in, voert de getoonde controle uit en
registreert wat werkelijk is vastgesteld. Succes: geen ontbrekende uitvoerstap
of stilzwijgende voorkennis en de analogiegrens is aanwijzbaar.
Geen test-first voor proza; bestaande casuscontroles leveren uitvoerbewijs.
**Rollout/rollback:** les/oefening/index samen; revert van tekstpakket.
**Done when:** AC1/2/5/6 voor module 2 zijn onderbouwd.

### 2. Meten vóór verklaren, met uitvoerbare eigen route

**Goal:** de student kan gekozen checks uitvoeren en de uitslagen verantwoord lezen.
**Non-goals:** geen nieuwe toolplicht, casusfunctionaliteit of volledige review.
**Files:** module 3 index.md, les.md en oefening.md; onderzoeksregistratie.

**Implementation checklist:**

- [ ] Koppel noodzakelijkheid van groen aan de ingestelde vereisten.
- [ ] Verdeel conceptuitleg en volledige casusverklaring over les en oefening.
- [ ] Scheid setup, meetopdrachten, noteerhandelingen en verklaringen.
- [ ] Voeg stackgerichte setup-ingangen toe en controleer officiële bronnen.
- [ ] Maak terugval expliciet met bestaande casus en gerichte assertie.
- [ ] Registreer voor/na-bevindingen, uitgevoerde checks en grenzen in onderzoek.

**Verification plan:** manual-with-expected-results voor leesvolgorde en
validation-workflow voor bestaande casus. In een tijdelijke kopie: volledige
suite verwacht zes pass/100%/exit 0; selectie zonder terugbrengtest verwacht
vijf pass, lagere dekking/exit 0; dezelfde selectie met 95% verwacht vijf pass
en niet-nul exit. Gerichte assertie op eerste lener verwacht falen door
overschrijven. Registreer werkelijk gemeten percentages, versies en uitvoer.
Onafhankelijke reviewer reproduceert ten minste één hiervan zelf voor AC5.
Geen casuscode wijzigen of tests toevoegen aan de repository: bestaande
gedragingen en tijdelijke controle volstaan voor deze tekstwijziging.

Aanvullend: vergelijk casusbestanden tegen basis; lees behouden leeruitkomsten
en vaste lesstaarten; `make -C docs html` onder `-W --keep-going`; controleer
lokale links en fragmenten van gewijzigde pagina's en `git diff --check`.
Verwacht geen waarschuwingen, kapotte links of ongemotiveerde betekeniswijziging.
**Rollout/rollback:** samen met wijziging 1; revert van tekstpakket.
**Done when:** AC2–7 gedekt, exacte productcommit en bewijsgrenzen in C5.

## Risks

Uitkomsten staan ook in casuscommentaar; metingen vóór de uitleg garanderen
geen onbeïnvloede ontdekking. Benoem dit als leeractiviteit met zichtbaar bewijs,
geen experiment. De terugval hergebruikt een bekend defect en stelt minder
zelfstandige transfer vast. Externe setupdocumentatie kan veranderen; leg
raadpleegdatum en concrete bron vast. Agentlezing is geen studentvalidatie.

## Assumptions

De student heeft module 1 uitgevoerd en de voorbereiding gelezen; eigen code
kan ontbreken, waarvoor de terugval bestaat. De duurindicaties zijn niet
gevalideerd. Studentwaarnemingen en leereffect zijn niet beschikbaar.

## Open questions

C4: akkoord met dit tekstpakket, de verdeling tussen les en oefening en de
terugval via de bestaande casus? Deze terugval verandert geen leeruitkomst of
casusgedrag, maar haar bewijsgrens voor zelfstandige toepassing wordt expliciet.
Dit plan geeft nog geen bouw- of mergetoestemming.
