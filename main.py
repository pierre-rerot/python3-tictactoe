import random

# Function to display the game board
def display_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print("\n-------------")

# Function to check if a player has won
def check_win(board, symbol):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == symbol:
            return True

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == symbol:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True

    return False

# Function for a player's turn
def player_turn(board, symbol):
    while True:
        move = input(f"Enter your move (row column): ")
        try:
            row, col = map(int, move.split())
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                board[row][col] = symbol
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

# Function for the computer's turn
def computer_turn(board, symbol):
    # Check for a winning move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = symbol
                if check_win(board, symbol):
                    return
                else:
                    board[i][j] = " "

    # Check for a blocking move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X" if symbol == "O" else "O"
                if check_win(board, "X" if symbol == "O" else "O"):
                    board[i][j] = symbol
                    return
                else:
                    board[i][j] = " "

    # Choose a random move
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = symbol
            break

# Function to play a game
def play_game():
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        symbols = ["X", "O"]
        player_symbol = random.choice(symbols)
        computer_symbol = symbols[(symbols.index(player_symbol) + 1) % 2]
        turn = random.choice([0, 1])

        print("Welcome to Tic Tac Toe!")
        display_board(board)

        while True:
            if turn % 2 == 0:
                player_turn(board, player_symbol)
                symbol = player_symbol
            else:
                computer_turn(board, computer_symbol)
                symbol = computer_symbol

            display_board(board)

            if check_win(board, symbol):
                if symbol == player_symbol:
                    print("Congratulations! You won!")
                else:
