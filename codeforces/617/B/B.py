#!/usr/bin/env python3

input()
pieces = list(map(int, input().split()))
N = len(pieces)

oneIndexes = [i for i, e in enumerate(pieces) if e == 1]

if len(oneIndexes) == 0:
	print(0)
else:

	ans = 1
	for i in range(len(oneIndexes) - 1):
		ans *= (oneIndexes[i+1] - oneIndexes[i])

	print(ans)