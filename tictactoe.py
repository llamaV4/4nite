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