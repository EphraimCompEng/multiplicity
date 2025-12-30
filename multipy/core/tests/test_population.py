################################
# Import Modules Without Error #
################################

import multipy as mp

def test_empty_matrix():
    matrix = mp.Matrix(8)
    assert matrix == matrix
    assert matrix.matrix == [
        ['_', '_', '_', '_', '_', '_', '_', '_', 0, 0, 0, 0, 0, 0, 0, 0],
        ['_', '_', '_', '_', '_', '_', '_', 0, 0, 0, 0, 0, 0, 0, 0, '_'],
        ['_', '_', '_', '_', '_', '_', 0, 0, 0, 0, 0, 0, 0, 0, '_', '_'],
        ['_', '_', '_', '_', '_', 0, 0, 0, 0, 0, 0, 0, 0, '_', '_', '_'],
        ['_', '_', '_', '_', 0, 0, 0, 0, 0, 0, 0, 0, '_', '_', '_', '_'],
        ['_', '_', '_', 0, 0, 0, 0, 0, 0, 0, 0, '_', '_', '_', '_', '_'],
        ['_', '_', 0, 0, 0, 0, 0, 0, 0, 0, '_', '_', '_', '_', '_', '_'],
        ['_', 0, 0, 0, 0, 0, 0, 0, 0, '_', '_', '_', '_', '_', '_', '_']
    ]

def test_build_matrix():
    matrix         = mp.Matrix(8)
    mult_by_zero_a = mp.Matrix(8)
    mult_by_zero_b = mp.Matrix(8)
    # exceed_matrix  = mp.Matrix(8)

    matrix.build_matrix(0, 0, 8)
    mult_by_zero_a.build_matrix(0, 42, 8)
    mult_by_zero_b.build_matrix(42, 0, 8)
    assert matrix.bits   == mult_by_zero_a.bits
    assert matrix.bits   == mult_by_zero_b.bits
    # print(vars(matrix))
    # print(vars(mult_by_zero_a))
    # print(vars(mult_by_zero_b))

def test_agorithm():
    temp1 = mp.Matrix(8) # Placeholder for template
    temp2 = mp.Matrix(8) # Placeholder for template
    arg   = [temp1, temp2]
    alg   = mp.Algorithm(temp1)
    alg.populate(arg)

    print(alg.bits)
    print(alg)
    # print(temp1.bits)
    # print(temp2.bits)


def main() -> None:
    test_empty_matrix()
    test_build_matrix()
    test_agorithm()

if __name__ == "__main__":
    main()
