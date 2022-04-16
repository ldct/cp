#!/usr/bin/env pypy3

import io, os, sys
from sys import stdin, stdout

# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd, sqrt
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

### CODE HERE

@lru_cache(None)
def ans(x, k):
    if k == 0: return x

    divisors = get_divisors(x)

    return sum([ans(d, k-1) for d in divisors]) / len(divisors)

def get_divisors(n):
    ret = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            ret += [i]
            if i*i != n:
                ret += [n//i]
    return ret

def num_divisors(x):
    return len(get_divisors(x))

print(ans(866421317361600, 1))

# print(num_divisors(866421317361600))
# 27k divisors
# 16M edges