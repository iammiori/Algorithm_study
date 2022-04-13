import sys
from itertools import combinations
input = sys.stdin.readline

# 첫번째 풀이
def solution(numbers):
	answer = []

	for i in range(len(numbers)):
		for j in range(i+1,len(numbers)):
			tmp_sum = numbers[i] + numbers[j]
			# 중복제거를 위해
			if tmp_sum not in answer :
				answer.append(numbers[i] + numbers[j])
	answer.sort()
	return answer

def solution2(numbers):
	answer = []
	l = list(combinations(numbers,2))
	#print(l)
	for i in l:
		answer.append(i[0]+i[1])

	# set을 활용한 중복제거
	answer = list(set(answer))
	answer.sort()

	return answer


if __name__ == '__main__':
	arr = list(map(int,input().split()))
	print(solution(arr))
	print(solution2(arr))


