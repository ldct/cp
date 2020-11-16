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
    g = []
    for _ in range(26):
        g += [[float("inf")]*26]

    for name in names:
        chars = list(set(name))
        for a in chars:
            for b in chars:
                i = label(a)
                j = label(b)
                g[i][j] = 1

    for i in range(26):
        g[i][i] = 0

    for k in range(26):
        for i in range(26):
            for j in range(26):
                g[i][j] = min(
                    g[i][j] ,
                    g[i][k]+ g[k][j]
                )

    ret = []
    for (i, j) in queries:
        n1 = names[i-1]
        n2 = names[j-1]

        r = float("inf")
        for a in set(n1):
            for b in set(n2):
                candidate = g[label(a)][label(b)]
                r = min(r, candidate)

        r += 2
        if r == float("inf"):
            r = -1

        ret += [r]

    return ' ' .join(map(str, ret))

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
