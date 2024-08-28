<!---
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
-->

# Toctree-Only

Inspired by https://stackoverflow.com/questions/15001888/conditional-toctree-in-sphinx

## Configuration

`conf.py`:

```
extensions = [
    'toctree_only',
    # other extensions
]
```

Usage inside a reStructuredText file:

```
.. toctree-only::
    :maxdepth: 2
    :caption: Contents:

    env_html : introduction
    env_latex and env_pdf : usage
    env_singlehtml or not env_html : advanced
    anotherdoc
```
