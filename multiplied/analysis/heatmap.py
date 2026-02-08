import pandas as pd
import pyarrow as pa
import matplotlib.pyplot as plt
import matplotlib as mpl
"""

https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html
"""
# -- sources --
# https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html
def df_global_heatmap(path: str, df: pd.DataFrame) -> None:
    """Export pyplot of global heatmap"""

    # sum all columns
    # cast to nested list
    # cast nested list to .im_show
    # Use columns as hints to generate axis labels
    # plt.savefig('filename.png')

    # print(df)
    df_ = df.sum(axis=0)
    pd.set_option('display.max_rows', None)
    hint = df_.index[-1]


    print(df_)
    print(df_.index)
    print(hint)
    # for i in df_:
    #     print(i)


def df_stage_heatmap(path: str, df: pd.DataFrame, stages: list[int]) -> None:
    """Export pyplot heatmap of selected stages"""
    ...


def df_stage_bound_heatmap(
    path: str,
    df: pd.DataFrame,
    stages: list[int],
    bound: list[tuple[int, int]]
) -> None:
    """Export pyplot heatmap of bounding box region across stages"""
    ...
