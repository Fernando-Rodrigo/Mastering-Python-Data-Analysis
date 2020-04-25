import matplotlib.pyplot as plt
import numpy.random as rnd
from pandas import DataFrame
import scipy.stats as st
import os

plt.style.use(os.path.join(os.getcwd(), 'mystyle.mplstyle'))

nvalues = 10
norm_variates = rnd.randn(nvalues)

for i, v in enumerate(sorted(norm_variates), start=1):
    print('{0:2d} {1:+.4f}'.format(i, v))

binorm_variates = st.multivariate_normal.rvs(mean=[0, 0], size=300)
df = DataFrame(binorm_variates, columns=['Z1', 'Z2'])
df.head(10)

df.plot(kind='scatter', x='Z1', y='Z2')
plt.title('Bivariate Normal Distribution')
plt.axis([-4, 4, -4, 4])

plt.show()
