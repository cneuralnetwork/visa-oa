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
