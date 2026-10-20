#
def player(x, sym) :
    import random
    done = False
    random.seed()
#
    if(len(x) == 1):
#
#      Strip x of the outer wrapper and restore it
# 
        a = x[0][0]
        b = x[0][1]
        c = x[0][2]
        x = [a, b, c]
#
    while( not done ):
        i = 0 + int( 2* random.random() + 0.5) # rnd no. between 0 and 2
        j = 0 + int( 2* random.random() + 0.5) # rnd no. between 0 and 2
#
        if(x[i][j] == ''):
            x[i][j] = sym
            done = True
    return[x]
#