import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

var = plt.style.available
plt.style.use(os.path.join(os.getcwd(), 'mystyle.mplstyle'))

cols = ['movie id', 'movie title', 'genre']
movies = pd.read_csv('data/movies.dat', sep='::', index_col=False, names=cols, encoding="UTF-8")

movies.head()

drama = movies[movies['genre'] == 'Crime|Drama']

is_drama = movies['genre'] == 'Crime|Drama'
is_drama.head()

drama_ids = drama['movie id']
drama_ids.head()

print(is_drama.head())
print(drama_ids.head())
