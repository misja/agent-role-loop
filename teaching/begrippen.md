# Begrippenlijst

De rolprompts en contracten in `core/` zijn Engelstalig (ze presteren consistenter in het Engels en zijn internationaal herbruikbaar); de lessen en oefeningen zijn Nederlandstalig. Deze lijst overbrugt de twee talen. De Engelse term is leidend in de artefacten; gebruik in je verslagen de Nederlandse. Waar het lesmateriaal naar een specifiek bestand in `core/` verwijst, is dat een klikbare link naar het Engelse bronbestand in de repository, buiten deze site; een verwijzing naar een map (zoals `core/`) blijft als code staan.

| Engels | Nederlands | Toelichting |
|---|---|---|
| work item (C0) | werkitem | De invoer van de loop: een taak in platte Markdown, onafhankelijk van een ticketsysteem |
| handoff | overdracht | Het moment waarop werk van de ene rol naar de andere gaat |
| contract | contract | De afgesproken vorm van een overdracht; de stabiele interface tussen rollen (C0 t/m C7) |
| artifact | artefact | Het concrete document dat een rol oplevert volgens een contract |
| context rot | context rot | Kwaliteitsverval wanneer één gesprek alles opstapelt: opdracht, logs, mislukte pogingen, oude aannames. We vertalen deze term bewust niet |
| context isolation | contextisolatie | Elke rol een eigen, verse context geven als tegenmaatregel tegen context rot |
| confident mush | zelfverzekerde brij | Output die stellig klinkt maar aannames, oude instructies en gissingen door elkaar haalt; het herkenbaarste symptoom van context rot |
| scope drift | scope-verschuiving | Het werk groeit ongemerkt voorbij de oorspronkelijke opdracht |
| triage | triage | De proportionaliteitscheck vooraf: volledige loop, licht pad, of afwijzen |
| planner | planner | Rol die een werkitem omzet in een uitvoerbaar bouwplan |
| build packet (C2) | build packet | Het bouwplan: doelen, aanpak, acceptatiecriteria, changes en verificatie. We houden de Engelse term aan |
| clarifier | verhelderaar | Rol die ambiguïteit uit het plan haalt vóór er gebouwd wordt |
| human gate | menselijke poort | Beslismoment tussen plannen en bouwen dat alleen een mens mag nemen |
| quality gate, gate | poort (kwaliteitspoort) | In teaching-materiaal de Nederlandse term poort. "gate" alleen intern (board, werkitem-taal) en als productnaam (SonarQube quality gate) |
| builder | bouwer | Rol die het goedgekeurde plan uitvoert en bewijs verzamelt |
| reviewer | beoordelaar | Rol die het resultaat vanuit één perspectief beoordeelt; er zijn er vier, parallel en geïsoleerd |
| reviewer boss | hoofdbeoordelaar | Rol die de vier oordelen samenvoegt tot één eindoordeel |
| verdict (C6, C7) | oordeel | BLOCK, SHIP of SHIP WITH NITS, met bevindingen |
| acceptance criteria | acceptatiecriteria | Toetsbare uitspraken die bepalen wanneer het werk af is |
| verification | verificatie | Het bewijs dat een change doet wat beloofd is; per change gekozen model |
| test-first (red/green/refactor) | test-first (rood/groen/refactor) | Verificatiemodel: eerst een falende test, dan de kleinste implementatie, dan opschonen |
| validation workflow | validatieworkflow | Verificatiemodel: een scriptmatige of stapsgewijze controle met vooraf bekende uitkomsten |
| separation of concerns | scheiding van verantwoordelijkheden | Ontwerpprincipe: elk onderdeel één taak. De rollenloop past dit toe op een werkproces |
| interface | interface (koppelvlak) | Het afgesproken raakvlak tussen onderdelen; in de loop zijn de contracten de interface en de rolprompts de implementatie |
| information hiding | informatie verbergen | Wat achter de interface gebeurt, blijft daar; een rol hoeft de transcripten van andere rollen niet te zien |
| orchestrator | orkestrator | Wie of wat de artefacten tussen de rollen heen en weer draagt; in de manual adapter ben jij dat |
| proportionality | proportionaliteit | Gereedschap afstemmen op de klus: geen zes rollen voor een typo |
