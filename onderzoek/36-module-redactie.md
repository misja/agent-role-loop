# Redactie van modules 4 tot en met 6 (#36)

## Basis en menselijk besluit

Het [C2](https://github.com/misja/agent-role-loop/issues/36#issuecomment-5973048543)
inventariseert vóór uitvoering 24 afgebakende ingrepen op de negen bestaande
modulepagina's, met acht voor/na-passages. De
[onafhankelijke C3](https://github.com/misja/agent-role-loop/issues/36#issuecomment-5973078797)
geeft PASS. Het projectbord is vóór planning geraadpleegd; eerdere werkitems
voor core, schrijfwijzer, praktijkvoorbeeld en modules 1–3 waren afgerond.
Slides/docentennotities (#22) en summatieve toetsing (#23) blijven afzonderlijk
werk.

Het [menselijke C4](https://github.com/misja/agent-role-loop/issues/36#issuecomment-5973122656)
geeft het concrete plan vrij. Het bevestigt mogelijke perspectiefspanning in
plaats van verplichte botsing, aantoonbare fouten als fouten, een geconstrueerd
verwijdervoorstel voor module5, bronbegrensde historische publicatie en de
individuele student als menselijke besluitnemer voor plan en merge na
onafhankelijke agentreview. Een externe medestudent/docent is voor deze werkvorm
niet vereist. Norm- en procesbasis:
`5286aa7ac3cd4bbe14d7ea4fdfbfcd1085837ea1`.

## Uitkomst en structurele bevindingen

Module4 verbindt gedrag aan criteria en gebruiksdoel. Twee gegeven beoordelingen
leveren herleidbare invoer voor twee eigen C6-uitwerkingen en een C7-oordeel.
De oefening vereist geen verzonnen tegenspraak en claimt geen vier uitgevoerde
onafhankelijke agents of volledige historische eisenbasis.

Module5 onderscheidt verdwijnen uit de lijst van vernietiging van alle
objectgegevens. Een eerder bewaarde Boek-referentie behoudt lener en wachtlijst;
de publieke boekenplank-API heeft geen herstelmethode. De code bevat geen
permanente of gedeelde opslag. Het gebruik waarin reserveringen waarde hebben,
is expliciet scenario-invoer bij voorstel P1. Een bevestiging kan een vergissing
verminderen, maar vormt geen herstelvoorziening. C4 vindt vóór de voorgenomen
toepassing plaats; latere codeoplevering en merge vragen hun eigen beoordeling
en menselijk besluit.

Het poortfragment is exact behouden uit de historische lespublicatie op
`80d2ea5`. De bevestigende #13-reactie bevat niet het hele oorspronkelijke
menselijke gesprek; dat gesprek is niet afzonderlijk teruggevonden. De tekst
geeft context voor de vier historische beslispunten en onderscheidt oude
botsings-/garantieclaims van de actuele norm en gemeten onderwijseffecten.

Module6 laat de student zelf functionaliteit en architectuur ontwerpen. De
projectketen maakt opdracht, normversie, planbesluit, codecommit, PR, C5/C6 en
mergebesluit vindbaar. Bordstatus blijft voortgang. De drie basiskeuzen en
afnemende ondersteuning zijn behouden. Een eigen menselijk mergebesluit is
onderscheiden van de native GitHub-reviewhandeling Approve op een eigen PR.

De ongewijzigde casusbeschrijvingen, docstrings en testnamen bevatten nog oudere
uitspraken over foutloosheid, botsing en definitief wissen; de modulepagina's
begrenzen die beschrijvingen met daadwerkelijk codegedrag. Deze bronnen zijn
geen zelfstandige extra bewijzen. Eventuele redactie van die casebronnen vraagt
een eigen afgebakend vervolg; dit werkitem wijzigde uitsluitend de negen
modulepagina's. Core, normen en gedeeld praktijkhoofdstuk zijn ongewijzigd.

## Verificatie en grenzen

Beoordeelde tekstcommit: `8921d1c5789700a25562513cd86f35a74665bbf7`.
De [C5-kern](https://github.com/misja/agent-role-loop/issues/36#issuecomment-5973204736)
registreert de concrete controles en lokale bewijsvindplaatsen.

- `make -C docs html` gebruikt `sphinx-build -b html -W --keep-going` en slaagt
  zonder waarschuwingen. Vier aanvankelijk niet door MyST vindbare kopankers
  zijn vóór review vervangen door verwijzingen naar het praktijkhoofdstuk.
- 694 lokale HTML-links en fragmenten gecontroleerd, nul fouten. Dit is geen
  integrale controle van externe websites.
- De bestaande casustests zijn in gescheiden tijdelijke kopieën uitgevoerd:
  module4 vijf tests, module5 drie tests geslaagd. Direct uitlenen bij reserveren
  en uitlenen aan de eerste wachtende bij terugbrengen zijn gecontroleerd.
  Na verwijderen is de lijst leeg; een eerdere referentie behoudt lener en
  wachtlijst. Dit bevestigt de begrensde claims en algemene foutloosheid volgt
  er niet uit. Casebronnen bleven ongewijzigd.
- Historisch Markdowncitaat exact vergeleken met `80d2ea5`: gelijk.
- Alle negen gebouwde pagina's zijn in headless Chrome bij 1400×1000 visueel
  gelezen, met boven-, midden- en eindgedeelten. Titels/navigatie, gegeven
  beoordelingen, codeblokken, P1, opdrachten en vaste lesstaarten zijn leesbaar
  in de bekeken gebieden. Geen mobiele of alle-viewportcontrole.
- Diffcontrole geslaagd; geen em/en-dash in de negen modulepagina's.

## Onafhankelijke beoordeling

De twee initial reviewers kregen C5-kern, vaste normen, criteria, C4-keuzes en
objectief bewijs, zonder maaktranscript of elkaars oordeel. Beide beoordeelden
de exacte tekstcommit hierboven tegenover de vaste normbasis.

[Redactioneel/didactisch](https://github.com/misja/agent-role-loop/issues/36#issuecomment-5973232960):
SHIP voor AC1/2/4/5/7 en tekstconventies. Per module is de hoofdredenering
naverteld en een opdracht op papier doorlopen. De lezer kan in module4 twee
criteria-gebaseerde C6's en een herleidbare C7 maken, in module5 een C4 op P1
met herstelvoorwaarden schrijven, en in module6 de eigen projectketen volgen.
Geen ontbrekende instructie of begripsprong die herstel vraagt gevonden.
Deze opdrachtgangen zijn agentlezing, geen uitgevoerde studentprojecten of echte
menselijke poortbesluiten.

[Technisch/casus](https://github.com/misja/agent-role-loop/issues/36#issuecomment-5973233186):
SHIP voor AC3/6/7 en de technische delen van AC1/4. De reviewer controleerde
opnieuw casustests, lokale links, historische tekstvergelijking en diffscope;
de gebouwde bronbestanden zijn bytegelijk aan de reviewcommit. Het bouwlog is
als aangeleverd bewijs gelezen en de visuele collages zijn zelfstandig bekeken.

Geen blockers, nits of contract drift. De verenigbare beoordelingen zijn in C7
samengevoegd; geen inhoudelijke arbitrage of automatische herstelronde nodig.
Herstelstand: ontwerp0, oplevering0. [PR #45](https://github.com/misja/agent-role-loop/pull/45)
is gereed voor menselijke merge. Deze registratie wijzigt geen beoordeelde
moduletekst.

Studentwaarnemingen, gemeten leereffect, totale agentduur/tokens, menselijke
leestijd en haalbaarheid van vier uur zijn niet beschikbaar. Er is geen
volledige interface uitgevoerd voor iedere toegestane stack en geen
productiedata-/dataverliesproef gedaan. De structurele taalkundige taak blijft
bij nieuw ontwerp, uitvoering en review van toepassing via de schrijfwijzer.
