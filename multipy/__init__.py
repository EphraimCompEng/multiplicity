from .core.matrix import (
    Matrix,
)

from .core.algorithm import (
    Algorithm
)

from .core.truth import (
    truth_scope,
    shallow_truth_table,
    truth_table,
)

from .core.template import (
    Template
)

from .io.lazy_json import (
    json_pretty_store,
)


"""
MultiPy - Build, test and analyse multiplier designs
====================================================

Tools
    - Use built-in, or custom, reduction templates
    - Output truth tables to Parquet files
    - Perform fine-grain analysis on truth tables

Documentation
-------------
A growing number of resources can be found in /doc/ as well
as extensive use of docstrings throughout the library

Docstrings will assume 'Multipy' has been imported as 'mp':

    >>> import multipy as mp


Utilities
---------

test
    Run tests

config
    Update config files

__version__
    Show MultiPy version string

Copy vs in-place
----------------
??? TBD ???
"""


SUPPORTED_BITWIDTHS = {4, 8}

__all__ = [
    'Matrix',
    'Algorithm',
    'Template',
    'truth_scope',
    'shallow_truth_table',
    'truth_table',
    'json_pretty_store',
]
