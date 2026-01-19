import multiplied as mp

def test_auto_resolve_single() -> None:
    m = mp.Matrix(4)
    p = mp.Pattern([
        'a',
        'a',
        'b',
        'b',
    ])
    alg = mp.Algorithm(m)
    print(alg)
    alg.auto_resolve_pattern(p, m)

def test_auto_resolve_recursive_full() -> None:
    ...

def test_auto_resolve_recursive_partial() -> None:
    ...


def main():
    test_auto_resolve_single()

if __name__ == "__main__":
    main()
