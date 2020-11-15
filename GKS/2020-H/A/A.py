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

def ans(N, K, S):
    return K-1 + min(
        N+1,
        K-S + (N-S) + 1
    )

T = int(input())
for t in range(T):
    N, K, S = input().split()
    N = int(N)
    K = int(K)
    S = int(S)
    print("Case #" + str(t+1) + ": " + str(ans(N, K, S)))
