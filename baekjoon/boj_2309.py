import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]
arr.sort()

total = sum(arr)
for i in range(0,9):
	for j in range(i+1,9):
		if total - arr[i] - arr[j] == 100:
			for k in range(9):
				if i == k or j == k:
					continue
				print(arr[k])
			sys.exit(0)