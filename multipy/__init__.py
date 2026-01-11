#!bin/python3

from pathlib import Path
import toml_rs

# -- core ---------------------------------------

from .core.matrix import (
    Matrix,
    Slice,
    build_matrix,
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

from .core.map import (
    Map,
    build_dadda_map,
    resolve_rmap,
)

# -- utils --------------------------------------
from .core.utils.char import (
    ischar,
)


from .core.utils.pretty import (
    pretty,
    mprint,
)

# -- datasets -----------------------------------



# -- io -----------------------------------------

from .io.lazy_json import (
    json_pretty_store,
)

# from .io.parquet import()
#


# -- External -----------------------------------


# -- Tests --------------------------------------

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



# -- pyproject.toml metadata --------------------


with open(Path(__file__).parent.parent / "pyproject.toml", "r") as f:
    MP_TOML = toml_rs.loads(f.read())

MP_VERSION = MP_TOML["project"]["version"]

SUPPORTED_BITWIDTHS = {4, 8}


__all__ = [
    'Matrix',
    'Slice',
    'build_matrix',
    'Pattern',
    'Template',
    'Algorithm',
    'build_dadda_map',
    'resolve_rmap',
    'build_simple_template',
    'build_csa',
    'build_adder',
    'truth_scope',
    'shallow_truth_table',
    'truth_table',
    'json_pretty_store',
    'Map',
    'ischar',
    'pretty',
    'mprint',
    'MP_VERSION',
    'SUPPORTED_BITWIDTHS',




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
