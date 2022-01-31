#!/usr/bin/env pypy3

import io, os
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
    if S == S[::-1]: return "Yes"

    new_S = deque(S)

    n = 0
    while len(new_S) and new_S[0] == 'a':
        n += 1
        new_S.popleft()

    m = 0
    while len(new_S) and new_S[-1] == 'a':
        m += 1
        new_S.pop()

    S = ''.join(new_S)
    if S != S[::-1]:
        return "No"

    if n <= m:
        return "Yes"
    return "No"

S = input()
print(ans(S))
