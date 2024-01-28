def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

def find_empty_location(board, l):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False

def is_safe(board, row, col, num):
    # Check if the number is not present in the current row and column
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False

    # Check if the number is not present in the current 3x3 subgrid
    startRow, startCol = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[startRow + i][startCol + j] == num:
                return False

    return True

def solve_sudoku(board):
    l = [0, 0]

    if not find_empty_location(board, l):
        return True

    row, col = l[0], l[1]

    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

if __name__ == "__main__":
    # Example Sudoku board (0 represents empty cells)
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(sudoku_board):
        print("Sudoku Solution:")
        print_board(sudoku_board)
    else:
        print("No solution exists.")
