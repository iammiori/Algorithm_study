def solution(numbers):
	answer = []

	for i in range(len(numbers)):
		for j in range(i+1,len(numbers)):
			tmp_sum = numbers[i] + numbers[j]
			if tmp_sum not in answer :
				answer.append(numbers[i] + numbers[j])
	answer.sort()
	return answer
