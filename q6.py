# Imagine that you're exploring a mysterious labyrinth in the shape of a rectangular matrix, which contains obstacles and teleports. 
# Starting from the upper-left corner, your goal is to reach the lower-right corner by first moving to the right, and then moving down if that doesn't work.

# You are given integers n and m representing the dimensions of the labyrinth. You are also given obstacles and teleports, which are lists of the cells that contain all the obstacles and teleports, respectively.

# Details about the labyrinth:

# An obstacle cannot be traversed - if there's an obstacle in the cell to your right, try moving down.
#  If there are obstacles in the cells to the right and below, stop immediately.
# A teleport is a pair of cells (start, end). If you reach the start cell, you immediately move to the end cell.
# Note that this doesn't work backwards: you cannot teleport from the end cell to the start cell.
# It is guaranteed that all teleports have unique start cells (i.e. each cell in the labyrinth has one teleport at most).
# It is guaranteed that the end cell for a teleport cannot be a start cell for another teleport.
# It is also guaranteed that both the start and end cells of a teleport do not contain obstacles.
# Any cell that doesn't contain an obstacle or a teleport is considered a free cell, and you can walk through it normally.
# You start at the upper-left corner cell with coordinates (0, 0), and the goal is to reach the exit located at the cell with coordinates (n - 1, m - 1). You move according to the following rules:

# First, you will always try moving to the right: if you're currently on the cell with coordinates (row, col) you will try moving to the cell with coordinates (row, col + 1).
# If the destination cell (row, col + 1) is the starting point of a teleport, proceed to the coordinates of the end cell.
# If the destination cell (row, col + 1) either contains an obstacle or is outside the bounds of the labyrinth, try moving down to the cell (row + 1, col).
# If the destination cell (row + 1, col) is the starting point of a teleport, proceed to coordinates of the end cell.
# If the destination cell (row + 1, col) either contains an obstacle or is outside the bounds of the labyrinth, stop moving and stay where you are.
# Your task is to check whether you can reach the goal (exit of the labyrinth) by following the algorithm above, and to return the 
# total number of cells you travelled through to reach the exit. Note that you should count all cells travelled, including the starting cell (0, 0) and both the start and end cells of all teleports. 
# If it is not possible to reach the exit, return -1 if it's because of an obstacle or due to trying to go outside the bounds of the labyrinth, or -2 if it's because of teleportation (i.e., an infinite teleport loop).

# It's guaranteed that the starting cell (0, 0) and the goal cell (n - 1, m - 1) do not contain an obstacle, or be the starting point of a teleport.

# Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(n * m * (obstacles.length + teleports.length)) will fit within the execution time limit.

# int solution(int n, int m, vector> obstacles, vector> teleports) {
# }

# Input: n = 3, m = 3, obstacles = [[2, 1]], teleports = [[0, 1, 2, 0]]
# Output: -1
# Explanation: You are unable to reach the exit because of an obstacle.




import java.util.*;

public class labyrinth {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            System.out.println("Enter rows and columns:");
            int n = sc.nextInt();
            int m = sc.nextInt();

            System.out.println("Enter no. of obstacles:");
            int obstacles = sc.nextInt();
            int[][] obsArray = new int[obstacles][2];
            System.out.println("Enter obstacle positions:");
            for (int i = 0; i < obstacles; i++) {
                obsArray[i][0] = sc.nextInt();
                obsArray[i][1] = sc.nextInt();
            }

            System.out.println("Enter no of teleport");
            int teleports = sc.nextInt();
            int[][] teleArray = new int[teleports][4];
            System.out.println("Enter teleport positions:");
            for (int i = 0; i < teleports; i++) {
                teleArray[i][0] = sc.nextInt();
                teleArray[i][1] = sc.nextInt();
                teleArray[i][2] = sc.nextInt();
                teleArray[i][3] = sc.nextInt();
            }

            int result = solve(n, m, obsArray, teleArray);
            System.out.println(result);


        }
    }

        private static int solve(int n,int m, int[][] obsArray, int[][] teleArray){
            boolean[][] obstacle = new boolean[n][m];

            for(int i=0;i<obsArray.length;i++){
                int row=obsArray[i][0];
                int col=obsArray[i][1];
                obstacle[row][col]=true;
            }

            Map<String, int[]> teleportMap = new HashMap<>();
            for(int i=0;i<teleArray.length;i++){
                int r1=teleArray[i][0];
                int c1=teleArray[i][1];
                int r2=teleArray[i][2];
                int c2=teleArray[i][3];
                teleportMap.put(r1 + "," + c1, new int[]{r2, c2});
            }

            Set<String> teleportVis = new HashSet<>();

            int r = 0, c = 0;
            int steps = 0;

            while(true){
                if(r == n-1 && c == m-1){
                    return steps;
                }

                int newr = r , newc = c+1;  //right move

                if( newc >= m || obstacle[newr][newc]){
                    newr = r+1;
                    newc = c;  //down move
                    if(newr >= n || obstacle[newr][newc]){
                        return -1;   //can't move
                    }
                }

                r = newr;
                c = newc;
                steps++;

               String  key = r + "," + c;
               while(teleportMap.containsKey(key)){
                    if(teleportVis.contains(key)){
                        return -2; //infinite loop
                    }
                    teleportVis.add(key);
                    int[] dest = teleportMap.get(key);
                    r = dest[0];
                    c = dest[1];
                    steps++;
               }
            }
        }
            
    }



