# You are given two sorted arrays A and B, each representing the departure times of two spaceships, and an integer mission.

# Your task is to determine the earliest time at which you can complete exactly mission pairings, where each pairing follows this rule:

# Select one element a from array A and find the smallest element b in array B such that b > a.

# This pairing represents one successful mission.

# Repeat this process until you complete mission such pairings.

# If fewer than mission valid pairings can be made, output -1.

# Example

# A = [1, 3, 5]
# B = [2, 4, 6]
# mission = 2


# Explanation:

# Pair 1: A[0]=1 → next greater in B is 2

# Pair 2: A[1]=3 → next greater in B is 4
# The second mission finishes at time 4.

# Output: 4

import sys

A=list(map(int,sys.stdin.readline().split()))
B=list(map(int,sys.stdin.readline().split()))
mission=int(sys.stdin.readline())
i=j=0
cnt=0
n,m=len(A),len(B)
chk=0
while i<n and j<m:
	if B[j]>A[i]:
		cnt+=1
		if cnt==mission:
			# return B[j]
			chk=1
			break
		i+=1
		j+=1
	else:
		j+=1
if chk:
	print(B[j])
else:
	print(-1)