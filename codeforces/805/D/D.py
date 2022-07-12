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

def ans(s, p):

    def weight(c):
        return (ord(c) - ord('a') + 1)

    ss = sorted(s)[::-1]
    score = 0
    for c in s:
        score += weight(c)
    if score <= p:
        return s

    to_remove = []
    i = 0
    while score > p:
        score -= weight(ss[i])
        to_remove += [ss[i]]
        i += 1

    to_remove = Counter(to_remove)

    ret = []
    for c in s:
        if to_remove[c] > 0:
            to_remove[c] -= 1
        else:
            ret += [c]

    return ''.join(ret)

for _ in range(read_int()):
    print(ans(input(), read_int()))