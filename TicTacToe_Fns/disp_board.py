#
# Display the board
#
def disp_board(x, n, sym):
    if( len(x) == 1):
        a = x[0][0]
        b = x[0][1]
        c = x[0][2]
        x = [a, b, c]
        print("\t\t\t\tPlayer{:2} ({:1})       :{:>2} {:>2} {:>2}".format(n, sym, " 1", " 2", " 3"))
    k = 1
    for i in x :
        print("\t\t\t\tRow{:1}               :{:>2} {:>2} {:>2}".format(k,i[0],i[1],i[2]))
        k += 1
    print("\n")
    return()
#