#!/usr/bin/env pypy3

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

def ans(K, A):

    def gap(i):
        ret = 0
        for a in A:
            if (1 << i) & a == 0:
                ret += 1
        return ret

    for j in range(30, -1, -1):
        if gap(j) <= K:
            K -= gap(j)
            A = [a | (1 << j) for a in A]

    r = -1
    for a in A:
        r &= a

    return r

for _ in range(read_int()):
    N, K = read_int_tuple()
    A = read_int_list()
    print(ans(K, A))