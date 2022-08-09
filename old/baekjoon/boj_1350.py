import sys
input = sys.stdin.readline

# 디스크 공간의 개수를 구하는 함수
def diskSpace(file,cluster):
	total = 0
	for i in file : 
		# 파일사이즈가 0이거나 클러스터 크기랑 같을때
		if i % cluster == 0 :
			total += i//cluster
		# 그 외에는 몫 + 1
		else:
			total += i//cluster + 1 
	return total

n = int(input())
file = list(map(int,input().split()))
cluster = int(input())

# 위의 함수에서 디스크 공간에 필요한 개수를 구했으니까 클러스터 크기랑 곱해서 실 공간 출력
ans = diskSpace(file,cluster) * cluster
print(ans)