
def sFizzBuzz():

    for x in xrange(1, 101):

        if (not x % 3 and not x % 5):
            print x, "FizzBuzz 3&5"
        elif (not x % 3):
            print x, "Fizz 3"
        elif (not x % 5):
            print x, "Buzz 5"
        else:
            print x


def FizzBuzz(n, d = { 3 : "Fizz", 5 : "Buzz" }):

    for x in xrange(1, n + 1):

        o = ""

        # match all
        for i in d:

            # @ default i = 3,5
            # if remainder found
            if (not x % i):

                o += d[i]

        print "%i - %s" % (x, o)

if __name__ == "__main__":
    FizzBuzz(15)