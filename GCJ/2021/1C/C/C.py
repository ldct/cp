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

def BNOT(x):
    x = "{0:b}".format(x)
    x = map(int, x)
    x = [1-d for d in x]
    x = ''.join(map(str, x))
    return int(x, 2)

def dist(S, E):

    if S == E: return 0

    curr_level = set([S])
    visited = set([S])

    ret = 0
    while(True):
        ret += 1
        next_level = set([])
        for s in curr_level:
            if 2*s not in visited: next_level.add(2*s)
            if BNOT(s) not in visited: next_level.add(BNOT(s))

        next_level = [n for n in next_level if n < 2**16]
        if len(next_level) == 0: return -1
        if E in next_level: return ret

        for n in next_level: visited.add(n)
        curr_level = next_level

def ans(S, E):
    S = int(S, 2)
    E = int(E, 2)

    return dist(S, E)

if True:
    md = 0
    for i in range(2**4):
        for j in range(i+1, 2**4):
            if dist(i, j) == 7:
                print(i, j)
            md = max(md, dist(i, j))
    print(md)
else:
    T = int(input())
    for t in range(T):
        S, E = input().split()
        print("Case #" + str(t+1) + ": " + str(ans(S, E)))
