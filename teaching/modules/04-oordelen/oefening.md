# Oefening 4 - Beoordeel een AI-gebouwde uitbreiding vanuit vier perspectieven

In module 3 zocht je de plek waar een groene poort niets bewees. Nu oordeel je zelf. Je beoordeelt een door AI gebouwde reserveringen-uitbreiding van de boekenplank die werkt en groen is, maar ontwerpkeuzes maakt waarover je het oneens kunt zijn. Je neemt de vier beoordelaarsrollen in en prioriteert tot één eindoordeel.

**Duur:** circa 90 minuten.
**Nodig:** het materiaal in `teaching/cases/module4-reserveringen/` uit de repository, met `pytest`. De vier beoordelaarsrollen onder `core/roles/` en de contracten C6 en C7.
**Inleveren:** je oordelen (C6) per perspectief, je eindoordeel (C7) met prioritering, en de beantwoorde verantwoordingsvragen.

## Worked example: twee perspectieven voorgedaan

Draai eerst de tests, zodat je ziet dat de uitbreiding werkt:

```
pytest
```

Alles slaagt. We beoordelen nu dezelfde werkende code vanuit twee perspectieven.

**Adversarieel.** Reserveren van een beschikbaar boek leent het stil uit in plaats van te reserveren; wie "reserveren" typt, verwacht misschien geen uitlening. De wachtlijst vervalt nooit: reserveer een boek en haal het nooit op, dan blijft de rij groeien en blokkeert de reservering het boek. En verwijder je een boek met een wachtlijst, dan is onduidelijk wat er met de rij gebeurt. Geen van deze is een crash; het zijn niet-afgevangen situaties die je zou willen bespreken.

**Onderhoudbaarheid.** `terug` doet nu twee dingen: het boek teruggeven en het meteen opnieuw uitlenen aan de eerste op de wachtlijst. Wie later `terug` leest, verwacht dat niet. De wachtlijst is verstrengeld met het uitlenen in plaats van een eigen zorg, en namen dienen als identiteit (twee mensen die "Bob" heten zijn niet te onderscheiden). Dit werkt, maar het maakt de volgende wijziging lastiger.

Merk op: allebei de perspectieven wegen keuzes, geen fouten. De pragmatische beoordelaar zou een deel hiervan verdedigen.

## Jouw opdracht: de andere twee perspectieven en de synthese

1. Schrijf een oordeel (C6, volg {core}`contracts/reviewer-verdict.md`) vanuit de **strikte** beoordelaar: welke ambiguïteiten in de opdracht moeten worden gepind voordat dit af is?
2. Schrijf een oordeel (C6) vanuit de **pragmatische** beoordelaar: wat is goed genoeg voor nu, en welke van de bezwaren hierboven zou je bewust laten liggen?
3. Schrijf het eindoordeel (C7, volg {core}`contracts/final-verdict.md`) als **hoofdbeoordelaar**. Los de spanning niet op door één perspectief te laten winnen, maar prioriteer expliciet: correctheid en veiligheid eerst, dan onderhoudbaarheid, dan afwerking. Verantwoord welke bevindingen must-fix zijn en welke kunnen wachten, en waarom.

## Verantwoordingsvragen

Beantwoord schriftelijk:

1. **Beargumenteer** waarom deze uitbreiding niet fout is en toch verbeterd kan worden. Wat zegt dat over kwaliteit in de oordeelslaag?
2. Twee beoordelaars spreken elkaar tegen over dezelfde keuze (bijvoorbeeld de wachtlijst zonder vervaltermijn). **Verantwoord** welke je zwaarder laat wegen en waarom.
3. **Verantwoord** je prioritering in de C7. Waarom is prioriteren iets anders dan de vier oordelen naast elkaar leggen, en waar zat voor jou de moeilijkste afweging?

## Variant zonder AI

Speel de vier beoordelaars met vier studenten die elk afzonderlijk, zonder overleg, hun C6 schrijven op dezelfde uitbreiding; een vijfde is hoofdbeoordelaar en schrijft de C7. De debriefing draait om waar de oordelen botsten en hoe de prioritering dat besliste.
