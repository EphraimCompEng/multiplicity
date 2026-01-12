############################
# Map Bits Inside A Matrix #
############################


import multiply as mp
from typing import Any


class Map:

    def __init__(self, map: list[Any]) -> None:
        assert isinstance(map, list), ValueError("Map must be a list")
        assert (bits := len(map)) in mp.SUPPORTED_BITWIDTHS, (
            (f"Unsupported bitwidth {bits}. Expected {mp.SUPPORTED_BITWIDTHS}")
        )
        self.bits = bits
        if isinstance(map[0], list):
            self.map = map
        elif all([isinstance(x, str) for x in map]):
            self.map  = self.build_map(map)
            self.rmap = map
        self._index = 0


    def build_map(self, rmap: list[str]) -> list[list[str]]:
        """
        Use row map to generate standard map. Each element of simple map
        is a 2-bit, signed hex value. +ve = up, -ve = down.
        """

        assert (n := len(rmap)) in mp.SUPPORTED_BITWIDTHS, (
            (f"Unsupported bitwidth {n}. Expected {mp.SUPPORTED_BITWIDTHS}")
        )
        map = []
        for i in range(n):
            if len(rmap[i]) != 2 and not(isinstance(rmap[i], str)):
                raise ValueError(f"Invalid row map element {rmap[i]}")
            map.append([rmap[i] for _ in range(n*2)])
        return map

    def __repr__(self) -> str:
        return mp.pretty(self.map)

    def __str__(self) -> str:
        return str(self.__repr__())

    def __iter__(self):
        return iter(self.map)

    def __next__(self):
        if self._index >= self.bits:
            raise StopIteration
        self._index += 1
        return self.map[self._index - 1]

# May remove reversed option
def resolve_rmap(matrix: mp.Matrix) -> Map:
    """
    Find empty rows, create simple map to efficiently pack rows.
    Defaults to bottom unless reversed=True.
    """
    offset = 0
    smap = []
    for i in matrix:
        if all([(b == '_' or b == '0') for b in i]):
            offset += 1
            smap.append("00")
            continue

        # Not sure how else to convert -ve int -> 2s comp hex
        smap.append(f"{hex(255-offset+1)[2:].upper()}")
    return Map(smap)


def build_dadda_map(bits) -> Map:
    """
    Return map which represents starting point of Dadda tree algorithm.
    """
    assert bits in mp.SUPPORTED_BITWIDTHS, (
        ValueError(f"\tError: Unsupported bitwidth {bits}. Expected {mp.SUPPORTED_BITWIDTHS}")
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

    return Map(dadda_map[bits])
