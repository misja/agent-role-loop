# #51: eigen proces en praktijkketen navolgbaar maken

## Besluit en normbasis

[C4 PROCEED](https://github.com/misja/agent-role-loop/issues/51#issuecomment-5991925220)
registreert het gebruikersantwoord “akkoord” op C2 v1 in `onderzoek/51-plan.md`.
Het geeft de interne opsplitsing van stap 4/6, het weglatingsvoorbeeld en de
praktijk-/naslagroutes vrij. Geen mergebesluit.

Proces-/normbasis: `9a89825f3de6aa3473e15cd8ec925a0d91b73cad`.
C1/C2 en leesbare bronnen staan in het plan en de
[startregistratie](https://github.com/misja/agent-role-loop/issues/51#issuecomment-5984299004).
Root plant/bouwt; één verse onafhankelijke reviewer `/root/review51` voor AC1–7.
Geen afzonderlijke C3. Herstelstand vóór initial review: ontwerp 0, oplevering 0.

## Voor en na

| Bronbevinding #46 | Uitvoering | Gevolg voor de lezer |
|---|---|---|
| Module6 stap4 bundelt route, planning en C4. | Afzonderlijke C1-, route-, eventuele C3-herstel- en mensbesluitmomenten. | Eigenaar, invoer en te bewaren uitkomst zijn zichtbaar; LIGHT/REJECT blijven onderscheiden. |
| Stap6 bundelt initial review, herstel en merge. | Invoer samenstellen, C6's bewaren, eindoordeel, blokkadepad en mensbesluit apart. | Directe C5/C6/C7-links en herstelbijlage bij de blokkade; menselijk mergebesluit volgt pas op passende uitkomst. |
| Les vraagt weglatingsreden zonder concreet geval. | Kleine in-memory-demonstratie zonder nieuwe dependencies, geen bestaande scanplicht; scan voor nieuwe dependencies kan worden weggelaten. | Expliciete scope/reden plus resterende reviewvragen over invoer, logica-aanroepen en foutmeldingen; geen kwetsbaarheidsvrijheidsclaim of vervallen verplichting. |
| Praktijklinks landen op volledige pagina. | Labels bij bronmapping, sessie-invoer, beginstappen en exporttabel; gerichte verwijzingen vanuit module6 en uitvoerstappen. | Geen zoeken naar de bedoelde tabel of sessie-invoer. |
| Codes/voorbereiding/naslag zijn onvoldoende gesignaleerd. | Codes verklaard bij eerste gebruik, voorbereiding wijst naar bestaande uitleg; verhuizing en historie aparte optionele routes. | Opdracht-/planlabels versus contractcodes en codecommits blijven onderscheiden; naslag is geen verplichte vervolgopdracht. |

De zes hoofdactiviteiten zijn behouden. Binnen stap4/6 zijn de bestaande
verantwoordelijkheden uitgewerkt; geen tweede routingnorm. Core blijft leidend.
Planherstel en opleveringsherstel zijn apart begrensd; initial-contextisolatie,
verse repair-review, eerder vastgestelde dekking en menselijk vervolg blijven.
Het aantal voorbeelden groeit niet tot een tweede volledige module-1-uitvoering.

## S4-keten en bronbegrenzing

Het filtervoorbeeld gebruikt S4: filtering behoudt boeken en uitleenstatus.
De blijvende bronnen staan in de ongewijzigde praktijkbundel:

1. C0-W1 noemt S4 expliciet. C1 kiest PLANNED en wijst S1–S4 toe aan Robin.
2. C2-P1 verbiedt mutatie van de geregistreerde verzameling en koppelt S4 aan
   `test_s4_filter_verandert_geen_toestand`. C4-P1 staat P1 met behoud van
   toevoegvolgorde toe; dit is een fictief besluit in het scenario.
3. Code A overschrijft de interne lijst. C5-A bevat drie geslaagde controles
   voor S1–S3 en meldt dat S4 niet is vastgesteld. C6-A blokkeert met R1/S4.
4. De herstelbijlage bewaart ontwerp0/oplevering1, A..B-diff, R1 en eerdere
   dekking; wegens dezelfde methode worden alle vier criteria op B hercontroleerd.
5. B geeft een aparte lijst terug. C5-B bevat falende regressie op A en vier
   geslaagde controles op B. C6-B geeft SHIP; M1 beschrijft de fictieve menselijke
   merge. De echte agentrun en echte menselijke goedkeuring zijn niet beschikbaar.

A/B zijn bestandslabels, geen echte bouwcommits. De code en controle-uitvoer
zijn reproduceerbaar, maar vormen geen complete test-first-historie of echte
project-PR. P1/P2 en normen in de bundel behouden hun bestaande versies;
het groene B-oordeel geldt niet voor de nog niet vrijgegeven sorteervraag P2.
De student moet in eigen werk werkelijke code-/basiscommits, normversies en
menselijke besluitbronnen bewaren. Reviewer volgt deze keten zelfstandig voor AC4.

## Objectief bewijs vóór onafhankelijke review

Verificatie: manual-with-expected-results voor tekst-/criteriumgang;
validation-workflow voor bestaande controles, beschermde vergelijkingen, build
 en links. Geen nieuw codegedrag; geen nieuwe repositorytests of kunstmatige
voorwijzigingsfout voor proza. Voor/na in dit register is geen begripmeting.

Op 5 oktober 2026 is de ongewijzigde zipbundel uitgepakt in een tijdelijke map.
Commando's via `/tmp/arl51-verify.py`, volledige uitvoer
`/tmp/arl51-evidence.json`. Linux, Python 3.14.8, standaardbibliotheek.

| Invoer/actie | Verwachting | Waarneming |
|---|---|---|
| python3 controleer.py a zwak | Drie pass, exit0; S4 ontbreekt. | Drie pass, OK, exit0. |
| python3 controleer.py a regressie | Eén fail, exit1; boek2 verdwijnt. | S4 fail, exit1; tuple (2, Atlas, Noor) ontbreekt na filtering. |
| python3 controleer.py b volledig | Vier pass, exit0. | S1 tot en met S4 pass, OK, exit0. |

Beschermde vergelijking tegen basis:
- Alle drie basiskeuzen en het volledige dossiergedeelte van module6 zijn
  bytegelijk; geen punt of taak toegevoegd/verwijderd.
- Module6 organizer/leeruitkomsten en vaste lesstaart bytegelijk.
- Casusbestanden, zipbundel, core/adapters, voorbereiding en modules1–5 diff leeg.
- Geen em/en-dash in gewijzigde module6/praktijkteksten; diffcontrole schoon.

`make -C docs html` gebruikt -W --keep-going en slaagt zonder waarschuwingen:
`/tmp/arl51-build.log`. De eerste sandboxpoging blokkeerde uv-cachetoegang;
de goedgekeurde herhaling slaagde. `/tmp/arl51-links.py` controleert links van
gewijzigde pagina's én inkomende links naar die pagina's: 569 lokale
HTML-links/fragmenten, nul fouten. C5 pinnt de exacte productcommit.
Geen screenshots: geen vormgevingswijziging of concreet weergaveprobleem.

## Behouden afhankelijkheid en bewijsgrenzen

De manual adapter adviseert nog de teaching introduction plus module2 als
voorbereiding. De oriënterende introductie bevat niet langer alle agentuitleg.
Het praktijkhoofdstuk verwijst daarom zelf naar `van-chat-naar-agent.md` en de
benodigde secties over uitvoering, rol en overdracht. De adapter blijft buiten
C0-scope; zijn oudere leesadvies is een bekende bronbeperking. Het hoofdstuk
heeft daarmee een vindbare eigen voorbereiding zonder adapterwijziging.

Andere providerarchitectuur, live interface, volledige studentcode-review,
werkelijke GitHub-/Codeberg-verhuizing en accountrechten zijn niet uitgevoerd.
Bestaande platform-/historieverwijzingen zijn behouden; geen nieuwe platformclaim
of integrale externe linkaudit. De korte naslaglabels veranderen die bronnen niet.
De weglatingskeuze geldt alleen onder de genoemde scope/normvoorwaarden, niet
voor elke Textual-uitbreiding of aanwezige dependencyset.

Studentwaarnemingen, gemeten leereffect en haalbaarheid van vier uur zijn niet
beschikbaar. Uitvoerbare bundelcontrole is geen echte agentrun of mensbesluit.
Een dossiergang door een agent is agentlezing, geen studentvalidatie.

## Onafhankelijke C6 en overdracht naar de mens

[/root/review51: C6 SHIP](https://github.com/misja/agent-role-loop/issues/51#issuecomment-5992265942)
beoordeelt productcommit `2b22c4d1cf96ed22d4f5ab0fa43ad0b0196a9aac`.
Alle AC1–7 pass; geen blockers, nits of contract drift. De reviewer volgde S4
zelfstandig van criterium tot het fictieve mensbesluit en voerde de falende
A-regressie en vier geslaagde B-controles uit. Ook de 569 lokale links,
beschermde bytevergelijkingen en PLANNED-leesgang met LIGHT/REJECT-afwijkingen
zijn zelfstandig gecontroleerd. De build is ingezien auteursbewijs, geen door
de reviewer herhaalde build. De hiervoor genoemde bewijsgrenzen blijven gelden.

Herstelstand na C6: ontwerp 0, oplevering 0. Deze registratie wijzigt het
beoordeelde onderwijsmateriaal niet. [PR #56](https://github.com/misja/agent-role-loop/pull/56)
is gereed voor het afzonderlijke menselijke mergebesluit. GitHub rapporteert
geen CI-checks voor deze PR; lokale build- en controlebewijzen staan hierboven.
