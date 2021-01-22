# stem & leaf practice:

def greet():
    'greet user & obtain a number 1-3'
    print("Hello user, let's make a stem and leaf plot.")
    num = input('Please enter a number 1-3: ')
    num = int(num)
    return num

def content(num):
    if num == 1:
        file = open('/Users/jonathanlynch/Desktop/CSC_430/StemAndLeaf1.txt')
        content = file.readlines()
        file.close()
    elif num == 2:
        file = open('StemAndLeaf2.txt')
        content = file.readlines()
        file.close()
    elif num == 3:
        file = open('StemAndLeaf3.txt')
        content = file.readlines()
        file.close()
    content = [string.rstrip() for string in content]
    return content


def stem(lst):
    temp1 = []
    temp2 = []
    stem_list = []
    for string in lst:
        temp1.append(string[:-1])
    set_list = list(set(temp1))
    for item in set_list:
        temp2.append(int(item))
    temp2.sort()
    for num in temp2:
        stem_list.append(str(num))
    return stem_list

def leaves(stems, lst, number):
    for stem in stems:
        if number == 1 or number == 2:
            if len(stem) == 1:
                print(' ' + stem + ' | ' + leaf(lst, stem))
            else:
                print(stem + ' | ' + leaf(lst, stem))
        else:
            if len(stem) == 2:
                print(' ' + stem + ' | ' + leaf(lst, stem))
            else:
                print(stem + ' | ' + leaf(lst, stem))
                

def leaf(lst, stem):
    leaf = ''
    for x in lst:
        if x[:-1] == stem:
            leaf += x[-1] + ' '
    return leaf



def main():
    while True:
        number = greet()
        lst = content(number)
        stems = stem(lst)
        leaves(stems, lst, number)
        play_again = input('Would you like to play again (yes/no): ')
        if play_again == 'no':
            break

main()

        
