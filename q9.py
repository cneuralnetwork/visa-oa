# Given an array nums and an integer k, find the number of contiguous subarrays that contain
 # at least k distinct elements (repeated occurrences of the same element 
# within a subarray do not count as distinct).

def solve(nums,k):
	cnt=defaultdict(int)
	l=0
	ans=0
	uni=0
	for r,val in enumerate(nums):
		if cnt[val]==0:
			uni+=1
		cnt[val]+=1
		while uni>k:
			cnt[nums[l]]-=1
			if cnt[nums[l]]==0:
				uni-=1
			l+=1
		ans+=r-l+1
	return ans

import sys
nums=list(map(int,sys.stdin.readline().split()))
k=int(sys.stdin.readline())
n=len(nums)
print(n*(n+1)//2 - solve(nums,k-1))