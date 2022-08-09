import sys
input = sys.stdin.readline

def superstar(n,m,k):
	songs = {}
	for i in range(1,n+1):
		songs[i] = []
	for i in range(m): #장르 dict mapping
		ability = list(map(float,input().split()))
		for j in range(len(ability[::2])):
			songs[ability[2*j]].append(ability[(2*j)+1])
	winner = [max(songs[t]) for t in range(1,n+1)]
	winner.sort(reverse=True)
	return sum(winner[:k])

if __name__ == '__main__':
	n,m,k = map(int,input().split())
	ans = superstar(n,m,k)
	print("{0:0.1f}".format(ans))