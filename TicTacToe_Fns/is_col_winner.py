#
#   Check if the player is a Column Winner
#
def is_col_winner(board, look_for):
#    print(f"\tboard[0]: {board[0]}\tLength of board: {len(board)}")
    if len(board) == 1:
        a = board[0][0]
        b = board[0][1]
        c = board[0][2]
        board = [a, b, c]
#    print(f"\tNow Length of board: {len(board)}")
#    print(f"\tboard[0][0]: {board[0][0]}\tboard[1][0]: {board[1][0]}\tboard[2][0]: {board[2][0]}")
#
    win_flg = True
    pos = 0
#
#   Set up the 1st column
#
    this_col = [board[0][0], board[1][0], board[2][0]]
#    print(f"\tthis_col: {this_col}")
    for c in this_col:
        if(look_for != c):
            break # --> next column
        else:
            pos += 1
            continue
    if(pos == 3):
        return(win_flg)
#
#   Set up the 2nd column
#
    this_col = [board[0][1], board[1][1], board[2][1]]
#    print(f"\tthis_col: {this_col}")
    pos = 0
    for c in this_col:
        if(look_for != c):
            break # --> next column
        else:
            pos += 1
            continue
    if(pos == 3):
        return(win_flg)
#
#   Set up the 3nd column
#
    this_col = [board[0][2], board[1][2], board[2][2]]
#    print(f"\tthis_col: {this_col}")
    pos = 0
    for c in this_col:
        if(look_for != c):
            break # --> next column
        else:
            pos += 1
            continue
    if(pos == 3):
        return(win_flg)
    else:
        return(False)
#