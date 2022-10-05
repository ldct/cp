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

def slow(S):
    S = list(S)
    def move(S):
        for i in range(1, len(S)-1):
            if S[i-1] != S[i+1]: return i

    num_moves = 0
    while True:
        i = move(S)
        if i is None: break
        num_moves += 1
        del S[i]

    return num_moves % 2

def fast(S):
    if S[0] == S[-1]:
        t = 3
    else:
        t = 2

    return (len(S) - t) % 2

if False:
    import random
    for _ in range(1000000):
        tc = ''.join(random.choice("abcdef") for _ in range(5))
        assert(slow(tc) == fast(tc))
else:
    S = list(input())
    print("Second" if 0 == fast(S) else "First")
