# 완주하지 못한 선수

<b>try #1</b>
```
def solution(array, commands):
    answer = []
    for x in commands:
        arr = array[x[0]-1:x[1]]
        arr.sort()
        arr2 = arr[x[2]-1]
        answer.append(arr2)
    return answer
```

result : Accuracy 50/50 Efficiency 50/50 total 100/100
<br><br>

 <b>좋은 풀이</b>
 ```
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
 ```
 - python 간결함의 예술의 경지
 - map 이랑 lambda를 더 공부해야겠다
