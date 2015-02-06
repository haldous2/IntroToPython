
## Slicing lab

"""
Define a function called 'centered_average' which returns the average of all the integers in a list
except for the minimum and maximum values. Don't worry about duplicate max / min values.
"""

my_list = [1,8,7,4,99,33,4,57,12,90,32,1,9,77,101,2,6]
#my_list = [1, 3, 5, 1, 100, 7]

def centered_average():

    new_list = my_list[:]
    new_list.sort()
    avg_list = new_list[1:-1]

    print my_list
    print new_list
    print avg_list

    # Average out all but max and min
    avg_tot = sum(avg_list) / float(len(avg_list))

    print avg_tot

def second_lowest_highest():

    new_list = my_list[:]
    new_list.sort()
    avg_list = new_list[1:-1]

    print my_list
    print new_list
    print avg_list

    avg_tot = (max(avg_list) + min(avg_list)) / 2

    print avg_tot

if __name__ == "__main__":

    #centered_average()
    second_lowest_highest()