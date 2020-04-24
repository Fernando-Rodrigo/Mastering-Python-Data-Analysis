import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import scipy.stats as stats
from scipy.stats import linregress

var = plt.style.available

plt.style.use(os.path.join(os.getcwd(), 'mystyle.mplstyle'))

gss_data = pd.read_stata('data/GSS2012merged_R5.dta', convert_categoricals=False)
gss_data.head()

gss_data.index = gss_data['id']
gss_data.drop('id', 1, inplace=True)
gss_data.head()

gss_data['age'].hist()
plt.grid()
plt.locator_params(nbins=5)

gss_data['age'].hist(bins=25)
plt.grid()
plt.locator_params(nbins=5)

inc_age = gss_data[['realrinc', 'age']]
inc_age.head(10)
# inc_age.tail(10)

inc_age = gss_data[['realrinc', 'age']].dropna()
inc_age.head(10)

ax_list = inc_age.hist(bins=40, figsize=(8,3), xrot=45)
for ax in ax_list[0]:
    ax.locator_params(axis='x', nbins=6)
    ax.locator_params(axis='y', nbins=3)

inc_age[inc_age['realrinc'] > 3.0E5].count()
inc_age[inc_age['realrinc'] > 3.0E5].head()

inc_age = gss_data[['realrinc', 'age']].dropna()
lowinc_age = inc_age[inc_age['realrinc'] < 3.0E5]
ax_list = lowinc_age.hist(bins=20, figsize=(8,3), xrot=45)
for ax in ax_list[0]:
    ax.grid()
    ax.locator_params(axis='x', nbins=6)
    ax.locator_params(axis='y', nbins=3)

ax_list = lowinc_age.hist(bins=20, figsize=(8,3),
                          xrot=45, color='SteelBlue')
ax1, ax2 = ax_list[0]
ax1.set_title('Age (years)')
ax2.set_title('Real Income ($)')
for ax in ax_list[0]:
    ax.grid()
    ax.locator_params(axis='x', nbins=6)
    ax.locator_params(axis='y', nbins=4)

age = gss_data['age'].dropna()
age.plot(kind='kde', lw=2, color='Green')
plt.title('KDE plot for Age')
plt.xlabel('Age (years)')

"""ax = age.hist(bins=30, color='LightSteelBlue', normed=True)
age.plot(kind='kde', lw=2, color='Green', ax=ax)
plt.title('Histogram and KDE for Age')
plt.xlabel('Age (years)')"""

stats.probplot(age, dist='norm', plot=plt)

inc = gss_data['realrinc'].dropna()
lowinc = inc[inc < 3.0E5]
lowinc.describe()

lowinc.describe(percentiles=np.arange(0, 1.0, 0.1))

# lowinc.plot.box();
lowinc.plot(kind='box')
plt.locator_params(nbins=5)

inc_gen = gss_data[['realrinc', 'sex']]
inc_gen = inc_gen[inc_gen['realrinc'] < 3.0E5]
inc_gen.boxplot(column='realrinc', by='sex')
plt.title('')
plt.locator_params(nbins=5)

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
