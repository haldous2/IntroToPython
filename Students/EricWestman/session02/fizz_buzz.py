for x in xrange(1, 101):

    if (not x % 3 and not x % 5):
        print x, "FizzBuzz 3&5"
    elif (not x % 3):
        print x, "Fizz 3"
    elif (not x % 5):
        print x, "Buzz 5"
    else:
        print x
