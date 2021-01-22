# Jonathan Lynch
# 5/29/20
# https://youtu.be/O_9ZjT8w29w
# "I have not given or received any unauthorized assistance on this assignment."

import numpy as np

a = np.arange(100)                    # create array 0 to 99 (inclusive)

b = np.arange(0, 100, 10)             # create array with 10 equally spaced values in range 0 to 100

c = np.linspace(0., 10., 101)         # create array in range 0 to 10 (inclusive) with steps of .1

d = np.random.random((10, 10))        # create a random array with dimensions 10x10

a.shape = (10, 10)                    # make array a two-dimensionsal, with dimensions 10x10

print(a[4,5])                         # print value in 4th row, 5th column of array a
print()                               # make new line

print(a[4])                           # print 4th row of array a
print()                               # make new line

print(d.sum())                        # print sum of array d                    
print()                               # make new line

print(a.max())                        # print max value in array a
print()                               # make new line

print(b.transpose())                  # print transpose of array b
print()                               # make new line

print(a+d)                            # print sum of array a and array d
print()                               # make new line

print(a*d)                            # print the element-wise multiplication of array a and array d
print()                               # make new line

print(np.dot(a, d))                   # print the matrix multiplication of array a and array d











