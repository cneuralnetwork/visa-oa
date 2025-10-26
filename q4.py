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




----------------java solution-----------------


import java.util.*;

public class Yprotein {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            int n = sc.nextInt();
            int[][] mat = new int[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    mat[i][j] = sc.nextInt();
                }
            }

            int mid = n / 2;
            // Create a boolean mask for Y-shaped positions
            boolean[][] isY = new boolean[n][n];

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if ((i <= mid && (j == i || j == n - i - 1)) || (i >= mid && j == mid)) {
                        isY[i][j] = true;
                    }
                }
            }

            int minChanges = Integer.MAX_VALUE;

            // Try all 6 (Y_state, background_state) combinations
            for (int yState = 0; yState < 3; yState++) {
                for (int bgState = 0; bgState < 3; bgState++) {
                    if (yState == bgState) continue;

                    int changes = 0;
                    for (int i = 0; i < n; i++) {
                        for (int j = 0; j < n; j++) {
                            int expected = isY[i][j] ? yState : bgState;
                            if (mat[i][j] != expected) {
                                changes++;
                                mat[i][j] = expected;
                            }
                        }
                    }

                    minChanges = Math.min(minChanges, changes);
                }
            }

            System.out.println("Total changes : " +minChanges);

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    System.out.print(mat[i][j] + " ");
                }
                System.out.println();
            }
        }

        sc.close();
    }
}


