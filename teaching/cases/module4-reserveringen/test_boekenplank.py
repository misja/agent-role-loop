"""Testsuite bij de reserveringen-uitbreiding.

De suite is groen: de code doet consistent wat is gebouwd. De tests leggen het
gedrag vast, niet of de ontwerpkeuzes de beste zijn. Dat oordeel is aan jou.
"""

import pytest

from boekenplank import Boekenplank


def maak_plank() -> Boekenplank:
    plank = Boekenplank()
    plank.toevoegen("Dune", "Frank Herbert")
    plank.toevoegen("Neuromancer", "William Gibson")
    return plank


def test_reserveren_van_beschikbaar_boek_leent_meteen_uit():
    plank = maak_plank()
    plank.reserveren(1, "Misja")
    assert plank.boek(1).uitgeleend_aan == "Misja"
    assert plank.boek(1).wachtlijst == []


def test_reserveren_van_uitgeleend_boek_gaat_naar_wachtlijst():
    plank = maak_plank()
    plank.uitlenen(1, "Misja")
    plank.reserveren(1, "Bob")
    assert plank.boek(1).wachtlijst == ["Bob"]


def test_terug_leent_uit_aan_eerste_op_wachtlijst():
    plank = maak_plank()
    plank.uitlenen(1, "Misja")
    plank.reserveren(1, "Bob")
    plank.reserveren(1, "Carla")
    plank.terug(1)
    assert plank.boek(1).uitgeleend_aan == "Bob"
    assert plank.boek(1).wachtlijst == ["Carla"]


def test_terug_zonder_wachtlijst_maakt_boek_beschikbaar():
    plank = maak_plank()
    plank.uitlenen(1, "Misja")
    plank.terug(1)
    assert not plank.boek(1).is_uitgeleend


def test_uitlenen_van_uitgeleend_boek_wordt_geweigerd():
    plank = maak_plank()
    plank.uitlenen(1, "Misja")
    with pytest.raises(ValueError):
        plank.uitlenen(1, "Bob")
