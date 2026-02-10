import pandas as pd
import pyarrow as pa
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

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
    df_ = df.sum(axis=0) # Create heatmap for each stage
    pd.set_option('display.max_rows', None)
    hint = str(df_.index[-1])[2:-2].split("', '")

    total_stages = int(hint[0].split('_')[-1]) + 1
    bits         = int(hint[1].split('_')[-1]) + 1

    print(hint)

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
        arr += np.array(ppm) # Unify all heatmaps

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

    ax.set_title(title, pad=50)


    # -- canvas level offsets ---------------------------------------
    pos  = ax.get_position()
    ax.set_position((pos.x0-0.05, pos.y0, pos.width, pos.height))

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
def df_global_3d_heatmap(path: str, title: str, df: pd.DataFrame) -> None:
    """Export 3d plot with heatmap for each stage stacked along the x-axis"""

    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    if not isinstance(title, str):
        raise TypeError(f"title must be a string got {type(title)}")
    if not isinstance(path, str):
        raise TypeError(f"path must be a string got {type(path)}")

    # -- collect data, metadata -------------------------------------

    df_  = df.sum(axis=0) # Create heatmap for each stage
    hint = str(df_.index[-1])[2:-2].split("', '")
    print(hint)

    total_stages = int(hint[0].split('_')[-1]) + 1
    bits         = int(hint[1].split('_')[-1]) + 1

    # -- build stage heatmaps ---------------------------------------
    arr_list = []
    for s in range(total_stages):
        ppm = []
        for p in range(bits):
            row = [0]*(bits << 1)
            for b in range(bits << 1):
                row[b] = df_.loc[f"('stage_{s}', 'ppm_{p}', 'b{b}')"]
            ppm.append(row[::-1])
        arr_list.append(ppm)


    stages      = np.stack(arr_list)
    vmin, vmax  = stages.min(), stages.max()
    stages_norm = (stages - vmin) / (vmax - vmin)
    _, nx, ny   = stages_norm.shape

    print(stages_norm.shape)

    # -- plot setup -------------------------------------------------
    x_spacing = 2.0
    alpha     = 0.7
    fig       = plt.figure(figsize=(16,9), dpi=200)
    ax        = fig.add_subplot(111, projection='3d')
    cmap      = plt.get_cmap('magma_r')


    # -- build 3d stacked heatmaps ----------------------------------
    for i in range(total_stages):
        x_plane           = np.full_like(stages[i], i*x_spacing, shape=[nx+1, ny+1])
        y_plane, z_plane  = np.meshgrid(
            np.arange((bits << 1) +1), np.arange(bits, -1, -1), indexing='xy'
        )

        facecolors = cmap(stages_norm[i])

        # plane -- heatmap
        surf = ax.plot_surface(
            x_plane, y_plane, z_plane,
            facecolors=facecolors,
            shade=False,
            linewidth=0,
            antialiased=True,
            alpha=alpha
        )
        surf.set_clip_on(False)

        # faint grid
        ax.plot_wireframe(
            x_plane, y_plane, z_plane + 0.001, color='k', linewidth=0.3, alpha=0.2
        ).set_clip_on(False)



    # -- axis values ------------------------------------------------
    ax.set_xticks(np.arange(-1, total_stages*2-1, 2) ,[f"stage_{i}" for i in range(total_stages)])
    ax.set_yticks(np.arange(bits << 1)+1, np.arange((bits << 1)-1, -1, -1))
    ax.set_zticks(np.arange(bits), labels=[f'ppm_{i}' for i in range(bits-1, -1, -1)])


    # -- titles -----------------------------------------------------
    ax.set_xlim(-x_spacing, (total_stages - 1) * x_spacing + x_spacing)
    ax.set_ylabel('bits')
    ax.set_zlabel('Partial Product', va='bottom')
    ax.set_ylim(-0.5, (bits << 1)+0.5)
    ax.set_zlim(-0.5, bits)
    ax.set_title(title, pad=70)

    # -- colour bar -------------------------------------------------
    mappable = plt.cm.ScalarMappable(cmap=cmap)
    mappable.set_array(np.linspace(vmin, vmax, 256))
    cb = plt.colorbar(mappable, ax=ax, aspect=40, shrink=0.6, pad=0.2, location='bottom')

    # -- canvas level offsets ---------------------------------------
    cax  = cb.ax
    cpos = cax.get_position()
    cax.set_position((cpos.x0, cpos.y0-0.1, cpos.width, cpos.height))

    pos  = ax.get_position()
    ax.set_position((pos.x0, pos.y0-0.1, pos.width, pos.height))

    # -- export ----------------------------------------------------
    ax.set_clip_on(False) # Fixes 2d planes from being clipped
    ax.set_box_aspect((5,3,1), zoom=2)
    plt.savefig(path)




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
