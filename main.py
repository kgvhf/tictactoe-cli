import random
from copy import deepcopy


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


def vs_bot(board, n, possible_moves, difficulty):
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

        if win_check(board, 'O', n, row, col):
            print_board(board, max_width)
            print("You win!")
            break

        if not possible_moves:
            print_board(board, max_width)
            print("Draw! Board is full.")
            break

        # Bot move begins here
        print("Bot is thinking...")
        bot_num = -1
        check = random.randint(0, 100)

        # Medium difficulty - 50% chance of bot being easy, 50% chance being abyssal
        if difficulty == 2:
            if check <= 50:
                difficulty = 0
            else:
                difficulty = 4
        # Hard difficulty - 20% chance of bot being easy, 80% chance being abyssal
        elif difficulty == 3:
            if check <= 20:
                difficulty = 0
            else:
                difficulty = 4

        print(possible_moves)
        # Easy difficulty - Bot selects a random move
        if difficulty == 1:
            bot_num = random.choice(possible_moves)
        # Abyssal difficulty - Bot utilizes minimax to find optimal move
        elif difficulty == 4:
            temp, bot_num = minimax(board, n, possible_moves, True)
            if bot_num == -1:
                print("Bot has forfeited! You won!")
                break

        row = bot_num // n
        col = bot_num % n
        board[row][col] = 'X'
        possible_moves.remove(bot_num)

        if win_check(board, 'X', n, row, col):
            print_board(board, max_width)
            print("You lost!")
            break

        if not possible_moves:
            print_board(board, max_width)
            print("Draw! Board is full.")
            break


# Returns winning player (O or X), or D if draw
def find_winner(board, n):
    for i in range(n):
        horizontal = True
        for j in range(0, n - 1):
            if board[i][j] == '.':
                break
            if board[i][j] != board[i][j + 1]:
                horizontal = False
        if horizontal:
            return board[i][0]

    for i in range(n):
        vertical = True
        for j in range(0, n - 1):
            if board[j][i] == '.':
                break
            if board[j][i] != board[j + 1][i]:
                vertical = False
        if vertical:
            return board[0][i]

    diagonal_down = True
    for i in range(0, n - 1):
        if board[i][i] == '.':
            break
        if board[i][i] != board[i + 1][i + 1]:
            diagonal_down = False
    if diagonal_down:
        return board[0][0]

    diagonal_up = True
    for i in range(0, n - 1):
        if board[i][n - 1 - i] == '.':
            break
        if board[i][n - 1 - i] != board[i + 1][n - 2 - i]:
            diagonal_up = False
    if diagonal_up:
        return board[0][n - 1]

    return 'D'


def minimax(board, n, possible_moves, maximizing_player):
    best_move = -1
    if not possible_moves:
        winner = find_winner(board, n)
        if winner == 'O':
            return -1, best_move
        elif winner == 'X':
            return 1, best_move
        else:
            return 0, best_move

    if maximizing_player:
        value = -10
        for move in possible_moves:
            new_board = deepcopy(board)
            new_possible = deepcopy(possible_moves)
            row = move // n
            col = move % n
            new_board[row][col] = 'X'
            new_possible.remove(move)
            new_value, new_move = minimax(new_board, n, new_possible, False)
            if new_value > value:
                value = new_value
                best_move = move

        return value, best_move

    else:
        value = 10
        for move in possible_moves:
            new_board = deepcopy(board)
            new_possible = deepcopy(possible_moves)
            row = move // n
            col = move % n
            new_board[row][col] = 'O'
            new_possible.remove(move)
            new_value, new_move = minimax(new_board, n, new_possible, True)
            if new_value < value:
                value = new_value
                best_move = move

        return value, best_move


def vs_player(board, n, possible_moves):
    max_width = len(str(n ** 2)) + 1
    player = 'O'
    while True:
        print_board(board, max_width)
        num = int(input("Player " + player + " - Input location: "))
        if num < 0 or num >= (n ** 2):
            print("Please choose a valid location!")
            continue

        row = num // n
        col = num % n
        if board[row][col] == 'O' or board[row][col] == 'X':
            print("Cannot replace a player's piece!")
            continue

        board[row][col] = player
        possible_moves.remove(num)
        
        if win_check(board, player, n, row, col):
            print_board(board, max_width)
            print("Player " + player + " wins!")
            break

        if not possible_moves:
            print_board(board, max_width)
            print("Draw! Board is full.")
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

    print("Select game mode:")
    while True:
        print("1 - Easy bot")
        print("2 - Medium bot")
        print("3 - Hard bot")
        print("4 - Abyssal bot (You're not expected to win!)")
        print("5 - Multiplayer")
        play_type = int(input("Your choice: "))

        if play_type == 1:
            vs_bot(board, n, possible_moves, 1)
            break
        elif play_type == 2:
            vs_bot(board, n, possible_moves, 2)
            break
        elif play_type == 3:
            vs_bot(board, n, possible_moves, 3)
            break
        elif play_type == 4:
            vs_bot(board, n, possible_moves, 4)
            break
        elif play_type == 5:
            vs_player(board, n, possible_moves)
            break
        else:
            print("Invalid option!")

    print("Game over! Press return to close...")
    input()


main()
