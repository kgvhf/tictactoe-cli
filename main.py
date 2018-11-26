def print_board(board, max_width):
    for row in range(len(board)):
        for col in range(len(board)):
            print("{:>{}}".format(board[row][col], max_width), end='')
        print()


n = int(input("Input size of tic-tac-toe board: "))
filled = 0
board = []
for i in range(n):
    new_row = []
    for j in range(n):
        new_row.append(i * n + j)
    board.append(new_row)
max_width = len(str(n ** 2)) + 1
print_board(board, max_width)

player = 'O'
while True:
    num = int(input("Player " + player + " - Input location: "))
    row = num // n
    col = num % n
    if board[row][col] == 'O' or board[row][col] == 'X':
        print("Cannot replace player's piece")
        continue

    board[row][col] = player
    filled += 1
    print_board(board, max_width)

    if filled == (n ** 2):
        print("Draw! Board is full.")
        break

    horizontal_win = True
    for i in range(n):
        if board[row][i] != player:
            horizontal_win = False

    vertical_win = True
    for i in range(n):
        if board[i][col] != player:
            vertical_win = False

    diagonal_down_win = True
    for i in range(n):
        if board[i][i] != player:
            diagonal_down_win = False

    diagonal_up_win = True
    for i in range(n):
        if board[i][n - 1 - i] != player:
            diagonal_up_win = False

    if horizontal_win or vertical_win or diagonal_down_win or diagonal_up_win:
        print("Player " + player + " wins")
        break

    if player == 'O':
        player = 'X'
    else:
        player = 'O'
