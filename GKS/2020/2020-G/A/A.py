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
	n0 = 0

	ret = 0

	for i in range(len(A)):
		if A[i:i+4] == "KICK":
			n0 += 1
		elif A[i:i+5] == "START":
			ret += n0

	return ret

T = int(input())
for t in range(T):
	S = input()
	print("Case #" + str(t+1) + ": " + str(ans(S)))
