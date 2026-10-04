# #48: plan voor de eerste begeleide uitvoering

Status: C2 v1, voorstel vóór uitvoering. C0 staat op
[issue 48](https://github.com/misja/agent-role-loop/issues/48).

## Summary

Laat portie 1 één keer zien als een complete uitvoering met losse chats: opdracht,
plan, menselijk besluit, code toepassen, controles, beoordelingen en overdracht
naar portie 2. Houd de eigen oefening compact door het ingevulde voorbeeld op een
aparte pagina te plaatsen, die pas na deel A wordt gelezen.

## Goals

1. De student kan voor iedere overgang aanwijzen wie handelt, wat meegaat,
   waarom dat nodig is en welke uitvoer wordt bewaard.
2. Een chatvoorstel, toegepaste code en waargenomen controle-uitvoer blijven
   onderscheiden. Alle vijf criteria van portie 1 zijn terug te vinden.
3. De student voert daarna de drie eigen werkitems uit met dezelfde eisen,
   onafhankelijke beoordelingen en menselijke besluiten.

## Non-goals

Geen nieuwe requirements, casusimplementatie, providerkeuze of contractnorm.
Geen herschrijving van andere modules, voorbereiding, adapters of toetsing.
Geen uitgevoerde LLM-run, studentvalidatie of belofte dat de bestaande duur klopt.
Geen routinematige screenshots of beeldcollages.

## Current state

Module 1 deel B noemt acht stappen met C0–C7. De daadwerkelijke bouwactie en
uitvoering van tests staan niet als afzonderlijke stap. De voorbereiding uit #46
laat één C5-fragment zien, maar nog geen volledige portie-1-keten. De les gebruikt
requirement 13 bij een verandering aan requirement 12 zonder de tijdvolgorde
expliciet te maken. De oefening suggereert gevoeligheid van requirements 9/12
zonder bewijs. De budgetvariant staat pas na de procedure.

Bord gecontroleerd: #46 Done, #48/#49/#22/#23 Backlog. #49 bouwt op deze eerste
uitvoering voort. De eerder vastgelegde visuele controleafspraak is de enige
lokale wijziging bij de start; #48-productteksten zijn nog ongewijzigd.

## Proposed approach

De pagina `teaching/modules/01-ervaren/eerste-uitvoering.md` toont één geconstrueerde
uitvoering van portie 1. Zij krijgt een ingang bij “Beginnen met deel B” en in de
module-navigatie na de oefening. De openingsaanwijzing noemt het leesmoment: na
deel A en les 1, vóór de eigen deel-B-uitvoering. Het voorbeeld vervangt de eigen
code, controles en logboeken niet.

Gebruik één herkenbare controle: registreer een boek, bekijk de lijst, leen uit,
controleer status/lener, meld terug en controleer opnieuw. Een nieuwe aanroep
controleert dat de gegevens bewaard zijn. Maak oplopende nummers zichtbaar met
een tweede boek. De latere eisen over dubbele uitlening, datum en nooit
hergebruikte nummers worden niet als portie-1-criteria toegevoegd.

Per overgang toont de pagina de concrete bronnen, rolprompt of menselijke
handeling, ingevulde uitvoer en volgende ontvanger. Gebruik vaste voorbeeldnamen
W1, P1 en B1 met betekenis bij eerste gebruik. Leg de gekozen echte normcommit vast;
B1 is een gelabelde voorbeeldsnapshot, geen bestaande repositorycommit of gemeten
run. Verwachte en voorbeeldmatig waargenomen uitkomsten heten uitdrukkelijk
illustraties. De student bewaart bij eigen uitvoering echte versies en resultaten.

## Acceptance criteria

C0 AC1–7 behouden; AC7 is op expliciet gebruikersbesluit bijgesteld naar inhoud,
build en links, zonder verplichte visuele lezing bij uitsluitend tekstwerk.
Alle criteria zijn toegewezen aan één verse onafhankelijke reviewer `/root/review48`.

| AC | Wijziging en verwachte verificatie-uitkomst |
|---|---|
| 1 | Volledige portie-1-keten op nieuwe pagina; lezer kan iedere bron, rolprompt/handeling, ingevulde uitvoer en ontvanger aanwijzen. |
| 2 | Bouwerovergang noemt code toepassen, daadwerkelijke checks en bewaren van uitvoer; vijf eisen, versie en normbasis volgen mee tot oordeel. |
| 3 | Les preciseert controle na portie 3; oefening verwijdert de ongedekte specifieke gevoeligheidsclaim. Geen gegarandeerd symptoom of methodewinst. |
| 4 | Budgetkeuze vóór uitvoering, nog steeds PLANNED; geselecteerde onafhankelijkheid, echte mensbesluiten en herstelgrenzen behouden. |
| 5 | Vijftien requirements en portietekst bytegelijk; precies drie eigen werkitems en behoud van eerdere eisen bij elke volgende portie. |
| 6 | Leeruitkomstbetekenis, vaste lesstaart, casusgedrag en eigen reflectie behouden. Alleen module 1 krijgt de extra steun. |
| 7 | Passagelezing tegen vastgelegde normen; schone build onder -W --keep-going, lokale links zonder fouten, diffcontrole. Onderzoek vermeldt bewijsgrenzen. |

## Basis and sources

Proces/normbasis `e0f064aa7e5642b272d82e5db227e9b53d6a5de4`: CLAUDE, core/loop,
rolprompts en contracten; doelgroep, schrijfwijzer, conventies, begrippen.
Aanvullende expliciete gebruikersinstructie: inhoud eerst, screenshots alleen bij
vormgeving of een concreet weergaveprobleem; vastgelegd in conventies,
“Controles bij tekstwerk”, blob `6d5ccfd51698377366726163c6b0c0c51295a4d2`.
Neem deze al besloten registratie mee in dezelfde PR, zonder opnieuw toestemming
voor die afspraak te vragen.

Bronnen: module 1 index/les/oefening, voorbereiding van-chat-naar-agent.md,
adapters/manual/README.md en handoff-log-template.md, onderzoek/46-inventarisatie-en-plan.md
vroege bevindingen 1–7 en onderzoek/46-uitvoering.md. Geen nieuwe externe bronclaims.

## Repair state

Ontwerp 0, oplevering 0; stand en eventuele bevindingen op #48. Geen resets bij
nieuwe sessies. Maximaal één automatische herstelronde per fase volgens core.

## Interfaces / contracts / data changes

Geen generieke contract- of codewijziging. De nieuwe pagina is onderwijsondersteuning
voor bestaande contracten. Index en les/oefening wijzen samen naar die uitlegplek.
Conventies bevatten de al door de gebruiker besloten beperking op visuele controles.

## Changes

### 1. Eén ingevulde uitvoering vóór deel B

**Goal:** de student kan een complete eerste uitvoering volgen en daarna zelf handelen.
**Files:** nieuwe eerste-uitvoering.md; index.md voor navigatie, les.md en
 oefening.md voor de gerichte ingang. Geen volledige rolcontracten in de intro.

**Implementation checklist:**

- [ ] Begin met W1: de vijf ongewijzigde criteria van portie 1, bron en normversie.
- [ ] Toon ingevulde C1 met de bestaande oefenkeuze PLANNED, planner/verhelderaar,
  vier beoordelaarsperspectieven en volledige criteriatoewijzing.
- [ ] Toon de plannerinvoer en concrete rolprompt, P1 met aanpak/controleplan,
  vervolgens eigen verhelderaarinvoer/prompt en een onderbouwde voorbeeld-C3.
- [ ] Toon een ingevuld menselijk C4 voor P1, met bron en versie. Het is een
  voorbeeld van een mensbesluit, geen toestemming voor de eigen uitvoering.
- [ ] Toon de builderinvoer/prompt, wie het voorstel toepast en controles uitvoert,
  plus een ingevulde overdracht met criteria, versie, verwachting/waarneming en
  beperkingen. Markeer alle voorbeeldgegevens als geconstrueerd.
- [ ] Geef de vier onafhankelijke beoordelaars afzonderlijke invoer/prompt en
  ingevulde, criteriumgebonden C6's. Geen vooraf geforceerde tegenspraak. Zij
  ontvangen geen maaktranscript of andere initial oordelen.
- [ ] Toon herleidbare samenvoeging van verenigbare oordelen in C7 en het aparte
  menselijke besluit over B1. Benoem gericht wat bij een blokkade gebeurt met
  bronlink naar core; geen volledige tweede herstelprocedure.
- [ ] Sluit af met de overdracht naar het werkitem voor portie 2: behouden eisen,
  nieuwe criteria, werkelijk geaccepteerde versie en eigen logboek. Portie 3
  gebruikt dezelfde werkwijze; totaal drie werkitems.

**Verification plan:** manual-with-expected-results. De onafhankelijke lezer volgt
één criterium van W1 tot besluit, wijst voor elke overgang bron/uitvoerder/invoer/
uitkomst aan en kan één eigen eerste chat voorbereiden zonder ontbrekende kennis.
Controleer dat alle normatief verplichte velden vindbaar zijn; fragmenten worden
als fragment gemarkeerd en vervangen geen complete vereiste invoer. Geen test-first:
er verandert tekst en ondersteuning, geen codegedrag.
**Rollout/rollback:** nieuwe pagina en ingangen samen aanbieden; gewone revert van
het documentatiepakket. **Done when:** AC1/2/5/6 gedekt door die leesgang.

### 2. Gerichte correcties en eigen uitvoering

**Goal:** de eigen oefening blijft uitvoerbaar met eerlijke verwachtingen.
**Files:** module 1 index.md, les.md en oefening.md.

**Implementation checklist:**

- [ ] Lesvoorbeeld: “Na portie 3 controleer je of verwijderde boeknummers opnieuw
  worden gebruikt. Requirement 13 verbiedt dat.” Koppel een eventuele opslagwijziging
  aan requirement 12 zonder een nog niet gegeven eis als vergeten eis voor te stellen.
- [ ] Schrap de specifieke gevoeligheidsclaim voor 9/12; laat eigen waarnemingen,
  geen symptomen en meerdere verklaringen toe.
- [ ] Geef budgetvariant een herkenbare keuze vóór deel B; behoud bestaande
  oefenoptie van vier perspectieven bij portie 2 en passende dekking elders.
- [ ] Splits de eigen route in duidelijke beslismomenten met bronlinks naar de
  begeleide uitvoering: plannen, mensbesluit, toepassen/checks, beoordelen,
  samenvatten en eigen acceptatiebesluit. Behoud versie-/herstellogboek.
- [ ] Laat de praktijkverwijzing na module 2 beschikbaar als naslag, zonder extra
  leesopdracht bij eerste oriëntatie. Behoud leeruitkomst en modulevolgorde.

**Verification plan:** manual-with-expected-results voor tijdvolgorde/claims/
uitvoerstappen; validation-workflow voor vergelijking van requirements en
leeruitkomsten tegen de basis, `make -C docs html`, lokale links en
`git diff --check`. Verwacht gelijke beschermde eisen/porties, geen waarschuwingen
of kapotte links. Geen codegedrag gewijzigd, dus geen nieuwe tests voor tekst.
Geen browser-/screenshotcontrole tenzij een concreet probleem ontstaat.
**Rollout/rollback:** samen met wijziging 1; revert van tekstpakket.
**Done when:** AC3/4/5/6/7 pass; C5 registreert exacte commit en bewijsgrenzen.

## Risks

Meer uitleg kan de oefening opnieuw lang maken: houd de complete keten op één
aparte pagina en de eigen stappen kort. Voorbeelden kunnen latere eisen naar voren
halen: controleer uitsluitend requirements 1–5. Een ingevuld oordeel of mensbesluit
kan voor echte toestemming worden aangezien: label voorbeeldstatus en laat de
student zelf besluiten over de eigen uitvoering. Afzonderlijke chatvensters blijven
middel; core is de enige procesnorm.

## Assumptions

De student heeft deel A gedaan en de voorbereiding/les gelezen vóór deze keten.
Codekeuze blijft vrij; controles gebruiken de voorgeschreven CLI-handelingen, geen
nieuwe verplichte taal of framework. Studentwaarnemingen en gemeten duur ontbreken.

## Open questions

Menselijk C4: akkoord met de aparte begeleide pagina na deel A en de gerichte
modulecorrecties hierboven? De bestaande controlebeperking is al besloten.
Dit plan geeft nog geen uitvoerings- of mergetoestemming.
