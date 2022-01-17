#!/usr/bin/env pypy3

import io, os
from sys import stdin, stdout

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

### CODE HERE

def vote(i, words):
    ret = 0
    for word in words:
        if (1 << i) & word > 0:
            ret += 1
    return ret

def ans(words):
    n = len(words)
    ret = 0
    for i in range(31, -1, -1):
        if vote(i, words) > (n // 2):
            ret |= (1 << i)
    return ret

for _ in range(read_int()):
    N, L = read_int_tuple()
    words = read_int_list()
    print(ans(words))