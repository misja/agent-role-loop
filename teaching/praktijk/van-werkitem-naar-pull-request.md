# Van werkitem naar pull request

## Een wijziging volgen

Je werkt aan de boekenplank uit de leerlijn. Een medewerker wil alleen de boeken
zien die beschikbaar zijn om uit te lenen. Je kunt die vraag in een chat aan een
AI-assistent stellen. Maar je medestudent moet later ook kunnen terugvinden wat
precies is afgesproken, welke versie is gebouwd en waarop de beoordeling berust.
Daarvoor gebruiken we hier een issue en een pull request.

Lees dit hoofdstuk na [module 2](../modules/02-begrijpen/index.md). Je kent dan de
rollen en de contracten die hun overdrachten beschrijven. Algemene kennis van
Git en tests gebruiken we hieronder. Ervaring met een agent die GitHub zelf kan
bedienen is niet nodig. De [inleiding](../index.md) legt het verschil uit tussen
een taalmodel, een agent en een rol.

Na dit voorbeeld kun je de geldige opdracht, het menselijke besluit en de
beoordeelde codeversie aanwijzen. Je kunt ook uitleggen welke informatie bij een
verhuizing naar een andere projectomgeving behouden moet blijven.

De boekenplank in dit hoofdstuk is een bewerkt onderwijsvoorbeeld. De gesprekken,
besluiten en beoordelingen zijn geconstrueerd; de code en testuitkomsten kun je
zelf controleren. De bestaande modulecases blijven aparte oefeningen.

## Dezelfde opdracht, een andere opslagplaats

Eerst schrijven we de opdracht op. Een medewerker wil een selectie kunnen
opvragen, terwijl het bestaande overzicht van alle boeken beschikbaar blijft.
Die laatste voorwaarde doet ertoe: het filter mag uitgeleende boeken niet uit de
registratie verwijderen.

```{literalinclude} ../cases/praktijk-projectomgeving/overdrachten.md
:language: md
:start-at: "## C0-W1:"
:end-before: "## C1:"
```

Deze tekst is een ingevuld werkitem volgens {core}`contracts/work-item.md`.
Markdown maakt de kopjes en criteria leesbaar. Wanneer je de tekst in de
beschrijving van een GitHub-issue plakt, blijft de opdracht gelijk. Het issue
voegt een nummer, reacties en koppelingen toe. Die helpen om het werk te volgen.

Een contract beschrijft welke informatie nodig is; Markdown is hier de opmaak.
Een bestand of issue is de plaats waar je die informatie bewaart. Het
projectbord laat vervolgens zien in welke fase het werk staat. Een kaart met
status *In progress* vertelt nog niet welk plan is goedgekeurd.

| Informatie | Geldige bron in dit voorbeeld | Wat elders staat |
|---|---|---|
| Opdracht en criteria | Issuebeschrijving W1 | PR en bord verwijzen naar het issue |
| Route en herstelstand | Aangewezen C1-reactie op het issue | Overdrachten noemen de geldende stand |
| Plan | C2-reactie met versie P1 | Besluit verwijst naar P1 |
| Menselijk besluit | C4-reactie met persoon, planversie en reden | C5 geeft de relevante beslissing met bron mee |
| Code | Exacte Git-commit | PR vergelijkt de branch met de basis |
| Oplevering | C5 in de PR, met bewaarde beoordeelde versie | Link naar eisen, besluiten en bewijs |
| Beoordeling | C6 bij de PR, met exacte codecommit | Herstelbijlage verwijst naar eerdere bevindingen |
| Voortgang | Status van het gekoppelde item op het bord | Geen kopie van plan of akkoord |

De [ingevulde overdrachten](overdrachten.md) bevatten de volledige voorbeeldroute.
Daar staan ook het versieregister en het zijpad met een gewijzigde opdracht.

## Wie geeft wat aan de volgende rol?

Jij bent in deze eerste uitvoering de orkestrator. Je verzamelt de informatie
voor een rol, geeft die aan een afzonderlijke sessie en bewaart de teruggegeven
overdracht. Dat kan handmatig met chatvensters. Een issue op een bord start niet
vanzelf een agent. Een latere koppeling kan deze handelingen overnemen, maar moet
nog steeds de juiste opdracht, versie en rechten meekrijgen.

De triage kiest hier `PLANNED`. Het optionele argument van `lijst()` vraagt een
klein interfacebesluit. De planner legt in P1 vast dat
`lijst(alleen_beschikbaar=False)` standaard het bestaande gedrag houdt. Bij
`True` wordt alleen de teruggegeven lijst gefilterd. De vier criteria krijgen
ieder een controle en worden aan één onafhankelijke beoordelaar toegewezen.

De menselijke opdrachtgever beoordeelt P1 vóór de bouw. In het voorbeeld staat
in C4-P1 dat de toevoegvolgorde behouden blijft. Een losse reactie “akkoord” is
alleen bruikbaar als duidelijk is op welke planversie zij betrekking heeft.

| Opdracht aan een sessie | Informatie die meegaat | Resultaat |
|---|---|---|
| Plan deze wijziging | C0, C1, basiscode, geldende normen | C2-P1 |
| Bouw het goedgekeurde plan | C1, P1, C4-P1, code en normen | Wijziging en C5 |
| Beoordeel de oplevering | C5-kern met criteria, code, besluit, normen en bewijs | C6 |

Geef ook de betreffende rolprompt en de leesbare contractdefinitie mee. Een
webchat kan een lokaal bestand niet lezen doordat je alleen het pad noemt.
Plak de benodigde inhoud of gebruik de bestandsmogelijkheden van je omgeving.
Geef de beoordelaar de bronnen waarmee hij de opdracht kan toetsen; het
maakgesprek met eerdere pogingen blijft erbuiten.

Voor dit kleine werkitem is geen aparte verhelderaar gekozen. Eén beoordelaar
dekt S1-S4; diens C6 is het eindoordeel. Er ontstaan dus geen lege C3 en C7.
Andere werkzaamheden kunnen een andere bezetting nodig hebben. De actuele
routekeuze staat in {core}`loop.md`.

## Een groene controle, toch een blokkade

De bouwer levert versie A aan in een PR. Het filter geeft de juiste beschikbare
boeken terug en de drie uitgevoerde tests slagen. In C5-A staat echter dat S4
niet is vastgesteld. De beoordelaar ziet bovendien dat de methode de interne
lijst overschrijft. Een boek dat was uitgeleend verdwijnt daardoor uit een
volgende aanroep van `lijst()`.

Dit is een concrete reden om de wijziging tegen te houden: criterium S4 wordt
niet gehaald. Het oordeel C6-A noemt de plaats, het gevolg en wat de reparatie
moet aantonen. De bouwer kan daarmee aan hetzelfde werk verdergaan zonder een
nieuw volledig ontwerp te maken.

Download de {download}`voorbeeldbundel <boekenplank-projectomgeving.zip>` en pak
haar uit. Python 3.10 of nieuwer volstaat; extra pakketten zijn niet nodig.
Voer vanuit de uitgepakte map uit:

```sh
python controleer.py a zwak
python controleer.py a regressie
python controleer.py b volledig
```

| Controle | Verwachte uitkomst | Wat blijkt eruit? |
|---|---|---|
| A, zwak | 3 tests slagen, exitcode 0 | De gecontroleerde lijstuitkomsten voldoen |
| A, regressie | 1 test faalt, exitcode 1 | Na het filteren ontbreekt boek 2 in de registratie |
| B, volledig | 4 tests slagen, exitcode 0 | Ook behoud van boeken en uitleenstatus is gecontroleerd |

De middelste opdracht hoort te falen. In `bewijs.txt` staat de waargenomen
uitvoer bij het maken van dit materiaal. Dat is reproductiebewijs van de
meegeleverde versies, geen verslag van een echte eerdere agentrun. Bij eigen
uitvoering schrijf je de regressiecontrole vóór de reparatie, zodat je ziet dat
zij het probleem daadwerkelijk aantoont.

Versie B retourneert een aparte lijst. De bouwer levert een nieuwe C5 en een
herstelbijlage: de A..B-diff, de eerdere blokkade en de eerder vastgestelde
dekking. De auteur mag zijn sessie behouden. De herbeoordeling begint met een
eigen context en de expliciete herstelbijlage. Omdat dezelfde methode verandert,
worden in dit voorbeeld alle vier de criteria opnieuw gecontroleerd. Eerder
bewijs van A wordt niet als nieuw bewijs voor B opgevoerd.

C6-B luidt `SHIP`. Dat betekent dat de wijziging klaar is voor de menselijke
mergebeslissing. Was er nog een blokkade, dan zou na deze ene automatische
herstelronde een menselijke keuze voor een begrensd vervolg, splitsen of stoppen
nodig zijn. Een verbruikslimiet maakt een fout niet acceptabel.

## Welke versie is goedgekeurd?

In de uitleg zijn A en B korte leeslabels voor de twee meegeleverde bestanden.
In een werkelijke PR gebruik je volledige commit-ID's. Een branchnaam is niet
voldoende: een nieuwe commit verandert de inhoud van die branch. Bewaar daarom
bij C5 en C6 zowel de codecommit als de basis van de vergelijking.

Ook een issuebeschrijving of reactie kan worden bewerkt. Spreek af dat een nieuw
plan een nieuwe versie krijgt, met een eigen besluit. Bewaar bij een
beslismoment een snapshot van de betreffende tekst, bijvoorbeeld
`bewijs/P1.md` op een vaste commit. Het besluit linkt naar die versie. Op GitHub
kun je bij een bestand met de toets `y` de branchlink omzetten in een link naar
de exacte commit. Zie de [documentatie over permanente bestandslinks](https://docs.github.com/en/repositories/working-with-files/using-files/getting-permanent-links-to-files).

Zo'n snapshot bewaart wat eerder is beoordeeld. Je onderhoudt hem niet naast de
actuele opdracht als tweede backlog. Het issue wijst aan welke versie nu geldt;
het besluit bewaart waarop het destijds van toepassing was.

Stel dat na B een wens ontstaat om beschikbare boeken alfabetisch te sorteren.
Daarvoor geldt P1 niet: toevoegvolgorde was expliciet afgesproken. In het
[zijpad P2](overdrachten.md) wordt die wens als
voorstel vastgelegd. De mens houdt de uitvoering tegen omdat regels voor
hoofdletters en gelijke titels ontbreken. De bestaande groene beoordeling
blijft een oordeel over B tegen W1/P1, niet over de nieuwe sorteereis.

## Zelf beginnen op GitHub

Werk in een eigen oefenrepository en met een medestudent als menselijke
opdrachtgever. Je hebt GitHub-toegang, Git en Python nodig. Gebruik voor de
agentrollen een omgeving waarin je afzonderlijke sessies kunt beginnen.
Onderstaande stappen gebruiken de webinterface voor issues en PR's; zij
veronderstellen geen geïnstalleerde agentkoppeling.

1. **Maak je werkplek.** Maak op GitHub een eigen repository met README en clone
   haar lokaal. Pak de voorbeeldbundel in die lokale repository uit. Lees het
   licentiebestand en behoud de bronvermelding. Kopieer `boekenplank_basis.py`
   naar `boekenplank.py`; leg dit als basiscommit vast. De meegeleverde A/B-bestanden
   zijn naslag, het werkbestand heet `boekenplank.py`.
2. **Leg de opdracht vast.** Kies in je repository *Issues*, *New issue* en plak
   C0-W1 uit `overdrachten.md` in de beschrijving. Bewaar de issue-URL. Zo ontstaat
   een repository-issue waar je later een PR aan kunt koppelen, volgens de
   [GitHub-instructie voor issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue).
3. **Maak de voortgang zichtbaar.** Kies op je profiel *Projects*, *New project*
   en een *Board*. Voeg je bestaande issue toe door de URL bij *Add item* te
   plakken. Gebruik de status voor voortgang; bewaar beslissingen bij het issue.
   Zie [een project maken](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project)
   en [bestaande items toevoegen](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/adding-items-to-your-project).
4. **Plan en laat besluiten.** Leg C1 vast met namen van de uitvoerders en S1-S4
   als toewijzing aan de beoordelaar. Laat de planner P1 maken. Gebruik de
   voorbeeldcontracten als vorm, niet de fictieve goedkeuring als toestemming.
   Bewaar de concrete P1-snapshot met commitlink. Laat je medestudent het plan
   lezen en C4 vastleggen met die verwijzing. Ga pas daarna bouwen.
5. **Maak de wijziging afzonderlijk beoordeelbaar.** Start een branch vanaf je
   basis en voeg het filter toe, of reproduceer de voorbereide A-variant met de
   patch. Controleer de uitkomsten. Leg de wijziging vast en noteer de codecommit.

   ```sh
   git switch -c filter-beschikbare-boeken
   git apply basis-naar-a.patch
   python controleer.py werk zwak
   git add boekenplank.py
   git commit -m "Voeg een filter voor beschikbare boeken toe"
   git rev-parse HEAD
   git push -u origin filter-beschikbare-boeken
   ```

6. **Open de PR.** Kies *Compare & pull request*. Controleer de basisbranch en
   de branch met je wijziging. Zet C5 in de beschrijving met je eigen codecommit,
   bewijs en links naar issue, plan en besluit. De [GitHub-instructie voor PR's](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request)
   beschrijft deze velden. Gebruik `Closes #N` met je echte issuenummer wanneer
   deze PR het werkitem volledig afrondt. Het sluitwoord in de PR-beschrijving
   werkt bij een PR naar de standaardbranch; na merge sluit het gekoppelde
   issue. Zie [de voorwaarden voor deze koppeling](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue).
7. **Laat onafhankelijk beoordelen.** Geef een nieuwe beoordelingssessie C5-kern,
   de normen, code en controles. Bewaar C6 als herkenbare agentbeoordeling bij de
   PR, met de exacte commit. Een GitHub-review kent onder meer *Comment*, *Approve*
   en *Request changes*; wie die mag indienen hangt van de rechten af. De auteur
   kan [zijn eigen PR niet goedkeuren](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request). Een overgenomen agentoordeel in een comment
   is geen zelfstandig menselijk akkoord. Zie [pull request reviews](https://docs.github.com/en/pull-requests/reference/pull-request-reviews).
8. **Reproduceer zo nodig het herstel.** Gebruik bij A de R1-bevinding, voer
   `python controleer.py werk regressie` uit en verklaar de fout. Pas
   `git apply a-naar-b.patch` toe. Voer `python controleer.py werk volledig` uit,
   leg de reparatie vast in een nieuwe commit en push die naar dezelfde branch.
   Werk C5 bij en bewaar de eerdere versie. Geef de onafhankelijke herbeoordeling
   de herstelbijlage met beide echte SHA's en de gebruikte ronde.
9. **Rond aantoonbaar af.** Laat de mens beslissen over de daadwerkelijk beoordeelde
   codecommit en voeg daarna samen. Controleer of het issue gesloten is en werk
   de bordstatus bij als de ingestelde automatisering dat niet doet. Bewaar de
   menselijke beslissing en de mergeverwijzing.

Je eindresultaat is een navolgbare keten van opdracht naar merge. Een tweede
student moet de juiste versie kunnen vinden zonder jouw chat terug te lezen.

## Dezelfde inhoud in een andere omgeving

Codeberg biedt ook issues, pull requests en projectborden. Die functies kun je
voor dezelfde verantwoordelijkheden gebruiken. Dat betekent niet dat de
instellingen en koppelingen identiek zijn aan die van GitHub. De
[Codeberg-documentatie over repositoryrechten](https://docs.codeberg.org/collaborating/repo-permissions/)
onderscheidt toegang tot code, issues, reviews en projectborden; controleer dus
wat in jouw repository beschikbaar is.

| Verantwoordelijkheid | GitHub in dit voorbeeld | Overeenkomst op Codeberg |
|---|---|---|
| Opdracht en besluiten bewaren | Issue en reacties | Issue en reacties |
| Codeversies onderscheiden | Git-branch, commits en PR | Git-branch, commits en PR |
| Beoordeling vastleggen | C6 bij de PR | C6 bij de PR |
| Voortgang tonen | Project met bordweergave | Projectbord, als beschikbaar en toegankelijk |

Codeberg beschrijft het werken met branches en PR's in
[Pull requests and Git flow](https://docs.codeberg.org/collaborating/pull-requests-and-git-flow/).
Op een andere Forgejo-installatie controleer je de beschikbare versie, rechten
en functies. Neem GitHub-sluitwoorden of bordautomatisering niet zonder controle
over. De opdracht, criteria en beoordelingsbasis blijven inhoudelijk dezelfde.

### Een overdracht uitproberen

Open de uitgepakte bundel zonder GitHub. Zoek in `overdrachten.md` het moment na
C6-A op. Je kunt W1, C4-P1, versie A en de volgende herstelstap aanwijzen. Open
`boekenplank_a.py` en `a-naar-b.patch` om de code en het herstel te bekijken.
Dit is de informatie die inhoudelijk mee moet naar een nieuwe projectomgeving.

Een volledige verhuizing van je eigen project vraagt daarnaast een registratie:

| Mee te nemen | Hoe vastleggen | Wat niet vanzelf terugkomt |
|---|---|---|
| Opdracht, plannen, besluiten en C5/C6 | Markdown-snapshots met bron, versie en datum | Native reacties en reviewstatus |
| Code en vergelijking | Git-historie of benodigde versies en patches | Issues en projectbordgegevens |
| Testbewijs en bijlagen | Logbestanden en bestanden met verwijzingen | Externe CI-runs en tijdelijke downloadlinks |
| Verbanden en voortgang | Register oud object/URL → nieuw object/URL; status met peildatum | Automatisering en identiteit/rechten van accounts |

De bundel bevat `overdrachtregister.csv` als kleine uitgewerkte illustratie.
Omdat hier geen echte oefenissues zijn gepubliceerd, vermeldt het register bij
platform-ID's “niet aangemaakt”. Bij een werkelijke verhuizing vul je de oude en
nieuwe URL's in en controleer je elke verwijzing. Een tekstuele kopie van een
besluit bewaart de inhoud en bronregistratie; zij maakt geen nieuwe menselijke
ondertekening of native review aan.

### Een echte projectketen teruglezen

In deze repository kun je [werkitem #29](https://github.com/misja/agent-role-loop/issues/29)
volgen naar het [uitvoeringsbesluit](https://github.com/misja/agent-role-loop/issues/29#issuecomment-5641493461),
[PR #40](https://github.com/misja/agent-role-loop/pull/40) en de
[onafhankelijke beoordeling](https://github.com/misja/agent-role-loop/issues/29#issuecomment-5645059502).
Daarna volgde de menselijke mergebeslissing. Dit is echte projecthistorie;
het filtervoorbeeld hierboven is speciaal voor het onderwijs samengesteld.

## Zelfcheck

1. Welke informatie blijft gelijk wanneer je C0 van een bestand naar een issue
   verplaatst? Welke informatie voegt de projectomgeving toe? Zie de bronmapping.
2. Welke code is na C6-A beoordeeld en wat mag de bouwer nu doen? Zoek de bronnen
   in de ingevulde overdrachten.
3. Waarom is C6-B geen goedkeuring van de sorteerwens P2? Wijs de gewijzigde eis
   en het toepasselijke menselijke besluit aan.
4. Welke gegevens zou je naast een Git-clone meenemen naar een ander platform?
   Controleer dit met de exporttabel en het overdrachtregister.

Je kunt het hoofdstuk bij [module 3](../modules/03-machine/index.md) opnieuw
gebruiken om het verschil tussen testbewijs en beoordeling te onderzoeken.
Bij [module 5](../modules/05-poort/index.md) ligt de nadruk op het menselijke
besluit; in [module 6](../modules/06-ontwerpen/index.md) verantwoord je zelf de
gekozen werkwijze en projectomgeving.
