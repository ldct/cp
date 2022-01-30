#!/usr/bin/env pypy3

import io, os
from sys import stdin, stdout

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

### CODE HERE

def lcm3(a, b, c):
    return lcm(lcm(a, b), c)

def lcm(x, y):
    return x*y // gcd(x, y)

def ans_gcd(N):
    ret = 0
    for a in range(1, N+1):
        for b in range(1, N+1):
            for c in range(1, N+1):
                if gcd(a, b) == 1 and gcd(b, c) == 1 and gcd(a, c) == 1:
                    ret = max(ret, a*b*c)
    return ret

def ans(N):
    if N == 1: return 1
    if N == 2: return 2
    if N == 3: return 6

    if N % 2 == 1:
        return N*(N-1)*(N-2)
    if N % 3 == 0:
        return (N-1)*(N-2)*(N-3)
    return N*(N-1)*(N-3)


print(ans(read_int()))