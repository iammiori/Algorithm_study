import sys
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

if __name__ == '__main__':
	arr = list(map(int,input().split()))
	print(solution(arr))


