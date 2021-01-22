# Jonathan Lynch
# 4/24/20
# https://youtu.be/FoYlFbQ7ZwY
# "I have not given or received any unauthorized assistance on this assignment."

def humanPyramid(r, c):
    'For row and column entered, returns the total weight on person in a human pyramid'
    if r == 0:                                                       # base case when row is zero
        return 0
    elif c == 0:                                                     # base case when column is zero (left side of pyramid)
        return (128 + humanPyramid(r-1, c))/2                        # recursive function for column zero
    elif c == r:
        return (128 + humanPyramid(r-1, c-1))/2                      # recursive function for right side of pyramid
    elif r == 2 and c == 1:
        return 2*humanPyramid(2,2)                                   # weight on person in the middle (second row)
    elif r == 3 and c == 1 or r == 3 and c == 2:
        return humanPyramid(3,0) + (humanPyramid(2,1) + 128)/2       # weight on people in the middle (third row)
    elif r == 4 and c == 1 or r == 4 and c == 3:
        return humanPyramid(4,0) + (humanPyramid(3,2) + 128)/2       # weight on people in bottom row, first and third columns 
    elif r == 4 and c == 2:
        return 2*((humanPyramid(3,2) + 128)/2)                       # weight on person in bottom row, middle

