"""Testsuite bij de verwijder-uitbreiding.

De suite is groen: verwijderen doet wat is gebouwd. De tests leggen het gedrag
vast, ook het onomkeerbare deel: een boek met een openstaande wachtlijst wordt
zonder waarschuwing gewist. Of dat zo mag, is geen testvraag maar een
poort-beslissing.
"""

import pytest

from boekenplank import Boekenplank


def maak_plank() -> Boekenplank:
    plank = Boekenplank()
    plank.toevoegen("Dune", "Frank Herbert")
    plank.toevoegen("Neuromancer", "William Gibson")
    return plank


def test_verwijderen_haalt_boek_van_de_plank():
    plank = maak_plank()
    plank.verwijderen(1)
    with pytest.raises(KeyError):
        plank.boek(1)


def test_verwijderen_wist_ook_een_openstaande_wachtlijst():
    plank = maak_plank()
    plank.uitlenen(1, "Misja")
    plank.reserveren(1, "Bob")
    plank.verwijderen(1)
    assert [b.nummer for b in plank.lijst()] == [2]


def test_overige_boeken_blijven_ongemoeid():
    plank = maak_plank()
    plank.verwijderen(1)
    assert plank.boek(2).titel == "Neuromancer"
