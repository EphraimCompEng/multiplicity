# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
import multipy as mp
sys.path.insert(0, os.path.abspath(os.path.join('..', '..', '..')))
print(sys.path)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MultiPy'
copyright = '2025, Ephraim Madugba'
author = 'Ephraim Madugba'
release = mp.MP_VERSION
stable = 'v' + ".".join(release.split('.')[:2])

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.apidoc','sphinx.ext.autodoc','sphinx.ext.viewcode']

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Exposing variables to .rst files ----------------------------------------
# https://stackoverflow.com/a/69211912 , https://stackoverflow.com/q/34006784
variables_to_export = [
    "project",
    "copyright",
    "release",
    "stable",
]

frozen_locals = dict(locals())
rst_epilog = '\n'.join(map(lambda x: f".. |{x}| replace:: {frozen_locals[x]}", variables_to_export))
del frozen_locals
