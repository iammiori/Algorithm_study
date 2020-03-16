import sys
input = sys.stdin.readline

def choco(n,m):
	# n(m-1) + (n-1)
	#ans = (m-1)*n + (n-1)
	ans = n*m-1
	print(ans)

if __name__ == '__main__':
	N,M = map(int,input().split())
	choco(N,M)