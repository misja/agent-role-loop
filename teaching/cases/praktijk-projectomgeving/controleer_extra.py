"""Aanvullende controles: python3 -B controleer_extra.py b.

Alleen standaardbibliotheek. Een falende controle geeft exitcode 1.
Deze suite wijzigt de oorspronkelijke S1-S4-controles niet.
"""
import argparse
from pathlib import Path
import unittest

from controleer import laad


def toestand(boeken):
    return [(b.nummer, b.titel, b.uitgeleend_aan) for b in boeken]


def controles(Boekenplank):
    class Criteria(unittest.TestCase):
        def maak(self, leners=(None, "Noor", None)):
            plank = Boekenplank()
            for titel, lener in zip(("Zee", "Atlas", "Bos"), leners):
                plank.toevoegen(titel, lener)
            return plank

        def test_e1_false_is_standaard(self):
            for leners in ((None, "Noor", None), (), ("Noor", "Sam", "Ali")):
                with self.subTest(leners=leners):
                    plank = self.maak(leners)
                    standaard = plank.lijst()
                    expliciet = plank.lijst(alleen_beschikbaar=False)
                    verwacht = list(zip(range(1, len(leners) + 1),
                                        ("Zee", "Atlas", "Bos"), leners))
                    self.assertEqual(toestand(standaard), verwacht)
                    self.assertEqual(toestand(expliciet), verwacht)
                    for eerste, tweede in zip(standaard, expliciet):
                        self.assertIs(eerste, tweede)

        def test_e2_containers_veranderen_geen_opslag(self):
            for argumenten in ({}, {"alleen_beschikbaar": False},
                               {"alleen_beschikbaar": True}):
                for actie in ("clear", "append", "pop"):
                    with self.subTest(argumenten=argumenten, actie=actie):
                        plank = self.maak()
                        voor = toestand(plank.lijst())
                        resultaat = plank.lijst(**argumenten)
                        # Controleer filterbehoud voordat de container wordt gewijzigd.
                        self.assertEqual(toestand(plank.lijst()), voor)
                        if actie == "append":
                            resultaat.append(None)
                        else:
                            getattr(resultaat, actie)()
                        self.assertEqual(toestand(plank.lijst()), voor)
                        self.assertEqual(toestand(plank.lijst(alleen_beschikbaar=True)),
                                         [voor[0], voor[2]])
                        self.assertEqual(toestand(plank.lijst()), voor)

        def test_e3_toevoegen_na_filteren(self):
            plank = self.maak()
            voor = plank.lijst()
            plank.lijst(alleen_beschikbaar=True)
            nieuw = plank.toevoegen("Duin")
            na = plank.lijst()
            self.assertEqual(toestand(na),
                             [(1, "Zee", None), (2, "Atlas", "Noor"),
                              (3, "Bos", None), (4, "Duin", None)])
            self.assertEqual(len({b.nummer for b in na}), len(na))
            for eerste, tweede in zip(voor, na):
                self.assertIs(eerste, tweede)
            self.assertIs(na[-1], nieuw)
            self.assertEqual(toestand(plank.lijst(alleen_beschikbaar=True)),
                             [(1, "Zee", None), (3, "Bos", None), (4, "Duin", None)])
            self.assertEqual(toestand(plank.lijst()), toestand(na))
    return Criteria


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("versie", choices=["a", "b", "werk"])
    args = parser.parse_args()
    bestand = "boekenplank.py" if args.versie == "werk" else f"boekenplank_{args.versie}.py"
    tests = controles(laad(Path(__file__).parent / bestand))
    resultaat = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(tests))
    return 0 if resultaat.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
