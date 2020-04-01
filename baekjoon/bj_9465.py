import sys
input = sys.stdin.readline

def sticker(length,arr):
	global dp
	for i in range(2):
		for j in range(2,length+1):
				#print(max(dp[i+1][j-1],dp[i+1][j-2]))
				dp[0][j] = max(dp[1][j-1],dp[1][j-2]) + arr[0][j-1]
				dp[1][j] = max(dp[0][j-1],dp[0][j-2]) + arr[1][j-1]
	return max(dp[0][length],dp[1][length])

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		n = int(input())
		arr_in = [list(map(int, input().split())) for __ in range(2)]
		#print(arr_in)
		dp =[[0]*(n+1) for k in range(2)]
		dp[0][1] = arr_in[0][0]
		dp[1][1] = arr_in[1][0]

		ans = sticker(n,arr_in)
		#print(dp)
		print(ans)