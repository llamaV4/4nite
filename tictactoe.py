board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

def print_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def player_move(player):
    while True:
        move = input(f"Player {player}, pick a spot (1-9): ")
        move = int(move) - 1
        if board[move] == " ":
            board[move] = player
            break
        else:
            print("That spot is taken! Try again.")

def check_winner(player):
    if board[0] == board[1] == board[2] == player: return True
    if board[3] == board[4] == board[5] == player: return True
    if board[6] == board[7] == board[8] == player: return True
    if board[0] == board[3] == board[6] == player: return True
    if board[1] == board[4] == board[7] == player: return True
    if board[2] == board[5] == board[8] == player: return True
    if board[0] == board[4] == board[8] == player: return True
    if board[2] == board[4] == board[6] == player: return True
    return False

def check_tie():
    return " " not in board
def play_game():
    current_player = "X"
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        player_move(current_player)
        print_board()

        if check_winner(current_player):
            print(f"Player {current_player} wins! 🎉")
            break

        if check_tie():
            print("It's a tie!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

play_game()