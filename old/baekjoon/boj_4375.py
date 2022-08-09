import sys
input = sys.stdin.readline

# input 개수 제한 없는 경우는
# try, except 구문

while True:
	try : 
		n = int(input())
	except:
		break

	# num : 수가 너무 커지면 그 수를 계산 하는데 오래 걸림
	# 따라서, 나눈 나머지를 기억
	# i : 1의 개수
	num = 0
	i = 1
	while True:
		num = num*10 + 1
		num %= n
		if num == 0 :
			print(i)
			break
		i += 1