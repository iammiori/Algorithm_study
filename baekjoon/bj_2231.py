import sys
input = sys.stdin.readline

def num_len(num):
	_len = 0
	while(True):
		num //= 10
		_len +=1
		if num==0:
			break
	#print(_len)
	return _len


def Decomposition(num):
	_sum = num
	while True:
		if num<=0:
			break
		_sum += num % 10
		num //= 10
	return _sum

if __name__ == '__main__':
	a = int(input())
	min_num = a-(9*num_len(a))
	#print(min_num)
	ans = 0
	for i in range(min_num,a+1):
		b = Decomposition(i)
		#print(b)
		if b==a:
			ans = i
			print(ans)
			break
	if ans==0:
		print(0)
