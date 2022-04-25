import copy

# Checks if the value is correct to be inserted at arr[x][y] place according to sudoku rules.
def is_valid(arr, x, y, num):
    # Inserting value assuming its correct
    arr[x][y] = num
    
    # Checking if there is any doubles in column y
    column_list = [arr[i][y] for i in range(9)] # All numbers in column y
    zeroes = column_list.count(0) # Number of zeroes need to be excluded as they can't be counted as doubles
    if zeroes != 0: zeroes -= 1 # If there is more than 0 zeroes then subtract 1 because set of array will have one 0
    if len(set(column_list)) + zeroes != 9: 
        return False

    # Checking if there is any doubles in row x as we did for columns
    row_list = [arr[x][j] for j in range(9)]
    zeroes = row_list.count(0)
    if zeroes != 0: zeroes -= 1
    if len(set(row_list)) + zeroes != 9:
        return False

    # Checking if there is any double in box
    row_no = (x//3)*3 # Gives number of box it belong horizontally
    col_no = (y//3)*3 # Gives number of box it belong vertically

    # all numbers in that box
    box_list = [arr[i][j] for i in range(row_no, row_no+3) for j in range(col_no, col_no+3)]
    zeroes = box_list.count(0)
    if zeroes != 0: zeroes -= 1
    if len(set(box_list)) + zeroes != 9:
        return False

    return True
     
# Takes the 2D array and returns the coordinates of first 0 it finds
def empty_cell(arr):
    for x, i in enumerate(arr):
        for y, j in enumerate(i):
            if j == 0:
                return (x, y)
    return None

# This function takes a 2D 9x9 array and a 1D array. 
# It solves the sudoku board using backtracking algorithm.
# Returns 3 objects, one being boolean value if board is solved or not, second is steps which is 2D
# array containing x and y coordinate of board which was changed to value (EX: [["3x3":3]])
# Third is final board of array. Neccessary to return in case board wasn't completely solved so
# it shows till where it was solved.
def solve(arr, steps):
    # If any empty cell is not left then board is solved and it returns
    cell = empty_cell(arr)
    if cell == None:
        return (True, steps, arr)

    x, y = cell
    for i in range(1, 10):
        # Checks if adding this value is valid according to sudoku rules
        if is_valid(copy.deepcopy(arr), x, y, i):
            arr[x][y] = i
            steps.append([f"{x}x{y}",  i])
            a, steps, arr = solve(arr, steps)
            if a:
                return True, steps, arr
            
            arr[x][y] = 0
            steps.append([f"{x}x{y}",  " "])


    return False, steps, arr

# Its only checking resp to number not whole board so if board is invalid
# initially then too it won't identify that!!
# def is_valid(arr, x, y, num):
#     for i in range(9):
#         if arr[i][y] == num and i != x:
#             return False

#     for i in range(9):
#         if arr[x][i] == num and i != y:
#             return False
#     row_no = (x//3)*3 
#     col_no = (y//3)*3

#     for i in range(row_no, row_no+3):
#         for j in range(col_no, col_no+3):
#             if arr[i][j] == num and (i, j) != (x, y):
#                 return False
#     return True


