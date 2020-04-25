import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rnd
import scipy.stats as st
import os

plt.style.use(os.path.join(os.getcwd(), 'mystyle.mplstyle'))

nvalues = 10
norm_variates = rnd.randn(nvalues)

for i, v in enumerate(sorted(norm_variates), start=1):
    print('{0:2d} {1:+.4f}'.format(i, v))

mean = 0.0
sdev = 1.0
rvnorm = st.norm(loc=mean, scale=sdev)
cdf = rvnorm.cdf
pdf = rvnorm.pdf
a = -.6
b = 1.2
xmin = mean - 3 * sdev
xmax = mean + 3 * sdev
xx = np.linspace(xmin, xmax, 200)
plt.figure(figsize=(9, 3.5))
yy = cdf(xx)
plt.subplot(1, 2, 1)
plt.title('Cumulative distribution function', fontsize=15)
# plt.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
# plt.tick_params(axis='y', which='both', left='off', right='off', labelleft='off')
plt.plot([a, a], [0.0, cdf(a)], lw=1.2, ls='--', color='black')
plt.plot([b, b], [0.0, cdf(b)], lw=1.2, ls='--', color='black')
plt.plot([xmin, a], [cdf(a), cdf(a)], lw=1.2, ls='--', color='black')
plt.plot([xmin, b], [cdf(b), cdf(b)], lw=1.2, ls='--', color='black')
plt.plot(xx, yy, color='Brown', lw=2.5)
plt.plot([xmin, xmin], [cdf(a) + 0.01, cdf(b) - 0.015], lw=10, color='black')
plt.text(a, -0.06, '$a$', fontsize=14, horizontalalignment='center')
plt.text(b, -0.06, '$b$', fontsize=14, horizontalalignment='center')
plt.text(xmin - 0.06, cdf(a), '$F(a)$', fontsize=14,
         horizontalalignment='right', verticalalignment='center')
plt.text(xmin - 0.06, cdf(b), '$F(b)$', fontsize=14,
         horizontalalignment='right', verticalalignment='center')
plt.text(b, -0.06, '$b$', fontsize=14, horizontalalignment='center')
plt.text(xmin + 0.15, 0.5 * (cdf(a) + cdf(b)), '$P=F(b)-F(a)$', fontsize=14,
         verticalalignment='center')
yy = pdf(xx)
plt.subplot(1, 2, 2)
plt.title('Probability density function', fontsize=15)
# plt.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
# plt.tick_params(axis='y', which='both', left='off', right='off', labelleft='off')
plt.plot([a, a], [0.0, pdf(a)], lw=1.2, color='black')
plt.plot([b, b], [0.0, pdf(b)], lw=1.2, color='black')
plt.fill_between(xx, yy, where=(a <= xx) & (xx <= b), color='LemonChiffon')
plt.text(a, -0.025, '$a$', fontsize=14, horizontalalignment='center')
plt.text(b, -0.025, '$b$', fontsize=14, horizontalalignment='center')
plt.text(0.5 * (a + b) - .1, 0.2, '$P=$Area', fontsize=14,
         horizontalalignment='center',
         verticalalignment='top')
plt.plot(xx, yy, color='Brown', lw=2.5)

plt.show()
