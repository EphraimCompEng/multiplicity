################################################
# Returns Template Objects Using User Patterns #
################################################


"""
Simple templates should be represented as a list with each element on
a new line, this makes it clear how each layer is reduced:
>>> my_simple_template = [
    1,
    1,
    2,
    2,
    2,
    .
    .
    .
]

The "run" of a given element determines where adders, run=2, or a
combination of CSAs and HAs, run=3, are used. Elements can be
int or strings, as long as they follow the "run" principle.

Complex templates require a more rigorous approach.

"""
from typing import Any
import multipy as mp

class Template:

    # Carry Save Adder
    csa = 0

    """
    ...FEDCBA9876543210| bit
       ----------------+-----
       ________00000000|  0
       _______00000000_|  1
       ______00000000__|  2
       _____00000000___|  3
       ____00000000____|  4
       ___00000000_____|  5
       __00000000______|  6
       _00000000_______|  7
                       .
                       .
                       .
    """

    def __init__(self, pattern: list[Any]): # Complex or simple
        valid_range = mp.SUPPORTED_BIT_LENGTHS
        if len(pattern) not in valid_range:
            raise ValueError(f"Valid bit lengths: {valid_range}")
        if '_' in set(pattern):
            raise ValueError("Invalid pattern: '_' is not allowed")
        self.layers   = len(pattern)
        self.pattern  = pattern
        self.template = self.__build_template(self.pattern)
        self.result   = None


    def __build_template(self, pattern) -> list[list[int]]:
        """
        Build a template for a bitwidth of self.bits. For example:
        >>> self.bits = 4
        >>> build_template(self.pattern)
        [['_','_','_','_',1,1,1,1], # p = [1,
         ['_','_','_',1,1,1,1,'_'], #      1,
         ['_','_',2,2,2,2,'_','_'], #      2,
         ['_',2,2,2,2,'_','_','_']] #      2,]
        """
        row = [0]*self.layers
        matrix = []

        return matrix

    # def





"""
Complex templates implement decoders and bit-mapping.

Decoders reduce 4 or more bits at a time.

Bit mapping allows for outlining where bits are placed in each stage,
enabling complex implementations and possible optimisations.
"""
