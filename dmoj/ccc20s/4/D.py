#!/usr/bin/env pypy3

import io, os
from sys import stdin, stdout

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

def ans(S):
    freq = dict()
    for c in "AB":
        freq[c] = S.count(c)

    def score(cs, S, start):
        N = len(S)
        ret = 0
        for i in range(N):
            j = (i + start) % N
            if cs[i] != S[j]:
                ret += 1
        return ret

    ret = float("inf")

    for pp in permutations("B"):
        p = ("A",) + pp
        cs = ''.join(c*freq[c] for c in p)
        for start in range(len(S)):
            ret = min(ret, score(cs, S, start))

    return ((ret + 1) // 2)

print(ans(input()))