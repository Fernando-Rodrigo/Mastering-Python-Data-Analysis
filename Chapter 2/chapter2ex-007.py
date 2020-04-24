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

age = gss_data['age'].dropna()
age.plot(kind='kde', lw=2, color='Green')
ax = age.hist(bins=30, color='LightSteelBlue', normed=True)
age.plot(kind='kde', lw=2, color='Green', ax=ax)
plt.title('Histogram and KDE for Age')
plt.xlabel('Age (years)')

plt.show()
