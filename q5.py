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




import java.util.*;

public class blackMatrix {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            System.out.println("Enter rows and columns:");
            int n = sc.nextInt();
            int m = sc.nextInt();
            // write your logic here
            int[][] matrix = new int[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    matrix[i][j] = 0;
                }
            }

            System.out.println("Enter number of Black cells:");
            int blackRows = sc.nextInt();
            int[][] bArray = new int[blackRows][2];
            System.out.println("Enter Black matrix positions:");
            
            for(int i=0;i<blackRows;i++){
                for(int j=0;j<2;j++){
                    bArray[i][j]=sc.nextInt();
                }
            }

            for(int i=0;i<blackRows;i++){
                int row=bArray[i][0];
                int col=bArray[i][1];
                matrix[row][col]=1;
            }

            int[] ans = new int[5];


  for (int r1 = 0; r1 < n - 1; r1++) {
    for (int c1 = 0; c1 < m - 1; c1++) {
        int r2 = r1 + 1;
        int c2 = c1 + 1;
        int blacks = checkBlack(matrix, r1, c1, r2, c2);
        ans[blacks]++;
    }
}



                System.out.println(ans[0] + " " + ans[1] + " " + ans[2] + " " + ans[3] + " " + ans[4]);


        }

    }

    private static int checkBlack(int[][] matrix, int r1, int c1, int r2, int c2){
        int count = 0;

        for(int i=r1;i<=r2;i++){
            for(int j=c1;j<=c2;j++){
                if(matrix[i][j] == 1){
                    count++;
                }
            }
        }

        return count;
    }
}
