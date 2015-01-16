

def grid_gen(edge, rows, cols):

    max_rows = 1
    max_cols = 1

    # edge - defined as how many pixels wide, tall
    #        edge must be defined as > 2
    #        else return +'s
    # rows - defined as how many rows across
    #        default 1
    # cols - defined as how many cols down
    #        default 1

    #        +-----+ x 1 -> 6/6 --> 6/1=6-1=5
    #        +--+--+ x 2 -> 6/3 --> 6/2=3-1=2
    #        +-+-+-+ x 3 -> 6/2 --> 6/3=2-1=1 ... ((edge - 1) / max_rows) - 1

    if (edge == 1):
        print "+"
        return
    elif (edge == 2):
        print "++\n","++"
        return
    else:

        # max rows
        for x in xrange(2, edge):
            if ((edge - 1) % x == 0):
                max_edge = (edge - 1) / x
                if (rows >= max_edge):
                    max_rows = max_edge
                    break

        # max cols
        for x in xrange(2, edge):
            if ((edge - 1) % x == 0):
                max_edge = (edge - 1) / x
                if (cols >= max_edge):
                    max_cols = max_edge
                    break


    print "grid size",edge,"rows",rows,"max_rows",max_rows,"cols",cols,"max_cols",max_cols

    # number of dashes - (((edge - 1) / max_rows) - 1)
    #                    (((7 - 1) / 3) - 1) = 1

    inc_row = (((edge - 1) / max_rows) - 1)
    inc_col = (((edge - 1) / max_cols) - 1)

    prow = ("+" + ("-" * inc_row)) * max_rows + "+\n"
    pcol = ("+" + (" " * inc_row)) * max_rows + "+\n"

    print ((prow + (pcol * inc_col)) * max_cols) + prow


grid_gen(1,1,1);
grid_gen(2,1,1);
grid_gen(7,4,4);
grid_gen(7,3,3);
grid_gen(7,2,2);
grid_gen(8,4,3);
grid_gen(9,4,3);
