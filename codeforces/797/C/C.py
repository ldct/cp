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

def ans(S, F):

    free_time = 0

    tst = []

    for i in range(len(S)):
        s, f = S[i], F[i]

        tst += [max(free_time, s)]

        free_time = f

    durations = [F[i] - tst[i] for i in range(len(S))]
    return durations

for _ in range(read_int()):
    input()
    S = read_int_list()
    F = read_int_list()
    print(*ans(S, F))