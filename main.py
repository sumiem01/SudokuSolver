"""coding: utf-8
Name: SudokuSolver
Description: An algorithm for solving given sudoku board if there exist a solution. Will use backtracking algorithm.
Input: numpy.array
Output: numpy.array

Remarks:
Each cell can have position (i, j) from (0, 0) to (8, 8)
Each board has 9 * 9 = 81 cells so I need to create conditions for each cell based on it's position.
There are 3 conditions each for row, column, and square.
The biggest problem is square condition as it changes based on position of the cell.
i.e. There are 9 squares inside a sudoku board and they also have their position from (0, 0) to (2, 2)
cell (0, 2) is in square (0, 0) but (0, 3) is in square (0, 1)
I should probably create a class Cell with Position, Number, Status attributes
Status can be a property of a cell
"""
import itertools
# example from wikipedia
sudoku = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def solved(area: list, is_square=False) -> bool:
    if is_square:
        #  making square flat because it's a nested list
        area = list(itertools.chain.from_iterable(area))
    return len(area) == len(set(area))


def check_row(table: list, cell_position: tuple) -> bool:
    return solved(table[cell_position[0]][:])


def check_col(table: list, cell_position: tuple) -> bool:
    return solved([i[cell_position[1]] for i in table])


def check_square(table: list, cell_position: tuple):
    square = [i[((cell_position[1] // 3) * 3):(3 + (cell_position[1] // 3) * 3)] for i in table[((cell_position[0] // 3) * 3):(3 + (cell_position[0] // 3) * 3)]]
    return solved(square, True)


if __name__ == "__main__":
    print(check_square(sudoku, (0, 1)))
