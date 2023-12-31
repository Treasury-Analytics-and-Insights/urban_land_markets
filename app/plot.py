import matplotlib.pyplot as fig
import numpy as np
import pandas as pd

GOLD = np.array((241, 164, 45))/255
BLUE = np.array((0, 79, 103))/255
GREEN = np.array((103, 168, 84))/255
ORANGE = np.array((220,88,42))/255

LINEWIDTH = 2


def symmetric_plot_data(eq):
    negatives = eq[['r(d)', 'P(d)', 'r_', 'p(d)']].iloc[1:].iloc[::-1]
    negatives.index = -negatives.index
    symmetric = pd.concat([negatives, eq[['r(d)', 'P(d)', 'r_', 'p(d)']]], axis=0)
    symmetric.columns = ['Land price', 'House price', 'Rural land price', 'House rents']
    return symmetric


def plot(fig, symmetric, diff_land_rents, d_):
    fig.clf()
    ax = fig.gca()
    ax.plot(symmetric['House rents'].loc[abs(symmetric.index) <= d_], label = 'House rents', color=GOLD, linewidth=LINEWIDTH)
    ax.plot(symmetric['Land price'], label = 'Land price', color=BLUE, linewidth=LINEWIDTH)
    ax.plot(symmetric['Rural land price'], label = 'Rural land price', color=GREEN, linewidth=LINEWIDTH)
    ax.plot(symmetric['House price'].loc[abs(symmetric.index) <= d_], label = 'House price', color=ORANGE, linewidth=LINEWIDTH)
    # put the legend outside the plot, horizontally at the bottom
    ax.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc='lower left',
                ncol=4, mode="expand", borderaxespad=0., frameon=False)
    # shade the area between the house price and the rural land price in blue with 30% transparency
    ax.fill_between(symmetric.index[abs(symmetric.index) <= d_], symmetric['Land price'].loc[abs(symmetric.index) <= d_], 
                        symmetric['Rural land price'].loc[abs(symmetric.index) <= d_], color=BLUE, alpha=0.3)

    # annotate the plot with the integrated differential land rents near the top right corner
    ax.annotate('Integrated differential land rents: {:.2f}'.format(diff_land_rents), 
        xy=(0.95, 0.9), xycoords='axes fraction', fontsize=10,
        horizontalalignment='right', verticalalignment='top')

    # format plot in the tufte style using matplotlib
    for spine in ax.spines.values():
        spine.set_visible(False)

    # make tick marks invisible
    ax.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=True, left=False, right=False, labelleft=True)

    #draw very faint grid lines

    ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.7)

    ax.set_xlabel('Distance from city centre', fontsize=16)
    ax.set_title('Closed city - competitive model', fontsize=18)

