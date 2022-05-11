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

def ans(K, S):
    goodness = 0
    for i in range(0, len(S) // 2):
        if S[i] != S[len(S)-1-i]: goodness += 1
    return abs(goodness - K)

T = int(input())
for t in range(T):
    N, K = input().split()
    K = int(K)
    S = input()
    print("Case #" + str(t+1) + ": " + str(ans(K, S)))
