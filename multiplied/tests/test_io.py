from functools import cache
import multiplied as mp
import pandas as pd
import pyarrow as pa

def gen_resources(bits: int, *, a=0, b=0
) -> tuple[mp.Matrix, mp.Pattern, mp.Algorithm]:
    m = mp.Matrix(bits, a=a, b=b)
    match bits:
        case 4:
            p = mp.Pattern(['a','a','b','b',])
        case 8:
            p = mp.Pattern(['a','a','a','b','b','b','c','c'])
        case _:
            raise ValueError(f"Unsupported number of bits: {bits}")
    alg = mp.Algorithm(m)
    return m, p, alg

def test_export_algorithm() -> None:
    m, p, alg = gen_resources(4)
    alg.auto_resolve_stage()
    path = ''
    mp.export_algorithm(alg, path)



# def test_import_algorithm() -> None:
#     path = ''
#     mp.import_algorithm(path)
#

@cache
def test_export_parquet_4() -> None:
    from pathlib import Path
    scope = mp.truth_scope((1, 15), (1, 255))
    alg = mp.Algorithm(mp.Matrix(4))
    alg.auto_resolve_stage()
    # print(alg)
    t = mp.truth_table(scope, alg)
    df = mp.truth_dataframe(scope, alg)
    print(df.head())
    print(df.info())


@cache
def test_export_parquet_8() -> None:
    # from pathlib import Path
    import time
    start_t = time.perf_counter()
    scope = mp.truth_scope((1, 255), (1, 65535))
    print([i for i in scope])
    end_t = time.perf_counter()
    print(f"{end_t - start_t:.6f} seconds")
    # alg = mp.Algorithm(mp.Matrix(8))
    # alg.auto_resolve_stage()
    # # print(alg)
    # t = mp.truth_table(scope, alg)
    # df = mp.truth_dataframe(scope, alg)
    # print(df.head())
    # print(df.info())
    # path = Path(__file__).parent.parent.parent / 'examples/datasets/example_8b_mult_truthtable.parquet'
    # print(path)
    # df.to_parquet(path)
    # # df1 = pd.read_parquet(path)




def main() -> None:
    # test_export_parquet_4()
    test_export_parquet_8()


if __name__ == "__main__":
    main()
