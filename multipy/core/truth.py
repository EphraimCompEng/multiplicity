###################################
# Generate Multiplier Truth Table #
###################################


from collections.abc import Generator
import multipy as mp
import pathlib



"""
Do not optimise generation until functionality is actually tested for
edge cases and speed. Then refactor by using appropriate patterns,
simplification, etc., before applying multiprocessing and beyond.

"""

# Efficient calculation of possible input values(hopefully):
# for x < a * b < y use x/b < a < y/b to find limits of 'a', for a fixed 'b'
def truth_scope(domain_: tuple[int,int], range_: tuple[int,int]) -> Generator:
    """
    Generate a generator based on the domain and range of a desired truth table
    >>> domain = (min_input, max_input)
    >>> range  = (min_output, max_output)
    """

    min_input, max_input = domain_
    min_output, max_output = range_
    if min_input <= 0 or min_output <= 0:
        raise ValueError("Minimum input and output values must be greater than zero.")
    if min_input > max_input:
        raise ValueError("Minimum input value greater than maximum input value.")
    if min_output > max_output:
        raise ValueError("Minimum output greater than maximum output value.")

    gen1 = (b for b in range(min_input, max_input + 1))
    k = 0
    for b in gen1:
        if (mn := min_output // b) == 0:
            k = 1
        gen2 = (a for a in range(mn + k, (max_output // b)+1))
        for a in gen2:
            yield a, b
