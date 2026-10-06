# #58 - C1 en C2 v1: aanvullende boekenplankcontroles

## C1 - triage

PLANNED, S. Bron: https://github.com/misja/agent-role-loop/issues/58.
Proces- en projectnorm: b07b477c9fb8aa291753d0c99f70c2b29ee9c72d.
Leesbare grondslag: CLAUDE.md, core/loop.md, core/contracts/build-packet.md,
core/contracts/review-handoff.md en reviewer-verdict.md; teaching/conventies.md,
doelgroep.md, schrijfwijzer.md en begrippen.md op die commit.
Root orkestreert, plant en bouwt na C4. Eén verse onafhankelijke strikte
beoordelaar wordt bij C5 aangewezen voor alle AC1-5: Python/unittest,
regressiedekking en didactische leesgang. Geen aparte verhelderaar: eisen en
broncode zijn concreet; de plaatsingskeuze wordt hier aan de mens voorgelegd.
Ontwerp0, oplevering0; vóór eventueel herstel tellers en bevindingen opslaan.
Geen bouwvrijgave. C4 op dit concrete C2 vereist; mens beslist later over merge.

## Summary

Voeg een aparte aanvullende controlesuite toe aan het gedeelde praktijkvoorbeeld
met False, onafhankelijke lijstcontainers en toevoegen na filteren. Behoud de
vier bestaande S-controles en historische proefdossiers. Lever dezelfde suite
in de downloadbundel en leg nieuw daadwerkelijk rood/groen-bewijs apart vast.

## Goals

1. Maak AC1-3 herhaalbaar met Python 3.10+ en de standaardbibliotheek.
2. Maak plaats, gebruik en bewijsgrenzen zichtbaar zonder bestaande proeven te wijzigen.

## Non-goals

Geen providerproef, productuitbreiding, core-/contractwijziging of nieuwe claims
van studentbegrip. Geen wijziging aan oorspronkelijke controleer.py, codeversies,
patches, overdrachten en bewijs.txt, of onderzoek/32-proef, 33-proef en 34-proef.

## Current state

controleer.py in teaching/cases/praktijk-projectomgeving bevat S1-S4 en de
basis/zwak/regressie/volledig-selectie. boekenplank_b.py geeft twee verse
lijstcontainers terug en gebruikt len(_boeken)+1 voor nummering. A overschrijft
de opslag bij filteren. onderzoek/32-proef/controleer_extra.py controleert False
via nummers en containerwijziging met assert; toevoegen na filteren ontbreekt.
docs/package_practice.py bundelt via een expliciete bestandslijst, met de
historische corebasis ae561f50a45ca42967e4687434cf0d2e8d4f5827.

## Proposed approach

Nieuwe controleer_extra.py in de gedeelde casus importeert de bestaande laadfunctie
uit controleer.py en biedt versiekeuze a/b/werk. unittest, drie afzonderlijke
criteria; falen geeft exit1. Zo blijven bestaande studentcommando's en hun
verwachte testaantallen intact, terwijl aanvullende dekking bereikbaar is.
README krijgt een aparte optionele vervolgsectie na de huidige controles:
probleem, invoer, commando, reden en herkenbare uitkomst. Voorkennis: Python,
tests en de zojuist uitgevoerde S1-S4-casus; nieuwe tussenstap is het onderscheid
tussen een teruggegeven lijstcontainer en de boekobjecten erin. Leg uit dat
containerisolatie geen diepe kopie van de boeken belooft. Geen nieuw LLM-begrip.

## Acceptance criteria

Alle criteria -> één verse onafhankelijke strikte beoordelaar, final C6.

1. Expliciet False levert dezelfde boekobjecten in dezelfde volgorde als standaard;
   test gemengde, lege en volledig uitgeleende plank. Controleer titels/leners mede.
2. Wijzigen van standaard/False-container én gefilterde container laat interne
   opslag en uitleentoestand behouden. Test clear/append/pop met nieuwe planken;
   vergelijk volledige toestandsnapshot en volgende lijstaanroep.
3. Filter gemengde plank, voeg een nieuw boek toe: alle bestaande boeken inclusief
   uitgeleend boek behouden, nieuw boek aanwezig, nummers uniek en in deze fixture
   1,2,3,4. Controleer tevens beschikbaarheidsvolgorde en uitleentoestand.
4. Plaatsingsrationale en nieuw rood/groen-bewijs vastgelegd; historische bestanden
   bytegelijk. Zip bevat nieuwe suite/uitleg met dezelfde bytes als bronnen;
   oorspronkelijke bundelbestanden blijven gelijk behalve expliciete README.
5. Gewijzigde casusuitleg voldoet aan teaching/conventies.md. Onafhankelijke
   leesgang benoemt invoer, handeling, reden, uitkomst en container/objectgrens;
   docs-build -W --keep-going en gerichte lokale linkcontrole slagen.

## Basis and sources

Bovengenoemde normcommit en vindplaatsen; C0 #58; onderzoek/32-proef/C6-main.md,
C6-herstel.md en controleer_extra.py als eerdere bevinding, niet nieuwe meting.
Gedeelde casusbron en docs/package_practice.py rechtstreeks gelezen op deze basis.

## Repair state

Ontwerp0, oplevering0. Geen herstel uitgevoerd. Tellerregistratie vóór herstel;
na verbruik uitsluitend menselijke begrensde vervolgopdracht volgens core/loop.md.

## Interfaces / contracts / data changes

Nieuwe optionele CLI: python3 -B controleer_extra.py a|b|werk. Bestaande CLI blijft.
Bundel krijgt één nieuw bestand; historische gebundelde procesbasis blijft gelijk.

## Changes

### Eén pakket: suite, uitleg, bundel en bewijs

**Goal:** borg AC1-5 met zelfstandige aanvullende controles.

**Non-goals:** bovenstaand.

**Files or components:** teaching/cases/praktijk-projectomgeving/controleer_extra.py
(nieuw), README.md, docs/package_practice.py, teaching/praktijk/boekenplank-projectomgeving.zip;
onderzoek/58-uitvoering.md en geselecteerd nieuw bewijs onder onderzoek/58-proef/.

**Implementation checklist:**

- [ ] Schrijf drie criteriumgerichte tests en voer eerst op foutvarianten uit.
- [ ] Gebruik A voor de werkelijke opslag/nummeringregressie; voor False en
  containeraliasing maak uitsluitend tijdelijke gerichte foutvarianten onder /tmp.
- [ ] Bewaar gebruikte tijdelijke foutdiffs, uitvoer en exitcodes als nieuw bewijs.
- [ ] Voer dezelfde ongewijzigde tests uit op bestaande B: verwacht alle groen,
  zonder productfix. Ook werk-selectie op tijdelijke B-kopie moet groen geven.
- [ ] Schrijf optionele uitleg, voeg suite aan bundellijst toe en regenereer zip.
- [ ] Controleer oude hashes/commando's, bron-zipgelijkheid, docs en links.
- [ ] Leg exacte productcommit, feitelijke controles en bewijsgrenzen in C5 vast.

**Verification plan:** validation-workflow. Dit is uitbreiding van regressiedekking
van reeds correcte B-code; kunstmatig productrood of een productfix zou misleiden.
Nieuwe rood/groen-uitvoering gebruikt bekende A en gerichte tijdelijke mutanten
als bewijs dat iedere nieuwe controle de bedoelde fout kan herkennen. Verwacht
False-mutant AC1 rood, containeraliasmutant AC2 rood, A AC3 rood; B alle drie groen,
exit0. Noteer eventuele extra fouten afzonderlijk. Oude vier commando's behouden
respectievelijk 1pass/0, 3pass/0, 1fail/1, 4pass/0. Build/linkcontrole is technische
verificatie; onafhankelijke agentlezing blijft agentlezing, geen studentproef.

**Rollout / rollback:** reversible Git-change; zip uit bronnen opnieuw genereerbaar.

**Done when:** alle AC gedekt, onafhankelijke C6 SHIP of SHIP WITH NITS;
menselijk mergebesluit blijft vereist.

## Risks

Een nieuwe suite in de oude volledig-selectie zou historische aantallen veranderen;
daarom aparte CLI. Mutantgroen bewijst uitsluitend gemeten foutgevoeligheid,
geen algemene correctheid. Boekobjectmutatie valt buiten lijstcontainerisolatie.

## Assumptions

Geen provider nodig. B hoort te slagen op nieuwe criteria; uitvoering bevestigt dit.

## Open questions

Menselijke C4: akkoord met deze plaatsingskeuze, optionele casusuitleg, aanvullende
bundelsuite en validation-workflow met tijdelijke mutanten in plaats van productfix?
