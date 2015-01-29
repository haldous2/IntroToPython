
def string_number(n):

    """
        Rewrite: the first 3 numbers are: %i, %i, %i"%(1,2,3)
        for an arbitrary number of numbers...
        using: % encoding
    """

    sStr = ""
    fStr = ()

    for x in xrange(1, n + 1):

        if sStr:
            sStr += ",%i"
        else:
            sStr = "%i"

        fStr += (x,)

    print "The first %i numbers are: " % (n) + sStr%(fStr)

def string_number_format(n):

    """
        Rewrite: the first 3 numbers are: %i, %i, %i"%(1,2,3)
        for an arbitrary number of numbers...
        using: format
    """

    sStr = ""
    fStr = ""

    for x in xrange(1, n + 1):

        if sStr:
            sStr += ",{}"
        else:
            sStr = "{}"

        # .format won't work with tuples for some reason
        # ask teacher why ?
        #fStr += (x,)

        if fStr:
            fStr += ",{}".format(x)
        else:
            fStr = "{}".format(x)

    print "sStr:" + sStr
    print "fStr:" + fStr

    #tUpl = (1,2,3)

    # Arghhhhhh! - this is going to drive me crazy!
    #print "{},{},{}".format(tUpl)

    # This works, however - it's not a tuple
    #print "{},{},{}".format(1,2,3)

    # Found this online - joining, looping and piecing together strings
    fStr = ', '.join('{}'.format(i) for i in xrange(1, n + 1))

    print "The first {} numbers are: ".format(n) + fStr


def string_encode():

    """
        Write a format string that will take:

        ( 2, 123.4567, 10000)

        and produce:

        'file_002 :   123.46, 1e+04'

        using: % encoding
    """

    sStr = "file_%03d : %.2f, %.0e" % (2, 123.4567, 10000)

    print sStr

def string_encode_format():

    """
        Write a format string that will take:

        ( 2, 123.4567, 10000)

        and produce:

        'file_002 :   123.46, 1e+04'

        using: format
    """

    sStr = "file_{:03d} : {:.2f}, {:.0e}" .format(2, 123.4567, 10000)

    print sStr

if __name__ == "__main__":
    #string_number(10)
    string_number_format(3)
    #string_encode()
    #string_encode_format()
