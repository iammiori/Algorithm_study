import sys
input = sys.stdin.readline

def fibo(n):
	if n<=1:
		return n
	else:
		#return fino(n-1)+fibo(n-2)
		i,t0,t1 = 2,0,1
		while i<=n:
			t0,t1 = t1,t0+t1
			i+=1
		return t1

def fibo2(n):
	young = 1
	ill = 0
	tmp = 0
	for _ in range(n):
		tmp = ill
		ill += young
		young = tmp
	print("{} {}".format(young,ill))


if __name__ == '__main__':
	N = int(input())
	while (N>0):
		x = int(input())
		fibo2(x)
		N-=1

