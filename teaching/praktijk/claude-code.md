# Een werkitem uitvoeren met Claude Code

In het [gedeelde praktijkvoorbeeld](van-werkitem-naar-pull-request.md) draag je
opdracht, plan en testbewijs zelf tussen sessies over. Hier laat je Claude Code
rollen uitvoeren in een lokale repository. Jij controleert de overdrachten en
neemt de menselijke besluiten. De afspraak over beschikbare boeken blijft gelijk.

Lees dit na module 2 en het praktijkvoorbeeld. Je gebruikt terminalcommando's,
Git en Python-tests. De [voorbereiding](../van-chat-naar-agent.md) legt model,
uitvoerend programma, sessie en rol uit. Claude Code is dat uitvoerende programma:
het vraagt een model om vervolgstappen en voert toegestane gereedschapsacties uit.
Een account geeft modeltoegang; projectbestanden geven de inhoud van de opdracht.

## Voorbereiden

Gebruik een aparte oefenrepository. Gebruik voor deze eerste proef geen project
met echte gebruikersgegevens. Je hebt Python 3, Git, Claude Code en een account
met toegang tot het gekozen model nodig. Volg voor installatie en aanmelden de
[officiële installatiehulp](https://code.claude.com/docs/en/setup). Een
terminal waarin `claude --version` niet werkt, kan de volgende stappen niet uitvoeren.

Download de bundel bij het praktijkvoorbeeld en pak haar uit. Neem
`boekenplank_basis.py` als `boekenplank.py` en `controleer.py` in de oefenmap.
De controle gebruikt de Python-standaardbibliotheek; een nieuwe dependency is
niet nodig. Initialiseer Git en bewaar de basis met je gebruikelijke Git-werkwijze.
Voer in de oefenmap uit:

```sh
python3 controleer.py werk basis
claude --version
claude auth status
```

De basiscontrole moet slagen. Het versiecommando noemt de CLI-versie. De
accountcontrole meldt of je bent aangemeld; zij bewijst nog niet dat een
modelaanroep zal slagen. Bewaar geen accountgegevens of tokens in het dossier.
Bij ontbrekende toegang los je eerst de accountstap op of gebruik je de
[handmatige sessieroute](van-werkitem-naar-pull-request.md). Beschrijf die keuze;
zij is geen uitgevoerde Claude Code-proef.

## Stappen

### 1. Projectafspraken en installatie controleren

Bekijk bestaande `CLAUDE.md`, `AGENTS.md` en configuratie onder `.claude/`.
Deze bestanden kunnen instructies of gereedschapsrechten toevoegen. Ook
gebruikers- en organisatie-instellingen kunnen gelden. Noteer de normbestanden,
testcommando's en relevante instellingen, zonder credentials over te nemen.
Zo voorkom je dat een nieuwe installatie bestaande afspraken vervangt.

Volg de kopieerinstallatie in de
[technische adapterhandleiding](https://github.com/misja/agent-role-loop/blob/main/adapters/claude-code/README.md#copy-installation).
Die voegt rolbestanden, het commando `orc` en dezelfde core toe en bewaart een
manifest van de gekopieerde bestanden. Bij een naamconflict stopt de kopie;
los het conflict eerst op. Controleer daarna de Git-diff en het manifest.
Klaar wanneer de eigen adapterbestanden aanwezig zijn en bestaande afspraken
ongewijzigd zijn. Het manifest ondersteunt ook het gecontroleerd ongedaan maken
van een ongewijzigde installatie.

### 2. Opdracht en normbronnen aanbieden

Schrijf het filterwerkitem uit het praktijkvoorbeeld in `work-items/W1/C0.md`.
Gebruik de vier criteria over standaardvolgorde, beschikbare selectie, lege
selectie en behoud van boeken/status. Bewaar de projectafspraken in een
vindbaar bestand, bijvoorbeeld `PROJECT.md`. Noteer de basiscommit en de
versie van de geïnstalleerde core. Een branchnaam alleen legt geen vaste versie vast.

Het commando `/orc` orkestreert: het geeft de gekozen rollen hun opdracht en
neemt hun contractuitvoer terug. Een rolbestand beschrijft hoe een rol werkt;
het werkitem bevat wat er moet veranderen. Geef daarom beide, plus de normen,
mee. Een onbereikbare issue-URL vervangt geen opdrachttekst. Lever dan de
volledige tekst met haar herkomst aan. Klaar wanneer een rol de opdracht en
normen kan lezen zonder jouw eerdere chatgesprek nodig te hebben.

### 3. Route en concreet plan laten vastleggen

Start `claude` in de oefenmap. Begin een nieuwe sessie na installatie. Geef:

```text
/orc work-items/W1/C0.md
Gebruik PROJECT.md als projectnorm en noteer de basiscommit en core-versie.
Bewaar contracten bij work-items/W1/. Laat eerst C1 en het benodigde C2 zien.
Stop vóór bouwen voor mijn besluit op dat concrete plan.
```

C1 benoemt de route en wijst ieder criterium aan een geschikte onafhankelijke
beoordelaar toe. Het nieuwe optionele argument is een interfacekeuze; een
PLANNED-plan moet vastleggen dat de bestaande oproep gelijk blijft en het
filter de opgeslagen verzameling niet verandert. Controleer dit in het
werkelijk teruggegeven C2. Laat ontbrekende keuzes beantwoorden voordat je
verdergaat. Een API-fout of geweigerde gereedschapsactie is geen voltooid plan.

### 4. Zelf over het plan beslissen

Lees C2 en eventueel geselecteerde C3. Geef PROCEED, REVISE of STOP op de
exacte planversie, met de reden. Bewaar het besluit als C4 met zijn bron.
Bij PROCEED krijgt de bouwer dat plan, C1, normen en besluit. Bij REVISE of
STOP bouwt hij niet verder. Goedkeuring van een toolactie geeft alleen
uitvoeringstoegang; zij vervangt dit inhoudelijke mensbesluit niet.

### 5. Bouwen, controleren en een codeversie bewaren

Laat de bouwer eerst de relevante falende controle op de basis uitvoeren en
vervolgens het filter implementeren. Laat hem de volledige suite uitvoeren:

```sh
python3 controleer.py werk volledig
```

Verwacht vier geslaagde controles na de wijziging. Bekijk de waargenomen
uitvoer; een voorgesteld testcommando is nog geen uitgevoerd commando. Bij een
permissionmelding controleer je welke handeling toegang vraagt. Sta voor de
proef alleen benodigde bestandsacties en het concrete testcommando toe;
verleen geen algemene bypass om een foutmelding kwijt te raken.
Voer toegestane testcommando's afzonderlijk uit. Een combinatie met bijvoorbeeld
een extra shellcommando kan alsnog worden geweigerd. Je kunt `python3 -B` gebruiken
om tijdens de controle geen bytecodecache te schrijven; leg die commandovariant
vast in het plan en de testregistratie.

Bekijk de code-diff en bewaar het product met Git. Neem de echte commit in C5
op, samen met criteria, besluiten, testuitvoer en bekende beperkingen. Jij
verzorgt in deze eerste route commits en terugkoppeling naar issue/PR. Claude
krijgt geen opdracht om trackergegevens te wijzigen of te merge.

### 6. Onafhankelijk beoordelen en gericht herstellen

Geef de gekozen beoordelaar C5-kern, toegewezen criteria, codecommit en geldige
normen. Laat hem in een verse rolcontext beginnen. Geef geen maakgesprek of
ander initial oordeel mee. Gebruik voor initial review en herreview geen fork
of hervatting van de vorige beoordelaar. De adapter biedt normbestanden
expliciet aan; controleer welke andere instructies of rechten werkelijk laden.
Een eigen gesprek voorkomt niet dat een agent toegankelijke bestanden kan lezen.

Bewaar C6 op de beoordeelde commit. Bij BLOCK registreer je de concrete blocker
én de herstelstand voordat de bouwer repareert. Geef een nieuwe beoordelaar
bij herreview de expliciete herstelbijlage met voor/na-diff, eerdere blocker en
nog geldige eerdere dekking. De toegestane ronde en menselijke vervolgstap
staan in de core; een nieuwe sessie geeft geen nieuwe herstelruimte.

### 7. Uitkomst en mensbesluit terugkoppelen

Bij SHIP besluit je afzonderlijk of het product mag worden overgenomen.
Bewaar de beslissing met de beoordeelde commit. Als je een issue/PR gebruikt,
plaatst de mens de contractuitkomsten bij de aangewezen bronnen uit de
{ref}`bronmapping <praktijk-bronmapping>`.
Werk daarna de bordstatus bij. Een statuskaart is geen besluitbron.

Klaar wanneer het dossier de opdracht, route, geldig planbesluit, codeversie,
uitgevoerde controle, onafhankelijke beoordeling en menselijke vervolgkeuze
bevat. Noteer ook welke externe stappen niet zijn uitgevoerd. De lokale
bestandsroute bewijst geen native GitHub-review of accountrechten.

## Wat deze route aantoont

Een werkelijk uitgevoerde proef kan aantonen dat de gekozen CLI, configuratie
en roluitvoering deze wijziging verwerken. Een onafhankelijke lezing kan
ontbrekende instructiestappen vinden. Voor bewijs dat studenten de route
zelfstandig kunnen gebruiken zijn studentwaarnemingen nodig. Houd die drie
soorten bewijs in je verslag uit elkaar.
