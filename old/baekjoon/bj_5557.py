import sys
input = sys.stdin.readline


def dpFunc(arr):
	dp = [[0]*21 for _ in range(len(arr)-1)]
	dp[0][arr[0]] = 1
	for i in range(1,len(arr)-1):
		for j in range(21):
			tmp = dp[i-1][j]
			if tmp!=0:
				if j-arr[i] >=0 :
					dp[i][j-arr[i]] += tmp
				if j+arr[i]<=20:
					dp[i][j+arr[i]] += tmp
	print(dp[len(arr)-2][arr[-1]])


if __name__ == '__main__':
	n = int(input())
	numbers = list(map(int,input().split()))
	dpFunc(numbers)