# Jonathan Lynch
# 5/2/20
# https://youtu.be/iUpxy7idzeE
# "I have not given or received any unauthorized assistance on this assignment."

import random


class SixSidedDie:                                                # create class SixSidedDie
    # implement __init__ overloading operator (die parameters default values set)
    def __init__(self, low=1, high=7):
        'initialize parameters for a die with six sides'
        # establish low die limit
        self.low = low
        # establish high die limit
        self.high = high

    # create roll method for class SixSidedDie
    def roll(self):
        'simulates one roll of a six sided die'
        # simulate one roll of die
        self.die = random.randrange(self.low, self.high)
        return self.die                                           # return roll value

    # create getFaceValue method for class
    def getFaceValue(self):
        'returns the value of a single roll'
        return self.die                                           # return roll value

    # implement overloading operator __repr__
    def __repr__(self):
        'canonical string representation SixSidedDie(roll)'
        # return canonical string representation
        return 'SixSidedDie({})'.format(self.die)


# create class TenSidedDie (using inheritance)
class TenSidedDie(SixSidedDie):
    # create roll method for class (using extension)
    def roll(self):
        'simulates one roll of a ten sided die'
        # reestablish high die limit
        self.high = 11
        # return roll value
        return SixSidedDie.roll(self)

    # implement overloading operator __repr__
    def __repr__(self):
        'canonical string representation TenSidedDie(roll)'
        # return canonical string representation
        return 'TenSidedDie({})'.format(self.die)


# create class TwentySidedDie (using inheritance)
class TwentySidedDie(SixSidedDie):
    # create roll method for class (using extension)
    def roll(self):
        'simulates one roll of a twenty sided die'
        # reesteblish high die limit
        self.high = 21
        # return roll value
        return SixSidedDie.roll(self)

    # implement overloading operator __repr__
    def __repr__(self):
        'canonical string representation TwentySidedDie(roll)'
        # return canonical string representation
        return 'TwentySidedDie({})'.format(self.die)


# create class Cup
class Cup:
    # initialize default values (dice amounts and limits)
    def __init__(self, six_sided=1, ten_sided=1, twenty_sided=1, low=1, high=7):
        'initialize parameters for a cup holding three types of dice (default set to one of each type)'
        # establish six sided die
        self.six = six_sided
        # establush ten sided die
        self.ten = ten_sided
        # establish twenty sided die
        self.twenty = twenty_sided
        # establish low die limit
        self.low = low
        # establish high die limit
        self.high = high

    # create roll method for class
    def roll(self):
        'simulate one roll of any number of dice of three separate types'
        # empty string for six sided dice (to use in __repr__)
        self.six_dice = ''
        # empty stirng for ten sided dice (to use in __repr__)
        self.ten_dice = ''
        # empty string for twenty sided dice (to use in __repr__)
        self.twenty_dice = ''
        # create list containing all rolls of six sided dice
        self.six = [SixSidedDie.roll(self) for i in range(self.six)]
        # create list containing all rolls of ten sided dice
        self.ten = [TenSidedDie.roll(self) for i in range(self.ten)]
        # create list containing all rolls of twenty sided dice
        self.twenty = [TwentySidedDie.roll(self) for i in range(self.twenty)]
        # sum the total values in all three lists
        self.sum = sum(self.six) + sum(self.ten) + sum(self.twenty)
        # iterate through six sided die list
        for x in self.six:
            # create string item for each value and add to empty string for six sided dice
            self.six_dice += 'SixSidedDie({}), '.format(x)
        # iterate through ten sided die list
        for y in self.ten:
            # create string item for each value and add to empty string for ten sided dice
            self.ten_dice += 'TenSidedDie({}), '.format(y)
        # iterate through twenty sided die list
        for z in self.twenty:
            # create string item for each value and add to empty string for twenty sided dice
            self.twenty_dice += 'TwentySidedDie({}), '.format(z)
        # return the sum of total values from all three lists
        return self.sum

    # create a getSum method for class
    def getSum(self):
        'return the sum of all dice for a single roll'
        # return the sum of all dice for a sinle roll
        return self.sum

    # implement overloading overator __repr__
    def __repr__(self):
        'canonical string representation Cup(SixSidedDie(roll), TenSidedDie(roll), TwentySidedDie(roll))'
        # return canonical string representation
        return 'Cup({}, {}, {})'.format(self.six_dice[:-2], self.ten_dice[:-2], self.twenty_dice[:-2])


# define greeting function
def greeting():
    'greets the user, obtains name, and determines if user wants to play game'
    # request user input (name)
    name = input('Hello! What is your name? ')
    print('Hi {}, I have credited your account $100.'.format(
        name))                  # print account balance for user
    play = input('Would you like to play a game (yes/no)? ')
    if play == 'yes':
        return name
    else:
        return 0


# define get_wager function
def get_wager(goal, account):
    'determines how much user wants to bet/wager'
    print('The goal to hit is {}, without going over.'.format(
        goal))                 # print goal
    while True:
        # ask user for bet amount
        wager = input('How much would you like to bet? ')
        # convert bet amount to integer
        wager = int(wager)
        # determine if bet amount is valid
        if wager > 0 and wager <= account:
            # return bet amount, if valid
            return wager
        else:
            # prompt user to re-enter valid bet amount, if not
            print('Please enter a valid amount to bet.')


# define get_small function
def get_small():
    'prompts user to enter how many six sided dice to roll'
    # ask user to enter number of six sided dice to use
    small = input('How many six sided dice would you like to roll? ')
    # convert to integer
    small = int(small)
    # return number of six sided dice to roll
    return small


# define get_med function
def get_med():
    'prompts user to enter how many ten sided dice to roll'
    # ask user to enter number of ten sided dice to use
    med = input('How many ten sided dice would you like to roll? ')
    # convert to integer
    med = int(med)
    # return number of ten sided dice to roll
    return med


# define get_big function
def get_big():
    'prompts user to enter how many twenty sided dice to roll'
    # ask user to enter number of twenty sided dice to use
    big = input('How many twenty sided dice would you like to roll? ')
    # convert to integer
    big = int(big)
    # return number of twenty sided dice to roll
    return big


# define cup function
def cup(small, med, big):
    'accepts number of each size dice, and simulates one roll of each'
    # create instance object cup from class Cup
    cup = Cup(small, med, big)
    # simulate one roll of all dice in cup and return sum
    return cup.roll()


# define calculate function
def calculate(goal, roll, wager):
    'accepts goal, roll, and wager, and determines amount to add to account'
    # determine if roll equals goal
    if roll == goal:
        # return 10xwager if roll equals goal
        return wager * 10
    # determine if roll is lower than goal and within three
    elif roll < goal and goal - roll <= 3:
        # return 5xwager if so
        return wager * 5
    # determine if roll is lower than goal and within ten
    elif roll < goal and goal - roll <= 10:
        # return 2xwager if so
        return wager * 2
    else:
        # otherwise return zero
        return 0


# define result function
def result(name, roll, account):
    'informs user of result of dice roll, and provides updated account balance'
    print('Hi {}, the sum of the dice rolled was {}.'.format(
        name, roll))            # print sum of dice roll for user
    print('Your game account balance is now ${}.'.format(account)
          )                   # print new account balance for user


# main function
def main():
    'betting game requiring user input that simulates rolls of three different sized dice'
    # establish account balance
    account = 100
    # assign variable name to value returned by greeting function
    name = greeting()
    # enter while loop if user wants to play game
    while name != 0:
        # generate random number 1-100, and assign to goal
        goal = random.randrange(1, 101)
        # value returned by get_wager function assigned to wager
        wager = get_wager(goal, account)
        # deduct wager from account
        account -= wager
        # value returned by get_small function assigned to small
        small = get_small()
        # value returned by get_med function assigned to med
        med = get_med()
        # value returned by get_big function assigned to big
        big = get_big()
        # one roll of all dice simulated; total summed and assigned to roll
        roll = cup(small, med, big)
        # account balance updated based on returned value of calculate function
        account += calculate(goal, roll, wager)
        # user informed of result of dice roll, and provided new account balance
        result(name, roll, account)
        # user prompted to play again
        play_again = input('Would you like to play again (yes/no)? ')
        # determine whether user wants to play again
        if play_again == 'no':
            # exit while loop if user does not want to play again
            break


main()
