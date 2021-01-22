# Jonathan Lynch
# 5/17/20
# https://youtu.be/h8VgVfcIusk
# "I have not given or received any unauthorized assistance on this assignment."

file = open('war-and-peace.txt')
import math

def read():
    'reads though already opened file and creates a pseudo random list of ones and zeros'
    lst = []                                             # create empty list lst
    while len(lst) < 32:                                 # enter while loop if lst length less than 32
        while True:                                      # enter second while loop
            content = file.read(100)                     # read 100 characters of file into a string
            letter = content[-1]                         # set last character of string equal to letter
            if letter != ' ':                            # determine if last character is a blank space/empty string
                break                                    # exit while loop if not blank space/empty string
        content2 = file.read(100)                        # read 100 more characters of file into a string
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
        content = infile.read(100)                       # read first 100 characters of file into a string
        letter = content[-1]                             # set last string character equal to letter
        content2 = infile.read(100)                      # read second 100 characters of file into a string
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
    'class that can be used to create objects with method which retrieves pseudo random number'
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

class Point:
    'class that creates a point object'
    def __init__(self, xcoord, ycoord):                  # initialize overloaded operator __init__ accepting two arguments
        self.x = xcoord                                  # initialize self.x
        self.y = ycoord                                  # initialize self.y
    def get(self):                                       # create get method
        return (self.x, self.y)                          # return self.x and self.y
    def getx(self):                                      # create getx method
        return self.x                                    # return self.x
    def gety(self):                                      # create gety method
        return self.y                                    # return self.y

def distance(p1, p2):
    'accepts two points and returns the distance between them'
    x1 = p1.getx()                                       # set x coordinate of object p1 to x1
    x2 = p2.getx()                                       # set x coordinate of object p2 to x2
    y1 = p1.gety()                                       # set y coordinate of object p1 to y1
    y2 = p2.gety()                                       # set y coordinate of object p2 to y2
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)        # calculate the distance between two point objects
    return dist                                          # return calculated distance

class Ellipse:
    'class that accepts two points and width to represent an ellipse'
    def __init__(self, p1, p2, w):                       # initialize overloaded operator __init__ accepting three arguments
        self.p1 = p1                                     # initialize self.p1
        self.p2 = p2                                     # initialize self.p2
        self.w = w                                       # initialize self.w
    def inside(self, p3):                                # create method inside that determines if a point is inside of ellipse
        dist1 = distance(self.p1, p3)                    # calculate distance between accepted point object and object p1 
        dist2 = distance(self.p2, p3)                    # calculate distance between accepted point object and object p2
        return dist1 + dist2 < self.w                    # return True if sum of two distances is less than self.w, and False otherwise
    def getw(self):                                      # create method getw
        return self.w                                    # return self.w
    def getx1(self):                                     # create getx1 method
        return self.p1.getx()                            # return x coordinate of object p1
    def getx2(self):                                     # create getx2 method
        return self.p2.getx()                            # return x coordinate of object p2
    def gety1(self):                                     # create gety1 method
        return self.p1.gety()                            # return y coordinate of object p1
    def gety2(self):                                     # create gety2 method
        return self.p2.gety()                            # return y coordinate of object p2

class ComputeEllipsesOverlap:
    'class that accepts two ellipses and returns the approximate area of overlap through method area'
    def __init__(self, e1, e2):                                 # initialize overloaded operator __init__ accepting two arguments
        self.e1 = e1                                            # initialize self.e1
        self.e2 = e2                                            # initialize self.e2
    def area(self):                                             # create method area that determines area of overlap of two ellipses
        shots = 0                                               # create counter shots set to zero
        hits = 0                                                # create counter hits set to zero
        left_right = []                                         # create empty list left_right
        top_bottom = []                                         # create empty list top_bottom
        ww = []                                                 # create empty list ww
        left_right.append(self.e1.getx1())                      # append first x coordinate of object e1 to left_right 
        left_right.append(self.e1.getx2())                      # append second x coordinate of object e1 to left_right
        left_right.append(self.e2.getx1())                      # append first x coordinate of object e2 to left_right
        left_right.append(self.e2.getx2())                      # append second x coordinate of object e2 to left_right
        top_bottom.append(self.e1.gety1())                      # append first y coordinate of object e1 to top_bottom
        top_bottom.append(self.e1.gety2())                      # append second y coordinate of object e1 to top_bottom
        top_bottom.append(self.e2.gety1())                      # append first y coordinate of object e2 to top_bottom
        top_bottom.append(self.e2.gety2())                      # append second y coordinate of object e2 to top_bottom
        ww.append(self.e1.getw())                               # append width of e1 to ww 
        ww.append(self.e2.getw())                               # append width of e2 to ww
        left_bound = min(left_right) - (max(ww)/2)              # subtract the max width divided by two from the min x coordinate and set to left_bound
        right_bound = max(left_right) + (max(ww)/2)             # add the max width divided by two to the max x coordinate and set to right_bound 
        top_bound = max(top_bottom) + (max(ww)/2)               # add the max width divided by two to the max y coordinate and set to top_bound
        bottom_bound = min(top_bottom) - (max(ww)/2)                    # subtract the max width divided by two from the min y coordinate and set to bottom_bound
        area = (right_bound - left_bound)*(top_bound - bottom_bound)    # calculate the area using right_bound, left_bound, top_bound, and bottom_bound
        while shots < 1000:                                             # enter while loop if shots counter is less than 1000 
            prn1 = WarAndPeacePseudoRandomNumberGenerator()             # create object of class WarAndPeacePseudoRandomNumberGenerator set to prn1
            prn2 = WarAndPeacePseudoRandomNumberGenerator()                       # create object of class WarAndPeacePseudoRandomNumberGenerator set to prn2
            random_x = left_bound + prn1.random()*(right_bound - left_bound)      # create random x value within range of left_bound and right_bound set to random_x
            random_y = bottom_bound + prn2.random()*(top_bound - bottom_bound)    # create random y value within range of top_bound and bottom_bound set to random_y
            random_point = Point(random_x, random_y)                                                 # use random_x and random_y to create an object of class Point set to random_point                              
            if self.e1.inside(random_point) == True and self.e2.inside(random_point) == True:        # deterine if random_point is inside both ellipse objects
                hits += 1                                                                            # increment hits counter if inside
                shots += 1                                                                           # increment shots counter if inside
            else:
                shots += 1                                                                           # if outside increment shots counter only
        return (hits/shots)*area                                                                     # return approximated area of overlap of two ellipses





            
