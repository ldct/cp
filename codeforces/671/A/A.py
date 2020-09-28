#!/usr/bin/env pypy3
	
from collections import defaultdict

def ans(N):

	num = defaultdict(int)	

	for i, e in enumerate(N):
		e = int(e) % 2
		i = 1 - (i % 2)
		num[(i, e)] += 1

	if len(N) % 2 == 1:
		# P2 moves last
		if num[(1, 1)] > 0:
			return 1
		else:
			return 2
	else:
		# P1 moves last
		if num[(0, 0)] > 0:
			return 2
		else:
			return 1

	return '?'

T = int(input())
for t in range(T):
	input()
	N = input()
	print(ans(N))