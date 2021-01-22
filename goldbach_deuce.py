# Jonathan Lynch
# 4/25/20
# https://youtu.be/zT5zf7vBSrM
# "I have not given or received any unauthorized assistance on this assignment."


def integers_list():
    'Prompts user for input; uses input number to create a list of random integers'
    import random                                                                       # import random module from Python library                                                                         
    i = input('Enter a number to determine the size of a list: ')                       # prompt user to enter a number
    num = int(i)                                                                        # convert from string to integer
    lst = [random.randrange(1, 101) for x in range(num)]                                # create a list of random integers 1-100; length of list is equal to user input 
    return lst                                                                          # return the list

def number():
    'Prompts user to enter a number'
    print("Let's see if two numbers in the generated list sum to a chosen number.")     # print statement for user to read
    n = input('Choose a number: ')                                                      # prompt user to enter a number
    num = int(n)                                                                        # convert from string to integer
    return num                                                                          # return number

def findSums(x, nums):
    'Uses binary search to determine if two numbers in list sum to a given number'
    nums.sort()                                                                         # sort the list
    for i in nums:                                                                      # iterate through list of integers
        low = 0                                                                         # set low index
        high = len(nums) - 1                                                            # set high index
        while low <= high:                                                              # enter while loop if low is less than or equal to high
            mid = (low + high)//2                                                       # determine mid index by taking average of low and high
            pick = nums[mid]                                                            # pick integer from list at index mid
            if i + pick == x:                                                           # determine if sum of pick and current iteration value equals number
                return i, pick                                                          # return current iteration value and pick if sum equals number
            elif i + pick < x:                                                          # determine if current iteration value and pick sum is less than number
                low = mid + 1                                                           # reset low index to one greater than mid if above sum less than number
            else:
                high = mid - 1                                                          # reset high index to one less than mid if sum greater than number
    -1

def main():
    'Main function: given user input, generates a list, and determines if two numbers sum to a chosen number'
    nums = integers_list()                                                              # set value returned by integers_list() to nums
    x = number()                                                                        # set value returned by number() to x
    res = findSums(x, nums)                                                             # set values returned by findSums() to res
    if res == None:                                                                     # determine if value(s) equal None
        print('No numbers in the list summed to chosen number.')                        # if value of res equals None, print statement
    else:
        print('Two numbers in the list that sum to {} are {}.'.format(x, res))          # otherwise, print statement that includes values of res
    
