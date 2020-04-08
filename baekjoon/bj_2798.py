import sys
input = sys.stdin.readline

def blackjack(arr,goal):
	length = len(arr)
	pick = 0
	ans = 0
	for i in range(0,length-2):
		for j in range(i+1,length-1):
			for k in range(j+1,length):
				pick = arr[i] + arr[j] + arr[k]
				if pick<=goal and goal-pick<goal-ans:
					ans = pick
	return ans


if __name__ == '__main__':
	n,m = map(int,input().split())
	num_arr = list(map(int,input().split()))
	ans = blackjack(num_arr,m)
	print(ans)