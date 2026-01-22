import multiplied as mp


def test_step() -> None:
    m = mp.Matrix(4, a=5, b=4)
    p = mp.Pattern([
        'a',
        'a',
        'b',
        'b',
    ])
    alg = mp.Algorithm(m)

    print(alg)


def test_auto_resolve_single_4() -> None:
    m = mp.Matrix(4)
    p = mp.Pattern([
        'a',
        'a',
        'b',
        'b',
    ])
    alg = mp.Algorithm(m)
    alg.push(p)
    print(alg)
    # alg.auto_resolve_pattern(p, m)
    t2 = mp.Template(mp.Pattern(['a','a','b','c']), matrix=alg.algorithm[0]['pseudo'])
    alg.push(t2)
    print(alg)


def test_auto_resolve_single_8() -> None:
    m = mp.Matrix(8)
    p = mp.Pattern([
        'a',
        'a',
        'a',
        'b',
        'b',
        'b',
        'c',
        'c',
    ])
    alg = mp.Algorithm(m)
    alg.push(p)
    # alg.auto_resolve_pattern(p, m)
    t2 = mp.Template(mp.Pattern(['a','a','a','b','b','b','c','d']), matrix=alg.algorithm[0]['pseudo'])
    alg.push(t2)
    print(alg)


def test_auto_resolve_recursive_full() -> None:
    m   = mp.Matrix(4, a=5, b=7)
    alg = mp.Algorithm(m)
    alg.auto_resolve_stage()
    # print(alg)
    m2   = mp.Matrix(8, a=5, b=7)
    alg2 = mp.Algorithm(m2)
    alg2.auto_resolve_stage()
    print(alg2)

def test_auto_resolve_recursive_partial() -> None:
    ...


def main():
    test_auto_resolve_single_4()
    test_auto_resolve_recursive_full()

if __name__ == "__main__":
    main()
