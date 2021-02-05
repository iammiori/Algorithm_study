import sys
input = sys.stdin.readline

def Solution(num):
	ans = 1
	while num > 0:
		ans *= num
		num -= 1
	return ans

if __name__ == '__main__':
	n = int(input())
	#Solution(n)
	#print("---")
	print(Solution(n))