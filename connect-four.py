""" Represent a game of Connect Four as a data structure. You should be able to edit the data structure directly to add pieces to the board.

A traditional Connect Four board is 7 columns and 6 rows, but feel free to make your board as big as you like! """

# Create the board


def print_board():
    board = [['.' for i in range(7)] for j in range(6)]
    print('1 2 3 4 5 6 7')
    for row in range(6):
        print(' '.join(board[row]))

# Add a piece to the board


def add_piece(board, col, piece):
    for row in range(5, -1, -1):
        if board[row][col] == '.':
            board[row][col] = piece
            break
        elif row == 0:
            print('That column is full!')
        elif board[row][col] == piece:
            print('That piece is already there!')
            break
        else:
            print('Something went wrong!')

# Check if the game is over


def is_game_over(board):
    for row in range(6):
        for col in range(7):
            if board[row][col] == '.':
                continue
            if col <= 3 and board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3]:
                return True
            if row <= 2 and board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col]:
                return True
            if row <= 2 and col <= 3 and board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]:
                return True
            if row <= 2 and col >= 3 and board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2] == board[row + 3][col - 3]:
                return True
    for row in range(6):
        for col in range(7):
            if board[row][col] == '.':
                return False
    return True

# Play the game


def connect_four_game():
    board = [['.' for i in range(7)] for j in range(6)]
    print('1 2 3 4 5 6 7')
    for row in range(6):
        print(' '.join(board[row]))
    player = 1
    while not is_game_over(board):
        if player == 1:
            piece = 'X'
        else:
            piece = 'O'
        col = int(input(f'Player {player}, enter a column (1-7): ')) - 1
        add_piece(board, col, piece)
        print_board()
        if is_game_over(board):
            break
        player = 3 - player
    print_board()
    if is_game_over(board) == 'tie':
        print("It's a tie!")
    else:
        print(f"Player {3 - player} wins!")

connect_four_game()
