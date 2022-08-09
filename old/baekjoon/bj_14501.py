import sys
input = sys.stdin.readline

def dp(n,arr):
	memoization = [0]*20
	for i in range(n):
		if memoization[i] > memoization[i+1]:
			memoization[i+1] = memoization[i]
		# 상담 금액 > t 일후
		if memoization[i+arr[i][0]] < memoization[i] + arr[i][1]:
			memoization[i+arr[i][0]] = memoization[i] + arr[i][1]
	print(memoization[n])


if __name__ == "__main__":
	N = int(input())
	arr = list(list(map(int, input().split())) for _ in range(N))
	dp(N,arr)
