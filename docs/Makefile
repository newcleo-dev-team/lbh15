# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean:
	-rm -rf $(BUILDDIR)

.PHONY: help Makefile clean latexpdf

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
#%: Makefile
#	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
latexpdf:
	$(SPHINXBUILD) -b latex "$(SOURCEDIR)" "$(BUILDDIR)/latex" "$(ALLSPHINXOPTS)"
	@echo "Running LaTeX files through pdflatex..."
	sed -i 's/sphinxhowto/nwcldocs/g' $(BUILDDIR)/latex/lbh15.tex
	sed -i 's/sphinxmanual/nwcldocs/g' $(BUILDDIR)/latex/lbh15.tex
	sed -i 's/\pagestyle{empty}//g' $(BUILDDIR)/latex/lbh15.tex
	sed -i 's/pagestyle{plain}/newpage/g' $(BUILDDIR)/latex/lbh15.tex
	sed -i 's/pagestyle{normal}/newpage/g' $(BUILDDIR)/latex/lbh15.tex
	$(MAKE) -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

