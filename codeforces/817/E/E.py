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

def ans(rectangles, queries):
    K = 0
    rectangles = [(2*x, 2*y) for (x, y) in rectangles]
    queries = [(2*x+1, 2*y+1, 2*X-1, 2*Y-1) for (x, y, X, Y) in queries]

    for x, y in rectangles:
        K = max(K, x, y)
    for x, y, X, Y in queries:
        K = max(K, x, y, X, Y)

    K += 1

    weights = []
    prefix = []

    for _ in range(K):
        weights += [[0]*K]
        prefix += [[0]*K]

    for x, y in rectangles:
        weights[x][y] += x*y

    for i in range(1, K):
        for j in range(1, K):
            prefix[i][j] = weights[i][j] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

    for x, y, X, Y in queries:
        r =  prefix[X][Y] - prefix[x][Y] - prefix[X][y] + prefix[x][y]
        print(r//4)


for _ in range(read_int()):
    N, Q = read_int_tuple()
    rectangles = [read_int_tuple() for _ in range(N)]
    queries = [read_int_tuple() for _ in range(Q)]
    ans(rectangles, queries)