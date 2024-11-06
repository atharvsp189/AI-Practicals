import math

# Constants representing players and empty cells
PLAYER_X = 1  # Maximizing player
PLAYER_O = -1  # Minimizing player
EMPTY = 0

# Initialize the Tic-Tac-Toe board
board = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]

def print_board(board):
    """Utility function to print the Tic-Tac-Toe board."""
    for row in board:
        print(["X" if x == PLAYER_X else "O" if x == PLAYER_O else " " for x in row])
    print()

def is_moves_left(board):
    """Check if there are moves left on the board."""
    for row in board:
        if EMPTY in row:
            return True
    return False

def evaluate(board):
    """Evaluate the board for a winning state."""
    # Check rows and columns for win
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    # Check diagonals for win
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return 0  # No winner yet

def minimax(board, depth, alpha, beta, is_max):
    """Minimax function with Alpha-Beta pruning."""
    score = evaluate(board)

    # If Maximizer (X) has won, return score
    if score == PLAYER_X:
        return 10 - depth
    # If Minimizer (O) has won, return score
    if score == PLAYER_O:
        return depth - 10
    # If there are no moves left, it's a tie
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    best = max(best, minimax(board, depth + 1, alpha, beta, False))
                    board[i][j] = EMPTY
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        return best
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    best = min(best, minimax(board, depth + 1, alpha, beta, True))
                    board[i][j] = EMPTY
                    beta = min(beta, best)
                    if beta <= alpha:
                        return best
        return best

def find_best_move(board, player):
    """Find the best move for the given player using Minimax with Alpha-Beta pruning."""
    best_val = -math.inf if player == PLAYER_X else math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                # Make the move
                board[i][j] = player
                move_val = minimax(board, 0, -math.inf, math.inf, player == PLAYER_O)
                # Undo the move
                board[i][j] = EMPTY
                # Update best move
                if (player == PLAYER_X and move_val > best_val) or (player == PLAYER_O and move_val < best_val):
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Example usage
current_player = PLAYER_X  # X starts

while is_moves_left(board) and evaluate(board) == 0:
    print("Current Board:")
    print_board(board)
    if current_player == PLAYER_X:
        print("Player X's Move:")
        row, col = find_best_move(board, PLAYER_X)
    else:
        print("Player O's Move:")
        row, col = find_best_move(board, PLAYER_O)

    if row != -1 and col != -1:
        board[row][col] = current_player
    else:
        print("No valid moves left!")

    # Switch player
    current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

# Final result
print("Final Board:")
print_board(board)
result = evaluate(board)
if result == PLAYER_X:
    print("Player X wins!")
elif result == PLAYER_O:
    print("Player O wins!")
else:
    print("It's a tie!")
