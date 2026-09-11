# Doelgroep en redactionele uitgangspunten (#37)

## Besluit en afbakening

De gebruiker vroeg om de uitgangspunten projectbreed vast te leggen en gaf
vervolgens opdracht #37 uit te voeren. De inhoudelijke uitgangspunten staan in
[#37](https://github.com/misja/agent-role-loop/issues/37); de begrensde uitvoering
is [op het issue geregistreerd](https://github.com/misja/agent-role-loop/issues/37#issuecomment-5641309996).
De nieuwe doelgroepbeschrijving en gerichte aanvullingen van schrijfwijzer,
conventiepagina en sjabloon voeren die opdracht uit. De projectingangen wijzen
naar dezelfde grondslag. Er komt geen tweede rollenlus bij.

#30 is inmiddels samengevoegd via #38. De afspraak om de doelgroep daar eerst
toe te passen en daarna algemeen te borgen is behouden. #37 heropent de
tekstherziening niet. De normwijziging ligt ter merge aan de mens; de regels
worden niet als reeds ingevoerd voorgesteld zolang de PR openstaat.

## Vijf verificatiescenario’s

| Invoer | Verwachte reactie en verantwoordelijke | Toets aan de normtekst |
|---|---|---|
| De eerste kennismaking zegt “start een agent” zonder eerdere uitleg. | Ontwerper wijst de ontbrekende model-/programma-/contextuitleg aan; auteur bouwt die op; beoordelaar wijst de ontbrekende stap aan als zij blijft ontbreken. | `doelgroep.md` sluit deze voorkennis uit; de schrijfwijzer geeft dit als voorbeeld; de conventiepagina belegt alle drie verantwoordelijkheden. |
| Module 4 gebruikt context nadat de inleiding het heeft uitgelegd. | Ontwerper noemt de eerdere uitleg; auteur verwijst waar nodig. Beoordelaar verlangt geen volledige herintroductie. | `doelgroep.md`, Voortbouwen in de leerlijn, maakt eerder behandelde kennis bruikbaar en vindbaar. |
| Een passage legt zonder aanleiding opnieuw uitgebreid uit wat een test is. | Ontwerper/auteur schrappen overbodige herhaling of motiveren de didactische noodzaak. Beoordelaar toetst tegen de bekende SE-voorkennis. | Het doelgroepdocument noemt tests als bekende kennis en vraagt een reden voor een volledige herintroductie. |
| “Contextisolatie garandeert betrouwbare review.” | Auteur verklaart mechanisme en beperkingen. Beoordelaar vraagt onderbouwing en markeert de ongedekte garantie. | Het voor/na-voorbeeld in de schrijfwijzer laat zien wat ontbreekt; alleen “kan” toevoegen is onvoldoende. |
| Een beoordelaar start zonder gesprekshistorie. | Orkestrator levert de geregistreerde normcommit, relevante leesbare secties en menselijke besluiten. De beoordelaar toetst op dezelfde basis. | Projectingang en conventiepagina regelen vindbaarheid; een nieuwe norm tijdens de taak vraagt een expliciet besluit over toepassing. |

Dit zijn scenario’s voor proces- en normverificatie, geen studentwaarnemingen.
De onafhankelijke beoordeling en build-/weergavecontrole worden op #37 en de PR
vastgelegd. Ontbrekende metingen blijven niet beschikbaar.

## Toepassing op vervolgwerk

#35 en #36 gebruiken de gedeelde normen bij hun start en de samengevoegde tekst
van #30 als uitgewerkt voorbeeld. #31 en studentgerichte uitleg in #32-#34 volgen
dezelfde scopebepaling. Docentmateriaal in #22 en toetsmateriaal in #23 vallen
ook onder de conventies. Geen van deze werkitems hoeft de normtekst te kopiëren.
Lopend werk houdt zijn geregistreerde basis totdat de mens anders besluit.

De aanleiding is een concrete gemiste begripsprong in de eerdere agentlezing
van #30, beschreven in [de redactieproef](30-redactie.md). Een positief oordeel
van een agent vervangt dus niet een expliciet doelgroepbeeld of waarneming bij
studenten. Tokens, agentduur en studentwaarnemingen: niet beschikbaar.
