import urllib.request

import matplotlib.pyplot as plt
import pandas as pd

suicide_rate_url = 'http://apps.who.int/gho/athena/data/xmart.csv?target=GHO/MH_12&profile=crosstable&filter=COUNTRY' \
                   ':*;REGION:*&x-sideaxis=COUNTRY&x-topaxis=GHO;YEAR;SEX '
local_filename, headers = urllib.request.urlretrieve(suicide_rate_url, filename='who_suicide_rates.csv')

rates = pd.read_csv(local_filename, names=['Country', 'Both', 'Female', 'Male'], skiprows=3)
rates.head(10)

rates.plot.hist(stacked=True, y=['Male', 'Female'],
                bins=30, color=['Coral', 'Green'])
plt.xlabel('Rate')

plt.show()
