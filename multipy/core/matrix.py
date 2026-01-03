#################################################
# Generating, Aligning Initial Partial Products #
#################################################

import multipy as mp
from typing import Any


class Matrix:
    def __init__(self, bits: int):
        valid_range = mp.SUPPORTED_BITWIDTHS
        if bits not in valid_range:
            raise ValueError(f"Valid bit lengths: {valid_range}")
        self.bits = bits
        self.matrix = self.__empty_matrix()

    def __empty_matrix(self) -> list[list[Any]]:
        """
        Build a wallace tree style logic AND matrix for a bitwidth of self.bits.
        """
        row = [0]*self.bits
        matrix = []
        for i in range(self.bits):
            matrix.append(["_"]*(self.bits-i) + row + ["_"]*i)
        return matrix

    @classmethod
    def build_matrix(cls, operand_a: int, operand_b: int, bits: int):
        """
        Build Logical AND matrix using source operands.
        """
        if (operand_a > ((2**bits)-1)) or (operand_b > ((2**bits)-1)):
            raise ValueError("Operand bit width exceeds matrix bit width")

        # convert to binary, removing '0b' and padding with zeros
        # b is reversed to bring LSB to the top of matrix
        a = bin(operand_a)[2:].zfill(bits)
        b = bin(operand_b)[2:].zfill(bits)[::-1]
        i = 0
        matrix = []
        for i in range(bits-1, -1, -1):
            if b[i] == '0':
                matrix.append(["_"]*(i+1) + ['0']*(bits) + ["_"]*(bits-i-1))
            elif b[i] == '1':
                matrix.append(["_"]*(i+1) + list(a) + ["_"]*(bits-i-1))
        return matrix, a, b # exposing operands for access as everthing uses generators

    @classmethod
    def pretty(cls, matrix: list[list[Any]]) -> str:
        """
        Format matrix as a string:

        >>> ____0000
        >>> ___0000_
        >>> __0000__
        >>> _0000___
        """
        pretty_ = ""
        for i in matrix:
            row = [str(x) for x in i]
            pretty_ += "".join(row) + "\n"
        return pretty_


    def __repr__(self) -> str:
        return self.pretty(self.matrix)

    def __str__(self) -> str:
        return str(self.__repr__())

    def __len__(self) -> int:
        return self.bits

    def __getitem__(self, index: int) -> list:
        return self.matrix[index]

    def __eq__(self, matrix: Any, /) -> bool:
        if matrix.bits != self.bits:
            return False
        for i in range(self.bits):
            if matrix[i] != self.matrix[i]:
                return False
        return True
