import sys 
input = sys.stdin.readline

# DFS 활용

# 방법론
# 특정 지점의 상하좌우 값이 0이면서, 아직 방문 안했으면 방문
# 방문한곳 다시 상하좌우 확인

def DFS(x,y) :
	# 범위 밖
	if x<=-1 or x>=n or y<=-1 or y>=m :
		return False
	if graph[x][y] == 0 :
		graph[x][y] = 1

		# 상하좌우 재귀 호출
		DFS(x-1,y)
		DFS(x,y-1)
		DFS(x+1,y)
		DFS(x,y+1)
		return True
	return False

if __name__ == '__main__':
	n,m = map(int,input().split())
	graph = []
	for i in range(n):
		graph.append(list(map(int,input().rstrip())))

	answer = 0
	for i in range(n):
		for j in range(m):
			if DFS(i,j) == True:
				answer += 1

	print(answer)
		