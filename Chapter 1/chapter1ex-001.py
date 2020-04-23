import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

var = plt.style.available

plt.style.use(os.path.join(os.getcwd(), 'mystyle.mplstyle'))

cols = ['user id', 'item id', 'rating', 'timestamp']
ratings = pd.read_csv('data/ratings.dat', sep='::',
                      index_col=False, names=cols, encoding="UTF-8")

ratings.head()

rating_counts = ratings['rating'].value_counts()
sorted_counts = rating_counts.sort_index()

sorted_counts.plot(kind='bar', color='SteelBlue')
plt.title('Movie ratings')
plt.xlabel('Rating')
plt.ylabel('Count')

plt.show()
