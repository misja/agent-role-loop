"""Een minimale boekenplank voor module 3 (worked example).

Bewust klein gehouden: net genoeg om er tests en coverage op te draaien, niet
meer. Persistentie is weggelaten; het gaat hier om logica, niet om opslag.

Let op: in deze code zit een opzettelijk defect (zie README.md). De testsuite
ernaast is groen en haalt 100% regeldekking, en mist het defect toch. Dat is de
leerstof van de module: groen is noodzakelijk maar niet voldoende.
"""

from dataclasses import dataclass


@dataclass
class Boek:
    nummer: int
    titel: str
    auteur: str
    uitgeleend_aan: str | None = None

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
        # Defect: requirement 6 (een al uitgeleend boek kan niet nogmaals worden
        # uitgeleend) wordt hier niet gehandhaafd. Een tweede uitlening
        # overschrijft stilzwijgend de vorige lener.
        boek = self.boek(nummer)
        boek.uitgeleend_aan = naam

    def terug(self, nummer: int) -> None:
        boek = self.boek(nummer)
        boek.uitgeleend_aan = None
