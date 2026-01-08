##################################
# Map, Swap Bits Inside A Matrix #
##################################




###
# Simple maps move entire rows
###

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
        else:
            self.map = self.build_map(map)


    def build_map(self, simple: list[Any]) -> object:
        """
        Use simple map to generate standard map. Each element of simple map
        is a 2-bit, signed hex value. +ve = up, -ve = down.
        """

        ...

def build_simple_map(matrix: mp.Matrix, reversed: bool=False) -> object:
    """
    Find empty rows, create simple map to efficiently pack rows.
    Defaults to bottom unless reversed=True.
    """
    ...

def build_dadda_map(bits) -> object:
    """
    Return map which represents starting point of Dadda tree algorithm.
    """
    assert bits in mp.SUPPORTED_BITWIDTHS, (
        ValueError(f"\tError: Unsupported bitwidth {bits}. Expected {mp.SUPPORTED_BITWIDTHS}")
    )

    # -- Repulsive - Design algorithm for 16-bit+ --------------------------------------------- #
    dadda_map = {                                                                               #
        4: [                                                                                    #
            ['00','00','00','00','00','00','00','00'],                                          #
            ['00','00','00','FF','00','00','00','00'],                                          #
            ['00','00','FE','FF','00','00','00','00'],                                          #
            ['00','FD','FE','FF','00','00','00','00']                                           #
        ],                                                                                      #
        8: [                                                                                    #
            ['00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00'],  #
            ['00','00','00','00','00','00','00','FF','00','00','00','00','00','00','00','00'],  #
            ['00','00','00','00','00','00','FE','FF','00','00','00','00','00','00','00','00'],  #
            ['00','00','00','00','00','FD','FE','FF','00','00','00','00','00','00','00','00'],  #
            ['00','00','00','00','FC','FD','FE','FF','00','00','00','00','00','00','00','00'],  #
            ['00','00','00','FB','FC','FD','FE','FF','00','00','00','00','00','00','00','00'],  #
            ['00','00','FA','FB','FC','FD','FE','FF','00','00','00','00','00','00','00','00'],  #
            ['00','F9','FA','FB','FC','FD','FE','FF','00','00','00','00','00','00','00','00']   #
        ]                                                                                       #
    }                                                                                           #
    # ----------------------------------------------------------------------------------------- #

    return Map(dadda_map[bits], bits)
