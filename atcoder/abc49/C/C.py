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

def match(S, s):
    if len(s) > len(S): return False
    return S[-len(s):] == list(s)

def ans(S):
    S = list(S)
    while len(S):
        matched = False
        for word in ["dream", "dreamer", "erase", "eraser"]:
            if match(S, word):
                matched = True
                for _ in word: S.pop()
        if not matched:
            return "NO"

    return "YES"

S = input()
print(ans(S))