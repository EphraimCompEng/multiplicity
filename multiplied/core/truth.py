###################################
# Generate Multiplier Truth Table #
###################################

import multiplied as mp
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
    while x <= max_out:
        if  min_out <= (y := max_out//x) <= max_out:
            valid_domain.add((x, y))
        x += 1
    mirror = {(i[1], i[0]) for i in valid_domain}
    output = sorted(valid_domain | mirror)
    return (i for i in output)





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
