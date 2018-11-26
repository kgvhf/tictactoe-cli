def print_board(board, max_width):
    for row in range(len(board)):
        for col in range(len(board)):
            print("{:>{}}".format(board[row][col], max_width), end='')
        print()


def win_check(board, player, n, row, col):
    horizontal, vertical, diagonal_down, diagonal_up = True, True, True, True
    # Check for horizontal win
    for i in range(n):
        if board[row][i] != player:
            horizontal = False

    # Check for vertical win
    for i in range(n):
        if board[i][col] != player:
            vertical = False

    # check for downwards diagonal (i.e. top left to bottom right)
    for i in range(n):
        if board[i][i] != player:
            diagonal_down = False

    # Check for upwards diagonal (i.e. bottom left to top right)
    for i in range(n):
        if board[i][n - 1 - i] != player:
            diagonal_up = False

    return horizontal or vertical or diagonal_down or diagonal_up


def vs_ai(board, n, possible_moves):
    max_width = len(str(n ** 2)) + 1
    while True:
        print_board(board, max_width)
        num = int(input("Player - Input location: "))
        if num < 0 or num >= (n ** 2):
            print("Please choose a valid location!")
            continue

        row = num // n
        col = num % n
        if board[row][col] == 'O' or board[row][col] == 'X':
            print("Cannot replace a player's piece!")
            continue

        board[row][col] = 'O'
        possible_moves.remove(num)

        if not possible_moves:
            print_board(board, max_width)
            print("Draw! Board is full.")
            break

        if win_check(board, 'O', n, row, col):
            print_board(board, max_width)
            print("Player " + player + " wins!")
            break

        # To be added: bot moves


def vs_player(board, n, possible_moves):
    max_width = len(str(n ** 2)) + 1
    player = 'O'
    while True:
        print_board(board, max_width)
        num = int(input("Player " + player + " - Input location: "))
        if num < 0 or num >= (n**2):
            print("Please choose a valid location!")
            continue

        row = num // n
        col = num % n
        if board[row][col] == 'O' or board[row][col] == 'X':
            print("Cannot replace a player's piece!")
            continue

        board[row][col] = player
        possible_moves.remove(num)

        if not possible_moves:
            print_board(board, max_width)
            print("Draw! Board is full.")
            break

        if win_check(board, player, n, row, col):
            print_board(board, max_width)
            print("Player " + player + " wins!")
            break

        if player == 'O':
            player = 'X'
        else:
            player = 'O'


def main():
    while True:
        n = int(input("Input size of tic-tac-toe board: "))
        if n > 1:
            break
        else:
            print("Board cannot be smaller than size 2!")

    board = []
    possible_moves = []
    for i in range(n):
        new_row = []
        for j in range(n):
            new_row.append(i * n + j)
            possible_moves.append(i * n + j)
        board.append(new_row)

    print("Play with bot or another player?")
    play_type = int(input("Enter 1 for bot, 2 for multi-player: "))

    if play_type == 1:
        print("Sorry! Bot is not ready yet!")
    elif play_type == 2:
        vs_player(board, n, possible_moves)
    else:
        print("Invalid option! Game exiting...")


main()
