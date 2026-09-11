# Proportionele routes en gericht herstel (#29)

## Besluit en grondslag

De mens gaf opdracht tot uitvoering na het [concrete voorstel op #29](https://github.com/misja/agent-role-loop/issues/29#issuecomment-5641462973).
Het [C1/C4-uitvoeringsrecord](https://github.com/misja/agent-role-loop/issues/29#issuecomment-5641493461)
registreert dat besluit, de rolbezetting, criteriumtoewijzing en aangewezen
onderwijspassages. Basis: `bc08df79d1a165ee59bae5c9bb0642556db1db0c`.
Merge blijft een afzonderlijk menselijk besluit. De nieuwe norm geldt pas na
invoering voor nieuw gestarte werkitems; lopend werk houdt zijn vastgelegde basis.

De routenorm staat in [core/loop.md](../core/loop.md). Dit verslag registreert de
aanleiding en controle, en voegt geen procesregels toe.

## Vergelijking met Programmeren #203

Bronnen: [issue #203](https://github.com/hanze-hbo-ict/programmeren/issues/203),
het [menselijke besluitpakket](https://github.com/hanze-hbo-ict/programmeren/issues/203#issuecomment-5625179565),
het [proefverslag](https://github.com/hanze-hbo-ict/programmeren/blob/main/onderzoek/203-proef.md)
en de lokaal gelezen `.claude/agent-role-loop/core/loop.md` uit dat project.
De gelezen registratie beschrijft voorgestelde praktijkproeven; zij levert nog
geen vergelijkbare effectmeting van de nieuwe generieke routes.

| Maatregel uit #203 | Voorstel voor de generieke lus | Reden |
|---|---|---|
| Triage door de orkestrator | Overnemen; een aparte triage-agent is optioneel. | De verantwoordelijkheid blijft zichtbaar in C1 zonder standaard extra overdracht. |
| Minder vaste rollen | Overnemen, met criteriumtoewijzing en motivering van extra perspectieven. | Het aantal agents volgt uit het werk; minder agents mag geen ongedekt criterium opleveren. |
| Gecombineerde verkenning/ontwerp | Planner onderzoekt zelf; een afzonderlijke feiteninventarisatie alleen bij expliciete noodzaak. | De generieke planner doet al repositoryonderzoek. Geen nieuw verplicht verkennercontract invoeren. Een apart feitenartefact wordt gericht als bron van C2 aangewezen. |
| Besluiten en objectief bewijs naar beoordelaars | Overnemen in C5-kern. | Een geïsoleerde context moet wel de geldende opdracht en controleerbaar bewijs bevatten. |
| Auteurscontext behouden bij reparatie | Overnemen; geen verplichting context weg te gooien binnen dezelfde herstelopdracht. | De onafhankelijkheid is vooral bij de beoordeling nodig. |
| Gericht herstel en eindige rondelimiet | Overnemen: één automatische herstelronde per ontwerp en per oplevering. | Herstel blijft begrensd en controleerbaar. |
| Hoofdbeoordelaar alleen bij tegenspraak | Overnemen; mechanische samenvoeging door orkestrator als oordelen verenigbaar zijn. | Alleen inhoudelijke arbitrage vraagt die afzonderlijke rol. |
| Eerstejaars-, onderwijs- en curriculumrollen | Niet overnemen in core. | Dit zijn projectgebonden verantwoordelijkheden; de vier bestaande generieke perspectieven blijven beschikbaar. |
| 30%-besparingsdoel en 70%-budgetgrens | Niet als generieke norm overnemen. | Dit zijn proefafspraken, geen aangetoonde optimale grenzen. Een project kan vooraf een budget en handelwijze vastleggen. Onbekende usage blijft onbekend. |
| GitHub als vaste opslag | Alleen projectpraktijk, geen core-eis. | De core blijft onafhankelijk van een tracker; dit project bewaart werk en overdrachten op GitHub. |

De historische registratie noemt zowel terechte vondsten als herhaling door ontbrekende besluiten en doorgroeiend herstel. Dat motiveert een ontwerpwijziging, maar bewijst niet dat een specifieke rol overbodig is of dat een vast besparingspercentage haalbaar is. De proefopzet en meetbeperkingen uit #203 blijven als bron herkenbaar.

## Uitgevoerde wijziging

C1 legt verantwoordelijkheden en criteriumdekking vast. LIGHT behoudt review;
PLANNED betekent niet automatisch dat iedere beschikbare rol wordt gestart.
De eerdere tegenstelling tussen “skip planning and review” in C1 en de wel
getekende review is daarmee opgeheven. C0 blijft ongewijzigd.

C5-kern draagt de relevante besluiten en objectieve verificatiebewijzen. De
scheiding met uitgebreide auteursinformatie volgt nu het doel van de
beoordeling: geen maaktranscript, wel de vastgelegde basis waarop geoordeeld
moet worden. C3 en C6 maken herstelmodus herkenbaar. Core en bestaande adapters
gebruiken dezelfde contractversie en bewaren de herstelstand bij het werkitem.

De handmatige adapter, Claude-command en wrappers, en negen API-voorbeeldpayloads
zijn aangepast. Dit is geen nieuwe providerintegratie. README, begrippenlijst,
kwaliteitsraamwerk en de aangewezen passages in modules 1 en 4 sluiten hierop aan.
Vier perspectieven blijven een expliciete oefenkeuze. De kostenaanwijzing in
module 1 maakt nieuwe functionaliteit en datamigratie niet langer automatisch
LIGHT. De brede redactie en praktische installatiehandleidingen blijven bij
hun eigen werkitems.

## Zes scenario’s: controle van de beschrijving

Onderstaande controle is een handmatige doorloop van de gewijzigde teksten.
De invoer is geconstrueerd om een beslispunt te onderzoeken; er zijn geen zes
praktijkwerkitems door agents uitgevoerd. Per scenario is ook nagegaan welke
ontbrekende informatie of blokkade het werk tegenhoudt.

| Scenario en invoer | Criteriumdekking en waargenomen route in de teksten | Volgende stap en stopmoment |
|---|---|---|
| 1. Spellingcorrectie. C0: wijzig één verkeerd gespeld label; AC1 juiste spelling, AC2 geen gedragswijziging. C1 LIGHT met controle van label en diff. | C1 wijst AC1/AC2 aan één beoordelaar toe. De bouwer ontvangt C0 + C1, levert C5 met exacte wijziging en waargenomen controles. Geen C2/C3 of routinematige C4. | C6 is zelfstandig eindverdict; SHIP gaat naar menselijke merge. Een onbedoelde codewijziging blokkeert AC2 en kan één gericht herstel krijgen. Vindplaatsen: loop Responsibilities, C1 LIGHT execution basis, C6. |
| 2. Afgebakende exportreparatie. C0: geen dubbele orderregels (AC1), bestaande enkelvoudige export blijft gelijk (AC2). C1 PLANNED, één strikte beoordelaar. | Planner maakt C2 met verificatie per criterium en C1-toewijzing. C4 verwijst naar de concrete planversie. C5 geeft beide bewijsplaatsen mee; C6 toetst AC1/AC2. Verheldering is optioneel met motivering in C1. | Zonder toepasselijke menselijke C4 bouwt de bouwer niet. Ontbrekend AC2-bewijs mag niet passeren. Vindplaatsen: loop Contracts, C2, builder Inputs, C6. |
| 3. Gedeeld datatype. C0: gewijzigde datumrepresentatie; AC1 conversie juist, AC2 twee bestaande afnemers blijven werken. | C1 benoemt gedeelde afnemers en kiest verhelderaar plus twee passende perspectieven: correctheid voor AC1, compatibiliteit voor AC2. C2 plant controles van beide afnemers. C3 toetst plan/dekking; C4 vóór bouw. Twee C6’s gaan pas na volledige ontvangst naar C7. | Ontbrekende afnemertest blokkeert AC2. Een tijdens herstel geraakte derde afnemer kan eerder bewijs ongeldig maken: expliciete herplanning en zo nodig bredere review, zonder tellerreset. XL wordt eerst gesplitst. Vindplaatsen: loop Responsibilities en Isolation, C1 Risks, C5 Contracts. |
| 4. Eerder menselijk besluit. C2 noemt datumvolgorde; C4 staat ID-volgorde expliciet toe voor AC2, met bron en versie. | C5-kern draagt deze toegestane afwijking, normversie en objectief resultaat. De reviewer toetst de uitvoering aan het geldende besluit. De geïsoleerde context verliest deze informatie dus niet. | Geen hernieuwde toestemming voor dezelfde afwijking. Een niet door C4 toegestane wijziging aan het bestandsformaat blijft een nieuwe keuze en blokkeert verder werk. Vindplaatsen: C4 Artifact and source, C5 Scope and human decisions, reviewer Guardrails. |
| 5. Gerichte reparatie. Eerste C6 blokkeert AC2; AC1 is vastgesteld op revisie A. Herstelstand oplevering 0. | Vóór reparatie wordt oplevering 1 geregistreerd. Auteur mag context houden en levert revisie B. Onafhankelijke herstelbeoordelaar krijgt C5-kern, A..B-diff, AC2-blokkade en eerdere AC1-dekking. Hij controleert AC2 en gevolgen voor AC1; ongeraakt geldig bewijs heet eerder vastgesteld. | Resterend AC2-probleem gaat naar de mens voor een begrensd vervolg, splitsen of stoppen. Een nieuwe sessie levert geen tweede automatische ronde. Bij ongeldig geworden AC1-bewijs moet dit opnieuw worden onderzocht. Dezelfde grens is voor ontwerp met C3 beschreven. Vindplaatsen: loop Isolation, C3 Repair state, C6 Inputs and modes. |
| 6. Tegenspraak. Strikte reviewer vindt AC1 aantoonbaar geschonden; pragmatische reviewer wil dezelfde schending laten passeren. | Orkestrator kan dit niet als verenigbare synthese afdoen. De hoofdbeoordelaar krijgt alle gekozen C6’s en volledige C5; C7 verklaart de afweging per bron. Een ontbrekend tweede oordeel betekent wachten, geen gedeeltelijk eindverdict. | Een geldige onopgeloste schending blijft BLOCK. Een keuze over doel of aanvaardbaar risico gaat naar de mens. Bij verenigbare oordelen kan de orkestrator zonder aparte hoofdbeoordelaar samenvatten. Vindplaatsen: loop Contracts, C7, reviewer-boss. |

Alle zes doorlopen vinden een volgende stap en stopvoorwaarde in core, met
passende uitvoerinstructies in de adapters. Dit toont samenhang van de beschreven
routes, geen garantie dat een model iedere instructie volgt.

## Publicatie en onafhankelijke beoordeling

- `git diff --check`: geslaagd.
- Negen JSON-voorbeelden geparseerd met Python `json.loads`: geldig.
- Schone Sphinx-build met `-E -a -b html -W --keep-going`: geslaagd, 48 pagina’s.
- 45 lokale Markdown-verwijzingen in gewijzigde bestanden gecontroleerd: geen ontbrekende doelen. De Sphinx-build controleert de onderwijspublicatie.
- Headless Chrome: C1, C5, C6, de lus, het kwaliteitsraamwerk en oefening 1 bekeken. De twee Mermaid-diagrammen leveren SVG op; geen horizontale pagina-overloop bij 1280px. Screenshots van schema, contracten en oefening gelezen.
- De eerste diagramweergave was te klein. Het schema is tot hoofdroutes beperkt; `docs/conf.py` gebruikt `mermaid_height = "auto"` zodat lange diagrammen niet in 500px worden samengedrukt. Beide diagrammen opnieuw bekeken: labels leesbaar, kort diagram zonder overmatige witruimte.
- Onafhankelijke beoordeling: wordt vóór oplevering aangevuld.

De objectieve voor-toestand is de beschreven tegenstrijdige LIGHT-instructie en
vaste rolbezetting op de basiscommit. Er is geen falende softwaretest verzonnen
voor deze wijziging van procesdocumentatie. Verificatiemodel:
`manual-with-expected-results` voor de scenario’s, aangevuld met de docs-build
en bestandscontroles.

Niet uitgevoerd: providerpraktijkproef, studentlezing en vergelijkbare
kosten-/kwaliteitsmeting. Tokens, menselijke leestijd en totale doorlooptijd:
niet beschikbaar. De onafhankelijke agentbeoordeling is geen studentproef.
