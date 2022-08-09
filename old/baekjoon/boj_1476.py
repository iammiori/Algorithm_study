import sys
input = sys.stdin.readline

e,s,m = map(int(input()).split())

i_e, i_s , i_m = 1, 1, 1
year = 1

while True:
	if e==i_e and s == i_s and m ==i_m :
		print(year)
		break
	e += 1
	s += 1
	m += 1
	if e == 16 :
		e = 1
	if s == 29 :
		s = 1
	if m == 20:
		m = 1
	year += 1
