# #34: uitvoering Mistral/Vibe

## Grondslag en vrijgave

Werkitem [#34](https://github.com/misja/agent-role-loop/issues/34), norm-/procesbasis
`04c087cee43ef074f1e132686688cbf01014f2ce`. C1/C2 in [34-plan.md](34-plan.md),
vastgelegd als [concreet plan](https://github.com/misja/agent-role-loop/issues/34#issuecomment-6024662487).
Menselijk akkoord uit de werksessie is
[C4 PROCEED](https://github.com/misja/agent-role-loop/issues/34#issuecomment-6024762858).
PLANNED M; root orkestreert/plant/bouwt. Eén verse onafhankelijke review34 krijgt
alle AC1-11. Geen C3/C7, geen normwijziging. #34 ontwerp0/oplevering0;
W1 ontwerp0/oplevering0; NEG ontwerp0/oplevering1, met hieronder benoemde fout.
Merge nog niet vrijgegeven. #58 blijft afzonderlijk vervolg.

## Adapter en uitleg

`adapters/openai-compatible/mistral/` bevat technische naslag, projectingang,
AGENTS-voorbeeld, rolopdracht en installer. De installer kopieert twintig
ongewijzigde corebestanden plus drie gewone adapterbestanden onder
`.vibe/role-loop/`, met herkomst-/hashmanifest. Geen globaal Vibe-profiel, SDK,
MCP-server of framework toegevoegd. Bestaande projectinstructies/configuratie
blijven behouden; eventuele handmatige verwijzing heeft eigen rollback.

De compatible-README onderscheidt tekstaanroepen van Vibe met bestands-tools.
De nieuwe Nederlandse praktijkpagina en navigatie sluiten aan op module2 en
gedeelde casus, met het derdejaars doelgroepbeeld. Input, uitvoerder, toegang,
handeling, reden, succes/fout staan per stap. Nieuwe toepassing: Vibe-installatie,
account, expliciet absoluut projectpad, config/trust, toolselectie, nieuwe processen,
menseigen tests/Git, JSON-contractextractie en commitsnapshot. Technische naslag
staat apart; geen nieuwe voorkennisnorm of studentvalidatie geclaimd.

## Gemeten omgeving en grenzen

6 oktober 2026, Linux, Vibe 2.19.0. Geconfigureerde alias `mistral-medium-3.5`,
API-modelnaam `mistral-vibe-cli-latest`, provider `mistral`, endpoint
`https://api.mistral.ai/v1`. Exacte gewichten achter `latest` niet beschikbaar.
Geen modelupgrade of providerbenchmark. Credential in keyring aangetroffen zonder
waarde/identiteit te tonen; daadwerkelijke aanroepen werkten. Geen credentials,
ruwe conversaties of redeneerinhoud gepubliceerd.

Vooraf gelezen officiële Mistral-documentatie, links in plan/adapter. Die wijkt
op defaults af van lokale help; daarom expliciet `plan` of `accept-edits` en CLI-
allow-list. In 2.19.0 heet tekstvervanging `edit`, dezelfde geplande bevoegdheid
als `search_replace`. Metadata bevestigt beschikbare gereedschappen: planner en
beoordelaars alleen `read_file`/`grep`; bouwer ook `write_file`/`edit`.
`bypass_tool_permissions=false`, projectcontextinjectie en connectors per proces
uitgeschakeld. Geen shell/task/MCP/Git/trackergereedschap aan het model gegeven.
Tools kunnen onbekende namen proberen: die requests werden afgewezen, geen
uitgevoerde shell of schrijfactie van de leesrollen. Het ingebouwde planprofiel
vroeg soms om een planbestand; dat schrijfgereedschap was niet beschikbaar.

Globale config geïnventariseerd: geen eigen agent-/skill-/prompt-/toolpaden,
geen MCP-servers, geen globale hooks.toml/AGENTS.md; ingebouwde Vibe-skill en
explore-subagent stonden wel in de systeembeschrijving maar hadden geen uitvoerbaar
skill/task-gereedschap. Geen project/ancestor-hooks of andere AGENTS in de
/tmp-proef. Alleen de eigen neutrale AGENTS/PROJECT plus expliciete rolbronnen.
Gebruikersconfiguratie niet gewijzigd; sessielogs buiten de proef opgeslagen.
Toolselectie en trust zijn geen OS-sandbox; er wordt geen containmentclaim gedaan.

Hoststart vereiste toestemming omdat Vibe zijn eigen logbestand buiten de werkmap
opent en netwerk gebruikt. Dat verleent geen andere modeltools. De docs-build
vereiste eveneens hosttoegang voor de bestaande uv-cache. Test- en Gitcommando's
zijn door root als menselijke orkestratie uitgevoerd, niet door het Mistral-model.

## Echte hoofdproef W1

Tijdelijke repository `/tmp/arl34-smoke-0c2dckc3`, geen productieproject.
Basis `a201bb630740c5597a8c5e0c408f75b6b99265d6`, normen/core bytegelijk aan
bovenstaande projectbasis. De aangeleverde controleer.py blijft bytegelijk.

Eerste planner gebruikte bij uitgezette contextinjectie verkeerde ~/paden;
leesacties geweigerd, geen C2. Na absoluut pad kwam een concreet maar onvolledig
C2. Een nieuwe planner met exacte contractpaden/schema rondde de opdracht af.
Beide onvoltooide contractuitkomsten en geselecteerde gereedschapswaarnemingen
blijven in 34-proef. Geen C3-oordeel of productreparatie uit deze starts verzonnen.
De uiteindelijke C2 werd vóór bouwen vergeleken met exact vrijgegeven signature,
comprehension, scope, rechten en ongewijzigde suite; vergelijking staat in C4.
Planner noemt verificatie manual-with-expected-results wegens geen shell; root
behield werkelijke test-first-volgorde met rood vóór bouwen en groen erna.

Echte bouwer gebruikte `edit` voor alleen boekenplank.py. Root controleerde
exacte diff en ongewijzigde tests. Basis: één pass/drie TypeErrors, exit1.
Product: vier pass, exit0. Codecommit
`d3f1125760d441a6d8624c4b7c47b9185b7a8e43`.
C5-concept markeert groen/commit als pending; root vulde die pas na uitvoering aan.
Nieuwe Mistral-review las uitsluitend aangewezen C5/code/tests/normen/bewijs,
geen C1/C2 of maakgesprek. Exacte commitsnapshot gelezen; menselijke Gitlookup
blijft onderscheiden van eigen modelinspectie. C6 SHIP, S1-S4 nieuw onderzocht,
geen nits. Dit bewijst de technische hoofdroute, geen zelfstandig studentgebruik.

## Negatieve proef en fout in herstelorkestratie

Root injecteerde bewust gedeelde A-fixture, geen spontaan Mistral-defect.
Commit `e94946707ead4ad7180bfc3d6d59f13bf0caac78`:
zwakke suite drie pass/exit0; volledige suite drie pass/S4fail/exit1.
Nieuwe Mistral-review gaf BLOCK op opslagmutatie. Het oordeel generaliseert ook
S2/S3-falen; dat wordt niet als gemeten feit overgenomen. De daadwerkelijke suite
bewijst hun verse fixtures groen en S4 rood. Alle gevraagde fixes betreffen dezelfde
regel; de herstelbeoordeling krijgt geen hergebruikte C6-passdekking.

Het voorbereidingsscript hergebruikte `/tmp/arl34-negative.json` voor fixture-
metadata én CLI-berichten. Daardoor kreeg het bij registratie een lijst in plaats
van een object en faalde voordat de teller/invoer werden geschreven. Root liet
vervolgens ten onrechte de afhankelijke bouwer starten. Die las de ontbrekende
repair-input, vervolgens bestaande C5/code, en repareerde de ene regel.
De vereiste teller was tijdens deze bewerking nog 0. Dit is een procesfout en
**geen bewijs van vooraf geregistreerd herstel**. Niet achteraf als correct geboekt.

NEG delivery1 is daarna met de foutbron geregistreerd, zonder reset.
Het gerepareerde product is bytegelijk aan het hoofdproduct; echte menselijke
volledige suite vier pass/exit0. Herstelcommit
`74e351d9bef6f0d5f936b2108185426226eee865`.
C5-concept beweert ten onrechte dat de teller vooraf bestond en noemt eerder rode
uitvoer groen; C5-kern corrigeert beide met werkelijke bronnen en grenzen.
Een verse repair-review kreeg exact diff, eerdere blockers, actuele testuitvoer,
geen behouden passdekking, persistente stand en deze fout expliciet mee. C6 BLOCK:
S1-S4 nieuw onderzocht en pass, maar PROCESS-BLOCKER-001 vereist een werkelijk
menselijk continuation/split/stop-besluit wegens te late registratie. Er wordt
geen SHIP van de herstelketen geclaimd.

Het private proefscript heeft nu verplichte input-/tellerpreflight: bij ontbrekende
repair-input stopt het vóór Vibe-start. Die stop is daadwerkelijk gecontroleerd.
Metadata en provideruitvoer krijgen verschillende paden. Er is nog geen extra
bouwer gestart. Een eventuele extra begrensde bewijsproef vereist een werkelijk
menselijk vervolgopdracht volgens core/loop.md; de asynchrone vraag is gesteld.
Een antwoord wordt afzonderlijk met exact bereik geregistreerd; wachten is geen
akkoord en herhaalde processen herstellen historische registratie niet.

## Controles en bewijsgrenzen

Acht installerfixtures geslaagd: bestaande bytes behouden en rollback;
installatieconflict; symlinkstop; gewijzigde/missende owned bytes stoppen vóór
verwijderen; ongeldige bestands-/directoryownership stoppen; vreemd bestand behouden.
Negen normbronnen bytegelijk, twintig gekopieerde corehashes gelijk aan normcommit.
Docs-build onder -W --keep-going exit0; 310 lokale links/fragmenten inclusief
inkomende nieuwe navigatie, nul fouten. Geen routinebeeldcontrole bij dit tekstwerk.
Working-tree diff --check schoon vóór toevoeging van bewijsbestanden; definitieve
commitcontrole volgt afzonderlijk, zonder ongetrackte bestanden daarin te claimen.

Technische runs, contractlezing en studentwaarnemingen zijn verschillende bronnen.
Studentwaarnemingen niet beschikbaar. Bare Mistral-HTTP-pad niet uitgevoerd en
niet door Vibe-evidence bewezen. Native GitHub-reviewintegratie niet geclaimd;
root verzorgt issue/PR-feedback. Het werkitem wordt niet volledig getest afgesloten
zolang het vereiste procesbewijs en onafhankelijke AC1-11-beoordeling ontbreken.
