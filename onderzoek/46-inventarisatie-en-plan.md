# #46: inventarisatie en uitvoeringsplan

Status: C2 v1, voorstel voor menselijk besluit. Normen en lesmateriaal zijn nog
niet gewijzigd. Dit document vult de beperkte inleidingsproef aan.

## Doel en grens

Maak de bestaande doelgroep- en schrijfafspraken bruikbaar voor studenten die
in jaar 1 en 2 de eerste ontwikkelprincipes hebben leren kennen. Laat in een
begrensde schrijfproef zien hoe zij een opdracht, test en beoordeling met elkaar
kunnen verbinden. Leg de resterende verbeteringen vast als afzonderlijke
opdrachten. #46 wordt daarmee een eindige herstelopdracht; doelgroepgericht
schrijven en beoordelen blijven bij iedere bijdrage gelden.

Geen volledige herschrijving van modules, corecontracten, casuscode, adapters,
slides of toetsing. Leeruitkomsten, vijftien requirements en drie porties van
module 1 blijven behouden. Alleen expliciet genoemde voorkennisverwijzingen
worden in de modules aangepast. Geen woordquota of claims over gemeten begrip.

## Basis en huidige stand

Proces en projectnormen: `2f8b43f085053bdee4d6ccb9c75b23f4bb9663c9`.
Leesbare bronnen: `CLAUDE.md`, `core/loop.md`, de contracten voor C2 tot C7,
`teaching/conventies.md`, `doelgroep.md`, `schrijfwijzer.md` en `begrippen.md`.
C0 is [issue 46](https://github.com/misja/agent-role-loop/issues/46).
C1 staat [op het issue](https://github.com/misja/agent-role-loop/issues/46#issuecomment-5978187812).
De onderzoeksbranch bevat nog geen gewijzigde normen of productteksten.
Concept-PR47 is geen normbesluit of mergebesluit.

De gebruiker geeft het startniveau aan. Specifieke curriculumgegevens en
studentwaarnemingen zijn niet beschikbaar. De inventaris hieronder is een
agentlezing: tekstbevindingen zijn controleerbaar, leesgevolgen zijn verwachtingen.
De eerdere proef en onafhankelijke beperkte lezing zijn bronnen, geen volledige
C3 of C6 voor deze opdracht. Herstelstand: ontwerp 0, oplevering 0.

De inventaris omvat 21 hoofdpagina's: twee inleidingen, achttien modulepagina's
en het praktijkhoofdstuk. De manualadapter is aanvullende afhankelijkheidsbron.
Open werkitems #22, #23 en #32–#34 krijgen een overdracht; hun toekomstige
uitvoering wordt hier niet als beoordeeld aangemerkt.

## Wijziging 1: verduidelijk de bestaande grondslag

Bestanden: `teaching/doelgroep.md`, `schrijfwijzer.md`, `conventies.md` en
`_werkitem-template.md`. Geen tweede schrijfwijzer of nieuwe generieke rol.

Vervang de eerste doelgroepalinea door dit voorstel:

> Dit materiaal richt zich op derdejaars Software Engineering-studenten. In de
> eerste twee studiejaren hebben zij kennisgemaakt met programmeren en
> ontwikkelprincipes, waaronder tests, versiebeheer en scheiding van
> verantwoordelijkheden. Een principe herkennen betekent nog niet dat zij het
> zelfstandig kunnen toepassen op het werken met AI. Gebruik een herkenbare
> programmeerhandeling als vertrekpunt en leg uit hoe het principe in deze
> situatie wordt gebruikt. Geef een korte herinnering waar die nodig is;
> introduceer bekende onderwerpen niet zonder aanleiding opnieuw.

Voeg bij voortbouwen toe, en vervang de verwijzing die alle agentuitleg aan de
startpagina toeschrijft door een verwijzing naar de voorbereiding:

> Benoem bij iedere nieuwe toepassing wat de student al kan gebruiken, welke
> uitleg eerder is aangeboden en welke stap hier nog wordt geleerd. Een eerdere
> vermelding van een term is geen bewijs dat de student ermee kan redeneren.
> Controleer bij het verplaatsen van uitleg ook de verwijzingen vanuit latere
> onderdelen.

Voeg bij de schrijfafspraken toe:

> Bepaal de functie van de passage vóór het schrijven: oriënteren, uitleggen,
> laten uitvoeren of verdiepen. Bouw een nieuwe toepassing op vanuit wat er
> gebeurt: welke invoer is er, welke handeling volgt en wat ziet de lezer daarna?
> Benoem vervolgens het principe dat die handelingen verbindt. Bij instructies
> moeten voorbereiding, handeling, reden en herkenbare uitkomst vindbaar zijn.
> Houd de nodige uitleg bij de stap.

Voeg bij literatuur en naslag toe:

> Help de lezer kiezen waarvoor en wanneer een bron bruikbaar is. Noem de
> benodigde voorkennis wanneer die verder gaat dan de omliggende tekst.
> Selecteer samenvatting en bronkritiek op die leesvraag; maak van een verwijzing
> geen extra theoriehoofdstuk of verdediging van de hele werkwijze. Controleer
> inhoudelijke bronclaims aan de bron. Optionele tekst mag dezelfde doelgroep
> niet ongemerkt meer voorkennis toeschrijven.

Vul de bestaande verantwoordelijkhedentabel aan: ontwerp legt tekstfunctie en
benodigde overgang naar de nieuwe toepassing vast; uitvoering maakt die overgang
zichtbaar; beoordeling wijst probleem, invoer, handeling, reden, uitkomst en
onbenoemde voorkennis aan. Een agentantwoord is geen studentwaarneming.
Het sjabloon vraagt lezer, voorkennis, nieuwe toepassing en een gerichte leesgang,
ook voor technische instructies buiten `teaching/` die voor studenten zijn bedoeld.

Onderbouw per aanvulling welke bevinding zij adresseert. Vergelijk daarvoor de
passages en geregistreerde aanpak van #30, #37, #35, #36 en #42. Onderscheid een
ontbrekende of onduidelijke norm van onvoldoende toepassing of reviewdekking.
Trek geen conclusies over verborgen beweegredenen van eerdere auteurs/reviewers.

Invoering: pas na C4. #46 behoudt de vastgelegde basis; de door de mens besloten
nieuwe tekst wordt een expliciete aanvullende grondslag voor de eigen proef.
Nieuwe werkitems gebruiken na merge de nieuwe normcommit. Lopende opdrachten
behouden hun basis tenzij een menselijk besluit de wijziging daar invoert.

## Wijziging 2: korte start, voorbereiding vóór eerste gebruik

Bestanden: `teaching/index.md`, nieuwe pagina `teaching/van-chat-naar-agent.md`;
alleen voorkennisverwijzingen in module 1 les/oefening en module 2 les.

Gebruik voorstel A uit `46-inleidende-teksten-proef.md`: een boekenplanksituatie
met ontbrekende controle van een tweede uitlening. Kop: “De ontwikkelstraat”.
Subtitel: “AI laten programmeren en de code controleren”. Het voorbeeld toont
ontbrekend bewijs, geen bewezen softwarefout. Behoud navigatie en modulevolgorde.

De voorbereiding bewaart noodzakelijke uitleg vóór module 1 deel A en B:

1. Een chat krijgt een opdracht, code en eerdere berichten. Het model maakt een
   antwoord; het programma bepaalt wat aan het model wordt aangeboden.
2. Een losse chat wijzigt geen lokale bestanden en voert geen tests uit. De mens
   past code toe en controleert haar, of een agent met gereedschappen voert deze
   handelingen aantoonbaar uit binnen zijn bevoegdheden.
3. Leg agent, sessie, context en rol uit aan deze handelingen. Toon een bouwer
   die code, eis, testuitkomst en beperking overdraagt aan een aparte beoordelaar.
4. Toon één ingevulde overdracht en de bijbehorende rolprompt. Benoem wie de code
   werkelijk toepast, wie de controles uitvoert en welke uitvoer wordt bewaard.
   Een contract beschrijft invoer en uitvoer; het garandeert geen juiste inhoud.
5. Geef een korte functiewijzer voor de contracten die deel B gebruikt, met
   eigenaar, invoer, resultaat en gerichte links naar core/manual. Benoem waar
   menselijke planbeslissing en merge plaatsvinden. Neem geen tweede routenorm op.

Volg bij beoordeling start → voorbereiding → deel A → les → deel B. Voor ieder
begrip en iedere eerste overdracht moet de benodigde uitleg vóór gebruik
vindbaar zijn. Module 2 verdiept deze kennis; zij wordt geen verborgen voorwaarde
voor het al uitvoeren van deel B. De complete begeleide uitvoering van portie 1
blijft een vervolgopdracht; de nieuwe voorbereiding moet op zichzelf wel de
hierboven genoemde eerste overdracht en uitvoeringsverantwoordelijkheid tonen.

## Wijziging 3: begrensde raamwerk- en literatuurproef

Bestand: `teaching/kwaliteit-als-gedeelde-verantwoordelijkheid.md`.
Wijzig opening en eerste twee secties, tot “Drie soorten kwaliteitsmechanismen”,
en de Farley-toelichting. De rest van de pagina blijft expliciet vervolgwerk.

Gebruik dezelfde uitleenafspraak. Toon welk testgeval aanwezig is, welk geval
ontbreekt en welk aanvullend resultaat de beoordelaar vraagt. Testuitvoering
moet ook de verwachte uitkomst tonen; alleen een test toevoegen levert geen
bewijs dat de afspraak wordt nageleefd. Benoem daarna afspraak, controle en
beoordeling. De mens beslist over het overnemen van de wijziging.

Koppen: “Wie controleert de wijziging?” en “Waarom verschillen beoordelingen?”.
Maak bij de tweede kop twee concrete beoordelingen zichtbaar: een gemist geval
kan een fout aantonen, een ontwerpafweging kan meerdere verdedigbare keuzes
hebben. Forceer geen meningsverschil. Behoud het onderscheid tussen voorafgaand
planbesluit en latere merge; rollen zijn taken, geen verplichte andere modellen.

Gebruik Farley-voorstel B uit het eerdere rapport. Controleer de hoofdstukclaim
aan de primaire uitgeversbron; beweer niet dat het boek deze rollenlus valideert.
Leg voor/na functie, voorkennis, nieuwe begrippen en verplaatste uitleg vast.
De andere drie toelichtingen krijgen broncontrole in het vervolgitem hieronder.

## Wijziging 4: afzonderlijke vervolgopdrachten en overdracht

Na C4 worden onderstaande C0's opgesteld, gepubliceerd en gekoppeld aan #28.
Dit geeft nog geen bouwvrijgave voor die opdrachten. Elk item krijgt de concrete
vindplaatsen uit de bijlagen, begrensde wijzigingen, te behouden leeruitkomsten,
casus en oefenopbouw, normbasis en onafhankelijke leesvragen.

| Vervolg | Scope en controleerbare uitkomst | Afhankelijkheid |
|---|---|---|
| Eerste uitvoering begeleiden | Module 1 les/oefening: één complete keten voor portie 1, rolprompt en ingevulde uitvoer; patch/check-eigenaar zichtbaar. Herstel de tijdvolgorde van requirements 12/13 en ongefundeerde gevoeligheidsclaim. Alle eisen, drie porties en echte regressiecontrole blijven. | Besloten voorbereiding #46 |
| Overdracht uitleggen en controles uitvoeren | Modules 2–3: prompt versus uitvoering, unieke analyse-uitkomst, dubbel uitgewerkte proeven verdelen, setup en terugvaloptie uitvoerbaar. Student kan bronnen/versies/ontbrekende informatie aanwijzen en de controle uitvoeren. | Eerste uitvoering; norm/proef #46 |
| Oordelen en besluiten oefenen | Modules 4–5: ingevuld oordeel met dekking versus softwaregoedkeuring; concreet samenvoegen versus geschil; besluitbron en noodzakelijke/uitstelbare voorwaarden. Historisch fragment als naslag. | Eerdere contractuitleg |
| Eigen proces uitvoeren | Module 6 en praktijkhoofdstuk: afzonderlijke beslismomenten, directe contractlinks, weggelaten controle met resterende beoordelingsvraag, gerichte naslaglinks. Dossier volgt één criterium van opdracht tot besluit. | Eerdere oefeningen |
| Raamwerk en bronnen afronden | Rest kwaliteitsraamwerk en overige drie literatuurtoelichtingen: concrete functie, leesdoel/voorkennis, primaire broncontrole en beperkingen. Geen hele methodeverdediging per bron. | Begrensde proef #46 |

De bouwer registreert elk nieuw item en zijn eigenaar/status op het bord; de
onafhankelijke samenhangreviewer controleert volledigheid en teruglezing.
#22/#23/#32–#34 en overzicht #28 krijgen de besloten grondslag, relevante
bevindingen en verwijzingen naar de nieuwe opdrachten. Zij blijven zelf
verantwoordelijk voor hun plannen en beoordelingen. Als die nog niet bestaan,
staat dat expliciet in de overdracht; #46 bewijst hun begrijpelijkheid niet.

## Criteria, verificatie en oplevering

C0-criteria 1–10 blijven integraal gelden. De literatuuraanvulling valt onder
1/3/5/6/7. Afgeleid AC11: leeruitkomsten, casussen, oefenopbouw, vijftien eisen en
drie porties blijven ongewijzigd behalve de genoemde voorkennisverwijzingen.
C1 wijst AC11 vóór review toe aan de samenhangreviewer.

| Criteria | Verificatie met verwachte uitkomst | Onafhankelijke reviewer |
|---|---|---|
| 1 | Alle 21 pagina's hebben bevinding of gemotiveerd behoud; externe studentgerichte gevolgen zijn benoemd. | Didactiek |
| 2, 4, 9 | Normvoorstel en diagnose verbinden elke aanvulling aan passages en eerdere norm/reviewregistratie; geen onbewezen beheersingsclaim of extra rol. | Didactiek |
| 3, 5 | Voor/na en leesroute tonen concreet probleem, handelingen en voorbereiding vóór gebruik. | Didactiek; samenhang voor verwijzingen |
| 6 | Verse lezing van proef, eerste overdracht module 1, module 4-oefening en Farley. Lezer wijst invoer, reden, handeling, uitkomst en ontbrekende kennis aan. Problemen/herstel en bewijsgrenzen geregistreerd. | Didactiek |
| 7, 10 | Elke bevinding is aan #46, een begrensd vervolg of gemotiveerd behoud/uitstel gekoppeld; issue/bordoverdracht teruggelezen. | Samenhang |
| 8 | Tekstnormcontrole, schone docs-build onder `-W --keep-going`, lokale links/fragmenten en visuele lezing van gewijzigde gepubliceerde pagina's. | Samenhang; didactiek voor tekst |
| 11 | Vergelijk beschermde passages met de basis; alleen verklaarde voorkennislinks verschillen in modules. | Samenhang |

Verificatiemodellen: `manual-with-expected-results` voor de leesvragen en
passagevergelijking; `validation-workflow` voor build, links en issueoverdracht.
Geen codegedrag gewijzigd, dus geen test-first of tests die de tekst kopiëren.
Controleer `git diff --check` en scope. Registreer waargenomen uitkomsten en
beperkingen met de exacte reviewcommit in C5. Studenten zijn niet geobserveerd.

Twee onafhankelijke C6's krijgen C5 en leesbare normen zonder maaktranscript of
elkaars verdict. Didactiek krijgt 1/2/3/4/5/6/9; samenhang 7/8/10/11 met genoemde
overlap. Compatibele oordelen worden via C7 samengebracht; inhoudelijk geschil
volgt core. Een SHIP is geen mergebesluit.

## Risico's, herstel en menselijk besluit

Inkorten kan voorbereiding verwijderen: lever start, voorbereiding en links als
één pakket. Een kleine proef kan voor volledig herstel worden aangezien: benoem
resterende pagina's en de vervolgitems. Extra normtekst kan weer abstract worden:
toets haar aan de concrete handelingen en voorbeelden. Geen gemeten leereffect.
Terugval is revert van het samenhangende documentatiepakket; issuewijzigingen
worden traceerbaar gecorrigeerd, zonder eerdere besluitgeschiedenis te verwijderen.

Na onafhankelijke C3 is C4 nodig volgens `core/loop.md` en het onderdeel “Een
nieuwe conventie toevoegen” in `teaching/conventies.md`. Voor te leggen besluit:

- A: bovenstaande normverduidelijkingen en borging op hun bestaande plek.
- B: korte boekenplankstart, aparte voorbereiding en minimale voorkennislinks.
- C: raamwerkbegin en Farley als begrensde proef; overige raamwerktekst volgt apart.
- D: genoemde vervolgitems en overdrachten opstellen; hun uitvoering volgt later.

Ontwerp en oplevering hebben elk maximaal één automatische herstelronde. Leg
teller, bevinding en artefact vóór herstel vast op #46. Geen reset door een sessie.

## Bijlage: broninventaris modules 1–3

# #46: inventaris modules 1–3 voor planvoorbereiding

Leesbasis: lokale HEAD `9405459fd930ba51265dea1f1c7e13fd6ecf5512`; de negen modulebestanden hebben geen diff met normcommit `2f8b43f085053bdee4d6ccb9c75b23f4bb9663c9`. Normen op die laatste commit: conventies, doelgroep, schrijfwijzer, begrippen. Tevens gelezen: onderzoek/46-inleidende-teksten-proef.md en adapters/manual/README.md. Geen externe broncontrole, uitvoering of studentproef. Startniveau: derdejaars, eerste SE-principes geleerd in jaar 1/2; bekendheid bewijst geen zelfstandige transfer naar dit proces.

Onderstaande gevolgen zijn verwachtingen uit één agentlezing, geen waargenomen studentproblemen. P1 = voorbereiding/uitvoerbaarheid eerst; P2 = gerichte uitleg/redactie; P3 = optioneel opruimen. Geen volledige herschrijving voorgesteld.

## Eindige inventaris per pagina

| ID/prio | Aangetroffen passage en tekstprobleem | Verwacht lees- of uitvoergevolg | Gerichte vervolgactie | Te behouden |
|---|---|---|---|---|
| 1/P2, 01/index | R11: “opgebouwde gesprekscontext tot kwaliteitsverlies”; tegelijk definitie, drie symptomen, onderbouwing. Als organizer acceptabel, maar verklaart context nog niet. | Student kan symptomen lezen als bewijs van context rot terwijl les dit terecht begrenst. | Houd leeruitkomst compact en laat de eis van een onderbouwde mogelijke verklaring herkenbaar aansluiten op les r35–40. Geen contextcollege in index. | R3 concrete onderzoeksvraag; r13 volgorde deel A/les/deel B. |
| 2/P3, 01/index | R24–27 verwijst naar een voorbeeld dat pas na module 2 nodig is: “Je hoeft het voorbeeld ... nog niet te lezen.” | Extra zijpad bij de eerste oriëntatie, zonder huidige handeling. | Verplaats deze leesaanwijzing naar module 2 of maak haar uitsluitend latere naslag. | Navigatie en één leeruitkomst, geen lange aanloop. |
| 3/P1, 01/les | R56–67 stapelt manual adapter, triage, orkestrator, route, planning, verheldering, menselijke poort en vier perspectieven. R44–54 verklaart planner/bouwer/beoordelaar concreter, maar geeft nog geen uitgevoerde overdracht. | Bekende taakverdeling is onvoldoende om zelf C1, planreview en besluit uit te voeren; verwijzing naar core vereist nog selectie van juiste invoer. | Plan vóór deel B één begeleide overdracht met bron, rolprompt, ingevulde uitvoer, mensbesluit en volgende ontvanger. Bewaar core als normatieve route. | R44–54: eigen gesprek + eisen/code/bewijs, en eis die zonder overdracht niet terugkomt; r62–67 begrenst vier perspectieven als oefenkeuze. |
| 4/P2, 01/les | R30–33: “bij requirement 12 ... nummers opnieuw gebruikt, terwijl requirement 13 dat verbiedt”. Requirement 13 volgt op 12; de tekst preciseert niet of het defect pas na portie 3 wordt vastgesteld. | Tijdvolgorde kan een nog niet gegeven eis als vergeten afspraak laten lijken. | Specificeer controle na portie 3 of gebruik een eerder reeds geldende eis. | R35–40 onderscheidt illustratie, mogelijke oorzaak en bewijs; r18–20 maakt toepassingsafhankelijkheid van context expliciet. |
| 5/P1, 01/oefening | R54–78 bevat acht stappen met C0–C7, PLANNED/PROCEED/REVISE/STOP, C5-kern en hoofdbeoordelaar. “Laat de planner C2 maken” verwijst voor invoer naar loop; concrete uitvoering van builder ontbreekt als aparte stap. | Student moet uit drie soorten bronnen (oefening/adapter/core) de eerste bruikbare chat samenstellen. Transfer wordt al vereist voordat module 2 haar verklaart. | Werk voor portie 1 één beperkte invoer/uitvoerketen uit; plaats contractcodes naast documentfunctie en eigenaar. Wijs bij elke overgang leesbare bron en te bewaren versie aan. Geen tweede procesdefinitie. | R75–78 drie werkitems en regressie-eisen; r64–66 menselijke keuze; r67–74 onafhankelijkheid en begrensd herstel. |
| 6/P1, 01/oefening | R65 “geef ... aan de bouwer”, r67 “codeversie ... relevant bewijs”; wie met losse chats patch toepast en checks draait staat hier niet. Adapter r43–45: “A chat without repository tools cannot apply changes or execute checks.” | Een chatantwoord kan worden verward met gewijzigde bestanden of daadwerkelijk uitgevoerde verificatie. | Maak op builderovergang expliciet: mens past voorstel toe, voert passende checks uit en geeft waargenomen uitvoer terug; of gekozen coding-agent doet dat aantoonbaar. Verwijs naar adapter voor procedure. | Deel A r39 vraagt code/foutmeldingen/testuitvoer; r48 volledige eindcontrole werkt/werkt niet/weet ik niet. |
| 7/P2, 01/oefening | R83 introduceert LIGHT en proportionaliteit terwijl de huidige opdracht PLANNED blijft. Kostenvariant is concreet maar erg dicht, naast vier-perspectievenvariant en herstelroute. R43: “requirement 9 en 12 zijn er gevoelig voor” is een niet onderbouwde verwachting. | Extra routekennis nodig om een variant te begrijpen; verwachte symptomen kunnen waarneming sturen. | Zet budgetvariant bij uitvoeringskeuze met minimale benodigde uitleg; motiveer 9/12 vanuit gewijzigde eisen of schrap specifieke gevoeligheidsclaim. Duur van 90 minuten deel B is onbeproefd, geen feitelijk onhaalbaarheidsoordeel. | R110–113 verbiedt algemeen methode-effect afleiden; reflectie r91–105 laat gelijke/ontbrekende uitkomsten toe; rollenspel bewaart echte overdrachten. |
| 8/P2, 02/index | Leeruitkomst 2: “de interface, de implementatie en het verborgene aanwijzen”. De bekend klinkende driedeling is abstract en “het verborgene” weinig concreet. | Organizer kan een classificatieopdracht suggereren vóór begrip van gegevensselectie. | Benoem welke drie bronnen de student straks vergelijkt en wat niet wordt doorgegeven; laat theoretische labels daarop aansluiten. | Leeruitkomst 3 vraagt opbrengst én kosten; praktijkverwijzing wijst specifieke plan-/besluitpassages aan. |
| 9/P2, 02/les | R46 “Je kent scheiding ...”, r65 kop “rolprompts als implementatie”. R67–77 nuanceert uitvoering terecht; de kop is stelliger dan die uitleg. Een prompt is niet de feitelijke uitvoering. | Student kan analogie als gelijkheid overnemen en promptkwaliteit met uitgevoerd gedrag verwarren. | Toon naast C2-P1 eerst rolprompt én één uitgevoerde handeling; label overeenkomst en grens van analogie. Geen herintroductie van alle softwaremodulariteit nodig. | R22–42 filter/register/plan/besluit/prompt is concrete voorbereiding; r71–77 onderscheidt mens/model/context/tools en begrenst uitwisselbaarheid. |
| 10/P3, 02/les | R104–123 historische Mermaid-naslag introduceert tweede casus, dependency/configuratie/rendercheck na afgeronde boekenplankuitleg. Leeruitkomsten r14–16 herhalen alleen indexverwijzing, evenals 03/les. | Extra onderwerpen zonder noodzakelijke toepassing; vertraagt doorgang naar eigen analyse. | Zet historische naslag buiten hoofdlezing of motiveer haar unieke leerfunctie; combineer lege organizerverwijzing met plaats-in-leerlijn. | R79–102 legt selectie, leesbare bronnen en onderhoudskosten uit; r156–161 concrete brug naar geautomatiseerde controle; vaste staart behouden. |
| 11/P2, 02/oefening | R25–29 herhaalt les-analogie bijna volledig; r55 “Eén contract leek je ... misschien te zwaar” neemt ervaring impliciet aan. Worked example analyseert opnieuw hetzelfde C2-P1. | Herhaling kan niets toevoegen voor wie les al las; vraag geeft weinig aanknopingspunt als geen contract zwaar leek. | Behoud één uitgewerkt analysemodel; laat oefening unieke output expliciet tonen (bron/versie/vereist/ontbrekend). Formuleer schaalvraag ook voor geen ervaren invullast. | R40–47 toetsbare voltooiing door terugvindbare brononderdelen en ontbrekende data niet achteraf aanvullen; r31–36 laat onjuiste aanname ondanks selectie zien. |
| 12/P2, 03/index | R3 “groen noodzakelijk maar niet voldoende”; r11–13 specificeren gekozen controles maar titel/leerdoel suggereren algemene verplichting. | Student kan elke tool of een groene status als onvoorwaardelijke vereiste behandelen, ook wanneer norm/controle anders is gekozen. | Koppel noodzakelijkheid expliciet aan vereiste/geconfigureerde controles. Houd advance organizer, vermijd volledige tooldiscussie vooraf. | R13 zwakke assertie en ontbrekende drempel zijn twee concrete leerobjecten; praktijkverwijzing benoemt ander defect. |
| 13/P2, 03/les | R55–82 vertelt volledige dubbele-uitleningscasus én 93%/95%-proef; oefening r36–95 vertelt beide nogmaals met dezelfde conclusie. Dit is grotendeels duplicatie, geen aangetoonde studentlast. | Studenten lezen de uitkomst tweemaal voordat zij haar toepassen; proef kan uitsluitend bevestiging worden. | Beleg één hoofdbron voor uitgewerkt resultaat. Les kan concept + kleine assertie tonen; oefening laat meten/verklaren voordat antwoord wordt gelezen. Houd voldoende steun voor eerste transfer. | R22–37 omgeving/config/invoer/codeversie; tabel r41–47 onderscheidt betekenis en grens; r61–65 maakt gemiste eis zichtbaar; r80–82 onderscheidt normkeuze en handhaving. |
| 14/P2, 03/oefening | Kop r84 “Uitleg: wie kiest de drempel?” bevat r88 “Noteer welke dekking ...”; uitleg en uitvoering lopen hier samen. R102 introduceert linter/type-checker zonder stackgerichte startaanwijzing. | Student moet zelf herkennen dat opdracht verscholen zit in uitleg; bekendheid met tests bewijst geen zelfstandig coverage-/toolsetup. | Verplaats noteerhandeling onder opdracht; bied alleen gerichte setup-verwijzing voor gekozen stack, geen volledig toolcollege. | R16–34 werkkopie, expliciete omgeving, versies en verwachte waarneming; r86–95 verklaart waarom 95% proefkeuze is, geen projectnorm. |
| 15/P2, 03/oefening | R107–111 fallback requirement 7 laat student zelf nieuwe code/test construeren; r109 “alle toegevoegde regels” vraagt al transfer van dekking naar een extra defect. | Fallback voor ontbrekend eerder artefact is inhoudelijk zwaarder dan hergebruik. | Geef fallback een minimale uitgangswijziging of verwijs naar bestaand ingevuld geval; verifieer dat zij dezelfde leeruitkomst en haalbare omvang houdt. | R104–105 gerichte assertie en onderscheid defect/onjuiste verwachting; r120 verwijst expliciet naar eigen agenttests; r121 proportionaliteit van gekozen controles. |

## Afhankelijkheden die het plan gezamenlijk moet sluiten

1. **Intro → module 1 A:** 01/les r5–9 en 01/oefening r6 verwijzen voor model/context/agent/sessie naar teaching/index.md. De doelgroepnorm noemt die plek expliciet. Als #46 de intro inkort, moet model versus uitvoerend programma en wat in een volgende chat-aanroep meegaat vóór deel A leesbaar blijven. Begrippenlijst is naslag, geen vervangende eerste uitleg.
2. **Intro/01-les → deel B/manual adapter:** begrip rol/sessie/context plus praktische contractdefinitie/ingevuld artefact/rolprompt moet vóór 01/oefening r54 aanwezig zijn. Module 2 kan deze begrippen verdiepen, maar niet als eerste voorbereiding worden gebruikt voor een reeds voltooide deel B. Plan een begeleide eerste overdracht op de bestaande plek of expliciet besloten nieuwe voorbereiding.
3. **Deel B → module 2:** 02/les r5–10 en 02/oefening r9 vereisen echt overdrachtslogboek. C2-P1/C4-P1 onderwijsvoorbeeld is een andere wijziging (beschikbaar-filter) dan de vijftien CLI-requirements; leg dit verschil kort uit, zodat geen uitvoering met de eigen artefacten wordt verward. De bestaande les noemt het bewerkt voorbeeld al, behouden.
4. **Raamwerk → 02 en 03:** 02/les r94–102 en 02/oefening r55 gebruiken conventionele laag; 03/les r7–9 vereist geautomatiseerde laag. Verplaatsen van het raamwerk vraagt per eerste gebruik een leesmoment of uitleg van afspraak, automatische controle en beoordeling. Alleen laaglabels vooraf zijn geen uitleg.
5. **01 deel B-code → 03 oefening:** 03/oefening r9 en r99–105 gebruiken eigen boekenplank; fallback r107–111 moet uitvoerbaar blijven. Bewaar de koppeling eisen/codeversie/bewijs door de eerste overdrachten heen.
6. **Core/manual adapter als normbron:** adapter r24–27 schrijft rolprompt + benoemde invoer + leesbare gepinde normen/besluiten voor; r43–45 vereist echte uitvoering buiten chat; r49–59 beschrijft repair mode en tellers. Oefening moet dit voorbereiden zonder nieuwe route naast core te maken. Gewone PLANNED uitvoering vraagt daarnaast juiste C0/C1, C2/C3/C4, C5/C6/C7-eigenaarschap. Een korte functiewijzer en ingevuld voorbeeld zijn gerichter dan alle contractvelden in de intro.

## Redactionele en epistemische grenzen

Geen harde bevinding “lege AI-tekst” op basis van stijlwoord alleen. Functionele tegenstellingen zoals “een eigen gesprek ... niet ... als niemand haar heeft meegegeven” (01/les r50–52), “een contract ... geen vervanging” (02/les r41–42) en noodzakelijkheid versus voldoende bewijs dragen inhoud en mogen blijven. Algemene conclusie 02/les r61 is direct gekoppeld aan ontbrekende eis r62–63, dus niet leeg. Concrete opgave/zelfcheck/terugblik heeft een andere functie dan zinloze herhaling; verwijder haar niet mechanisch.

Meeste winst verwacht bij praktische aanloop deel B, expliciete transfer van prompt naar uitvoering, beperken tweede casus en dubbele uitwerking. Geen gemeten begrip, duur, effect van contextisolatie of aantal vereiste reviews beschikbaar. Gerichte latere leestoets: laat een student voor de eerste bouw- en reviewovergang aanwijzen welke invoer beschikbaar is, wie werkelijk code wijzigt/checks draait, welke uitvoer bewaard wordt en welk besluit nog menselijk is. Dit zijn voorgestelde vragen, geen bewijs van begrip.

## Bijlage: broninventaris modules 4–6 en praktijk

# Broninventaris #46: modules 4–6 en praktijkvoorbeeld

Basis: commit `2f8b43f085053bdee4d6ccb9c75b23f4bb9663c9`. Gelezen: `CLAUDE.md`; doelgroep, schrijfwijzer, conventies en begrippenlijst op die normcommit; onderstaande tien pagina's op dezelfde commit. Vindplaatsen zijn bronregels op die commit, niet de actuele werkboom. Dit is een agentlezing, geen studentproef. Geen repository- of GitHub-wijzigingen uitgevoerd; bronnen en historische claims niet opnieuw geaudit.

Uitgangspunt: derdejaars met eerste SE-principes uit jaar 1/2. Bekendheid met een principe impliceert nog geen zelfstandige toepassing op rollen, bewijstoewijzing en agentcontext. Eerder behandelde kennis mag worden gebruikt; het vervolg moet die kennis vindbaar aanspreken. Vakwoorden blijven waar zij een noodzakelijke onderscheiding dragen.

Prioriteit: P1 = uitleg/uitvoerbaarheid eerst oplossen; P2 = gerichte redactie of vindbaarheid; P3 = behoud/kleine afwerking. Elke rij onderscheidt de waarneembare tekst van het veronderstelde leesprobleem.

| Nr / pagina | Tekstbevinding met citaat en vindplaats | Mogelijk gevolg, geen studentclaim | Gerichte vervolgactie / prioriteit | Wat goed blijft |
|---|---|---|---|---|
| 1. `04-oordelen/index.md` | R12 noemt direct “strikte, pragmatische, adversariële en onderhoudbaarheidsperspectieven”; r15 wijst naar module 3 en raamwerk. Dit is een leeruitkomst, geen uitleg, en wordt vervolgens concreet uitgewerkt. Geen aangetoonde begripsprong op deze index. | Een eerste lezer kent mogelijk “adversarieel” nog niet; de index hoeft dat niet geheel uit te leggen als de les het doet. | Behouden; hoogstens direct naar sectie “Vier perspectieven” linken. P3. Geen kunstmatige jargonverwijdering. | R5: tests tegenover reserveringsregels is een concrete oriëntatie. R15 maakt voortbouwen zichtbaar. |
| 2. `04-oordelen/les.md` | R38–42 schakelen van concrete reserveringskeuzes naar “herleidbare synthese in C7”, “inhoudelijke tegenspraak” en “arbitrage”. De contracten zijn gelinkt; er staat geen uitgewerkt paar oordelen met eerst een verenigbare uitkomst en daarna een echt geschil. | Het verschil tussen samenvoegen en beslissen bij tegenspraak is benoemd, maar de toepassing moet uit abstracte rolbeschrijvingen worden afgeleid. | Voeg één kort paar concrete bevindingen toe waarmee zichtbaar is welke tekst C7 samenvoegt en welke keuze de hoofdbeoordelaar moet onderbouwen; verwijs bij C6/C7 gericht naar eerdere uitleg in module 2. P1. | R17–21: automatisch uitlenen versus eerst ophalen bouwt de afweging vanuit codegedrag op. R29–34 onderscheidt fout, ontbrekende eis en ontwerpkeuze zorgvuldig. |
| 3. `04-oordelen/oefening.md` | G-A r29–35 geeft “Dekking A1: pass voor het onderzoeken van het scenario” naast “should fix” en “SHIP WITH NITS”; G-M r39–45 idem. Het criterium betreft het onderzoeken, niet het voldoen van software aan de ophaalregel. R53 vraagt daarnaast een grote hoeveelheid contractvelden in één stap. | Zonder expliciete uitleg kan “pass” worden gelezen als softwaregoedkeuring, terwijl de voorbeelden juist een open gebruikskeuze vaststellen. De vertaling van waarneming naar dekking, ernst en besluit blijft deels aan het contract overgelaten. | Annotatie bij één gegeven C6: wat is de vraag, wat is aangetoond, waarom is dat pass, welk toepassingsbesluit ontbreekt nog? Splits r53 in invulvolgorde of verwijs naar betreffende contractonderdelen. P1. | R25 en r56 geven eerlijke grenzen van het onderwijsvoorbeeld. R49 en r70 verbieden verzonnen tegenspraak. Tests, verwachte aantallen en artefactcommit zijn concrete uitvoering. |
| 4. `05-poort/index.md` | R13 introduceert samen “Proportionaliteit en triage”, LIGHT/PLANNED/REJECT, XS/S/M/L/XL en “tijd, tokens en aandacht”. R3 en r12 geven wel een duidelijk beslisdoel; r24–28 verwijst naar praktijk en les. | De derde leeruitkomst kan ogen als een tweede procesopdracht voordat zichtbaar is hoe inzet met het verwijderrisico samenhangt. Dit is geen reden om alle routetermen opnieuw uit te leggen. | Bind de inzetweging kort aan een concreet gevolg van verwijderen; wijs voor bestaande routekennis naar module 2 of de betreffende lessectie. P2. | Onderscheid planbesluit/mergebeslissing in r12; bruikbare verwijzing om C4 werkelijk vast te leggen. |
| 5. `05-poort/les.md` | Tussen eerste beslisuitleg en verwijdercasus staat r40–92 een historisch poortbesluit met vier ontwerpkeuzes, lang citaat en correcties op historische formuleringen. “fading en verdictvorm” (r76) wordt binnen het citaat niet verklaard. De passage concludeert in r83–86 dat voorwaarden met het besluit meegaan; dat doel vereist niet de gehele historische aanloop. | De lezer moet onderwijsontwerp, bronstatus en vervallen claims verwerken vóór de relevante verwijderfeiten. Dat kan de nieuwe redenering over risicokeuze onderbreken; geen gemeten effect. | Houd in de hoofdroute één concrete voorwaarde en haar gevolg voor de volgende rol; zet het volledige historische fragment bij naslag. Behoud bronbeperking expliciet. P1. | R23–38 legt het verschil tussen testen, kwaliteitsoordeel, C4 en merge scherp uit. R96–114 onderscheidt ontbrekend API-herstel van vernietiging en legt het mechanisme van bevestiging en soft-delete uit. |
| 6. `05-poort/oefening.md` | R68 vraagt “de bron van je menselijke besluit”, terwijl de student zelf die bron is. R70 vraagt “welke vragen je expliciet veilig kunt uitstellen”; voorbeelden tonen een REVISE-reden en plannervraag, maar geen ingevuld bronveld of veilige uitstelafweging. | Wie C4 wel kent, moet nog bepalen of bron persoon/datum/document/verwijzing betekent en hoe een uitstelbare vraag verschilt van een noodzakelijke herstelvoorwaarde. | Toon één minimaal ingevuld bronveld voor deze oefensituatie, en één gemotiveerde uitstelbare vraag tegenover een noodzakelijke voorwaarde. P1/P2. | P1 is afgebakend in r40–49; r53–64 geeft een uitvoerbare herstelvraag. R28–36 laat de lezer testnaam, assert en feitelijk gedrag vergelijken. |
| 7. `06-ontwerpen/index.md` | R21–23 vraagt “Werkwijze, medium en tool onderscheiden” en zeggenschap meewegen. Dit nieuwe onderscheid wordt in de les wel uitgelegd. R38–42 noemt “bronmapping” en “beginstappen”, maar beide links gaan naar de volledige praktijkpagina. | De index oriënteert voldoende; de naam van het doel is duidelijker dan de aankomst van de link. Een lezer moet zelf twee gedeelten in een lange pagina vinden. | Verwijs rechtstreeks naar de bronmapping en de beginstappen. P2. | Leeruitkomsten noemen ontwerp, randvoorwaarden, proces en menselijk oordeel; geen lege algemene afsluiting. |
| 8. `06-ontwerpen/les.md` | R54–56 vraagt “Voor stijl, type checking, linting en formattering ... wat je inzet en waarom”, na slechts één formattervoorbeeld. Geen voorbeeld toont een weggelaten controle met de resterende beoordelingsvraag. Links r77 en r83 naar “bronmapping” en “exporttabel” landen op de hele praktijkpagina. | Engineeringtermen mogen bekend zijn, maar de transfer van toolkeuze naar bewijsgrens wordt voor drie keuzes aan de lezer overgelaten. De les maakt niet zichtbaar hoe een aanvaardbare weglatingsreden eruitziet. | Geef één afweging die een controle weglaat en de resterende vraag aan een beoordelaar toewijst; geen volledige herintroductie van tools. Maak praktijkverwijzingen gericht. P2. | R26–31 gebruikt een uitleenhandeling als vertrekpunt. R95–105 vergelijkt twee concrete implementaties en verbindt duplicatie met een latere wijziging: sterke zelfstandige SE-transfer. R67–76 legt werkwijze/medium/tool met daadwerkelijke opslagplaatsen uit. |
| 9. `06-ontwerpen/oefening.md` | Stap 4 r100–113 combineert route, bevoegdheid, criteria, planner/verhelderaar, planversie, C4 en LIGHT-uitzonderingen. Stap 6 r128–148 combineert contextisolatie, architectuur, C6/C7, synthese/arbitrage, twee herstelgrenzen, nits, merge en status. “C5-kern” en “expliciete herstelbijlage” worden genoemd zonder directe contractlink bij deze handeling. | Eerdere kennis wordt terecht aangesproken, maar de beslismomenten en concrete overdrachten zijn binnen lange stappen lastig afzonderlijk terug te vinden. Zelfstandig uitvoeren vergt reconstrueren welke rol wanneer welke documenten krijgt, vooral in het minder waarschijnlijke herstelpad. | Maak binnen stap 4 en 6 afzonderlijke beslismomenten met invoer/uitkomst en gerichte verwijzingen naar C1, C5/C6 en herstelbijlage. Zet hersteltoelichting bij “als geblokkeerd” en behoud de grenzen. P1. | Voorbereiding r17–29 verwijst naar verworven kennis. Basiskeuze, terugvaloptie en “Klaar wanneer”-criteria maken uitvoering controleerbaar. R180–183 vraagt één criterium van opdracht tot besluit te volgen, een concrete dossiercontrole. |
| 10. `praktijk/van-werkitem-naar-pull-request.md` | R48–57 toont W1, C1/C2/C4/C5/C6, P1 en S1–S4 samen; r59 stuurt naar volledige overdrachten. In “Zelf beginnen” r191–195 moet de lezer C1 vastleggen en een planner P1 laten maken, terwijl de concrete invoer/uitvoer eerder r80–90 staat. R237–289 volgt nog platformvergelijking, export en echte projecthistorie na de GitHub-uitvoering. | Het voorbeeld heeft een begrijpelijke hoofdroute, maar uitvoering vraagt heen-en-weerzoeken voor codes en sessie-invoer. Naslag voor verhuizing kan als verplichte voortzetting worden gelezen; bronhistorie is een ander leesdoel. | Label codes bij eerste tabel compact of wijs naar ingevulde overdracht. Link uitvoerstap 4 rechtstreeks naar sessie-invoer. Markeer verhuizing en projecthistorie als afzonderlijke naslagroutes, zonder nuttige inhoud te verwijderen. P2. | R5–15 begint bij een concrete informatiebehoefte en benoemt voorkennis. R64–90 maakt handmatige sessies, leesbare bestanden en ontbreken van automatische agentstart uitvoerbaar. R99–142 groene tests/blokkade/herstel is een sterk worked example. R146–160 verklaart waarom exacte commits en plansnapshots nodig zijn. |

## Overkoepelende afbakening

- Geen zelfstandige bevinding “klinkt als AI”: in deze pagina's overheersen concrete handelingen, expliciete grenzen en functionele tegenstellingen. Formuleringen zoals “geen automatische merge” dragen een werkelijk procesverschil en blijven.
- De herhaalde terugblikken, zelfchecks en overgangsteksten vervullen het verplichte modulestramien. Niet integraal schrappen als herhaling. Wel kan de losse sectie “Leeruitkomsten” met alleen een verwijzing (4 les r9–11, 5 les r15–17, 6 les r18–20) redactioneel korter zonder de indexleeruitkomsten te dupliceren; P3.
- Grootste winst ligt bij toegepaste onderscheidingen: dekking versus softwaregoedkeuring; synthese versus arbitrage; besluitbron en uitstelbare vraag; controlekeuze versus resterende beoordeling; reguliere route versus herstelpad.
- Latere modules hoeven rollen en SE-principes niet opnieuw volledig te introduceren. Gerichte vindplaatsen en een klein transfervoorbeeld zijn passender dan alle vaktermen verwijderen of een gehele les herschrijven.
- Nader menselijk/studentonderzoek kan uitwijzen of de veronderstelde leesproblemen optreden. Het huidige dossier onderbouwt tekstkeuzes, geen uitspraken over feitelijke leerprestaties of begrip.
