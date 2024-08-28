# -*- coding: utf-8 -*-

# pylint: skip-file

import os
import platform
import re
import sys
import unicodedata
import time

_conf_location = os.path.realpath(os.path.dirname(__file__))


### Import project configuration ##############################################
# @see https://www.kernel.org/doc/html/next/kbuild/kconfig-language.html

# Obsolete - BEGIN
y = True
n = False

with open(".config") as f:
    exec(f.read())
# Obsolete - END

def translate_config_file(input_file=".config", output_file="config.py"):
    CONFIG_PREFIX = r"^CONFIG_"

    # Define the path for the input and output files
    current_directory = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(current_directory, input_file)
    output_file_path = os.path.join(current_directory, output_file)

    # Check if the output file needs to be created or updated
    if (not os.path.exists(output_file_path) or
        os.path.getmtime(config_file_path) > os.path.getmtime(output_file_path)):

        # Read the input file
        with open(config_file_path, "r") as config_file:
            lines = config_file.readlines()

        # Process the lines
        processed_lines = []
        for line in lines:
            if re.match(CONFIG_PREFIX, line):
                # Remove the CONFIG_PREFIX
                processed_lines.append(re.sub(CONFIG_PREFIX, "", line))
            else:
                processed_lines.append(line)

        # Write to the output file
        with open(output_file_path, "w") as output_file:
            output_file.write("n = False\n")
            output_file.write("y = True\n")
            output_file.writelines(processed_lines)

# Call the function
translate_config_file()

# Import the generated config module
sys.path.append(f"{os.getcwd()}")
import config

###############################################################################

### SPHINX CONFIGURATION (GENERAL) ############################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html

# The configuration values shall be placed in the same order as they are placed in the documenting manual.
# The documenting chapter of the manual shall be reflected by a section in this config file.
# The hyperlink to that chapter shall be placed in the very first line of that section.

# Helper variables which are used inside this configuration file which support a calculation of a
# configuration value shall be named so they start with an underscore ("_") so it"s obvious
# that they are local helper variables only used here.
# This is not a function by the interpreter but a common syntax hint to the programmer.

###############################################################################
### Investigte environment ####################################################
###############################################################################

# Investigate the environment variables
if False:
    f = open("env.txt", "w")
    for key, value in os.environ.items():
        f.write(f"{key}: {value}\n")
    f.close()

#
## Find the current builder ###################################################
#
# This configuration knows the following builders
#
# - "dirhtml"
# - "html"
# - "latex"
# - "revealjs"

builder = "dirhtml"
if "-b" in sys.argv:
    builder = sys.argv[sys.argv.index("-b")+1]

### Project information #######################################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# pyright: reportShadowedImports=false
import datetime
from tzlocal import get_localzone
import git
import getpass

_timezone = get_localzone()
_current_time = datetime.datetime.now(_timezone)
_formatted_time = _current_time.strftime("%Y-%m-%d %H:%M:%S")
_print_out_timestamp = f"{_formatted_time} {_current_time.tzname()}"
_year = _current_time.strftime("%Y")


_git_upstream_repo_url = None
_git_repo_version = ""
_git_commit_sha_short = "n.a."
_git_branch = "n.a."
try:
    _repo = git.Repo(search_parent_directories=True)
    try:
        _git_upstream_repo_url = _repo.remotes.origin.url
    except:
        pass
    try:
        _git_repo_version = _repo.git.describe(dirty="+")
    except:
        pass
    try:
        _git_commit_sha_short = _repo.git.rev_parse(_repo.head.object.hexsha, short=8)
    except:
        pass
    try:
        _git_branch = _repo.active_branch.name
    except TypeError:
        _git_branch = "detached HEAD"
except:
    pass

_username = getpass.getuser()


_commit = _git_repo_version
if "" == _commit:
    _commit = _git_commit_sha_short

project   = config.DOC__PROJECT
author    = config.DOC__AUTHOR
copyright = f"{config.DOC__YEAR}, {config.DOC__AUTHOR}"


_confidential_level = f"{config.DOC__CONFIDENTIALITY_LEVEL_LABEL}: {config.DOC__CONFIDENTIALITY_LEVEL}"

### Construct meta-data header:

_metadata   = f"commit: {_commit} | branch: {_git_branch} | printed at {_print_out_timestamp} by {_username} | {_confidential_level}"

## Add CI information
# Indicator is the environment variable "BUILD_NUMBER" which is set by the CI/CD system.

_build_number = os.environ.get('BUILD_NUMBER')
if _build_number is not None:
    _metadata += f" | Jenkins build-no: {_build_number}"


### Make (project) information available in restructured text #################

## By using the placeholder functionality of Sphinx ###########################
# The exposed variables shall begin with "conf_" to make it clear that they are configuration variables.
rst_prolog = f"""
.. |conf_git_branch| replace:: {_git_branch}
.. |conf_metadata| replace:: {_metadata}
.. |conf_confidential_level| replace:: **{_confidential_level}**
"""


### General configuration #####################################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language
language = config.DOC__LANGUAGE

templates_path = []

source_suffix = [
    ".rst",
    ".md",
    ".ipynb"
]

exclude_patterns = [
    "README.md",
    "15-Meeting-Minutes/2024CW99/**", # Template
]

## Let's expand `some string` to `some string` instead of *some string*
default_role = "code"

master_doc = "index"

numfig = True


### Options for HTML output ###################################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Just initialize as a list here. To be filled from extensions below
html_static_path = []

# Just initialize as a list here. To be filled from extensions below
html_extra_path = []

html_show_sourcelink = False

html_theme = "sphinx_material"

# Override the html_theme for previewing in VSCode.
# Esbonio language server we use in VSCode for previewing crashes when using the "sphinx_material" theme.
# We use environment variable "VSCODE_CLI" to detect if we are in the VSCode environment.

if os.environ.get('VSCODE_CLI') is not None:
    pass #html_theme = "classic"


# The theme settings are theme specific. So wrap their settings into if-clauses for easy
# switching of themes.
if "sphinx_material" == html_theme: ###########################################
# @eee https://bashtage.github.io/sphinx-material/customization.html

    html_sidebars = {
        "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
    }

    html_theme_options = {
        "repo_name": "Code",

        "globaltoc_depth": 3,
        "globaltoc_collapse": "true",
        "globaltoc_includehidden": "true",

        #"localtoc_label_text": "Seiteninhalt",
        "localtoc_label_text": "Auf dieser Seite",
    }

    ## repo_url ###########################################
    html_theme_options["repo_url"] = f"https://{config.SCM__HOST}/{config.SCM__OWNER_KIND}/{config.SCM__OWNER}/repos/{config.SCM__REPO}/browse"

    ## nav_title ##########################################
    html_theme_options["nav_title"] = config.DOC__TITLE

    if "" != config.STYLING__COLOR_PRIMARY:
        html_theme_options["color_primary"] = config.STYLING__COLOR_PRIMARY

    if "" != config.STYLING__COLOR_ACCENT:
        html_theme_options["color_accent"] = config.STYLING__COLOR_ACCENT

    html_title = f"{_metadata}"

elif "classic" == html_theme: #################################################
    html_sidebars = {
        "**": []
    }

elif "pydata_sphinx_theme" == html_theme: #####################################
    html_theme_options = {
    "show_toc_level": 2
    }

    pass

else:
    pass


### Access control for publish on Apache 2 ####################################

html_extra_path.append("web_root")


### Options for latex / PDF output ############################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output
# @see more settings at https://www.sphinx-doc.org/en/master/latex.html#the-latex-elements-configuration-setting

latex_elements = {

    "papersize"   : "a4paper",
    "pointsize"   : "12pt",

    "preamble" : r"""
\setlength{\headheight}{15pt}
\addtolength{\topmargin}{-3pt}
\usepackage[utf8]{inputenc}
"""
}

# @see https://chatgpt.com/share/1ed3fcdf-0405-45a3-9fd6-fcb97d7e793c
def sanitize_filename(internal_string):
    # Normalize the string to decompose special characters (like umlauts)
    normalized_string = internal_string
    #normalized_string = unicodedata.normalize('NFKD', internal_string)

    # Encode the normalized string to ASCII bytes, ignoring non-ASCII characters
    ascii_bytes = normalized_string.encode('ascii', 'ignore')

    # Decode the bytes back to a string
    ascii_string = ascii_bytes.decode('ascii')

    # Replace spaces and other undesirable characters with underscores
    safe_string = re.sub(r'[^\w\s-]', '', ascii_string).strip().lower()
    safe_string = re.sub(r'[-\s]+', '_', safe_string)

    return safe_string


_pdf_basename = sanitize_filename(config.DOC__TITLE)

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        "index",
        f"{_pdf_basename}.tex",
        config.DOC__TITLE,
        author,
        "manual"
    ),
    (
        "00-Project-Manual/index",
        f"Projekthandbuch-{project}.tex",
        project,
        author,
        "manual"
    ),
]


###############################################################################
### EXTENSIONS AND THEIR SETTINGS #############################################
###############################################################################

# Ordered list. Order: Most general first, then for more and more special usescases
# Just initialize as a list here. To be filled from extensions below
extensions = []

# List of functions to be called by Sphinx's setup(app) function
app_setups = []


### Create redirects for moved pages ##########################################
# @see https://sphinxext-rediraffe.readthedocs.io

extensions.append("sphinxext.rediraffe")

rediraffe_redirects = "redirects.txt"
rediraffe_branch = _git_branch


### Draw diagrams with "draw.io" ##############################################
# @see https://pypi.org/project/sphinxcontrib-drawio/

extensions.append("sphinxcontrib.drawio")

# Prevent from nasty console flickering
drawio_disable_verbose_electron = True

# Linux-only settings:
if "Linux" == platform.system():

    # Run virtual X-Server.
    drawio_headless = True

    # Make it work in docker containers
    drawio_no_sandbox = True


### Embedd diagrams as code in plantuml language with "plantuml" #############
# @see https://github.com/sphinx-contrib/plantuml
# @see https://crashedmind.github.io/PlantUMLHitchhikersGuide/

extensions.append("sphinxcontrib.plantuml")

_plantuml_config_file="plantuml.config"

plantuml = f"java -jar {_conf_location}/../.tools/plantuml.jar -config {_conf_location}/{_plantuml_config_file}"

plantuml_batch_size = 500

plantuml_output_format = "svg"

plantuml_latex_output_format = "pdf"


### Author diagrams of arbitrary types with "Mermaid" #########################
# @see https://sphinxcontrib-mermaid-demo.readthedocs.io
# @see https://mermaid.js.org/syntax/gitgraph.html

extensions.append("sphinxcontrib.mermaid")

# Set the output format depending on builder:
# Use svg but overwrite it in case we want to build a pdf via latex-builder

mermaid_output_format = "svg"

def setup_app__mermaid(app):
    app.connect('builder-inited', _mermaid_on_builder_inited)

app_setups.append(setup_app__mermaid)

def _mermaid_on_builder_inited(app):

    if "latex" == app.builder.name:
        # Override setting(s)
        app.config.mermaid_output_format = "pdf"

# This allows commands other than binary executables to be executed on Windows.
# Does work on Windows, only.
if "Windows" == platform.system():
    mermaid_cmd_shell = "True"

# For individual parameters, a list of parameters can be added. Refer to https://github.com/mermaidjs/mermaid.cli#options.
mermaid_params =  []

# Make it work under Linux as root (in CI in docker container)
# Works on Windows with any user as well.
mermaid_params += ["-p", os.path.join(_conf_location, "puppeteer-config.json")]

# Styling
mermaid_params += [ "--backgroundColor", "transparent"]
mermaid_params += ["--theme", "forest"]
mermaid_params += ["--width", "400" ]

mermaid_d3_zoom = True


### Author diagrams of arbitrary types with "Graphviz" ########################
# @see https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html
# @see https://graphviz.org/gallery/
# @see https://graphviz.org/docs/attrs/rankdir/

extensions.append("sphinx.ext.graphviz")


### Add copy-to-clipboard button to codeblocks ################################
# @see https://sphinx-copybutton.readthedocs.io

extensions.append("sphinx_copybutton")


### Manage todos with "todo" ##################################################
# @see https://www.sphinx-doc.org/en/master/usage/extensions/todo.html

extensions.append("sphinx.ext.todo")

todo_include_todos = True


### Add sophistic html elements - use with care ###############################
# @see https://sphinx-design.readthedocs.io

extensions.append("sphinx_design")

tags_create_tags = False


### Add tagging ###############################################################
# @see https://sphinx-tags.readthedocs.io

extensions.append("sphinx_tags")

# Enable/disable the functionality
tags_create_tags = False

# Configuring the functionality
tags_create_badges = True
tags_page_header = "Tags"
tags_page_title = "Seiten getaggt mit"

tags_badge_colors = {
    "in_work"        : "warrning",
    "draft"          : "dark",
    "in_review"      : "primary",
    "approved"       : "success",
    "info"           : "info",
    "in_doubt"       : "danger",
}


### Include Markdown (*.md) sources, e.g. for tables  #########################
# @see https://sphinx-mdinclude.omnilib.dev

extensions.append("sphinx_mdinclude")


### Create sophisticated tables  ##############################################
# @see https://sharm294.github.io/sphinx-datatables/
# @see https://datatables.net/

extensions.append("sphinxcontrib.jquery")
extensions.append("sphinx_datatables")


### Enable bibliography in bibtex format ######################################
# @see https://sphinxcontrib-bibtex.readthedocs.io/
# @see https://www.bibtex.com/g/bibtex-format/

extensions.append("sphinxcontrib.bibtex")

bibtex_bibfiles = []

bibtex_bibfiles_candidates = [
    "references.bib",
]

def append_existing_files(file_list, filenames_to_check):
    for filename in filenames_to_check:
        if os.path.exists(filename):
            file_list.append(filename)
        else:
            print(f"info: Bibfile '{filename}' does not exist.")

append_existing_files(bibtex_bibfiles, bibtex_bibfiles_candidates)


### Make use of Inkscape for PDF output work  #################################
# @see https://pypi.org/project/sphinxcontrib-svg2pdfconverter/

extensions.append("sphinxcontrib.inkscapeconverter")


### Create hyperlinks to issues  ##############################################
# @see https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html

extensions.append("sphinx.ext.extlinks")

extlinks = {
    "jira": ("https://jira.vitronic.de/browse/%s","%s"),
    "user": ("https://intranet.vitronic.de/Allgemeines/Mitarbeitertelefonliste/MitarbeiterInfoMain.php?kurz=%s", "%s"),
}

extlinks_detect_hardcoded_links = False


### Link documentation items with "mlx.traceability" ##########################
# @see https://melexis.github.io/sphinx-traceability-extension

extensions.append("mlx.traceability")

import mlx.traceability

html_static_path.append(os.path.join(os.path.dirname(mlx.traceability.__file__), "assets"))

traceability_relationships = {
    'jira': '',
}

traceability_relationship_to_string = {
    'jira': 'JIRA item',
}

traceability_external_relationship_to_url = {
    'jira': 'https://jira.vitronic.de/browse/field1',
}

traceability_render_relationship_per_item = True


###############################################################################
### BEGIN OF EXTENSIONS UNDER EARLY DEVELOPMENT ###############################
###############################################################################

### Tag sections, paragraphs, figures, ... anything ###########################
# @see ../sphinx-contrib/pre-post-build/README.md

sys.path.append(f"{os.getcwd()}/../sphinx-contrib/pre-post-build/src")

extensions.append('pre_post_build')

pre_post_build_programs = {
    "post": [
        {
            "name"     : "Create PDF from Latex code",
            "builder"  : "latex",
            "program"  : "make",
            "cwd"      : "$outputdir",
            "severity" : "info"
        },
        {
            "name"     : "View",
            "builder"  : "latex",
            "program"  : "sumatrapdf",
            "args"     : [f"$outputdir\\{_pdf_basename}.pdf"],
            "severity" : "info"
        }
    ]
}


### Conditional toctree entries with toctree-only #############################
# @see ../sphinx-contrib/toctree-only/README.md

sys.path.append(f"{os.getcwd()}/../sphinx-contrib/toctree-only/src")

extensions.append('toctree_only')


## By applying Jinja2 Templating Engine every rst file ########################

# @see https://ericholscher.com/blog/2016/jul/25/integrating-jinja-rst-sphinx/
# @see https://stackoverflow.com/questions/54520956/declare-additional-dependency-to-sphinx-build-in-an-extension
# @see https://www.sphinx-doc.org/en/master/extdev/appapi.html
# @see https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.add_config_value
# @see https://jinja.palletsprojects.com/en/3.0.x/api/


config_as_dict = {name: value for name, value in vars(config).items() if not name.startswith('__')}

def rstjinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    src = source[0]
    try:
        rendered = app.builder.templates.render_string(
            src,
            app.config.config_as_dict # This is the glue: the app.config.config_as_dict is the config variable in conf.py
        )
    except:
        print("ERROR in Jinja template while processing " + docname)

    source[0] = rendered


def setup_app__rstjinja(app):
    app.add_config_value(name='config_as_dict', default={}, rebuild=True)
    app.connect("source-read", rstjinja)

app_setups.append(setup_app__rstjinja)

###############################################################################
### END OF EXTENSIONS UNDER EARLY DEVELOPMENT #################################
###############################################################################

### Call all the above collected app setups functions #########################

def setup(app):
    for app_setup in app_setups:
        app_setup(app)


### EOF #######################################################################
