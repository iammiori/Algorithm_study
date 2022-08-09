import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

def isPrime(n):
	if n < 2 :
		return False
	i = 2
	while i*i <= n:
		if n%i == 0 :
			 return False
		i += 1
	return True

def Solution(data):
	ans = 0
	for x in data:
		if isPrime(x) :
			ans += 1
	return ans

print(Solution(data))

