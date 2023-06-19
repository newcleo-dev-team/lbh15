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

.PHONY: help Makefile clean latexpdf_nwcl

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


latexpdf_nwcl:
	$(SPHINXBUILD) -b latex "$(SOURCEDIR)" "$(BUILDDIR)/latex" "$(ALLSPHINXOPTS)"
	@echo "Running LaTeX files through pdflatex..."
	sed -i 's/letterpaper/techdoc/g' $(BUILDDIR)/latex/lbh15.tex
	sed -i 's/sphinxhowto/nwcldocs/g' $(BUILDDIR)/latex/lbh15.tex
	sed -i 's/sphinxmanual/nwcldocs/g' $(BUILDDIR)/latex/lbh15.tex
	sed -i 's/\\pagestyle{empty}//g'  $(BUILDDIR)/latex/lbh15.tex
	sed -i 's/pagestyle{plain}/mkWorkflowTable/g' $(BUILDDIR)/latex/lbh15.tex
	sed -i 's/sphinxtableofcontents/mkDistributionList/g' $(BUILDDIR)/latex/lbh15.tex
	sed -i 's/pagestyle{normal}/newpage\n\\mkRevisionHistory\n\\newpage/' $(BUILDDIR)/latex/lbh15.tex
	sed -i 's/\\phantomsection\\label{\\detokenize{index::doc}}/\\tableofcontents\n\\newpage/'  $(BUILDDIR)/latex/lbh15.tex
	#sed -i -e '/\\phantomsection\\label{\\detokenize{index::doc}}/c \\tableofcontents\n\\newpage\n' $(BUILDDIR)/latex/lbh16.tex
	$(MAKE) -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

