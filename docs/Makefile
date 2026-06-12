# Build van de Sphinx-site uit teaching/ (bron) naar docs/_build (output).
# De build zelf is kale sphinx-build en daarmee platformonafhankelijk (D11);
# uv levert alleen de omgeving (D12). CI draait exact dit doel: make html.
# -W --keep-going: elke warning (incl. broken references) laat de build falen (AC1).

SPHINXBUILD ?= uv run --group docs sphinx-build
SOURCEDIR    = ../teaching
BUILDDIR     = _build

.PHONY: html clean

html:
	$(SPHINXBUILD) -b html -W --keep-going -c . "$(SOURCEDIR)" "$(BUILDDIR)"

clean:
	rm -rf "$(BUILDDIR)"
