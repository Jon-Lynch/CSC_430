# Jonathan Lynch
# 4/4/20
# https://youtu.be/1ZXSwZqXeZ4
# "I have not given or received any unauthorized assistance on this assignment."

def coprime(a,b):
    'funtion that determines whether two numbers are coprime'
    divisors = []
    for x in range(2, min(a,b)+1):           # iterate from 2 through min number
        if min(a,b)%x == 0:                  # determine divisors of lowest number
            divisors.append(x)               # add divisors to empty list
    for y in divisors:
        if max(a,b)%y == 0:                  # test if any divisors of min are also divisors of max
            return False                     # if max and min share a common divisor return False
    return True                              # return True if no divisors shared

def coprime_test_loop():
    'function that requires user input to generate coprime message response'
    while True:
        a = input('Please enter a number: ')                     # prompt user to enter number
        a = int(a)                                               # convert str input into an int
        b = input('Please enter a number: ')                     # prompt user to enter number
        b = int(b)                                               # convert str input into an int
        if coprime(a,b) == False:                                # test whether coprime
            print('The numbers you entered are not coprime.')    # print message if not coprime
        else:
            print('The numbers you entered are coprime.')        # print message if coprime
        stop = input('Would you like to stop (yes/no)? ')        # determine if user wants to stop
        if stop == 'yes':
            break                                                # exit while loop if user wants to stop
