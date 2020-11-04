import sys
input = sys.stdin.readline

def Solution(num):
	mock = 2
	while num != 1:
		if num % mock == 0:
			num //= mock
			#print(num) 몫 출력
			print(mock)
		else:
			mock += 1
		
if __name__ == '__main__':
	n = int(input())
	Solution(n)