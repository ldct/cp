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

def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))

### CODE HERE

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def count(strings, c):
    ret = 0
    for s in strings:
        if c in s:
            ret += 1
    return ret

def test(strings, K):
    ret = 0
    for c in ALPHABET:
        if count(strings, c) == K:
            ret += 1
    return ret

N, K = read_int_tuple()

strings = [input() for _ in range(N)]

ret = 0
for ss in subsets(strings):
    ret = max(ret, test(ss, K))

print(ret)