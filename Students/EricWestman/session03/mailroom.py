
people = [{"name": "Grace Kelly", "donations": [200,101,300,150]},
            {"name": "Catherine Deneuve", "donations": [201,102,301,151]},
            {"name": "Audrey Hepburn", "donations": [203,103,302,152]},
            {"name": "Sharon Tate", "donations": [204,105,304,154]},
            {"name": "Veronica Lake", "donations": [205,106,305,155]}]
print people

#print people[0]["donations"][1]

def user_maintenance():

    """
    User maintenance program

    Send mail or print list of donors
    """

    pRI_option = raw_input("Type 1 to Send a Thank You note or 2 to Create a report")

    if pRI_option == "1":

        while True:

            # Who are you Thanking ?
            pRI_fullname = raw_input("Enter the full name of the donor")

            if pRI_fullname == "list":

                # List all users in current dict
                for person in people:

                    print person["name"]

            else:

                if not findPerson(pRI_fullname):

                    # No match, add user to list
                    addPerson(pRI_fullname)

                break

        # How much did they Donate ?
        while True:

            # Who are you Thanking ?
            pRI_donation = raw_input("How much did they donate?")

            if (isNumeric(pRI_donation)):

                donPerson(pRI_fullname, float(pRI_donation))

                break

            # Send a Thank You!


    if pRI_option == "2":
        print "it's 2!"


def findPerson(pPerson):

    """
    Find person in people list
    """

    foundPerson = False

    # Match input to list, if not found keep looping
    for person in people:

        if (str(person["name"]).lower() == str(pPerson).lower()):

            foundPerson = True
            break

    return foundPerson


def addPerson(pPerson):

    """
    Add person to people list
    """

    if pPerson:

        sPerson = "{\"name\":\"%s\", \"donations\":\"()\"}" % pPerson
        people.append(sPerson)


def donPerson(pPerson, pDonation=0):

    """
    Add donation to specified person in people
    """

    # Only update if donating
    if pDonation <= 0:

        return

    # Find the donator
    for index in range(len(people)):

        if (str(people[index]["name"]).lower() == str(pPerson).lower()):

            dIdx = index
            break

    # Update donation
    if dIdx:

        #people[dIdx]["donations"].append(pDonation)
        people[dIdx]["donations"].insert(0, pDonation)

def isNumeric(pNbr):

    if type(pNbr) == str:
        if pNbr.isdigit() == True:
            return True

    if type(pNbr) == int or type(pNbr) == float or type(pNbr) == long or type(pNbr) == complex:
         return True

    return False

if __name__ == "__main__":
    #isNumeric(.000001)
    #donPerson("Audrey Hepburn",999)
    user_maintenance()
    print people