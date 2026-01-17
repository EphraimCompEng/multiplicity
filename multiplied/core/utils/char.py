from collections.abc import Generator


# --  Character related helper functions ----------------------------

def ischar(ch:str) -> bool:
    """
    Tests if a string is exactly one alphabetic character
    """
    try:
        ord(ch)
        return True
    except (ValueError, TypeError):
        return False

def chargen() -> Generator[str]:
    """
    Continuously generate characters from A to Z.
    """
    i = 0
    while True:
        yield chr((i % 26) + 65)
        i += 1

def chartff(char_) -> Generator[str]:
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
    i = True
    while True:
        if i := not(i):
            yield char_.lower()
        else:
            yield char_.upper()





# -- testing --------------------------------------------------------
def main():
    testgen = chargen()
    for _ in range(32):
        tmp = next(testgen)
        testtff = chartff(tmp)
        for _ in range(8):
            print(next(testtff), end='')
        print(tmp)

if __name__ == "__main__":
    main()
