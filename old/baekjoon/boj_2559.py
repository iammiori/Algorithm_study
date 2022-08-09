import sys
input = sys.stdin.readline

n,k = map(int,input().split())
in_arr = list(map(int,input().split()))


sub_sum = sum(in_arr[:k])
# 1
ans = sub_sum
# 1
for i in range(k,n):
	# 2, 10
	sub_sum += in_arr[i]
	sub_sum -= in_arr[i-k]
	if sub_sum > ans :
		ans = sub_sum
print(ans)


# 3 -2 -4 -9 0 3 7 13 8 -3

# 1 -6 -13 -9 3 10 20 21 5
