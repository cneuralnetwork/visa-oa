# Number of 2x2 Submatrices with Black Cells

# Problem Description

# For a grid of black and white cells with rows rows and cols columns, you're given an array black that contains the [row, column] coordinates of all the black cells in the grid.

# Your task is to compute how many 2 x 2 submatrices of the grid contain exactly blackCount black cells, for each 0 <= blackCount < 4. 
# As a result, you will return an array of 5 integers, where the ith element is the number of 2 x 2 submatrices with exactly i black cells.

# It is guaranteed that black cell coordinates are pairwise unique, so the same cell is not colored twice.

# Examples

# Example 1:
# Input: rows = 3, cols = 3, black = [[0, 0], [0, 1], [1, 0]]
# Output: [1, 2, 0, 1, 0]

