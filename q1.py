# since you love games of chance, you've decided to participate in a dice-rolling competition. The competition involves rolling three 6-sided dice, 
# and the results of each die are represented by the integers a, b, and c respectively. Scores are calculated according to the following rules:

# If all three dice had the same value (a = b = c), you earn 1000 * a.
# If exactly two of them are the same, you earn 500 * x (where x is the value of the two equal dice).
# If all of them are different, you earn 100 * min(a, b, c).
# Given the values of a, b, and c, your task is to calculate and return your total score.


a,b,c=map(int,sys.stdin.readline().split())
if a==b==c:
	print(1000*a)
elif a==b or a==c:
	print(500*b)
elif c==b:
	print(500*a)
else:
	print(100*min(a,b,c))




--------------java solution-----------------

import java.util.*;

public class dice {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();

            if(a==b && b==c){
                System.out.println(1000*a);
            }
            else if(a==b || b==c){
                System.out.println(500*b);
            }
            else if(a==c){
                System.out.println(500*a);
            }
            else{
                System.out.println(100*Math.min(a,Math.min(b,c)));
            }
        }
    }
}
