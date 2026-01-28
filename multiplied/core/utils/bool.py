#################################
# Commonly Reused Sanity Checks #
#################################

SUPPORTED_BITWIDTHS = {4, 8}


def validate_bitwidth(bits: int) -> None | ValueError:
    if not isinstance(bits, int) or bits not in SUPPORTED_BITWIDTHS:
       return ValueError(
            f"Unsupported bitwidth {bits}. Expected {SUPPORTED_BITWIDTHS}"
       )

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
