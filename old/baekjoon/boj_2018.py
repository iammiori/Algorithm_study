import sys
input = sys.stdin.readline

N = int(input())
n_sum = 0
cnt = 1

for i in range (1,N//2+1):
	for j in range(i,N//2+2):
		n_sum += j
		if n_sum== N :
			#print(i,j)
			cnt += 1
			n_sum = 0
			break
		elif n_sum > N :
			n_sum = 0
			break

print(cnt)