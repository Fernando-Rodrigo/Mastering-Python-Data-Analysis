import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import scipy.stats as stats
from scipy.stats import linregress

var = plt.style.available

plt.style.use(os.path.join(os.getcwd(), 'mystyle.mplstyle'))

# Relationships
hubble_data = pd.read_csv('data/hubble.csv', skiprows=2, names=['id', 'r', 'v'])
hubble_data.head()

hubble_data.plot(kind='scatter', x='r', y='v', s=50)
plt.locator_params(nbins=5)

"""rv = hubble_data.as_matrix(columns=['r','v'])
a, b, r, p, stderr = linregress(rv)
print(a, b, r, p, stderr)

hubble_data.plot(kind='scatter', x='r', y='v', s=50)
rdata = hubble_data['r']
rmin, rmax = min(rdata), max(rdata)
rvalues = np.linspace(rmin, rmax, 200)
yvalues = a * rvalues + b
plt.plot(rvalues, yvalues, color='IndianRed', lw=2)
plt.locator_params(nbins=5)"""

plt.show()
