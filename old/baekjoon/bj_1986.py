import sys
input = sys.stdin.readline

def knight(x,y):
	safe[x][y] = 0
	for k in range(len(knightx)):
		#print(knightx)
		tmpx = x + knightx[k]
		tmpy = y + knighty[k]
		if 0<=tmpx<n and 0<=tmpy<m:
			safe[tmpx][tmpy]=0

def queen(x,y):
	safe[x][y] = 0
	for q in range(len(queenx)):
		tmpx = x + queenx[q]
		tmpy = y + queeny[q]
		while True:
			if 0<=tmpx<n and 0<=tmpy<m and nonsafe[tmpx][tmpy]==0:
				safe[tmpx][tmpy] = 0
				tmpx += queenx[q]
				tmpy += queeny[q]
			else:
				break

if __name__ == '__main__':
	knightx = [-1,-1,-2,-2,1,1,2,2]
	knighty = [2,-2,1,-1,2,-2,1,-1]
	queenx = [-1,-1,-1,0,0,1,1,1] 
	queeny = [-1,0,1,-1,1,-1,0,1]
	n,m = map(int,input().split())
	q = list(map(int,input().split()))
	k = list(map(int,input().split()))
	p = list(map(int,input().split()))
	qn,kn,pn = q.pop(0),k.pop(0),p.pop(0)
	#print(pn)
	
	safe = [[1] * m for _ in range(n)]
	nonsafe = [[0] * m for _ in range(n)]
	
	#print(safe)
	for i in range(0,2*qn,2):
		nonsafe[q[i]-1][q[i+1]-1]="X"
	for i in range(0,2*kn,2):
		nonsafe[k[i]-1][k[i+1]-1]="X"
	for i in range(0,2*pn,2):
		nonsafe[p[i]-1][p[i+1]-1]="X"	

	for i in range(0,2*qn,2):
		queen(q[i]-1,q[i+1]-1)
		#print(safe)
	for i in range(0,2*kn,2):
		knight(k[i]-1,k[i+1]-1)	
		#print(safe)
	for i in range(0,2*pn,2):
		#print(p[i]-1,p[i+1]-1)
		safe[p[i]-1][p[i+1]-1]=0
	#print(safe)
	ans = 0
	for i in range(n):
		ans += sum(safe[i])
	print(ans)
