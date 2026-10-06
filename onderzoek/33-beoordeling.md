# C6 INITIAL #33 — SHIP

Reviewer: review33, onafhankelijke strikte technische en didactische beoordelaar. Eén geselecteerde beoordelaar, alle AC1–11; geen criteria elders toegewezen. Dit C6 is final volgens core/loop.md. SHIP betekent gereed voor het afzonderlijke menselijke mergebesluit.

## Artefact, invoer en grondslag

Nieuw onderzochte productcommit `e51f2dee0ba60a3bab1704bea024be55e298f0d6`, exacte diff vanaf `a9864c8a0b8cc0acab38d31d47a4582e0886966f`. Exclusieve #33-C5-invoer: `/tmp/arl33-c5.md`. Geen maaktranscript of ander #33-oordeel gelezen. De C6-bestanden van de boekenplankproef zijn onderzochte AC4-productresultaten, geen collega-oordelen over #33.

Via AGENTS.md eerst CLAUDE.md gelezen; daarna core/loop.md, reviewer-strict.md, C5/C6-contracten en teaching/conventies.md, doelgroep.md, schrijfwijzer.md en begrippen.md. Eigen bytecontrole bevestigt alle negen grondslagbestanden op de pinned basis. Geen andere route of nieuwe norm toegepast. #33 C0 en C4 zijn gericht read-only bij GitHub opgehaald. C4-comment6017668277 geeft PROCEED op plan6017597771 inclusief concrete oefenkeuzes, geen mergevrijgave. C4.md bewaart vergelijking met de werkelijke planner-C2 en verklaart het verschil in naam van het verificatiemodel, met ongewijzigde verplichte rood/groen-uitvoering. #33 ontwerp0/oplevering0; dit is INITIAL, geen repair-appendix.

Alle 43 gewijzigde bestanden komen bytegelijk overeen met de reviewcommit. Diff bevat alleen de opgegeven Codex-adapter, studentroute/navigatie en #33-plan/bewijs. Gedeelde core, bestaande adapters en casusbron blijven behouden.

## Criteriadekking

Alle onderstaande dekking is **nieuw onderzocht**. Geleverde historische modelruns zijn als productbewijs beoordeeld; zij zijn geen door deze reviewer opnieuw uitgevoerde providerproeven.

| AC | Resultaat | Concrete basis |
|---|---|---|
| 1 | pass | entry.md en role-task.md verwijzen naar bestaande core/rollen/contracten. README gebruikt gewone projectbestanden en afzonderlijke exec-aanroepen. plan/build/review JSON hebben verschillende thread-ID's; geen resume/fork. Geen rechten ontleend aan Claude-configuratie. |
| 2 | pass | README beschrijft inventaris, coherent kopiëren, manifest, gerichte handmatige AGENTS-verwijzing en afzonderlijk terugdraaien daarvan. install.py preflight weigert bestaande bestemming/onveilige paden; rollback controleert eigendom en alle hashes vóór verwijderen. Eigen acht fixtures slagen, bestaande AGENTS/CLAUDE/configbytes behouden, 23 gekopieerde bestanden geverifieerd. |
| 3 | pass | README en studentintro onderscheiden aanbieder, uitvoerend programma en repository. Sandbox is expliciete schrijfgrens; vers gesprek verwijdert geen geladen instructies of toegankelijke bestanden. Roltaak bevat readable bronnen/normversies, volledige lokale opdracht bij onbereikbare URL en menselijke Git/trackerverantwoordelijkheid. |
| 4 | pass | C0/C1, echte C2, concrete C4-vergelijking, builderrood/groen, exact commit, verse initial C6 SHIP en lokale terugkoppeling zijn aanwezig. Eerste incomplete review stopte zonder verdict/criteria/tests; gecorrigeerde C5 kreeg een nieuwe thread. Afzonderlijke negatieve fixture heeft eigen BLOCK B1[S4], NEG0/1 vastgelegd vóór reparatie, rood/groen-repair en verse REPAIR C6 met expliciete appendix. Eigen snapshots komen overeen met alle drie Git-commits en reproduceren groen/rood/groen. |
| 5 | pass | Voorbereiding en stappen1–7 geven concrete commando's/handelingen, herkenbare resultaten en fouten. Rookproef gebruikt tijdelijke oefenrepository. Gepubliceerde selecties bevatten geen credentials/accountidentiteit; raw providertranscripten blijven buiten publicatie. |
| 6 | pass | Datum6 oktober2026, CLI0.160.0, aparte defaultheader gpt-6.1-sol en expliciet modelgepinde latere runs staan met configuratie/commandexit/testresultaten vast. Plan/build-JSON heeft geen per-invocation resolved modelveld; apart headerbewijs wordt uitdrukkelijk niet daarmee gelijkgesteld. Hostinitialisatieprobleem, ontbrekende native externe acties en grenzen worden onderscheiden. Hoofdpad is werkelijk uitgevoerd. |
| 7 | pass | Geen core-/oude-adapter-/casuswijziging; 20 installed-corehashes zelfstandig vergeleken met de normcommit. Eigen docs-build met -W --keep-going exit0 en 306 lokale links/fragmenten inclusief inkomende navigatie zonder fouten. Didactische normlezing hieronder. Exacte diff--check heeft de expliciet hieronder beschreven uitzondering in een bewijsfence; geen inhoudelijke whitespacefout. |
| 8 | pass | README benoemt technische installatie/onderhoud en wijst student naar Nederlands pad. Studentroute noemt module2/gedeelde praktijk, terminal/Git/Python en voorbereiding over model/programma/sessie/rol. Geen stilzwijgende agentervaring boven het vastgestelde startniveau vereist. |
| 9 | pass | 33-plan tekstontwerp benoemt voorkennis en nieuwe toepassing. Studentstappen verklaren AGENTS/override, rolinvoer, exec/stdin/output, read-only/workspace-write/approval, echte commanduitvoer en commitbinding bij eerste gebruik. Voorbereiding en eerdere gedeelde route zijn vindbaar. |
| 10 | pass | Invoer, handeling, uitvoerder, toegang, reden en uitkomst zijn per stap concreet afleidbaar; zie leesgang. Tooling/accountvoorwaarde en falende modelaanroep worden vóór afhankelijk gebruik behandeld. Roltaakplaceholders vragen exacte leesbare invoer en beslissingen. |
| 11 | pass | Deze onafhankelijke agentlezing doorloopt hieronder voorbereiding en alle zeven stappen tegen de aangeboden voorkennis. Geen concrete uitvoerblokkerende begripsprong gevonden. Technische rookproef, agentlezing en ontbrekende studentwaarneming worden expliciet onderscheiden. |

## Onafhankelijke hoofdpadlezing

Dit is een agentlezing, geen studentproef of meting van begrip.

Voorbereiden: het herkenbare probleem is dezelfde boekenfilterwijziging uit de gedeelde praktijk uitvoeren met afzonderlijke Codex-aanroepen. Student krijgt Python3.10+, Git, CLI/account/modeltoegang als voorwaarden, versie/logincommando's en basiscontrole. Codex voert model/toolhandelingen uit, Python voert de test uit, student bewaart de basis met bekende Git-werkwijze. Geslaagde basiscontrole is herkenbaar; login bewijst geen modeltoegang. Account- en CLI-installatie zijn gerichte officiële vervolgbronnen, geen impliciet reeds voltooide stappen.

1. Projectinvoer is bestaande AGENTS/override/config plus coherent broncheckout en aparte doelmap. Student inventariseert en voert de gelinkte concrete Pythonhelper uit. README legt LOOP_SOURCE/LOOP_TARGET, kopieerbestemming en inspectie van manifest/diff uit. Helper krijgt schrijfrecht in de doelmap, geen Codex-toolrechten. Reden is behoud van bestaande afspraken; uitkomst zijn leesbare adapterbestanden zonder vervangen projectinstructies. Conflictstop en handmatige AGENTS-wijziging/rollback zijn verklaard.

2. Student schrijft bekende S1–4-opdracht, PROJECT.md, C1 en exacte versies; invulvorm noemt rolbron, contracten, criteria, besluiten en leesbare bronnen. Reden voor PLANNED is de optionele interfaceparameter. Klaar betekent dat de nieuwe planner alle input kan lezen zonder eerdere chat. De volledige C1-uitleg mag vanuit de expliciet vooraf gelezen gedeelde praktijk worden gebruikt.

3. planner-task.txt is stdin van een nieuw exec-proces. Flags en uitvoerder zijn nabij het commando uitgelegd: modeltools read-only, CLI bewaart laatst antwoord, geen nieuwe toolgoedkeuring. Student controleert echte C2 op behoud van default/storage en bewaart bron. Sandbox/API/quotumfout is geen C2. Reden en grens van vers proces tegenover toegankelijke bestanden zijn expliciet.

4. Invoer is concreet C2/C3; uitvoerder is de mens, geen model. Hij bewaart exact besluit/source/reden, en geeft alleen bij PROCEED bouwinvoer door. Vergelijking voor hergebruikt akkoord en nieuw besluit bij andere keuzes zijn verklaard. De lezer kan planakkoord van tooltoegang onderscheiden.

5. builder-task bevat vrijgegeven contracten/normen; nieuw exec krijgt workspace-write. Model verandert uitsluitend het gevraagde product, maar student begrijpt waarom sandbox breder is en echte diff gecontroleerd moet worden. Pythoncontrole vóór/na heeft exacte verwachte 1pass/3TypeErrors en 4pass/exit0. Student bewaart codecommit/C5 met criteria/evidence/limits; Git/tracker blijven menselijke verantwoordelijkheid. Voorgesteld commando is expliciet onvoldoende bewijs.

6. Nieuwe reviewer ontvangt uitsluitend C5-kern, codecommit, criteria en normen. Student houdt maakgesprek/andere initial verdict buiten invoer en transcripten buiten de map; read-only en vers proces maken toegankelijke bestanden niet onleesbaar. Echte tests moeten bij commit horen. Bij BLOCK bewaart student blocker/tellers vóór herstel, geeft builder bestaande wijziging en nieuwe beoordelaar expliciete repair-appendix. Reden, afhankelijkheden en geen extra allowance door nieuwe sessie staan erbij; generieke limiet wordt naar core verwezen.

7. C6 en exacte commit zijn input voor afzonderlijk mensbesluit en terugkoppeling. Bronmapping uit vooraf gelezen gedeelde praktijk geeft de uitkomsten naar issue/PR; mens werkt gebruikt bord bij. Herkenbare afronding is complete lokale dossierketen; ontbrekende externe actie wordt geregistreerd. Geen native GitHub-integratie of studentbegrip uit agentlezing afgeleid.

De tekst heeft functionele uitleg bij concrete handelingen, professioneel Nederlands en herkenbare stappen. Het modulestramien is hier niet verplicht omdat dit een praktijkpagina is. Verwijzingen ondersteunen het eerdere leren; zij vervangen niet de nieuwe uitleg van Codex-uitvoering.

## Eigen verificatie en bewijsgrenzen

- `python3 -B onderzoek/33-proef/controleer_installatie.py`: exit0, acht geïsoleerde fixtures; 23 hashes, behoud en refusal-before-delete geverifieerd.
- `/tmp/arl33-reviewchecks.py`: exit0; alle gewijzigde productbytes en negen normbestanden exact; 20 installed-corehashes; snapshots/testbytes matchen commit3be0eaf,49f810f,328555e; eigen volledige suites exit0/1/0 met alleen negatieve S4-fout.
- `make -C docs html SPHINXOPTS='-W --keep-going'`: exit0.
- Gelezen en opnieuw uitgevoerde `/tmp/arl33-links.py`: 306 betrokken lokale links/fragmenten inclusief inkomende navigatie, nul fouten. Geen volledige externe linkaudit geclaimd.
- Exacte `git diff --check basis product` geeft **exit2** en meldt uitsluitend onderzoek/33-proef/C5-herstel.md:24: de enkele spatie is de letterlijke unified-diff-contextregel binnen de bewijsfence. Het behouden van die regel bewaart het oorspronkelijke diff. Dit bevestigt de algemene tekstclaim 'diff--check schoon' niet voor de exacte commitdiff. Orkestrator is hierover geïnformeerd en heeft een registerverduidelijking aangekondigd: eerdere controle betrof de werkboom. Geen productfout en geen reden voor een repairronde.

Geen nieuwe provideraccount-run uitgevoerd; niet vereist om de aangewezen werkelijk uitgevoerde keten opnieuw te beoordelen. Negatieve exercise-review checkte destijds geen Git-correspondentie; die grens is zichtbaar geregistreerd en eigen Git/snapshotcontrole plus verse repair-review sluiten de betrokken concrete productreferenties aan. Reviewers in beide goede runs onderzochten S1–4 opnieuw. Geen objectidentiteits-/deepcopybewijs, benchmark, UI/productiontest of studentvalidatie vastgesteld.

## Contract drift en bevindingen

Contract drift: `<none>`. De optionele boekenparameter is precies de vrijgegeven keuze; geen nieuwe generieke contractkopie/route, permissiesysteem of trackerintegratie.

Must fix: `<none>`.

Should fix: `<none>` als productbevinding. De aangekondigde registerverduidelijking van diff--check is een correctie van de bewijsbeschrijving, geen inhoudelijke productreparatie of uitgestelde feature.

Nice to have: `<none>`.

Repair outcome: `<none>` voor deze INITIAL #33-review. Oefen-B1 is productbewijs onder AC4; geen #33-blocker of tellerverbruik.

Next action: bewaar dit C6 bij werkitem/PR en leg de afzonderlijke menselijke mergekeuze voor. Behoud normbasis, letterlijke bewijsdiff en geregistreerde beperkingen. Geen Git/tracker-mutatie of merge door reviewer uitgevoerd; alleen eigen tijdelijke proef-/C6-bestanden en normale docs-buildoutput geschreven.
