# #50: oordelen en menselijke besluiten concretiseren

## Besluit en grondslag

[C4 PROCEED](https://github.com/misja/agent-role-loop/issues/50#issuecomment-5984012135)
registreert het gebruikersantwoord “akkoord” op C2 v1 in `onderzoek/50-plan.md`.
Het geeft het tekstpakket vrij, inclusief de keuze synthese bij verenigbare
beoordelingen en arbitrage bij inhoudelijk geschil. Geen mergebesluit.

Proces-/normbasis: `b6ddcd55fbb9de37db316a626d0ddee4afe703e9`.
[C1-start](https://github.com/misja/agent-role-loop/issues/50#issuecomment-5983989003)
en het plan geven leesbare normen, AC1–7 en de toewijzing aan één verse
onafhankelijke reviewer `/root/review50`. Root plant/bouwt. Geen C3 geselecteerd.
Herstelstand vóór initial review: ontwerp 0, oplevering 0.

## Voor en na, bron en gevolg

| Bronbevinding #46 | Gerichte wijziging | Wat de lezer kan aanwijzen |
|---|---|---|
| Module-4-les beschrijft synthese/arbitrage abstract. | G-A/G-M als verenigbaar paar met C7-velden; G-X/G-Y als geconstrueerd geschil over expliciete O1-eis. | Bronherleiding, verschillende uitvoerders en welk codebewijs het geschil beslecht. |
| G-A-pass kan softwaregoedkeuring suggereren. | Annotatie verbindt A1-onderzoek, aangetoond gedrag, pass en nog open gebruikskeuze. | Pass op onderzoek geeft geen vrijgave voor het ophaalscenario. |
| Veel C6/C7-velden in één oefenstap. | Afzonderlijke basis-, bewijs-, oordeel- en samenbrengstappen met contractlinks. | Welke invoer meegaat, wat wordt ingevuld en welk artefact wordt bewaard. |
| Historisch poortfragment onderbreekt hoofdlezing. | Eén voorwaarde plus bouwergevolg in hoofdroute; volledig citaat in optionele dropdown. | Waarom besluitvoorwaarden met het plan meegaan; historische bronbeperkingen blijven vindbaar. |
| Besluitbron en veilig uitstel zijn nog niet ingevuld. | Voorbeeld-C4 met P1 op echte basiscommit, fictieve menselijke logboekbron, herstelvoorwaarde en gemotiveerd uitstel van meldingstekst. | Voorstelversie, wie beslist, wat eerst moet en waarom een vraag voor deze stap kan wachten. |
| Proportionaliteit op index is abstract. | Verbindt korte verwijderwijziging aan verlies van toegang tot reserveringen. | Omvang van code en gevolgen hoeven niet gelijk op te gaan. |

Voorkennis is vindbaar bij het module-2-analysemodel en de begeleide
module-1-uitvoering. De eigen oefening blijft twee gegeven en twee zelf te
schrijven C6's, bronherleidbaar C7 en individueel menselijk C4. Groepsvariant
volgt dezelfde keuze tussen synthese en arbitrage. De les levert geen eigen
studentbesluiten aan en schrijft geen volledige ontbrekende C5 of agentrun.

O1 is een aanvullende les-scenario-eis, geen gevonden historische opdracht.
G-X/G-Y zijn geconstrueerde uitspraken; arbitrage wijst de feitelijk onjuiste
uitspraak af en behoudt BLOCK voor O1. Het wijzigen van een gebruiksdoel blijft
menselijk. Historische garantie-/botsingsclaims blijven historisch en zijn
geen actuele norm of onderwijseffectbewijs. Oude casusdocstrings/README/testnamen
zijn ongewijzigd; hun claims worden door werkelijk codegedrag begrensd, conform
de overdracht uit `onderzoek/36-module-redactie.md`.

## Objectieve controles

Verificatiemodellen: manual-with-expected-results voor lees-/besluitgang;
validation-workflow voor bestaande casuscontroles, citaat, beschermde bestanden,
build en links. Geen codegedrag gewijzigd, geen nieuwe repositorytests of
kunstmatige voorwijzigingsfout voor proza. Voor/na hierboven beschrijft
tekstfuncties, geen gemeten studentbegrip.

Uitvoering via `/tmp/arl50-verify.py`, volledige sessie-uitvoer in
`/tmp/arl50-evidence.json`. Gescheiden tijdelijke kopieën, Linux/Python 3.14.8,
pytest 9.1.1. Blijvend beknopt bewijsregister:

| Invoer en actie | Verwachting | Waarneming |
|---|---|---|
| Ongewijzigde module-4-casuskopie, python -m pytest | Vijf pass, exit 0. | Vijf pass, exit 0. |
| Boek uitlenen aan Misja, Bob/Carla laten reserveren, terugbrengen. | Bob direct lener; Carla op wachtlijst. | uitgeleend_aan = Bob; wachtlijst = [Carla]. Dit weerspreekt G-X onder de expliciete O1-eis. |
| Ongewijzigde module-5-casuskopie, python -m pytest | Drie pass, exit 0. | Drie pass, exit 0. |
| Zelfde uitleen-/reserveringsinvoer; Boek-referentie bewaren en verwijderen. | Lege plank/KeyError bij opvragen; bewaarde referentie houdt gegevens. | lijst = []; boek(1) geeft KeyError; bewaarde lener Misja en wachtlijst [Bob, Carla]. Geen vernietigingsbewijs. |
| Historische citaatinhoud vergelijken met basiscommit. | Exact gelijk, afgezien van buitenste Markdownfence voor dropdown. | Citaatinhoud bytegelijk. |
| Diff beschermde casus/core/adapters/modules 1–3 en 6. | Geen wijzigingen. | Diff leeg. |

Indexleeruitkomsten van module 4 zijn bytegelijk. Module 5 voegt bij dezelfde
triage-uitkomst één gevolgvoorbeeld toe, geen nieuwe vaardigheid. De vaste
lesstaarten met terugblik, zelfcheck en overgang zijn behouden. Eigen invulstappen
ondersteunen bestaande taken zonder de eigen inhoudelijke afweging vooraf te geven.

`make -C docs html` onder `-W --keep-going`: geslaagd zonder waarschuwingen,
`/tmp/arl50-build.log`. De sandbox blokkeerde eerst uv-cachetoegang; herhaling
met goedgekeurde escalatie slaagde. `/tmp/arl50-links.py`: 475 lokale
HTML-links/fragmenten van beide modules, nul fouten. `git diff --check` schoon;
geen em/en-dash in modulepagina's. Exacte productcommit wordt in C5 vastgelegd.
Geen screenshots: uitsluitend tekst, geen concreet weergaveprobleem.

## Bewijsgrenzen en onafhankelijke beoordeling

De gegeven oordelen, O1-variatie en Sam-besluit zijn geconstrueerde onderwijsinvoer.
De P1-basiscommit is echt; Sams logboek en besluitbron zijn fictief en worden
niet als beschikbaar menselijk besluit gepresenteerd. Voor de eigen uitvoering
moet de student echte versies, bron en waarnemingen bewaren.

Geen studentwaarnemingen, gemeten leereffect/duur, echte agentreviewrun van de
casus, productiegegevens of volledige bibliotheekomgeving beschikbaar. Geen
herstelvoorziening gebouwd en geen volledige externe linkaudit. De codefeiten
betreffen deze kleine in-memory-cases en bewijzen geen algemene foutloosheid.
Het oorspronkelijke historische menselijke gesprek is niet teruggevonden;
de bestaande publicatie plus bevestigende issue-reactie blijven de bronbasis.

Initial C6 volgt op exacte productcommit. Reviewer beantwoordt concrete
leesvragen over synthese/arbitrage, pass versus softwaregoedkeuring en de
C4-bron/voorwaarde/uitstelgang. Een door de agent voorbereid C4 is agentlezing,
geen nieuw menselijk besluit of studentvalidatie.

## Finale onafhankelijke C6

Reviewer `/root/review50` geeft **SHIP** op
`fad0170de2be5641bb802331622a2f4f6b3ad2bc`. AC1–7 zijn nieuw onderzocht;
geen blockers, nits of contract drift. Volledige C6 staat op #50.

De reviewer schreef een bronherleidbare synthese van G-A/G-M, beslechtte het
O1-geschil met codebewijs en bereidde een C4 op papier voor met expliciet nog
ontbrekende menselijke besluitbron. Dit is agentlezing, geen echt mensbesluit.
Hij reproduceerde de exacte casuskopieën: vijf en drie tests pass en de
beschreven terug-/verwijdertoestand bevestigd. Historisch citaat bytegelijk,
beschermde diff leeg, 475 lokale links/fragmenten zonder fouten. Buildlog is
als auteursbewijs gelezen; geen eigen buildreproductie. De bewijsgrenzen blijven.

Herstelstand ontwerp 0, oplevering 0; geen reparatie nodig. Met één reviewer
is C6 finaal; geen C7. PR #55 wacht op menselijk mergebesluit. GitHub meldt
geen CI-checks; lokale docs-build is geslaagd. Deze afrondingsregistratie
wijzigt geen beoordeelde onderwijstekst.
