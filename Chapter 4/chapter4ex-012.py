import urllib.request
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.transforms as transforms
import numpy as np
import pandas as pd
import scipy.stats as st
from scipy.stats import linregress

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

mindfe = 30.
selection = ~rates.DFE.isnull() * rates.DFE>mindfe
rv = rates[selection].as_matrix(columns=['DFE','Both'])
a, b, r, p, stderr = linregress(rv.T)
print('slope:{0:.4f}\nintercept:{1:.4f}\nrvalue:{2:.4f}\npvalue:{3:.4f}\nstderr:{4:.4f}'.format(a, b, r, p, stderr))

fig = plt.figure()
ax = fig.add_subplot(111)
rates.plot(kind='scatter', x='DFE', y='Both', ax=ax)
xdata = rates['DFE']
xmin, xmax = min(xdata), max(xdata)
xvalues = np.linspace(mindfe, xmax, 200)
yvalues = a * xvalues + b
ax.plot(xvalues, yvalues, color='red', lw=1.5)
ax.grid(lw=1, ls='dashed');


ax.errorbar(groups_rates.mean().DFE, 
            groups_rates.mean().Both, 
            yerr=np.array(groups_rates.std().Both),
            #xerr=,
            marker='.', 
            ls='None',
            lw=1.5,
            color='g', 
            ms=1)

trans = transforms.blended_transform_factory(
    ax.transData, ax.transAxes)

rect = patches.Rectangle((0,0), width=mindfe, height=1,
                         transform=trans, color='yellow',
                         alpha=0.5)

ax.add_patch(rect);
ax.set_xlim((xmin,xmax+3))

plt.show()
