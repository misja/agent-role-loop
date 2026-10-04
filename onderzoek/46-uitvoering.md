# #46: grondslag, schrijfproef en vervolg

## Besluit en scope

C2 v1 staat in [inventarisatie en plan](46-inventarisatie-en-plan.md), commit
0252164. De [C3](46-planreview.md) geeft PASS. De gebruiker gaf op 4 oktober 2026
akkoord op A–D: normverduidelijkingen, korte start met aparte voorbereiding,
begrensde raamwerkproef/Farley en registratie van vijf vervolgopdrachten.
[C4 en bron](https://github.com/misja/agent-role-loop/issues/46#issuecomment-5980396686).
Proces- en normbasis blijft `2f8b43f085053bdee4d6ccb9c75b23f4bb9663c9`.
De besloten toevoegingen gelden expliciet voor de eigen proef. Nieuwe werkitems
gebruiken na merge de nieuwe normcommit; lopend werk krijgt geen stilzwijgende
normwijziging. Het akkoord is geen merge of bouwvrijgave voor de vervolgitems.
Herstelstand bij uitvoering: ontwerp 0, oplevering 0.

Bouwer: root; afgebakende onderdelen door bouw46_normen en bouw46_raamwerk,
[vastgelegd in C1](https://github.com/misja/agent-role-loop/issues/46#issuecomment-5980403016).
Review wordt onafhankelijk op de exacte oplevercommit uitgevoerd.

## Waarom de eerdere borging onvoldoende was

Dit is een vergelijking van tekst en geregistreerde aanpak, geen verklaring van
verborgen auteurs- of reviewerkeuzen. Bronnen: de inventarisbijlagen, het beperkte
inleidingsonderzoek en onderzoek/30-redactie.md, 37-uitgangspunten.md,
35-module-redactie.md, 36-module-redactie.md en 42-schrijfwijzer.md.

| Bevinding | Bestaande norm en geregistreerde toets | Diagnose en gerichte borging |
|---|---|---|
| Deel B vraagt contracten en besluiten vóór een ingevulde eerste overdracht. | Doelgroep sprak van algemene engineeringkennis en kunnen uitvoeren; #35 vermeldt tekstueel doorlopen zonder volledige chatrun. | Startniveau te ruim te lezen. Herkennen, bekende toepassing en transfer onderscheiden; voorbereiding toont de eerste overdracht. Verdere begeleide keten in #48. |
| Intro combineert oriëntatie en alle agentbegrippen; de conclusie over taakverdeling voegt geen handeling toe. | Schrijfwijzer vroeg al concrete uitleg, selectie en zinsfunctie. #30-review toont correcte begripsweergave, niet waarom alle uitleg bij de ingang nodig is. | Bestaande selectieafspraak onvoldoende toegepast/getoetst. Tekstfunctie vooraf kiezen en review naar de benodigde handelingen laten wijzen. |
| Module 4 geeft pass op onderzoek naast een softwareverdict; module 5 vraagt besluitbron zonder ingevuld voorbeeld. | Conventies vragen ontbrekende stappen; #36 registreert opdrachtgangen en geen gevonden begripsprong. | Het verslag bewijst geen toets van deze specifieke toepassing. In review probleem, invoer, reden en resultaat aanwijzen; voorbeelden in #50. |
| Verder lezen mengt leesadvies met raamwerkvergelijking en methodeverdediging. | #30 hield Verder lezen inclusief bronkritiek behouden; #37-scenario's behandelen eerste agentgebruik en claims, geen bronkeuze door studenten. | Selectie geldt al, maar functie en voorkennis van naslag waren onvoldoende expliciet in toetsdekking. Literatuur/naslag gericht opnemen; Farley als proef, rest #52. |
| #37 behandelt de samengevoegde #30-tekst als uitgewerkt voorbeeld. | Positieve agentreview en schone build zijn geregistreerd; studentwaarnemingen ontbreken. #42 scherpt taalregels aan en claimt geen studentproef. | Een bruikbaar voorbeeld kan nog begripsprongen bevatten. #30 krijgt geen algemene status als geslaagde didactische referentie. Nieuwe review benoemt concrete dekking en grenzen. |

Bestaande normen ontbraken dus niet geheel. De aanvullingen maken hun toepassing
concreter; extra rollen of een lijst verboden woorden vervangen geen toepassing.
Leeruitkomsten en zelfchecks hebben een functie en blijven. Bruikbare passages
over codekeuzen en bewijsgrenzen worden niet mechanisch geschrapt.

## Schrijfproef en leesroute

| Voor | Na | Functie en grens |
|---|---|---|
| Index: veranderende orders bij CSV-export en 717 woorden vóór navigatie. | Eén uitleeneis, tests met beschikbare boeken, gemiste tweede uitlening en wat de student oefent. | Oriëntatie. Ontbrekend bewijs toont nog geen softwarefout. Woordenaantal is geen begripstoets. |
| Model, context, API, agent, sessie, rol en contract in dezelfde ingang. | Voorbereiding met chatinvoer, werkelijke bestands-/testactie, rol, ingevulde overdracht en functiewijzer. | Nieuwe kennis vóór deel A/B. Module 1/2 verwijzen naar de nieuwe plek. Volledige portie-1-keten volgt in #48. |
| Raamwerkbegin met exportreparatie en retorische koppen. | Uitleenafspraak, ontbrekend testgeval, verwachting/waarneming, taakverdeling en verschil tussen defect en ontwerpafweging. | Eerste twee secties vervangen. Planbesluit en merge onderscheiden. Overige raamwerktekst blijft #52. |
| Farley: vergelijking van twee complete stelsels. | Hoofdstuk 5 Feedback, leesvraag over tussentijds controleren, programmeer-/testvoorkennis en eigen toepassing op AI. | Korte leesrichting; geen validatie van de rollenlus. Andere drie toelichtingen ongewijzigd. |

Route: start → voorbereiding tot rollen → module 1 deel A → les 1 →
voorbereiding overdracht/contractwijzer → deel B. Module 2 verdiept het
interfacebegrip aan ingevulde voorbeelden. Raamwerk blijft beschikbaar bij de
latere modules die de drie soorten kwaliteitsmechanismen gebruiken; hun
verwijzingen blijven behouden. Noodzakelijke uitleg is niet door naslag vervangen.
Generieke Engelse contracten blijven normbron.

## Vervolg, prioriteit en behoud

Vijf vervolgitems krijgen eigenaar misja en status Backlog. Roluitvoerders worden
bij hun eigen C1 toegewezen. Bouwvrijgave volgt hun eigen route en gate.
Ontbrekende voorbereiding gaat vóór latere zelfstandige toepassing; het
raamwerkvervolg kan na de proef afzonderlijk starten.

| Bronnen in inventaris | Afhandeling |
|---|---|
| Inleidingsbevindingen 1–7 | Korte start/voorbereiding en raamwerkbegin in #46. Herhalingen en latere exportpassages blijven #52. |
| Inleidingsbevindingen 8–9 | Farley proef in #46; overige raamwerk/naslag/literatuur in #52. |
| Vroege inventaris 1–7 | #48: eerste uitvoering; alle eisen/porties blijven, geen onbewezen context- of tijdclaim. |
| Vroege inventaris 8–15 | #49: modules 2–3, analogiegrens, unieke oefenuitkomst en uitvoerbare controles. |
| Late inventaris 1 | Behoud van concrete organizer module 4; optionele gerichte link in #50. |
| Late inventaris 2–6 | #50: oordelen, menselijke besluiten, historische naslag. |
| Late inventaris 7–10 | #51: eigen proces en praktijkvoorbeeld, beslismomenten en gerichte verwijzingen. |

[Module 1 #48](https://github.com/misja/agent-role-loop/issues/48),
[modules 2–3 #49](https://github.com/misja/agent-role-loop/issues/49),
[modules 4–5 #50](https://github.com/misja/agent-role-loop/issues/50),
[module 6/praktijk #51](https://github.com/misja/agent-role-loop/issues/51),
[raamwerk/bronnen #52](https://github.com/misja/agent-role-loop/issues/52).

Aanvullende studentgerichte bronnen gelezen: README.md, adapters/manual/README.md,
adapters/claude-code/README.md en adapters/openai-compatible/README.md. README
verwijst nog naar de inleiding voor het voorbeeld van een collega die een
wijziging beoordeelt; de nieuwe inleiding gebruikt een boekenplank. Dit is geen
technische contractbreuk. Overzicht #28 krijgt dit als gerichte samenhangactie.
Manual vraagt intro plus module 2 vóór het praktijkvoorbeeld; voorbereiding
is via intro vindbaar, maar #51 moet de ingang naar de precieze uitleg toetsen.
Adapterinstructies veronderstellen uitvoeringskennis; #32–#34 blijven eigenaar
van expliciete lezer/voorkennis, handelingen en onafhankelijke uitvoeringscheck.
Casusbeschrijvingen/docstrings bevatten volgens onderzoek/36-module-redactie.md
oude claims. Geen casuscode gewijzigd; #50 krijgt de bronbegrenzing mee en
kan noodzakelijke casusredactie als afzonderlijke scope voorleggen.
Docentmateriaal #22 en summatieve toetsing #23 blijven eigen werkitems.

## Verificatie en grenzen

Build, lokale links, visuele lezing, beschermde passages en exacte reviewcommit
worden in C5 vastgelegd. Geen nieuwe tests voor tekst; geen codegedrag gewijzigd.
C6 leest proef, eerste overdracht, module 4-oefening en Farley met concrete vragen.
Ontbrekende voorbereiding in ongewijzigde passages kan vervolgwerk zijn, maar
wordt niet opgevoerd als opgelost door deze proef.

Student-/docentwaarnemingen, gemeten begrip, leereffect, uitvoeringsduur en
budgetmetingen zijn niet beschikbaar. Een agentlezing is geen studentvalidatie.

## Primaire broncontrole Farley

# Farley-broncontrole voor #46

Controle: 4 oktober 2026. Primaire uitgeversbron: InformIT / Addison-Wesley Professional, productpagina met inhoudsopgave.

URL: https://www.informit.com/store/modern-software-engineering-doing-what-works-to-build-9780137314782

Claim: hoofdstuk 5 heet Feedback. De inhoudsopgave noemt feedback bij code en integratie en vroegtijdige feedback. Dit ondersteunt de beperkte leesrichting: tussentijds controleren tijdens ontwikkeling. De producttoelichting gebruikt voorstel B, met behoud van bibliografische citeersleutel.

Grens: alleen de openbare uitgeversinhoudsopgave is gecontroleerd. Het volledige boek of hoofdstuk is niet gelezen of herbeoordeeld. Geen claim dat het boek de AI-rollenlus valideert. Ervaring met programmeren en tests is de gekozen leesvoorbereiding voor deze leerlijn, geen gemeten studentbegrip. De overige literatuurtoelichtingen blijven ongewijzigd en zijn hier niet brongecontroleerd.

## Bouw- en registratiecontrole vóór C6

- `make -C docs html`: exit 0, Sphinx met `-W --keep-going`, geen waarschuwing.
  Log: /tmp/arl46-build.log. Bestaande uv-omgeving; geen dependencywijziging.
- Negen gewijzigde gepubliceerde pagina's: 709 lokale HTML-links en fragmenten,
  nul fouten, via /tmp/arl46-links.py. Externe websites niet integraal getest.
- Headless Chrome 1400×1000: koppen, tekst, codeblokken, contracttabel, navigatie
  en Farley gelezen; screenshots boven/midden/einde in /tmp/arl46-visual/.
  Geen mobiele of gedeployde-sitecontrole. Het werkitemsjabloon wordt niet gepubliceerd.
- Alle achttien modulepagina's vergeleken met de basis: uitsluitend de drie
  vrijgegeven voorkennislinks verschillen. Daarmee zijn alle eisen, porties,
  leeruitkomsten, vaste staarten en casusverwijzingen behouden.
- Raamwerk vanaf “Drie soorten kwaliteitsmechanismen” identiek, behalve Farley.
- Ingang vóór navigatie: 129 woorden inclusief kop, subtitel en leesaanwijzing;
  eerder 717. Dit meet omvang, geen toegankelijkheid of leerprestatie.
- `git diff --check`: schoon. Geen code/core/adapter/casuswijzigingen.
- Nieuwe issues #48–#52 teruggelezen: criteria en eigenaar misja aanwezig.
  Projectbord teruggelezen: #46 Building, #48–#52 Backlog.
- Overdrachten op #22/#23/#28/#32/#33/#34 teruggelezen. Aanvullende samenhangactie
  README bij #28; manual-afhankelijkheid bij #51 en casusbronbegrenzing bij #50.
  Lokale readbacks: /tmp/arl46-issue*-readback.json en /tmp/arl46-board-readback.json.

## Onafhankelijke opleveringsbeoordeling

Beoordeelde productcommit: `379790406630bbc6845f559471b7a2de52b94bd0`.
[C5-kern](https://github.com/misja/agent-role-loop/issues/46#issuecomment-5981568243).
Beide initial reviewers kregen de geldige normen, C4, criteria en objectief bewijs,
zonder maaktranscript of elkaars oordeel.

[Didactiek](https://github.com/misja/agent-role-loop/issues/46#issuecomment-5981621615):
SHIP voor AC1/2/3/4/5/6/9 en tekstuele overlap. De verse leesgang volgt de proef,
eerste overdracht, module 4-oefening en Farley. Probleem, invoer, handelingen,
reden en uitkomst zijn concreet aangewezen. Bestaande toepassingsproblemen blijven
gericht bij #48/#50/#52; zij zijn niet als opgelost voorgesteld.

[Samenhang](https://github.com/misja/agent-role-loop/issues/46#issuecomment-5981621809):
SHIP voor AC7/8-techniek/10/11 en verwijzings-/normbronoverlap. Beschermde passages
en 709 lokale links zelfstandig gecontroleerd; issues en overdrachten live gelezen.
Build/bordstatus als aangeleverd bewijs met grenzen. Actuele losse eindbeelden
bevestigen Farley en de finale schrijfwijzerpassage; oudere collages zijn niet
als finale passagecontrole gebruikt.

Geen blockers, nieuwe nits of contract drift. Alle toegewezen criteria afgedekt.
Verenigbare oordelen worden door root in C7 samengebracht; geen arbitrage of
herstelronde nodig. Herstelstand ontwerp 0, oplevering 0. Geen GitHub-CI-checks
gerapporteerd; de schone docs-build is lokaal uitgevoerd.

PR47 is gereed voor een menselijk mergebesluit. Deze afrondingsregistratie wijzigt
geen beoordeelde producttekst. #46 sluit pas na merge; de vijf vervolgitems blijven
afzonderlijke opdrachten en de schrijfverantwoordelijkheid geldt doorlopend.
