# Jonathan Lynch
# 4/13/20
# https://youtu.be/udyvWEq1y9w
# "I have not given or received any unauthorized assistance on this assignment."

import os
print(os.getcwd())


def magic(content, stem):
    'Create an iteration for the last digit, if all numbers excluding the last digit equal the stem.'
    # create empty string
    leaf = ''
    for num in content:                                                     # iterate through content list
        # determine if all digits excluding the last equal input variable stem
        if num[:-1] == stem:
            # add to empty string if they do
            leaf += num[-1] + ' '
    # return string (leaf)
    return leaf


def greeting():
    'Print a greeting for the user, and request user input.'
    # print greeting
    print("Hello, let's make a stem and leaf plot!")
    # request user input
    num = input('Enter a number 1, 2, or 3: ')
    # convert user input into an integer
    num = int(num)
    # return integer
    return num


def file_open(num):
    'Open and read a text file into a list, based on user input received in greeting function.'
    one = '/Users/jonathanlynch/Desktop/CSC_430/StemAndLeaf1.txt'
    two = 'StemAndLeaf2.txt'
    three = 'StemAndLeaf3.txt'
    if num == 1:
        # open file, if user input 1
        file = open(one)
        # read file into a list, if user input 1
        content = file.readlines()
        file.close()
    elif num == 2:
        # open file, if user input 2
        file = open(two)
        # read file into a list, if user input 2
        content = file.readlines()
        file.close()
    else:
        # open file, if user input 3
        file = open(three)
        # read file into a list, if user input 3
        content = file.readlines()
        file.close()
    # remove '\n' marks from list
    content = [strip.rstrip() for strip in content]
    # return list
    return content


def stem_list(content):
    'Convert list obtained from file_open function into stems.'
    # create empty temp list
    temp1 = []
    # create empty temp list
    temp2 = []
    # create final list to hold stems
    stems = []
    for item in content:
        # add every character of each list item except last one to temp1 list
        temp1.append(item[:-1])
    # convert list to a set in order to remove duplicates, then back to a list again
    set_list = list(set(temp1))
    for string in set_list:
        # convert all items in list to integers, then add to empty temp2 list
        temp2.append(int(string))
    # sort list  temp2
    temp2.sort()
    for num in temp2:
        # convert list items back to strings and add to list stems
        stems.append(str(num))
    # return list stems
    return stems


def leaves(stems, content):
    'Create the leaves for each of the stems.'
    for stem in stems:
        # iterate through stem list (print stem, and corresponding leaves with magic)
        print(stem + ' | ' + magic(content, stem))


def main():
    while True:                                                             # enter while loop
        # greet user and obtain user input
        number = greeting()
        # open correct file based on user input, clean, and return in list format
        content = file_open(number)
        # create list of stems from content list
        stems = stem_list(content)
        # print stem and leaves
        leaves(stems, content)
        # determine if user wants to make another plot
        replay = input(
            'Would you like to make another stem and leaf plot (yes/no)? ')
        if replay == 'no':
            # exit while loop (if user does not want to make another)
            break


main()
