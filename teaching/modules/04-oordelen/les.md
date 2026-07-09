# Kwaliteit als afweging tussen botsende perspectieven

## Plaats in de leerlijn

Vierde module. In module 3 zag je dat een groene poort niets bewijst en dat er een mens moet oordelen. Deze module gaat over dat oordeel: je neemt zelf de rol van beoordelaar in. Vereiste voorkennis: module 3 afgerond, en het kwaliteitsraamwerk, soort 3.

De les hoort bij [oefening 4](oefening.md), waarin je een door AI gebouwde reserveringen-uitbreiding beoordeelt vanuit de vier perspectieven.

## Leeruitkomsten

De leeruitkomsten staan als "Wat ga je leren" op de [module-index](index.md).

## Opbouw

### Kwaliteit spreekt zichzelf tegen

In het [kwaliteitsraamwerk](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md) is de derde soort kwaliteitsmechanisme de oordeelsmatige: vragen waarop geen drempel en geen scan antwoord geeft. Vier beoordelaars vertegenwoordigen kwaliteitsdimensies die in de praktijk botsen: de strikte wil correctheid en volledige dekking, de pragmatische wil opleveren, de adversariële zoekt het niet-afgevangen geval, en de onderhoudbaarheids-beoordelaar kijkt voorbij vandaag. Correctheid tegenover snelheid, volledigheid tegenover opleveren, veiligheid tegenover eenvoud. Dit zijn reële spanningen, geen schijntegenstellingen.

### De vier beoordelaars op een concrete uitbreiding

Het worked example is een door AI gebouwde reserveringen-uitbreiding van de boekenplank (`teaching/cases/module4-reserveringen/`). De code werkt en de tests slagen. Het gaat hier niet om verstopte fouten, maar om verdedigbare ontwerpkeuzes waarover de vier perspectieven het oneens zijn:

- **Strikt:** de opdracht is niet gepind. Moet reserveren van een beschikbaar boek het meteen uitlenen? Wat gebeurt er bij een dubbele reservering? Die ambiguïteit is onaf.
- **Pragmatisch:** een simpele wachtlijst zonder vervaltermijn is goed genoeg voor nu; niet elke uitbreiding hoeft af te zijn.
- **Adversarieel:** reserveer een boek en verwijder het; een wachtlijst die nooit vervalt en zo een boek blijft blokkeren; reserveren van een beschikbaar boek dat het stil uitleent in plaats van reserveert.
- **Onderhoudbaarheid:** `terug` doet nu twee dingen, teruggeven en opnieuw uitlenen; de wachtlijst is verstrengeld met het uitlenen; namen dienen als identiteit.

Geen van deze vier noemt de code fout. Ze wegen dezelfde werkende uitbreiding anders. Dat is de kern van de oordeelslaag: redelijke mensen zijn het oneens over code die werkt en verdedigbare keuzes maakt.

### De hoofdbeoordelaar prioriteert

De vier oordelen spreken elkaar tegen, en dat lost de hoofdbeoordelaar ({core}`roles/reviewer-boss.md`) niet op door één perspectief gelijk te geven. Hij prioriteert volgens een expliciete regel: correctheid en veiligheid eerst, dan onderhoudbaarheid, dan afwerking. Er bestaat geen uitkomst waarin alle vier tegelijk hun zin krijgen. Het prioriteren zelf is de oordeelsvaardigheid, niet het verzamelen van vier meningen.

### Wat dit is en wat niet

Deze module gaat over het oordeel: de perspectieven wegen en prioriteren. Nog niet over de beslissing of iets onomkeerbaars door mag, en niet over een rijkere interface; dat is de menselijke poort van module 5. Hier oefen je het wegen, daar het beslissen.

## Werkvormen en toetsing

- Werkvormen: korte instructie, gezamenlijke ontleding van twee perspectieven op de uitbreiding (worked example), daarna zelf de overige perspectieven en de synthese in oefening 4.
- Toetsing: formatief, via de oordelen en de verantwoordingsvragen van oefening 4.

## Bronnen

- Het raamwerk [Kwaliteit als gedeelde verantwoordelijkheid](../../kwaliteit-als-gedeelde-verantwoordelijkheid.md), sectie "Kwaliteit spreekt zichzelf tegen" en de derde soort.
- De repository zelf: de vier beoordelaarsrollen onder `core/roles/` en {core}`roles/reviewer-boss.md`, en de contracten {core}`contracts/reviewer-verdict.md` (C6) en {core}`contracts/final-verdict.md` (C7).
- Fagan, Design and code inspections {cite}`fagan1976design`. De klassieke onderbouwing van formele, onafhankelijke review: gestructureerde inspectie door meerdere ogen vangt fouten die één blik mist, de reden dat de loop vier beoordelaars parallel en geïsoleerd laat oordelen.

## Afronding

### Wat heb je geleerd

Kwaliteit is in de oordeelslaag geen afleesbare eigenschap maar de uitkomst van een afweging. Vier beoordelaars vertegenwoordigen botsende dimensies, en over werkende code die verdedigbare keuzes maakt zijn redelijke mensen het oneens. De hoofdbeoordelaar lost die spanning niet op maar prioriteert: correctheid en veiligheid eerst, dan onderhoudbaarheid, dan afwerking. Dat prioriteren is de vaardigheid.

### Zelfcheck

Beantwoord uit je hoofd; de sleutel wijst alleen waar je het kunt nakijken.

1. Waarom is kwaliteit in deze laag geen eigenschap die je afleest? Noem twee dimensies die botsen. (zie "Kwaliteit spreekt zichzelf tegen")
2. Neem één ontwerpkeuze uit de reserveringen-uitbreiding en laat zien hoe twee perspectieven haar verschillend wegen, zonder dat de code fout is. (zie "De vier beoordelaars op een concrete uitbreiding")
3. Hoe komt de hoofdbeoordelaar tot één oordeel als de vier elkaar tegenspreken, en waarom is dat prioriteren de kern? (zie "De hoofdbeoordelaar prioriteert")

### Volgende stap

Je hebt geoordeeld: de perspectieven gewogen en geprioriteerd. Module 5 (De menselijke poort) gaat over de beslissing die daarna komt en die alleen een mens mag nemen: mag dit zo door, vooral als de gevolgen onomkeerbaar zijn? Daar groeit de casus mee naar een door AI gebouwde interface met onomkeerbare en gedeelde operaties. Je gaat van het wegen van kwaliteit naar het bewaken van de poort.
