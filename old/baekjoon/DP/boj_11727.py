import sys
input = sys.stdin.readline

def makeTile2(n):
    # 초기
    arr[1] = 1
    if n >= 2 :
        arr[2] = 3
    for i in range(3,n+1) :
        # 점화식
        arr[i] = (arr[i-2] * 2) + arr[i-1]
    return arr[-1]%10007
        
N = int(input())
arr = [0] * (N+1)
print(makeTile2(N))
