import matplotlib.pyplot as plt
import numpy.random as rnd
import os

plt.style.use(os.path.join(os.getcwd(), 'mystyle.mplstyle'))

nvalues = 10
norm_variates = rnd.randn(nvalues)
norm_variates

for i, v in enumerate(sorted(norm_variates), start=1):
    print('{0:2d} {1:+.4f}'.format(i, v))

plt.figure()
ax = plt.gca()
ax.axis('off')
plt.plot([1, 2], [1, 1], lw=2, color='green')
plt.plot([2, 2], [1, 2], lw=2, color='green', ls='--')
plt.plot([2, 3.5], [2, 2], lw=2, color='green')
plt.plot(1, 1, marker='o', mfc='green')
plt.plot(2, 1, marker='o', mfc='white', mec='green', mew=2)
plt.plot(2, 2, marker='o', mfc='green')
plt.plot(3.5, 2, marker='o', mfc='white', mec='green', mew=2)
plt.text(2.0, 0.9, '$v$', fontsize=20,
         horizontalalignment='center',
         verticalalignment='top')
xx = 3.8
delta = 0.1
plt.plot([xx, xx], [1, 2], lw=1.2, color='black')
plt.plot([xx - delta, xx + delta], [1, 1], lw=1.2, color='black')
plt.plot([xx - delta, xx + delta], [2, 2], lw=1.2, color='black')
plt.text(xx + delta, 1.5, '$1/N$', fontsize=20,
         horizontalalignment='left',
         verticalalignment='center')
plt.axis([0.5, 5, 0, 3])

plt.show()
