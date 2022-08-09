import sys
input = sys.stdin.readline

# bottom up으로 구현
def makeOne(num):
    for i in range (2, N+1) :
        # -1 하는 경우
        memoization[i] = memoization[i-1] + 1 
        # 3으로 나누는 경우
        if i%3 == 0 :
            memoization[i] = min(memoization[i],memoization[i//3]+1)
        # 2로 나누는 경우
        if i%2 == 0 :
            memoization[i] = min(memoization[i],memoization[i//2]+1)
    return memoization[num]
        

N = int(input())
memoization = [0] * (N+1)
# 가장 작은 크기의 문제 답 필수!
memoization[1] = 0
print(makeOne(N))
