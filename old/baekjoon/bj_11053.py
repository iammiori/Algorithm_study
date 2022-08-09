import sys
input = sys.stdin.readline

def LIS(arr):#시간복잡도 On^2
	global dp
	dp = [1]*len(arr)
	for i in range(1,len(arr)):
		for j in range(i):
			if arr[j] < arr[i]:
				#print("i:{}, j:{}, dp[i]:{}, dp[j]:{}, dp:{}".format(i,j,dp[i],dp[j]+1,dp))
				dp[i] = max(dp[i],dp[j]+1)
	print(max(dp))

def binary_search(arr,n):
	lower = 0
	upper = len(arr)-1
	while lower<=upper:
		mid = (lower+upper)//2
		if n <= arr[mid]:
			upper = mid-1		
		else:
			lower = mid+1
	return lower

def bs_LIS(arr):
	lis_list = [arr[0]]
	for i in range(1,len(arr)):
		if lis_list[-1] < arr[i]:
			lis_list.append(arr[i])
		else:
			idx = binary_search(lis_list,arr[i])
			lis_list[idx] = arr[i]
	return lis_list

if __name__ == '__main__':
	N = int(input())
	arr = list(map(int,input().split()))
	#LIS(arr)
	#print(lis(arr))
	ans = len(bs_LIS(arr))
	print(ans)