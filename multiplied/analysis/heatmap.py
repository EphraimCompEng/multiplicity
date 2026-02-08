import pandas as pd
import pyarrow as pa
import matplotlib.pyplot as plt
import matplotlib as mpl
"""

https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html
"""


def df_global_heatmap(path: str, df: pd.DataFrame) -> None:
    """Produce pyplot of global heatmap"""
    ...


def df_stage_heatmap(path: str, df: pd.DataFrame, stages: list[int]) -> None:
    """Produce pyplot heatmap of selected stages"""
    ...


def df_stage_bound_heatmap(
    path: str,
    df: pd.DataFrame,
    stages: list[int],
    bound: list[tuple[int, int]]
) -> None:
    """Produce pyplot heatmap of bounding box region across stages"""
    ...
