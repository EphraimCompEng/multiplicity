import multipy as mp
from typing import Any, Iterator

class Slice:
    """

    """
    def __init__(self, matrix: list[list[str]]):
        self.slice  =  matrix
        self.bits   = len(self.slice[0][0]) >> 1
        self._index = 0
        self.len    = len(self.slice)

    def __getitem__(self, index: int) -> list[str]:
        return self.slice[index]

    def __iter__(self) -> Iterator:
        return self

    def _repr_(self):
        return mp.pretty(self.slice)

    def __str__(self):
        return str(self._repr_())

    def __next__(self):
        if self._index >= self.len:
            raise StopIteration
        self._index += 1
        return self.slice[self._index - 1]






class Matrix:
    """

    """
    def __init__(self, bits: int):
        valid_range = mp.SUPPORTED_BITWIDTHS
        self.bits   = bits
        self._index = 0

        if bits not in valid_range:
            raise ValueError(f"Valid bit lengths: {valid_range}")
        self.matrix = self.__empty_matrix()
        self.len    = len(self.matrix)

    def __empty_matrix(self) -> list[list[str]]:
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




    def __repr__(self) -> str:
        return mp.pretty(self.matrix)

    def __str__(self) -> str:
        return str(self.__repr__())

    def __len__(self) -> int:
        return self.bits


    def __eq__(self, matrix: Any, /) -> bool:
        if matrix.bits != self.bits:
            return False
        for i in range(self.bits):
            if matrix[i] != self.matrix[i]:
                return False
        return True

    def __getslice__(self, start: int, stop: int) -> Slice:
        slice = self.matrix[start:stop]
        return mp.Slice(slice)

    def __getitem__(self, index: int) -> Slice:
        return mp.Slice([self.matrix[index]])

    def __iter__(self):
        return iter(self.matrix)

    def __next__(self):
        if self._index >= self.len:
            raise StopIteration
        self._index += 1
        return self.matrix[self._index - 1]
