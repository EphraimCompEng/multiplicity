################################################
# Returns Template Objects Using User Patterns #
################################################

import copy
from typing import Any
from .utils.char import ischar




def build_simple_template(pattern: list[str]) -> list[list[str]]:
    """
    Build a simple template for a given bitwidth.
    >>> self.bits = 4
    >>> build_template(self.pattern)

    matrix = [  # pattern = [\n
    [____AaAa], #  'a',\n
    [___AaAa_], #  'a',\n
    [__BbBb__], #  'b',\n
    [_BbBb___], #  'b']\n
    ]
    """
    matrix = []

    return matrix

# Defining a new Template type for list[list[Any]] would be useful?

def build_csa(
    char: str, zeroed_slice: list[list[Any]]
) -> tuple[list, list]: # Carry Save Adder -> (template, result)
    """
    Create CSA template slice with zero initialised slice and chosen char.
    Returns template "slices" for a csa reduction and the resulting slice.\n
    [slice-] || [csa---] || [result]\n
    ____0000 || ____AaAa || __AaAaAa\n
    ___0000_ || ___aAaA_ || __aAaA__\n
    __0000__ || __AaAa__ || ________\n
    """
    if len(zeroed_slice) != 3:
        raise ValueError("Invalid template slice: must be 3 rows")

    # loop setup
    n = len(zeroed_slice[0])
    result = [['_']*n, ['_']*n, ['_']*n]
    csa_slice = copy.copy(zeroed_slice)
    tff = char == char.lower() # Toggle flip flop
    for i in range(n):
        # For int in template slice, map possible CSA operands to adder_slice
        # Then map possible outputs to result
        # [ bA + bB + bC = 0b00, 0b01, 0b10 ]
        # CSA auto maps Cout: FF, see templates/map.py
        csa_slice[0][i] = char if (y0:=csa_slice[0][i] != '_') else '_'
        csa_slice[1][i] = char if (y1:=csa_slice[1][i] != '_') else '_'
        csa_slice[2][i] = char if (y2:=csa_slice[2][i] != '_') else '_'
        result[0][i]    = char if 1 <= (y0+y1+y2) else '_'
        result[1][i-1]  = char if 1 <  (y0+y1+y2) else '_'
        tff  = not(tff) # True -> False -> True...
        char = char.lower() if tff else char.upper()
    return csa_slice, result


def build_adder(
    char: str, zeroed_slice: list[list[Any]]
) -> tuple[list, list]: # Carry Save Adder -> (template, result)
    """
    Create CSA template slice with zero initialised slice and chosen char.
    Returns template "slices" for addition and the resulting slice.\n
    [slice ] || [adder-] || [result]\n
    ___0000_ || ___aAaA_ || _aAaAaA_\n
    __0000__ || __AaAa__ || ________\n
    """
    if len(zeroed_slice) != 2:
        raise ValueError("Invalid template slice: must be 2 rows")

    # loop setup
    n = len(zeroed_slice[0])
    result = [['_']*n, ['_']*n]
    adder_slice = copy.copy(zeroed_slice) # ensure no references

    # -- TODO ------------------------------------------------------ #
    # tff + char startegy can be replace with an infinite generator: #
    # while True: yield outputs char.upper(); yeild char.lower       #
    # make and add to _utils?                                        #
    tff = (char == char.lower()) # Toggle flip flop                  #
    # -------------------------------------------------------------- #


    for i in range(n):
        # For int in template slice, map possible ADD operands to adder_slice
        # Then map possible outputs to result
        # [ bA + bB = 0b00, 0b01, 0b10, 0b11]
        adder_slice[0][i] = char if (y0:=adder_slice[0][i] != '_') else '_'
        adder_slice[1][i] = char if (y1:=adder_slice[1][i] != '_') else '_'
        result[0][i]      = char if y0 or y1 else '_'
        tff  = not(tff) # True -> False -> True...
        char = char.lower() if tff else char.upper()

    # Adding final carry
    tff      = not(tff) # Undo last flip to find last used tff value
    pre_char = char
    char     = char.lower() if tff else char.upper()
    index    = result[0].index(char)-1 # find first instance of char - 1
    result[0][index] = pre_char # Final carry place in result template

    return adder_slice, result



class Pattern:
    def __init__(self, pattern: list[str]):
        assert isinstance(pattern, list) and all(ischar(row) for row in pattern), (
            "Error: Invalid pattern format. Expected list[char]"
        )
        self.pattern = pattern

    def __str__(self):
        pretty_str = ""
        for p in self.pattern:
            pretty_str += " " + p + "\n"
        return f"{'['+ pretty_str[1:-2]+']'}"

class Template:
    # import string
    # cell = (ch for ch in string.ascii_lowercase)

    def __init__(self, template: list[Any], result: Any = None, map: Any = None): # Complex or simple
        from .. import SUPPORTED_BITWIDTHS
        valid_range  = SUPPORTED_BITWIDTHS
        self.len     = len(template)
        self.map     = map
        self.result  = result
        self.pattern = None
        self.template = None


        # length of any template represents it's bitwidth
        if len(template) not in valid_range:
            raise ValueError(f"Valid bit lengths: {valid_range}")
        if ischar(template[0]):
            self.pattern  = template
            self.template, self.result = build_simple_template(template)
        elif ischar(template[0][0]):
            self.template = template
            self.merged = None

    def merge(self, templates: list[Any]) -> None:
        """
        Merge multiple template slices into a single template.
        """
        assert isinstance(templates, list)
        # This looks terrible... Works tho?
        # templates[template[row[str]]]
        assert isinstance(templates[0][0][0][0], str)


        if len(templates) == 0:
            raise ValueError("No templates provided")

        self.merged = None # PLACEHOLDER #
        ...














"""
Complex templates implement decoders and bit-mapping.

Decoders reduce 4 or more bits at a time.

Bit mapping allows for outlining where bits are placed in each stage,
enabling complex implementations and possible optimisations.
"""
