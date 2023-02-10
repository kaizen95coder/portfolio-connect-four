""" Represent a game of Connect Four as a data structure. You should be able to edit the data structure directly to add pieces to the board.

A traditional Connect Four board is 7 columns and 6 rows, but feel free to make your board as big as you like! """

# Create the board
def print_board():
    board = [['.' for i in range(7)] for j in range(6)]
    print('1 2 3 4 5 6 7')
    for row in range(6):
        print(' '.join(board[row]))

print_board()

# Add a piece to the board
def add_piece(board, col, piece):
    for row in range(5, -1, -1):
        if board[row][col] == '.':
            board[row][col] = piece
            break
        elif row == 0:
            print('That column is full!')
        elif board[row][col] != '.':
            continue
        elif board[row][col] == piece:
            print('That piece is already there!')
            break
        else:
            print('Something went wrong!')


