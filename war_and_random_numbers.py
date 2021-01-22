# Jonathan Lynch
# 5/15/20
# https://youtu.be/FrZQpmINF4o
# "I have not given or received any unauthorized assistance on this assignment."

file = open('war-and-peace.txt')

def read():
    'reads though already opened file and creates a pseudo random list of ones and zeros'
    lst = []                                             # create empty list lst
    while len(lst) < 32:                                 # enter while loop if lst length less than 32
        while True:                                      # enter second while loop
            content = file.read(10)                      # read 10 characters of file into a string
            letter = content[-1]                         # set last character of string equal to letter
            if letter != ' ':                            # determine if last character is a blank space/empty string
                break                                    # exit while loop if not blank space/empty string
        content2 = file.read(10)                         # read 10 more characters of file into a string
        letter2 = content2[-1]                           # set last character of string equal to letter2                           
        if letter > letter2:                             # determine if letter greater than letter2 
            lst.append(1)                                # append 1 to lst if greater
        else:
            lst.append(0)                                # append 0 to lst if not greater
    return lst                                           # return lst


def seed_read(infile):
    'accepts newly opened file and begins reading from the start to create a list of ones and zeros that is the same each time'
    seed_lst = []                                        # create empty list seed_lst
    while len(seed_lst) < 32:                            # enter while loop if seed_lst length less than 32
        content = infile.read(10)                        # read first 10 characters of file into a string
        letter = content[-1]                             # set last string character equal to letter
        content2 = infile.read(10)                       # read second 10 characters of file into a string
        letter2 = content2[-1]                           # set last character of string equal to letter2
        if letter > letter2:                             # determine if letter greater than letter2
            seed_lst.append(1)                           # append 1 to seed_lst if greater
        else:
            seed_lst.append(0)                           # append 0 to seed_lst if not greater
    return seed_lst                                      # return seed_lst


def division(n):
    'creatses list of numbers beginning with .5, with each successfive number in list half of that preceeding it'
    lst = []                                             # create empty list
    while len(lst) < 32:                                 # enter while loop if list length less than 32
        n = n/2                                          # divide number by two
        lst.append(n)                                    # append result to list
    return lst                                           # return list

def r(lst, lst2):
    'accepts two lists and returns a pseudo random float between zero, inclusive, and one, non-inclusive'
    i = 0                                                # set i equal to zero
    r = 0                                                # set r equal to zero
    while i < 32:                                        # enter while loop if i less than 32
        num = lst[i]*lst2[i]                             # multiply items at index i from each list by one another 
        r += num                                         # add product to r
        i += 1                                           # increment i by 1
    return r

class WarAndPeacePseudoRandomNumberGenerator():
    'class that can be used to create objects with method which represents retreival of pseudo random number'
    def __init__(self, seed = 0):                        # initialize overloaded operator __init__, set seed default to 0
        self.seed = seed                                 # initialize self.seed
        if self.seed == 0:                               # determine if self.seed equals 0 (seed not set)
            lst = read()                                 # call read() function to return a list, and set to lst
            lst2 = division(1)                           # call division() function to return a list, and set to lst2                          
            self.r = r(lst, lst2)                        # create pseudo random float between zero (inclusive) and one (exclusive), set to self.r
        if self.seed > 0:                                # determine if seed was set (self.seed > 0)
            infile = open('war-and-peace.txt')           # open file to read from start, if seed set 
            seed_lst = seed_read(infile)                 # call seed_read function to create a list, and set to seed_lst 
            lst2 = division(1)                           # call division function to return a list, and set to lst2
            self.r = r(seed_lst, lst2)                   # create a float between zero (inclusive) and one (exclusive); will be same each time
    def random(self):                                    # create random method
        return self.r                                    # return self.r, pseudo random float (unless seed set)





            
