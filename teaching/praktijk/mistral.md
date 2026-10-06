# Een werkitem uitvoeren met Mistral

In het [gedeelde praktijkvoorbeeld](van-werkitem-naar-pull-request.md) draag je
opdracht, plan en bewijs tussen sessies over. Hier laat je Mistral Vibe de
rollen uitvoeren. Jij bewaart hun contractuitvoer, voert tests en Git-acties uit
en neemt de menselijke besluiten.

Lees dit na module 2 en het praktijkvoorbeeld. Je gebruikt terminalcommando's,
Git en Python-tests. De [voorbereiding](../van-chat-naar-agent.md) legt model,
uitvoerend programma, sessie en rol uit. Mistral levert modeltoegang. Vibe is
het programma dat het model aanroept en toegestane bestandsacties uitvoert.
De oefenrepository levert code en projectafspraken. Een losse API-aanroep zou
alleen aangeleverde tekst ontvangen; hier geeft Vibe ook leesgereedschappen mee.

## Voorbereiden

Gebruik een aparte oefenrepository zonder echte gebruikersgegevens. Je hebt
Git, Python 3.10 of nieuwer voor de boekencasus en een Mistral-account met
modeltoegang nodig. Installeer Vibe volgens de
[officiële handleiding](https://github.com/mistralai/mistral-vibe).
Vibe heeft eigen installatievereisten; de Python-versie van de boekencasus is
geen garantie dat Vibe daarmee kan worden geïnstalleerd. Controleer:

```sh
vibe --version
vibe --help
```

Deze route is onderzocht met Vibe 2.19.0 op Linux. Een ontbrekend commando vraagt
eerst installatie. Richt accounttoegang via de ondersteunde Vibe-aanmelding in;
voor een API-sleutel gebruik je `vibe --setup`. Bewaar geen sleutel of
accountidentiteit in je dossier. Aanmelding bewijst nog geen geslaagde
modelaanroep of beschikbaar quotum; dat blijkt bij de plannerstap.

Download de bundel bij het gedeelde praktijkvoorbeeld. Neem boekenplank_basis.py
als boekenplank.py en controleer.py in de oefenmap. De tests gebruiken alleen de
Python-standaardbibliotheek. Initialiseer Git en bewaar de basis met je gebruikelijke
Git-werkwijze. Controleer vanuit de oefenmap:

```sh
python3 -B controleer.py werk basis
```

Verwacht een geslaagde basiscontrole. `-B` voorkomt Python-bytecodecache.
Bij ontbrekende providerrechten kun je de handmatige sessieroute gebruiken,
maar registreer die keuze; dat is geen uitgevoerde Mistral-proef.

## Stappen

### 1. Projectafspraken inventariseren en adapter toevoegen

Bekijk AGENTS.md, toepasselijke instructies in bovenliggende mappen en bestaande
Vibe-configuratie. AGENTS is een bestand met projectinstructies dat Vibe kan
laden. `.vibe/config.toml` en gebruikersconfiguratie kunnen daarnaast tools,
agentprofielen, prompts, hooks en externe verbindingen instellen. Een profiel
kiest gedrag en gereedschapsrechten; het is iets anders dan de rol uit de core.
Inventariseer zulke bronnen, projectnormen en testcommando's zonder credentials
te kopiëren. Controleer ook of eigen profielen `plan` of `accept-edits` vervangen.

Volg de kopieerprocedure in de
[technische adapterhandleiding](https://github.com/misja/agent-role-loop/blob/main/adapters/openai-compatible/mistral/README.md#inspect-before-installation).
De helper voegt alleen gewone bestanden onder `.vibe/role-loop/` toe; het manifest
bewaart hun herkomst en hashes. Bestaande AGENTS/configuratie wordt behouden.
Een conflict stopt vóór kopiëren. Inspecteer manifest en diff.

Maak PROJECT.md met projectnormen en het testcommando. In een nieuwe oefenmap
zonder AGENTS.md kun je de gekopieerde AGENTS.example.md na inspectie als ingang
gebruiken. Bij een bestaande ingang voeg je alleen een gerichte verwijzing toe.
Klaar wanneer de adapter leesbaar is en bestaande afspraken hun inhoud behouden.
De handleiding beschrijft rollback; jouw handmatige ingangsaanpassing valt daar
buiten en moet apart worden teruggedraaid.

### 2. De opdracht en expliciete rolinvoer voorbereiden

Bewaar het filterwerkitem met de vier bekende criteria in work-items/W1/C0.md.
Noteer basiscommit, coreversie en normen. Maak C1 volgens de gedeelde praktijk,
met PLANNED, verantwoordelijkheden, S1-S4 voor één onafhankelijke beoordelaar
en ontwerp-/opleveringsteller 0/0. De optionele parameter is een interfacekeuze
waarvoor je eerst een concreet plan wilt beoordelen.

Gebruik de gekopieerde role-task.md als invulvorm. Vervang alle hoofdlettervelden,
wijs rolbron en contractinvoer aan en geef het **absolute oefenpad** bovenaan:
`Working directory: /jouw/absolute/oefenpad; resolve project paths here.`
Plannerinvoer is C0+C1+PROJECT.md en de code/tests. Een issue-URL alleen levert
geen leesbare opdracht; neem de tekst met haar herkomst op. Bewaar de ingevulde
opdracht als planner-task.txt. Vraag een complete C2, zonder code te wijzigen.

Klaar wanneer de invoer rol, opdracht, criteria, normversies, bestandslocaties en
verwachte uitvoer aanwijst. De planner hoeft dan je eerdere gesprek niet te kennen.

### 3. Een nieuwe planner laten uitvoeren

Voer vanuit de oefenmap uit:

```sh
VIBE_INCLUDE_PROJECT_CONTEXT=false VIBE_ENABLE_CONNECTORS=false \
  vibe --workdir . --trust --agent plan \
  --enabled-tools read_file --enabled-tools grep \
  --max-turns 40 --max-price 2 --output json \
  -p "$(cat planner-task.txt)" > /tmp/W1-planner.json
```

`-p` geeft de ingevulde tekst aan een nieuwe Vibe-aanroep. De twee toegestane
modelgereedschappen lezen en zoeken; bewerken, shellcommando's en delegatie
worden niet aangeboden. De procesinstellingen vóór `vibe` schakelen automatische
projectcontext en connectors voor deze aanroep uit. Daarom heb je het absolute
pad en de normen zelf in de invoer gezet. Zij veranderen je opgeslagen
gebruikersconfiguratie niet. AGENTS-instructies kunnen nog steeds gelden.

`--trust` staat het laden van de geïnspecteerde projectbestanden voor deze run toe.
Het bewaart geen permanente trust en is geen inhoudelijk planakkoord. De
allow-list is geen OS-sandbox: leesbare bestanden en geconfigureerde hooks vragen
nog steeds aandacht. Gebruik daarom de afgesproken oefenomgeving.
`--max-turns` begrenst de roluitvoering; `--max-price` is een CLI-stopgrens in
dollars, geen gegarandeerde factuur. Bij een limiet of API-fout kan C2 ontbreken.

De CLI schrijft een JSON-lijst van berichten naar /tmp/W1-planner.json. Bekijk
het laatste assistant-bericht dat de complete C2 bevat. Gereedschapsberichten
zijn tussenstappen. Bewaar de contracttekst als work-items/W1/C2.md en houd het
volledige transcript buiten de reviewinvoer. Controleer C2 tegen het werkitem.
Een exitstatus 0 bewijst alleen dat het programma eindigde; een uitleg waarom
het niet kon lezen is geen plan. Een geweigerd pad vraagt een padcorrectie,
geen ruimere rechten. Bij account- of quotumfouten herstel je die voorwaarde
voordat je verdergaat. Klaar wanneer je een leesbaar, concreet C2 hebt.

### 4. Het concrete plan vrijgeven en rood bewijs verzamelen

Lees C2 en eventueel geselecteerde C3. Geef als mens PROCEED, REVISE of STOP
op de exacte planversie en bewaar C4 met reden en bron. Bij PROCEED ontvangt
de bouwer C1+C2+C4 en normen. Een bestaand akkoord geldt alleen voor dezelfde
keuzes; leg die vergelijking vast. Een nieuwe interface of scope vraagt een
nieuw besluit. Tooltoegang vervangt C4 niet.

Voer vóór bouwen zelf uit:

```sh
python3 -B controleer.py werk volledig
```

Bewaar volledige uitvoer en exitstatus bij W1 met het basiscommit. Op de basis
verwacht je één geslaagde controle en drie TypeErrors wegens het ontbrekende
argument, exit1. Lever dit bewijs aan de bouwer. Vibe heeft hier geen shelltool
en kan deze controle dus niet zelf uitvoeren.

### 5. Bouwen, groen controleren en de codecommit bewaren

Vul builder-task.txt in met bouwerrol, goedgekeurde invoer, absolute oefenpad
en rode testuitvoer. Vraag uitsluitend boekenplank.py te wijzigen en een C5-
concept terug te geven waarin nog niet uitgevoerde tests als ontbrekend staan.
Start een nieuwe aanroep:

```sh
VIBE_INCLUDE_PROJECT_CONTEXT=false VIBE_ENABLE_CONNECTORS=false \
  vibe --workdir . --trust --agent accept-edits \
  --enabled-tools read_file --enabled-tools grep \
  --enabled-tools write_file --enabled-tools edit \
  --max-turns 40 --max-price 2 --output json \
  -p "$(cat builder-task.txt)" > /tmp/W1-builder.json
```

`accept-edits` staat de aangeboden bestandsbewerkingen toe. `edit` heet in
Vibe 2.19.0 zo en vervangt tekst; het is niet `search_replace`. Shell, tests,
Git en trackeracties blijven menselijke handelingen. De schrijfbevoegdheid is
ruimer dan de opdracht om één bestand te veranderen; lees de werkelijke diff.
Voer zelf opnieuw de volledige controle uit. Verwacht vier geslaagde controles,
exit0. Bewaar uitvoer, exitstatus en de hash van de ongewijzigde controleer.py.

Bekijk C5-concept en vul pas nu het werkelijk uitgevoerde groene bewijs aan.
Bewaar alleen de productwijziging met Git. Voeg exact basis-/productcommit,
code uit die commit, criteria, besluiten en beperkingen aan C5-kern toe.
De technische handleiding beschrijft welke snapshot en bewijs de beoordelaar
nodig heeft; een modelclaim dat tests slagen is daarvoor niet genoeg.
Klaar wanneer C5 verwijst naar het product dat werkelijk is gecontroleerd.

### 6. Onafhankelijk beoordelen en begrensd herstellen

Maak reviewer-task.txt met strikte beoordelaarsrol, C5-kern, S1-S4, exacte
productcommit/snapshot en normen. Geef geen maaktranscript, plannerverhaal of
ander initial oordeel. Start de leesaanroep uit stap 3 met reviewer-task.txt en
/tmp/W1-reviewer.json. Gebruik geen `--continue` of `--resume`.

De beoordelaar leest code en tests, vergelijkt de aangeleverde commitsnapshot
met het bestand en beoordeelt jouw werkelijke testbewijs. Hij voert geen tests
of Git uit; vermeld dat onderscheid in C6. Bewaar zijn complete oordeel.
Een nieuwe conversatie verwijdert eerdere gespreksinvloed, maar geen geladen
instructies of leesbare bestanden. Houd de relevante bronnen bereikbaar en
maakgeschiedenis buiten het project.

Bij BLOCK registreer je de criteriumgebonden blocker en verbruikte herstelruimte
vóór reparatie. Geef de bouwer één gerichte herstelopdracht. Controleer de code
opnieuw en bewaar een nieuw exact commit en bijgewerkte C5. Een nieuwe
beoordelaarsaanroep krijgt expliciet repair-invoer: voor/na-diff, eerdere
blockers, eerder vastgestelde onaangetaste dekking en geregistreerde tellers.
Core bepaalt de toegestane ronde; een nieuw proces geeft geen extra ruimte.
Bij opnieuw BLOCK neemt de mens de vervolgbeslissing.

### 7. Oordeel en mensbesluit terugkoppelen

Bij SHIP besluit je afzonderlijk of de code mag worden overgenomen. Bewaar het
besluit met de beoordeelde commit. De mens plaatst contractuitkomsten in issue/PR
volgens de {ref}`bronmapping <praktijk-bronmapping>` en werkt een gebruikt bord bij.
Deze route geeft Vibe geen GitHub-toegang. Registreer ontbrekende externe acties.

Klaar wanneer het dossier opdracht, route, concreet planbesluit, codecommit,
werkelijke controle, onafhankelijke beoordeling en menselijke vervolgkeuze bevat.
Een technische proef bewijst die uitvoering met de gemeten tooling. Een
agentlezing onderzoekt de instructies. Zij bewijst geen zelfstandig studentgebruik;
studentwaarnemingen zijn daarvoor apart nodig.
