############################
# Map Bits Inside A Matrix #
############################


import multipy as mp
from typing import Any


class Map:

    def __init__(self, map: list[Any], bits: int) -> None:
        assert isinstance(map, list), ValueError("Map must be a list")
        assert bits in mp.SUPPORTED_BITWIDTHS, (
            ValueError(f"\tError: Unsupported bitwidth {bits}. Expected {mp.SUPPORTED_BITWIDTHS}")
        )
        self.bits = bits
        if isinstance(map[0], list):
            self.map = map
        elif isinstance(all(map), str):
            self.rmap = self.build_map(map)
        self.len = len(map)
        self._index = 0


    def build_map(self, simple: list[Any]) -> object:
        """
        Use simple map to generate standard map. Each element of simple map
        is a 2-bit, signed hex value. +ve = up, -ve = down.
        """

        ...
    def __repr__(self) -> str:
        return mp.pretty(self.map)

    def __str__(self) -> str:
        return str(self.__repr__())

    def __iter__(self):
        return iter(self.map)

    def __next__(self):
        if self._index >= self.len:
            raise StopIteration
        self._index += 1
        return self.map[self._index - 1]

def resolve_rmap(matrix: mp.Matrix, reversed: bool=False) -> Map:
    """
    Find empty rows, create simple map to efficiently pack rows.
    Defaults to bottom unless reversed=True.
    """
    ...

def build_dadda_map(bits) -> Map:
    from multipy import SUPPORTED_BITWIDTHS
    """
    Return map which represents starting point of Dadda tree algorithm.
    """
    assert bits in SUPPORTED_BITWIDTHS, (
        ValueError(f"\tError: Unsupported bitwidth {bits}. Expected {SUPPORTED_BITWIDTHS}")
    )

    # -- Repulsive - Design algorithm for 16-bit+ ------------------------------ #
    dadda_map = {                                                                #
        4: [                                                                     #
            ['00','00','00','00'] + ['00']*4,                                    #
            ['00','00','00','FF'] + ['00']*4,                                    #
            ['00','00','FE','FF'] + ['00']*4,                                    #
            ['00','FD','FE','FF'] + ['00']*4                                     #
        ],                                                                       #
        8: [                                                                     #
            ['00','00','00','00','00','00','00','00'] + ['00']*8,                #
            ['00','00','00','00','00','00','00','FF'] + ['00']*8,                #
            ['00','00','00','00','00','00','FE','FF'] + ['00']*8,                #
            ['00','00','00','00','00','FD','FE','FF'] + ['00']*8,                #
            ['00','00','00','00','FC','FD','FE','FF'] + ['00']*8,                #
            ['00','00','00','FB','FC','FD','FE','FF'] + ['00']*8,                #
            ['00','00','FA','FB','FC','FD','FE','FF'] + ['00']*8,                #
            ['00','F9','FA','FB','FC','FD','FE','FF'] + ['00']*8                 #
        ]                                                                        #
    }                                                                            #
    # -------------------------------------------------------------------------- #

    return Map(dadda_map[bits], bits)
