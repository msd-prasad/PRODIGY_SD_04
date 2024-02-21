import tkinter as tk

def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    
    if num in [board[i][col] for i in range(9)]:
        return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  
    
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0 
    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def get_input_from_keyboard():
    print("Enter the Sudoku puzzle row by row. Use 0 for empty cells.")
    board = []
    for i in range(9):
        while True:
            row_input = input(f"Enter row {i+1} (9 numbers separated by space): ")
            row = list(map(int, row_input.split()))
            if len(row) == 9:
                board.append(row)
                break
            else:
                print("Invalid input. Please enter exactly 9 numbers.")

    return board

def display_board(board):
    for i in range(9):
        for j in range(9):
            cell_label = tk.Label(root, text=str(board[i][j]), width=3, font=('Helvetica', 16, 'bold'))
            cell_label.grid(row=i+1, column=j)

def solve_and_display():
    input_grid = get_input_from_keyboard()
    if solve_sudoku(input_grid):
        output_label.config(text="Solved Sudoku puzzle:")
        display_board(input_grid)
    else:
        output_label.config(text="No solution exists.")

root = tk.Tk()
root.title("Sudoku Solver")

input_label = tk.Label(root, text="Enter Sudoku puzzle:", font=('Helvetica', 14))
input_label.grid(row=0, column=0, columnspan=9)

output_label = tk.Label(root, text="", font=('Helvetica', 14))
output_label.grid(row=10, column=0, columnspan=9)

solve_button = tk.Button(root, text="Solve", command=solve_and_display)
solve_button.grid(row=11, column=0, columnspan=9)

root.mainloop()