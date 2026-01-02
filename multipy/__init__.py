#!bin/python3
from .core.matrix import (
    Matrix,
)


from .core.template import (
    Pattern,
    Template,
    build_simple_template,
    build_csa,
    build_adder,
)

from .core.algorithm import (
    Algorithm
)

from .core.truth import (
    truth_scope,
    shallow_truth_table,
    truth_table,
)

from .io.lazy_json import (
    json_pretty_store,
)

# from .io.parquet import()

# -- External -------------------------


# -- Tests ----------------------------

# from .tests.test_population import (
#     test_pop_empty_matrix,
#     test_pop_build_matrix,
#     test_pop_agorithm,
# )

# from .tests.test_templates import (
#    test_temp_build_csa4,
#    test_temp_build_csa8,
#    test_temp_build_adder4,
#    test_temp_build_adder8,
# )

# from .tests.test_to_json import (
#     test_to_json4,
#     test_to_json8,
# )


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
    'Pattern',
    'Template',
    'Algorithm',
    'build_simple_template',
    'build_csa',
    'build_adder',
    'truth_scope',
    'shallow_truth_table',
    'truth_table',
    'json_pretty_store',

    # 'test_pop_empty_matrix',
    # 'test_pop_build_matrix',
    # 'test_pop_agorithm',
    # 'test_temp_build_csa4',
    # 'test_temp_build_csa8',
    # 'test_temp_build_adder4',
    # 'test_temp_build_adder8',
    # 'test_to_json4',
    # 'test_to_json8',


]
