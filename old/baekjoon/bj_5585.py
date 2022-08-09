import sys
input = sys.stdin.readline

def coin(n):
	remain = 1000 - n
	change = [500,100,50,10,5,1]
	ans = 0
	for i in change:
		ans += remain//i
		remain %= i
	print(ans)

if __name__ == '__main__':
	N = int(input())
	coin(N)