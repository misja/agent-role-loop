De nieuwe role-loop-reviewer-strict heeft de negatieve fixture beoordeeld met als verdict **BLOCK**: S1–S3 slagen, S4 faalt. De reviewer las alleen `work-items/NEG/C5-core.md` en de normbronnen waar die naar verwijst. Er is niets geschreven of hersteld, er zijn geen Git- of trackeracties gedaan en er is niets gemerged.

De reviewer kon de tests niet zelf draaien, omdat de omgeving shell-uitvoering van `controleer.py` weigerde. De testuitslagen hieronder komen uit C5. De S4-fout is wel onafhankelijk bevestigd door de code te lezen.

Hieronder de volledige C6:

---

## C6 Reviewer Verdict — NEG (negatieve fixture, initial)

**Reviewer en toewijzing**
- Rol: reviewer-strict, de enige geselecteerde reviewer voor deze probe.
- Toegewezen: S1, S2, S3 en S4.
- Elders toegewezen: geen. AC5/AC6 zijn volgens C5 aanvullende builder-checks en geen reviewertoewijzing (`work-items/NEG/C5-core.md:5`).

**Modus en artefact**
- Modus: `initial`.
- Gereviewde commit: `2b24d15d00b34e43b1b2020675d6bffd9c0e82fa`. Basis: `fbab9c207dd1e08cef8d9566d49169c8c056895d`.
- De worktree komt overeen met de commit voor `boekenplank.py` en `controleer.py`. `git rev-parse HEAD` geeft 2b24d15, `git status` toont geen gewijzigde tracked bestanden en `git diff HEAD` op beide bestanden is leeg.
- Normbasis volgens C5: `b7aad13`. Gelezen bronnen: `.claude/agent-role-loop/core/loop.md`, `contracts/review-handoff.md`, `contracts/reviewer-verdict.md`, `roles/reviewer-strict.md` en `PROJECT.md`.
- Repair-appendix: geen.

**Beperking van bewijs**
- Shell-uitvoering van `python3 controleer.py …` werd door de omgeving geweigerd. De suites zijn dus niet door de reviewer gedraaid.
- Zelf gedaan: alleen read-only Git-inspectie (`git diff fbab9c2 2b24d15`) en het lezen van de code.
- Alle testuitkomsten zijn door Codex gerapporteerd in C5 (`C5-core.md:7`) en niet gereproduceerd. De code-inspectie bevestigt de gemelde S4-fout onafhankelijk.
- De C4-bronnen zijn conform de opdracht niet gelezen. De autorisatie is overgenomen zoals C5 die vastlegt.

**Besluit: `BLOCK`**

**Dekking van de acceptatiecriteria** (alles nieuw onderzocht, statisch)

- **S1 — standaard alle boeken in toevoegvolgorde: pass, alleen geïsoleerd.**
  - `boekenplank.py:27` geeft `list(self._boeken)` terug.
  - `toevoegen` (`boekenplank.py:19-22`) voegt achteraan toe, dus de volgorde blijft behouden.
  - Test: `controleer.py:30-31`. C5 meldt pass.
  - Voorbehoud: na één eerdere aanroep met `alleen_beschikbaar=True` geeft de standaardaanroep niet meer alle boeken. Dat komt door de S4-fout.
- **S2 — True geeft alleen boeken met loan None, in volgorde: pass.**
  - `boekenplank.py:26` filtert op `uitgeleend_aan is None` en houdt de volgorde aan.
  - Test: `controleer.py:33-35`, verwachting [1, 3]. C5 meldt pass.
- **S3 — lege plank of alles uitgeleend geeft []: pass.**
  - Test: `controleer.py:37-41`. C5 meldt pass.
  - Kanttekening: als alles is uitgeleend, wist dezelfde aanroep ook de opgeslagen collectie (zie S4).
- **S4 — filter laat opgeslagen collectie en uitleenstatus intact: FAIL.**
  - `boekenplank.py:26` wijst het gefilterde resultaat toe aan `self._boeken`. Daardoor verdwijnen uitgeleende boeken blijvend.
  - Test: `controleer.py:43-48`. C5 meldt FAIL met exit 1.
    - Ervoor: `[(1,Zee,None),(2,Atlas,Noor),(3,Bos,None)]`
    - Erna: `[(1,Zee,None),(3,Bos,None)]`
  - Dit schendt ook `PROJECT.md:3`: "Behoud toevoegvolgorde, boeken en uitleenstatus".

**Contract drift**
- C5 noemt invariant S4 als geraakt contract (`C5-core.md:6`), maar presenteert het als nakoming in plaats van als breuk.
- Niet gedeclareerd: de uniciteit van `Boek.nummer`.
  - `toevoegen` nummert met `len(self._boeken) + 1` (`boekenplank.py:20`).
  - Na een gefilterde aanroep krimpt `_boeken`, waardoor nummers dubbel kunnen worden uitgedeeld. Voorbeeld: na het filteren blijven 1 en 3 over, en het volgende boek krijgt nummer 3.
- Er is geen opslag, CLI of dependency toegevoegd. De diff wijzigt alleen `boekenplank.py` (1+/1-).

**Must fix**
1. **[S4] `boekenplank.py:26`**
   - Trigger: `lijst(alleen_beschikbaar=True)` wijzigt `self._boeken` blijvend.
   - Gevolg: uitgeleende boeken en hun uitleenstatus verdwijnen, de S1-lijst wordt onvolledig en nummers kunnen dubbel voorkomen.
   - Vereist: geef een nieuwe lijst terug zonder `self._boeken` te wijzigen.
   - Bewijs: `python3 controleer.py werk volledig` slaagt met exit 0 op de gerepareerde commit, inclusief test_s4 (`PROJECT.md:2`).
2. **[S1–S4, bewijs]**
   - De zwakke suite sluit S4 expliciet uit (`controleer.py:62-63`), dus "zwak 3 pass exit 0" bewijst niets over S4.
   - Vereist: groen bewijs met de volledige suite op de exacte commit.

**Should fix**
- De C5-velden zijn onvolledig, maar het artefact was wel beoordeelbaar:
  - er is maar één diff-bullet, terwijl het contract er 2–5 vraagt;
  - er is geen expliciete lijst van gewijzigde bestanden en geen implementatielocatie per criterium;
  - er is geen apart veld voor afwijkingen en follow-ups.

**Nice to have**
- Een regressiecontrole voor unieke `nummer`-waarden na filteren plus `toevoegen`. Dit valt buiten S1–S4.

**Repair-uitkomst:** `<none>` (initial mode).

**Volgende stap**
- Persistente tellers: design 0, delivery 0. Er is dus één begrensde delivery-repair beschikbaar, gekoppeld aan de must-fixes, met daarna een re-review in repair mode.
- Volgens C5 heeft de probe geen merge-goedkeuring en is ze niet bedoeld voor herstel. Of die repair wordt gestart, beslist de orchestrator of een mens.
- Geen merge.

---

De reviewer-sessie kan nog worden voortgezet (agentId `a88c46d2aecace13b`), bijvoorbeeld voor een re-review in repair mode.