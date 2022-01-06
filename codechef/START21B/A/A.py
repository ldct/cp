#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
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

def ans(p, q):
    if sum(p)%2 == sum(q)%2:
        return 0
    return 1

for _ in range(read_int()):
    N, x, y = read_int_list()
    target = ((N+1)//2, (N+1)//2)

    print(ans(target, (x, y)))