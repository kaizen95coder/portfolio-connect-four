""" Represent a game of Connect Four as a data structure. You should be able to edit the data structure directly to add pieces to the board.

A traditional Connect Four board is 7 columns and 6 rows, but feel free to make your board as big as you like! """

# Create the board
def print_board():
    board = [['|' for i in range(8)] for j in range(6)]
    print(' 1 2 3 4 5 6 7')
    print(' ' * 7)
    for row in range(6):
        print(' '.join(board[row]) + '\n' + ' -' * 7)

print_board()
