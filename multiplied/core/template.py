################################################
# Returns Template Objects Using User Patterns #
################################################

from typing import Any
from .utils.char import ischar
import multiplied as mp
import copy



def build_csa(
    char: str, zeroed_slice: mp.Slice
) -> tuple[mp.Slice, mp.Slice]: # Carry Save Adder -> (template, result)
    """
    Create CSA template slice with zero initialised slice and chosen char.
    Returns template "slices" for a csa reduction and the resulting slice.

    >>> [slice-] || [csa---] || [result]
    >>> ____0000 || ____AaAa || __AaAaAa
    >>> ___0000_ || ___aAaA_ || __aAaA__
    >>> __0000__ || __AaAa__ || ________
    """
    if len(zeroed_slice) != 3:
        raise ValueError("Invalid template slice: must be 3 rows")

    # loop setup
    n         = len(zeroed_slice[0])
    tff       = mp.chartff(char) # Toggle flip flop
    result    = [['_']*n, ['_']*n, ['_']*n]
    csa_slice = copy.copy(zeroed_slice)

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
        char = next(tff)
    return csa_slice, mp.Slice(result)


def build_adder(
    char: str, zeroed_slice: mp.Slice
) -> tuple[mp.Slice, mp.Slice]: # Carry Save Adder -> (template, result)
    """
    Create Adder template slice with zero initialised slice and chosen char.
    Returns template "slices" for addition and the resulting slice.
    >>> [slice ] || [adder-] || [result]
    >>> ___0000_ || ___aAaA_ || _aAaAaA_
    >>> __0000__ || __AaAa__ || ________
    """
    if len(zeroed_slice) != 2:
        raise ValueError("Invalid template slice: must be 2 rows")

    # loop setup
    n           = len(zeroed_slice[0])
    tff         = mp.chartff(char) # Toggle flip flop
    result      = [['_']*n, ['_']*n]
    adder_slice = copy.copy(zeroed_slice) # ensure no references

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
        char = next(tff)

    # Adding final carry
    pre_char = char
    char     = next(tff)
    index    = result[0].index(char)-1 # find first instance of char - 1
    result[0][index] = pre_char # Final carry place in result template

    return adder_slice, mp.Slice(result)

def build_noop(
    char: str, zeroed_slice: mp.Slice
) -> tuple[mp.Slice, mp.Slice]:
    """
    Create a No-op template slice with zero initialised slice and chosen char.
    Returns template "slices" and resulting slice. Target row unaffected
    >>> [slice ] || [noop  ] || [result]
    >>> ___0000_ || ___aAaA_ || ___aAaA_
    """
    if len(zeroed_slice) != 1:
        raise ValueError("Invalid template slice: must be 1 rows")

    n           = len(zeroed_slice[0])
    tff         = mp.chartff(char) # Toggle flip flop
    noop_slice  = copy.copy(zeroed_slice) # ensure no references
    for i in range(n):
        noop_slice[0][i] = char if (noop_slice[0][i] != '_') else '_'
        char = next(tff)

    # (noop_slice, noop_slice) == tuple both pointing to one object.
    return noop_slice, copy.copy(noop_slice)

    ...

class Pattern:
    """

    """
    def __init__(self, pattern: list[str]):
        if not(isinstance(pattern, list) and all(ischar(row) for row in pattern)):
            raise ValueError("Error: Invalid pattern format. Expected list[char]")
        self.pattern = pattern
        self.bits    = len(pattern)



    def get_runs(self) -> list[tuple[int, int, int]]:
        """
        Returns list of tuples of length, position, and run of a given char in pattern
        """
        metadata = []
        i = 1
        k = 0
        while i < len(self.pattern):
            run = 1
            while i < len(self.pattern) and self.pattern[i-1] == self.pattern[i]:
                run += 1
                i   += 1
            if run < 4:
                metadata.append((None, i-run, run))
            else:
                raise ValueError(f"Unsupported run length {run}")
            i += 1
            k += 1
        return metadata

    def __str__(self):
        pretty_ = ""
        for p in self.pattern:
            pretty_ += " " + p + "\n"
        return f"{'['+ pretty_[1:-2]+']'}"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return self.bits

    def __getitem__(self, index: int) -> str:
        return self.pattern[index]

class Template:
    """

    """

    def __init__(self,
        source: Pattern | list[list[str]], *,
        map: Any    = None,
        dadda: bool = False,
        result: Any = None,
    ) -> None: # Complex or pattern

        self.map    = map
        self.bits   = len(source)
        self.dadda  = dadda
        self.result = result if isinstance(result, Template) else None

        # length of any template represents it's bitwidth
        if self.bits not in mp.SUPPORTED_BITWIDTHS:
            raise ValueError(f"Valid bit lengths: {mp.SUPPORTED_BITWIDTHS}")
        if isinstance(source, Pattern):
            self.pattern  = source
            matrix = mp.Matrix(self.bits)
            if dadda:
                # TODO
                raise NotImplementedError("Applying maps not implemented")
            self.build_from_pattern(self.pattern, matrix)
        elif ischar(source[0][0]):
            self.template = source
            self.pattern  = None
        else:
            raise ValueError(
                "Error: Invalid template format.\
                \tExpected pattern: list[char], or template: list[list[str]]")

    def __str__(self) -> str:
        return f"{mp.pretty(self.template)}\n{mp.pretty(self.result)}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.template}, {self.result})"

    def __len__(self):
        return len(self.template)

    def init_base_template(self, pattern: Pattern, *, dadda=False) -> None:
        """
        Create template for zeroed matrix using pattern
        """


    # Templates must be built using matrix
    def build_from_pattern(self, pattern: Pattern, matrix: mp.Matrix
    ) -> None:
        """
        Build a simple template for a given bitwidth based on matrix.
        Defaults to empty matrix if matrix=None.
        >>> self.bits = 4
        >>> build_template(self.pattern)

        >>> [matrix] || [pattern]
        >>> ____AaAa || ['a',
        >>> ___AaAa_ ||  'a',
        >>> __BbBb__ ||  'b',
        >>> _BbBb___ ||  'b']
        """

        # -- sanity check -----------------------------------------------
        if not(isinstance(pattern, Pattern)):
            raise ValueError("Expected Pattern")
        if len(pattern) not in mp.SUPPORTED_BITWIDTHS:
            raise ValueError(
                f"Unsupported bitwidth {len(pattern)}. Expected {mp.SUPPORTED_BITWIDTHS}"
            )

        # -- find run ---------------------------------------------------
        template_slices = {}
        i = 1
        while i < len(pattern):
            run = 1
            while i < len(pattern) and pattern[i-1] == pattern[i]:
                run += 1
                i   += 1
            match run:
                case 1: # Do nothing
                    template_slices[i-run] = build_noop(pattern[i-run], matrix[i-run:i])
                case 2: # Create adder
                    template_slices[i-run] = build_adder(pattern[i-run], matrix[i-run:i])
                case 3: # Create CSA row
                    template_slices[i-run] = build_csa(pattern[i-run], matrix[i-run:i])
                case _:
                    raise ValueError(f"Unsupported run length {run}")
            i += 1

        # -- build template and resultant ---------------------------
        template = []
        for i in template_slices.values():
            template += i[0]
        result = []
        for i in template_slices.values():
            result += i[1]
        self.template, self.result = template, result



    # To be used in complex template results
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

Bit mapping defines where bits are placed in each stage,
enabling complex implementations and possible optimisations.
"""
