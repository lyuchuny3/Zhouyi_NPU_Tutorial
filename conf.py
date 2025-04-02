# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath("/home/chulv01/chulv01/gbuilder/python/src/"))

project = 'Zhouyi NPU Documentation'
copyright = '2025, Zhouyi NPU Team'
author = 'Zhouyi NPU Team'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    "sphinx_markdown_tables",
    # "sphinx.ext.autodoc",
    "recommonmark",
    # "myst_parser",
]
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
templates_path = ["_templates"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# -- Options for other extensions --------------------------------------------
# myst_heading_anchors = 3
# autodoc_class_signature = "separated"
# autodoc_member_order = "bysource"
