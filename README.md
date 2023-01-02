# Sudoku_Solver
I, like many others, enjoy solving puzzles. and Sudoku is one of such things, that I love solving.

Sudoku is a popular Japanese puzzle game that is based on the logical placement of numbers. It doesn’t require any special mathematics skills or calculations.

One algorithm to solve Sudoku puzzles is the backtracking algorithm. Essentially, you keep trying numbers in empty spots until there aren't any that are possible, then you backtrack and try different numbers in the previous slots.
So I did use the concepts of backtracking and recursion, to solve this logical game.
To decide whether a number is valid for the first empty cell, we can use recursion to try solving the remaining 9 cells. If a solution is found for the remaining 9 cells, we know that the current number is the correct number.

On the other hand, if we are unable to find a solution for the remaining 9 cells, we update the current cell to the next possible number. In other words, based on the failed result of the remaining 9 cells, we backtrack to the current cell to update its value.

And Yooooooo, we are done!!!
