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
import locale
locale.setlocale(locale.LC_TIME, 'en_US.utf8')
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import shutil
import subprocess
from datetime import datetime
from setup import get_info
from typing import Any
from typing import Dict

__company__ = get_info('lbh15/__init__.py', 'company')
__author__ = get_info('lbh15/__init__.py', 'author')
__version__ = get_info('lbh15/__init__.py', 'version')
__date__ = get_info('lbh15/__init__.py', 'date')

#####################
# Project Information
#####################

project = 'lbh15'
copyright = '2022, ' + __company__
author = __author__

# The short X.Y version
version = str(__version__)
# The full version, including alpha/beta/rc tags
release = str(__version__)

# Tex documentation template
# Alternatives:
# . 'manual' ==> report-style
# . 'nwcldocs' ==> newcleo corporate-style (proprietary)
latex_theme_to_use = 'manual'
# Tex documentation title
title = 'lbh15: collection of properties from \
the lead-bismuth eutectic alloy and lead OECD/NEA handbook'
# Entries for "nwcldocs" template only
id_nwcldocs = '1000yyy' # ID Number
ref_code_nwcldocs = 'XXX-YYY-ZZZ-???' # Reference Code
rev_nwcldocs = '0' # Revision Number
mod_pages_nwcldocs = 'All'
mod_desc_nwcldocs = 'First Release'
abstract = 'This document is the reference manual for the \
\\sphinxstyleemphasis{lbh15} (\\sphinxstylestrong{L}ead \
\\sphinxstylestrong{B}ismuth \\sphinxstylestrong{H}andbook \
20\\sphinxstylestrong{15}) Python package, that implements the \
thermo\\sphinxhyphen{}physical and the thermo\\sphinxhyphen{}chemical \
properties of lead, bismuth and lead\\sphinxhyphen{}bismuth eutectic \
(lbe) metal alloy available from the handbook edited by OECD/NEA \
{[}\\hyperlink{cite.source/bibliography:id2}{1}{]}.'
authors_for_latex = 'Daniele Panico, , , , Gabriele Ottino, , , , '
reviewers_for_latex = 'Pierre-Alexandre Pantel, , , '
approvers_for_latex = 'Daniele Tomatis, , , '

###########################
# Project Information Ended
###########################

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
math_numfig = True

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

html_css_files = [os.path.join('css', 'theme.css'),
                  os.path.join('css', 'eqno.css')]

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

# List of folders where latex templates are placed
templates_path = ['_templates']

# Mapping of the available latex docclasses
latex_docclass = {
    'manual': 'report',
    'nwcldocs': 'nwcldocs'
}

#############################
# Setup for "manual" template
latex_theme = 'manual'
latex_elements: Dict[str, Any] = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
    'extrapackages': r'\input{../../_templates/extra_manual.texsty}',
    'makeindex': '\\usepackage[columns=1]{idxlayout}\\makeindex',
    'figure_align': 'tbp',
}
latex_authors = author

##########################################
# Settings to use with "nwcldocs" template
extrapackages_nwcldocs = r'\input{../../_templates/extra_nwcl.texsty}'
preamble_nwcldocs = r'\input{../../_templates/preamble_nwcl.texsty}'
makeindex_nwcldocs = '\\usepackage[columns=1,totoc]{idxlayout}\\makeindex'
date_list = __date__.split(' ')
from datetime import datetime
date_nwcldocs = date_list[0] + "/" + \
    str(datetime.strptime(date_list[1], '%B').month) + "/" + date_list[2]
atendofbody_nwcldocs = {
    'id': id_nwcldocs,
    'ref_code': ref_code_nwcldocs,
    'rev': rev_nwcldocs,
    'abstract': abstract,
    'date': date_nwcldocs,
    'pages': mod_pages_nwcldocs,
    'desc': mod_desc_nwcldocs,
    'reviewers': '\\break '.join(str(item) for item
                                 in reviewers_for_latex.split(", ")),
    'approvers': '\\break '.join(str(item) for item
                                 in approvers_for_latex.split(", "))
}

# Check the availability of the theme and set it accordingly
if latex_theme_to_use == 'nwcldocs':
    if shutil.which('kpsewhich'):
        check = subprocess.run(["kpsewhich", "nwcldocs.cls"],
                               stdout=subprocess.PIPE, text=True)
        if not check.stdout:
            raise RuntimeError("'nwcldocs.cls' tex class not found!\n"
                               "PDF file cannot be generated!\n Please change "
                               "document class to use and try again!")
        else:
            latex_theme = 'nwcldocs'
            latex_toplevel_sectioning = 'section'
            latex_elements.pop('papersize', None)
            latex_elements['classoptions'] = 'techdoc'
            latex_elements['extrapackages'] = extrapackages_nwcldocs
            latex_elements['preamble'] = preamble_nwcldocs
            latex_elements['makeindex'] = makeindex_nwcldocs
            latex_elements['atendofbody'] = atendofbody_nwcldocs
            latex_elements['sphinxsetup'] = 'TitleColor={named}{black}'
            latex_authors = '\\break '.join(str(item) for item
                                           in authors_for_latex.split(", "))
    else:
        raise RuntimeError("No tex environment found!\n"
                           "PDF file cannot be generated!\n Please change "
                           "document class to use and try again!")
elif latex_theme_to_use != 'manual':
    raise RuntimeError("Only 'manual' and 'nwcldocs' document classes are "
                       f"allowed, while '{latex_theme_to_use}' has been "
                       "provided!\n Please change document class to use "
                       "and try again!")

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
# author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'lbh15.tex', title,
     latex_authors, latex_theme),
]

latex_logo = html_logo
