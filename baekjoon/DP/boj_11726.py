import sys
input = sys.stdin.readline

def makeTile(n):
    # 초기
    arr[0] = 1 
    arr[1] = 1
    for i in range(2,n+1) :
        # 점화식
        arr[i] = arr[i-1] + arr[i-2]
        arr[i] %= 10007
    return arr[-1]
        
N = int(input())
arr = [0] * (N+1)
print(makeTile(N))
