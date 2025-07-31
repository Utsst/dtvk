# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# Project info
project = 'DTVK 1.0 documentation'
html_title = "DTVK documentation"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.githubpages",
    "sphinx_last_updated_by_git",  # ✅ must be exactly this name
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
    # Items displayed at the start (left) of the navbar — usually the logo
    "navbar_start": ["navbar-logo"],

    # Items centered in the navbar — typically the main navigation links
    "navbar_center": ["navbar-nav"],

    # Items displayed at the end (right) of the navbar — here: theme toggle, icon links, and search button
    # "navbar_end": ["theme-switcher", "navbar-icon-links", "search-button"],
    "navbar_end": ["theme-switcher"],

    # Placeholder text shown in the floating search dialog
    "search_bar_text": "Search the docs ...",

    # Content shown at the start (left) of the footer — here, custom footer content
    "footer_start": ["footer"],

    # Content shown at the end (right) of the footer — typically the copyright line
    "footer_end": ["copyright"],

    # Enables previous/next navigation links at the bottom of each page
    "show_prev_next": True,

    # Allows keyboard navigation (← → arrows) between pages
    "navigation_with_keys": True,

    # Hides the "Edit this page" button that would link to your GitHub source
    "use_edit_page_button": False,

    # (Optional) Uncomment below to use light/dark mode logos — must match filenames in _static/
    # "light_logo": "logo-light.png",
    # "dark_logo": "logo-dark.png",

    # Controls the appearance and label of the theme toggle (light/dark/system)
    "theme_toggle": {
        "icon": "material/toggle-switch",  # Icon for the toggle button
        "label": "Switch theme",           # Tooltip or button label
    },
}

html_last_updated_fmt = "%Y-%m-%d"
html_last_updated = True

# html_logo = "_static/logo-light.png"
# html_favicon = "_static/favicon.ico"

import datetime

html_context = {
    "default_mode": "light",
}

html_show_sphinx = False  # Remove "Built with Sphinx"
html_show_copyright = False  # Remove copyright
html_show_sourcelink = False # Remove source

html_static_path = ["_static"]
html_css_files = ["custom.css"]

myst_enable_extensions = [
    "colon_fence",
    "jinja",  # ✅ This enables {{ last_updated }} to be rendered in .md
]