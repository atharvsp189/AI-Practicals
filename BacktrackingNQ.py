def printBoard(board, N):
    for row in board:
        print(" ".join("Q" if col else"-" for col in row ))
    print()

def isSafe(board, row, col, N):
    # check for same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # check for upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # check for right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solveNQueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    def solve(row):
        if row >= N:
            printBoard(board, N)
            return True
        
        res = False
        for i in range(N):
            if isSafe(board, row, i, N):
                board[row][i] = 1
                res = solve(row+1) or res
                board[row][i] = 0
        return res

    if not solve(0):
        print("No Solution Exist")

N = 5
solveNQueens(N)