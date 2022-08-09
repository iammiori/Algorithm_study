import sys
input = sys.stdin.readline

in_arr = list(map(int,input().split()))
#in_arr.sort()
budget = int(input())


def solution(d, budget) :
	d.sort()
	answer = 0
	#tmp = d[0]

	for i in range(len(d)):
		if d[i] <= budget :
			answer += 1
			budget -= d[i]
		else:
			break
	return answer

print(solution(in_arr,budget))