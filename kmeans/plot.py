from pandas.plotting import scatter_matrix

def plot_scatter(data):
    fig=scatter_matrix(data, alpha=0.1, figsize=(15,15), diagonal='hist', range_padding=0.5)
    for ax in fig.flatten():
        ax.xaxis.label.set_rotation(90)
        ax.yaxis.label.set_rotation(0)
        ax.yaxis.label.set_ha("right")
    return fig