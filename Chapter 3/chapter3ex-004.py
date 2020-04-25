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

N = 4857
mean = 63.8
serror = 0.06
sdev = serror * np.sqrt(N)
rvnorm = st.norm(loc=mean, scale=sdev)

xmin = mean - 3 * sdev
xmax = mean + 3 * sdev
xx = np.linspace(xmin, xmax, 200)
plt.figure(figsize=(8, 3))
plt.subplot(1, 2, 1)
plt.plot(xx, rvnorm.cdf(xx))
plt.title('CDF')
plt.xlabel('Height (in)')
plt.ylabel('Proportion of women')
plt.axis([xmin, xmax, 0.0, 1.0])
plt.subplot(1, 2, 2)
plt.plot(xx, rvnorm.pdf(xx))
plt.title('PDF')
plt.xlabel('Height (in)')
plt.axis([xmin, xmax, 0.0, 0.1])

plt.show()
