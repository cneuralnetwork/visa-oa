# Return the sum of elements in array which are greater then it's neighbours

arr=list(map(int,sys.stdin.readline().split()))
n=len(arr)
s=0
for i in range(1,n-1):
	if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
		s+=arr[i]
print(s)