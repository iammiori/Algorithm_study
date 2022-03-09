import sys
input = sys.stdin.readline

def makeOne(num):
    for i in range (2, N+1) :
        memoization[i] = memoization[i-1] + 1 
        if i%3 == 0 :
            memoization[i] = min(memoization[i],memoization[i//3]+1)
        if i%2 == 0 :
            memoization[i] = min(memoization[i],memoization[i//2]+1)
    return memoization[num]
        

N = int(input())
memoization = [0] * (N+1)
memoization[1] = 0
print(makeOne(N))
