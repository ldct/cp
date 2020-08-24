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

def ans(A):
	diffs = []
	for i in range(len(A)-1):
		diffs += [A[i+1] - A[i]]

	i = 0
	j = 1

	ret = float("-inf")

	while i < len(diffs):
		while j < len(diffs) and diffs[j] == diffs[i]:
			j += 1
		ret = max(ret, j-i)
		i += 1

	return ret+1

T = int(input())
for t in range(T):
	input()
	A = list(map(int, input().split()))
	print("Case #" + str(t+1) + ": " + str(ans(A)))
