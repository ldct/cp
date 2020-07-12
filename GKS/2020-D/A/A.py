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

def ans(V):
	max_so_far = float("-inf")
	ret = 0
	for i, v in enumerate(V):
		if v > max_so_far:
			max_so_far = v
			if i == len(V)-1 or v > V[i+1]:
				ret += 1
	return ret

T = int(input())
for t in range(T):
	input()
	V = input().split(' ')
	V = list(map(int, V))
	print("Case #" + str(t+1) + ": " + str(ans(V)))
