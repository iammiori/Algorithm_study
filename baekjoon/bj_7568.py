import sys
input = sys.stdin.readline

def dunchi(arr):
	for i,pre in enumerate(arr):
		rank = 1
		for after in arr:
			if (pre[0]!=after[0]) & (pre[1]!=after[1]):
				if (pre[0]<after[0]) & (pre[1]<after[1]):
					rank += 1
		print(rank)

	return

if __name__ == '__main__':
	n = int(input())
	info = []
	for i in range(n):
		w,h = map(int,input().split())
		info.append((w,h))
	dunchi(info)