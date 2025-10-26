# Return the sum of elements in array which are greater then it's neighbours

arr=list(map(int,sys.stdin.readline().split()))
n=len(arr)
s=0
for i in range(1,n-1):
	if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
		s+=arr[i]
print(s)


-------java ----------

import java.util.*;

public class large_neigh {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int sum = 0;

        for (int i = 0; i < n; i++) {
            if ((i == 0 && arr[i] > arr[i + 1]) ||
                    (i == n - 1 && arr[i] > arr[i - 1]) ||
                    (i > 0 && i < n - 1 && arr[i] > arr[i - 1] && arr[i] > arr[i + 1])) {
                sum += arr[i];
            }
        }

        System.out.println(sum);

    }
}
