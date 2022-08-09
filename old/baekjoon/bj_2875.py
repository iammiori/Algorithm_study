import sys
input = sys.stdin.readline

def makeTeam(n,m,k):
	team=0
	while True:
		n-=2
		m-=1
		# 인원수에서 빼주면서,team 을 만들어
		if n<0 or m<0 or (n+m)<k: #종료조건 
			break
		team += 1
	print(team)

if __name__ == '__main__':
	N, M, K = list(map(int, input().split()))
	makeTeam(N,M,K)