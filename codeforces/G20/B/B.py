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

def bad(s):

    if ''.join(sorted(s)) != s: return True
    if 'A' not in s: return True
    if 'B' not in s: return True
    if s.count('A') < s.count('B'): return True
    return False

def ans(S):
    if S[-1] != "B": return "NO"
    cnt = 0
    for c in S:
        if c == "B":
            cnt -= 1
        else:
            cnt += 1
        if cnt < 0:
            return "NO"

    return "YES"

for _ in range(read_int()):
    print(ans(input()))