# Sphinx-configuratie voor het lesmateriaal (teaching/).
# Bron is MyST Markdown (D4), thema furo (Q2), taal Nederlands (D3).

project = "Agent Role Loop"
author = "Misja Hoebe"
copyright = "2026, Misja Hoebe - CC BY-NC-SA 4.0"

extensions = ["myst_parser", "sphinx.ext.extlinks"]

# Migratiescharnier: bestandsverwijzingen vanuit teaching/ naar core/ worden
# klikbare links naar de Engelse bronbestanden in de repository. core/ blijft
# bewust buiten de build (vendor-neutraal). Een verhuizing van de hosting of een
# latere overstap naar interne links is een wijziging van deze ene regel.
CORE_BASE_URL = "https://github.com/misja/agent-role-loop/blob/main/core/"
extlinks = {"core": (CORE_BASE_URL + "%s", "core/%s")}

source_suffix = {".md": "markdown"}
master_doc = "index"
language = "nl"

# Buiten de build: _toetsing is een lege placeholder; cases bevat code-artefacten
# (worked examples) die net als core/ geen site-document zijn en waarnaar de lessen
# als inline pad verwijzen; het werkitem-template is pure projectinfrastructuur.
# conventies.md bouwt wel mee maar staat bewust niet in de navigatie-toctree: het
# is als orphan gemarkeerd (front matter), dus rendert en is aanlinkbaar.
exclude_patterns = ["_build", "_toetsing", "cases", "_werkitem-template.md"]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

html_theme = "furo"
html_title = "Agent Role Loop - lesmateriaal"
