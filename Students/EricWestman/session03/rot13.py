
import codecs
import string

def rot13(pStr):

    # define translation string
    rot13 = string.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

    #return string.translate(pStr, rot13)

    # use built in string decoder
    return str(pStr).decode('rot13')

if __name__ == "__main__":
    print rot13("Zntargvp sebz bhgfvqr arne pbeare")