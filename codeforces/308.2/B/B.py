#!/usr/bin/env python3

N_str = input()
N = int(N_str)

def num_overlaps(a, b, c, d):
	# number of elements in [a, b] ^ [c, d]

	lb = max(a, c)
	ub = min(b, d)

	return len(range(lb, ub+1))

def range_with_digits(d):
	return (10**(d-1), 10**d - 1)

ans = 0
for d in range(1, len(N_str) + 1):
	no = num_overlaps(1, N, *range_with_digits(d))
	ans += no * d

print(ans)