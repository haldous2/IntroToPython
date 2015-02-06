
## Exception handling

# try, except (a.k.a. catch), raise (a.k.a throw), finally, else - and try, try again - finally

# Note: finally always runs. else only runs when exception not raised
# Note: probably should never use 'pass' to ignore exceptions and such

import __builtin__
import sys

def list_exceptions():
    exp = [name for name in dir(__builtin__) if "Error" in name]
    print exp

def safe_input(sAsk):

    try:
        inDta = raw_input("%s:" % sAsk)
        #return inDta

    except (KeyboardInterrupt, EOFError) as err:
        #print err
        #print err.args
        #quit(0)
        return None

    except:
        #e = sys.exc_info()[0]
        #print "Error %s" % e
        #quit(0)
        return None

    else:
        return inDta

def is_numeric(sAsk):

    # Make this thing throw an exception
    try:
        float(sAsk)
        return True
    except ValueError:
        return False

    # Easy way to test string for digits
    #if sAsk.isdigit():
    #    return True

def ask_number():

    if is_numeric(safe_input("Let's have an integer")):
        print "We have a number"
    else:
        print "Not a number"

if __name__ == "__main__":
    #list_exceptions()
    #safe_input("Let's have an integer")
    ask_number()