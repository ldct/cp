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

def ans(S):
    S = list(map(int, S))
    S = ['x'] + S
    if S[1] == 1: return 'No'
    columns = []
    if S[7] > 0: columns += [0]
    if S[4] > 0: columns += [1]
    if S[8] + S[2] > 0: columns += [2]
    if S[5] + S[1] > 0: columns += [3]
    if S[9] + S[3] > 0: columns += [4]
    if S[6] > 0: columns += [5]
    if S[10] > 0: columns += [6]

    for i in range(len(columns) - 1):
        if columns[i] + 1 != columns[i+1]:
            return 'Yes'
    return 'No'

print(ans(input()))