# #52: kwaliteitsraamwerk en literatuurtoelichtingen

## C1: route en verantwoordelijkheden

- C0: [#52](https://github.com/misja/agent-role-loop/issues/52), vervolg op #46.
  Bord gecontroleerd op 5 oktober 2026: #48–51 Done; #52 Backlog.
- Route: PLANNED, omvang M. Eén pagina, maar samenhangende uitleg,
  bronclaims en verwijzingen vanuit modules vragen een concreet ontwerp.
- Proces- en projectnormbasis: `0765540c53243a328a2b9809770fe2097d4a05fe`.
  Leesbare bronnen: `CLAUDE.md`, `core/loop.md`, `core/contracts/`,
  `teaching/conventies.md`, `doelgroep.md`, `schrijfwijzer.md`, `begrippen.md`.
- Orkestrator/planner/bouwer: root. Eén verse onafhankelijke reviewer
  `review52`, met tekst-, bronkritiek- en procesdekking voor AC1–7.
  Geen aparte C3 of inventarisagent: de onzekerheden betreffen gerichte
  broncontrole en tekstkeuzen die de planner hieronder afbakent.
- Herstelstand: ontwerp 0, oplevering 0; blijvend register op #52 en in
  `onderzoek/52-uitvoering.md` bij uitvoering. Eén ronde per soort volgens core.
- C4 vereist op dit C2 v1 vóór bouwen. Het besluit bij #46 autoriseerde de
  registratie van het vervolg; het mergebesluit bij #51 betreft die PR.
- Risico: passages over verplaatste thema's moeten vindbaar blijven voor
  modules 2–6. Geen norm-, route-, doelgroep- of codewijziging.
- LIGHT-basis en REJECT-advies: niet van toepassing.

## C2 v1: samenvatting

Werk het restant van het kwaliteitsraamwerk uit aan dezelfde uitleenhandeling
als het reeds besloten begin. De lezer ziet welke afspraak geldt, welke situatie
een automatische controle onderzoekt en welke vraag beoordeling toevoegt.
Plaats de uitgebreide gereedschapskaart bij gerichte naslag. Geef per overige
literatuurbron een leesvraag, benodigd leesmoment/voorkennis en een beperking
die bepaalt welke conclusies de bron toelaat. Onderzoek legt bronclaims en
bewijsgrenzen vast; het onderwijsmateriaal krijgt geen onderzoeksverslag.

## Doelen

1. Afspraak, controle en beoordeling onderscheiden aan concrete handelingen.
2. Eén doorlopende casus en gerichte verdiepingsroutes bieden.
3. Brontoelichtingen beperken tot controleerbare inhoud en bruikbaar leesadvies.

## Geen doelen

Geen herschrijving van het raamwerkbegin of de Farley-proef, nieuwe module,
extra competentiekader, empirische studentvalidatie, volledige literatuurreview,
nieuwe providerarchitectuur, code/core/adapters/slides/toetsing of normwijziging.

## Huidige stand

Het begin tot 'Drie soorten kwaliteitsmechanismen' gebruikt de tweede
uitleenpoging en benoemt een bewijsleemte. Het vervolg gebruikt plots orders
en export; de thematabel introduceert veel tools en numerieke soortlabels.
Werkingsprincipes keren gedeeltelijk terug zonder nieuwe toepassing.
Modules 2 en 3 noemen bestaande sectietitels als leesaanwijzing; modules 4–6
gebruiken de oordeelslaag/menselijke poort en de gereedschapskaart.
Deze leesfuncties moeten behouden blijven.

Codex-, Alenezi- en Sweller-toelichtingen mengen leesadvies met brede claims
over de waarde van de aanpak en het onderwijs. Farley is al begrensd tot
hoofdstuk 5, Feedback. Studentenwaarnemingen zijn niet beschikbaar.

## Aanpak en onderwijsontwerp

Tekstfunctie: uitleg bij de drie mechanismen; naslag bij thema's en principes;
bronkeuze bij Verder lezen. Voorkennis: programmeren, tests en versiebeheer,
plus de vindbare voorbereiding `van-chat-naar-agent.md` over agent, rol en
overdracht. Eerdere kennismaking garandeert geen zelfstandige toepassing.

De nieuwe stap is eenzelfde wijziging vanuit drie verschillende vragen lezen:
de afgesproken weigering van de tweede uitlening, de uitgevoerde test met twee
pogingen en bewaarde uitleenstatus, en de beoordeling van ontbrekend bewijs.
De controle wordt als uitleg beschreven, zonder gefingeerde testuitvoer.
Gebruik de bestaande sectietitels/ankers bij de drie soorten waar mogelijk,
zodat eerdere leesaanwijzingen kloppen. De uitleencasus vervangt de
exportvoorbeelden; er ontstaat geen nieuwe gedragsvereiste voor oefencode.

Behoud de betekenisvolle grens bij coverage: meting, afgesproken drempel en
inhoudelijke testdekking zijn verschillende vragen. Benoem de eigenaar en
het waarneembare gevolg van afspraak, uitvoering en beoordeling. Gebruik
gewone woorden vóór categorie- of toolnamen.

De uitgebreide themakaart wordt 'Naslag: kwaliteitsthema’s', met benoemd
leesdoel en woorden in plaats van terugzoekende cijferlabels. Selecteer en
verklaar details op hun functie; geen afzonderlijke introductie van iedere
tool. Principes krijgen een korte concrete toepassing op dezelfde overdracht,
met verwijzing naar core voor volledige regels. Menselijk planbesluit en
merge blijven onderscheiden; core blijft de enige routenorm.

Verder lezen: per bron één concrete vraag, een passend leesmoment en vindbare
voorkennis. Codex beschrijft geobserveerd gebruik, niet bewezen methodewinst.
Alenezi biedt een voorstel/synthese, niet zelfstandig empirisch bewijs van
ons onderwijs. Sweller wordt gekoppeld aan de onderzochte leerprocessen;
de keuze voor afnemende begeleiding hier blijft een eigen ontwerpkeuze.
Beweringen over specifieke competenties, beginnereffecten, referentiefouten
of fading blijven alleen als de oorspronkelijke bron ze controleerbaar draagt.
Anders schrappen of begrenzen, met reden in het onderzoeksregister.

## Acceptatiecriteria en controle

C0 AC1–7 ongewijzigd; alle toegewezen aan review52:

| AC | Verwachte controle en uitkomst |
|---|---|
| 1 | Reviewer wijst in één uitleenhandeling afspraak, invoer, controle, waarnemingsgrens en beoordelingsvraag aan; thema's/principes hebben een herkenbare leesfunctie. |
| 2 | Geen onverklaarde casuswisseling; exportvoorbeelden vervangen door uitleenvoorbeeld. Geen nieuw oefengedrag. |
| 3 | Claimregister met oorspronkelijke bron/sectie, te behouden of begrensde claim en leesdoel voor Codex, Alenezi, Sweller; reviewer controleert elke herziene toelichting gericht aan de primaire bron. |
| 4 | Bronbeperkingen bepalen gebruik; geen onbekende competentielijst of methodeverdediging; Farley-toelichting bytegelijk. |
| 5 | Zelfstandige leesgang: waarvoor opent de lezer elk van de vier bronnen, wat kent hij vooraf en welke claim doet de toelichting? Registreer agentlezing, geen studentwaarneming. |
| 6 | Raamwerkbegin, modules/leeruitkomsten, cases en bundel ongewijzigd; herordening geeft geen extra opdracht of ingevulde oefenoplossing. Noodzakelijk verschil eerst aan mens. |
| 7 | Normlezing met concrete passages; docs-build -W --keep-going zonder waarschuwingen; lokale links van/naar gewijzigde pagina en eventuele nieuwe fragmenten werken; bewijsgrenzen geregistreerd. |

## Basis en bronnen

Naast de normcommit: `onderzoek/46-inventarisatie-en-plan.md` wijziging 3/4,
`46-inleidende-teksten-proef.md` raamwerk/Verder lezen, `46-uitvoering.md`.
Primaire bronnen gericht geopend op 5 oktober 2026:

- [Codex-gebruiksstudie, PDF](https://cdn.openai.com/pdf/5d1e1489-21c0-43e4-9d42-f87efdbf0082/the-shift-to-agentic-ai-evidence-from-codex.pdf): introductie, onderzoekspopulaties en gebruikspatronen; bij uitvoering de exacte claimplaatsen en beperkingen vastleggen.
- [Alenezi v1](https://arxiv.org/html/2604.10599v1): oorspronkelijke synthese; abstract alleen is onvoldoende voor alle huidige detailclaims.
- [Sweller, uitgeverspagina](https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1202_4): abstract over probleemoplossen en kennisopbouw; geen grond om uitsluitend hieruit fading of effect van deze leerlijn af te leiden.
- Farley: bestaande broncontrole uit #46 hergebruiken uitsluitend voor de behouden hoofdstukverwijzing, niet als nieuwe volledige boekcontrole.

## Herstelstand

Ontwerp 0, oplevering 0. Geen eerdere blockers. Registreer tellers vóór eventueel
herstel en geef een verse repair-reviewer de expliciete herstelbijlage.

## Interfaces, contracten en gegevens

Geen. Bestaande verwijzingen naar sectietitels zijn gedeelde tekstafhankelijkheden.

## Wijzigingen

### 1. Raamwerkvervolg en naslag

Bestand: `teaching/kwaliteit-als-gedeelde-verantwoordelijkheid.md`, vanaf
'Drie soorten kwaliteitsmechanismen' tot Verder lezen.

- [ ] Drie mechanismen en hun samenwerking aan de bestaande uitleenhandeling uitleggen.
- [ ] Thema's en principes selecteren/herordenen met expliciet naslagdoel.
- [ ] Bestaande sectieverwijzingen behouden of, indien noodzakelijk, uitsluitend hun gerichte verwijzingen bijwerken en registreren.

Verificatie: manual-with-expected-results, aangevuld met validation-workflow
voor build/links/beschermde diff. Test-first past niet bij tekst zonder gewijzigd
programmagedrag. Reviewer kan aan het voorbeeld de drie vragen onderscheiden,
vindt de nodige uitleg vóór gebruik en benoemt de resterende bewijsgrens.
Geen screenshots tenzij vormgeving wijzigt of een concreet weergaveprobleem blijkt.
Gereed: AC1/2/6/7 pass. Rollback: wijzigingscommit terugdraaien.

### 2. Literatuurtoelichtingen en bewijsregister

Bestanden: dezelfde pagina (drie toelichtingen), `onderzoek/52-uitvoering.md`;
`teaching/references.bib` alleen bij een aangetoonde bibliografische fout.

- [ ] Primaire passages controleren en claimregister vastleggen met bronbeperkingen.
- [ ] Leesvraag/moment/voorkennis/beperking formuleren; Farley behouden.
- [ ] C5 met exacte productcommit, besluiten en bewijsgrenzen aan onafhankelijke reviewer geven.

Verificatie: manual-with-expected-results; geen softwaregedrag dat test-first
kan toetsen. Iedere resterende inhoudelijke claim heeft passende bronsteun.
De vier leesadviezen helpen kiezen zonder winst of studentbegrip te beloven.
Gereed: AC3/4/5/7 pass. Rollback: wijzigingscommit terugdraaien.

## Risico's, aannames en open vragen

Een compactere toelichting kan nuance verliezen; het claimregister en de
onafhankelijke bronlezing toetsen dat. Niet beschikbare volledige bronpassages
worden niet vervangen door secundaire samenvattingen of stellige claims.
Geen aanname van gemeten leereffect. Geen open inhoudelijke normkeuze.
C4-vraag: uitvoering van dit C2 v1 vrijgeven?
