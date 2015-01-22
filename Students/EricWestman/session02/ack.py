def ack(m,n):

    """
    Calculate Ackermann values.

    Input values for this must be non negative integers.

    Note: Ackerman 4,1 and above will throw a maximum recursion error
    """

    # Force upper recursion limit for stubborn answers - use at your own risk!
    #import sys
    #sys.setrecursionlimit(10000)

    if (m == 0):
        # Final answer is returned here
        return n+1

    if (m > 0 and n == 0):
        return ack(m-1, 1)

    if (m > 0 and n > 0):
        return ack(m-1, ack(m, n-1))

    return 0

def ack_test():

    if (ack(0,0) == 1 and
        ack(0,1) == 2 and
        ack(1,0) == 2 and
        ack(1,1) == 3 and
        ack(2,0) == 3 and
        ack(2,1) == 5 and
        ack(3,0) == 5 and
        ack(3,1) == 13 and
        ack(4,0) == 13):
        print "All Tests Pass"

# If this module is ran by itself and not included in another module
# it should run this function as it's main
if __name__ == "__main__":
    ack_test()
