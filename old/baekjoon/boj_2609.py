import sys
input = sys.stdin.readline

a,b = map(int,input().split())

def GCD(x,y):
	if y==0:
		return x
	else:
		return GCD(y,x%y)

gcd = GCD(a,b)
print(gcd)
print(a*b // gcd)