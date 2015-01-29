
fruits = ["Apples", "Pears", "Oranges", "Peaches"]

def fruity_list():

    print fruits

    # Add a new fruit
    new_fruit = raw_input("Add a fruit:")

    if (new_fruit):
        fruits.append(new_fruit)

    print fruits

    # Display fruit @ index
    idx_fruit = raw_input("Display fruit at index 1 to %d:" % len(fruits))

    if (idx_fruit.isdigit()):

        idx_fruit = int(idx_fruit)

        if (idx_fruit > 0 and idx_fruit <= len(fruits)):

            print "The fruit @ index %i is %s" % (int(idx_fruit), str(fruits[idx_fruit]))

        else:
            print "Invalid index"

    else:
        print "Invalid input"

    # Add another fruit to the list using + @ beginning of list
    even_more_fruits = ["Strawberry","Potato"]
    fruits = even_more_fruits + fruits

    print fruits

    # Add another fruit to the beginning of the list via .insert
    fruits.insert(0, "Asian Pear")

    print fruits

    # Loop through fruits and display fruits that start with 'P'
    for fruit in fruits:
        if (fruit[0:1] == "P"):
            print fruit

def fruity_list_part2():

    # Remove last fruit from list and display
    print fruits
    del fruits[len(fruits) - 1]
    print fruits

    del_fruit = False
    while (del_fruit == False):

        in_fruit = raw_input("Which fruit would you like to delete :")

        if (in_fruit in fruits):

            fruits.remove(in_fruit)
            #del fruits[fruits.index(in_fruit)]
            del_fruit = True

    print fruits

def fruity_list_part3():

    # Remove fruits from list by asking preference yes or no
    for in_fruit in fruits[:]:

        in_answer = ""
        while (in_answer != "Yes" and in_answer != "No"):

            in_answer = raw_input("Do you like %s ? Yes or No" % in_fruit)

            if (in_answer == "No"):

                fruits.remove(in_fruit)

    # At this point, print the local copy of fruits -
    # Trying to copy cpy_fruits back to fruits will result in an error with trying to make global fruits local and pre-assigning
    # Options would be to return cpy_fruits (list) and then updating the global fruits list
    print fruits

def fruity_list_part4():

    # Make a copy of the list and reverse the letters in each fruit in the copy.

    cpy_fruits = fruits[:]

    for in_fruit in cpy_fruits:

        rev_fruit = in_fruit[::-1]
        cpy_fruits[cpy_fruits.index(in_fruit)] = rev_fruit

    # Delete the last item of the original list. Display the original list and the copy.

    del fruits[len(fruits) - 1]

    print fruits
    print cpy_fruits


if __name__ == "__main__":
    #fruity_list()
    #fruity_list_part2()
    fruity_list_part3()
    #fruity_list_part4()