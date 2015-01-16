## NameError, TypeError, SyntaxError, AttributeError

def NameError():
    try:
        print (a)
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to be printed directly
        print "\n"

def TypeError():
    try:
        print 5 + "text"
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to be printed directly
        print "\n"

## Note: program will not run with a syntax error - the following crashes the whole enchilada
def SyntaxError():
    try:
        bleep bleep bleep
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to be printed directly
        print "\n"

def AttributeError():
    try:
        print "The answer is..." + str.isnumeric()
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to be printed directly
        print "\n"

NameError();
TypeError();
SyntaxError();
AttributeError();
