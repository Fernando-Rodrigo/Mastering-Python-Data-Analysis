import matplotlib.pyplot as plt
from pandas import DataFrame
import numpy.random as rnd
import scipy.stats as st
import os

plt.style.use(os.path.join(os.getcwd(), 'mystyle.mplstyle'))

nvalues = 10
norm_variates = rnd.randn(nvalues)

for i, v in enumerate(sorted(norm_variates), start=1):
    print('{0:2d} {1:+.4f}'.format(i, v))

eta = 1.0
beta = 1.5
rvweib = st.weibull_min(beta, scale=eta)

weib_variates = rvweib.rvs(size=500)
print(weib_variates[:10])

weib_df = DataFrame(weib_variates, columns=['weibull_variate'])
weib_df.hist(bins=30)

plt.show()
