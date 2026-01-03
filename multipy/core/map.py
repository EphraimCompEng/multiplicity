##################################
# Map, Swap Bits Inside A Matrix #
##################################




###
# Simple maps move entire rows
###
#
# import multipy as mp
# from typing import Any


def build_map(
) -> list[list[int]]:
    """
    A map matrix holds signed hexadecimal numbers representing a vertical
    offset for a given bit when applied to an algorithm.

    [matrix] || [map---] || [effect]
     _ 0 1 > || 00 02 01 || > _ 1 _
     0 1 _ > || 00 FF 00 || > 0 _ 1
     _ _ _ > || 00 00 00 || > _ 0 _
    """
    ...

def build_dadda_map():
    """
    Return map to collect partial products into an upside down triangle:
    a prerequisite for the dadda algorithm.
    """
    ...

def build_simple_map():
    """
    """
    ...
