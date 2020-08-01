#!/usr/bin/env python3
	
N = 500
inf = 10**9

print(N)

for i in range(N):
	if i % 4 in [0, 2]:
		print(*[1]*N)
		continue
	r = [inf]*N
	if i % 4 == 1:
		r[-1] = 1
	else:
		r[0] = 1
	print(*r)