import pandas as pd
import pyarrow as pa
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# -- sources --
# https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html
def df_global_heatmap(path: str, title: str, df: pd.DataFrame) -> None:
    """Export pyplot of global heatmap"""

    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    if not isinstance(title, str):
        raise TypeError(f"title must be a string got {type(title)}")
    if not isinstance(path, str):
        raise TypeError(f"path must be a string got {type(path)}")

    # sum all columns
    # cast to nested list
    # cast nested list to .im_show
    # Use columns as hints to generate axis labels
    # plt.savefig('filename.png')

    # print(df)
    df_ = df.sum(axis=0)
    pd.set_option('display.max_rows', None)
    hint = str(df_.index[-1])[2:-2].split("', '")

    total_stages = int(hint[0].split('_')[-1]) + 1
    bits         = int(hint[1].split('_')[-1]) + 1


    mini_heatmaps = []

    arr = None
    for s in range(total_stages):
        ppm = []
        for p in range(bits):
            row = [0]*(bits << 1)
            for b in range((bits << 1)-1, -1, -1):
                row[b] = df_.loc[f"('stage_{s}', 'ppm_{p}', 'b{b}')"]
            ppm.append(row[::-1])
        # mini_heatmaps.append(np.array(ppm))
        if arr is None:
            arr = np.array(ppm)
            continue
        arr += np.array(ppm)

    print(arr)
    if arr is None:
        raise ValueError("No data found")

    fig, ax = plt.subplots(figsize=(16, 9), dpi=200)
    im = ax.imshow(arr, cmap='magma_r')

    ax.set_xticks(range(bits << 1), labels=[f'b{i}' for i in range((bits << 1)-1, -1, -1)])
    ax.set_yticks(range(bits), labels=[f'ppm_{i}' for i in range(bits)])

    for i in range(bits):
        for j in range((bits << 1)-1, -1, -1):
            text = ax.text(j, i, arr[i, j], ha="center", va="center", color="w")

    ax.set_title(title)
    fig.tight_layout()
    plt.colorbar(im, shrink=0.7)
    plt.savefig(path)

    # print(df_)
    # print(df_.index)
    # print(mini_heatmaps)
    # for i in df_:
    #     print(i)

# -- sources --
# https://matplotlib.org/stable/gallery/mplot3d/index.html
def df_global_3d_heatmap(path: str, df: pd.DataFrame, stages: list[int]) -> None:
    """Export 3d plot with heatmap for each stage stacked along the z-axis"""
    ...


def df_stage_heatmap(path: str, df: pd.DataFrame, stages: list[int]) -> None:
    """Export pyplot heatmap for each selected stage"""

    if not isinstance(stages, list):
        raise TypeError(f"Expected list[int] got {type(stages)}")
    if not all([isinstance(i, int) for i in stages]):
        raise TypeError("All elements of stages must be integers")
    # sum all columns
    # cast to nested list
    # cast nested list to .im_show
    # Use columns as hints to generate axis labels
    # plt.savefig('filename.png')

    # print(df)
    df_ = df.sum(axis=0)
    pd.set_option('display.max_rows', None)
    hint = str(df_.index[-1])[2:-2].split("', '")

    total_stages = int(hint[0].split('_')[-1]) + 1
    bits         = int(hint[1].split('_')[-1]) + 1


    mini_heatmaps = []


    if stages == []:
        stages = [i for i in range(total_stages)]

    for s in stages:
        ppm = []
        for p in range(bits):
            row = [0]*(bits << 1)
            for b in range((bits << 1)-1, -1, -1):
                row[b] = df_.loc[f"('stage_{s}', 'ppm_{p}', 'b{b}')"]
            ppm.append(row)
        mini_heatmaps.append(ppm)






    print(df_)
    print(df_.index)
    # print(mini_heatmaps)
    # for i in df_:
    #     print(i)




def df_stage_bound_heatmap(
    path: str,
    df: pd.DataFrame,
    stages: list[int],
    bound: list[tuple[int, int]]
) -> None:
    """Export pyplot heatmap of bounding box region across stages"""
    ...
