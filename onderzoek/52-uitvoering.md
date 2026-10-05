# #52: uitvoering en broncontrole

## Besluit en basis

[C4 PROCEED](https://github.com/misja/agent-role-loop/issues/52#issuecomment-5995937482)
registreert het gebruikersantwoord “akkoord” op
[C2 v1](https://github.com/misja/agent-role-loop/issues/52#issuecomment-5995842633),
ook vastgelegd in `52-plan.md`. Dit geeft uitvoering vrij, geen merge.
Norm- en procesbasis: `0765540c53243a328a2b9809770fe2097d4a05fe`.
Orkestrator/planner/bouwer root; één verse reviewer review52, AC1–7.
Herstelstand vóór initial C6: ontwerp 0, oplevering 0.

## Voor en na

| Bevinding uit #46 | Wijziging | Gevolg voor de lezer |
|---|---|---|
| Raamwerk wisselt van uitleenhandeling naar export. | Alle vervolgvoorbeelden gebruiken dezelfde uitleenafspraak; concrete testinvoer, twee pogingen en twee verwachtingen. | Afspraak, automatische controle en beoordeling zijn aan dezelfde wijziging terug te vinden. |
| Mechanismen/themakaart vragen terugzoeken tussen categorieën. | Drie-bijdragetabel naast de handeling; themakaart met woorden en eigen naslagfunctie. | De hoofduitleg vraagt geen eerdere toolkennis; de kaart ondersteunt later de projectkeuze. |
| Principes herhalen grenzen zonder concrete toepassing. | Korte toepassingen op de eis/codeversie/testbewijs en mensbesluit; volledige route blijft core. | Informatie, ontvanger en resterende verantwoordelijkheid zijn herkenbaar. |
| Verder lezen mengt leesadvies, claims en methodeverdediging. | Leesvraag, moment/voorkennis en gebruiksbeperking per bron; Farley ongewijzigd. | De lezer kan kiezen welke bron bij zijn vraag past. |

De eerste drie mechanisme-sectietitels en 'De drie samen' blijven behouden.
De module-2/3-leesaanwijzingen blijven daardoor correct; modules 4–6 vinden
de oordeelslaag, menselijke poort en projectkaart nog op dezelfde pagina.
Geen nieuwe opdracht, gedragsvereiste of ingevulde oefenoplossing toegevoegd.
Het voorbeeld beschrijft verwachte controle, geen nieuw uitgevoerde uitleentest.

## Claimregister: primaire bronnen

Gerichte bronlezing op 5 oktober 2026 via de onderstaande primaire vindplaatsen.
Geen integrale controle van alle geciteerde studies. De productpassages blijven
binnen de hier vastgestelde bronsteun.

### Codex-gebruiksstudie

[Primaire PDF](https://cdn.openai.com/pdf/5d1e1489-21c0-43e4-9d42-f87efdbf0082/the-shift-to-agentic-ai-evidence-from-codex.pdf),
introductie pp. 1–3, conclusie pp. 21–23; titelblad auteurs.

Behouden: beschrijving van gebruik bij drie populaties, delegatie/beoordeling
als leesvraag, OpenAI-herkomst en niet-representatieve interne omgeving.
Geschrapt: kwalificatie 'volwassen', algemene thesebevestiging en inferentie
dat geobserveerde verschillen ons onderwijs rechtvaardigen. Gebruiksdata
valideren deze rollenlus niet. Geen productiviteitscijfers overgenomen.
Bibliografische fout hersteld: titelblad noemt Drew Johnston en Alex Martin
Richmond, niet Scott Johnston/Maxwell Richmond. Citeersleutel/URL behouden.

### Alenezi

[Primaire v1](https://arxiv.org/html/2604.10599v1), secties 2, 4, 5.1, 6.4 en
referentie [14]; [versierecord](https://arxiv.org/abs/2604.10599v1).

Behouden: literatuur/praktijksynthese, voorstellen over vaardigheden en
onderwijs, conceptueel en nog te toetsen raamwerk (§6.4). 'Preprint' beperkt
tot de arXiv-versie; peer review is hier niet vastgesteld. Referentie [14]
bevat `2503.XXXXX`: de waarschuwing wordt concreet, zonder oordeel over alle
referenties. Competentielijst en overeenkomst met onze modules verwijderd.
Versnellings-/beginners-/onderhoudbaarheidsclaims worden niet overgenomen:
de achterliggende studies zijn hier niet onafhankelijk onderzocht. Geen nieuwe
empirische onderwijsclaim; aanbevelingen blijven voorstellen voor discussie.

### Sweller

[Primaire uitgeverspagina en abstract](https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1202_4),
1988, Cognitive Science 12(2), pp. 257–285.

Behouden: probleemoplossen kan kennisopbouw hinderen door de benodigde
verwerkingscapaciteit. Alleen het abstract is inhoudelijk geraadpleegd;
volledige experimenten/hoofdstukken niet onderzocht. Claim dat deze bron
worked examples met fading en het effect van onze didactiek onderbouwt is
verwijderd. Afnemende begeleiding wordt in gewone handelingen uitgelegd en
als eigen ontwerpkeuze begrensd. Geen gemeten leereffect geclaimd.

### Farley: eerder vastgesteld bewijs

De toelichting is bytegelijk. Broncontrole uit `46-uitvoering.md`, sectie
'Primaire broncontrole Farley', hergebruikt voor hoofdstuk 5, Feedback:
[uitgeversinhoudsopgave](https://www.informit.com/store/modern-software-engineering-doing-what-works-to-build-9780137314782).
Geen nieuwe volledige boeklezing of validatie van de AI-werkwijze.
De ruimere Farley-verwijzing in de oude 'De drie samen'-passage is verwijderd;
de inhoudelijke samenhang wordt nu uit de uitleenhandeling zelf verklaard.

## Objectieve controles

- `make -C docs html` gebruikt `-W --keep-going`: build geslaagd, geen
  waarschuwingen; `/tmp/arl52-build.log`. Eerste sandboxpoging kon geen
  uv-cachelock maken; goedgekeurde herhaling slaagde.
- `/tmp/arl52-links.py`: 273 lokale links/fragmenten van gewijzigde
  raamwerk-/literatuurpagina en alle inkomende links daarnaartoe, nul fouten.
  Bibliografie wordt door de gewijzigde auteursnamen geraakt.
- Bytevergelijking met basis: raamwerkbegin tot 'Drie soorten
  kwaliteitsmechanismen' en Farley-toelichting identiek.
- Beschermde diff leeg voor alle modules, praktijk/cases, core/adapters,
  voorbereiding, startpagina en doelgroep/schrijfwijzer/conventies.
- Geen export/orders of em/en-dash in de gewijzigde raamwerkpagina.
  `git diff --check` schoon. C5 pinnt de exacte productcommit.

Geen screenshots: tekstwerk zonder vormgevingswijziging of concreet
weergaveprobleem, volgens de op 4 oktober door de gebruiker bijgestelde
controleafspraak in de gepinde conventiepagina. De oudere AC7-formulering
'visuele lezing' creëert geen nieuwe standaard-screenshotcontrole.

## Bewijsgrenzen en review

Studentwaarnemingen, gemeten begrip/leereffect en haalbaarheid van de moduleduur
zijn niet beschikbaar. Bronlezing en agentlezing zijn geen studentvalidatie.
Geen nieuwe casustests, platformrechten- of providerproef en geen integrale
externe-linkaudit. De primaire broncontrole betreft de genoemde passages.
Initial C6 volgt op de exacte productcommit en toetst alle criteria, inclusief
een zelfstandige leesgang langs de vier bronnen en de benodigde voorkennis.
