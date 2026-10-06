"""Voer de voorbeeldcontroles uit: python controleer.py a zwak.

Standaardbibliotheek; geen pytest of internet nodig. Een falende controle
geeft exitcode 1. De fout in versie A is opzettelijk geconstrueerd.
"""
import argparse
import importlib.util
from pathlib import Path
import sys
import unittest


def laad(pad):
    spec = importlib.util.spec_from_file_location("voorbeeld", pad)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.Boekenplank


def controles(Boekenplank):
    class Criteria(unittest.TestCase):
        def maak(self):
            plank = Boekenplank()
            plank.toevoegen("Zee")
            plank.toevoegen("Atlas", "Noor")
            plank.toevoegen("Bos")
            return plank

        def test_s1_standaard_volgorde(self):
            self.assertEqual([b.nummer for b in self.maak().lijst()], [1, 2, 3])

        def test_s2_beschikbaar_in_volgorde(self):
            boeken = self.maak().lijst(alleen_beschikbaar=True)
            self.assertEqual([b.nummer for b in boeken], [1, 3])

        def test_s3_leeg_of_alles_uitgeleend(self):
            plank = Boekenplank()
            self.assertEqual(plank.lijst(alleen_beschikbaar=True), [])
            plank.toevoegen("Atlas", "Noor")
            self.assertEqual(plank.lijst(alleen_beschikbaar=True), [])

        def test_s4_filter_verandert_geen_toestand(self):
            plank = self.maak()
            voor = [(b.nummer, b.titel, b.uitgeleend_aan) for b in plank.lijst()]
            plank.lijst(alleen_beschikbaar=True)
            na = [(b.nummer, b.titel, b.uitgeleend_aan) for b in plank.lijst()]
            self.assertEqual(na, voor)
    return Criteria


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("versie", choices=["basis", "a", "b", "werk"])
    parser.add_argument("suite", choices=["basis", "zwak", "regressie", "volledig"])
    args = parser.parse_args()
    bestand = "boekenplank.py" if args.versie == "werk" else f"boekenplank_{args.versie}.py"
    tests = controles(laad(Path(__file__).parent / bestand))
    namen = unittest.defaultTestLoader.getTestCaseNames(tests)
    if args.suite == "basis":
        namen = [n for n in namen if n.startswith("test_s1")]
    elif args.suite == "zwak":
        namen = [n for n in namen if not n.startswith("test_s4")]
    elif args.suite == "regressie":
        namen = [n for n in namen if n.startswith("test_s4")]
    resultaat = unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(tests(n) for n in namen))
    return 0 if resultaat.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
