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
