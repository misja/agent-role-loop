"""Zelfstandig onderwijsvoorbeeld bij het praktijkhoofdstuk.

Dit is een bewerkte minimale boekenplank, geen volledige CLI of opslaglaag.
"""
from dataclasses import dataclass


@dataclass
class Boek:
    nummer: int
    titel: str
    uitgeleend_aan: str | None = None


class Boekenplank:
    def __init__(self):
        self._boeken = []

    def toevoegen(self, titel, uitgeleend_aan=None):
        boek = Boek(len(self._boeken) + 1, titel, uitgeleend_aan)
        self._boeken.append(boek)
        return boek

    def lijst(self, alleen_beschikbaar=False):
        if alleen_beschikbaar:
            return [b for b in self._boeken if b.uitgeleend_aan is None]
        return list(self._boeken)
