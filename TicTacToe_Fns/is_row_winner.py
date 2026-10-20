#
# Chapter 4 Project --> Tic-Tac-Toe Game
# Check if the player is a row winner
#
def check_row(r, look_for):
#    print(f"\n\tLength of r: {len(r)}")
#   print(f"\tEntered check_row: {r} looking for: {look_for}")
    k = 0
    for i in r :
        if(i == look_for) :
            k += 1
        else:
            return(False)
    if k == 3: 
        return(True)
#    
#   .............................................................
#
def is_row_winner( x, plyr_symbol) :
#    from . import disp_board
#    row_len = len(x[0])  # Note: lengths of x[0] = x[1] = x[2] = 3
    look_for = plyr_symbol
#    print(f"\tx: {x}\tLength of x: {len(x)}")
#
    if(len(x) == 1):
#
#      Strip x of the outer wrapper and restore it
# 
        a = x[0][0]
        b = x[0][1]
        c = x[0][2]
        x = [a, b, c]
#        print(f"\tx: {x}\tLength of x: {len(x)}")
#    
#    disp_board(x)
#    print(f"\tlook_for: {look_for}")
#
#   Check 3 rows for a winner one row at a time.
#
    win_flg = check_row(x[0], look_for)
    if( win_flg ):
        return( win_flg)
    else:
        win_flg = check_row(x[1], look_for)
        if( win_flg ):
            return( win_flg)
        else:
            win_flg = check_row(x[2], look_for)
            if( win_flg ):
                return( win_flg)
            else:
                return(False)   # Player is not a row winner
#     