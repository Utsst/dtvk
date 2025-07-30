# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DTVK'
copyright = '2025, AA'
author = 'AA'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.githubpages"
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "footer_start": ["footer"],
    "footer_end": ["copyright"],
    "show_prev_next": False,

    "use_edit_page_button": False,
    "navigation_with_keys": True,
#   "light_logo": "logo-light.png",
#  "dark_logo": "logo-dark.png",
    "theme_toggle": {
        "icon": "material/toggle-switch",
        "label": "Switch theme",
    },
}

# html_logo = "_static/logo-light.png"
# html_favicon = "_static/favicon.ico"

html_context = {
    "default_mode": "light",
}

html_show_sphinx = False  # Remove "Built with Sphinx"
html_show_copyright = False  # Remove copyright

html_static_path = ["_static"]
html_css_files = ["custom.css"]
