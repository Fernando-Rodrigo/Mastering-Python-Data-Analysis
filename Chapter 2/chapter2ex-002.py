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
inc_age.head(10)

ax_list = inc_age.hist(bins=40, figsize=(8, 3), xrot=45)
for ax in ax_list[0]:
    ax.locator_params(axis='x', nbins=6)
    ax.locator_params(axis='y', nbins=3)

plt.show()
