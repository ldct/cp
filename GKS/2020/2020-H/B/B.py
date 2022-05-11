#!/usr/bin/env python3

from __future__ import division, print_function

import itertools
import sys

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

def num_boring_slow(N):
    ret = 0
    for i in range(1, N):
        if is_boring(i):
            ret += 1
    return ret+1 # include 0

def is_boring(N):
    S = str(N)
    for i in range(len(S)):
        if i % 2 == (int(S[i]) % 2): return False
    return True

def num_boring(N):
    if N < 20: return num_boring_slow(N)

    ret = 0
    S = str(N)

    # everything shorter
    for s in range(len(S)):
        ret += 5**s
    # print("shorter", N, ret)

    for i in range(len(S)):
        d = int(S[i])

        for j in range(d):
            l = (len(S)-i-1)
            if j % 2 == (1 - (i % 2)):
                # print(str(j) + l*"?", 5**l)
                ret += 5**l

        if d % 2 == (1 - (i % 2)):
            continue
        else:
            break
    return ret

def ans(a, b):
    return num_boring(b+1) - num_boring(a)

T = int(input())
for t in range(T):
    A, B = input().split()
    A = int(A)
    B = int(B)
    print("Case #" + str(t+1) + ": " + str(ans(A, B)))
