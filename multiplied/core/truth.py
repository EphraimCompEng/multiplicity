###################################
# Generate Multiplier Truth Table #
###################################

from pprint import pprint
import multiplied as mp
import pandas as pd
from collections.abc import Generator



"""
Do not optimise generation until functionality is actually tested for
edge cases and speed. Then refactor by using appropriate patterns,
simplification, etc., before applying multiprocessing and beyond.

"""


def truth_scope(domain_: tuple[int,int], range_: tuple[int,int]) -> Generator[tuple]:
    """
    A generator based on the domain and range of a desired truth table.

    Domain_: A tuple of integers representing the range of input values.
    Range_: A tuple of integers representing the range of output values.

    Yields tuple: (operand_a, operand_b)
    """

    if not all([isinstance(d, int) for d in domain_]):
        raise TypeError("Domain must be a tuple of integers.")
    if not all([isinstance(r, int) for r in range_]):
        raise TypeError("Range must be a tuple of integers.")

    min_in, max_in = domain_
    min_out, max_out = range_

    # improve error messages
    if min_in <= 0 or min_out <= 0:
        raise ValueError("Minimum input and output values must be greater than zero.")
    if min_in > max_in:
        raise ValueError("Minimum input value greater than maximum input value.")
    if min_out > max_out:
        raise ValueError("Minimum output greater than maximum output value.")
    if min_in > max_out:
        raise ValueError("Minimum input value greater than maximum output value.")
    if min_out > max_in:
        raise ValueError("Minimum output value greater than maximum input value.")


    valid_domain = set()
    # x could be set by value cl
    x = min_in
    while x <= max_in:
        for y in range(min_in, max_in + 1):
            if min_out <= x*y <= max_out:
                valid_domain.add((x, y))

        x += 1
    return (i for i in sorted(valid_domain))





def shallow_truth_table(scope: Generator[tuple], alg: mp.Algorithm
) -> Generator[mp.Matrix]:
    """
    Return Generator of partial product matrices for all operand tuples
    """

    return (mp.Matrix(alg.bits, a=a, b=b) for a, b in scope)

def truth_table(scope: Generator, alg: mp.Algorithm
) -> Generator[dict]:
    """
    A generator which yields all stages of an algorithm for a given
    set of operands a, b.
    """
    if not isinstance(scope, Generator):
        raise TypeError("Scope must be a generator.")
    if not isinstance(alg, mp.Algorithm):
        raise TypeError(f"Expected Algorithm instance got {type(alg)}")

    for a, b in scope:
        yield alg.exec(a=a, b=b)

def truth_dataframe(scope: Generator[tuple[int, int]], alg: mp.Algorithm
) -> pd.DataFrame:
    """
    Return a pandas DataFrame of all stages of an algorithm for a given
    set of operands a, b.
    """
    if not isinstance(scope, Generator):
        raise TypeError("Scope must be a generator.")
    if not isinstance(alg, mp.Algorithm):
        raise TypeError(f"Expected Algorithm instance got {type(alg)}")

    # -- old plan ---------------------------------------------------
    # columns:: index | a | b | ppm_0 | ppm_1 | ... | ppm_s0 | ppm_s1 | ...
    # ppm = partial product matrix, _<index> = row , _s<index> = formatted row
    # df row = index | a | b | output | matrix[i]: int | ... | matrix[i]: str | ... |

    # -- new multi-index plan ---------------------------------------
    #               | ppm_0              | ppm_1              |
    # index | a | b | b0 | b1 | ... | bn | b0 | b1 | ... | bn | ... | ppm_s0 | ppm_s1 | ...
    # 0     | 0 | 5 | 0  | 0  | ... | 0  | 0  | 0  | ... | 0  | ... |'000...'|'000...'| ...


    bits = alg.bits
    col = pd.MultiIndex.from_product([
        [f"stage_{i}" for i in alg.algorithm],
        [f"ppm_{i}" for i in range(bits)],
        [f"b{i}" for i in range(bits << 1)]

    ])




    dtype_map = {c: 'int8' for c in col}

    data     = []
    pretty   = []
    operands = []

    for a, b in scope:
        entry        = {}
        output       = alg.exec(a=a, b=b)
        pretty_entry = []
        operands.append((a, b, a*b))
        for stage, matrix in output.items():
            pretty_entry.append(str(matrix).split('\n'))
            for r, row in enumerate(matrix):
                for b, bit in enumerate(row):
                    entry[
                        (f"stage_{stage}",f"ppm_{r}",f"b{b}")
                    ] = 0 if bit in ['_', '0'] else 1
        data.append(entry)
        pretty.append(pretty_entry)

    ind     = pd.DataFrame(operands, columns=['a', 'b', 'output'])
    table   = pd.DataFrame(data, columns=col).astype(dtype_map)
    end_col = pd.DataFrame(pretty, columns=[f"ppm_s{i}" for i in range(bits)])
    return pd.concat([ind, table, end_col], axis=1)
