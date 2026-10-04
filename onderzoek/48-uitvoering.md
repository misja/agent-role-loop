# #48: de eerste uitvoering begeleiden

## Besluit en grondslag

De gebruiker gaf akkoord op C2 v1, onderzoek/48-plan.md, commit b26a84a.
[C4 PROCEED](https://github.com/misja/agent-role-loop/issues/48#issuecomment-5982620818)
geeft de aparte begeleide pagina en gerichte modulecorrecties vrij. Het besluit
behoudt de vijftien requirements, drie porties, eigen uitvoering en latere
afnemende ondersteuning. Geen mergebesluit.

Proces- en normbasis: `e0f064aa7e5642b272d82e5db227e9b53d6a5de4`, met de expliciete
controleaanvulling in teaching/conventies.md op b26a84a. De gebruiker vroeg eerst
inhoud, screenshots alleen bij vormgeving of een concreet weergaveprobleem, en
vervolgens vastlegging van die afspraak. AC7 van #48 is op dat besluit bijgesteld.
De afspraak wordt in deze PR duurzaam meegenomen; geen screenshotcontrole nodig.

C1 staat [op #48](https://github.com/misja/agent-role-loop/issues/48#issuecomment-5982602267):
PLANNED, M, root als planner/bouwer, één verse onafhankelijke reviewer voor AC1–7.
Geen afzonderlijke inventarisatie of planreview geselecteerd. Herstelstand:
ontwerp 0, oplevering 0, volgens core/loop.md; een sessie reset haar niet.

## Voor en na

| Eerdere passage | Gerichte wijziging | Functie voor de student |
|---|---|---|
| Deel B noemt acht stappen met codes; code toepassen en checks uitvoeren ontbreken als afzonderlijke handeling. | Zeven beslismomenten met expliciete bouw-/controlehandeling, invoer en opgeslagen uitvoer. | De student weet wie de code werkelijk wijzigt en hoe bewijs de volgende rol bereikt. |
| Voorbereiding toont één C5-fragment. | Aparte pagina met de volledige portie-1-keten, voorbeeldinvoer/rolprompt en ingevulde uitvoer per overgang. | De student kan een eerste plannerchat voorbereiden en een criterium volgen tot het eigen besluit. |
| Nummerhergebruik wordt bij een opslagwijziging genoemd zonder moment van eis 13. | Controle na portie 3; requirement 12 blijft het mogelijke wijzigingsmoment, 13 de dan geldende eis. | Nog niet aangeboden eisen worden niet als vergeten afspraken voorgesteld. |
| Requirements 9/12 heten gevoelig voor vergeten instructies zonder bewijs. | Specifieke claim verwijderd; eigen waarneming en afwezige symptomen blijven mogelijk. | Geen vooraf gestuurde uitkomst of methodegarantie. |
| Budgetvariant staat na de hele route. | Uitvoeringskeuze vóór de eigen stappen. | Selectie van beoordelaars wordt vooraf in C1 vastgelegd; kosten veranderen de route niet automatisch. |
| Module-index verwijst alvast naar praktijkvoorbeeld na module 2. | Ingang naar begeleide uitvoering na deel A; praktijk blijft in algemene navigatie en module 2 beschikbaar. | De eerste oriëntatie vraagt geen zijpad dat nog niet nodig is. |

Alle vijftien requirements en portietekst zijn bytegelijk aan de basis.
Leerdoel/leeruitkomst op de index en de hele lesstaart zijn exact behouden.
De beginzin van de les verwijst naar het zojuist gemaakte deel A in plaats van
algemene zelfstandige beheersing te veronderstellen. Andere modules, code,
casussen, voorbereiding, core en adapters zijn ongewijzigd.

## Voorbeeld en bewijsgrenzen

De begeleide pagina is een geconstrueerd onderwijsvoorbeeld, geen echte run.
W1/P1/B1 en de ingevulde C3/C4/C5/C6/C7 maken vorm, invoer en ontvanger zichtbaar.
B1 is geen beschikbare repositorycommit; de student moet bij eigen uitvoering
echte bestanden, exacte versies en waargenomen resultaten meegeven. De pagina
benoemt deze grens vooraf en bij de code- en reviewovergang.

Controles K1–K5 dekken de eerste vijf CLI-eisen. K5 staat vóór terugmelden K4,
zodat een nieuwe aanroep de nog bestaande uitlening aan Noor kan lezen.
Voorbeelden gebruiken enkelvoudige titels/auteurs; requirements 6–15 worden
niet stilzwijgend in de eerste portie getoetst. Vier ingevulde beoordelingen
mogen verenigbaar zijn; de orkestrator syntheseert, de hoofdbeoordelaar komt
alleen bij inhoudelijke tegenspraak aan bod. Menselijk plan- en acceptatiebesluit
blijven onderscheiden en zijn voor de eigen uitvoering nooit vooraf ingevuld.

Student-/docentwaarnemingen, leereffect, daadwerkelijke agentrun, gemeten duur
of kostenbesparing zijn niet beschikbaar. De bestaande duurindicatie is behouden,
maar niet gemeten of gevalideerd. Bewijs van routeleesbaarheid komt uit C6,
niet uit de docs-build of de geconstrueerde waarnemingen.

## Verificatie vóór onafhankelijke review

Verificatiemodellen: manual-with-expected-results voor passage/routelezing;
validation-workflow voor build, links en beschermde vergelijking. Geen codegedrag
gewijzigd, dus geen nieuwe code- of tekstspiegeltests.

- Requirements/porties, indexleeruitkomst en vaste lesstaart exact vergeleken
  met de basis: gelijk. Nieuwe pagina alleen binnen module 1.
- `git diff --check`: schoon. Geen em/en-dash in de modulepagina's.
- Eerste build vond een ongeldige automatisch afgeleide koplink naar deel B.
  Hersteld met een expliciet MyST-label; dit is bouwverificatie vóór C6, geen
  verbruikte onafhankelijke herstelronde.
- Finale build- en lokale linkuitkomsten worden in C5 met de exacte productcommit
  vastgelegd. Geen browser of screenshots gebruikt, conform gebruikersbesluit.

#49 krijgt deze complete eerste uitvoering als bron voor latere eigen
contractanalyse. #22/#23 blijven eigenaar van docentmateriaal en toetsing.

Finale controles vóór C6: `make -C docs html` onder `-W --keep-going` geslaagd
zonder waarschuwingen; /tmp/arl48-build.log. Linkscript /tmp/arl48-links.py over
vier modulepagina's en de gewijzigde conventiepagina: 391 lokale links/fragmenten,
geen fouten. Beschermde vergelijking opnieuw geslaagd; diffcontrole schoon en
geen em/en-dash in module 1. Externe websites niet integraal gecontroleerd.
