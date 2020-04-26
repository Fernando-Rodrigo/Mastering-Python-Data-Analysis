import urllib.request
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.transforms as transforms
import numpy as np
import pandas as pd
import scipy.stats as st

suicide_rate_url = 'http://apps.who.int/gho/athena/data/xmart.csv?target=GHO/MH_12&profile=crosstable&filter=COUNTRY' \
                   ':*;REGION:*&x-sideaxis=COUNTRY&x-topaxis=GHO;YEAR;SEX '
local_filename, headers = urllib.request.urlretrieve(suicide_rate_url, filename='who_suicide_rates.csv')

coords = pd.read_csv('C:/Users/Fernando/Documents/Programas de computador/PacktCodes/Mastering-Python-Data-Analysis/Chapter 4/data/countrycentroids/countrycentroidsprimary.csv', sep='\t')
coords.keys()

rates = pd.read_csv(local_filename, names=['Country', 'Both', 'Female', 'Male'], skiprows=3)
rates.head(10)

eta = 1.
beta = 1.5
beta, loc, eta = st.weibull_min.fit(rates['Both'], floc=0, scale=12)
np.random.seed(1100)
rvweib = st.weibull_min(beta, scale=eta)

rates['Lat'] = ''
rates['Lon'] = ''
for i in coords.index:
    ind = rates.Country.isin([coords.SHORT_NAME[i]])
    val = coords.loc[i, ['LAT', 'LONG']].values.astype('float')
    rates.loc[ind, ['Lat', 'Lon']] = list(val)

rates.head()

rates.loc[rates.Lat.isin(['']), ['Lat']] = np.nan
rates.loc[rates.Lon.isin(['']), ['Lon']] = np.nan
rates[['Lat', 'Lon']] = rates[['Lat', 'Lon']].astype('float')

rates['DFE'] = ''
rates['DFE'] = abs(rates.Lat)
rates['DFE'] = rates['DFE'].astype('float')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(rates.DFE, rates.Both, '.')

trans = transforms.blended_transform_factory(
    ax.transData, ax.transAxes)

rect = patches.Rectangle((0,0), width=23.5, height=1,
                         transform=trans, color='yellow',
                         alpha=0.5)
ax.set_xlabel('DFE')
ax.set_ylabel('Both')
ax.add_patch(rect)

plt.show()
