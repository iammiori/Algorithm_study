import sys
input = sys.stdin.readline

# 자연수가 1,000,000
MAX = 1000000

# d list는 1의 배수의 합
# s list는 자기꺼와 자기전들꺼 합 미리 저장
d = [1]*(MAX+1)
s = [0]*(MAX+1)

# 미리 구해놔 (각 숫자의 배열의 합)
for i in range(2,MAX+1):
	j = 1
	while i*j <= MAX:
		d[i*j] += i
		j += 1

# 전들꺼 합들도 저장
for i in range(1,MAX+1):
	s[i] = s[i-1] + d[i]

# 테스트 케이스
t = int(input())
ans = []
for _ in range(t):
	n = int(input())
	ans.append(s[n])

print('\n'.join(map(str,ans)))


