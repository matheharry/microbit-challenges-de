# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Lumache'
copyright = '2023, MatheHarry'
author = 'Harald March'

release = '0.4'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
    'navigation_depth': 5,
}

#html_title = None
html_title ="micro:bit MicroPython Tutorial" 

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'matheharry.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'hm.ico'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Output file base name for HTML help builder.
htmlhelp_basename = 'BBCMicrobitTutorialdoc'

# Bibliographic Dublin Core info.
epub_title = u'Microbit Micropython Tutorial'

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'MicrobitMicropython.tex', u'micro:bit MicroPython Tutorial',
   u'Harald March, Rae Harbird, Stephen Hailes', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = 'matheharry.jpeg'