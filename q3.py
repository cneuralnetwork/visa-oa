# given an array of integer find pair such tht 0<=i<j<n and number of difference in the digit is one like 100,101 one digit is diff 
# other 2 are same 203 102 here 2 digit are diff so this wont count as pair so return the number of pairs

from collections import defaultdict
import sys


arr=list(map(int,sys.stdin.readline().split()))
n=len(arr)
s=set(arr)
grps=defaultdict(list)
for i in arr:
	grps[len(str(i))].append(str(i))
ans=0
for g in grps.values():
	cnt=defaultdict(int)
	d=len(g[0])
	for i in g:
		for j in range(d):
			patt=i[:j]+'*'+i[j+1:]
			cnt[patt]+=1
	for i in g:
		for j in range(d):
			patt=i[:j]+'*'+i[j+1:]
			ans+=cnt[patt]-1
return ans//2



------------------java-----------------

import java.util.*;

public class digitPair {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] arr = new int[n];

        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }

        int count=0;
        for(int i=0;i<n-1;i++){
            for(int j=i+1;j<n;j++){
                if(difference(arr[i],arr[j])){
                    count++;
                }
            }
        }

        System.out.println(count);
        
    }

    static boolean difference(int a,int b){
        String s1 = String.valueOf(a);
        String s2 = String.valueOf(b);
        int diff=0;

        if(s1.length()!=s2.length()){
            return false;
        }

        for (int i = 0; i < s1.length(); i++) {
            if (s2.charAt(i) != s1.charAt(i)) {
                diff++;
            }
            if(diff>1){
                return false;
            }
        }
        return diff==1;
    }
}
