#########################################
# Algorithm Are Defined Using Templates #
#########################################

"""
Algorithm process:
0: Generate logical AND matrix
1: split matrix
2: apply template, update state
3: generate result
4: optionally apply map
5: update matrix
6: GOTO 1:

"""

import multipy as mp
from typing import Any

class Algorithm(mp.Matrix):
    """
    A given algorithm is created on top of a zero initialised Logical
    AND matrix. The first operation in the algorithm must populate
    this matrix with partial products.
    """


    def __init__(self, matrix: mp.Matrix) -> None:
        self.bits      = 0
        self.state     = 0
        self.stages    = len(self.algorithm)
        self.matrix    = matrix
        self.result    = {}
        self.algorithm = {}
        # self.populate(matrix) # -- Reactor

    def __repr__(self) -> str:
        pretty = ""
        print()
        for i, t in self.algorithm.items():
            pretty += f"S{i}:\n" + str(t) + "\n"
        return pretty

    def populate(self, arg: Any) -> None:
        """
        Adds template(s) to an existing algorithm. All templates must be of
        consistent bitwidth.
        """

        if isinstance(arg, mp.Template): # warp matrix in list to reuse code
            arg = [arg] # list(arg) throws error -- implement __iter___?
        elif not(isinstance(all(arg), list)):
            raise TypeError("Invalid argument type. Expected list[Matrix] or Matrix.")

        self.bits = arg[0].bits if (self.bits == 0) else self.bits # intialise
        for template in arg:

            # This test should be inside Template class------------------------- #
            if template.bits != self.bits:                                       #
                raise ValueError("All templates must have consistent bitwidth.") #
            # ------------------------------------------------------------------ #

            self.algorithm[len(self.algorithm)] = template



    def truth(self, matrix: mp.Matrix, template: mp.Template) -> None:
        ...

    def step(self, matrix: mp.Matrix) -> None:
        """
        Take template[internal_state], apply to matrix, advance internal_state
        """
        ...


    # Used to
    @classmethod
    def split(cls, matrix: mp.Matrix, rows: int):
        """
        Returns list of slices via progressive allocation.

        Append n contiguous slices of matrix, each containing x rows.
        If not enough rows, progress to rows-1 -> row-2 -> ...
        """
        x = 0
        if len(matrix) - (x * rows) < rows:
            ...
        ...

    @classmethod
    def reduce(cls):
        """
        Takes a template, splits
        """
        ...

    @classmethod
    def trim(cls, matrix: mp.Matrix) -> None:
        """
        Trim empty rows from a matrix
        """
        ...


    @classmethod
    def exec(cls):
        """
        Run algorithm with a single set of intputs then reset internal state
        """
        ...
