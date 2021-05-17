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

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations

def weight(L):
    L = list(L)
    ret = 0
    for i in range(len(L)-1):
        Lj = min(L[i:])
        j = L.index(Lj)
        L[i:j+1] = L[i:j+1][::-1]
        ret += j-i+1
    return ret

def ans(N, C):
    if not N-1 <= C <= (N*(N+1))//2 - 1:
        return "IMPOSSIBLE"
    if N == 1:
        assert(C == 0)
        return [1]
    i = C - (N-1)
    if i >= N: i = N-1
    ret = ans(N-1, C-(i+1))
    ret = [1] + [x + 1 for x in ret]

    ret[0:i+1] = ret[0:i+1][::-1]
    return ret

if False:
    for N in range(99, 100):
        for C in range(N-1, (N*(N+1))//2):
            assert(C == weight(ans(N, C)))
    import sys
    sys.exit(0)


T = int(input())
for t in range(T):
    N, C = read_int_tuple()
    r = ans(N, C)
    if r is not "IMPOSSIBLE":
        r = ' '.join(map(str, r))
    print("Case #" + str(t+1) + ": " + r)
