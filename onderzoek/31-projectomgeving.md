# Praktijkvoorbeeld van werkitem naar pull request (#31)

## Besluit en uitvoering

Het [C1/C2-plan](https://github.com/misja/agent-role-loop/issues/31#issuecomment-5664070093)
is vrijgegeven met het [menselijke C4](https://github.com/misja/agent-role-loop/issues/31#issuecomment-5664111027).
Normbasis: `ae561f50a45ca42967e4687434cf0d2e8d4f5827`, met CLAUDE.md en
teaching/conventies.md, doelgroep.md, schrijfwijzer.md en begrippen.md.

Het gedeelde praktijkhoofdstuk volgt een beschikbare-boekenfilter van opdracht
naar beoordeling en herstel. De volledige overdrachten zijn als bijlage leesbaar
en zitten samen met code, patches, testbewijs, versieregister en de vaste
procesbasis in een downloadbundel. Personages, besluiten en beoordelingen zijn
expliciet fictief. A/B zijn codeversielabels, geen verzonnen commit-ID's.

Het hoofdstuk sluit aan na module 2. README, manual adapter, hoofdnavigatie en
module-ingangen verwijzen ernaar. In module 2 is de oude vaste rolbezetting
vervangen door een verwijzing naar de canonieke route. Bestaande cases zijn
ongewijzigd. Brede module-redactie blijft bij #35/#36.

## Controlebewijs

- Basiscontrole: één test geslaagd. A met zwakke suite: drie tests geslaagd.
  A met S4-regressie: één test faalt doordat het uitgeleende boek verdwijnt.
  B met volledige suite: vier tests geslaagd. De waargenomen uitvoer staat in
  `teaching/cases/praktijk-projectomgeving/bewijs.txt`.
- Dit is reproductie van geconstrueerde versies, geen historische test-first-
  of agentrun. Het materiaal laat de student bij eigen herstel eerst rood
  vaststellen en daarna de reparatie uitvoeren.
- Downloadbundel uitgepakt in een tijdelijke lokale Git-repository. De beide
  patches toegepast op boekenplank.py, afzonderlijke commits gemaakt en
  dezelfde groen/rood/groen-volgorde waargenomen. De resultaten komen bytegelijk
  overeen met de A/B-bestanden. Geen externe oefenissues of PR's aangemaakt.
- ZIP-integriteit gecontroleerd; opnieuw genereren met
  `python docs/package_practice.py` levert dezelfde bytes. De bundel bevat de
  vaste core-versie, licentie en herkomst, zonder caches of lokale werkbestanden.
- Schone Sphinx-build: `sphinx-build -E -a -b html -W --keep-going -c docs teaching`
  met uitvoer naar een lege tijdelijke publicatiemap; geslaagd. Eerste fouten
  in literalinclude-opties en een fragmentverwijzing zijn vooraf hersteld.
- 245 lokale HTML-linkdoelen op hoofdstuk, overdrachten, module 2 en index
  gecontroleerd: aanwezig. De gepubliceerde ZIP is bytegelijk aan de bron.
- `git diff --check`: geslaagd.

## Visuele controle en redactionele beperking

De gebruiker heeft de gebouwde pagina's zelf visueel geïnspecteerd en antwoordde:
“de pagina's lijken mij prima. nog steeds aardig text-intensief, maar voor nu
alle prima”. Dit is akkoord voor de huidige publicatie, met tekstdichtheid als
redactioneel aandachtspunt voor vervolgwerk. Geen studentproef verondersteld.

De agent heeft de voorgenomen browsercontrole op verzoek gestaakt en de gestarte
headless Chrome-sessie afgesloten. Er wordt geen voltooide visuele agentcontrole
geclaimd. Nieuwe browserstarts zijn voor deze oplevering niet nodig.

## Productbronnen en grenzen

De officiële GitHub-documentatie is op 14 september 2026 geraadpleegd voor issues,
Projects, PR-aanmaak, reviewtypen, eigen PR niet kunnen goedkeuren, sluitwoorden
bij de standaardbranch en permanente bestandslinks. De bronnen staan bij de
betreffende aanwijzingen in het hoofdstuk. Codeberg-documentatie over rechten
(en de Projects-eenheid) en branches/PR's onderbouwt de beperkte functievergelijking.
Er wordt geen gelijke automatisering op andere Forgejo-installaties aangenomen.

Wel uitgevoerd: controle van documentatie en lokale Git-/codehandelingen.
Niet uitgevoerd: een volledige live GitHub-/Codeberg-oefenroute, providerintegratie
of praktijkproef met studenten. Exportmateriaal bewaart de inhoud en expliciete
verbanden; het reconstrueert geen native reviews, accounts of bordautomatisering.

## Onafhankelijke beoordeling

De onafhankelijke [C6](https://github.com/misja/agent-role-loop/issues/31#issuecomment-5669654898)
beoordeelde commit `8ef6fbfb5f1b5c9579f9f8694c0c48b444f713d8`: SHIP,
AC1-AC8 pass, geen blockers, nits of contract drift. De reviewer kreeg de normen,
geldige besluiten en C5-kern, zonder maaktranscript. De volledige leesantwoorden
staan in C6: bij A volgt beoordeling; na C6-A volgt gericht herstel; na C6-B
volgt de menselijke mergebeslissing; P2 blijft een niet-vrijgegeven voorstel.
Deze gegevens bleven ook in de offline bundel aanwijsbaar.

De reviewer heeft bundelinhoud en vaste normen zelfstandig vergeleken met de
bron en de codecontroles opnieuw uitgevoerd met de verwachte uitkomsten.
Build- en linkcontrole zijn als aangeleverd bewijs gebruikt. De visuele controle
is niet herhaald; daarvoor geldt het menselijke akkoord. Tekstdichtheid is ook
[overgedragen aan #35](https://github.com/misja/agent-role-loop/issues/35#issuecomment-5669631476).

Werkelijke herstelstand #31: ontwerp 0, oplevering 0. Deze afronding wijzigt alleen
de onderzoeksregistratie; het beoordeelde materiaal blijft gelijk. PR #41 wacht
op menselijke merge. Tokens, totale duur en menselijke leestijd: niet beschikbaar.
