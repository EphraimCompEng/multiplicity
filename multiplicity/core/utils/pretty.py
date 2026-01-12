from typing import Any

from multiply import Matrix, Slice, Map


def pretty(listy_object: Any) -> str:
    """
    Format matrix as a string:

    >>> ____0000
    >>> ___0000_
    >>> __0000__
    >>> _0000___
    """
    assert isinstance(listy_object, (Matrix, Slice, Map, list)), (
        "Unsupported type"
    )

    pretty_    = ""
    whitespace = " " if isinstance(listy_object, Map) else ""

    for i in listy_object:
        row = [str(x) + whitespace for x in i]
        pretty_ += "".join(row) + "\n"
    return str(pretty_)



def mprint(matrix: Any):
    """Print formatted Matrix object"""
    print(pretty(matrix))
