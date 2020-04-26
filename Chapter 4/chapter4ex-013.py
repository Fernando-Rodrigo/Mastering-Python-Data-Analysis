import urllib.request
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.transforms as transforms
import numpy as np
import pandas as pd
import scipy.stats as st
from scipy.stats import linregress
import statsmodels.formula.api as smf
from statsmodels.sandbox.regression.predstd import wls_prediction_std

suicide_rate_url = 'http://apps.who.int/gho/athena/data/xmart.csv?target=GHO/MH_12&profile=crosstable&filter=COUNTRY' \
                   ':*;REGION:*&x-sideaxis=COUNTRY&x-topaxis=GHO;YEAR;SEX '
local_filename, headers = urllib.request.urlretrieve(suicide_rate_url, filename='who_suicide_rates.csv')

rates = pd.read_csv(local_filename, names=['Country', 'Both', 'Female', 'Male'], skiprows=3)
rates.head(10)

coords = pd.read_csv('C:/Users/Fernando/Documents/Programas de computador/PacktCodes/Mastering-Python-Data-Analysis/Chapter 4/data/countrycentroids/countrycentroidsprimary.csv', sep='\t')
coords.keys()

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

bins = np.arange(23.5, 65+1,10, dtype='float')
bins = np.linspace(23.5, 65,11, dtype='float')
# now group the data into the bins
groups_rates = rates.groupby(np.digitize(rates.DFE, bins))

mod = smf.ols("Both ~ DFE", rates[selection]).fit()
print(mod.summary())

prstd, iv_l, iv_u = wls_prediction_std(mod)

fig = plt.figure()
ax = fig.add_subplot(111)
rates.plot(kind='scatter', x='DFE', y='Both', ax=ax)

xmin, xmax = min(rates['DFE']), max(rates['DFE'])

ax.plot([mindfe, xmax], [mod.fittedvalues.min(), mod.fittedvalues.max()], 
        'IndianRed', lw=1.5)
ax.plot([mindfe, xmax], [iv_u.min(), iv_u.max()], 'r--', lw=1.5)
ax.plot([mindfe, xmax], [iv_l.min(), iv_l.max()], 'r--', lw=1.5)

ax.errorbar(groups_rates.mean().DFE, 
            groups_rates.mean().Both, 
            yerr=np.array(groups_rates.std().Both),
            ls='None',
            lw=1.5,
            color='Green')

trans = transforms.blended_transform_factory(
    ax.transData, ax.transAxes)

rect = patches.Rectangle((0,0), width=mindfe, height=1,
                         transform=trans, color='Yellow',
                         alpha=0.5)

ax.add_patch(rect)
ax.grid(lw=1, ls='dashed')
ax.set_xlim((xmin,xmax+3))

plt.show()
