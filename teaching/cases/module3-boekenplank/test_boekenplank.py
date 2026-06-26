"""Testsuite bij boekenplank.py.

Deze suite is groen en haalt 100% regeldekking. Toch laat ze een echt defect
ongemoeid. Eén test in het bijzonder lijkt requirement 6 te toetsen, maar de
assertie is te zwak: ze controleert dat het boek uitgeleend is, niet dat de
tweede uitlening geweigerd werd. Het opsporen van dat gat is de opdracht.
"""

import pytest

from boekenplank import Boekenplank


def maak_plank() -> Boekenplank:
    plank = Boekenplank()
    plank.toevoegen("Dune", "Frank Herbert")
    plank.toevoegen("Neuromancer", "William Gibson")
    return plank


def test_toevoegen_geeft_oplopende_nummers():
    plank = maak_plank()
    nummers = [b.nummer for b in plank.lijst()]
    assert nummers == [1, 2]


def test_lijst_toont_alle_boeken():
    plank = maak_plank()
    assert len(plank.lijst()) == 2


def test_uitlenen_zet_boek_op_uitgeleend():
    plank = maak_plank()
    plank.uitlenen(1, "Misja")
    assert plank.boek(1).is_uitgeleend


def test_terug_maakt_boek_weer_beschikbaar():
    plank = maak_plank()
    plank.uitlenen(1, "Misja")
    plank.terug(1)
    assert not plank.boek(1).is_uitgeleend


def test_onbekend_nummer_geeft_fout():
    plank = maak_plank()
    with pytest.raises(KeyError):
        plank.boek(99)


def test_uitlenen_voorkomt_dubbele_uitlening():
    """Lijkt requirement 6 te toetsen, maar de assertie is te zwak."""
    plank = maak_plank()
    plank.uitlenen(1, "Misja")
    plank.uitlenen(1, "Bob")  # zou geweigerd moeten worden
    assert plank.boek(1).is_uitgeleend  # nog steeds uitgeleend, dus groen
