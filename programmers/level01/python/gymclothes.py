def solution(n, lost, reserve):
    answer = n - len(lost)
    for r in reversed(reserve) :
        if r-1 in lost or r+1 in lost :
            answer += 1
            lost.pop()
    return answer
    
