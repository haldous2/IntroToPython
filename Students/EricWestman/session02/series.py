def fibonacci(n):

    """Return value of nth position in Fibonacci series via recursion"""

    # nth   0, 1, 2, 3, 4, 5, 6, 07, 08...
    # val   0, 1, 1, 2, 3, 5, 8, 13, 21...

    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)

    return n

def fibonacci_gen(n):

    """Return list of Fibonacci values up to nth position via generator"""

    # Returns generator iteration which is a list (like an array)
    # So, n = 5 returns [0,1,1,2,3,5]

    a, b = 0, 1
    for y in xrange(n + 1):
        yield a
        a, b = b, a + b

def lucas(n):

    """Return value of nth position in Lucas series via recursion"""

    # nth   0, 1, 2, 3, 4, 05, 06, 07, 08...
    # val   2, 1, 3, 4, 7, 11, 18, 29, 47...

    if (n == 0):
        return 2
    if (n == 1):
        return 1
    if (n > 1):
        return lucas(n - 1) + lucas(n - 2)

    return n


def lucas_gen(n):

    """Return list of Lucas values up to nth position via generator"""

    a, b = 2, 1
    for y in xrange(n + 1):
        yield a
        a, b = b, a + b

def sum_series(n = 0, v1 = 0, v2 = 1):

    """Call sequence generator and print the nth value"""

    print list(sum_series_gen(n, v1, v2))[n]

def sum_series_gen(n = 0, v1 = 0, v2 = 1):

    """Generate sequence of n values starting with v1 and v2 in the sequence"""

    a, b = v1, v2
    for _ in xrange(n + 1):
        yield a
        a, b = b, a + b

if __name__ == "__main__":

    #print fibonacci(0)
    #print fibonacci(1)
    #print fibonacci(2)
    #print fibonacci(5)
    #print fibonacci(6)
    #print list(fibonacci_gen(6))[6]
    #print fibonacci(7)

    #print "lucas:", lucas(6)
    #print "lucas_gen:", list(lucas_gen(6))[6]

    assert(list(lucas_gen(6))[6] == 18),"That is not the right answer!"

    sum_series(6)
    sum_series(6,0,1)
    sum_series(6,2,1)
    sum_series(6,10,6)
    sum_series(100)
