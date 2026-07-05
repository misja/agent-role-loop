"""Boekenplank met een onomkeerbare operatie voor module 5 (worked example).

Een door AI gebouwde uitbreiding: verwijderen. De operatie werkt en de tests
slagen. Het gaat in deze module niet om de kwaliteit van de code, maar om de
poort-beslissing: mag deze onomkeerbare operatie zo door? verwijderen wist een
boek en zijn wachtlijst definitief. Er is geen bevestiging, geen archief, geen
weg terug, ook niet als er nog reserveringen openstaan.
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

    def verwijderen(self, nummer: int) -> None:
        # Onomkeerbaar. Het boek en zijn wachtlijst verdwijnen definitief, ook als
        # er nog mensen op de wachtlijst staan. Geen bevestiging, geen archief.
        boek = self.boek(nummer)
        self._boeken.remove(boek)
