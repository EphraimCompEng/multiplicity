#!/usr/bin/env python
from collections import deque
from functools import cache
from pprint import pprint
import numpy as np
import json




class NpEncoder(json.JSONEncoder): # TIL json no like numpy
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)


@cache
def and_matrix(bits, x, y):
    """
    3 * 4 -> 0b0011 * 0b0100

    Generates:

        0011
    [___0000] 0
    [__0000_] 0
    [_0011__] 1
    [0000___] 0

    """

    max_value = (2**bits)-1
    if int(x) > max_value or int(y) > max_value:
        raise ValueError

    bin_x = f"{int(x):0{bits}b}"
    bin_y = f"{int(y):0{bits}b}"
    y_axis = list(bin_y)
    y_axis.reverse()
    and_matrix = []
    format_list = [('-'*n) for n in range(bits)]
    print(f"\t {bin_x}")
    for layer, y in enumerate(y_axis):
        if y == '1':
            formatted_x = format_list[-1-layer] + bin_x + format_list[layer]
        else:
            formatted_x = format_list[-1-layer] + '0'*(bits) + format_list[layer]


        print(layer, formatted_x, y)
        and_matrix.append(formatted_x)

    return and_matrix


def carry_save_layers():
    pass
def add_layers():
    pass

def operand_test_list(max_value, min_value=1, min_output_value=1, clamp=True):
    # if int(max_value) != 256:
    #     raise ValueError
    if int(max_value) < int(min_value):
        raise ValueError
    if int(max_value) < int(min_output_value):
        raise ValueError
    if min_value == 0:
        input_range = range(1, max_value)
    else:
        input_range = range(min_value, max_value)
    if clamp == True:
        clamp_value = 255
    else:
        clamp_value = max_value




    unordered_test_list = []
    for y in input_range: # find MSB of Y -> Shift X by position -> IF > clamp: next
        shift_distance = y.bit_length()-1
        for x in input_range:
            if (min_output_value <= x*y <= max_value) and (x << shift_distance) < clamp_value: # todo: dynamic parameter selection
                print(f"{y:b}", shift_distance)
                unordered_test_list.append((x, y))
            else:
                continue

    array = np.array(unordered_test_list, dtype=('uint8,uint8'))
    sorted_array = np.sort(array)
    # print(sorted_array)lamp == True:
    return sorted_array




def push_json(dictionary):
    """
    Push(?) a dictionary containing information about the multiply.
    Dict could contain any amount of layers: AND matrix, CSAs and Adds

        raise ValueError
    """
    pass

@cache
def main(): # Build the json
    """

    Here are scenarios I want to like to test:

    Type I
    a) Input values < 255
    b) Input pairs which do not cross overflow threshold during
       AND-matrix

       overflow|valid
       --------+-----------
        -------|00000000
        ------0|0000000-
        -----00|000000--
        ----000|00000---
        ---0000|0000----
        --00000|000-----
        -000000|00------
        0000000|0-------

    c) Input pairs which overflow in partial product reduction



    """

    test_list = operand_test_list(381, 3, 255) # Generate operands
    # print(test_list)
    # print(len(test_list))
    data = {}
    for i, xy_tuple in enumerate(test_list): # generate dict - just AND matrix

        print(i, xy_tuple)
        and_matrix_output = and_matrix(8, xy_tuple[0], xy_tuple[1])
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

main()
