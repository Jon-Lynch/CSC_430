# Jonathan Lynch
# 4/17/20
# https://youtu.be/6lDfyGz5A9k
# "I have not given or received any unauthorized assistance on this assignment.'

def prime(num):
    'Determines whether a number is prime'
    if num == 1:                                                 # check whether number is one
        return False                                             # return False if 1
    if num == 2:                                                 # check whether number is two
        return True                                              # return True if 2
    for i in range(2, num):                                      # iterate through numbers in range
        if num % i == 0:                                         # determine if number passed to function is divisible by any in range
            return False                                         # return False if divisible
    return True                                                  # return True if not divisible

def happy(num):
    'Determines whether a number is happy'
    while True:                                                  # enter while loop
        num = str(num)                                           # convert integer num to a string
        lst = [i for i in num]                                   # create a list of strings for each digit of num
        lst2 = [int(i) for i in lst]                             # create a list, converting all string items back to integers
        lst3 = [i**2 for i in lst2]                              # create a list, with each list item squared
        num = sum(lst3)                                          # sum the list of squared numbers
        if num == 1:                                             # determine if this sum equals one
            return True                                          # return True if equals one
        if num == 4:                                             # determine if sum of squared numbers equals four
            return False                                         # return False if equals four
def greeting():
    'Greets the user and requests user input'
    print("Hello, let's determine if a number is happy or sad, and prime or non-prime.")        # print greeting
    num = input('Please enter a positive number: ')                                 # request user input
    num = int(num)                                                                  # convert to an integer
    return num                                                                      # return number

def print_stmt(num):
    'Prints a statement indicating if the number is happy/sad prime or happy/sad non-prime'
    if prime(num) == True and happy(num) == True:                                  # determine if num is prime and happy
        print('The number entered is happy prime.')                                # print result if prime and happy
    elif prime(num) == True and happy(num) == False:                               # determine if num is prime and sad
        print('The number entered is sad prime.')                                  # print result if prime and sad
    elif prime(num) == False and happy(num) == True:                               # determine if num is non-prime and happy
        print('The number entered is happy non-prime.')                            # print result if non-prime and happy
    elif prime(num) == False and happy(num) == False:                              # determine if num is non-prime and sad
        print('The number entered is sad non-prime.')                              # print result if non-prime and sad

def main():
    'Takes input from user, determines if happy/sad prime or happy/sad non-prime, and prints result'
    while True:                                                                      # enter while loop
        num = greeting()                                                             # greet user and obtain user input
        print_stmt(num)                                                              # print result
        response = input('Would you like to evaluate another number (yes/no): ')     # request user input
        if response == 'no':                                                         # determine if user wants to evaluate another number
            break                                                                    # break if user does not
        
        
        
