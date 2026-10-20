#
# Checks if the board is full --> in which case it is a draw
#
def is_draw(x) :
#
    j = 0
    for i in x :
            if(i[j] == ""):
                return(False)
            else:
                j += 1
                if(j == 3):
                    j = 0
            continue
    return(True)
#