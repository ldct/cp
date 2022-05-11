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

def cdiv(x, y):
    return x // y if x % y == 0 else x // y + 1

def ok(offset, a_inc):
    a_opp = []
    for i in range(len(a_inc)):
        a_opp += [a_inc[(i + offset) % len(S)]]
    for i in range(len(a_inc)):
        if a_inc[i][0] == a_opp[i][0]: return False
    return a_opp

def ans(S):
    S = [(s, i) for i,s in enumerate(S)]
    a_inc = sorted(S)
    for offset in range(len(S) // 2 - 1, len(S) // 2 + 1):
        a_opp = ok(offset, a_inc)
        if a_opp:
            d = dict()
            for i in range(len(S)):
                d[a_inc[i]] = a_opp[i][0]
            ret = []
            for i in range(len(S)):
                ret += d[S[i]]
            return ''.join(ret)
    return "IMPOSSIBLE"


T = int(input())
for t in range(T):
    S = input()
    print("Case #" + str(t+1) + ": " + str(ans(S)))
