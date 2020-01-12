#solve 1

def solution1(participant, completion):
    participant.sort()
    completion.sort()
    for i,j in zip(participant,completion):
        if i!=j:
            return i
    return participant[-1]

'''
# 코드해석

- sort()로 정렬
- zip을 쓰면 두개의 배열 한 인자씩 묶어줘
- 각각을 비교
- 틀린게 있으면 바로 반환
- 없다면 끝까지 가서 맨 뒤에꺼 반환
'''

#solve 2

import collections

def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


'''
# 코드해석

- 결과는 다음과 같은 과정으로 나온다
1. Counter({'josipa': 1}) => answer 값
2. ['josipa'] =>  answer.keys()
3. 'josipa' => (answer.keys())[0]
'''

# ex
solution1(['marina', 'josipa', 'nikola', 'vinko', 'filipa'],['vinko', 'filipa', 'marina', 'nikola'])
solution2(['marina', 'josipa', 'nikola', 'vinko', 'filipa'],['vinko', 'filipa', 'marina', 'nikola'])