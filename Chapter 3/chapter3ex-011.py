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

N = 20
p = 0.5
rv_binom = st.binom(N, p)

mean = rv_binom.mean()
std = rv_binom.std()
print(mean, std)

mean = N * p
std = np.sqrt(N * p * (1 - p))
print(mean, std)

rvnorm = st.norm(loc=mean, scale=std)
pdf = rvnorm.pdf
xx = np.linspace(0, 20, 200)
yy = pdf(xx)
plt.plot(xx, yy, linewidth=3., color='Chocolate')

xx = np.arange(N + 1)
pmf = rv_binom.pmf(xx)
left = xx - 0.5
plt.bar(left, pmf, 1.0, color='CornflowerBlue')
rvnorm = st.norm(loc=mean, scale=std)
plt.axis([0, 20, 0, .18])

plt.show()
