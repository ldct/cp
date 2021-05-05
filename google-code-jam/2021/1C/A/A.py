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

def cdiv(x, y):
    return x // y if x % y == 0 else x // y + 1

def ans(K, L):
    sL = set(L)
    L = sorted(sL)

    closed = []
    hopen = []

    for i in range(len(L)-1):
        a, b = L[i], L[i+1]
        if a+1 <= b-1:
            closed += [(b-(a+1))]

    if L[0] > 1:
        hopen += [L[0]-1]

    if L[-1] < K:
        hopen += [K - L[-1]]

    hopen = sorted(hopen)[::-1]
    closed = sorted(closed)[::-1]

    candidates = []

    closed += [0,0,0]

    for NUM_HOPEN in [0,1,2]:
        for NUM_CLOSED in [0,1,2]:
            if NUM_HOPEN + NUM_CLOSED > 2: continue
            if NUM_HOPEN > len(hopen): continue

            ret = 0

            if NUM_HOPEN == 1:
                ret += hopen[0]
            if NUM_HOPEN == 2:
                ret += hopen[0]
                ret += hopen[1]

            if NUM_CLOSED == 1:
                ret += cdiv(closed[0], 2)
            elif NUM_CLOSED == 2:
                ret += max(
                    cdiv(closed[0], 2) + cdiv(closed[1], 2),
                    closed[0]
                )


            candidates += [ret]
            # print(NUM_HOPEN, NUM_CLOSED, ret)

    # print("hopen=", hopen, "closed=", closed)
    return max(candidates)

def dist(x, A):
    return min(abs(x-a) for a in A)

def score(K, L, mine):
    ret = 0
    for i in range(1, K+1):
        if dist(i, L) > dist(i, mine):
            ret += 1
    return ret

def ans_slow(K, L):
    ret = 0
    for i in range(1, K+1):
        for j in range(1, K+1):
            ret = max(ret, score(K, L, [i,j]))
    return ret

if False:
    import random
    for _ in range(10000):
        K = 5
        N = 5
        tc = list(set([random.randint(1, K) for _ in range(N)]))
        if ans(K, tc) != ans_slow(K, tc):
            print(tc)
            assert(False)

else:
    T = int(input())
    for t in range(T):
        _, K = read_int_tuple()
        L = read_int_list()
        print("Case #" + str(t+1) + ": " + str(ans(K, L)/K))
