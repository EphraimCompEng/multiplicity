####################################################
# Generating, Testing, and Manipulating Characters #
####################################################

from collections.abc import Generator


def chargen() -> Generator[str]:
    """Continuously generate characters from A to Z"""

    i = 0
    while True:
        yield chr((i % 26) + 65)
        i += 1

def chartff(ch: str) -> Generator[str]:
    """
    Generator to flip flop between upper and lowercase characters.

    >>> x = chartff('a')
    >>> next(x)
    'a'
    >>> next(x)
    'A'
    >>> next(x)
    'a'
    """
    from .bool import ischar

    if not ischar(ch):
        raise ValueError("Input must be a single alphabetic character")

    i = True
    while True:
        if i := not(i): # toggle flip flop
            yield ch.lower()
        else:
            yield ch.upper()

def allchars(matrix: list[list[str]], *, hash = []) -> set[str]:
    """
    Returns set of unique characters from a matrix.
    Ignores underscore characters and converts characters to uppercase

    >>> allchars([['A', 'B'], ['C', 'D']])
    {'A', 'B', 'C', 'D'}

    options:
        hash: use checksum to assist in calculations
    """
    if not isinstance(matrix, list) or not all([isinstance(row, list) for row in matrix]):
        raise TypeError("Input must be type list[list[char]]")

    if not hash:
        # By no means efficient, but gets the job done.
        # Maybe integrated into __reduce()?

        chars = set(ch for row in matrix for ch in row)
        chars.remove('_')
        return set(ch.upper() for ch in chars)

    else:
        if (h := len(hash)) != (m := len(matrix)):
            raise ValueError(f"Hash(len={h}) and matrix(len={m}) lengths do not match")
        subset = []
        for i, j in enumerate(hash):
            if j:
                subset.append(matrix[i])
        chars = set(ch for row in subset for ch in row)
        chars.remove('_')
        return set(ch.upper() for ch in chars)
