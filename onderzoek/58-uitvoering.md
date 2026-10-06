# #58 - aanvullende boekenplankcontroles

## Basis en menselijk besluit

C1/C2 v1: [58-plan](58-plan.md), goedgekeurde commit
276a804a5ef723aba0e04800761e2cb4f3037128.
[C4 PROCEED](https://github.com/misja/agent-role-loop/issues/58#issuecomment-6025714624)
registreert het werkelijke gebruikersantwoord akkoord. Normbasis
b07b477c9fb8aa291753d0c99f70c2b29ee9c72d, bronnen volgens C1/C2.
Ontwerp0, oplevering0; [herstelstand](58-herstelstand.json).

## Plaats en uitleg

Aparte controleer_extra.py in teaching/cases/praktijk-projectomgeving,
opgenomen in downloadbundel. Bestaande S1-S4/CLI, codeversies en historisch bewijs
blijven behouden. Nieuwe optionele README-sectie laat de derdejaarsstudent
met bekende Python/tests het resultaat van een lijstaanroep onderzoeken.
Containerwijziging en boekobjectwijziging worden onderscheiden; het laatste
valt buiten deze suite. Per stap staan invoer, actie, reden en uitkomst.

## Feitelijk nieuw bewijs

Validation-workflow, niet product-test-first: bestaande B-code hoefde geen fix.
Tests eerst uitgevoerd op tijdelijke foutvarianten, vervolgens op dezelfde B.
[Resultaten](58-proef/resultaten.json) met codehashes; gebruikte foutdiffs en
ongewijzigde stdout/stderr onder 58-proef. De tijdelijke varianten veranderen
alleen een kopie van B onder /tmp; bekende A komt uit de vaste casusbron.

- false.patch: filtert ook bij False; E1 en E3 falen, E2-subtests geven IndexError;
  suite exit1. Dit toont detectie van verkeerd False-gedrag, geen afzonderlijke
  garantie over ieder mogelijk implementatiefouttype.
- container.patch: retourneert de interne lijst bij standaard/False; E2 faalt
  bij clear/pop en geeft AttributeError bij append(None), exit1. E1/E3 slagen.
  De AttributeError is hier het geobserveerde gevolg van besmette opslag,
  geen correct productgedrag of beweerd assertion-resultaat.
- Bekende A: E1 slaagt; E2 en E3 falen omdat het filter de opslag wijzigt, exit1.
- B als tijdelijke werk-kopie en rechtstreeks met b: drie tests pass, exit0.

Oorspronkelijke commando's werkelijk opnieuw uitgevoerd: basis basis 1pass/0,
a zwak 3pass/0, a regressie 1fail/1, b volledig 4pass/0. Uitvoer afzonderlijk
bewaard; oude bewijs.txt en oorspronkelijke proefdossiers niet herschreven.

[Behoudcontrole](58-proef/behoud.json): 113 aangewezen historische bestanden
bytegelijk aan norm/basiscommit. Zip heeft één nieuw bestand controleer_extra.py
en gewijzigde README; alle overige oude zipentries bytegelijk, nieuwe suite en
README exact gelijk aan bron. Bundel blijft de historische corebasis bevatten.
Build make -C docs html -W --keep-going exit0, [log](58-proef/build.txt).
Eerste sandboxpoging stopte vóór Sphinx vanwege read-only uv-cache; herhaald
met de vereiste escalatie. [Gerichte lokale links](58-proef/links.txt), inclusief
inkomende links naar praktijkhoofdstuk en download, geen fouten.
README is bundeltekst, geen eigen Sphinx-pagina; geen standaard beeldcontrole.

## Grenzen en overdracht

Geen provider gestart, geen norm-/productcodewijziging, geen studentwaarneming.
Mutantdetectie en technische checks bewijzen geen algemene correctheid of begrip.
Alle AC1-5 gaan naar één verse onafhankelijke strikte beoordelaar met exacte
productcommit, C5-kern, leesbare normen en noodzakelijk objectief bewijs, zonder
maaktranscript. Eindbeoordeling en menselijk mergebesluit volgen nog.

Git diff --check meldt uitsluitend letterlijke trailing spaces in bewaarde
unittest/Sphinx-uitvoer en een lege contextregel in false.patch. Deze ruwe
bewijsbytes blijven behouden; gewijzigde productcode/uitleg hebben geen
whitespacebevindingen. Dit is geen claim van volledig schone onderzoeksdiff.
