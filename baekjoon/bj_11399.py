import sys
input = sys.stdin.readline

#해결방법 : sort를 해보자.
def atm(arr): #84ms
	min_bun = 0
	arr.sort()
	tmp = []
	for i,bun in enumerate(arr):
		for j in range(i+1):
			min_bun += arr[j]
		#print(min_bun)
	print(min_bun)

def atm2(arr): #56ms
	min_bun = 0
	total_bun = 0
	arr.sort()
	for bun in arr:
		min_bun += bun
		total_bun += min_bun
	print(total_bun)



if __name__ == "__main__":
	a = int(input())
	#board = [list(map(int, input().split())) for _ in range(a)]
	arr_in = list(map(int,input().split()))
	#atm(arr_in)
	atm2(arr_in)
	