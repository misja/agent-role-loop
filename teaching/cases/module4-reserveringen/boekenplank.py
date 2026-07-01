"""Boekenplank met reserveringen voor module 4 (worked example).

Een door AI gebouwde uitbreiding van de boekenplank: reserveren en een wachtlijst.
De code werkt en de tests slagen. In deze module gaat het niet om verstopte
fouten, maar om verdedigbare ontwerpkeuzes die botsen. Vier beoordelaars kunnen
het er oneens over zijn zonder dat de code simpelweg fout is.

De keuzes die je zult tegenkomen zijn met opzet betwistbaar, niet verkeerd:
reserveren van een beschikbaar boek leent het meteen uit; terugbrengen leent
meteen uit aan de eerste op de wachtlijst; er is geen vervaltermijn; en de
wachtlijst is een lijst met namen.
"""

from dataclasses import dataclass, field


@dataclass
class Boek:
    nummer: int
    titel: str
    auteur: str
    uitgeleend_aan: str | None = None
    wachtlijst: list[str] = field(default_factory=list)

    @property
    def is_uitgeleend(self) -> bool:
        return self.uitgeleend_aan is not None


class Boekenplank:
    def __init__(self) -> None:
        self._boeken: list[Boek] = []

    def toevoegen(self, titel: str, auteur: str) -> Boek:
        boek = Boek(nummer=len(self._boeken) + 1, titel=titel, auteur=auteur)
        self._boeken.append(boek)
        return boek

    def lijst(self) -> list[Boek]:
        return list(self._boeken)

    def boek(self, nummer: int) -> Boek:
        for boek in self._boeken:
            if boek.nummer == nummer:
                return boek
        raise KeyError(f"geen boek met nummer {nummer}")

    def uitlenen(self, nummer: int, naam: str) -> None:
        boek = self.boek(nummer)
        if boek.is_uitgeleend:
            raise ValueError(f"boek {nummer} is al uitgeleend")
        boek.uitgeleend_aan = naam

    def reserveren(self, nummer: int, naam: str) -> None:
        boek = self.boek(nummer)
        if not boek.is_uitgeleend:
            boek.uitgeleend_aan = naam
            return
        boek.wachtlijst.append(naam)

    def terug(self, nummer: int) -> None:
        boek = self.boek(nummer)
        boek.uitgeleend_aan = None
        if boek.wachtlijst:
            boek.uitgeleend_aan = boek.wachtlijst.pop(0)
