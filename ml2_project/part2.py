#!/bin/python
from movielens import *
import numpy as np
from sklearn.metrics import mean_squared_error

# Store data in arrays
user = []
item = []
rating = []
rating_test = []

# Load the movie lens dataset into arrays
d = Dataset()
d.load_users("data/u.user", user)
d.load_items("data/u.item", item)
d.load_ratings("data/u.base", rating)
d.load_ratings("data/u.test", rating_test)

n_users = len(user)
n_items = len(item)

# The utility matrix stores the rating for each user-item pair in the matrix form.
# Note that the movielens data is indexed starting from 1 (instead of 0).
utility = np.zeros((n_users, n_items))
for r in rating:
    utility[r.user_id-1][r.item_id-1] = r.rating

# Finds the average rating for each user and stores it in the user's object
for i in range(n_users):
    rated = np.nonzero(utility[i])
    n = len(rated[0])
    if n != 0:
        user[i].avg_r = np.mean(utility[i][rated])
    else:
        user[i].avg_r = 0.

print utility

# Finds the Pearson Correlation Similarity Measure between two users
def pcs(x, y):
    """
    Insert your code here.
    """
    return 0.0

# Guesses the ratings that user with id, user_id, might give to item with id, i_id.
# We will consider the top_n similar users to do this.
def guess(user_id, i_id, top_n):
    """
    Insert your code here.
    """
    return 0.0

## THINGS THAT YOU WILL NEED TO DO:
# Perform clustering on users and items
# Predict the ratings of the user-item pairs in rating_test
# Find mean-squared error
