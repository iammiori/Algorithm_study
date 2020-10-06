import sys
input = sys.stdin.readline

n, m = map(int,input().split())
in_arr = list(map(int,input().split()))
sub_sum = 0
sum_arr = []

# for i in range(len(in_arr)):
# 	sub_sum = 0
# 	for j in range(0,i+1):
# 		sub_sum += in_arr[j]
# 	sum_arr.append(sub_sum) 

for i in range(n):
	if i == 0 :
		sum_arr.append(in_arr[0])
	else:
		sum_arr.append(sum_arr[i-1] + in_arr[i])

for i in range(m):
	start,end = map(int,input().split())
	if start == 1 :
		print(sum_arr[end-1])
	else :
		print(sum_arr[end-1]-sum_arr[start-2])

#print(sum_arr)