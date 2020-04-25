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

wing_lengths = np.fromfile('data/housefly-wing-lengths.txt',
                           sep='\n', dtype=np.int64)
mean, std = st.norm.fit(wing_lengths)
print(mean, std)

st.probplot(wing_lengths, dist='norm', plot=plt)
plt.grid(lw=1, ls='dashed')

plt.show()
