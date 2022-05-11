#!/usr/bin/env python2

from __future__ import division, print_function

import itertools
import sys

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

from collections import defaultdict

def ans_slow(MODULUS, X):

	def ans2(target):
		def mod(x):
			x %= MODULUS
			x += MODULUS
			x %= MODULUS
			return min(x, MODULUS - x)

		return sum(mod(x - target) for x in X)

	return min(ans2(t) for t in set(X))

def ans(MODULUS, X):

	N = len(X)

	if N % 2 == 0:
		below_median = N//2
		above_median = N//2
	else:
		below_median = N//2 + 1
		above_median = N//2

	i = 0
	j = len(X)-1

	X = sorted(X)
	X += [x + MODULUS for x in X]

	# start value
	v = 0
	for k in range(i, j+1):
		v += abs(X[k] - X[(j - i) // 2])

	ret = v

	while True:
		i += 1
		j += 1

		if j == len(X): break

		median_idx = (i + j) // 2

		new_median = X[median_idx]
		old_median = X[median_idx - 1]
		gap = new_median - old_median

		v += (below_median * gap)
		v -= (above_median * gap)

		v -= (new_median - X[i-1]) # old tail removed
		v += X[j] - new_median # new head added

		ret = min(v, ret)

	return ret

T = int(input())
for t in range(T):
	W, N = input().split()
	W = int(W)
	N = int(N)
	X = list(map(int, input().split()))

	print("Case #" + str(t+1) + ": " + str(ans(N, X)))
