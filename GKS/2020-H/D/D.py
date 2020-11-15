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

alphabet = "abcdefghijklmnopqrstuvwxyz".upper()

def label(c): return ord(c) - ord('A')

def ans(names, queries):

    V = len(names)

    g = []
    for _ in range(V):
        g += [[float("inf")]*V]
    for i in range(V):
        g[i][i] = 0

    for i in range(V):
        for j in range(i+1, V):
            if len(set(names[i]) & set(names[j])) > 0:
                g[i][j] = 1
                g[j][i] = 1

    # Floyd-Warshall

    for k in range(V):
        for i in range(V):
            for j in range(V):
                g[i][j] = min(
                    g[i][j] ,
                    g[i][k]+ g[k][j]
                )

    ret = []
    for (i, j) in queries:
        x = g[i-1][j-1]
        if x == float("inf"):
            ret += [-1]
        else:
            ret += [x+1]

    return ' '.join(map(str, ret))

T = int(input())
for t in range(T):
    N, Q = input().split()
    N = int(N)
    Q = int(Q)
    names = input().split()
    queries = []
    for _ in range(Q):
        queries += [tuple(map(int, input().split()))]
    print("Case #" + str(t+1) + ": " + str(ans(names, queries)))
