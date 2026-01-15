






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
