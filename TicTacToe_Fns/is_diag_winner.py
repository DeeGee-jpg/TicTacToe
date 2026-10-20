#
# Check if the player is a diagonal winner
# 
# Check 2 Diagonals
# 
# 1st Diagonal --> Top Left  to Bottom Right
# 2nd Diagonal --> Top Right to Bpttom Left
#
def is_diag_winner(x, look_for, direction) :
#    print("\n\tDiagonal 1 --> Top Left to Bottom Right (LR)")
#    print("\tDiagonal 2 --> Top Right to Bottom Left (RL)")
#    print("\tFor Debugging: Entered is_diag_winner")
#    print(f"\tx: {x}")
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
#     print(f"\tx: {x}\tLength of x: {len(x)}")
#
    if(direction == 'LR'):
        d = [x[0][0], x[1][1], x[2][2]]
#        print(f"\n\tChecking LR Diagonal:\t{d}")
    else:
        d = [x[0][2], x[1][1], x[2][0]]
#        print(f"\n\tChecking RL Diagonal:\t{d}")
#
#    print(f"\tlook_for: {look_for}")
#
    for i in d:
#        print(f"\ti: {i}")
        if(look_for == i) :
            continue
        else:
            return(False)
    return(True)
#