# Worked example: een AI-gebouwde reserveringen-uitbreiding

Dit voorbeeld hoort bij module 4 (Oordelen). Het is een door AI gebouwde
uitbreiding van de boekenplank: reserveren en een wachtlijst. De code werkt en de
tests slagen.

In deze module gaat het niet om verstopte fouten. Je beoordeelt een uitbreiding
die *werkt*, maar die ontwerpkeuzes maakt waarover redelijke mensen het oneens
kunnen zijn. Je kijkt ernaar vanuit vier perspectieven (strikt, pragmatisch,
adversarieel, onderhoudbaarheid) en velt een onderbouwd oordeel.

## Wat is gebouwd

- `reserveren <nummer> <naam>` reserveert een boek.
- Reserveren van een beschikbaar boek leent het meteen uit.
- Reserveren van een uitgeleend boek zet je op de wachtlijst van dat boek.
- `terug` leent het boek meteen uit aan de eerste op de wachtlijst.
- Er is geen vervaltermijn; de wachtlijst is een lijst met namen.

## Draaien

Je hebt `pytest` nodig.

```
pytest
```

Alle tests slagen. De opdracht, de vier perspectieven en de vragen staan in
oefening 4.
