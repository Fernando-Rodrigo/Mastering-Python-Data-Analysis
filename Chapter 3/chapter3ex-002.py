import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rnd
import os

plt.style.use(os.path.join(os.getcwd(), 'mystyle.mplstyle'))

nvalues = 10
norm_variates = rnd.randn(nvalues)
norm_variates

for i, v in enumerate(sorted(norm_variates), start=1):
    print('{0:2d} {1:+.4f}'.format(i, v))


    def plot_cdf(data, plot_range=None, scale_to=None, **kwargs):
        num_bins = len(data)
        sorted_data = np.array(sorted(data), dtype=np.float64)
        data_range = sorted_data[-1] - sorted_data[0]
        counts, bin_edges = np.histogram(sorted_data, bins=num_bins)
        xvalues = bin_edges[1:]
        yvalues = np.cumsum(counts)
        if plot_range is None:
            xmin = xvalues[0]
            xmax = xvalues[-1]
        else:
            xmin, xmax = plot_range
        # pad the arrays
        xvalues = np.concatenate([[xmin, xvalues[0]], xvalues, [xmax]])
        yvalues = np.concatenate([[0.0, 0.0], yvalues, [yvalues.max()]])
        if scale_to:
            yvalues = yvalues / len(data) * scale_to
        plt.axis([xmin, xmax, 0, yvalues.max()])
        return plt.step(xvalues, yvalues, **kwargs)

nvalues = 20
# rnd.seed(123) # to get identical results every time
norm_variates = rnd.randn(nvalues)
axes = plot_cdf(norm_variates, plot_range=[-6, 3], scale_to=1.,
                lw=2.5, color='Brown')
for v in [0.25, 0.5, 0.75, 1.0]:
    plt.axhline(v, lw=1, ls='--', color='black')

plt.show()
