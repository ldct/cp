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
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

### CODE HERE

def cost_p(p):
    ret = 0
    for i in range(len(p)-1):
        ret = max(ret, p[i]^p[i+1])
    return ret

def cost(n):
    return min(cost_p(p) for p in permutations(range(n)))

def gen_p(n):
    b = (n-1).bit_length()-1
    return list(range(1 << b))[::-1] + list(range(1 << b, n))

for _ in range(read_int()):
    print(*gen_p(read_int()))