import urllib.request
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.transforms as transforms
import numpy as np
import pandas as pd
import scipy.stats as st
from scipy.stats import linregress
import statsmodels.api as sm
from mpl_toolkits.mplot3d import Axes3D

suicide_rate_url = 'http://apps.who.int/gho/athena/data/xmart.csv?target=GHO/MH_12&profile=crosstable&filter=COUNTRY' \
                   ':*;REGION:*&x-sideaxis=COUNTRY&x-topaxis=GHO;YEAR;SEX '
local_filename, headers = urllib.request.urlretrieve(suicide_rate_url, filename='who_suicide_rates.csv')

rates = pd.read_csv(local_filename, names=['Country', 'Both', 'Female', 'Male'], skiprows=3)
rates.head(10)

A = rates[selection][['DFE', 'GDP_CD']].astype('float')
A['GDP_CD'] = A['GDP_CD']/1000
b = rates[selection]['Both'].astype('float')
A = sm.add_constant(A)
est = sm.OLS(b, A).fit()

X, Y = np.meshgrid(np.linspace(A.DFE.min(), A.DFE.max(), 100), 
                       np.linspace(A.GDP_CD.min(), A.GDP_CD.max(), 100))
Z = est.params[0] + est.params[1] * X + est.params[2] * Y


fig = plt.figure(figsize=(7, 5))
ax = Axes3D(fig, azim=-135, elev=15)

surf = ax.plot_surface(X, Y, Z, cmap=plt.cm.RdBu, alpha=0.6, linewidth=0)


resid = b - est.predict(A)
ax.scatter(A.DFE, A.GDP_CD, b,  alpha=1.0)

ax.set_xlabel('DFE')
ax.set_ylabel('GDP_CD/1000')
ax.set_zlabel('Both')

plt.show()
