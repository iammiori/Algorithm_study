import sys
input = sys.stdin.readline

def pickme(test_num):
	for _ in range(test_num):
		n = int(input())
		arr = [0]*(n+1)
		for __ in range(n):
			p1,p2 = map(int,input().split())
			arr[p1] = p2
		winner = arr[1]
		pick = 1 #winner는 무조건 뽑히니까
		for person in arr[2:]:
			if winner > person:
				pick +=1
				winner = person # 더 높은 등수로 갱신
		print(pick)

if __name__=="__main__":
	test = int(input())
	pickme(test)
