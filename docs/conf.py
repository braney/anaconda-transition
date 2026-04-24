# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CaRCC Anaconda transtion'
copyright = '2025, CaRCC Anaconda transtion working group'
author = 'CaRCC Anaconda transtion working group'
author_tex = '{CaRCC} {A}naconda {T}ranstion {W}orking {G}roup'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']



# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_theme = 'manual'
latex_show_urls = 'footnote'
latex_elements = {
    # See https://www.sphinx-doc.org/en/master/latex.html#module-latex
    # for more tweaks that could be put here.
    'papersize': 'letterpaper',
    'pointsize': '11pt',
}

# This is to generate individual PDF files (as well as the default joint one)
pdf_title_tex = 'Addressing the Challenges Posed by {A}naconda’s New Licensing Model'
latex_documents = [
    # ('source_file', 'target_tex_file', 'Document Title', 'Author', 'Document Class', [toctree_only]),
    # Combined A+B+FAQ (this is the default when 'latex_documents' not given)
    ('index', 'carcc-anaconda_transtion.tex', pdf_title_tex, author_tex, 'manual'),

    ('PaperA_users-researchers/White-paper-to-users-researchers',
     'anaconda_transition-for-users-researchers.tex',
     f"{pdf_title_tex}: For Users, Researchers and System Administrators", author_tex, 'howto'),

    ('PaperB_institutional-leadership/White-paper-to-institutional-leadership',
     'anaconda_transition-for-leadership.tex',
     f"{pdf_title_tex}: For Institutional Leadership", author_tex, 'howto'),

    ('FAQ/FAQs', 'FAQ.tex', f"{pdf_title_tex}: FAQ", author_tex, 'howto'),
]
