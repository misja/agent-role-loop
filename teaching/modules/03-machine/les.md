# Groen is noodzakelijk maar niet voldoende

## Plaats in de leerlijn

In module 2 heb je contracten onderzocht als afspraken tussen rollen. Een van
die afspraken is de overdracht van bouwer naar beoordelaar. Deze les gaat over
de geautomatiseerde controles die daaraan voorafgaan. Vereiste voorkennis:
module 2 en de geautomatiseerde kwaliteitslaag uit het
[kwaliteitsraamwerk](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md).

De les hoort bij [oefening 3](oefening.md), waarin je onderzoekt hoe volledige
regeldekking en een defect samen kunnen voorkomen.

## Leeruitkomsten

De leeruitkomsten staan als “Wat ga je leren” op de [module-index](index.md).

## Opbouw

### De machine als poortwachter

Stel dat een project eist dat alle tests slagen en ten minste 95% van de
coderegels wordt uitgevoerd. Een testcommando kan deze afspraken controleren
zonder dat een beoordelaar de berekening telkens herhaalt. Onder dezelfde
omstandigheden levert de controle dezelfde uitslag op. De gebruikte omgeving,
configuratie en invoer horen daarom bij het bewijs.

De triage en het plan bepalen welke verificatie voor het werk nodig is. Niet
ieder werkitem vraagt alle beschikbare gereedschappen. De bouwer voert de
gekozen controles uit voordat hij de oplevering via
{core}`contracts/review-handoff.md` aan de beoordelaars overdraagt. Een mislukte
vereiste controle moet worden hersteld of als blokkade worden vastgelegd.

De beoordelaar hoeft een uitgevoerde berekening niet zonder aanleiding over te
doen. Hij onderzoekt wel of het bewijs geschikt, voldoende en reproduceerbaar
is. Een geslaagd testcommando op een andere codeversie ondersteunt bijvoorbeeld
geen uitspraak over de huidige oplevering.

### Wat elke poort wel en niet vaststelt

| Controle | Wat de uitkomst ondersteunt | Wat zij niet zelfstandig vaststelt |
|---|---|---|
| Regeldekking (coverage) | Welk deel van de gemeten regels tijdens de tests is uitgevoerd. | Of de asserties het vereiste gedrag controleren; regeldekking meet ook niet alle mogelijke paden of invoer. |
| Linter of formatter | Of de code aan de ingestelde regels voor bijvoorbeeld stijl of verdachte constructies voldoet. | Of alle requirements correct zijn uitgevoerd. |
| Type-checker | Of de onderzochte code volgens het gebruikte typesysteem en de configuratie typeconsistent is. | Of een typecorrecte berekening de bedoelde uitkomst heeft. |
| Securityscan | Of de ingestelde analyses aanwijzingen voor kwetsbaarheden vinden, bijvoorbeeld in broncode of afhankelijkheden. | Dat de software vrij is van kwetsbaarheden; bereik en analysemethode begrenzen de controle. |
| CI-pijplijn | Of de geconfigureerde bouw- en controlestappen in de CI-omgeving slagen. | Dat ontbrekende controles toch zijn uitgevoerd, of dat geslaagde stappen de volledige bedoeling afdekken. |

Het concrete voorbeeld gebruikt Python, pytest en coverage. Andere stacks
kunnen andere gereedschappen gebruiken. Onderzoek steeds welke uitspraak de
configuratie en uitvoer ondersteunen.

### Groen maar fout

In de aangeleverde boekenplank slagen zes tests en wordt 100% van de gemeten
regels uitgevoerd. Toch kan een al uitgeleend boek nogmaals worden uitgeleend.
Requirement 6 verbiedt dit. De test met de naam
`test_uitlenen_voorkomt_dubbele_uitlening` controleert na twee uitleningen
alleen of het boek uitgeleend is.

De tweede uitlening overschrijft de eerste lener. De assertie blijft waar, want
het boek is nog steeds uitgeleend. De toewijzing wordt uitgevoerd en telt mee
voor de regeldekking, terwijl de assertie het behoud van de eerste uitlening
niet controleert. Het testresultaat bewijst dat de ingestelde assertie slaagt
voor deze invoer. Het bewijst niet dat requirement 6 wordt nageleefd.

Er is ook een afzonderlijke configuratiekwestie. Een coveragecommando zonder
`--cov-fail-under` rapporteert dekking, maar stelt geen minimale dekking als
voorwaarde. Als je de terugbrengtest overslaat, blijven de overige tests slagen
terwijl de dekking daalt naar ongeveer 93%. Een drempel van 95% laat dezelfde
uitvoering vervolgens mislukken. De overgebleven tests controleren in beide
uitvoeringen nog steeds hun asserties.

| Waarneming | Wat je kunt concluderen |
|---|---|
| Alle zes tests slagen, 100% regeldekking. | Alle ingestelde asserties slagen; alle gemeten regels zijn uitgevoerd. De dubbele uitlening blijft ongecontroleerd. |
| Vijf tests slagen, ongeveer 93% dekking, geen drempel. | De vijf asserties slagen. Het commando verlangt geen minimum voor de dekking. |
| Dezelfde vijf tests slagen, drempel 95%, commando mislukt. | De tests slagen, maar de gekozen dekkingseis wordt niet gehaald. |

Een coverage-drempel hoort bij de conventionele laag: iemand kiest wat het
project verlangt. De geautomatiseerde laag handhaaft die ingestelde afspraak.
Een hogere drempel maakt de assertie voor dubbele uitlening niet sterker.

### De brug naar het oordeel

Om de zwakke assertie te herkennen, moet je de test vergelijken met requirement
6. Daarvoor is kennis van de bedoeling nodig. Een beoordelaar kan ook nagaan
welke invoer of situatie in het bewijs ontbreekt. Module 4 behandelt die
beoordeling. Deze module bereidt haar voor door de betekenis en grenzen van
geautomatiseerd bewijs te onderzoeken; je voert hier geen volledige review uit.

## Werkvormen en toetsing

- Werkvormen: korte instructie, gezamenlijke ontleding van de groene boekenplank, daarna zelf toepassen op de eigen boekenplank in oefening 3.
- Toetsing: formatief, via de verantwoordingsvragen van oefening 3.

## Bronnen

- Het raamwerk [Kwaliteit als gedeelde verantwoordelijkheid](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md), secties “1. Geautomatiseerd en deterministisch” en “De drie samen”.
- {core}`contracts/review-handoff.md` en {core}`roles/builder.md`, over verificatiebewijs en de overdracht naar beoordeling.
- Humble en Farley, Continuous Delivery {cite}`humble2010continuous`, over geautomatiseerde controles in een deployment pipeline.

## Afronding

### Wat heb je geleerd

De gekozen geautomatiseerde controles ondersteunen de overdracht naar review.
Hun uitslag geldt voor de onderzochte versie, omgeving en configuratie. Je hebt
twee grenzen onderzocht: regeldekking beoordeelt de inhoud van asserties niet,
en gerapporteerde dekking wordt pas een toegangsvoorwaarde als een drempel is
ingesteld. De overige testasserties blijven zonder die drempel wel van kracht.

### Zelfcheck

Beantwoord uit je hoofd; de sleutel wijst waar je het kunt nakijken.

1. Wie bepaalt welke controles nodig zijn, en wat onderzoekt de beoordelaar nog aan het bewijs? (zie “De machine als poortwachter”)
2. Wat toont regeldekking aan? Waarom mist de dubbele-uitleningstest requirement 6 ondanks 100% dekking? (zie “Groen maar fout”)
3. Wat verandert wanneer je een coverage-drempel instelt? Wat blijven de tests zonder die drempel controleren? (zie “Groen maar fout”)
4. Welke vraag over de bedoeling vereist nog beoordeling? (zie “De brug naar het oordeel”)

### Volgende stap

Module 4 (Oordelen) onderzoekt de oplevering tegen de eisen. Je neemt daar de rol
van beoordelaar en zoekt onder meer naar gevallen die de bestaande controles
missen. Daarmee ga je van de geautomatiseerde naar de oordeelsmatige laag.
