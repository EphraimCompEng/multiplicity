#################################
# Commonly Reused Sanity Checks #
#################################

SUPPORTED_BITWIDTHS = {4, 8}


# TODO: lists[list[char]]



# TODO: lists[list[hex2]]



# TODO: SUPPORTED BITWIDTH
def validate_bitwidth(bits: int) -> None | ValueError:
    if not isinstance(bits, int) or bits not in SUPPORTED_BITWIDTHS:
       return ValueError(
            f"Unsupported bitwidth {bits}. Expected {SUPPORTED_BITWIDTHS}"
       )

# TODO: ?
