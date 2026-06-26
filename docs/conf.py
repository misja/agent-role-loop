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

# _toetsing is in deze fase een lege placeholder en bouwt niet mee. cases bevat
# code-artefacten (worked examples) die geen site-document zijn: code blijft net
# als core/ buiten de build, en de lessen verwijzen ernaar als inline pad.
exclude_patterns = ["_build", "_toetsing", "cases"]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

html_theme = "furo"
html_title = "Agent Role Loop - lesmateriaal"
