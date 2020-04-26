import urllib.request

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import scipy.stats as st

suicide_rate_url = 'http://apps.who.int/gho/athena/data/xmart.csv?target=GHO/MH_12&profile=crosstable&filter=COUNTRY' \
                   ':*;REGION:*&x-sideaxis=COUNTRY&x-topaxis=GHO;YEAR;SEX '
local_filename, headers = urllib.request.urlretrieve(suicide_rate_url, filename='who_suicide_rates.csv')

rates = pd.read_csv(local_filename, names=['Country', 'Both', 'Female', 'Male'], skiprows=3)
rates.head(10)

print(rates['Male'].mean(), rates['Female'].mean())

eta = 1.
beta = 1.5
rvweib = st.weibull_min(beta, scale=eta)
beta, loc, eta = st.weibull_min.fit(rates['Both'], floc=0, scale=12)
print(beta, loc, eta)

rates['Both'].hist(bins=30)
np.random.seed(1100)
rvweib = st.weibull_min(beta, scale=eta)
plt.hist(rvweib.rvs(size=len(rates.Both)), bins=30, alpha=0.5)

plt.show()
