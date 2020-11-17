import sys
input = sys.stdin.readline

def make_one(num):
	dp_list = [0,0,1,1]
	for i in range(4,num+1):
		# 1을 빼는 경우
		dp_list.append(dp_list[i-1]+1)

		if i%2 == 0:
			dp_list[i] = min(dp_list[i],dp_list[i//2]+1)

		if i%3 == 0:
			dp_list[i] = min(dp_list[i],dp_list[i//3]+1)

	return dp_list[-1]

if __name__ == '__main__':
	N = int(input())
	print(make_one(N))