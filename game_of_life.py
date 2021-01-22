# Jonathan Lynch
# 5/30/20
# https://youtu.be/oRPA3X-udZQ
# "I have not given or received any unauthorized assistance on this assignment."

import numpy as np
import matplotlib.pyplot as plt

def conway(s, p):                                                
    'create a random square board of size s, with probability p'
    board = np.random.random((s, s))                       # create random 2-D array with sxs dimensions
    for i in range(len(board)):                            # iterate through row indices of array
        for j in range(len(board)):                        # iterate through column indices of array
            if board[i][j] <= p:                           # determine if item at index i, j is less than or equal to probability
                board[i][j] = 1                            # set item equal to one if less than or equal to probability
            else:
                board[i][j] = 0                            # set item equal to zero if greater than probability
    return board                                           # return array


def advance(arr, t):
    'advances random board t time steps forward per specified rules'
    size = len(arr)                                                                             # determine length of array arr and assign to size
    time = 0                                                                                    # create counter time set to zero
    while time < t:                                                                             # enter while loop if time is less than t
        arr2 = np.zeros((size, size))                                                           # create 2-D array arr2 of zeros with dimensions sizexsize
        for i in range(len(arr)):                                                               # iterate through row indices of array arr
            for j in range(len(arr)):                                                           # iterate through column indices of array arr
                sum_neigh = arr[i][j-1] + arr[i][j-size+1] + arr[i-1][j] + arr[i-size+1][j]     # determine number of neighbors that are equal to one
                if arr[i][j] == 1. and sum_neigh < 2:                                           # determine if sum of neighbors is less than two and item at current index is one
                    arr2[i][j] = 0.                                                             # set item at same index in arr2 to zero
                if arr[i][j] == 1. and sum_neigh == 2 or arr[i][j] == 1. and sum_neigh == 3:    # determine if item at current index is one and sum of neighbors is either two or three
                    arr2[i][j] = 1.                                                             # set item at same index in arr2 to one
                if arr[i][j] == 1. and sum_neigh > 3:                                           # determine if item at current index is one and sum of neighbors is greater than three
                    arr2[i][j] = 0.                                                             # set item at same index in arr2 to zero
                if arr[i][j] == 0. and sum_neigh == 3:                                          # determine if item at current index is zero and sum of neighbors is exactly three
                    arr2[i][j] = 1.                                                             # set item at same index in arr2 to one
        time += 1                                                                               # increment counter time by one
        arr = arr2                                                                              # set initial array arr equal to arr2
    return arr2                                                                                 # return arr2

def display(s, p, t):
    'accepts size of array s, probability p, and time steps t, and generates plot of final array arr2'
    arr = conway(s, p)                                     # create random array with sxs dimensions and probability p set to arr
    arr2 = advance(arr, t)                                 # advance arr t time steps and set to arr2
    plt.imshow(arr2, cmap = plt.cm.Greens)                 # use colormap from pyplot to color ones from arr2 dark-green and zeros light-green
    plt.show()                                             # display plot

