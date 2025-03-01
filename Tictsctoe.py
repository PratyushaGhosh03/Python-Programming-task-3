import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if there are empty spaces left on the board
def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

# Function to evaluate the board and return a score
def evaluate(board):
    # Check rows, columns, and diagonals for a winner
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != " ":
            return 10 if board[row][0] == "O" else -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return 10 if board[0][col] == "O" else -10

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return 10 if board[0][0] == "O" else -10

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return 10 if board[0][2] == "O" else -10

    return 0

# Minimax algorithm for AI move
def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:  # AI wins
        return score - depth
    if score == -10:  # Player wins
        return score + depth
    if not is_moves_left(board):  # Draw
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = " "
        return best

# Function to find the best move for AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = " "

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Function to play Tic-Tac-Toe
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    print("Welcome to AI Tic-Tac-Toe! You are 'X' and AI is 'O'.")
    print_board(board)

    for _ in range(9):
        if evaluate(board) == 10:
            print("AI wins!")
            return
        elif evaluate(board) == -10:
            print("You win!")
            return
        
        if is_moves_left(board):
            row, col = map(int, input("Enter your move (row and column: 0 1 2): ").split())
            if board[row][col] == " ":
                board[row][col] = "X"
            else:
                print("Invalid move! Try again.")
                continue

            if is_moves_left(board):
                ai_move = find_best_move(board)
                board[ai_move[0]][ai_move[1]] = "O"

            print_board(board)

    if evaluate(board) == 0:
        print("It's a draw!")

# Start the game
play_game()
