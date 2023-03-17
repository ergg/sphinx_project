# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import re
sys.path.insert(0, os.path.abspath('..'))

from sphinx_rtd_theme import __version__ as theme_version
from sphinx_rtd_theme import __version_full__ as theme_version_full
from sphinx.locale import _

project = 'sphinx_project'
copyright = '2023, Erich Geiger'
author = 'Erich Geiger'
release = '0.0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    'rtd': ('https://docs.readthedocs.io/en/stable/', None),
    'rtd-dev': ('https://dev.readthedocs.io/en/stable/', None),
}

# intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
RTD_NEW_THEME = True
html_theme_options = {
    'logo_only': True,
    'navigation_depth': 5,
}
html_context = {}

# html_static_path = ['_static']
# html_css_files = ['css/custom.css']
# html_logo = '_static/logo.png'
# html_favicon = "_static/favicon.ico"

html_theme_options = {
    'logo_only': False,
    'display_version': False,  # False so doc version not shown
    'prev_next_buttons_location': 'both',  # Can be bottom, top, both , or None
    'style_external_links': True,  # True to Add an icon next to external links
    'style_nav_header_background': 'linear-gradientlinear-gradient(to right, blueviolet 15%, limegreen 50%, royalblue 80%)',  # blue
    # Toc options
    'collapse_navigation': False,  # False so nav entries have the [+] icons
    'sticky_navigation': False,  # False so the nav does not scroll
    'navigation_depth': 4,  # -1 for no limit
    'includehidden': True,  # displays toctree that are hidden
    'titles_only': False  # False so page subheadings are in the nav.
}

# Grouping the document tree into LaTeX files. List of tuples# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
 ('index', 'yourdoc.tex', u'DocName', u'YourName', 'manual'),
]

# Make pdf nice
# maxlistdepth 6 -> Otherwise Latex is generating error when a pdf is created Erich 2023-03-16
## latex_elements = {
##    'maxlistdepth' : '6',
# The paper size ('letterpaper' or 'a4paper').
##    'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
##    'pointsize': '11pt',

# Additional stuff for the LaTeX preamble.
##    'preamble': r'''
##        \usepackage{charter}
##        \usepackage[defaultsans]{lato}
##        \usepackage{inconsolata}
##    ''',
##}

#    'extraclassoptions': 'openany,oneside',
# \usepackage[titles]{tocloft}
#\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
#\setlength{\cftchapnumwidth}{0.75cm}
#\setlength{\cftsecindent}{\cftchapnumwidth}
#\setlength{\cftsecnumwidth}{1.25cm}

#\usepackage{xcolor,colortbl}
#\arrayrulecolor{red}

#\usepackage[titles]{tocloft}
#\documentclass{ltxdoc}

#\usepackage[titles]{tocloft}

latex_engine = 'xelatex'
latex_elements = {
    'extraclassoptions': 'openany',
    'maxlistdepth' : '6',
    'fontpkg': r'''
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
''',
    'preamble': r'''
\usepackage{fancyhdr}
\pagestyle{fancy}
\setcounter{secnumdepth}{1}
\setcounter{tocdepth}{1}

\usepackage{tocloft}
\addtocontents{toc}{\protect\thispagestyle{fancy}}
''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
}
latex_show_urls = 'footnote'
