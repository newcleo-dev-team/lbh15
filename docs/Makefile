# Minimal makefile for Sphinx documentation
#
# You can set these variables from the command line, and also
# from the environment for the first two.
PROJECT = lbh15
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build
NWCLBUILD     = ./build_nwcl_tmpl
SOURCELATEX = latex
TEXFILE = $(PROJECT).tex

### Fill the table revision history:
REV_N=1
DATE="See signature"
PAGES="All"
DESCR="First release"

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean:
	@rm -rf $(BUILDDIR)

.PHONY: help Makefile latexpdf_nwcl

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


latexpdf_nwcl:
	@$(SPHINXBUILD) -M latex "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	#@$(SPHINXBUILD) -b  latex "$(SOURCEDIR)" "$(BUILDDIR)/latex" "$(ALLSPHINXOPTS)"
	$(shell) ${NWCLBUILD} ${BUILDDIR} ${SOURCELATEX} ${TEXFILE} ${REV_N} ${DATE} ${PAGES} ${DESCR}
	$(MAKE) -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/$(SOURCELATEX)"

