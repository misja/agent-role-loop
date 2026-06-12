# Sphinx-configuratie voor het lesmateriaal (teaching/).
# Bron is MyST Markdown (D4), thema furo (Q2), taal Nederlands (D3).

project = "Agent Role Loop"
author = "Misja Hoebe"
copyright = "2026, Misja Hoebe - CC BY-NC-SA 4.0"

extensions = ["myst_parser"]

source_suffix = {".md": "markdown"}
master_doc = "index"
language = "nl"

# _toetsing is in deze fase een lege placeholder en bouwt niet mee.
exclude_patterns = ["_build", "_toetsing"]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

html_theme = "furo"
html_title = "Agent Role Loop - lesmateriaal"
