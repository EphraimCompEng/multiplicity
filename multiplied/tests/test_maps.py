import multiplied as mp

def test_dadda_map(bits) -> None:
    try:
        mp.build_dadda_map(0)
    except AssertionError:
        pass
    m = mp.build_dadda_map(bits)
    mp.mprint(m)

def test_resolve_simple_map() -> None:
    sm = mp.Map(
        [
            '00',
            'FF',
            'FF',
            'FF',
        ]
    )
    mp.mprint(sm)
    m1 = mp.build_matrix(5, 5, 4)
    mp.mprint(m1)
    m1map = mp.resolve_rmap(m1)
    mp.mprint(m1map)

def test_empty_map(bits: int) -> None:
    m = mp.empty_map(bits)
    mp.mprint(m)


def main():
    test_dadda_map(8)
    test_resolve_simple_map()
    test_empty_map(16)

if __name__ == "__main__":
    main()
