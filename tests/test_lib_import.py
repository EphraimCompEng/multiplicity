#####################
# Temp Testing File #
#####################







from functools import cache
from pprint import pprint
from typing import Any
import numpy as np
import multipy as mp
import json


# When using json, it  not lot like to interact with numpy
# This was the solution I saw online, no source sadly, this was years ago.
# Unlikely to change this as MultiPY will move to .parquet files.
class NpEncoder(json.JSONEncoder):
    def default(self, obj: Any) -> Any: # No idea how to type this, just using Any
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj) # When obj is made wrap in default???

@cache # Once again, never used timings to test how much this helped
def main() -> None: # Build the json
    """

    Here are scenarios I want to like to test:

    Type I
    a) Input values < 255
    b) Input pairs which do not cross overflow threshold during
       AND-matrix

    >>> # overflow|valid
    >>> # --------+--------
    >>> # --------|00000000
    >>> # -------0|0000000-
    >>> # ------00|000000--
    >>> # -----000|00000---
    >>> # ----0000|0000----
    >>> # ---00000|000-----
    >>> # --000000|00------
    >>> # -0000000|0-------

    c) Input pairs which overflow in partial product reduction



    """

    test_list = mp.operand_test_list(381, 3, 255) # Generate operands
    # print(test_list)
    # print(len(test_list))
    data = {}
    for i, xy_tuple in enumerate(test_list): # generate dict - just AND matrix

        print(i, xy_tuple)
        and_matrix_output = mp.and_matrix(8, xy_tuple[0], xy_tuple[1])
        result = int(xy_tuple[0])*int(xy_tuple[1])
        data[i] = {
            '_operands': str(xy_tuple),
            'result': result,
            'result_bin': f"{result:08b}",
            'and_matrix': and_matrix_output,
            'layer_0': { # Real structure tbd as multiple CSAs and ADDs can happen at each layer
                'add_0': '',
                'output': {}
                },
            }
    pprint(data)
    # test_json = json.dumps(data, cls=NpEncoder)
    filename = 'smul_partial_gte_255_lte_381.json'

    with open(filename, 'w') as outfile: # add duplicate filename stuff
        json.dump(data, outfile, cls=NpEncoder, indent=4)

    # matrix = and_matrix(8, input("x: "), input("y: ")) # deque of AND matrix
    # pprint(matrix)

if __name__ == "__main__":
    main()
