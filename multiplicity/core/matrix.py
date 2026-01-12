import multiplicity as mp
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


    def _repr_(self):
        return mp.pretty(self.slice)

    def __str__(self):
        return str(self._repr_())

    def __len__(self) -> int:
        print(len(self.slice))
        return len(self.slice)

    def __iter__(self) -> Iterator:
        return self

    def __next__(self):
        if self._index >= self.len:
            raise StopIteration
        self._index += 1
        return self.slice[self._index - 1]






class Matrix:
    """

    """
    def __init__(self, source: Any) -> None:
        if isinstance(source, int):
            assert source in mp.SUPPORTED_BITWIDTHS, (
                f"Unsupported bitwidth {source}. Expected {mp.SUPPORTED_BITWIDTHS}"
            )
            self.bits = source
            self.__empty_matrix(source)
        elif all([isinstance(s, list) for s in source]):
            assert len(source) in mp.SUPPORTED_BITWIDTHS,(
                f"Unsupported bitwidth {len(source)}. Expected {mp.SUPPORTED_BITWIDTHS}"
        )
            assert len(source)*2 == len(source[0]), "Matrix must be 2m * m"
            self.bits = len(source)
            self.matrix = source

        self._index = 0


    def __empty_matrix(self, bits: int) -> None:
        """
        Build a wallace tree style logic AND matrix for a bitwidth of self.bits.
        """
        row = [0]*bits
        matrix = []
        for i in range(bits):
            matrix.append(["_"]*(bits-i) + row + ["_"]*i)
        self.matrix = matrix

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

    # def __getslice__(self, start: int=0, stop: int=0) -> Slice:
    #     slice = self.matrix[start:stop]
    #     print(slice)
    #     return mp.Slice(slice)

    def __getitem__(self, index: slice) -> Slice:
        return mp.Slice(self.matrix[index])

    def __iter__(self):
        return iter(self.matrix)

    def __next__(self):
        if self._index >= self.bits:
            raise StopIteration
        self._index += 1
        return self.matrix[self._index - 1]




def build_matrix(operand_a: int, operand_b: int, bits: int) -> Matrix:
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
    return Matrix(matrix)
