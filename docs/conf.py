# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'stapy120'
copyright = '2026, driller'
author = 'driller'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_revealjs",
    "sphinx_revealjs.ext.sass",
    "sphinxcontrib.mermaid",
    "sphinxext.remoteliteralinclude",
]

# -- Options for Reveal.js output -----------------------------------------------
revealjs_style_theme = "custom-solarized.css"
revealjs_static_path = ["_static"]
revealjs_sass_src_dir = "_sass"
revealjs_sass_out_dir = "_static"
revealjs_sass_auto_targets = True
revealjs_script_conf = {
    "width": 1200,
    "height": 700,
    "slideNumber": "c/t",
    "hash": True,
}
revealjs_css_files = [
    "revealjs/plugin/highlight/monokai.css",
    "mermaid-fix.css",
]
revealjs_script_plugins = [
    {
        "src": "revealjs/plugin/highlight/highlight.js",
        "name": "RevealHighlight",
    },
]

# -- MyST Parser configuration -----------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
]

# -- Mermaid configuration ---------------------------------------------------
mermaid_output_format = "svg"
mermaid_cmd = "npx -y @mermaid-js/mermaid-cli@latest"
mermaid_cmd_shell = "False"
mermaid_params = ["-b", "transparent", "-c", "mermaid-config.json", "-p", "puppeteer-config.json"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
