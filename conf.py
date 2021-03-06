# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'SAPP'
copyright = '2021, sehé, 002, chaoticzeros'
author = 'sehé, 002'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_copybutton',
    'sphinxcontrib.email'
]

copybutton_prompt_text = "> "

email_automode = True


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    "external_links": [
        {"url": "http://halo.isimaginary.com/SAPP%20Documentation%20Revision%202.5.pdf", "name": "PDF Docs"}
    ],
    "github_url": "https://github.com/chaoticzeros/halo-sapp-docs",

    "use_edit_page_button": True,
    "show_toc_level": 1,
    # "search_bar_position": "navbar",  # TODO: Deprecated - remove in future version
    # "navbar_align": "left",  # [left, content, right] For testing that the navbar items align properly
    # "navbar_start": ["navbar-logo", "navbar-version"],
    # "navbar_center": ["navbar-nav", "navbar-version"],  # Just for testing
    # "navbar_end": ["navbar-icon-links", "navbar-version"]  # Just for testing
    # "footer_items": ["copyright", "sphinx-version", ""]

    "collapse_navigation": True,
    "navigation_depth": 2,
    "show_prev_next": False,
    "google_analytics_id": "G-7XFJK42838",
    
}


html_context = {
    "github_user": "chaoticzeros",
    "github_repo": "halo-sapp-docs",
    "github_version": "master",
    # "doc_path": ".",
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

highlight_language = 'text'