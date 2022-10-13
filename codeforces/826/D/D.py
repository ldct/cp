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

def ans(N, p):
    def solve(a, b):
        l = b-a
        if l == 1:
            return (0, [p[a]])
        mid = (a + b) // 2

        left = solve(a, mid)
        right = solve(mid, b)

        expected = sorted(p[a:b])
        if left[1] + right[1] == expected:
            return (left[0] + right[0], expected)
        elif right[1] + left[1] == expected:
            return (left[0] + right[0] + 1, expected)
        else:
            return (float("inf"), expected)

    ret = solve(0, len(p))[0]
    if ret == float("inf"):
        return -1
    return ret

for _ in range(read_int()):
    N = read_int()
    p = read_int_list()
    print(ans(N, p))