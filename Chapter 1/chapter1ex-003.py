import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

var = plt.style.available
plt.style.use(os.path.join(os.getcwd(), 'mystyle.mplstyle'))
cols = ['user id', 'item id', 'rating', 'timestamp']
ratings = pd.read_csv('data/ratings.dat', sep='::',
                      index_col=False, names=cols, encoding="UTF-8")

cols = ['movie id','movie title','genre']
movies = pd.read_csv('data/movies.dat', sep='::', index_col=False, names=cols, encoding="UTF-8")

ratings.head()

rating_counts = ratings['rating'].value_counts()
sorted_counts = rating_counts.sort_index()

movies.head()

drama = movies[movies['genre'] == 'Crime|Drama']

is_drama = movies['genre'] == 'Crime|Drama'
is_drama.head()


drama_ids = drama['movie id']
drama_ids.head()

criterion = ratings['item id'].map(lambda x: (drama_ids == x).any())
drama_ratings = ratings[criterion]
drama_ratings.head()

rating_counts = drama_ratings['rating'].value_counts()
sorted_counts = rating_counts.sort_index()
sorted_counts.plot(kind='bar', color='SteelBlue')
plt.title('Movie ratings for crime dramas')
plt.xlabel('Rating')
plt.ylabel('Count')

plt.show()
