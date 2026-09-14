"""Maak de vaste downloadbundel uit de bronbestanden, zonder caches/werkbestanden."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parent.parent
CASE = ROOT / "teaching/cases/praktijk-projectomgeving"
DEST = ROOT / "teaching/praktijk/boekenplank-projectomgeving.zip"
FILES = [
    "README.md", "overdrachten.md", "overdrachtregister.csv", "bewijs.txt",
    "boekenplank_basis.py", "boekenplank_a.py", "boekenplank_b.py", "controleer.py",
    "basis-naar-a.patch", "a-naar-b.patch",
]


def main():
    entries = {name: (CASE / name).read_bytes() for name in FILES}
    entries["LICENSE"] = (ROOT / "LICENSE").read_bytes()
    entries["HERKOMST.md"] = (
        "# Herkomst\n\n"
        "Bron: https://github.com/misja/agent-role-loop, werkitem #31.\n"
        "Bewerkt onderwijsvoorbeeld door Misja Hoebe met AI-ondersteuning.\n"
        "Licentie CC BY-NC-SA 4.0, zie LICENSE.\n"
        "Procesbasis: ae561f50a45ca42967e4687434cf0d2e8d4f5827; "
        "normen/core bevat de ongewijzigde core van die versie.\n"
        "A/B zijn leeslabels voor codebestanden, geen Git-commits. "
        "Lees overdrachten.md voor de scenario-status.\n"
    ).encode()
    # Gebruik de vastgelegde normversie, ook als de actieve core later verandert.
    import subprocess
    basis = "ae561f50a45ca42967e4687434cf0d2e8d4f5827"
    paths = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", basis, "core"], cwd=ROOT, text=True
    ).splitlines()
    for path in paths:
        entries["normen/" + path] = subprocess.check_output(
            ["git", "show", f"{basis}:{path}"], cwd=ROOT
        )
    with ZipFile(DEST, "w", compression=ZIP_DEFLATED) as archive:
        for name, data in sorted(entries.items()):
            info = ZipInfo(name, date_time=(2026, 9, 14, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    print(f"{len(entries)} bestanden in {DEST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
