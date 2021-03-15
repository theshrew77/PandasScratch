import matplotlib.pyplot as plt
from scipy import stats
import numpy as np


def FourPlot(df, variable, HistogramParams=None,Distribution=None):
    fig, axes = plt.subplots(2, 2)

    fig.suptitle('4-Plot: ' + variable)

    axes[0,0].plot(df[variable].values,'k')
    axes[0,0].set_title('Run Sequence')

    axes[0,1].plot(df[variable].values, df[variable].shift(-1).values,'kx')
    axes[0,1].set_title('Lag Plot')

    if HistogramParams:
        df.hist(bins=np.linspace(HistogramParams[0],HistogramParams[1],HistogramParams[2]),ax=axes[1,0],color='k')
    else:
        df.hist(ax=axes[1,0],color='k')
    axes[1,0].set_title('Histogram')

    if Distribution is None:
        Distribution = 'norm'
    stats.probplot(df[variable].values, plot=axes[1,1],dist = Distribution)
    axes[1,1].set_title('Prob. Plot: '+ Distribution)
    axes[1,1].get_lines()[0].set_marker('x')
    axes[1,1].get_lines()[0].set_markerfacecolor('k')
    axes[1,1].get_lines()[0].set_markeredgecolor('k')

    plt.show()