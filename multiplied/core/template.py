################################################
# Returns Template Objects Using User Patterns #
################################################

from typing import Any
from .utils.char import ischar
import multiplied as mp
import copy






# Defining a new Template type for list[list[Any]] would be useful?

def build_csa(
    char: str, zeroed_slice: mp.Slice
) -> tuple[mp.Slice, mp.Slice]: # Carry Save Adder -> (template, result)
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
        #
        # Max bits per calculation = 1, therefore template result is:
        #
        # t = AaAa...
        #    AaAa...
        #
        # CSA auto maps Cout: FF, see templates/map.py
        csa_slice[0][i] = char if (y0:=csa_slice[0][i] != '_') else '_'
        csa_slice[1][i] = char if (y1:=csa_slice[1][i] != '_') else '_'
        csa_slice[2][i] = char if (y2:=csa_slice[2][i] != '_') else '_'
        result[0][i]    = char if 1 <= (y0+y1+y2) else '_'
        result[1][i-1]  = char if 1 <  (y0+y1+y2) else '_'
        tff  = not(tff) # True -> False -> True...
        char = char.lower() if tff else char.upper()
    return csa_slice, mp.Slice(result)


def build_adder(
    char: str, zeroed_slice: mp.Slice
) -> tuple[mp.Slice, mp.Slice]: # Carry Save Adder -> (template, result)
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
        # For int, [0, 1], in matrix slice, map possible ADD operands to
        # template_adder_slice
        # Then map possible outputs to result:
        # [ bA + bB = 0b0, 0b1]
        #
        # Max bits per calculation = 1, therefore template result is:
        #
        # t = AaAa...
        #

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

    return adder_slice, mp.Slice(result)

class Pattern:
    """

    """
    def __init__(self, pattern: list[str]):
        if not(isinstance(pattern, list) and all(ischar(row) for row in pattern)):
            raise ValueError("Error: Invalid pattern format. Expected list[char]")
        self.pattern = pattern

    def __str__(self):
        pretty_str = ""
        for p in self.pattern:
            pretty_str += " " + p + "\n"
        return f"{'['+ pretty_str[1:-2]+']'}"



class Template:
    """

    """
    # import string
    # cell = (ch for ch in string.ascii_lowercase)

    def __init__(self, template: list[Any], *,
        result: Any = None, map: Any = None, dadda: bool = False) -> None: # Complex or pattern
        self.len      = len(template)
        self.map      = map
        self.dadda    = dadda
        self.result   = result

        # length of any template represents it's bitwidth
        if len(template) not in mp.SUPPORTED_BITWIDTHS:
            raise ValueError(f"Valid bit lengths: {mp.SUPPORTED_BITWIDTHS}")
        if ischar(template[0]):
            self.pattern  = template
            self.init_base_template(self.pattern, self.dadda)
        elif ischar(template[0][0]):
            self.template = template
            self.pattern  = None
        else:
            raise ValueError(
                "Error: Invalid template format.\
                    Expected pattern: list[char] or template: list[list[str]]")

    def init_base_template(self, pattern: list[str], dadda=False) -> None:
        """
        Create template for zeroed matrix using pattern
        """


    # Templates must be built using thr current matrix
    def build_from_pattern(self, pattern: list[str], resultant: Any
    ) -> None:
        """
        Build a simple template for a given bitwidth based on matrix.
        Defaults to empty matrix if matrix=None.
        >>> self.bits = 4
        >>> build_template(self.pattern)

        [matrix] || [pattern]\n
        ____AaAa || ['a',\n
        ___AaAa_ ||  'a',\n
        __BbBb__ ||  'b',\n
        _BbBb___ ||  'b']\n
        """

        # -- sanity check -----------------------------------------------
        if not(isinstance(pattern, list)):
            raise ValueError("Pattern must be type list")
        if len(pattern) not in mp.SUPPORTED_BITWIDTHS:
            raise ValueError(
                f"Unsupported bitwidth {len(pattern)}. Expected {mp.SUPPORTED_BITWIDTHS}"
            )

        if isinstance(resultant, list):

        # -- find run ---------------------------------------------------
        template = {}
        i = 1
        while i < len(pattern):
            run = 1
            while pattern[i-1] == pattern[i]:
                run += 1
                i   += 1
            match run:
                case 1: # Do nothing
                    template[i-run] =
                case 2: # Create adder
                    ...
                case 3: # Create CSA row
                    ...
                case _:
                    raise ValueError(f"Unsupported run length {run}")

        matrix = []

        return matrix


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
