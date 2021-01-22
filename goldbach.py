# Jonathan Lynch
# 4/16/20
# https://youtu.be/_fvC4MtFyeo
# "I have not given or received any unauthorized assistance on this assignment."

def prime(num):
    'Determines if number is prime'
    if num == 1:                                             # test whether number equals one
        return False                                         # return False if number is 1
    if num == 2:                                             # test whether number equals two
        return True                                          # return True if number is 2
    for i in range(2, num):                                  # iterate through numbers in range 
        if num % i == 0:                                     # test whether number divides evenly
            return False                                     # return False if number divisible by number in range
    return True                                              # return True if number not divisible by any number in range

def prime_list(num):
    'Creates a list of primes based on a given number'
    res = []                                                 # create an empty list
    for i in range(2, num + 1):                              # iterate through numbers in range
        if prime(i) == True:                                 # determine if number is prime
            res.append(i)                                    # add number to list if prime
    return res                                               # return list of prime numbers

def even_list(num):
    'Create a list of even numbers based on a given number'
    res = []                                                 # create an empty list
    for i in range(4, num + 1, 2):                           # iterate through numbers in range, in increments of two
        res.append(i)                                        # add even numbers to empty list
    return res                                               # return list of even numbers

def dictionary(evens, primes):
    'Creates two dictionaries based on evens and primes lists, and prints two primes summing to each item in evens list'
    dict1 = {}                                                                            # create an empty dictionary (dictionary 1)
    dict2 = {}                                                                            # create an empty dictionary (dictionary 2)
    for even in evens:                                                                    # iterate through list of even numbers
        for j in primes:                                                                  # iterate through list of prime numbers
            for k in primes:                                                              # iterate through list of prime numbers
                if j + k == even:                                                         # determine if prime numbers sum to even number
                    if even not in dict1:                                                 # determine if key in dictionary 1
                        dict1[even] = j                                                   # add first prime that sums to even number to dictionary 1, if key not in dictionary
                    if even not in dict2:                                                 # determine if key in dictionary 2
                        dict2[even] = k                                                   # add second prime that sums to even number to dictionary 2, if key not in dictionary
                        print('{} = {} + {}'.format(even, dict1[even], dict2[even]))      # print each even, along with the first and second primes that sum to it, in a formatted print statement 

def sum_of_primes(num):
    'Main funtion that prints two primes summing to each even number, four through given input number'
    primes = prime_list(num)                                         # list of primes from prime_list function
    evens = even_list(num)                                           # list of evens from even_list function
    dictionary(evens, primes)                                        # dictionary function that accepts evens and primes lists, and prints two primes that sum to each even








