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
def Solution2(num):

	# 9의 약수를 찾으면 (1,9) (3,3) (9,1) 이다 
	# 16도 (1,16) (2,8) (4,4) (8,2) (16,1) 이고
	# 여기서 얻을 수 있는건 제곱근 까지 생각하면 된다는 것이다.

	start = 2
	while start <= int(num**0.5) :
		if num % start == 0:
			num //= start
			print(start)
		else:
			start += 1

	# 마지막 출력		
	if num > 1:
		print(num)
	


if __name__ == '__main__':
	n = int(input())
	#Solution(n)
	#print("---")
	Solution2(n)