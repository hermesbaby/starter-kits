#############################################################################
#                                                                           #
#   This file is part of hermesbaby - the software engineers' typewriter    #
#                                                                           #
#   Copyright (c) 2024 Alexander Mann-Wahrenberg (basejumpa)                #
#                                                                           #
#   https://hermesbaby.github.io                                            #
#                                                                           #
# - The MIT License (MIT)                                                   #
#   when this becomes part of your software                                 #
#                                                                           #
# - The Creative Commons Attribution-Share-Alike 4.0 International License  #
#   (CC BY-SA 4.0) when this is part of documentation, blogs, presentations #
#                  or other content                                         #
#                                                                           #
#############################################################################

from docutils.parsers.rst import directives
from docutils.parsers.rst.directives import unchanged, flag
from sphinx.directives.other import TocTree
from sphinx.util.docutils import SphinxDirective
from sphinx.util import logging

logger = logging.getLogger(__name__)

class ToctreeOnly(SphinxDirective):
    has_content = True
    optional_arguments = 1
    option_spec = {
        'maxdepth': directives.nonnegative_int,
        'glob': flag,
        'hidden': flag,
        'titlesonly': flag,
        'reversed': flag,
        'numbered': directives.unchanged,
        'caption': unchanged,
        'name': unchanged,
    }

    def run(self):
        env = self.state.document.settings.env
        tags = env.app.tags

        filtered_content = []
        for entry in self.content:
            if ':' in entry:
                condition, actual_entry = map(str.strip, entry.split(':', 1))
                if condition and tags.eval_condition(condition):
                    filtered_content.append(actual_entry)
            else:
                filtered_content.append(entry.strip())

        # Create a new TocTree node with the filtered content
        toctree_node = TocTree(self.name, [], self.options, filtered_content, self.lineno, self.content_offset, self.block_text, self.state, self.state_machine)
        return toctree_node.run()

def setup(app):
    app.add_directive('toctree-only', ToctreeOnly)
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
