# Y-Pattern Transformation

# Problem Description

# You are a molecular biologist working in a research laboratory that studies protein folding patterns. You have a square matrix representing a microscopic view of 
# a protein structure, where each cell contains one of three possible molecular states: 0 (inactive), 1 (partially active), or 2 (fully active).

# Your research has identified a specific molecular pattern that indicates optimal protein stability - a "Y-shaped" molecular pathway. 
# This pattern consists of two diagonal molecular chains extending from the upper corners down to the center, plus a vertical chain extending downward from the center.

# Your task is to determine the minimum number of molecular state changes required to transform the current protein matrix into one that exhibits this stable Y-pattern.

# The Y-pattern is achieved when:

# all molecular states along the diagonals from the upper-left and upper-right corners down to the center are identical;
# all molecular states along the vertical path from the center downward are identical to the diagonal states;
# all other molecular states (the background) are identical to each other but different from the Y-pattern states.
# Note: For a square matrix of size n x n (where n is odd), there are exactly 6 possible Y-pattern configurations. 
# The Y-pattern states and background states can be any combination of the three molecular states (0, 1, 2) as long as they are different from each other.

# Below, you can see an example of the Y-pattern for a 5 x 5 matrix (red cells represent the Y-pattern states, white cells represent background states):

# n = 5
# +---+---+---+---+---+
# | R | W | W | W | R |
# +---+---+---+---+---+
# | W | R | W | R | W |
# +---+---+---+---+---+
# | W | W | R | W | W |
# +---+---+---+---+---+
# | W | W | R | W | W |
# +---+---+---+---+---+
# | W | W | R | W | W |
# +---+---+---+---+---+
# (R = Y-pattern state, W = Background state)
# Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(n^2) will fit within the execution time limit

