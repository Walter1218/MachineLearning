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
    A = utility[x - 1]
    B = utility[y - 1]
    I = [ (rxi,ryi) for (rxi,ryi) in zip(A,B) if rxi>0 and ryi>0  ]
    #print(I)
    if len(I)>0:
        pa = 0
        pb = 0
        sum_pab = 0
        sum_pyz = 0
        for (rxi,ryi) in I:
            #print rxi,ryi
            pa = (rxi - user[x - 1].avg_r)
            pb = (ryi - user[y - 1].avg_r)
            sum_pab += pa * pb
            sum_pyz += (pa * pa) * (pb * pb)
        #print(sum_pab,sum_pyz)
        results = sum_pab/sum_pyz
    else:
        results = 0
    return results

# Guesses the ratings that user with id, user_id, might give to item with id, i_id.
# We will consider the top_n similar users to do this.
def guess(user_id, i_id, top_n):
    """
    Insert your code here.
    """
    n_users = utility.shape[0]
    pcs_matrix = np.zeros((n_users, n_users))
    for i in range(0, n_users):
        for j in range(0, n_users):
            pcs_matrix[i][j] = pcs(i , j )
    similarity_list = []
    #print(n_users)
    for i in range(0, n_users):
        if i != (user_id-1):
            similarity_list.append((pcs_matrix[user_id - 1][i],i + 1))
    similarity_list.sort(key=lambda x:x[0],reverse=True)
    similarity_list = similarity_list[:top_n]
    #print(similarity_list)
    #TODO FINISHE HERE
    rating_topN = [ri-user[u-1].avg_r for u,ri in [(i,utility[i-1][i_id-1]) for v,i in similarity_list if utility[i-1][i_id-1]>0 ]]
    avg = np.mean(rating_topN) if len(rating_topN)>0 else 0
    #print(avg)
    return abs(user[user_id-1].avg_r + avg)

## THINGS THAT YOU WILL NEED TO DO:
# Perform clustering on users and items
# Predict the ratings of the user-item pairs in rating_test
# Find mean-squared error
