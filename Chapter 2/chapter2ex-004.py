import matplotlib.pyplot as plt
import pandas as pd
import os

var = plt.style.available

plt.style.use(os.path.join(os.getcwd(), 'mystyle.mplstyle'))

gss_data = pd.read_stata('data/GSS2012merged_R5.dta', convert_categoricals=False)
gss_data.head()

gss_data.index = gss_data['id']
gss_data.drop('id', 1, inplace=True)
gss_data.head()

inc_age = gss_data[['realrinc', 'age']].dropna()
lowinc_age = inc_age[inc_age['realrinc'] < 3.0E5]

ax_list = lowinc_age.hist(bins=20, figsize=(8,3),
                          xrot=45, color='SteelBlue')
ax1, ax2 = ax_list[0]
ax1.set_title('Age (years)')
ax2.set_title('Real Income ($)')
for ax in ax_list[0]:
    ax.grid()
    ax.locator_params(axis='x' ,nbins=6)
    ax.locator_params(axis='y' ,nbins=4)

plt.show()
