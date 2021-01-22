# Jonathan Lynch
# 5/1/20
# https://youtu.be/YP9zrLx5KC4
# "I have not given or received any unauthorized assistance on this assignment."

import random

class SixSidedDie:                                                # create class SixSidedDie
    def __init__(self, low = 1, high = 7):                        # implement __init__ overloading operator (die parameters default values set)
        'initialize parameters for a die with six sides'
        self.low = low                                            # establish low die limit
        self.high = high                                          # establish high die limit
    def roll(self):                                               # create roll method for class SixSidedDie
        'simulates one roll of a six sided die'
        self.die = random.randrange(self.low, self.high)          # simulate one roll of die
        return self.die                                           # return roll value
    def getFaceValue(self):                                       # create getFaceValue method for class
        'returns the value of a single roll' 
        return self.die                                           # return roll value
    def __repr__(self):                                           # implement overloading operator __repr__
        'canonical string representation SixSidedDie(roll)'
        return 'SixSidedDie({})'.format(self.die)                 # return canonical string representation

class TenSidedDie(SixSidedDie):                                   # create class TenSidedDie (using inheritance)
    def roll(self):                                               # create roll method for class (using extension)
        'simulates one roll of a ten sided die'
        self.high = 11                                            # reestablish high die limit
        return SixSidedDie.roll(self)                             # return roll value
    def __repr__(self):                                           # implement overloading operator __repr__
        'canonical string representation TenSidedDie(roll)'
        return 'TenSidedDie({})'.format(self.die)                 # return canonical string representation

class TwentySidedDie(SixSidedDie):                                # create class TwentySidedDie (using inheritance)
    def roll(self):                                               # create roll method for class (using extension)                                               
        'simulates one roll of a twenty sided die'
        self.high = 21                                            # reesteblish high die limit
        return SixSidedDie.roll(self)                             # return roll value
    def __repr__(self):                                                  # implement overloading operator __repr__
        'canonical string representation TwentySidedDie(roll)'
        return 'TwentySidedDie({})'.format(self.die)                     # return canonical string representation

class Cup:                                                                                                  # create class Cup
    def __init__(self, six_sided = 1, ten_sided = 1, twenty_sided = 1, low = 1, high = 7):                  # initialize default values (dice amounts and limits)
        'initialize parameters for a cup holding three types of dice (default set to one of each type)'
        self.six = six_sided                                                         # establish six sided die
        self.ten = ten_sided                                                         # establush ten sided die
        self.twenty = twenty_sided                                                   # establish twenty sided die
        self.low = low                                                               # establish low die limit
        self.high = high                                                             # establish high die limit
    def roll(self):                                                                  # create roll method for class
        'simulate one roll of any number of dice of three separate types'
        self.six_dice = ''                                                           # empty string for six sided dice (to use in __repr__)
        self.ten_dice = ''                                                           # empty stirng for ten sided dice (to use in __repr__)
        self.twenty_dice = ''                                                        # empty string for twenty sided dice (to use in __repr__)
        self.six = [SixSidedDie.roll(self) for i in range(self.six)]                 # create list containing all rolls of six sided dice
        self.ten = [TenSidedDie.roll(self) for i in range(self.ten)]                 # create list containing all rolls of ten sided dice
        self.twenty = [TwentySidedDie.roll(self) for i in range(self.twenty)]        # create list containing all rolls of twenty sided dice
        self.sum = sum(self.six) + sum(self.ten) + sum(self.twenty)                  # sum the total values in all three lists
        for x in self.six:                                                           # iterate through six sided die list
            self.six_dice += 'SixSidedDie({}), '.format(x)                           # create string item for each value and add to empty string for six sided dice
        for y in self.ten:                                                           # iterate through ten sided die list
            self.ten_dice += 'TenSidedDie({}), '.format(y)                           # create string item for each value and add to empty string for ten sided dice
        for z in self.twenty:                                                        # iterate through twenty sided die list
            self.twenty_dice += 'TwentySidedDie({}), '.format(z)                     # create string item for each value and add to empty string for twenty sided dice
        return self.sum                                                              # return the sum of total values from all three lists
    def getSum(self):                                                                # create a getSum method for class
        'return the sum of all dice for a single roll'
        return self.sum                                                              # return the sum of all dice for a sinle roll
    def __repr__(self):                                                                                       # implement overloading overator __repr__
        'canonical string representation Cup(SixSidedDie(roll), TenSidedDie(roll), TwentySidedDie(roll))' 
        return 'Cup({}, {}, {})'.format(self.six_dice[:-2], self.ten_dice[:-2], self.twenty_dice[:-2])        # return canonical string representation

        
