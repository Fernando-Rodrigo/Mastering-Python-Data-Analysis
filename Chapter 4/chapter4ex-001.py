import urllib.request

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas.io

import scipy.stats as st

suicide_rate_url = 'http://apps.who.int/gho/athena/data/xmart.csv?target=GHO/MH_12&profile=crosstable&filter=COUNTRY:*;REGION:*&x-sideaxis=COUNTRY&x-topaxis=GHO;YEAR;SEX'
local_filename, headers = urllib.request.urlretrieve(suicide_rate_url, filename='who_suicide_rates.csv')
#local_filename = 'who_suicide_rates.csv_backup'

rates = pandas.read_csv(local_filename, names=['Country','Both', 'Female', 'Male'], skiprows=3)
#rates.head(10)
