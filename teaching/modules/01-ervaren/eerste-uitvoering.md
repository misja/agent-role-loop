# De eerste uitvoering met losse chats

Lees dit voorbeeld na deel A en de les, vóór je zelf aan deel B begint.
Je volgt portie 1 van de boekenplankopdracht: een opdracht vastleggen, een plan
laten maken, code toepassen en het resultaat laten beoordelen.

Dit is een geconstrueerd onderwijsvoorbeeld. De documenten, codeversie B1,
besluiten en controle-uitkomsten hieronder zijn illustraties van een uitvoering.
Er is voor dit voorbeeld geen code of agentrun uitgevoerd. Bij je eigen werk
bewaar je de echte codeversies en waargenomen uitkomsten.

## 1. Jij legt de opdracht vast

Een **werkitem** beschrijft wat er moet werken. W1 is hier het werkitem voor
portie 1, versie 1. C0 is de naam van het bijbehorende
{core}`contracts/work-item.md`.

**Ingevuld werkitem W1:**

- Titel: Bouw de eerste versie van de boekenplank.
- Aanleiding: een kleine bibliotheek wil boeken registreren en uitleningen bijhouden.
- Uitkomst: een command-line-tool met de vijf handelingen uit portie 1.
- Criteria: requirements 1 tot en met 5 uit [de oefening](oefening.md), met dezelfde nummers.
- Grenzen: taal naar keuze; werk in een nieuwe map met oefengegevens.
  Requirements 6 tot en met 15 worden later aangeboden.
- Geschatte omvang: M.

Bewaar W1 in je overdrachtslogboek. Voeg de vijf requirements er volledig aan toe;
een verwijzing moet voor de volgende rol leesbaar zijn. Je hebt nog geen AI nodig
om deze opdracht te beschrijven.

## 2. Jij kiest de taken en gesprekken

Je schrijft een {core}`contracts/triage-decision.md` (C1). Dat document legt vast
wie welke criteria beoordeelt en welke regels iedereen gebruikt.

**Ingevulde C1 voor W1:**

- Route: `PLANNED`; de nieuwe applicatie vraagt een plan vóór de bouw.
- Omvang: M, beperkt tot portie 1.
- Uitvoerders: jij organiseert het werk en neemt de menselijke besluiten;
  aparte chats voor planner, verhelderaar, bouwer en de vier geselecteerde
  beoordelaars. Vier perspectieven dienen hier de oefening.
- Toewijzing: strikt en pragmatisch beoordelen 1 tot en met 5; adversarieel 1, 3 en 5;
  onderhoudbaarheid 2, 4 en 5. Elk criterium heeft dus een onafhankelijke beoordelaar.
- Risico: je kunt met de verkeerde opslagmap werken. Gebruik alleen oefengegevens
  in de nieuwe map; bestaande gegevens uit deel A blijven apart.
- Herstelstand W1: ontwerp 0, oplevering 0; bewaar deze tellers in het logboek.
- Mensbesluiten: jij beslist over het concrete plan vóór bouw en over het
  resultaat na beoordeling. Er is nog geen besluit genomen.

De gezamenlijke **grondslag N1** bij deze C1 bevat de vijf eisen uit W1 versie 1
en de procesbron op commit `e0f064aa7e5642b272d82e5db227e9b53d6a5de4`:
{core}`loop.md`, rolprompts en contracten. Er zijn voor dit voorbeeld geen extra
codeconventies of coverage-drempels afgesproken. N1 is een naam voor dit
voorbeeldpakket. Geef bij je eigen uitvoering de werkelijk gekozen procesversie,
projectregels en leesbare bestanden mee; een versienummer alleen is geen invoer.

## 3. De planner maakt het plan

Open een nieuwe chat. Geef {core}`roles/planner.md`, W1, C1 en N1 mee en voeg toe:

```text
Maak C2 voor W1 versie 1. Gebruik alleen requirements 1 tot en met 5.
Beschrijf hoe de vijf handelingen worden gecontroleerd.
Noteer aannames en vragen; er is nog geen bestaande code.
```

De planner levert een {core}`contracts/build-packet.md` (C2).
**P1** is hieronder het ingevulde plan, versie 1:

- Samenvatting/doel: een CLI die boeken registreert, uitleent en terugneemt,
  met gegevens die een volgende aanroep kan lezen.
- Buiten scope: zoeken, uitleendatum, verwijderen en de overige latere eisen.
- Huidige toestand: een nieuwe werkmap zonder bestaande code of data.
- Aanpak: verdeel de CLI-afhandeling en opslag over afzonderlijke componenten.
  Bewaar nummer, titel, auteur, status en lener. Gebruik voor deze versie JSON
  in de werkmap; dat is een planvoorstel binnen het vrije formaat van eis 5.
- Criteria/toewijzing: neem 1 tot en met 5 en de beoordelaars uit C1 over.
- Bronnen: W1 versie 1, C1 en het leesbare N1-pakket.
- Herstelstand: ontwerp 0, oplevering 0.
- Interface/data: de vijf opgegeven CLI-commando's; een nieuw opslagbestand met
  oefengegevens. Er is geen migratie van bestaande data.
- Wijziging: maak CLI, opslag en controles. Controleer toevoegen/lijst,
  uitlenen/terugbrengen en bewaren tussen aanroepen. Bestandnamen worden pas
  bij de bouw gekozen; er zijn nog geen repositorybestanden om aan te wijzen.
- Verificatie: `manual-with-expected-results`, controles K1 tot en met K5 hieronder.
  Er is geen bestaande geteste codebasis; deze eerste proef controleert de
  voorgeschreven CLI-handelingen. Een latere automatische test kan dezelfde
  verwachtingen gebruiken.
- Gereed wanneer: alle vijf controles leveren hun verwachte uitkomst op.
  Terugval: behoud de vorige codeversie; gebruik steeds aparte oefengegevens.
- Risico/aannames: de gekozen taal kan de CLI en JSON-bestanden verwerken;
  controleer dat in de bouwomgeving. Bestaande gegevens worden niet overschreven.
- Open vraag voor jou: akkoord met JSON en de nieuwe werkmap? De eisen laten
  het formaat nu vrij; de planner kan de keuze ter besluit voorleggen.

**Controleplan bij P1:** begin met een lege opslagmap. Start ieder commando als
een nieuwe programma-aanroep. De nummers 1 en 2 zijn voorbeeldwaarden; de eis
vraagt oplopende nummers, geen verplicht beginnummer.

| Controle | Handeling | Verwachte uitkomst en criterium |
|---|---|---|
| K1 | `boekenplank toevoegen Dune Herbert`, daarna `boekenplank toevoegen Solaris Lem` | Twee boeken met oplopende nummers; criterium 1. |
| K2 | `boekenplank lijst` | Beide boeken met nummer, titel, auteur en status aanwezig; criterium 2. |
| K3 | `boekenplank uitlenen 1 Noor`, daarna `boekenplank lijst` | Boek 1 is uitgeleend aan Noor; criterium 3. |
| K5 | Sluit het programma na K3. Start vanuit dezelfde opslagmap opnieuw `boekenplank lijst`. | Beide boeken en de uitlening aan Noor zijn behouden; criterium 5. |
| K4 | `boekenplank terug 1`, daarna `boekenplank lijst` | Boek 1 is weer aanwezig; criterium 4. |

De tabel geeft de uitvoervolgorde: K5 controleert de bewaarde uitlening vóór
K4 het boek terugmeldt. Deze controles gebruiken alleen requirements 1 tot en met 5.

## 4. De verhelderaar controleert het plan

Open een andere chat met {core}`roles/clarifier.md`, W1, C1, P1 en N1:

```text
Beoordeel P1 versie 1 volgens C3. Controleer voor ieder criterium
of de handeling en verwachte uitkomst duidelijk zijn.
De keuze voor JSON ligt nog bij de mens.
```

**Ingevulde planreview, {core}`contracts/clarifier-result.md` (C3):**

- Modus/artefact: initial, P1 versie 1, N1.
- Criteriadekking: 1 tot en met 5 hebben controles K1 tot en met K5 en beoordelaars in C1;
  nieuw onderzocht in deze voorbeeldreview.
- Herstelstand: ontwerp 0, oplevering 0.
- Oordeel: `PASS`.
- Reden: handelingen, verwachtingen en de nieuwe opslagmap zijn bepaald.
  De formaatkeuze is een expliciete vraag voor het mensbesluit.
- Noodzakelijke wijzigingen/vragen: geen. Risico: verkeerde opslagmap gebruiken.

PASS betekent hier dat je het plan kunt beoordelen. De bouwer begint nog niet.

## 5. Jij beslist over P1

Lees W1, P1 en de planreview. Jij legt de
{core}`contracts/gate-decision.md` (C4) vast. Een chat kan dit besluit niet nemen.

**Ingevuld voorbeeldbesluit:**

```text
Bron: student Sam, logboek W1, besluit 1, na het lezen van P1 v1 en C3.
Artefact/grondslag: P1 versie 1, C3 PASS, N1.
Besluit: PROCEED.
Reden: de vijf eisen zijn controleerbaar en de oefengegevens staan apart.
Menselijke keuze: JSON is akkoord voor portie 1 in de nieuwe werkmap.
Vereiste wijzigingen vóór bouw: geen.
Veilig uitgestelde vragen: geen.
```

Dit voorbeeldbesluit geldt alleen voor het beschreven voorbeeld. Neem bij jouw
eigen uitvoering zelf een besluit over jouw plan en bewaar de bron en versie.
Bij `REVISE` of `STOP` volg je eerst de vastgelegde vervolgactie.

## 6. De bouwer stelt code voor; jij past haar toe

Open het bouwergesprek met {core}`roles/builder.md`, C1, P1, C4, W1 en N1.
Geef ook de beschikbare werkmap en bouwomgeving aan:

```text
Voer P1 versie 1 uit binnen het C4-besluit. Werk alleen aan eisen 1 tot en met 5.
Deze chat kan geen bestanden wijzigen of controles uitvoeren.
Geef het codevoorstel en de opdrachten voor mijn gekozen taal.
Gebruik mijn teruggestuurde uitvoer voor C5; verzin geen testresultaten.
```

Neem het voorstel over in je bestanden. Voer de voorgeschreven controles uit
en stuur de uitvoer terug. Verschilt zij van de verwachting, laat dan de bouwer
de oorzaak onderzoeken en controleer de aanpassing opnieuw. Bewaar daarna de
code en resultaten als één versie. **B1** is hier de naam van die voorbeeldversie;
gebruik zelf een echte commit met diff en leesbare bestanden.

De bouwer maakt {core}`contracts/review-handoff.md` (C5). De C5-kern bevat in
dit voorbeeld:

- Artefact: W1, snapshot B1, vergelijking met de lege beginmap. B1 is alleen
  een voorbeeldnaam; er is hier geen uitvoerbare snapshot of echte commit.
- Grondslag/besluit: N1, W1 v1, C1, P1 v1 en Sams C4-besluit 1.
- Wijzigingen: CLI toegevoegd; opslag toegevoegd; controles vastgelegd.
  Geraakte componenten: CLI-afhandeling en opslag.
- Criteriadekking: 1 → K1, 2 → K2, 3 → K3, 4 → K4, 5 → K5;
  toewijzing aan de beoordelaars blijft die van C1.
- Bewijs: logboek W1 met handelingen, verwachtingen en onderstaande
  voorbeeldwaarnemingen bij B1. Er was geen werkende voorganger om te vergelijken.
- Contracten/data: de vijf CLI-commando's, nieuw JSON-opslagbestand;
  geen bestaande data gemigreerd.
- Afwijkingen/vervolg: geen; alleen portie 1 uitgevoerd.
- Herstelstand: ontwerp 0, oplevering 0.

| Controle | Waarneming in het geconstrueerde logboek |
|---|---|
| K1 | Dune krijgt nummer 1, Solaris nummer 2. |
| K2 | Beide titels/auteurs en status aanwezig staan in de lijst. |
| K3 | Dune staat als uitgeleend aan Noor in de lijst. |
| K5 | Een nieuwe aanroep leest dezelfde boeken en uitlening. |
| K4 | Na terugmelden staat Dune weer als aanwezig in de lijst. |

Beperkingen: foutafhandeling en de latere requirements zijn niet onderzocht.
De controles tonen de genoemde gevallen; zij bewijzen geen algemene foutloosheid.
Extra maakgeschiedenis blijft buiten de C5-kern. Er is hier geen afzonderlijke
geschiedenis nodig voor beoordeling; het uitgebreide deel vermeldt daarom geen
extra bronnen.

## 7. Vier beoordelaars lezen onafhankelijk

Open vier nieuwe gesprekken. Geef ieder zijn eigen rolprompt, C5-kern, W1,
P1/C4, N1, leesbare codeversie en controlelog. Het bouwergesprek en de andere
beoordelingen gaan niet mee. Bij jouw uitvoering is dat je echte code; dit
voorbeeld laat alleen zien hoe de ingevulde beoordelingen worden bewaard.

Gebruik per gesprek de taak in deze tabel:

| Rolprompt | Aanvullende opdracht voor deze C6 |
|---|---|
| {core}`roles/reviewer-strict.md` | Beoordeel criteria 1 tot en met 5 tegen code en bewijs K1 tot en met K5. |
| {core}`roles/reviewer-pragmatic.md` | Beoordeel criteria 1 tot en met 5 binnen portie 1; maak latere wensen niet tot nieuwe eisen. |
| {core}`roles/reviewer-adversarial.md` | Beoordeel 1, 3 en 5; onderzoek nummering, uitleenstatus en het opnieuw lezen van opslag. |
| {core}`roles/reviewer-maintainability.md` | Beoordeel 2, 4 en 5; onderzoek hoe lijst, terugmelden en opslag worden gewijzigd. |

Voeg telkens toe: “Lever {core}`contracts/reviewer-verdict.md` (C6) met bewijs
per toegewezen criterium. Benoem niet-onderzochte onderdelen.” Bewaar alle
vier oordelen voordat je ze vergelijkt.

**Ingevulde voorbeeldbeoordelingen:**

| Oordeel/bron | Nieuw onderzochte dekking in het voorbeeld | Besluit |
|---|---|---|
| G-S, strikt | 1 tot en met 5 pass: K1 oplopende nummers, K2 velden/status, K3 lener/status, K4 terugmelden, K5 behouden gegevens, gekoppeld aan B1. | SHIP |
| G-P, pragmatisch | 1 tot en met 5 pass op dezelfde vijf waargenomen handelingen. De scope blijft portie 1; niet onderzochte foutgevallen zijn geen extra criteria. | SHIP |
| G-A, adversarieel | 1/3/5 pass: twee registraties, bewaren van lener/status en een nieuwe aanroep zijn in K1/K3/K5 onderzocht. 2/4 zijn elders toegewezen. | SHIP |
| G-M, onderhoudbaarheid | 2/4/5 pass: K2/K4/K5 plus de in B1 afzonderlijk beschreven CLI- en opslagcomponenten. 1/3 zijn elders toegewezen. | SHIP |

Elke voorbeeld-C6 heeft als modus/artefact initial, B1 en N1. Contractafwijkingen,
must fix, should fix, nice to have en hersteluitkomst: geen. Volgende stap:
wacht op de overige geselecteerde oordelen en maak C7. Deze uitkomsten zijn
geconstrueerd; er is geen codeonderzoek of echte reviewrun uitgevoerd.
Bij je eigen werk mag een niet onderzocht toegewezen criterium niet op pass staan.

## 8. Jij brengt de oordelen samen en beslist

De vier voorbeeldbeoordelingen zijn verenigbaar. Jij schrijft daarom een
{core}`contracts/final-verdict.md` (C7):

```text
Modus/uitvoerder: synthese door Sam als orkestrator.
Invoer: C5 bij B1 en alle vier C6's G-S/G-P/G-A/G-M; geen oordeel ontbreekt.
Grondslag: N1 en het C4-besluit over P1 versie 1.
Eindoordeel: SHIP.
Dekking: 1 tot en met 5 pass volgens G-S/G-P; 1/3/5 ook G-A, 2/4/5 ook G-M.
Bronnen: de dekkingstabellen en K1 tot en met K5 bij B1.
Contractafwijking en must/should/nice bevindingen: geen.
Meningsverschillen: geen; geen hoofdbeoordelaar nodig.
Volgende stap: mens beslist of B1 als basis voor portie 2 wordt overgenomen.
```

Je laat alleen inhoudelijke tegenspraak aan de hoofdbeoordelaar onderzoeken.
Een `BLOCK` vraagt herstel volgens {core}`loop.md`: registreer de verbruikte
ronde vóór herstel en geef een verse beoordelaar de expliciete herstelbijlage.
Een resterende blokkade vraagt een menselijk vervolg. De rondelimiet maakt de
blokkade niet ongedaan.

Lees het eindoordeel en beslis zelf over jouw code. In dit voorbeeld bewaart Sam:
“Logboek W1, besluit 2: ik neem B1 over als basis voor portie 2, op basis van C7
en K1 tot en met K5. Alleen eisen 1 tot en met 5 zijn onderzocht.” Dat is een ander besluit dan de
eerdere toestemming om P1 uit te voeren.

## 9. Je begint het volgende werkitem

W2 wordt het eigen werkitem voor portie 2. Neem requirements 6 tot en met 10 op als nieuwe
criteria en geef de geaccepteerde codeversie plus eisen 1 tot en met 5 mee als behouden
gedrag. De controles voor die eerdere eisen blijven nodig. Houd voor W2 een
eigen logboek en herstelstand bij. Werk daarna op dezelfde manier aan W3 voor
portie 3: in totaal drie werkitems.

Ga terug naar {ref}`deel B van de oefening <module1-deel-b>`.
Bereid je eerste plannerchat voor met je eigen C0, C1, leesbare normen en de
rolprompt. Je houdt je eigen resultaten bij; de ingevulde voorbeeldbeoordelingen
zijn geen inleverwerk of toestemming om jouw code over te nemen.
