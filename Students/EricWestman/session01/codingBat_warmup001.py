def sleep_in(weekday, vacation):
    if (weekday is False or vacation is True):
        return True
    else:
        return False


def monkey_trouble(a_smile, b_smile):
    if (a_smile is True and b_smile is True):
        return True
    elif (a_smile is False and b_smile is False):
        return True
    else:
        return False


def sum_double(a, b):
    if (a is b):
        return (a + b) * 2
    else:
        return a + b


def diff21(n):
    outval = abs(n - 21)
    if (n > 21):
        return outval * 2
    else:
        return outval


def parrot_trouble(talking, hour):
    if (talking is True):
        if (hour < 7 or hour > 20):
            # We are in trouble!
            return True
        else:
            # Normal hours
            return False
    else:
        # Not talking, we are good
        return False


def makes10(a, b):
    if (a + b) == 10 or a == 10 or b == 10:
        return True
    else:
        return False


def near_hundred(n):
    if ((abs(n) >= 90 and abs(n) <= 110) or (abs(n) >= 190 and abs(n) <= 210)):
        return True
    else:
        return False


def pos_neg(a, b, negative):
    if (negative is True):
        if (a < 0 and b < 0):
            # in Negative, both negative
            return True
        else:
            return False
    else:
        if ((a < 0 and b >= 0) or (a >= 0 and b < 0)):
            # not in Negative - one is + other is -
            return True
        else:
            return False


def not_string(str):
    if (str[:3] == 'not'):
        return str
    else:
        return 'not ' + str


def missing_char(str, n):
    outstr = ''
    if (str):
        outstr = str[0:n]
        outstr = outstr + str[n+1:len(str)]
    return outstr


def front_back(str):
    outstr = ''
    if (str):
        if (len(str) == 1):
            outstr = str
        elif (len(str) == 2):
            outstr = str[1:2] + str[0:1]
        else:
            outstr = str[len(str) - 1:len(str)]  + str[1:len(str) - 1] + str[0:1]

    return outstr


def front3(str):
    cbncpy = ''
    if (str):
        if (len(str) <= 3):
            cbncpy = str
        else:
            cbncpy = str[0:3]
    return cbncpy * 3


def string_times(str, n):
    return str * n


def string_bits(str):
   outstr = ''
   for i in range(len(str)):
       # every other e.g. 0,3,5 or (i * 2):(i * 2) + 1
       outstr = outstr + str[(i*2):((i*2)+1)]
   return outstr


def string_splosion(str):
   outstr = ''
   for i in range(len(str)):
       # concat i numbr of characters and return
       outstr = outstr + str[0:i + 1]
   return outstr
