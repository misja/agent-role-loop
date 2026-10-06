# #32: Claude Code installeren en één wijziging uitvoeren

## C1: route, basis en verantwoordelijkheden

- C0: [#32](https://github.com/misja/agent-role-loop/issues/32); eerstvolgende
  adapter volgens de werkvolgorde van #28. Bord gecontroleerd op 5 oktober
  2026: #29/31/35/36/37/46/48–52 afgerond; adapters #32–34 nog Backlog.
- Route PLANNED, omvang M. Bestaande wrappers en commando zijn het vertrekpunt;
  installatie, rechten en werkelijke provideruitvoering vragen concrete keuzes.
- Proces/normbasis: `b7aad138c18809c747a1e020590e0ad905903514`.
  Leesbaar: CLAUDE.md, core/loop.md en contracts/, teaching/conventies.md,
  doelgroep.md, schrijfwijzer.md en begrippen.md.
- Root orkestreert, onderzoekt, plant en bouwt. Eén verse onafhankelijke
  reviewer `review32` toetst AC1–11: technische installatie/rechten,
  contractisolatie en leesbaarheid van het hoofdpad.
- Geen aparte C3 of inventarisagent. Het werk blijft bij één kopieeradapter,
  één bestaand klein voorbeeld en de expliciete proeven hieronder.
- Herstelstand #32: ontwerp 0, oplevering 0; blijvend vastleggen op #32 en
  in onderzoek/32-uitvoering.md. De oefenrun heeft een eigen register/tellers.
- C4 vereist op dit C2 v1 vóór bouwen. Geen eerdere bouwvrijgave voor #32.
  Ook de latere merge vraagt een menselijk besluit.
- Risico's: instructies en bevoegdheden kunnen uit bestaande projecten worden
  geërfd; Bash in een wrapper is geen technische garantie van alleen lezen.
  Geen wijziging van core, doelgroep of route. LIGHT/REJECT niet van toepassing.

## C2 v1: samenvatting en doelen

Werk de bestaande Claude Code-kopieerinstallatie uit tot een begrensde route:
eerst projectafspraken inventariseren, dan uitsluitend eigen adapterbestanden
toevoegen, de installatie controleren en één wijziging aan de boekenplank in
een tijdelijke Git-repository uitvoeren. Bewaar echte versies, artefacten en
controles; toets onafhankelijke review en een gerichte reparatie daadwerkelijk.
Maak een Nederlandstalig studentpad naast Engelse technische adapternaslag.

1. Bestaande instructies/configuratie behouden en installatie/rollback aantonen.
2. Tool, modelaanbieder, projecttoegang en verse rolcontexten herkenbaar maken.
3. Hoofdpad en negatieve herstelproef uitvoeren met werkelijke Claude Code,
   met gescheiden bewijs voor tooling, agentlezing en studentwaarneming.

Geen nieuw orkestratieframework, nieuwe SDK/API-client, modelbenchmark,
productie-installatie of providerwissel. Geen installatie in deze repository
of wijziging van globale accountinstellingen. Geen credentials publiceren.

## Huidige stand en bronnen

`adapters/claude-code/` bevat negen wrappers en `commands/orc.md`. Core wordt
meegekopieerd naar `.claude/agent-role-loop/core/`. README heeft een compacte
kopieerinstructie, maar geen conflictinventaris, concrete eerste werkroute of
uitgevoerde platformrookproef. Reviewwrappers hebben Bash-toegang; de tekstuele
leesbeperking is geen bestandsbeveiliging.

Lokaal beschikbaar op 5 oktober: Claude Code 2.1.289; authenticatiestatus meldt
ingelogd via claude.ai, firstParty, Pro. Alleen deze statusvelden geraadpleegd;
geen accountidentiteit of credentials geregistreerd. Modeluitvoering en
quotumruimte zijn nog niet geverifieerd. CLI-aanwezigheid is geen rookproef.

Officiële bronnen gericht geopend:
[subagents](https://code.claude.com/docs/en/sub-agents),
[commands/skills](https://code.claude.com/docs/en/slash-commands),
[permissions](https://code.claude.com/docs/en/permissions),
[CLI](https://code.claude.com/docs/en/cli-reference).
Niet-forkende rollen zijn het uitgangspunt; projectinstructies kunnen wel
meekomen. Daarom audit van de instructies die automatisch laden, geen claim
dat een eigen context uitsluitend het overdrachtsbericht bevat.
Bij uitvoering actuele CLI/documentatie opnieuw vergelijken waar nodig.

Verder: `onderzoek/31-projectomgeving.md`, `51-uitvoering.md`, gedeeld
praktijkhoofdstuk en `teaching/cases/praktijk-projectomgeving/`. De historische
fictieve beoordelingen/mensbesluiten uit de bundel zijn geen echte runinvoer
of toestemming voor deze proef.

## Aanpak en tekstontwerp

Technische adapternaslag blijft Engels, zonder onderwijsstramien. Het nieuwe
studentpad in `teaching/praktijk/claude-code.md` volgt na module 2 en het
gedeelde praktijkhoofdstuk. Voorkennis: terminal, Git en Python-tests uit de
opleiding; model/agent/rol/sessie/overdracht via `van-chat-naar-agent.md`.
Nieuw: Claude CLI starten, projectinstructies vinden, rolbestanden installeren,
toolrechten herkennen en een onafhankelijke opdracht laten uitvoeren.
Leg deze toepassingen uit bij de handeling die ervan afhankelijk is.

Iedere stap vermeldt voorbereiding/invoer, uitvoerend programma, handeling,
reden en herkenbare uitkomst/fout. Benoem account en installatie als vereisten,
met officiële installatie-/loginverwijzing; geen stille aanname van toegang.
De mens beheert installatie en Git-bewaring. Claude leest/wijzigt alleen binnen
de afgesproken proef en ontvangt de juiste contractinvoer. De instructie
onderscheidt het mogen uitvoeren van een tool van een menselijk planbesluit.

### Installatie en rechten

Behoud de bestaande kopieerroute; geen algemene installer nodig. Maak een
manifest van alleen eigen `role-loop-*`-wrappers, `orc` en de meegeleverde core.
Inventariseer vooraf CLAUDE/AGENTS/rules, commands/skills, settings/hooks/MCP,
testcommando's en naamconflicten. Bij conflict stoppen of gerichte backup met
herkomst; nooit bestaande agentmappen of projectafspraken overschrijven.
Rollback verwijdert uitsluitend manifestbestanden en herstelt een eventuele
backup. Controleer hashes/instructies vóór en na op tijdelijke fixtures.

Nieuwe sessie na installatie, geen fork/resume voor initial reviewers en
repair-reviewers. Geldige normversies/besluiten gaan expliciet mee. Geen
auteursnarratief in automatisch geladen projectinstructies. Waar beschikbaar
toolsets voor rollen beperken; Bash-commando's voor reviewer specifiek
toestaan voor inspectie/tests. Geen bypassPermissions als hoofdpad.
Leg de grenzen van geërfde rechten en promptregels expliciet vast.

### Werkelijke rookproef en gerichte reparatie

Een tijdelijke Git-repository onder /tmp met alleen de minimale boekenplank,
controleer.py, eigen projectafspraken en gekopieerde adapter. Geen toegang tot
een productierepository via add-dir. Geen GitHub-mutatie vanuit Claude.
Werkiteminhoud komt uit het gedeelde filtervoorbeeld; verwijzingen naar echte
issue-/PR-bronnen worden gelezen of als complete Markdown aangeleverd wanneer
de tool geen trackertoegang heeft. De gekozen hoofdroute gebruikt lokale
contractbestanden en Git-commits; geen fictieve native review/PR publiceren.

Voer de standaardwijziging met echte Claude-roluitvoering uit: C0 ophalen,
C1 route/criteria, C2 bij PLANNED, C4, bouwer/C5, verse reviewer/C6 en terugkoppeling.
Bewaar uitvoerende tool/modelidentificatie, invoer, codecommit, commando's,
verwachte en waargenomen uitvoer en geïsoleerde delegatie. Bij een werkelijk
gegenereerd PLANNED-plan volgt C4 op dat concrete plan vóór bouwen; dit
adapterplan is geen voorafgaand akkoord op een nog onbekend oefenplan.
Toon het concrete oefenplan dan aan de gebruiker. Bestaand toepasbaar besluit
wordt met bron meegenomen en niet opnieuw gevraagd.

Verwacht S1–S4: standaardvolgorde behouden; beschikbaar filter in volgorde;
lege/volledig uitgeleende plank geeft leeg; filtering behoudt boeken/status.
Gedragswijziging gebruikt test-first: ontbrekend filter eerst rood, implementatie
daarna groen. De bestaande controletest mag doelgericht worden hergebruikt.

Voor gegarandeerde hersteldekking mag daarnaast de bestaande opzettelijk
defecte A-versie als gelabelde negatieve fixture worden aangeboden met echte
C5-uitvoer en de S4-eis. Laat een verse Claude-reviewer de afwijking onderzoeken:
verwacht BLOCK met concrete S4-bron. Registreer vóór reparatie de eigen
opleveringsteller 1; laat de bouwer herstellen, bewaar rood/groen en diff,
en start een verse repair-reviewer met expliciete bijlage. Geen injectie als
spontaan modeldefect presenteren; geen extra ronde verlenen aan de hoofdopdracht.
Oefenrun stopt na SHIP voor een afzonderlijk menselijk mergebesluit.

## Acceptatiecriteria, toewijzing en verificatie

C0 AC1–11 behouden; allemaal aan review32:

| AC | Verwachte controle/uitkomst |
|---|---|
| 1 | Wrappers/command/core coherent; geselecteerde CLI laadt de installatie en voert rollen uit. |
| 2 | Inventaris/manifest aanwezig; schoon-, bestaande-config- en conflictfixture; backup/rollback behouden bestaande bestanden bytegelijk. |
| 3 | Tool/provider/project afzonderlijk, herkomst geladen instructies bekend; echte verse review-invoer en taakrechten geregistreerd. |
| 4 | Werkelijke wijzigingsketen en negatieve herstelproef, echte controle-uitkomsten/commits, geldig mensbesluit waar vereist; geen bundelfictie als live bewijs. |
| 5 | Per stap invoer/handeling/uitkomst, credentials buiten materiaal/logs, uitsluitend tijdelijk voorbeeldproject. |
| 6 | Datum/CLI/resolved model en uitgevoerde handelingen geregistreerd. Hoofdpad niet uitgevoerd betekent geen volledig getest SHIP/afsluiting. |
| 7 | Core ongewijzigd; geen afwijkende contractkopie; doc-links/build -W --keep-going schoon. |
| 8 | Studentpad en technische naslag onderscheiden; normdoelgroep expliciet. |
| 9 | Nieuwe handelingen en eerdere uitleg bij eerste gebruik vindbaar. |
| 10 | Zelfstandige staplezing wijst uitvoerder, toegang, reden en herkenbare uitkomst/fout aan. |
| 11 | Onafhankelijke technische/inhoudelijke hoofdpadlezing, concrete ontbrekende invoer/kennis en herstel; geen studentvalidatie claimen. |

## Wijzigingen

1. Adapter README/commands/agents gericht bijwerken. Testmodel validation-workflow
   voor installatiefixtures/contractpaden/rechten; tekst manual-with-expected-results.
   Geen test-first voor tekst/config zonder nieuw softwaregedrag.
2. Studentpad en directe praktijkingang toevoegen. Bestanden
   `teaching/praktijk/claude-code.md` en gerichte navigatie in teaching/index.md
   en/of praktijkhoofdstuk; geen modules herschrijven.
3. Onderzoek/32-uitvoering.md: bronversies, echte runartefacten, beperkte
   reproduceerbare bewijsbestanden waar nuttig. Providertranscripts niet integraal
   publiceren; de reviewer krijgt C5-kern en noodzakelijke uitvoeringsbewijzen.

Gereed wanneer alle criteria aantoonbaar pass en onafhankelijke C6 beschikbaar.
Build/linkcontrole plus beschermde diff voor core, andere adapters, modules en
casusbundel. Geen standaard screenshots. Terugdraaien: eigen wijzigingscommit;
proefinstallatie via gecontroleerd manifest, geen globale instellingen wijzigen.

## Risico's, aannames en open besluiten

Authenticatie/quotum kan uitvoering blokkeren; dan ontbrekende stap registreren,
geen documentatiecontrole als providerproef aanmerken en geen volledige afsluiting.
Model kiest de bestaande accountconfiguratie; registreer werkelijk resolved ID,
geen nieuw abonnement of vaste modelkeuze afleiden. Geen studentmeting beschikbaar.
Planfase en uitvoeringsproef kunnen een noodzakelijke concrete permissiegoedkeuring
vragen; bestaande toestemming blijft gelden binnen haar scope.

C4-vraag: deze begrensde adapteruitvoering vrijgeven? Een nog te genereren
oefen-C2 en het uiteindelijke merge blijven afzonderlijke concrete besluiten.
