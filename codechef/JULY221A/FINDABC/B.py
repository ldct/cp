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

def bin(x):
    return "{0:b}".format(x)

def populate(arr, gap, i):
    ret = arr[:]
    if gap == 3:
        return ret
    elif gap == 1:
        ret[0] ^= i
    elif gap == -1:
        ret[0] ^= i
        ret[1] ^= i
    elif gap == -3:
        ret[0] ^= i
        ret[1] ^= i
        ret[2] ^= i
    
    return ret

def ans(A, N):

    ret = [0, 0, 0]
    for i in range(len(A)-1, -1, -1):
        if bin(i).count('1') == 1:
            gap = A[i] - A[0]
            assert(gap % i == 0)
            gap //= i

            ret = populate(ret, gap, i)
            ret = sorted(ret)

    assert(max(ret) <= N)
    return ret

def seq(a, b, c, N):
    def f(i):
        return (a^i)+(b^i)+(c^i)
    return [f(i) for i in range(0, N+1)]

# print(seq(4, 5, 6, 6))
for _ in range(read_int()):
    N = read_int()
    print(*ans(read_int_list(), N))