import numpy as np
from matplotlib import pyplot as plt

COLORS = ['#390099', '#9e0059']
COLOR_INDEX = 0

# Return a new color from the COLORS list
def get_color():
    global COLORS, COLOR_INDEX
    color = COLORS[COLOR_INDEX]
    COLOR_INDEX += 1
    COLOR_INDEX = COLOR_INDEX % len(COLORS)
    return color

# Display a line plot
def plot(y, x=None, figsize=(20, 4), title='', xlabel='', ylabel='', show_xticks=True, show_yticks=False, show=True):
    if x is None:
        x = range(len(y))
    
    plt.figure(figsize=figsize)
    plot_axes(title, xlabel, ylabel, show_xticks, show_yticks, x, y)
    plt.plot(x, y, c=get_color(), alpha=0.8)
    
    if show:
        plt.show()
    
# Display a heat map plot (imshow)
def heatmap(data, figsize=(20, 4), title='', xlabel='', ylabel='', show_xticks=True, show_yticks=False):
    plt.figure(figsize=figsize)
    plot_axes(title, xlabel, ylabel, show_xticks, show_yticks, range(len(data[0])), range(len(data)))
    plt.imshow(data, aspect='auto')
    plt.show()
    
# Display titles, axes, and labels for a plot
def plot_axes(title, xlabel, ylabel, show_xticks, show_yticks, x=[], y=[]):
    plt.title(title, fontsize=14, loc='left')
    
    ax = plt.gca()
    ax.axes.set_xlabel(xlabel)
    ax.axes.set_ylabel(ylabel)
    
    ax.axes.xaxis.set_ticklabels([])
    if show_xticks:
        ax.axes.xaxis.set_ticks([int(np.min(x)), int(np.max(x))])
        ax.axes.xaxis.set_ticklabels([int(np.min(x)), int(np.max(x))])
    
    ax.axes.yaxis.set_ticklabels([])
    if show_yticks:
        ax.axes.yaxis.set_ticks([int(np.min(y)), int(np.max(y))])
        ax.axes.yaxis.set_ticklabels([int(np.min(y)), int(np.max(y))])
