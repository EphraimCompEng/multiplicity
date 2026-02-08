############################################
# Extract Columns From Multiplied Parquets #
############################################

import pandas as pd
import pyarrow as pa


# -- cheat sheet ----------------------------------------------------
#
# cols = [("stage_1","ppm_0",f"b{i}") for i in range(8)]
# df   = pd.read_parquet("xyz.parquet", columns=cols)
#
# idx = pd.IndexSlice
#
# df.loc[:, idx["stage_1", :, :]]        # all ppms & bits for stage_1
# df.loc[:, idx[:, "ppm_0", :]]          # that ppm across all stages
# df.loc[:, idx[:, :, "b3"]]             # bit b3 across all stages/ppms
#
#

# TODO add metadata to .parquet datasets to extract bit width, alg length etc


def validate_path(path: str) -> None:
    if not isinstance(path, str):
        raise TypeError("path must be a string")
    if not path.endswith('.parquet'):
        raise ValueError("path must end with .parquet")

def pq_extract_bits(path: str, bits: list[int], stages: list[int]) -> pd.DataFrame:
    """Return a DataFrame of specified bits across multiple stages from .parquet"""
    validate_path(path)
    raise NotImplementedError



# -- Sources --
# https://stackoverflow.com/questions/53982871/pandas-reading-first-n-rows-from-parquet-file#69888274
def pq_extract_stages(path: str, *, stages: list[str]=[]) -> pd.DataFrame:
    """Return a DataFrame of specified stages from .parquet"""

    # Documentation is getting really annoying to find so the following is
    # just an attempt to get things to work

    # -- find algorithm length from first row -----------------------
    validate_path(path)
    from pyarrow.parquet import ParquetFile
    pf = ParquetFile(path)
    first = next(pf.iter_batches(batch_size = 1))
    row = pa.Table.from_batches([first]).to_pandas()
    pd.set_option('display.max_columns', None)

    print(row)

    # Multiplied datasets will always include formatted string columns
    # with the rightmost columns dedicated to formatted strings.
    # Hence the rightmost column is the final formatted string column
    final_ppm_s_column = row.columns[-1]

    # This is not optimal at all -- problem for future me ----------- #
    # TODO: manage metadata for .parquet <> DataFrame
    # trim and extract integer
    total_stages = int(final_ppm_s_column.split('_')[1][1:])

    # lists[str] converted to str by pandas, find length of first entry
    bits = row.loc[0]['ppm_s0'][2:].index("'") >> 1
    print(total_stages,  bits)
    # --------------------------------------------------------------- #

    # loop through stages and push to DataFrame

    if stages == []:
        stages = [f"stage_{s}" for s in range(total_stages)]

    columns = []
    for s in stages:
        for p in range(bits):
            for b in range((bits << 1)-1, -1, -1):
                # TODO: flatten columns to strings since they're converted anyway
                # e.g: 'stage_0_ppm_4_b_3'
                columns.append(str((s, f"ppm_{p}" , f"b{b}")))

    # Initialize DataFrame with stages as columns
    df = pd.read_parquet(path, columns=columns)
    print(df)
    return df






def pq_extract_formatted_all(path: str) -> pd.DataFrame:
    """Return DataFrame of all formatted strings from .parquet"""
    validate_path(path)
    raise NotImplementedError

def pq_extract_formatted_stages(path: str, stages: list[int]) -> pd.DataFrame:
    """Return DataFrame of formatted strings across multiple stages from .parquet"""
    validate_path(path)
    raise NotImplementedError
