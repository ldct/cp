#!/usr/bin/env pypy3

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

def ans(D, C, M, S):
    i = 0
    for s in S:
        if s == 'D':
            D -= 1
            C += M
        elif s == 'C':
            C -= 1
        else:
            assert(False)

        if D < 0 or C < 0: break

        i += 1

    if 'D' in S[i:]:
        return 'NO'
    return 'YES'
    # return S[i:]

T = int(input())
for t in range(T):
    N, D, C, M = read_int_list()
    S = input()
    print("Case #" + str(t+1) + ": " + str(ans(D, C, M, S)))
