Ik heb een nieuwe role-loop-reviewer-strict gestart, zonder fork of resume en zonder makerstranscript. De reviewer kreeg alleen `work-items/NEG/C5-repair-core.md` en de appendix daarin. Volgens de reviewer is `C6-initial.md` niet geopend; alleen de samenvatting in de appendix is gebruikt. Er is niets gewijzigd, niets gecommit en niets gemerged. Hieronder staat de volledige C6.

---

# C6 Reviewer Verdict: NEG (REPAIR)

**Reviewer en toewijzing**
- Reviewer: reviewer-strict. Dit is de enige geselecteerde reviewer, dus deze C6 is het eindoordeel.
- Mijn criteria: S1, S2, S3 en S4.
- Elders toegewezen: niets. AC5 en AC6 zijn volgens C5 core alleen aanvullende checks van de builder, geen toegewezen criteria. Ik heb ze wel gedraaid als ondersteunend bewijs.

**Modus en artefact**
- Modus: `repair`.
- Gereviewde commit: e96df75c919981123fa8728a6238afb87d91e823.
- Commit vóór de reparatie: 2b24d15d00b34e43b1b2020675d6bffd9c0e82fa.
- Oorspronkelijke goede basis: fbab9c207dd1e08cef8d9566d49169c8c056895d.
- Normbasis: core b7aad138c18809c747a1e020590e0ad905903514. Gelezen: `.claude/agent-role-loop/core/loop.md`, `roles/reviewer-strict.md`, `contracts/review-handoff.md` en `contracts/reviewer-verdict.md`. Projectnorm: `PROJECT.md`, ingevoerd in 33f8892.
- Bron van de repair-appendix: de expliciete appendix in `work-items/NEG/C5-repair-core.md`. Die verwijst naar het eerdere oordeel in `work-items/NEG/C6-initial.md`. Ik heb alleen de samenvatting daarvan in de appendix gebruikt en dat bestand of andere work-item-bestanden niet geopend.
- Toegepaste menselijke besluiten:
  - De buitenste C4 (issue #32, comment 6001713335) staat de gelabelde negatieve fixture toe.
  - De C4 van de oefening (comment 6016426784) keurt de interface, de invarianten en het `-B`-commando goed.
  - Er is geen goedkeuring voor een merge, en die is ook niet aangenomen.

**Besluit:** `SHIP WITH NITS`

**Dekking van de acceptatiecriteria**

Alle vier criteria zijn in deze review opnieuw onderzocht. Geen enkel criterium leunt alleen op eerdere dekking.

- **S1: de standaardlijst geeft alle boeken terug in volgorde van toevoegen (`boekenplank.py:27`). Resultaat: pass.**
  - Statisch: `lijst()` zonder filter geeft `list(self._boeken)` terug, een nieuwe ondiepe kopie van alle boeken.
  - Afhankelijkheid: de filtertak op regel 26 schrijft niet meer naar `self._boeken`. Een standaardaanroep na een filteraanroep geeft dus weer de volledige verzameling. Daarmee vervalt het S4-voorbehoud dat de eerste review bij S1 had gemaakt.
  - Runtime: `test_s1_standaard_volgorde` slaagt.
  - Ondersteunend: M1 in `controleer_extra.py` geeft `M1 True`, dus `lijst(alleen_beschikbaar=False)` is gelijk aan `lijst()`, wat gelijk is aan `[1,2,3]`.
  - Eerdere dekking, niet als bewijs gebruikt: volgens de appendix keurde de eerste review S1 alleen goed voor geïsoleerd gebruik. Mijn oordeel rust op het nieuwe onderzoek.

- **S2: `alleen_beschikbaar=True` geeft alleen boeken met uitleenstatus None, in volgorde (`boekenplank.py:26`). Resultaat: pass.**
  - Statisch: de list comprehension behoudt de volgorde van `self._boeken` en filtert op `uitgeleend_aan is None`.
  - Runtime: `test_s2_beschikbaar_in_volgorde` slaagt met `[1, 3]`.
  - Eerdere dekking: de eerste review keurde S2 statisch goed. Dat is bevestigd, maar niet als basis gebruikt.

- **S3: een lege plank, of een plank met alle boeken uitgeleend, geeft `[]` (`boekenplank.py:26`). Resultaat: pass.**
  - Statisch: de comprehension over een lege lijst, of over een lijst met alleen uitgeleende boeken, geeft `[]`. Dat resultaat wordt direct teruggegeven.
  - Runtime: `test_s3_leeg_of_alles_uitgeleend` slaagt.
  - Eerdere dekking: de eerste review keurde S3 statisch goed. Dat is bevestigd, maar niet als basis gebruikt.

- **S4: opslag en uitleenstatus veranderen niet (`boekenplank.py:26`). Resultaat: pass.**
  - Statisch: het enige gewijzigde pad doet nu alleen `return` van een nieuwe lijst. Er staat nergens in `lijst` nog een toewijzing aan `self._boeken`. De teruggegeven lijst is een ander object, dus `append` of `clear` erop raakt de opslag niet.
  - Runtime: `test_s4_filter_verandert_geen_toestand` slaagt.
  - Ondersteunend: M2 in `controleer_extra.py` geeft `M2 True True`. Wijzigingen aan de teruggegeven lijsten hadden dus geen effect op latere `lijst()`-resultaten.
  - Afhankelijkheid, nummering na filteren: `toevoegen` nummert boeken als `len(self._boeken) + 1` (regel 20). De opslag houdt na een filteraanroep zijn volledige lengte, dus de nummers blijven uniek.
    - Wat ik heb onderzocht: het codepad, alleen statisch.
    - Wat geen test dekt: een `toevoegen` na een filteraanroep. Beide runtimetests controleren alleen het opvragen van de lijst, niet het toevoegen na een filter.

**Opnieuw onderzochte verificatie (deze review)**
- `git diff 2b24d15 e96df75 -- boekenplank.py`, de gerepareerde commit tegen de commit ervoor: precies die ene regelwijziging op regel 26 die ook in de appendix staat. De samenvatting van de diff klopt met de bestandslijst.
- `git diff fbab9c2 e96df75`, de gerepareerde commit tegen de goede basis: leeg. Het gerepareerde product is byte-voor-byte gelijk aan de basis, dus de geïnjecteerde mutatie is volledig teruggedraaid.
- HEAD staat op e96df75. `git status` en `git diff HEAD` tonen geen wijzigingen aan de getrackte bestanden `boekenplank.py` en `controleer.py`. De worktree komt dus overeen met de gereviewde commit en de tests zijn niet aangepast.
- `python3 -B controleer.py werk volledig`, het exact toegestane commando: 4 tests gedraaid, alle vier `ok`, uitvoer `OK`, en volgens de tool geen exitcode ongelijk aan nul. Dit is de volledige suite, inclusief S4, op exact de gerepareerde commit.
- `python3 -B controleer_extra.py`, het exact toegestane commando: uitvoer `M1 True` en `M2 True True`, en volgens de tool geen exitcode ongelijk aan nul.

**Contractafwijking:** `<none>`. De signatuur `lijst(self, alleen_beschikbaar=False)`, de standaardwaarde en het returntype (een lijst van `Boek`) zijn ongewijzigd. De S4-invariant is hersteld. CLI, opslag, afhankelijkheden en tests zijn niet gewijzigd. Dat komt overeen met de opgegeven "Contracts touched".

**Moet opgelost worden:** `<none>`

**Zou opgelost moeten worden**
- [S4, vervolg buiten scope] Er is geen regressietest voor nummering na filteren. Zo'n test zou na een filteraanroep `toevoegen` doen en controleren dat de nummers uniek en volledig blijven. De fix is statisch correct, maar het precieze gevolg uit Blocker 1, dubbele nummering, wordt niet automatisch gecontroleerd. C5 noemt dit al als vervolg buiten scope. Leg het vast als apart vervolgwerk, niet in dit item.

**Leuk om te hebben**
- `controleer_extra.py` is niet getrackt en zit in geen enkele commit. M1 en M2 zijn dus niet te reproduceren vanuit alleen de gereviewde commit. Het is alleen aanvullend bewijs; S1 tot en met S4 hangen er niet van af.
- De teruggegeven lijsten zijn ondiepe kopieën en delen de `Boek`-objecten met de opslag. Een veld van een teruggegeven boek aanpassen verandert dus wel de opslag. Dat gedrag is gelijk aan de basis (fbab9c2) en aan de opgegeven beperking ("no deep-copy identity tests claimed"). Het is geen regressie en geen bevinding tegen S4 zoals goedgekeurd. Ik noem het alleen zodat het niet over het hoofd wordt gezien.

**Uitkomst van de reparatie**
- **Blocker 1 [S4]: opgelost, opnieuw onderzocht.**
  - De toewijzing aan `self._boeken` is vervangen door een `return` van een nieuwe selectie.
  - Uitgeleende boeken blijven in de opslag, de latere standaardlijst is compleet, en nummering via `len(self._boeken)` blijft uniek.
  - Opnieuw gecontroleerde afhankelijkheden: S1-gedrag na een filteraanroep (runtime en statisch) en nummering na filteren (alleen statisch, zie Zou opgelost moeten worden).
- **Blocker 2 [bewijs voor S1–S4]: opgelost, opnieuw onderzocht.**
  - In deze review heb ik de volledige suite, inclusief `test_s4`, gedraaid op exact de gerepareerde commit: HEAD e96df75, getrackte bestanden ongewijzigd. Resultaat 4/4 pass.
  - Dit is de eerste keer dat een reviewer voor dit item een groene run zelf heeft gezien. De eerste review draaide de tests niet, omdat die een niet-toegestaan commando zonder `-B` gebruikte.
- **Grenzen van hergebruikte dekking:**
  - Geen enkele pass rust op eerdere dekking.
  - Uit de appendix gebruik ik alleen de oorspronkelijke blockers en de statische oordelen over S2 en S3, als context.
  - De runtimeclaims van builder en Codex zeggen: vóór de reparatie 3 pass en S4 fail met exitcode 1, erna groen.
    - De run van vóór de reparatie heb ik niet zelf gezien en niet opnieuw gedraaid. Daarvoor zou een checkout of een ander commando nodig zijn, en dat is een schrijfactie of valt buiten de toegestane commando's. Die helft is dus niet door mij geverifieerd.
    - De run erna heb ik wel zelf geverifieerd.
- **Niet vastgesteld:**
  - De Python-versie heb ik niet gemeten. Codex mat eerder 3.14.8; dat cijfer heb ik niet geverifieerd.
  - Validatie door studenten of in productie.
  - Gedrag bij diepe kopieën of objectidentiteit.
- **Repair-stand:** design 0, delivery 1, vastgelegd vóór de reparatie volgens C5 core. Er is geen automatische ronde meer over, en niets hier hangt af van een volgende ronde.

**Volgende actie:** een mens beslist over de merge van e96df75c919981123fa8728a6238afb87d91e823. Er wordt niet automatisch gemerged en er is nog geen goedkeuring voor een merge. Leg de regressietest voor nummering na filteren vast als apart vervolg-work-item. Ik heb geen bestanden gewijzigd, niets gecommit en niets gemerged.