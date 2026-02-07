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

def test_export_parquet() -> None:
    scope = mp.truth_scope((1, 15), (1, 225))
    alg = mp.Algorithm(mp.Matrix(4))
    alg.auto_resolve_stage()
    t = mp.truth_table(scope, alg)
    df = mp.truth_dataframe(scope, alg)
    print(df)
    df.to_parquet('')
    df1 = pd.read_parquet('')
    print(df1)



def main() -> None:
    test_export_parquet()


if __name__ == "__main__":
    main()
