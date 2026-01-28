#################################
# Commonly Reused Sanity Checks #
#################################

from typing import Any


SUPPORTED_BITWIDTHS = {4, 8}


def validate_bitwidth(bits: int) -> None | ValueError:
    if not isinstance(bits, int) or bits not in SUPPORTED_BITWIDTHS:
       return ValueError(
            f"Unsupported bitwidth {bits}. Expected {SUPPORTED_BITWIDTHS}"
       )

def isint(source: Any) -> bool:
    """Return True if source converts to int"""
    match source:
        case int():
            return True
        case str():
            try:
                int(source)
                return True
            except ValueError:
                return False
        case _:
            return False


def ishex2(val: str) -> bool:
    """Return True if string represents a 2-bit hex value"""
    if 2 < len(val) or not(0 <= int(val, 16) <= 255):
        return False
    return True

def ischar(ch: str) -> bool:
    """Return True if string is exactly one alphabetic character"""
    try:
        ord(ch)
        return True
    except (ValueError, TypeError):
        return False
