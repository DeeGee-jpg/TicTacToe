#
# Tic-Tac-Toe Game
#
# The tic-tac-toe board
# Define 3 Rows
#
row1 = ['', '', '' ]
row2 = ['', '', '' ]
row3 = ['', '', '' ]
#
board = [row1, row2, row3]
#
# Define 3 Columns
#
# col1 = [ board[0][0], board[1][0], board[2][0] ]
# col2 = [ board[0][1], board[1][1], board[2][1] ]
# col3 = [ board[0][2], board[1][2], board[2][2] ]
#
# board_cols = [ col1, col2, col3 ]
#
# Define 2 Diagonals
#
# diag1 = [row1[0], row2[1], row3[2]]
# diag2 = [row1[2], row2[1], row3[0]]
#
# ................................................
#
# The imports
#
import random
from TicTacToe_Fns.is_row_winner import is_row_winner
from TicTacToe_Fns.is_col_winner import is_col_winner
from TicTacToe_Fns.is_diag_winner import is_diag_winner
from TicTacToe_Fns.is_draw import is_draw
from TicTacToe_Fns.declare_winner import declare_winner
from TicTacToe_Fns.player import player
from TicTacToe_Fns.disp_board import disp_board
#
# ................................................
#
# ..... TOSS HERE ..... To see who goes first and assign symbols.
#                       The toss is done only once during the game.
#
plyr1 = plyr2 = False
plyr1_symbol = plyr2_symbol = 'O'
plyr1_moves = plyr2_moves = 0
win_flag = draw_flag = False
avail_slots = 9
R = "Row"
C = "Column"
D = "Diagonal"
#
rnd = 1 + int(random.random() + 0.5) # rnd no. either 1 or 2
# print(f"\n\tRandom Toss: {rnd}")
#
if(rnd == 1): # Player1 won the toss
    plyr1 = True
    print(f"\tPlayer1 has won the toss plyr1: {plyr1}\n")
    plyr1_symbol = 'X'
else: # Player2 won the toss
    plyr2 = True
    print(f"\tPlayer2 has won the toss plyr2: {plyr2}\n")
    plyr2_symbol = 'X'
#
# ..... GAME STARTS HERE .....
#
while (not win_flag and not draw_flag and avail_slots > 0) :
    if(plyr1):  # Player1 has won the toss.
        board = player(board, plyr1_symbol)    # Player1 plays
        plyr1_moves += 1
        avail_slots -= 1
        disp_board(board, 1, plyr1_symbol)
        plyr1 = False
        plyr2 = True
#
#       Check if Player1 is a row, column or diagonal winner
#       Do this only if the player has made atleast 3 moves
#
        if( plyr1_moves >= 3 ) :
            win_flag = is_row_winner(board, plyr1_symbol)
            if( win_flag ):
                declare_winner( 1, R, '' )
            else:
#                print("\tPlayer1, not a row winner")
                win_flag = is_col_winner(board, plyr1_symbol)
                if( win_flag ):
                    declare_winner( 1, C, '' )
                else:
#                    print("\tPlayer1, not a column winner")
                    win_flag = is_diag_winner(board, plyr1_symbol, 'LR')
                    if( win_flag ):
                        declare_winner( 1, D, 'LR' )
                    else:
                        win_flag = is_diag_winner(board, plyr1_symbol,'RL')
                        if( win_flag ):
                            declare_winner( 1, D, 'RL' )
#            disp_board(board, 1, plyr1_symbol)
#               
    else:
        
        board = player(board, plyr2_symbol)
        plyr2_moves += 1
        avail_slots -= 1
        disp_board(board, 2, plyr2_symbol)
        plyr1 = True
        plyr2 = False
#        print("\tReturned from Player()")
#
#       Check if Player2 is a row, column or diagonal winner
#       Do this only if the player has made atleast 3 moves
#
        if( plyr2_moves >= 3 ) :
            win_flag = is_row_winner(board, plyr2_symbol)
            if( win_flag ):
                declare_winner( 2, R, '' )
            else:
#                print("\tPlayer2, not a row winner")
                win_flag = is_col_winner(board, plyr2_symbol)
                if( win_flag ):
                    declare_winner( 2, C, '' )
                else :
#                    print("\tPlayer2, not a column winner")
                    win_flag = is_diag_winner(board, plyr2_symbol,'LR')
#                    print(f"win_flag: {win_flag}")
                    if( win_flag ):
                        declare_winner( 2, D, 'LR' )
                    else:
                        win_flag = is_diag_winner(board, plyr2_symbol,'RL')
#                        print(f"win_flag: {win_flag}")
                        if( win_flag ):
                            declare_winner( 2, D, 'RL' )
#            disp_board(board, 2, plyr2_symbol)
#
# .............................................................
#
if win_flag == False :
    if( is_draw(board) ) :
            print(f"\n\tGame is a DRAW !!")
            disp_board(board, '', '')
            draw_flag = True
    print("\n")
#