def printBoard(board, N):
    for row in board:
        print(" ".join("Q" if col else "-" for col in row))
    print()

def solveNQueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    col = [False] * N
    diag1 = [False] * (2 * N -1) # left diagnoal
    diag2 = [False] * (2 * N -1) # right diagonal
    
    def solve(row):
        if row == N:
            printBoard(board, N)
            return True
        res = False
        for i in range(N):
            if not col[i] and not diag1[row+i] and not diag2[row-i+N-1]:
                # place queen
                board[row][i] = 1
                col[i] = diag1[row+i] = diag2[row-i+N-1] = True
                
                res = solve(row+1) or res # move to next row
                board[row][i] = 0
                col[i] = diag1[row+i] = diag2[row-i+N-1] = False # Backtrack
        
        return res
    
    if not solve(0):
        print("No solution Exist")

N = 4
solveNQueens(N)
