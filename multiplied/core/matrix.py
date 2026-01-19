###################################################
# Classes to Represent Matrices and Matrix Slices #
###################################################

import multiplied as mp
from typing import Any, Iterator

class Slice:
    """

    """
    def __init__(self, matrix: list[list[str]]):
        self.bits   = len(matrix[0]) >> 1
        if self.bits not in mp.SUPPORTED_BITWIDTHS:
            raise ValueError(
                f"Unsupported bitwidth {self.bits}. Expected {mp.SUPPORTED_BITWIDTHS}"
            )
        self.slice  =  matrix
        self._index = 0
        self.len    = len(self.slice)

    def __getitem__(self, index: int) -> list[str]:
        return self.slice[index]


    def _repr_(self):
        return self.__str__()

    def __str__(self):
        return str(mp.pretty(self.slice))

    def __len__(self) -> int:
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
    def __init__(self, source: Any, *, a: int=0, b: int=0) -> None:

        if isinstance(source, int) and (source not in mp.SUPPORTED_BITWIDTHS):
            raise ValueError(
                f"Unsupported bitwidth {source}. Expected {mp.SUPPORTED_BITWIDTHS}"
            )
        if isinstance(source, list) and (len(source) not in mp.SUPPORTED_BITWIDTHS):
            raise ValueError(
                f"Unsupported bitwidth {len(source)}. Expected {mp.SUPPORTED_BITWIDTHS}"
            )

        if all([isinstance(a, int), isinstance(b, int), (a != 0 or b != 0)]):
            if not isinstance(source, int):
                raise ValueError("Invalid input, ")
            self.bits = source
            self.matrix = build_matrix(a, b, source).matrix
        elif isinstance(source, int):
            self.bits = source
            self.__empty_matrix(source)
        elif all([isinstance(row, (list, Slice)) for row in source]):
            if len(source)*2 != len(source[0]):
                raise ValueError("Matrix must be 2m * m")
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
            if matrix.matrix[i] != self.matrix[i]:
                return False
        return True

    def __getitem__(self, index: slice) -> Slice:
        slice = self.matrix[index]
        if len(slice) == 1:
            slice = list(slice)
        return mp.Slice(slice)

    def __iter__(self):
        return iter(self.matrix)

    def __next__(self):
        if self._index >= self.bits:
            raise StopIteration
        self._index += 1
        return self.matrix[self._index - 1]


    def apply_map(self, map: mp.Map) -> None:
        if not isinstance(map, mp.Map):
            raise TypeError(f"Expected Map, got {type(map)}")
        if map.bits != self.bits:
            raise ValueError(f"Map bitwidth {map.bits} does not match matrix bitwidth {self.bits}")
        if rmap := map.rmap:
            temp_matrix = Matrix(self.bits).matrix
            for i in range(self.bits):
                if (val := int(rmap[i], 16)) and 128: # -ve 2-bit hex value
                    val = (val ^ 255 + 1) - 512 # 2s complement
                temp_matrix[i+val] = self.matrix[i]
                temp_matrix[i]     = "_"*self.bits*2
            self.matrix = temp_matrix
        else:
            raise NotImplementedError("Complex mapping not implemented")





def build_matrix(operand_a: int, operand_b: int, bits: int) -> Matrix:
    """
    Build Logical AND matrix using source operands.
    """
    if bits not in mp.SUPPORTED_BITWIDTHS:
        raise ValueError(
            f"Unsupported bitwidth {bits}. Expected {mp.SUPPORTED_BITWIDTHS}"
        )
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
