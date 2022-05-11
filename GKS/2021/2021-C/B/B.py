#!/usr/bin/env pypy

from __future__ import division, print_function

import itertools
import sys

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

MODULUS = 10**9+7

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import product

def ans(G):

    N = G*2

    ret = set()

    def solve(p, q):
        q -= 1
        b2 = p + q
        if b2 % 2 == 1: return None
        b = b2 // 2
        a = p - b
        assert(b - a == q)
        return (a,b)

    i = 1
    while i*i <= N:
        if N % i != 0:
            i += 1
            continue

        for r in [solve(i, N//i), solve(N//i, i)]:
            if r is not None:
                a, b = r
                if a > 0 and b > 0:
                    ret.add(r)
        i += 1

    return len(ret)




T = int(input())
for t in range(T):
    G = read_int()
    print("Case #" + str(t+1) + ": " + str(ans(G)))
