from collections.abc import Generator


# --  Character related helper functions ----------------------------

def ischar(ch: str) -> bool:
    """Tests if a string is exactly one alphabetic character"""
    try:
        ord(ch)
        return True
    except (ValueError, TypeError):
        return False

def chargen() -> Generator[str]:
    """Continuously generate characters from A to Z."""
    i = 0
    while True:
        yield chr((i % 26) + 65)
        i += 1

def chartff(ch: str) -> Generator[str]:
    """
    Infinitely generate char in upper then lowercase form.

    >>> x = chartff('a')
    >>> next(x)
    'a'
    >>> next(x)
    'A'
    >>> next(x)
    'a'
    """

    if not ischar(ch):
        raise ValueError("Input must be a single alphabetic character")

    i = True
    while True:
        if i := not(i):
            yield ch.lower()
        else:
            yield ch.upper()

def allchars(matrix: list[list[str]]) -> set[str]:
    """
    Generate all unique characters from a matrix.
    Ignores '_' and returns char.upper().

    >>> allchars([['A', 'B'], ['C', 'D']])
    {'A', 'B', 'C', 'D'}
    """
    if not isinstance(matrix, list) or not all([isinstance(row, list) for row in matrix]):
        raise TypeError("Input must be a list of lists")
    chars = set(ch for row in matrix for ch in row)
    chars.remove('_')
    return set(ch.upper() for ch in chars)
