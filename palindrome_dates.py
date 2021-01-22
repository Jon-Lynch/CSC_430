# Jonathan Lynch
# 5/10/20
# https://youtu.be/1Rey7oaoV2g
# "I have not given or received any unauthorized assistance on this assignment."

def testFeb(days_mo, years):
    'accepts list of days in Feb, and list of years, and returns list of palindrome dates' 
    Feb_palindromes = []                                           # create empty list
    for day in days_mo:                                            # iterate through list of days in Feb
        for year in years:                                         # iterate through list of years
            day_mo = day + '02'                                    # concatenate day and month strings
            year = str(year)                                       # convert year into string
            day_mo_year = day_mo + year                            # concatenate day_mo string and year string
            if day_mo_year == day_mo_year[::-1]:                   # determine if day_mo_year string is equivalent to day_mo_year string reversed
                palindrome = day + '/' + '02' + '/' + year         # if equivalent, create date string with appropriate slash marks
                Feb_palindromes.append(palindrome)                 # add to Feb_palindromes list
    return Feb_palindromes                                         # return list

def main():
    'determines palindrome dates and writes dates to an empty file'
    years = [i+1 for i in range(1999, 2100)]                           # create list of years in the 21st century
    days_Feb = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']  # list of days in Feb
    palindromes = testFeb(days_Feb, years)                             # determine palindrome dates
    palindromes_str = ''                                               # create empty string
    for date in palindromes:                                           # iterate through list of palindrome dates
        palindromes_str += date + ', '                                 # separate each date by a comma and add to palindromes_str
    outfile = open('file.txt', 'w')                                    # open text file in mode 'w'
    outfile.write(palindromes_str)                                     # write to file
    outfile.close()                                                    # close file

    
