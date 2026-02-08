###################################
# Generate Multiplier Truth Table #
###################################


from functools import cache
from multiplied import Algorithm, Matrix
import pandas as pd
from multiprocessing import Pool
from collections.abc import Generator



"""
Do not optimise generation until functionality is actually tested for
edge cases and speed. Then refactor by using appropriate patterns,
simplification, etc., before applying multiprocessing and beyond.

"""


def truth_scope(domain_: tuple[int,int], range_: tuple[int,int]
) -> Generator[tuple]:
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

    x = min_in
    while x <= max_in:
        lower_bound = min_out//x if min_out//x > min_in else min_in
        upper_bound = max_out//x if max_out//x < max_in else max_in
        for y in range(lower_bound, upper_bound):
            if min_out <= (k := x*y) <= max_out:
                yield (x, y)
            if max_out < k:
                break
        x += 1



def shallow_truth_table(scope: Generator[tuple], alg: Algorithm
) -> Generator[Matrix]:
    """
    Return Generator of partial product matrices for all operand tuples
    """

    return (Matrix(alg.bits, a=a, b=b) for a, b in scope)

def truth_table(scope: Generator, alg: Algorithm
) -> Generator[dict]:
    """
    A generator which yields all stages of an algorithm for a given
    set of operands a, b.
    """
    if not isinstance(scope, Generator):
        raise TypeError("Scope must be a generator.")
    if not isinstance(alg, Algorithm):
        raise TypeError(f"Expected Algorithm instance got {type(alg)}")

    for a, b in scope:
        yield alg.exec(a=a, b=b)



def _dataframe_operand_worker(a: int, b: int) -> tuple:
    return (a, b, a*b)

def _dataframe_pretty_worker(a: int, b: int , alg: Algorithm) -> list:
    pretty = []
    for matrix in alg.exec(a=a, b=b).values():
        pretty.append(str(matrix).split('\n')[:-1])
    return pretty

def _dataframe_entry_worker(a: int, b: int , alg: Algorithm) -> dict:
    entry = {}
    for stage, matrix in alg.exec(a=a, b=b).items():
        for r, row in enumerate(matrix):
            for b, bit in enumerate(row[::-1]):
                entry[
                    (f"stage_{stage}",f"ppm_{r}",f"b{b}")
                ] = 0 if bit in ['_', '0'] else 1
    return entry

@cache
def truth_dataframe(scope: Generator[tuple[int, int]], alg: Algorithm
) -> pd.DataFrame:
    """
    Return a pandas DataFrame of all stages of an algorithm for a given
    set of operands a, b.
    """
    if not isinstance(scope, Generator):
        raise TypeError("Scope must be a generator.")
    if not isinstance(alg, Algorithm):
        raise TypeError(f"Expected Algorithm instance got {type(alg)}")

    # -- old plan ---------------------------------------------------
    # columns:: index | a | b | ppm_0 | ppm_1 | ... | ppm_s0 | ppm_s1 | ...
    # ppm = partial product matrix, _<index> = row , _s<index> = formatted row
    # df row = index | a | b | output | matrix[i]: int | ... | matrix[i]: str | ... |

    # -- new multi-index plan ---------------------------------------
    #               | ppm_0              | ppm_1              |
    # index | a | b | b0 | b1 | ... | bn | b0 | b1 | ... | bn | ... | ppm_s0 | ppm_s1 | ...
    # 0     | 0 | 5 | 0  | 0  | ... | 0  | 0  | 0  | ... | 0  | ... |'000...'|'000...'| ...


    # -- duplicate generators for each pool -------------------------
    from itertools import tee
    scope1, scope2, scope3 = tee(scope, 3)

    # Uses every available core
    with Pool() as pool:
        operands = pool.starmap(_dataframe_operand_worker, scope1)
        pretty   = pool.starmap(_dataframe_pretty_worker, ((a, b, alg) for a, b in scope2))
        data     = pool.starmap(_dataframe_entry_worker, ((a, b, alg) for a, b in scope3))
        pool.close()
        pool.join()

    col = pd.MultiIndex.from_product([
        [f"stage_{i}" for i in alg.algorithm],
        [f"ppm_{i}" for i in range(alg.bits)],
        [f"b{i}" for i in range((alg.bits << 1)-1, -1, -1)]

    ])

    # col.dtype('int8')
    # dtype_map = {c: 'int8' for c in col}

    ppm_s_columns   = [f"ppm_s{i}" for i in range(len(alg.algorithm)+1)]


    operand_columns = pd.DataFrame(operands, columns=['a', 'b', 'output'], dtype='int32')
    pretty_columns  = pd.DataFrame(pretty, columns=ppm_s_columns, dtype='str')
    table           = pd.DataFrame(data, columns=col).astype('int8')

    return pd.concat([operand_columns, table, pretty_columns], axis=1)
