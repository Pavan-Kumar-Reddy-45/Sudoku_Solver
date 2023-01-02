from pprint import pprint


def valid_check(grid, guess, row, col):
    #Check's if our guess is valid or not, using the logic.
    #If our guess, collides with any number in that row, column or a particular square, return False
    #Else our guess is correct, return True..

    # let's start with the row
    row_check = grid[row]
    if guess in row_check:
        return False # if we've repeated, then our guess is not valid!

    # now the column
    col_check = [grid[i][col] for i in range(9)]
    if guess in col_check:
        return False

    # and then the square
    #Dividing into sections and then cross-checking the values..
    #Floor division gives section and multiplying it with 3 gives the exact location..
    row_look_up = (row // 3) * 3 
    col_look_up = (col // 3) * 3

    for r in range(row_look_up, row_look_up + 3):
        for c in range(col_look_up, col_look_up + 3):
            if grid[r][c] == guess:
                return False

    return True

def look_nill(grid):
    # Looks for the next row,column that's unfilled
    # If it's filled, return "None"..

    for r in range(9): #Loop till the last row
        for c in range(9): #Loop till the last column
            if grid[r][c] == -1:
                return r, c

    return None, None  #If every row and column is filled, return "None" tuple

def solve_sudoku(grid):
    # solving Sudoku using backtracking and recursion!
    # our puzzle is a list of lists, where each inner list is a row in our sudoku grid..
    
    #Choose somewhere on the puzzle to make a guess
    row, col = look_nill(grid)

    #if everything is filled, then we allowed only valid input's..
    if row is None:  
        return True 
    
    #If everything isn't nill, make a guess..
    for guess in range(1, 10): #Valid input's between 1 and 9 only..
        #Checking for validity..
        if valid_check(grid, guess, row, col):#If valid, then place the value in the square..
            grid[row][col] = guess
            
            if solve_sudoku(grid): #Recursive call to solve the complete grid..
                return True
        
        #If not true, try a new number by back-tracking..
        grid[row][col] = -1

    #If nothing works, the puzzle is UN-SOLVABLE!!!
    return False

if __name__ == '__main__':
    check_board = [
        [4, -1, 7,   -1, -1, -1,   -1, 6, -1],
        [-1, 1, -1,   6, -1, 7,   -1, -1, 2],
        [-1, 8, -1,   -1, -1, -1,   1, 9, 7],

        [1, -1, -1,   4, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, 3, 8,   2, 1, 9],
        [5, 9,  8,     -1, 6, 2,   -1, -1, -1],

        [-1, -1, 1,   3, 4, -1,   9, 2, -1],
        [2, -1, 6,    8, 9, -1,   -1, 7, 3],
        [-1, -1, 9,   -1, 2, 6,   8, -1, -1]
    ]
    print(solve_sudoku(check_board))
    pprint(check_board)