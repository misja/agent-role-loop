# Build Packet: agent-role-loop

> **Status:** v2 - Gate Decision: PROCEED (Misja, 2026-06-12); build gestart
> **Planner:** Claude (webinterface-sessie, juni 2026)
> **Builder:** Claude Code, in een lege repository
> **Bronnen:** Watkins, "Context isolation in coding agent loops" (depot.dev, mei 2026); bijbehorende gist met rolprompts; Anthropic, "How we built our multi-agent research system" (2025)

## Summary

We bouwen een repository `agent-role-loop` met daarin (1) een tool- en modelagnostische kern van rolprompts en handoff-contracten voor een multi-agent engineering-workflow, (2) adapters voor specifieke platforms, en (3) Sphinx/MyST-onderwijsmateriaal dat hetzelfde principe didactisch ontsluit voor HBO-ICT-studenten Software Engineering.

De kernworkflow:

```
Werkitem -> Triage -> Planner -> Clarifier -> Human Gate -> Builder -> Reviewers (parallel) -> Reviewer Boss
```

Ten opzichte van de oorspronkelijke /orc-loop zijn drie generalisaties doorgevoerd: een triage-stap vooraf (proportionaliteit van gereedschap), een geparametriseerd verificatiemodel (TDD is één invulling, niet dé invulling), en input geabstraheerd van "Linear ticket" naar "werkitem".

## Goals

1. Een herbruikbare, platformonafhankelijke definitie van de rollenloop, bruikbaar voor Misja's eigen softwareprojecten.
2. Handoff-contracten als stabiele interface, gescheiden van rolprompts (implementatie).
3. Minimaal drie adapters: Claude Code, handmatig (losse chats), en OpenAI-compatible API (lokale modellen via vLLM e.d.).
4. Een Sphinx/MyST-publicatiestructuur voor lessen, oefeningen en cases, publicabel als statische site.
5. Een eerste, werkende didactische eenheid: de oefening "ervaar context rot" plus één lesoutline, zodat de onderwijslaag niet leeg start.

## Non-goals

- Geen orchestratie-software of CLI-tool schrijven. De loop wordt gedragen door bestaande agents (Claude Code) of door de mens (manual adapter). Automatisering kan later.
- Geen volledige cursus. We leggen de structuur en één eenheid neer; de rest is vervolgwerk.
- Geen koppeling met Linear, Jira of GitHub Issues. Werkitems zijn platte Markdown.
- Geen evaluatie-infrastructuur (rubrics, toetsing) in deze fase, wel als placeholder benoemd.
- Geen aanpassing van de loop voor "extra large" featurewerk; we documenteren de beperking (sweet spot: S/M/L-taken), conform de bronartikelen.

## Current state

Er bestaat alleen de externe gist met zes rolprompts (planner, clarifier, human-gate, builder, reviewers, reviewer-boss) in het Engels, met Linear/TDD-aannames en zonder licentie-expliciete herbruikbaarheid voor onderwijs. Er is nog geen repository.

## Proposed approach

### Ontwerpbeslissingen (met rationale)

| # | Beslissing | Rationale |
|---|---|---|
| D1 | `core/` verwijst nergens naar een specifiek model, platform of dienst | Toekomstbestendigheid; onderwijs kan andere modellen/diensten gebruiken |
| D2 | Contracten zijn de stabiele interface, rolprompts zijn implementatie | Informatiehiding op procesniveau; prompts mogen evolueren zolang contracten staan |
| D3 | Rolprompts en contracten in het **Engels**, onderwijsmateriaal in het **Nederlands** | Prompts presteren consistent in het Engels en zijn internationaal herbruikbaar; doelgroep van het lesmateriaal is Nederlandstalig. Begrippenlijst (EN -> NL) in de teaching-laag overbrugt dit |
| D4 | Sphinx met MyST-parser, alles in Markdown | Geen reStructuredText nodig; Markdown is het gewenste bronformaat |
| D5 | Triage-stap toegevoegd vóór de Planner | Proportionaliteit: typo's verdienen geen council; tevens zelf een leerdoel |
| D6 | Verificatiemodel geparametriseerd per projecttype | TDD (red/green/refactor) als default, maar met expliciete alternatieven (validatieworkflow, handmatige checks met verwacht resultaat) voor data-, infra- en prototypewerk |
| D7 | Didactische volgorde: probleem -> principe -> tooling | Studenten ervaren eerst context rot in één lange chat, krijgen dan het principe, dan pas de tooling; voorkomt dat het een tool-tutorial wordt |
| D8 | Reviewers draaien parallel en contextvrij van elkaar; bouwen draait sequentieel | Conform Anthropic-bevinding: parallellisatie loont alleen bij echt onafhankelijke deeltaken. Review is dat, bouwen meestal niet |
| D9 | Nederlandse teksten gebruiken spatie-koppelteken-spatie ( - ), nooit em- of en-dash | Huisstijlconventie |
| D10 | Licentie: **CC BY-NC-SA 4.0** voor de gehele repository | Beslissing Misja. Kanttekening: CC-licenties zijn formeel niet bedoeld voor software, maar deze repo bestaat vrijwel volledig uit proza (prompts, contracten, lesmateriaal); de enkele JSON-payloads en configbestanden vallen er pragmatisch onder |
| D11 | Hosting op GitHub, publicatie via GitHub Pages; deploy-mechaniek bewust simpel en draagbaar houden | Mogelijke latere migratie naar Codeberg (Codeberg Pages werkt met een statische branch i.p.v. Actions); de Sphinx-build zelf blijft daarom platformonafhankelijk, alleen de deploy-stap is GitHub-specifiek |

### Repostructuur

```
agent-role-loop/
├── README.md                      # wat, waarom, snelstart, credits naar bronnen
├── LICENSE                        # CC BY-NC-SA 4.0 (D10)
├── .github/
│   └── workflows/
│       └── docs.yml               # Sphinx-build + deploy naar GitHub Pages (D11)
├── core/
│   ├── principles.md              # context-isolatie, expliciete handoffs,
│   │                              # proportionaliteit, human-in-the-loop
│   ├── loop.md                    # de pipeline, stadia, beslispunten, S/M/L-scope
│   ├── contracts/
│   │   ├── work-item.md           # C0: input van de loop
│   │   ├── triage-decision.md     # C1
│   │   ├── build-packet.md        # C2
│   │   ├── clarifier-result.md    # C3
│   │   ├── gate-decision.md       # C4
│   │   ├── review-handoff.md      # C5 (core + extended)
│   │   ├── reviewer-verdict.md    # C6
│   │   └── final-verdict.md       # C7
│   └── roles/
│       ├── triage.md
│       ├── planner.md
│       ├── clarifier.md
│       ├── human-gate.md          # rolbeschrijving voor de MENS, geen agentprompt
│       ├── builder.md
│       ├── reviewer-strict.md
│       ├── reviewer-pragmatic.md
│       ├── reviewer-adversarial.md
│       ├── reviewer-maintainability.md
│       └── reviewer-boss.md
├── adapters/
│   ├── claude-code/
│   │   ├── README.md              # installatie-instructie
│   │   ├── agents/                # subagent-definities die core/roles inladen
│   │   └── commands/orc.md        # slash command als orchestrator
│   ├── manual/
│   │   ├── README.md              # de "zes losse chatvensters"-procedure
│   │   └── handoff-log-template.md
│   └── openai-compatible/
│       ├── README.md              # gebruik met lokale modellen (vLLM e.d.)
│       └── examples/              # voorbeeld-payloads per rol (system + user)
├── teaching/                      # Sphinx-bron (MyST Markdown)
│   ├── index.md
│   ├── begrippen.md               # EN -> NL begrippenlijst
│   ├── lessen/
│   │   └── les1-context-rot.md    # outline + leerdoelen
│   ├── oefeningen/
│   │   └── oefening1-ervaar-context-rot.md
│   ├── cases/
│   │   └── .gitkeep
│   └── _toetsing/                 # placeholder, expliciet leeg in deze fase
├── docs/
│   ├── conf.py                    # Sphinx + myst_parser, html_theme
│   └── Makefile
└── .gitignore
```

### Contractdefinities (kern van het ontwerp)

Elk contract krijgt een eigen bestand met drie secties: **Purpose** (één alinea), **Schema** (verplichte en optionele velden), **Example** (ingevuld minivoorbeeld). De schema's hieronder zijn normatief voor de builder.

**C0 Work Item** - title, context, desired outcome, acceptance criteria (optioneel, mag de planner afleiden), constraints, size guess (S/M/L/XS/XL).

**C1 Triage Decision** - `FULL_LOOP` / `LIGHT` (direct naar builder met minimaal packet) / `REJECT` (te groot of te klein voor de loop, met advies). Plus reden in maximaal drie zinnen.

**C2 Build Packet** - zoals in de gist: summary, goals, non-goals, current state, proposed approach, acceptance criteria, interfaces/contracts/data changes, per change: goal, non-goals, files/components, implementation checklist, **verification plan** (geparametriseerd: `test-first` | `validation-workflow` | `manual-with-expected-results`, met verplichte motivatie als het geen test-first is), rollout/rollback, done-when. Afsluitend: risks, assumptions, open questions.

**C3 Clarifier Result** - PASS/FAIL, reason, requested edits (genummerd), questions for the planner, risks to acknowledge, sign-off criteria.

**C4 Gate Decision** - PROCEED/REVISE/STOP, reason, required changes, human decisions made, open questions deferred. Dit contract wordt door een mens ingevuld; de rolbeschrijving bevat de checklist uit de gist (goal nog steeds juist, scope acceptabel, criteria toetsbaar, verificatie geloofwaardig, risico's omkeerbaar, builder kan uitvoeren zonder requirements te verzinnen).

**C5 Review Handoff** - core (naar alle reviewers): diff summary 2-5 bullets, changed files/components, genummerde acceptance criteria met implementatielocatie, contracts touched of `<none>`. Extended (alleen naar boss): tests, red evidence, green evidence (of het equivalent uit het gekozen verificatiemodel), refactor after green, deviations, follow-ups not done.

**C6 Reviewer Verdict** - per reviewer: BLOCK / SHIP / SHIP WITH NITS, must fix, should fix, nice to have, acceptance criteria coverage (per AC: pass/fail + evidence), contract drift.

**C7 Final Verdict** - als C6, plus: reviewer disagreements met resolutie, builder next action. Prioriteitsregel vastgelegd: correctness en safety eerst, dan maintainability, dan polish.

### Rolprompts

Per rol één bestand met vaste secties: Role, Inputs (verwijzend naar contracten per ID), Guardrails, Procedure, Stop conditions, Output (verwijzend naar contract-ID). Inhoudelijk gebaseerd op de gist, met deze aanpassingen:

- Alle Linear-verwijzingen vervangen door C0 Work Item.
- Builder: het execution-loop-blok (restate goal, confirm commands, red proof, smallest change, refactor only in touched area, record evidence) blijft, maar de red/green-stappen verwijzen naar het gekozen verificatiemodel uit C2.
- Reviewers: de vier persona's uit de gist blijven, elk als los bestand zodat adapters ze onafhankelijk en parallel kunnen starten; expliciet vastgelegd dat reviewers elkaars output niet zien vóór hun eigen verdict.
- Triage: nieuwe rol, kort, met de S/M/L-heuristiek en de waarschuwing uit het bronartikel als grondslag.
- Human Gate: herschreven als instructie voor de mens, niet als agentprompt; dit verschil expliciet benoemd (didactisch relevant).

### Adapters

- **claude-code**: subagent-bestanden die per rol de bijbehorende `core/roles/*.md` als systeeminstructie gebruiken, plus een `/orc`-achtig command dat de pipeline orkestreert, bij de gate stopt en de gebruiker om C4 vraagt. README beschrijft installatie (kopiëren naar `.claude/`).
- **manual**: stappenplan om de loop met losse chatsessies te draaien (per rol een vers venster, alleen het contract-artefact meekopiëren), met een handoff-log-template waarin de mens als orchestrator C1 t/m C7 verzamelt. Dit is tevens de primaire onderwijsvorm.
- **openai-compatible**: per rol een voorbeeld van system prompt + user message (het contract) als JSON-payload, met een korte README over gebruik tegen een lokaal endpoint. Geen scripts in deze fase, alleen payload-voorbeelden.

### Teaching-laag (eerste eenheid)

- `les1-context-rot.md`: leerdoelen (uitleggen wat context rot is; het verband leggen met separation of concerns en interfaces; beargumenteren wanneer een multi-agent-aanpak proportioneel is), opbouw volgens D7, en verwijzingen naar de bronartikelen.
- `oefening1-ervaar-context-rot.md`: studenten lossen een middelgrote opdracht op in één lange chat zonder structuur, loggen waar het misgaat (vergeten instructies, scope-drift, "confident mush"), en draaien daarna dezelfde opdracht via de manual adapter. Reflectievragen vergelijken beide. Variant zonder AI: rollenspel waarin studenten zelf de rollen spelen en alleen de contract-artefacten mogen uitwisselen.
- `begrippen.md`: EN -> NL lijst (work item - werkitem, handoff - overdracht, enz.), conform D3.

## Acceptance criteria

1. `sphinx-build -b html docs/ docs/_build` (of `make html`) slaagt zonder errors en zonder broken-reference-warnings; de teaching-pagina's renderen.
2. Geen enkel bestand onder `core/` bevat de naam van een model, vendor of dienst (controleerbaar met grep op een afgesproken woordenlijst: claude, gpt, openai, anthropic, gemini, llama, vllm, linear, jira).
3. Elke rol onder `core/roles/` benoemt zijn input(s) en output uitsluitend via contract-ID's (C0 t/m C7) en elk genoemd contract-ID bestaat onder `core/contracts/`.
4. Elk contract bevat de drie secties Purpose, Schema, Example.
5. De drie adapters hebben elk een README met een uitvoerbare/volgbare procedure; de claude-code-adapter bevat per rol een agentdefinitie en één orchestrator-command.
6. Oefening 1 is volledig uitgewerkt (opdracht, stappen, reflectievragen, AI-loze variant); les 1 staat als outline met leerdoelen.
7. Nederlandse bestanden bevatten geen em-dash (—) of en-dash (–); controleerbaar met grep over `teaching/`.
8. README.md crediteert de gist en beide artikelen met links, en vermeldt de licentie (CC BY-NC-SA 4.0); het LICENSE-bestand bevat de volledige licentietekst.
9. De repo bevat een GitHub Actions workflow die bij push naar de hoofdbranch de Sphinx-site bouwt en naar GitHub Pages deployt; de buildstap is een los aanroepbaar commando (zodat het op Codeberg herbruikbaar is) en de workflow slaagt bij de eerste push.

## Build packet (changes voor de builder)

### Change 1: repo-skelet en fundament
**Goal:** mappenstructuur, README, .gitignore, `core/principles.md`, `core/loop.md`.
**Verification:** `manual-with-expected-results` - boomstructuur komt overeen met dit packet; AC2-grep slaagt op de twee core-documenten. *(Motivatie geen test-first: documentatie-artefacten, geen gedrag.)*
**Done when:** AC2 en AC8 gelden voor de aangemaakte bestanden.

### Change 2: contracten C0 t/m C7
**Goal:** acht contractbestanden conform de normatieve schema's hierboven.
**Verification:** `validation-workflow` - een check (scriptje of handmatige checklist) dat per bestand de drie secties aanwezig zijn en dat veldnamen uit de schema's voorkomen.
**Done when:** AC4 geldt; AC2-grep slaagt.

### Change 3: rolprompts
**Goal:** tien rolbestanden conform sectie-indeling en aanpassingen hierboven.
**Verification:** `validation-workflow` - cross-reference-check: alle contract-ID's in roles bestaan in contracts (AC3).
**Done when:** AC2 en AC3 gelden.

### Change 4: adapters
**Goal:** drie adapters zoals beschreven.
**Verification:** `manual-with-expected-results` - claude-code-adapter wordt in een testproject geïnstalleerd en `/orc` start en stopt bij de gate; manual-procedure is stap voor stap te volgen; openai-compatible payloads zijn valide JSON.
**Done when:** AC5 geldt.

### Change 5: Sphinx/MyST-setup
**Goal:** `docs/conf.py` met myst_parser, Makefile, `teaching/index.md` met toctree.
**Verification:** `test-first` in lichte vorm - eerst een build draaien die faalt op de nog ontbrekende toctree-doelen (red), dan de structuur compleet maken (green).
**Done when:** AC1 geldt.

### Change 6: didactische eenheid 1
**Goal:** les 1 (outline), oefening 1 (volledig), begrippenlijst.
**Verification:** `manual-with-expected-results` - AC6 en AC7; rendercheck in de gebouwde site.
**Done when:** AC1, AC6, AC7 gelden.

### Change 7: CI en publicatie
**Goal:** `.github/workflows/docs.yml` die de Sphinx-build draait en naar GitHub Pages deployt; Pages-configuratie gedocumenteerd in README (instelling "GitHub Actions" als source). Buildcommando identiek aan het lokale `make html`, zodat de deploy-laag later naar Codeberg verplaatst kan worden zonder de build aan te raken.
**Verification:** `validation-workflow` - push naar de hoofdbranch, workflow groen, gepubliceerde site bereikbaar en rendert les 1 en oefening 1.
**Done when:** AC9 geldt.

**Volgorde en afhankelijkheden:** 1 -> 2 -> 3 -> 4; 5 kan parallel aan 2-4; 6 vereist 2, 3 en 5; 7 vereist 5 en komt als laatste. Elke change is een eigen commit (of PR), reviewbaar op zichzelf.

## Risks

- **Schijnprecisie in contracten:** te strakke schema's nodigen uit tot invuloefeningen in plaats van denken. Mitigatie: elk schema markeert welke velden weggelaten mogen worden met `<none>` en de Examples tonen beknoptheid.
- **Onderhoudslast adapters:** platforms veranderen sneller dan de kern. Mitigatie: D1/D2 houden de kern stabiel; adapters dragen een "last verified"-datum in hun README.
- **Didactisch risico:** studenten kopiëren de loop als recept zonder het principe te begrijpen. Mitigatie: D7 plus de AI-loze rollenspelvariant.
- **Tokenkosten** bij volledige loop voor kleine taken; gemitigeerd door de triage-rol, maar in onderwijscontext (gratis/limited tiers, lokale modellen) expliciet benoemen in de manual-adapter-README.

## Assumptions

- A1: Claude Code's subagent- en commandformaat zoals bekend per medio 2026; builder verifieert het actuele formaat bij Change 4 tegen de officiële documentatie.
- A2: Publicatiedoel is een statische Sphinx-site op GitHub Pages (bevestigd); mogelijke latere migratie naar Codeberg, daarom blijft de buildstap los van de deploystap. Geen LMS-integratie nodig in deze fase.
- A3: De gist mag als inhoudelijke basis dienen mits gecrediteerd (de auteur nodigt expliciet uit tot hergebruik: "borrow the loop, steal the principle"); zie wel Q1.

## Resolved questions (gate-beslissingen)

- **Q1 Licentie:** CC BY-NC-SA 4.0 voor de gehele repository (D10). Creditering van de gist en artikelen in README volstaat; auteur benaderen is niet nodig gezien diens expliciete uitnodiging tot hergebruik.
- **Q2 Sphinx-thema:** furo aangehouden als default (rustig, goede MyST-ondersteuning, dark mode); triviaal te wisselen via `conf.py` als het niet bevalt.
- **Q3 Repolocatie en -naam:** GitHub, repo `agent-role-loop`, publicatie via GitHub Pages; deploy-mechaniek draagbaar houden met het oog op mogelijke migratie naar Codeberg (D11).
- **Q4 Taal `adapters/manual/`:** Engels, consistent met core; Nederlandse studenthandleiding in `teaching/oefeningen/` verwijst ernaar.

## Open questions

- `<none>`

---

## Gate Decision (ingevuld door Misja, 2026-06-12)

```
Decision: PROCEED

Reason: Packet v2 beoordeeld; ontwerpbeslissingen D1-D11 akkoord,
acceptance criteria zijn toetsbaar, risico's acceptabel.

Required changes before build: <none>

Human decisions made:
- Q1: CC BY-NC-SA 4.0 voor de gehele repo
- Q2: thema furo
- Q3: GitHub + GitHub Pages, repo "agent-role-loop"
- Q4: adapters in het Engels, NL-studenthandleiding in teaching/

Open questions still deferred: <none>
```
