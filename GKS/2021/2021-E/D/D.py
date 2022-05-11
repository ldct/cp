#!/usr/bin/env pypy

from __future__ import division, print_function

import itertools, sys, math

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
from fractions import Fraction

def score_perm(p):
    ret = 0
    last = -1
    for c in p:
        if c > last:
            last = c
            ret += 1
    return ret

def score_N(N):
    ret = []
    for p in itertools.permutations(list(range(1, N+1))):
        ret += [Fraction(score_perm(p), 1)]
    return sum(ret) / len(ret)

def ans_fast(N):
    ret = 0
    for i in range(1, N+1):
        ret += 1/i
    return ret

def ans_faster(n):
    if n < 10**5: return ans_fast(n)
    return math.log(n, math.e) + 0.5772156649 + 1/(2*n) - 1/(2*n*n) + 1/(120*n**4)

if False:
    for i in range(10**6, 10**6+10):
        print(ans_fast(i), ans_faster(i))
else:
    T = int(input())
    for t in range(T):
        N = int(input())
        print("Case #" + str(t+1) + ": " + str(ans_faster(N)))
