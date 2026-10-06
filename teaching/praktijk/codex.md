# Een werkitem uitvoeren met Codex

In het [gedeelde praktijkvoorbeeld](van-werkitem-naar-pull-request.md) draag je
opdracht, plan en bewijs tussen sessies over. Hier laat je afzonderlijke
Codex-aanroepen de rollen uitvoeren. Jij draagt hun contractuitvoer over,
controleert het bewijs en neemt de menselijke besluiten.

Lees dit na module 2 en het praktijkvoorbeeld. Je gebruikt terminalcommando's,
Git en Python-tests. De [voorbereiding](../van-chat-naar-agent.md) legt model,
uitvoerend programma, sessie en rol uit. Codex is het programma dat een model
om vervolgstappen vraagt en toegestane gereedschapsacties uitvoert. OpenAI levert
in deze route modeltoegang; de oefenrepository levert code en projectafspraken.

## Voorbereiden

Gebruik een aparte oefenrepository met Python 3.10 of nieuwer, Git en de Codex CLI. Je hebt
een account met toegang tot het gekozen model nodig. Volg de
[officiële Codex-hulp](https://learn.chatgpt.com/docs/codex/cli)
voor de CLI; controleer installatie en aanmelding:

```sh
codex --version
codex login status
```

Een ontbrekend commando vraagt eerst installatie; een ontbrekende aanmelding
vraagt eerst de accountstap. Loginstatus bewijst nog geen geslaagde modelaanroep
of beschikbaar quotum. Bewaar geen accountidentiteit of tokens in je dossier.
Gebruik voor deze eerste proef geen project met echte gebruikersgegevens.

Download de bundel bij het gedeelde praktijkvoorbeeld. Neem boekenplank_basis.py
als boekenplank.py en controleer.py in de oefenmap. De tests gebruiken de
Python-standaardbibliotheek, zonder extra dependency. Initialiseer Git en bewaar
de basis met je gebruikelijke Git-werkwijze. Controleer in de oefenmap:

```sh
python3 -B controleer.py werk basis
```

Verwacht een geslaagde basiscontrole. `-B` voorkomt schrijven van Python-
bytecodecache; daardoor kunnen dezelfde controles later zonder projectschrijfrecht
draaien. Als modeltoegang ontbreekt, gebruik de
[handmatige sessieroute](van-werkitem-naar-pull-request.md) en registreer die keuze.
Die vervanging is geen uitgevoerde Codex-proef.

## Stappen

### 1. Projectafspraken inventariseren en adapter toevoegen

Bekijk AGENTS.md, AGENTS.override.md en bestaande Codex-configuratie. AGENTS
is de projectingang die Codex aan het begin leest; een override kan een andere
ingang voorrang geven. Ook instructies en instellingen van je gebruiker of
organisatie kunnen gelden. Noteer toepasselijke normbestanden, testcommando's
en relevante toegang zonder credentials over te nemen.

Volg de kopieerprocedure in de
[technische adapterhandleiding](https://github.com/misja/agent-role-loop/blob/main/adapters/codex/README.md#copy-and-inspect).
De helper voegt alleen bestanden onder `.codex/role-loop/` toe. Het manifest
bewaart welke bytes zijn gekopieerd; bestaande AGENTS/configuratie wordt niet
vervangen. Bij een conflict stopt installatie vóór kopiëren. Controleer de
diff en het manifest voordat je verdergaat.

Voor een nieuwe oefenmap zonder AGENTS.md kun je de gekopieerde
AGENTS.example.md na inspectie als ingang gebruiken. Zij verwijst naar de
adapter en naar PROJECT.md. Bij een bestaande ingang voeg je een gerichte
verwijzing toe na vergelijking met de projectafspraken. Controleer dat de
bedoelde ingang geldt. Klaar wanneer de adapter leesbaar is en bestaande
instructies hun inhoud behouden. Rollback van gekopieerde bestanden staat in
de handleiding; jouw eigen ingangsaanpassing beoordeel je afzonderlijk.

### 2. De opdracht en expliciete rolinvoer voorbereiden

Schrijf het filterwerkitem met de vier bekende criteria in work-items/W1/C0.md.
Bewaar projectnormen en het testcommando in PROJECT.md. Noteer de basiscommit
en de exacte versie van de geïnstalleerde core. De boekencasus blijft gelijk;
Claude-configuratie verleent deze Codex-aanroepen geen gereedschapsrechten.

Iedere aanroep krijgt een tekstbestand als opdracht. Gebruik de gekopieerde
role-task.md als invulvorm en vervang alle hoofdlettervelden. Geef de rolbron,
contractinvoer, criteria, normen en bestaande besluiten aan. Voor een planner
zijn dat C0, C1 en projectfeiten; jij maakt C1 met route, verantwoordelijkheden,
criteriatoewijzing en herstelstand volgens de gedeelde praktijk. Gebruik hier
PLANNED vanwege de optionele parameter als interfacekeuze.

Bewaar de ingevulde planneropdracht als planner-task.txt. Zij vraagt een C2 en
stopt vóór bouwen. De rolbron zegt hoe de planner werkt, C0 zegt wat verandert,
PROJECT.md begrenst die opdracht. Een onbereikbare issue-URL levert geen tekst;
geef dan de volledige opdracht met haar herkomst mee. Klaar wanneer de rol
alles kan lezen zonder je eerdere chat nodig te hebben.

### 3. Een nieuwe planner laten uitvoeren

Voer vanuit de oefenmap uit:

```sh
codex -a never exec -C . -s read-only --ephemeral \
  -o /tmp/W1-C2.md - < planner-task.txt
```

`exec` begint een nieuwe aanroep met de tekst via standaardinvoer. `read-only`
begrenst modelgereedschappen tot lezen; de planner kan zo geen code aanpassen.
`-a never` vraagt geen toolgoedkeuring en geeft een geweigerde actie als fout
terug; het schakelt de sandbox niet uit. `--ephemeral` bewaart geen sessierollout,
maar verwijdert geen geladen projectinstructies. De CLI bewaart het laatste
antwoord in het genoemde uitvoerbestand, ook wanneer de rol zelf alleen mag lezen.

Lees de daadwerkelijk teruggegeven C2. Controleer of de bestaande oproep gelijk
blijft en filtering de opgeslagen boeken behoudt. Bewaar dit C2 bij W1 met zijn
bron. Een API-, quotum- of sandboxfout is geen voltooid plan; los de ontbrekende
voorwaarde op voordat je bouwt. Een nieuwe aanroep is onafhankelijk van eerdere
conversatie, maar kan nog steeds toegankelijke bestanden lezen.

### 4. Het concrete plan vrijgeven

Lees C2 en eventueel geselecteerde C3. Geef als mens PROCEED, REVISE of STOP
op de exacte versie, met je reden, en bewaar C4 met zijn bron. Bij PROCEED
krijgt de bouwer C1, C2, C4 en normen; anders bouwt hij niet verder.
Een bestaand besluit geldt alleen voor dezelfde concrete keuzes. Leg de
vergelijking vast; een veranderd doel of andere interface vraagt een nieuw
besluit. Tooltoegang is geen inhoudelijk planakkoord.

### 5. Bouwen, werkelijke tests lezen en een codecommit bewaren

Vul een builder-task.txt in met de bouwerrol en de vrijgegeven invoer. Vraag
alleen boekenplank.py te wijzigen, de aangeleverde controle intact te houden
en eerst rood op de basis, daarna groen op de implementatie te bewaren.
Voer een nieuwe aanroep uit:

```sh
codex -a never exec -C . -s workspace-write --ephemeral \
  -o /tmp/W1-C5.md - < builder-task.txt
```

`workspace-write` geeft modelgereedschappen schrijfrecht in de werkplek. Dat is
ruimer dan jouw opdracht om één bestand te wijzigen; bekijk daarom de echte
diff. Laat vóór en na de wijziging dit commando uitvoeren:

```sh
python3 -B controleer.py werk volledig
```

Verwacht op de basis één geslaagde controle en drie TypeErrors wegens het
ontbrekende argument; na de wijziging vier geslaagde controles. Lees de echte
uitvoer en exitstatus. Een voorgesteld commando is nog geen uitgevoerd bewijs.
Bij geweigerde toegang onderzoek je de gevraagde handeling; gebruik geen bypass
om een foutmelding weg te nemen. De technische naslag beschrijft JSON-uitvoer
als je uitgevoerde gereedschapsacties afzonderlijk wilt bewaren.

Bekijk de productdiff, voer de controles zo nodig zelf uit en bewaar de code
met Git. Vul die exacte commit in C5-kern aan, samen met criteria, normversies,
besluiten, testbewijs en beperkingen. Jij beheert Git en de terugkoppeling naar
issue/PR; de bouwer krijgt hier geen tracker- of mergeopdracht.

### 6. Een onafhankelijke beoordeling en begrensd herstel uitvoeren

Maak reviewer-task.txt met de strikte beoordelaarsrol, C5-kern, toegewezen
criteria, exact codecommit en normen. Geef geen maakgesprek, plannerverhaal
of ander initial oordeel. Start weer een nieuwe aanroep:

```sh
codex -a never exec -C . -s read-only --ephemeral \
  -o /tmp/W1-C6.md - < reviewer-task.txt
```

Gebruik hiervoor geen resume of fork. De nieuwe conversatie beperkt eerdere
gespreksinvloed; geladen AGENTS en leesbare bestanden blijven toegankelijk.
Houd transcripten buiten de oefenmap en vermeld welke bronnen nodig zijn.
Controleer dat de tests bij de beoordeelde commit horen en bewaar C6.

Bij BLOCK leg je de concrete blocker en herstelstand vast vóór reparatie.
Een nieuwe bouweropdracht herstelt de bestaande wijziging. Een nieuwe
beoordelaarsaanroep krijgt expliciet repair-invoer: aangepaste C5, voor/na-diff,
eerdere blockers, nog geldige eerdere dekking en de geregistreerde tellers.
De toegestane ronde en menselijke vervolgstap staan in core; een nieuw proces
geeft geen extra herstelruimte.

### 7. Het oordeel en mensbesluit terugkoppelen

Bij SHIP besluit je afzonderlijk of het product mag worden overgenomen.
Bewaar het besluit met de beoordeelde commit. Als je issues/PR's gebruikt,
plaatst de mens de contractuitkomsten volgens de
{ref}`bronmapping <praktijk-bronmapping>`. Werk een gebruikt bord daarna bij.
Een statuskaart vervangt geen besluitbron. Registreer ontbrekende externe acties;
de lokale route bewijst geen native GitHub-reviewintegratie.

Klaar wanneer het dossier opdracht, route, concreet planbesluit, codecommit,
uitgevoerde controle, onafhankelijke beoordeling en menselijke vervolgkeuze
bevat. Een technische proef bewijst deze uitvoering met de gekozen tooling.
Een onafhankelijke agentlezing onderzoekt de instructies. Studentwaarnemingen
zijn nodig om zelfstandig gebruik of begrip door studenten vast te stellen.
