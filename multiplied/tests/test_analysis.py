from pathlib import Path
import multiplied as mp
import pandas as pd
import pyarrow as pa


def test_pq_extract_bits() -> None:
    ...


def test_pq_extract_stages(path: Path) -> None:
    print(path)
    df = mp.pq_extract_stages(str(path))
    # print(df.head())
    path2 = Path(__file__).parent.parent.parent / 'examples/outputs/example_8b_wallace_heatmap.svg'
    print(path2)
    title = "8-Bit Wallace-Tree Truth Table Represented As Heatmap"
    mp.df_global_heatmap(str(path2), title, df)

def test_df_global_3d_heatmap(path: Path) -> None:
    print(path)
    df = mp.pq_extract_stages(str(path))
    path2 = Path(__file__).parent.parent.parent / 'examples/outputs/example_8b_wallace_3d_heatmap.svg'
    print(path2)
    title = "8-Bit Wallace-Tree Truth Table Represented As Heatmap"
    mp.df_global_3d_heatmap(str(path2), title, df)

def test_pq_extract_formatted_all() -> None:
    ...


def test_pq_extract_formatted_stages() -> None:
    ...




def main() -> None:
    path = Path(__file__).parent.parent.parent / 'examples/datasets/example_8b_mult_truthtable.parquet'
    # test_pq_extract_stages(path)
    test_df_global_3d_heatmap(path)

if __name__ == "__main__":
    main()
