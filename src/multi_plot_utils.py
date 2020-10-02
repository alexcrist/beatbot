''' TODO: Refactor this a bit for organization '''

import math
import numpy as np
import matplotlib.pyplot as plt

IMSHOW_COLORS = ['viridis', 'plasma', 'Blues', 'magma', 'cividis']
PLOT_COLORS = [
    '#8865FF',
    '#FF6FA5',
    '#EE3E38',
    '#9DB300',
    '#165BAA',
    '#A155B9',
    '#B83253',
    '#F10080',
    '#3B1568',
    '#55BEC0',
    '#F25E74',
    '#0682A5',
    '#543884',
    '#F320FA',
    '#F24F09',
    '#3921B3',
    '#A8234C',
    '#A455FF',
    '#2a9d8f',
    '#ffb997',
    '#264653',
    '#f67e7d',
    '#843b62',
    '#621940',
    '#0b032d'
]
    
def graph_clusters(items, title, clusters, num_columns, raw_figsize, graph_item):
    num_rows = math.ceil(len(items) / num_columns)
    figsize = (raw_figsize[0], num_rows * raw_figsize[1])
    fig, axs = plt.subplots(num_rows, num_columns, figsize=figsize, constrained_layout=True)
    fig.suptitle(title, fontsize=14, x=0, y=1)
    
    for i in range(num_rows):
        for j in range(num_columns):
            index = i * num_columns + j
            ax = axs[index] if num_rows == 1 else axs[i, j]
            ax.axis('off')
            if index < len(items):
                item = items[index]
                cluster = clusters[index % len(clusters)]
                ax.set_title(index, fontsize=8)
                graph_item(ax, item, cluster)
                
    plt.show()
    
def plot_item(ax, item, cluster):
    color = PLOT_COLORS[cluster % len(PLOT_COLORS)]
    ax.plot(item, color)
    
def create_imshow_item(vmin, vmax):
    def imshow_item(ax, item, cluster):
        color = IMSHOW_COLORS[0]
        ax.imshow(item.T, cmap=color, vmin=vmin, vmax=vmax)
    return imshow_item

def multi_plot(items, title='', clusters=[0], num_columns=11, figsize=(15, 1.5)):
    graph_clusters(items, title, clusters, num_columns, figsize, plot_item)

def multi_heatmap(items, title='', clusters=[0], num_columns=11, figsize=(15, 1.5), adjust_minmax=True):
    imshow_item = None
    if adjust_minmax:
        vmin, vmax = get_min_max(items)
        imshow_item = create_imshow_item(vmin, vmax)
    else:
        imshow_item = lambda ax, item, cluster: ax.imshow(item)
    graph_clusters(items, title, clusters, num_columns, figsize, imshow_item)
    
def get_min_max(array_3d):
    array_3d_min = float('inf')
    array_3d_max = -float('inf')
    for matrix in array_3d:
        matrix_min = matrix.min()
        matrix_max = matrix.max()
        if matrix_min < array_3d_min:
            array_3d_min = matrix_min
        if matrix_max > array_3d_max:
            array_3d_max = matrix_max
    return array_3d_min, array_3d_max