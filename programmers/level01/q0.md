# 완주하지 못한 선수

<b>try #1</b>
```
def solution(participant, completion):
    answer = ''
    for i in completion:
        if i in participant:
            participant.remove(i)
    answer = participant[0]
    return answer
 ```
result : Accuracy 50/50 Efficiency 0/50 total 50/100
<br><br>
<b>try #2</b>
```
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i,j in zip(participant,completion):
        if i!=j:
            return i
    return participant[-1]
 ```
 result : Accuracy 50/50 Efficiency 50/50 total 100/100
 <br><br>
 <b>좋은 풀이</b>
 ```
 import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
 ```
 - python 간결함의 예술의 경지
 - collection 모듈 공부하기..

