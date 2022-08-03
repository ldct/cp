#!/usr/bin/env python3

import io, os, sys
from sys import stdin, stdout

# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

### CODE HERE

def join(a, b, x, l):
    if a == b:
        assert(l == 0)
        return x, []
    if l == 0:
        assert(False)
        return None

    if l == 1:
        return x, [(a, b)]

    line = [a]

    for _ in range(l - 1):
        line += [x]
        x += 1
    
    line += [b]


    ret = []
    for i in range(len(line)-1):
        ret += [(line[i], line[i+1])]
    return x, ret

def ans(n, d12, d23, d31):
    TWO_TOTAL = d12 + d23 + d31
    if (TWO_TOTAL % 2 != 0):
        print("NO")
        return
    TOTAL = TWO_TOTAL // 2

    if TOTAL > n:
        print("NO")
        return

    a = TOTAL - d23
    b = TOTAL - d31
    c = TOTAL - d12

    if min(a, b, c) < 0:
        print("NO")
        return

    if len(set([x for x in [a, b, c] if x == 0])) > 1:
        assert(False)
        print("NOWAYDUDE")
        return

    CENTRAL_NODE = 4
    if a == 0:
        CENTRAL_NODE = 1
    if b == 0:
        CENTRAL_NODE = 2
    if c == 0:
        CENTRAL_NODE = 3

    # print(CENTRAL_NODE, a, b, c)

    x = max(3, CENTRAL_NODE) + 1

    x, e1 = join(1, CENTRAL_NODE, x, a)
    x, e2 = join(2, CENTRAL_NODE, x, b)
    x, e3 = join(3, CENTRAL_NODE, x, c)

    edges = e1 + e2 + e3

    remaining_edges = n-1 - len(edges)

    if remaining_edges > 0:
        x, e4 = join(1, n, x, remaining_edges)
        edges += e4

    nodes = []
    for e in edges:
        nodes += e
    if not (max(nodes) <= n):
        print("NO")
        return
        # print('hihi', n, d12, d23, d31)
        # assert(False)

    print("YES")
    assert(len(edges) == n-1)

    LINES = []

    for i, j in edges:
        LINES += [f"{i} {j}"]
    print("\n".join(LINES))
    
if False:
    for n in range(3, 10):
        for d12 in range(1, n):
            for d23 in range(1, n):
                for d31 in range(1, n):
                    print(n, d12, d23, d31)
                    ans(n, d12, d23, d31)
                    print()
else:
    for _ in range(read_int()):
        ans(*read_int_list())