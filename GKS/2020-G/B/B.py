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

def ans(N, grid):

	score = defaultdict(int)

	for i in range(N):
		for j in range(N):
			score[j-i] += grid[i][j]

	return max(score.values())

T = int(input())
for t in range(T):
	N = int(input())
	grid = []
	for _ in range(N):
		row = list(map(int, input().split()))
		grid += [row]

	print("Case #" + str(t+1) + ": " + str(ans(N, grid)))
