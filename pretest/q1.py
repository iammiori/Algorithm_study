import sys
input = sys.stdin.readline

def Solution(money):
	zipe = [50000,10000,5000,1000,500,100,50,10,1]
	kind = []
	for i in zipe:
		kind.append(money//i)
		money %= i
	print(kind)

if __name__ == '__main__':
	money = int(input())
	Solution(money)



