import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
ans = min(data) * max(data)
print(ans)