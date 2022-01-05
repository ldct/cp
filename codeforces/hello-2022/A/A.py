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

def cdiv(x, y):
    return x // y if x % y == 0 else x // y + 1

def ans(N, K):
    if K > cdiv(N, 2):
        print(-1)
        return
    ret = []
    for _ in range(N):
        ret += [list("."*N)]
    for i in range(K):
        ret[2*i][2*i] = 'R'
    for row in ret:
        print(''.join(row))

for _ in range(read_int()):
    N, K = read_int_tuple()
    ans(N, K)