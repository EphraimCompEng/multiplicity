import multiplied as mp



def gen_resources(bits: int, *, a=0, b=0
) -> tuple[mp.Matrix, mp.Pattern, mp.Algorithm]:
    m = mp.Matrix(bits)
    match bits:
        case 4:
            p = mp.Pattern(['a','a','b','b',])
        case 8:
            p = mp.Pattern(['a','a','a','b','b','b','c','d'])
        case _:
            raise ValueError(f"Unsupported number of bits: {bits}")
    alg = mp.Algorithm(m)
    return m, p, alg

def test_step() -> None:
    m = mp.Matrix(4, a=5, b=4)
    p = mp.Pattern(['a','a','b','b'])
    alg = mp.Algorithm(m)
    alg.push(p)
    alg.step()

    print(alg)


def test_auto_resolve_single_4() -> None:
    m = mp.Matrix(4)
    p = mp.Pattern(['a','a','b','b'])
    alg = mp.Algorithm(m)
    alg.push(p)
    print(alg)
    # alg.auto_resolve_pattern(p, m)
    t2 = mp.Template(mp.Pattern(['a','a','b','c']), matrix=alg.algorithm[0]['pseudo'])
    alg.push(t2)
    print(alg)


def test_manual_population_8() -> None:
    m = mp.Matrix(8)
    p = mp.Pattern(['a','a','b','b','c','c','d','d'])
    alg = mp.Algorithm(m)
    alg.push(p)
    print(alg)
    # alg.auto_resolve_pattern(p, m)
    t2 = mp.Template(mp.Pattern(['a','a','b','b','_','_','_','_']), matrix=alg.algorithm[0]['pseudo'])
    alg.push(t2)
    t3 = mp.Template(mp.Pattern(['a','a','_','_','_','_','_','_']), matrix=alg.algorithm[1]['pseudo'])
    alg.push(t3)
    # print(alg)


def test_auto_resolve_recursive_full() -> None:
    m, p, alg = gen_resources(4, a= 6, b=7)
    alg.auto_resolve_stage()
    print(alg)

    m, p, alg2 = gen_resources(8, a=12, b=42)
    alg2.auto_resolve_stage()
    print(alg2)

def test_isolate_arithmetic_units() -> None:
    template = mp.Template(mp.Pattern(['a','a','b','c']), matrix=mp.Matrix(4))
    isolated_units = mp.isolate_arithmetic_units(template)
    print(isolated_units)

def main():
    test_manual_population_8()
    test_auto_resolve_recursive_full()
    test_isolate_arithmetic_units()
    m = mp.Matrix(8)
    p = mp.Pattern(['a','a','b','b','c','c','d','d'])
    alg = mp.Algorithm(m)
    alg.push(p)
    alg.auto_resolve_stage()
    print(alg)

if __name__ == "__main__":
    main()
