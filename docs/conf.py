# Sphinx-configuratie voor het lesmateriaal (teaching/).
# Bron is MyST Markdown (D4), thema furo (Q2), taal Nederlands (D3).

import shutil
from pathlib import Path

from docutils import nodes
from sphinx import addnodes

project = "Agent Role Loop"
author = "Misja Hoebe"
copyright = "2026, Misja Hoebe - CC BY-NC-SA 4.0"

extensions = ["myst_parser", "sphinxcontrib.mermaid"]

# Mermaid rendert client-side (gate-keuze #21): geen node of headless browser in
# de build, D11/D12 blijven intact. De versie is expliciet gepind zodat het
# gedrag bij de lezer deterministisch is; het script komt van een CDN.
mermaid_version = "11.12.1"

# --- Referentiesectie: core/ gepubliceerd als onderdeel van de site. ---
# core/ zelf blijft vendor-neutraal en onaangeraakt. Bij elke build wordt het
# gekopieerd naar teaching/referentie/ (gegenereerd, gitignored); de staging
# wordt eerst leeggemaakt zodat bestanden die uit core/ verdwijnen geen wezen
# achterlaten. De dunne indexpagina's worden hier gegenereerd, buiten core/,
# en gebruiken glob zodat ze nooit uit de pas lopen met de inhoud van core/.
# De sync leeft in conf.py zodat kale sphinx-build (D11) de volledige site
# blijft produceren, zonder extra buildstappen of symlinks.

_DOCS = Path(__file__).resolve().parent
_CORE = _DOCS.parent / "core"
_STAGING = _DOCS.parent / "teaching" / "referentie"

_INDEX_TOP = """\
# Reference: roles and contracts

These are the English source files from the repository's `core/`, copied in at
build time. The index pages are generated, and links to directories are
redirected to them at copy time; the content is otherwise unchanged.

```{toctree}
:maxdepth: 1
:glob:

*
roles/index
contracts/index
```
"""

_INDEX_SUB = """\
# {title}

```{{toctree}}
:maxdepth: 1
:glob:

*
```
"""


# core/ linkt naar zijn mappen (roles/, contracts/); op GitHub is dat een
# mappenlijst, in de site is het doel de gegenereerde indexpagina. De sync
# herschrijft alleen die directory-links, uitsluitend in de staging.
_DIR_LINKS = {
    "](roles/)": "](roles/index.md)",
    "](contracts/)": "](contracts/index.md)",
    "](../roles/)": "](../roles/index.md)",
    "](../contracts/)": "](../contracts/index.md)",
}


def _sync_core() -> None:
    if _STAGING.exists():
        shutil.rmtree(_STAGING)
    shutil.copytree(_CORE, _STAGING)
    for md in _STAGING.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for old, new in _DIR_LINKS.items():
            text = text.replace(old, new)
        md.write_text(text, encoding="utf-8")
    (_STAGING / "index.md").write_text(_INDEX_TOP, encoding="utf-8")
    (_STAGING / "roles" / "index.md").write_text(
        _INDEX_SUB.format(title="Roles"), encoding="utf-8"
    )
    (_STAGING / "contracts" / "index.md").write_text(
        _INDEX_SUB.format(title="Contracts"), encoding="utf-8"
    )


_sync_core()

# Migratiescharnier, ingelost: de {core}-rol verwees via een externe base-URL
# (CORE_BASE_URL) naar de bronbestanden op GitHub; nu lost hij op naar interne
# pagina's in de referentiesectie. Alle teaching-teksten bleven daarbij
# ongewijzigd; alleen deze roldefinitie veranderde. Interne links zijn
# host-onafhankelijk, dus een hosting-verhuizing raakt ze niet meer.
# Een onvindbaar doel is een warning en laat de build falen (-W, AC1).


def _core_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    env = inliner.document.settings.env
    target = text[:-3] if text.endswith(".md") else text
    node = addnodes.pending_xref(
        rawtext,
        reftype="doc",
        refdomain="std",
        reftarget="/referentie/" + target,
        refdoc=env.docname,
        refexplicit=True,
        refwarn=True,
    )
    node += nodes.literal(rawtext, "core/" + text, classes=["xref", "doc"])
    return [node], []


def setup(app):
    app.add_role("core", _core_role)


source_suffix = {".md": "markdown"}
master_doc = "index"
language = "nl"

# Buiten de build: _toetsing is een lege placeholder; cases bevat code-artefacten
# (worked examples) die geen site-document zijn en waarnaar de lessen als inline
# pad verwijzen; het werkitem-template is pure projectinfrastructuur.
# conventies.md en schrijfwijzer.md bouwen wel mee maar staan bewust niet in de
# navigatie-toctree: het zijn docent- en projectdocumenten, als orphan gemarkeerd
# (front matter), dus ze renderen en zijn aanlinkbaar.
exclude_patterns = ["_build", "_toetsing", "cases", "_werkitem-template.md"]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

html_theme = "furo"
html_title = "Kwaliteit bewaken als AI bouwt"
