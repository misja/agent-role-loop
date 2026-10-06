Er draaide één nieuwe `role-loop-reviewer-strict` (geen fork of resume). De uitkomst is **SHIP WITH NITS** met een gereviewde commit `fbab9c2`. Er is één reviewer geselecteerd, dus deze C6 is het eindoordeel; er komt geen C7.

De reviewer kreeg alleen `work-items/W1/C5-core.md`, het daarin genoemde `C4.md`, `PROJECT.md` op basiscommit `33f8892`, de geïnstalleerde core (`b7aad13`) en de commit via `git show`. Hij kreeg geen C1, C2, `input.md`, logs, transcripten of andere oordelen. Toegestaan waren alleen de twee goedgekeurde testcommando's. Ik heb niets gewijzigd en geen Git-, tracker- of merge-acties uitgevoerd. Deze C6 is niet weggeschreven; sla hem zelf op als bijvoorbeeld `work-items/W1/C6.md`.

---

**C6 Reviewer Verdict: W1**

**Reviewer en toewijzing**
- Strikte onafhankelijke reviewer, de enige die geselecteerd is.
- Toegewezen criteria: alle zes (S1, S2, S3, S4, AC5, AC6). Niets is elders toegewezen.

**Mode en artefact**
- Mode: `initial`, zonder repair-bijlage.
- Gereviewde commit: `fbab9c207dd1e08cef8d9566d49169c8c056895d`. Basis: `33f88927165475fc2e6f8c513ef6f76741569969`.
- Procesnorm: de geïnstalleerde `.claude/agent-role-loop/core/` (gepind op `b7aad138…`), namelijk `loop.md`, `roles/reviewer-strict.md`, `contracts/reviewer-verdict.md` en `contracts/review-handoff.md`.
- Projectnorm: `PROJECT.md` op de basiscommit.
- Menselijk besluit: `work-items/W1/C4.md` (PROCEED, V1–V4, geen merge-goedkeuring).

**Besluit:** `SHIP WITH NITS`

**Dekking van de acceptatiecriteria** (alles nieuw onderzocht)

De wijziging: alleen `boekenplank.py` verandert (+3/−1).
```python
def lijst(self, alleen_beschikbaar=False):
    if alleen_beschikbaar:
        return [b for b in self._boeken if b.uitgeleend_aan is None]
    return list(self._boeken)
```

- **Werkboom gelijk aan de commit:** `git diff fbab9c2 -- boekenplank.py controleer.py` is leeg. `controleer.py` zit niet in de bestandslijst van de commit.
- **Testruns:**
  - `python3 -B controleer.py werk volledig`: 4 tests, alle OK.
  - `python3 -B controleer_extra.py`: `M1 True` en `M2 True True`.

| ID | Uitkomst | Bewijs |
|---|---|---|
| S1 | pass | `list(self._boeken)` geeft alle boeken in toevoegvolgorde terug. `test_s1_standaard_volgorde` slaagt (`[1,2,3]`). |
| S2 | pass | Het filter test `uitgeleend_aan is None` en houdt de volgorde aan. `test_s2_beschikbaar_in_volgorde` slaagt (`[1,3]`). |
| S3 | pass | `test_s3_leeg_of_alles_uitgeleend` slaagt: een lege plank en een volledig uitgeleende plank geven allebei `[]`. |
| S4 | pass | De code leest alleen en muteert niets. `test_s4_filter_verandert_geen_toestand` slaagt. Grens: de test vergelijkt waarden, geen objectidentiteit. Volgens code-inspectie blijft de identiteit wel behouden. |
| AC5 | pass | Een expliciete `False` volgt dezelfde tak als de default. Check M1 bevestigt dat beide `[1,2,3]` geven. |
| AC6 | pass | Beide takken leveren een nieuwe lijst op. Check M2 muteert de teruggegeven lijsten, en de opslag blijft daarna `[1,2]` en `[1]`. Grens: de `Boek`-elementen worden gedeeld, maar AC6 vraagt alleen om onafhankelijke containers. |

**Contractafwijking:** `<none>`
- De enige publieke wijziging is de optionele parameter. Die is goedgekeurd met C4 V3.
- Er zijn geen opslag, CLI of dependencies toegevoegd, en er zijn geen andere bestanden gewijzigd.
- Het gebruik van `-B` is goedgekeurd met C4 V2.

**Must fix:** `<none>`

**Should fix**
- Het bewijs voor AC5 en AC6 staat alleen in het ongetrackte `controleer_extra.py`. Na W1 beschermt dus niets in de repo deze criteria tegen regressie. Omdat C4 V1 `controleer.py` ongewijzigd houdt, moet jij hierover beslissen. Dit is een vervolgpunt, geen reparatie.

**Nice to have**
- `if alleen_beschikbaar:` test op truthiness, dus ook een waarde als `"nee"` zet het filter aan. Voor een gewone optionele parameter (C4 V3) is dat acceptabel.
- C5 core heeft geen apart veld "Contracts touched". De inhoud volgt wel uit "Change" en "No other product change".

**Grenzen van deze review**
- Eén extra `python3 -B -c`-controle van de reviewer werd door de permissies geweigerd en is niet omzeild. Het bewijs bestaat dus uit de twee goedgekeurde commando's, `git show`/`git diff` en het lezen van de code.
- De reviewer heeft alleen de resultaten ná de wijziging gecontroleerd. De builder meldt vóór de wijziging 1 pass en 3 TypeErrors; dat is niet opnieuw nagelopen, maar overgenomen uit C5. Het past wel bij de basiscode, waar `lijst(self)` nog geen parameter had.
- Er is niets in productie gevalideerd en niets door studenten gevalideerd. De Python-versie is overgenomen uit C5 en niet zelf gecontroleerd.

**Reparatie-uitkomst:** `<none>` (initial mode). Tellers: ontwerp 0, oplevering 0.

**Volgende stap:** jouw merge-besluit; er is nog geen merge-goedkeuring. Neem het should-fix-punt over de niet-gecommitte AC5/AC6-checks op als vervolgwerk.