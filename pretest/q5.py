import sys
input = sys.stdin.readline

#문자열로 바꿔서 푸는 방법

def Solution(number):
	# 3 6 9
	# 23 53 33
	# 26 56
	# 29 19
	# 문자열로 바꿔
	clap = 0
	
	for i in range(1,number+1):
		char_num = str(i)
		for j in char_num:
			if j=='3' or j=='6' or j=='9':
				clap +=1
	return clap

# 숫자로 해결
def Solution2(number):
	clap = 0
	for i in range(1,number+1):
		curr = i
		while curr != 0 :
			if curr % 10 == 3 or curr % 10 == 6 or curr % 10 == 9:
				clap += 1
			curr //= 10
	return clap

if __name__ == '__main__':
	number = int(input())
	print(Solution(number))
<<<<<<< HEAD
	print(Solution2(number))
=======
>>>>>>> 1cfedc8026968054575bd089bdd85cdb0194737c
