#!/usr/bin/env python3


def ans(N):
	if (N == 0): return 'INSOMNIA'

	seen_digits = set()
	num = 0
	while len(seen_digits) < 10:		
		num += N
		for d in str(num):
			seen_digits.add(d)
	return num

T = int(input())

for t in range(T):
	N = int(input())
	print("Case #{0}: {1}".format(t+1, ans(N)))

