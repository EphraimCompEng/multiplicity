################################
# Import Modules Without Error #
################################

import multipy as mp

def test_empty_matrix():
    matrix = mp.MpMatrix(8)
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
    matrix         = mp.MpMatrix(8)
    mult_by_zero_a = mp.MpMatrix(8)
    mult_by_zero_b = mp.MpMatrix(8)
    # exceed_matrix  = mp.MpMatrix(8)

    matrix.build_matrix(0, 0)
    mult_by_zero_a.build_matrix(0, 42)
    mult_by_zero_b.build_matrix(42, 0)
    assert matrix.bits   == mult_by_zero_a.bits
    assert matrix.bits   == mult_by_zero_b.bits

def test_agorithm():
    temp1 = mp.MpMatrix(8) # Placeholder for template
    temp2 = mp.MpMatrix(8) # Placeholder for template
    alg   = mp.Algorithm()
    arg   = [temp1, temp2]
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
