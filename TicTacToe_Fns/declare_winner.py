#            
# ...................................................
#
def declare_winner(plyr, w, direction) :
    if(direction != ''):
        print(f"\n\tCONGRATULATIONS ! Player{plyr} is a {w} ({direction}) Winner\n")
    else:
        print(f"\n\tCONGRATULATIONS ! Player{plyr} is a {w} Winner\n")
    return(True)
#