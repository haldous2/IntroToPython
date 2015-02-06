
## Calculate prime numbers using the sieve of eratosthenes

def go_sieve(n):

    l = [x for x in range(2, n + 1)]
    #l = set([x for x in range(2, n + 1)])

    print l

    #while True:

    for x in l:

        # find multiples in list
        for y in range(x, n + 1, x):
            # don't remove search
            if y != x:
                #print "%i remove: %i" % (x,y)
                if y in l:
                    l.remove(y)

        # halfway, get out
        if x + x > n:
            break

    print l


if __name__ == "__main__":

    go_sieve(10)