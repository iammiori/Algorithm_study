import sys
input = sys.stdin.readline

n, k = map(int, input().split()) 
#coin = [int(input()) for _ in range(n)] 
cnt = 0

for i in reversed(eval("int(input()),"*n)):
	cnt+=k//i
	k=k%i 
print(cnt)