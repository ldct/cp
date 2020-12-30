#!/usr/bin/env pypy3

from sys import stdin, stdout

def input():
    return stdin.readline().strip()

def ans(H, K):
	low = H[0]
	high = H[0]

	# print(low, high)
	for h in H[1:]:
		low -= (K-1)
		high += (K-1)

		low = max(low, h)
		high = min(high, h+K-1)

		if not (low <= high):
			return 'NO'

		# print(low, high)

	if not low <= H[-1] <= high: return 'NO'

	return 'YES'

for _ in range(int(input())):
	[N, K] = list(map(int, input().split()))
	H = list(map(int, input().split()))

	print(ans(H, K))