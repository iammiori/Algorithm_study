import sys
input = sys.stdin.readline

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

if __name__ == '__main__':
	number = int(input())
	print(Solution(number))