# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import lbh15

# -- Project information -----------------------------------------------------

project = 'lbh15'
copyright = '2022, ' + lbh15.__company__
author = lbh15.__author__

# The short X.Y version
version = str(lbh15.__version__)
# The full version, including alpha/beta/rc tags
release = str(lbh15.__version__)


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'myst_parser',
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.bibtex'
]

srcdir = 'source'
bibtex_bibfiles = [os.path.join(srcdir, 'lbh15.bib')]

# Make sure the target is unique
autosectionlabel_prefix_document = True

numfig = True

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
add_module_names = False

autodoc_mock_imports = []

autodoc_default_options = {
    'members': True,
    'special-members': '__call__',
}

autodoc_member_order = 'bysource'

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# The master toctree document.
master_doc = 'index'

language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [os.path.join(srcdir, '_static')]

html_css_files = [os.path.join(srcdir, 'css', 'theme.css')]

html_logo = os.path.join(srcdir, 'figures', 'newcleologo.png')

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'lbh15 documentation'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').

    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').

    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.

    'preamble': r'''
\renewcommand{\hyperref}[2][]{#2}
''',

    'makeindex': '\\usepackage[columns=1]{idxlayout}\\makeindex',

    # Latex figure (float) alignment

    'figure_align': 'tbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
# author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'lbh15.tex', 'lbh15: collection of properties from \
    the lead-bismuth eutectic alloy and lead OECD/NEA handbook',
     lbh15.__author__, 'manual'),
]

latex_logo = html_logo
