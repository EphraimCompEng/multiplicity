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

import multiplicity as mp
from typing import Any

class Algorithm(mp.Matrix):
    """
    A given algorithm is created on top of a zero initialised Logical
    AND matrix. The first operation in the algorithm must populate
    this matrix with partial products.
    """

    """
    pattern only implementation -- small steps:

        > detect pattern inside Template object
        > Slice matrix(data) along pattern "runs"
        > reduce slices
        > unify slices
        > apply row map
        > update Algorithm object state
    """

    def __init__(self, matrix: mp.Matrix) -> None:
        self.bits      = 0
        self.state     = 0
        self.len       = len(self.algorithm)
        self.matrix    = matrix
        self.result    = {}
        self.algorithm = {}
        """Structure of a given algorithm stage:
        >>> self.algorithm[x] = {
        >>>     "template" : mp.Template
        >>>     "result"   : mp.Matrix
        >>>     "map"      : mp.Map
        >>> }
        """
        self.stage     = self.algorithm[self.state]

    def __repr__(self) -> str:
        pretty = ""
        print()
        for i, t in self.algorithm.items():
            pretty += f"S{i}:\n" + str(t) + "\n"
        return pretty

    # -- Refactor to new structure ------------ #
    # >>> self.algorithm[x] = {                 #
    # >>>     "template" : mp.Template          #
    # >>>     "result"   : mp.Matrix            #
    # >>>     "map"      : mp.Map               #
    # >>> }                                     #
    def populate(self, arg: Any) -> None: # --- #
        """
        Adds template(s) to an existing algorithm. All templates must be of
        consistent bitwidth.
        """

        if isinstance(arg, mp.Template): # warp matrix in list to reuse code
            arg = [arg]
        elif not(isinstance(all(arg), list)):
            raise TypeError("Invalid argument type. Expected list[Matrix] or Matrix.")

        self.bits = arg[0].bits if (self.bits == 0) else self.bits # intialise

        for template in arg:
            if template.bits != self.bits:
                raise ValueError("All templates must have consistent bitwidth.")
            self.algorithm[len(self.algorithm)] = template



    # def _reduce(self):
    #     """
    #     Helper function to step through a single stage of an algorithm
    #     """
    #     ...

    def truth(self, matrix: mp.Matrix, template: mp.Template) -> None:
        ...

    def step(self, matrix: mp.Matrix) -> None:
        """
        Take template[internal_state], apply to matrix, advance internal_state
        """
        ...

    # Used to automate splitting a matrix into Slice(n * row)
    @classmethod
    def split(cls, matrix: mp.Matrix, rows: int):
        """
        Returns list of slices via progressive allocation. Used to automate
        slicing a matrix into (Slice(n * row) * k), then splitting remainder

        Append n contiguous slices of matrix, each containing x rows.
        If not enough rows, progress to rows-1 -> row-2 -> ...
        """
        x = 0
        if len(matrix) - (x * rows) < rows:
            ...
        ...




    @classmethod
    def exec(cls):
        """
        Run algorithm with a single set of intputs then reset internal state
        """
        ...
