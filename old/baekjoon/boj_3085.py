import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input()) for _ in range(n)]
ans = 0

def check(arr, start_row, end_row, start_col, end_col):
	n = len(arr)
	ans = 1
	# 행
	for i in range(start_row, end_row+1):
		cnt = 1
		for j in range(1,n) :
			if arr[i][j] == arr[i][j-1] :
				cnt += 1
			else :
				cnt = 1
			if ans < cnt :
				ans = cnt
	# 열
	for i in range(start_col,end_col+1):
		cnt = 1
		for j in range(1,n):
			if arr[j][i] == arr[j-1][i]:
				cnt += 1
			else :
				cnt = 1
			if ans < cnt :
				ans = cnt
	return ans

for i in range(n):
	for j in range(n):
		# 오른쪽
		if j+1 < n :
			arr[i][j] , arr[i][j+1] = arr[i][j+1], arr[i][j]
			tmp = check(arr,i,i,j,j+1)
			if ans < tmp:
				ans = tmp
			arr[i][j] , arr[i][j+1] = arr[i][j+1], arr[i][j]

		# 아래
		if i+1 < n :
			arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
			tmp = check(arr,i,i+1,j,j)
			if ans < tmp :
				ans = tmp
			arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
print(ans)
