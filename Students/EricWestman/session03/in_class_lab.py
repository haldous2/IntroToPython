
def reverse_ends(str):

    """
        return a string with the first and last characters exchanged.

        using slices: here so there are not integer or out of range errors
    """

    outStr = ""
    outStr = str[-1:]
    outStr += "'"

    outStr += str[1:-1]
    outStr += "'"

    outStr += str[0:1]

    return outStr

print "reverse ends", reverse_ends("abcdefg")

def remove_ever_other(str):

    """
        return a string with every other character removed

    """

    return str[::2]

print "remove ever other", remove_ever_other("abcdefg")

def remove_every_other_strip_four(str):

    """
        return a string with the first and last 4 characters removed, and every other char in between
    """
    return str[3,-4]