# Redactieproef #30

## Aanleiding en besluit

De eerste schrijfproef gebruikte het begrip agent zonder de programmatische
toepassing van een taalmodel uit te leggen. De onafhankelijke lezer van die proef
vond dat geen blokkade. De gebruiker benoemde vervolgens de ontbrekende
voorkennis: Software Engineering is bekend, LLM-gebruik uitsluitend via webchat.
Dat laat zien dat een leesbeoordeling tegen een onvoldoende expliciet
doelgroepbeeld een begripsprong kan missen.

De aanleiding en de algemene borgingsopdracht staan in
[#37](https://github.com/misja/agent-role-loop/issues/37).
De gebruiker vroeg daarna om #30 concreet uit te voeren met deze uitgangspunten.
Het [geregistreerde uitvoerbesluit](https://github.com/misja/agent-role-loop/issues/30#issuecomment-5641103857)
past ze toe op #30; #37 blijft verantwoordelijk voor de projectbrede normteksten
en de borging bij toekomstige werkitems. De oude drie-alineamaat begrenst deze
bijgestelde opdracht niet.

## Uitwerking

De introductie bouwt vanaf een menselijke wijziging en beoordeling de stap op
van webchat naar modelaanroepen via een API, context en gereedschappen. Daarna
volgen agents, sessies, rollen en overdrachtscontracten. Het kwaliteitsraamwerk
gebruikt dezelfde exportcasus om afspraken, automatische controles en
beoordeling te onderscheiden. De README-introductie sluit daarop aan.

De leerlijn en de sectie Verder lezen, inclusief bronkritiek, zijn behouden.
De generieke core en de normbestanden zijn niet gewijzigd. Deze registratie is
een procesverslag, geen tweede bron voor onderwijsconventies.

## Beoordeling en verificatie

Een auteur en een onafhankelijke lezer werkten met gescheiden contexten.
De lezer ontving C0, het menselijke uitvoerbesluit, de C5-kern en normvindplaatsen,
zonder maaktranscript of eerdere reviews. Zijn
[C6](https://github.com/misja/agent-role-loop/issues/30#issuecomment-5641217616)
is SHIP WITH NITS: geen inhoudelijke blokkades. De begripsweergave onderscheidt
model, agentsysteem, sessie en rol en benoemt de toepassing van de
engineeringprincipes en de verantwoordelijkheid van de mens.

Het ene precisiepunt over context rot is daarna gericht verwerkt: de introductie
stelt groeiende gespreksgeschiedenis niet gelijk aan kwaliteitsverlies. De
orkestrator las deze wijziging na. Geen tweede volledige onafhankelijke lezing.

De docs-build met `-W --keep-going` slaagde zonder waarschuwingen of fouten,
eerst op een nieuwe uitvoermap en daarna na de precisiecorrectie. Hiervoor is
de bestaande Sphinx-omgeving gebruikt; er zijn geen dependencies toegevoegd.
`git diff --check` slaagde.

De orkestrator bekeek de gebouwde introductie en raamwerkpagina in headless
Chrome, inclusief navigatie, citaties, tabel en het daadwerkelijk gerenderde
Mermaid-diagram. Ook een smalle weergave van de introductie en een lokale
Markdown-rendering van de README zijn bekeken. Dit is geen controle van een
gedeployde site of een volledige toegankelijkheidstoets.

## Grenzen en vervolg

Tokens en agentduur: niet beschikbaar. Studentwaarnemingen: niet beschikbaar.
De onafhankelijke agentlezing is geen studentproef en toont geen algemene
kwaliteits- of efficiëntiewinst aan.

De mens beslist over merge. #37 moet de doelgroep en redactionele uitgangspunten
nog projectbreed vastleggen en hun toepassing in ontwerp, overdracht en
beoordeling borgen. #35 en #36 voeren de latere moduleherzieningen uit.
