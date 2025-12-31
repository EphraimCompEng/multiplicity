#########################################
# Algorithm Are Defined Using Templates #
#########################################
"""
An algorithm is the application of multiple templates until no partial
products are left.

Algorithm objects must collect any number of templates based on:
    - bitwidth
    - template composition -- MultiPy should not stop users making any
      algorithm, even if suboptimal
    - Saturation -- Set to original bit width
    (Unsure if users likely to need saturation to arbitrary bitwidths)

Applying simple templates can be hardcoded, however complex templates
need to be analysed before execution. Especially so when implementing
decoders, flooding and sneaky tricks like using carry-in(cin) on adders.


"""


from typing import Any
import multipy as mp

class Algorithm(mp.Matrix):
    """
    A given algorithm is created on top of a zero initialised Logical
    AND matrix. The first operation in the algorithm must populate
    this matrix with partial products.
    """


    def __init__(self, matrix: mp.Matrix) -> None:
        self.algorithm = {}
        self.bits = 0
        self.populate(matrix)
        self.stages = len(self.algorithm)

    def populate(self, arg: Any) -> None:
        """
        Adds template(s) to an existing algorithm. All templates must be of
        consistent bitwidth.
        """

        if isinstance(arg, mp.Template): # warp matrix in list to reuse code
            arg = [arg] # list(arg) throws error -- implement __iter___?
        elif not(isinstance(arg, list)):
            raise TypeError("Invalid argument type. Expected list[Matrix] or Matrix.")

        bit = arg[0].bits if (self.bits == 0) else self.bits
        for template in arg:
            if template.bits != bit:
                raise ValueError("All templates must have consistent bitwidth.")
            self.algorithm[len(self.algorithm)] = template
        self.bits = bit


    @classmethod
    def step(cls, matrix: mp.Matrix) -> None:
        """
        Take youngest template, apply to matrix, remove template
        """
        ...

    @classmethod
    def trim(cls, matrix: mp.Matrix) -> None:
        """
        Trim empty rows from a matrix
        """
        ...

    def __repr__(self) -> str:
        pretty = ""
        print()
        for i, t in self.algorithm.items():
            pretty += f"S{i}:\n" + str(t) + "\n"
        return pretty
