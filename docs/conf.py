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
from setup import get_info

__company__ = get_info('lbh15/__init__.py', 'company')
__author__ = get_info('lbh15/__init__.py', 'author')
__version__ = get_info('lbh15/__init__.py', 'version')

# -- Project information -----------------------------------------------------

project = 'lbh15'
copyright = '2022, ' + __company__
author = __author__

# The short X.Y version
version = str(__version__)
# The full version, including alpha/beta/rc tags
release = str(__version__)


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

autodoc_mock_imports = ["numpy", "scipy"]

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
exclude_patterns = [
    'source/learn_more.rst'
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'navigation_depth': 5,
}

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

title = 'lbh15: collection of properties from\
    the lead-bismuth eutectic alloy and lead OECD/NEA handbook'

abstract = 'This document is the reference manual for the \
\\sphinxstyleemphasis{lbh15} (\\sphinxstylestrong{L}ead \
\\sphinxstylestrong{B}ismuth \\sphinxstylestrong{H}andbook \
20\\sphinxstylestrong{15}) Python package, that implements the \
thermo\\sphinxhyphen{}physical and the thermo\\sphinxhyphen{}chemical \
properties of lead, bismuth and lead\\sphinxhyphen{}bismuth eutectic \
(lbe) metal alloy available from the handbook edited by OECD/NEA \
{[}\\hyperlink{cite.source/bibliography:id2}{1}{]}:\\sphinxhref{https://www.oecd-nea.org/jcms/pl\\_14972/handbook-on-lead-bismuth-eutectic-alloy-and-lead-properties-materials-compatibility-thermal-hydraulics-and-technologies-2015-edition?details=true}{oecd\\sphinxhyphen{}nea.org}.'

templates_path = ['_templates']

latex_theme = 'nwcldocs'

latex_docclass = {
    'nwcldocs': 'nwcldcs',
}

# verificare che ci sia il file nwcldocs.cls

latex_elements = {

    'classoptions': 'techdoc',

    # The paper size ('letterpaper' or 'a4paper').

#    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').

    'pointsize': '11pt',

    'extrapackages': r'''
\usepackage[title,titletoc]{appendix}
\usepackage{caption}
''',

    # Additional stuff for the LaTeX preamble.

    'preamble': r'''
\date{}

\newlist{packagelist}{description}{1}
\setlist[packagelist]{itemsep=1pt,labelwidth=3cm,align=right,
  font={\color{purple}\bfseries},
  before={\color{indigo}{\itshape}}
}

\renewcommand{\hyperref}[2][]{#2}
''',
# \newcommand{\chapter}[1]{\section{}{#1}}

    'makeindex': '\\usepackage[columns=1]{idxlayout}\\makeindex',

    # Latex figure (float) alignment

    'figure_align': 'tbp',

    # Abused keywords
    'atendofbody': abstract, # Used for defining the abstract contents
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
# author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'lbh15.tex', title,
     __author__, 'nwcldocs'),
]

latex_logo = html_logo
